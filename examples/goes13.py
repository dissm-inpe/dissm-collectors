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

from flask import Flask
from bdc_collectors import CollectorExtension

app = Flask(__name__)
ext = CollectorExtension(app)

# Get specific GOES collector
provider = ext.get_provider('GOES')()

# Search scenes from 2016/04/08 until 2016/04/09, GOES-13/Band 04
scenes = provider.search(
    query='GOES-13', band='04',
    start_date='20160408', end_date='20160409'
)

# Download first scene
provider.download(scenes[0].scene_id, output_dir='./')
