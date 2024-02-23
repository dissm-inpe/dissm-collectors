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

from datetime import timedelta

# Hour values (i.e. ['00', '01, ..., '12', .., '20, '23'])
HOURS = [str(i).zfill(2) for i in range(0, 24)]

def generate_list_of_days(start, end):
    '''This function returns all-days between given two dates.'''
    delta = end - start
    return [start + timedelta(i) for i in range(delta.days + 1)]