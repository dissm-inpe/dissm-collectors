#
# This file is part of DISSM Collectors.
# Copyright (C) 2023 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#

"""Driver for Access GOES Data on DISSM Server."""

import os
import re
from datetime import date, datetime
from itertools import chain
from typing import List

import requests
from bdc_collectors.base import BaseProvider, SceneResult, SceneResults
from bdc_collectors.exceptions import DownloadError

from dissm_collectors.goes import repository
from dissm_collectors.utils import generate_list_of_days, HOURS

class GOES(BaseProvider):

    def __init__(self, **kwargs):
        """Build a data provider GOES instance."""
        self.kwargs = kwargs
        self.progress = kwargs.get('progress')

    def search(self, query, *args, **kwargs) -> SceneResults:
        """Search for data set in GOES Provider.

        Args:
            query - Geostationary Satellite reference name.
            *args - Optional parameters order for the given provider.
            **kwargs - Keywords for given provider: start_date, end_date and band.
        """
        satellite = query
        if satellite not in repository.SATELLITES:
            raise RuntimeError('Invalid geostationary satellite {}. Options: {}'.format(
                satellite, repository.SATELLITES))

        if 'band' not in kwargs:
            raise RuntimeError('Missing desired band')

        band = kwargs.get('band')
        if band not in repository.BANDS[satellite]:
            raise RuntimeError('Invalid band value. Options: {}'.format(band, repository.BANDS[satellite]))

        start_date = date.today()
        if kwargs.get('start_date'):
            start_date = datetime.strptime(kwargs['start_date'], '%Y%m%d')

        end_date = start_date
        if 'end_date' in kwargs:
            end_date = datetime.strptime(kwargs['end_date'], '%Y%m%d')

        if end_date < start_date:
            raise RuntimeError('end_date should be greater than start_date')

        # Searching for remote files
        files = []
        page = None
        current_month = None
        for day in generate_list_of_days(start_date, end_date):
            if not current_month or current_month != day.strftime('%m'):
                page = self._getMonthlyList(satellite, band, day)
                current_month = day.strftime('%m')
            if not page:
                continue
            day_files = re.findall('href="(.*.nc|.*.gz)"', page)
            for hour in HOURS:
                regex = '.*_{}{}.*'.format(day.strftime('%Y%m%d'), hour)
                r = re.compile(regex)
                files.append(list(filter(r.match, day_files)))
            
        # Flat list of files
        files = list(chain.from_iterable(files))

        scenes = []
        for file in files:
            # Build URL with file name
            url = '{}/{}/{}/{}/{}'.format(repository.BASE_URL, 
                repository.REMOTE_BASE_PATHS[satellite][band],
                day.strftime('%Y'), day.strftime('%m'), file)
            # Build scene info
            scenes.append(SceneResult(
                scene_id=url, 
                cloud_cover=None,
                link=url))

        return scenes

    def download(self, scene_id: str, *args, **kwargs) -> str:
        """Download a single file from remote server.

        Raises:
            DownloadError when any exception occurs.
        """
        try:
            # Prepare output location
            output_dir = kwargs.get('output_dir', '.')
            os.makedirs(output_dir, exist_ok=True)
            local_file = os.path.join(output_dir, os.path.basename(scene_id))
            # Download file!
            r = requests.get(scene_id, allow_redirects=True)
            open(local_file, 'wb').write(r.content)
            return local_file
        except Exception as e:
            raise DownloadError(str(e))

    def _getMonthlyList(self, satellite, band, day):
        try:
            url = '{}/{}/{}/{}/'.format(repository.BASE_URL, 
                repository.REMOTE_BASE_PATHS[satellite][band],
                day.strftime('%Y'), day.strftime('%m'))
            resp = requests.get(url)
            resp.raise_for_status()
            return resp.text
        except requests.exceptions.HTTPError as error:
            print(error)
            return None
