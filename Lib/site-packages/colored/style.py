#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
style.py is a part of colored.

Copyright 2014-2016 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
All rights reserved.

Colored is very simple Python library for color and formatting in terminal.

https://github.com/dslackw/colored

colored is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""


class style(object):

    ESC = "\x1b["
    END = "m"

    BOLD = ESC + "1" + END
    DIM = ESC + "2" + END
    UNDERLINED = ESC + "4" + END
    BLINK = ESC + "5" + END
    REVERSE = ESC + "7" + END
    HIDDEN = ESC + "8" + END
    RESET = ESC + "0" + END
    RES_BOLD = ESC + "21" + END
    RES_DIM = ESC + "22" + END
    RES_UNDERLINED = ESC + "24" + END
    RES_BLINK = ESC + "25" + END
    RES_REVERSE = ESC + "27" + END
    RES_HIDDEN = ESC + "28" + END
