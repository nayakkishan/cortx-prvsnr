#!/usr/bin/env python
#
# Copyright (c) 2020 Seagate Technology LLC and/or its Affiliates
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.
#
#
import curses

color_codes = {
    1 : [curses.COLOR_BLACK, curses.COLOR_WHITE],
    2 : [curses.COLOR_GREEN,curses.COLOR_BLACK],
    3 : [curses.COLOR_RED,curses.COLOR_BLACK]
}

error_color = 3
default_window_color = 2
menu_color = 2

tittle = "Lvye Rack II"
menu = ['Set Hostname', 'Set Managment VIP', 'Setup Netowrk', 'Setup Storage' , 'EXIT']
short_menu = ['hostname', 'management vip', 'network', 'storage']
default_textbox = ['seagate.com', '10.10.10.10', 'eno1', 'test']


