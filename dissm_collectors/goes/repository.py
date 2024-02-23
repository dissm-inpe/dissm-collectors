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

"""Informations about DISSM GOES repository."""

BASE_URL = 'http://ftp.cptec.inpe.br/goes'

SATELLITES = ['GOES-13', 'GOES-16']

BANDS = {
    'GOES-13': [str(i).zfill(2) for i in range(1, 6)], # ['01', '02', ..., '05']
    'GOES-16': [str(i).zfill(2) for i in range(1, 17)] # ['01', '02', ..., '16']
}
BANDS['GOES-13'].append('01_4km') # append 4km spatial resolution version of band 01 GOES-13

REMOTE_BASE_PATHS = {
    'GOES-13': {
        '01': 'goes13/retangular_1km/ch1_bin',
        '02': 'goes13/retangular_4km/ch2_bin',
        '03': 'goes13/retangular_4km/ch3_bin',
        '04': 'goes13/retangular_4km/ch4_bin',
        '05': 'goes13/retangular_4km/ch5_bin',
        '01_4km': 'goes13/retangular_4km/ch1_bin',
    },
    'GOES-16': {
        '01': 'goes16/retangular/ch01',
        '02': 'goes16/retangular/ch02',
        '03': 'goes16/retangular/ch03',
        '04': 'goes16/retangular/ch04',
        '05': 'goes16/retangular/ch05',
        '06': 'goes16/retangular/ch06',
        '07': 'goes16/retangular/ch07',
        '08': 'goes16/retangular/ch08',
        '09': 'goes16/retangular/ch09',
        '10': 'goes16/retangular/ch10',
        '11': 'goes16/retangular/ch11',
        '12': 'goes16/retangular/ch12',
        '13': 'goes16/retangular/ch13',
        '14': 'goes16/retangular/ch14',
        '15': 'goes16/retangular/ch15',
        '16': 'goes16/retangular/ch16',
    }
}
