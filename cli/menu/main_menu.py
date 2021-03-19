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
import config
from curses import textpad
from window import Window
from color_code import ColorCode
from is_primary import PrimaryWindow
from check import Check

class MainMenu(Window):
    _menu = None
    _menu_dict = None
    _parent = []

    def __init__(self, window):
        super().__init__(window)
        #self.set_menu(config.menu)
        #self._menu_dict = config.menu
        self._menu = config.menus

    def get_menu(self):
        return self._menu

    def set_menu(self, menu):
        tmp_menu = []
        for value in menu.values():
            if isinstance(value, dict):
                value = next(iter(value))
            tmp_menu.append(value)
        tmp_menu.append("Exit")
        self._menu = tmp_menu 

    def set_checks(self, name, value):
        self._checks[name] = value

    def get_checks(self):
        return Check().loads()

    def create_window(self, **kwargs):
        color_code = kwargs['color_code']
        selected_rows = kwargs['menu_code']
        self._window.border()
        col_code_attr = ColorCode().get_color_pair(color_code)
        checks = self.get_checks()
        for idx, row in enumerate(self._menu):
            x = self.get_max_width() // 2 - len(row)//2
            y = self.get_max_height()  // 2 - len(self._menu)//2 + idx
            if idx == selected_rows:
                self.on_attr(col_code_attr)
                self._window.addstr(y,x-3 ,">> ")
                self._window.addstr(y,x ,row)
                self.off_attr(col_code_attr)
            else:
                self._window.addstr(y,x ,row)
            #if row != "EXIT" and checks[row]:
            ##    self.on_attr(col_code_attr)
            #    self._window.addstr(y,x + len(row)+2 ,u"\u2713")
            #    self.off_attr(col_code_attr)
        self._window.refresh()

    def process_input(self, color_code):
        current_row = 0
        while 1:
            key = self._window.getch()
            import os
            os.system(f"echo 'key {key}' >> test.log")
            if key == curses.KEY_UP and current_row > 0:
                current_row = current_row - 1
                os.system(f"echo 'up {current_row}' > test.log")
            elif key == curses.KEY_DOWN and  current_row < len(self.get_menu())-1:
                current_row = current_row + 1
                os.system(f"echo 'down {current_row}' > test.log")
            elif key == 113:
                os.system(f"echo 'q {current_row}' > test.log")
                return
            elif key == curses.KEY_ENTER or key in (10, 13):
                if current_row == len(self.get_menu()) - 1:
                    return
                elif current_row >= 0 and current_row < len(self.get_menu()):
                    value = self._menu_dict[current_row+1]
                    if isinstance(value, dict):
                        #self._menu_dict = value
                        import os
                        os.system(f"echo {value} >> test.log") 
                        key = next(iter(value))      
                        self._menu_dict = value[key]
                        self.set_menu(self._menu_dict)
                    else:
                        wd = PrimaryWindow(self._window)
                        wd.create_default_window(config.default_window_color)
                        wd.create_window(color_code=color_code,selected="Yes")
                        wd.process_input(config.menu_color, current_row)

            self._window.clear()
            #self.create_default_window(config.default_window_color)
            import os
            os.system(f"echo {current_row} >> row.log")
            self.create_window(color_code=color_code,menu_code=current_row)
            self._window.refresh()

