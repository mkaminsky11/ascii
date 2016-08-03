#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
back.py is a part of colored.

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


class back(object):

    ESC = "\x1b[48;5;"
    END = "m"

    BLACK = ESC + "0" + END
    RED = ESC + "1" + END
    GREEN = ESC + "2" + END
    YELLOW = ESC + "3" + END
    BLUE = ESC + "4" + END
    MAGENTA = ESC + "5" + END
    CYAN = ESC + "6" + END
    LIGHT_GRAY = ESC + "7" + END
    DARK_GRAY = ESC + "8" + END
    LIGHT_RED = ESC + "9" + END
    LIGHT_GREEN = ESC + "10" + END
    LIGHT_YELLOW = ESC + "11" + END
    LIGHT_BLUE = ESC + "12" + END
    LIGHT_MAGENTA = ESC + "13" + END
    LIGHT_CYAN = ESC + "14" + END
    WHITE = ESC + "15" + END
    GREY_0 = ESC + "16" + END
    NAVY_BLUE = ESC + "17" + END
    DARK_BLUE = ESC + "18" + END
    BLUE_3A = ESC + "19" + END
    BLUE_3B = ESC + "20" + END
    BLUE_1 = ESC + "21" + END
    DARK_GREEN = ESC + "22" + END
    DEEP_SKY_BLUE_4A = ESC + "23" + END
    DEEP_SKY_BLUE_4B = ESC + "24" + END
    DEEP_SKY_BLUE_4C = ESC + "25" + END
    DODGER_BLUE_3 = ESC + "26" + END
    DODGER_BLUE_2 = ESC + "27" + END
    GREEN_4 = ESC + "28" + END
    SPRING_GREEN_4 = ESC + "29" + END
    TURQUOISE_4 = ESC + "30" + END
    DEEP_SKY_BLUE_3A = ESC + "31" + END
    DEEP_SKY_BLUE_3B = ESC + "32" + END
    DODGER_BLUE_1 = ESC + "33" + END
    GREEN_3A = ESC + "34" + END
    SPRING_GREEN_3A = ESC + "35" + END
    DARK_CYAN = ESC + "36" + END
    LIGHT_SEA_GREEN = ESC + "37" + END
    DEEP_SKY_BLUE_2 = ESC + "38" + END
    DEEP_SKY_BLUE_1 = ESC + "39" + END
    GREEN_3B = ESC + "40" + END
    SPRING_GREEN_3B = ESC + "41" + END
    SPRING_GREEN_2A = ESC + "42" + END
    CYAN_3 = ESC + "43" + END
    DARK_TURQUOISE = ESC + "44" + END
    TURQUOISE_2 = ESC + "45" + END
    GREEN_1 = ESC + "46" + END
    SPRING_GREEN_2B = ESC + "47" + END
    SPRING_GREEN_1 = ESC + "48" + END
    MEDIUM_SPRING_GREEN = ESC + "49" + END
    CYAN_2 = ESC + "50" + END
    CYAN_1 = ESC + "51" + END
    DARK_RED_1 = ESC + "52" + END
    DEEP_PINK_4A = ESC + "53" + END
    PURPLE_4A = ESC + "54" + END
    PURPLE_4B = ESC + "55" + END
    PURPLE_3 = ESC + "56" + END
    BLUE_VIOLET = ESC + "57" + END
    ORANGE_4A = ESC + "58" + END
    GREY_37 = ESC + "59" + END
    MEDIUM_PURPLE_4 = ESC + "60" + END
    SLATE_BLUE_3A = ESC + "61" + END
    SLATE_BLUE_3B = ESC + "62" + END
    ROYAL_BLUE_1 = ESC + "63" + END
    CHARTREUSE_4 = ESC + "64" + END
    DARK_SEA_GREEN_4A = ESC + "65" + END
    PALE_TURQUOISE_4 = ESC + "66" + END
    STEEL_BLUE = ESC + "67" + END
    STEEL_BLUE_3 = ESC + "68" + END
    CORNFLOWER_BLUE = ESC + "69" + END
    CHARTREUSE_3A = ESC + "70" + END
    DARK_SEA_GREEN_4B = ESC + "71" + END
    CADET_BLUE_2 = ESC + "72" + END
    CADET_BLUE_1 = ESC + "73" + END
    SKY_BLUE_3 = ESC + "74" + END
    STEEL_BLUE_1A = ESC + "75" + END
    CHARTREUSE_3B = ESC + "76" + END
    PALE_GREEN_3A = ESC + "77" + END
    SEA_GREEN_3 = ESC + "78" + END
    AQUAMARINE_3 = ESC + "79" + END
    MEDIUM_TURQUOISE = ESC + "80" + END
    STEEL_BLUE_1B = ESC + "81" + END
    CHARTREUSE_2A = ESC + "82" + END
    SEA_GREEN_2 = ESC + "83" + END
    SEA_GREEN_1A = ESC + "84" + END
    SEA_GREEN_1B = ESC + "85" + END
    AQUAMARINE_1A = ESC + "86" + END
    DARK_SLATE_GRAY_2 = ESC + "87" + END
    DARK_RED_2 = ESC + "88" + END
    DEEP_PINK_4B = ESC + "89" + END
    DARK_MAGENTA_1 = ESC + "90" + END
    DARK_MAGENTA_2 = ESC + "91" + END
    DARK_VIOLET_1A = ESC + "92" + END
    PURPLE_1A = ESC + "93" + END
    ORANGE_4B = ESC + "94" + END
    LIGHT_PINK_4 = ESC + "95" + END
    PLUM_4 = ESC + "96" + END
    MEDIUM_PURPLE_3A = ESC + "97" + END
    MEDIUM_PURPLE_3B = ESC + "98" + END
    SLATE_BLUE_1 = ESC + "99" + END
    YELLOW_4A = ESC + "100" + END
    WHEAT_4 = ESC + "101" + END
    GREY_53 = ESC + "102" + END
    LIGHT_SLATE_GREY = ESC + "103" + END
    MEDIUM_PURPLE = ESC + "104" + END
    LIGHT_SLATE_BLUE = ESC + "105" + END
    YELLOW_4B = ESC + "106" + END
    DARK_OLIVE_GREEN_3A = ESC + "107" + END
    DARK_GREEN_SEA = ESC + "108" + END
    LIGHT_SKY_BLUE_3A = ESC + "109" + END
    LIGHT_SKY_BLUE_3B = ESC + "110" + END
    SKY_BLUE_2 = ESC + "111" + END
    CHARTREUSE_2B = ESC + "112" + END
    DARK_OLIVE_GREEN_3B = ESC + "113" + END
    PALE_GREEN_3B = ESC + "114" + END
    DARK_SEA_GREEN_3A = ESC + "115" + END
    DARK_SLATE_GRAY_3 = ESC + "116" + END
    SKY_BLUE_1 = ESC + "117" + END
    CHARTREUSE_1 = ESC + "118" + END
    LIGHT_GREEN_2 = ESC + "119" + END
    LIGHT_GREEN_3 = ESC + "120" + END
    PALE_GREEN_1A = ESC + "121" + END
    AQUAMARINE_1B = ESC + "122" + END
    DARK_SLATE_GRAY_1 = ESC + "123" + END
    RED_3A = ESC + "124" + END
    DEEP_PINK_4C = ESC + "125" + END
    MEDIUM_VIOLET_RED = ESC + "126" + END
    MAGENTA_3A = ESC + "127" + END
    DARK_VIOLET_1B = ESC + "128" + END
    PURPLE_1B = ESC + "129" + END
    DARK_ORANGE_3A = ESC + "130" + END
    INDIAN_RED_1A = ESC + "131" + END
    HOT_PINK_3A = ESC + "132" + END
    MEDIUM_ORCHID_3 = ESC + "133" + END
    MEDIUM_ORCHID = ESC + "134" + END
    MEDIUM_PURPLE_2A = ESC + "135" + END
    DARK_GOLDENROD = ESC + "136" + END
    LIGHT_SALMON_3A = ESC + "137" + END
    ROSY_BROWN = ESC + "138" + END
    GREY_63 = ESC + "139" + END
    MEDIUM_PURPLE_2B = ESC + "140" + END
    MEDIUM_PURPLE_1 = ESC + "141" + END
    GOLD_3A = ESC + "142" + END
    DARK_KHAKI = ESC + "143" + END
    NAVAJO_WHITE_3 = ESC + "144" + END
    GREY_69 = ESC + "145" + END
    LIGHT_STEEL_BLUE_3 = ESC + "146" + END
    LIGHT_STEEL_BLUE = ESC + "147" + END
    YELLOW_3A = ESC + "148" + END
    DARK_OLIVE_GREEN_3 = ESC + "149" + END
    DARK_SEA_GREEN_3B = ESC + "150" + END
    DARK_SEA_GREEN_2 = ESC + "151" + END
    LIGHT_CYAN_3 = ESC + "152" + END
    LIGHT_SKY_BLUE_1 = ESC + "153" + END
    GREEN_YELLOW = ESC + "154" + END
    DARK_OLIVE_GREEN_2 = ESC + "155" + END
    PALE_GREEN_1B = ESC + "156" + END
    DARK_SEA_GREEN_5B = ESC + "157" + END
    DARK_SEA_GREEN_5A = ESC + "158" + END
    PALE_TURQUOISE_1 = ESC + "159" + END
    RED_3A = ESC + "160" + END
    DEEP_PINK_3A = ESC + "161" + END
    DEEP_PINK_3B = ESC + "162" + END
    MAGENTA_3B = ESC + "162" + END
    MAGENTA_3C = ESC + "164" + END
    MAGENTA_2A = ESC + "165" + END
    DARK_ORANGE_3B = ESC + "166" + END
    INDIAN_RED_1B = ESC + "167" + END
    HOT_PINK_3B = ESC + "168" + END
    HOT_PINK_2 = ESC + "169" + END
    ORCHID = ESC + "170" + END
    MEDIUM_ORCHID_1A = ESC + "171" + END
    ORANGE_3 = ESC + "172" + END
    LIGHT_SALMON_3B = ESC + "173" + END
    LIGHT_PINK_3 = ESC + "174" + END
    PINK_3 = ESC + "175" + END
    PLUM_3 = ESC + "176" + END
    VIOLET = ESC + "177" + END
    GOLD_3B = ESC + "178" + END
    LIGHT_GOLDENROD_3 = ESC + "179" + END
    TAN = ESC + "180" + END
    MISTY_ROSE_3 = ESC + "181" + END
    THISTLE_3 = ESC + "182" + END
    PLUM_2 = ESC + "183" + END
    YELLOW_3B = ESC + "184" + END
    KHAKI_3 = ESC + "185" + END
    LIGHT_GOLDENROD_2A = ESC + "186" + END
    LIGHT_YELLOW_3 = ESC + "187" + END
    GREY_84 = ESC + "188" + END
    LIGHT_STEEL_BLUE_1 = ESC + "189" + END
    YELLOW_2 = ESC + "190" + END
    DARK_OLIVE_GREEN_1A = ESC + "191" + END
    DARK_OLIVE_GREEN_1B = ESC + "192" + END
    DARK_SEA_GREEN_1 = ESC + "193" + END
    HONEYDEW_2 = ESC + "194" + END
    LIGHT_CYAN_1 = ESC + "195" + END
    RED_1 = ESC + "196" + END
    DEEP_PINK_2 = ESC + "197" + END
    DEEP_PINK_1A = ESC + "198" + END
    DEEP_PINK_1B = ESC + "199" + END
    MAGENTA_2B = ESC + "200" + END
    MAGENTA_1 = ESC + "201" + END
    ORANGE_RED_1 = ESC + "202" + END
    INDIAN_RED_1C = ESC + "203" + END
    INDIAN_RED_1D = ESC + "204" + END
    HOT_PINK_1A = ESC + "205" + END
    HOT_PINK_1B = ESC + "206" + END
    MEDIUM_ORCHID_1B = ESC + "207" + END
    DARK_ORANGE = ESC + "208" + END
    SALMON_1 = ESC + "209" + END
    LIGHT_CORAL = ESC + "210" + END
    PALE_VIOLET_RED_1 = ESC + "211" + END
    ORCHID_2 = ESC + "212" + END
    ORCHID_1 = ESC + "213" + END
    ORANGE_1 = ESC + "214" + END
    SANDY_BROWN = ESC + "215" + END
    LIGHT_SALMON_1 = ESC + "216" + END
    LIGHT_PINK_1 = ESC + "217" + END
    PINK_1 = ESC + "218" + END
    PLUM_1 = ESC + "219" + END
    GOLD_1 = ESC + "220" + END
    LIGHT_GOLDENROD_2B = ESC + "221" + END
    LIGHT_GOLDENROD_2C = ESC + "222" + END
    NAVAJO_WHITE_1 = ESC + "223" + END
    MISTY_ROSE1 = ESC + "224" + END
    THISTLE_1 = ESC + "225" + END
    YELLOW_1 = ESC + "226" + END
    LIGHT_GOLDENROD_1 = ESC + "227" + END
    KHAKI_1 = ESC + "228" + END
    WHEAT_1 = ESC + "229" + END
    CORNSILK_1 = ESC + "230" + END
    GREY_100 = ESC + "231" + END
    GREY_3 = ESC + "232" + END
    GREY_7 = ESC + "233" + END
    GREY_11 = ESC + "234" + END
    GREY_15 = ESC + "235" + END
    GREY_19 = ESC + "236" + END
    GREY_23 = ESC + "237" + END
    GREY_27 = ESC + "238" + END
    GREY_30 = ESC + "239" + END
    GREY_35 = ESC + "240" + END
    GREY_39 = ESC + "241" + END
    GREY_42 = ESC + "242" + END
    GREY_46 = ESC + "243" + END
    GREY_50 = ESC + "244" + END
    GREY_54 = ESC + "245" + END
    GREY_58 = ESC + "246" + END
    GREY_62 = ESC + "247" + END
    GREY_66 = ESC + "248" + END
    GREY_70 = ESC + "249" + END
    GREY_74 = ESC + "250" + END
    GREY_78 = ESC + "251" + END
    GREY_82 = ESC + "252" + END
    GREY_85 = ESC + "253" + END
    GREY_89 = ESC + "254" + END
    GREY_93 = ESC + "255" + END
