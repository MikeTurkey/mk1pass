#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# mk1pass, Generate random strings for passwords.
# Copyright (C) 2023-2024 Mike Turkey All rights reserved.
# contact: voice[ATmark]miketurkey.com
# license: GPLv3 License
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ADDITIONAL MACHINE LEARNING PROHIBITION CLAUSE
#
# In addition to the rights granted under the applicable license(GPL-3),
# you are expressly prohibited from using any form of machine learning,
# artificial intelligence, or similar technologies to analyze, process,
# or extract information from this software, or to create derivative
# works based on this software.
#
# This prohibition includes, but is not limited to, training machine
# learning models, neural networks, or any other automated systems using
# the code or output of this software.
#
# The purpose of this prohibition is to protect the integrity and
# intended use of this software. If you wish to use this software for
# machine learning or similar purposes, you must seek explicit written
# permission from the copyright holder.
#
# see also 
#     GPL-3 Licence: https://www.gnu.org/licenses/gpl-3.0.html.en
#     Mike Turkey.com: https://miketurkey.com/

import random
import string
import hashlib
import warnings
import re
import time
import os
import unicodedata
import sys


def printerror_python3x(major, minor):
    if sys.version_info.major == major and sys.version_info.minor < minor:
        errmes = 'Error: Need python {0}.{1} later. [python: {2}]'.format(
            major, minor, sys.version.split(' ')[0])
        print(errmes, file=sys.stderr)
        exit(1)


printerror_python3x(3, 6)
if sys.version_info.major == 3 and sys.version_info.minor >= 5:
    import typing
if __name__ == '__main__':
    from printdv import print_err, print_mes
else:
    from .printdv import print_err, print_mes


class Lpyk(object):
    @staticmethod
    def randomstrings(total_len: int, letters: str = string.ascii_letters+string.digits,
                      prefix: str = '', suffix: str = '') -> str:
        randomstring_len = total_len - len(prefix) - len(suffix)
        if randomstring_len <= 0:
            raise ValueError(
                '"total_len - length of prefix and suffix" is smaller than 1.')
        ret = ''.join([random.choice(letters)
                      for i in range(randomstring_len)])
        return prefix + ret + suffix


class Args_mk1pass(object):
    def __init__(self):
        self.lower: bool = False
        self.upper: bool = False
        self.special: bool = False
        self.numeric: bool = False
        self.count: int = 1
        self.avoid: bool = False
        self.prefix: str = ''
        self.suffix: str = ''
        self.version: bool = False
        self.help: bool = False
        self.license: bool = False
        if sys.version_info.major == 3 and sys.version_info.minor >= 9:
            self.length: typing.Union[int, None] = None
        else:
            self.length = None
        self._pass_check: bool = False
        return

    def _str2int(self, s: str) -> int:
        errmes: str = ''
        i: int = 0
        if isinstance(s, str) != True:
            errmes = 's is not string type.'
            raise TypeError(errmes)
        try:
            i = int(s)
        except:
            errmes = 'Error: Not numeric string. [{0}]'.format(i)
            print_err(errmes)
            exit(1)
        return i

    def print_attribute(self):
        for k, v in self.__dict__.items():
            mes = '{0}= {1}'.format(k, v)
            print(mes)
        return

    def analyze(self):
        arg: str
        on_count: bool = False
        on_prefix: bool = False
        on_suffix: bool = False
        dfletters: bool = True
        for arg in sys.argv[1:]:
            if arg == '-l' or arg == '--lower':
                self.lower = True
                dfletters = False
                continue
            if arg == '-u' or arg == '--upper':
                self.upper = True
                dfletters = False
                continue
            if arg == '-s' or arg == '--special':
                self.special = True
                dfletters = False
                continue
            if arg == '-n' or arg == '--numeric':
                self.numeric = True
                dfletters = False
                continue
            if arg == '-a' or arg == '--avoid':
                self.avoid = True
                dfletters = False
                continue
            if arg == '--version':
                self.version = True
                continue
            if arg == '-h' or arg == '--help':
                self.help = True
                continue
            if arg == '--license':
                self.license = True
                continue
            if on_count:
                self.count = self._str2int(arg)
                on_count = False
                continue
            if on_prefix:
                self.prefix = arg
                on_prefix = False
                continue
            if on_suffix:
                self.suffix = arg
                on_suffix = False
                continue
            if arg == '-c' or arg == '--count':
                on_count = True
                continue
            if arg == '-e' or arg == '--prefix':
                on_prefix = True
                continue
            if arg == '-f' or arg == '--suffix':
                on_suffix = True
                continue
            if self.length == None:
                self.length = self._str2int(arg)
                continue
            errmes = 'Error: Invalid argument. [{0}]'.format(arg)
            print_err(errmes)
            exit(1)
        if dfletters:
            self.lower = True
            self.upper = True
            self.numeric = True
            self.avoid = True
        return

    def check(self):
        errmes: str = ''
        length: int = 0
        if self.version:
            Main_mk1pass.show_version()
            exit(0)
        if self.help:
            Main_mk1pass.show_help()
            exit(0)
        if self.license:
            Main_mk1pass.show_licence()
            exit(0)
        if self.lower != True and self.upper != True and self.special != True and self.numeric != True:
            errmes = 'Error: No Charactor option. (--lower, --upper, --numeric, --special)'
            print_err(errmes)
            exit(1)
        if self.count <= 0:
            errmes = 'Error: count(--count) is NOT positive. [{0}]'.format(
                self.count)
            print_err(errmes)
            exit(1)
        if self.count >= 4096:
            errmes = 'Error: count(--count) is over the maximum limit. [{0}]'.format(
                self.count)
            print_err(errmes)
            exit(1)
        if self.length == None:
            errmes = 'Error: Empty String length.'
            print_err(errmes)
            exit(1)
        if self.length <= 0:
            errmes = 'Error: String length is NOT positive. [{0}]'.format(
                self.length)
            print_err(errmes)
            exit(1)
        if self.length >= 1048576:
            errmes = 'Error: String length is over the maximum limit. [{0}]'.format(
                self.length)
            print_err(errmes)
            exit(1)
        if len(self.prefix) >= self.length:
            errmes = 'Error: --prefix length is NOT less than random string length. [{0} >= {1}] '
            errmes = errmes.format(len(self.prefix), self.length)
            print_err(errmes)
            exit(1)
        if len(self.suffix) >= self.length:
            errmes = 'Error: --suffix length is NOT less than random string length. [{0} >= {1}] '
            errmes = errmes.format(len(self.suffix), self.length)
            print_err(errmes)
            exit(1)
        length = len(self.prefix) + len(self.suffix)
        if length >= self.length:
            errmes = 'Error: --prefix and --suffix length is NOT less than random string length. [{0} >= {1}] '
            errmes = errmes.format(length, self.length)
            print_err(errmes)
            exit(1)
        self._pass_check = True
        return


class Main_mk1pass(object):
    version: str = '0.0.5'
    date: str = '14 Dec 2024'

    @staticmethod
    def show_version():
        scr_version: str = Main_mk1pass.version
        print_mes(scr_version)
        return

    @staticmethod
    def show_help():
        mes: str
        scr_version: str = Main_mk1pass.version
        scr_date: str = Main_mk1pass.date
        scr_fname: str = 'mk1pass'
        meses: list = ['{0} created by MikeTurkey'.format(scr_fname),
                       'Version {0}, {1}'.format(scr_version, scr_date),
                       '2023, COPYRIGHT MikeTurkey, All Right Reserved.',
                       'ABSOLUTELY NO WARRANTY. The Licence is based on GPLv3 Licence.',
                       'URL: https://miketurkey.com',
                       '',
                       'Summary',
                       '  Generate random strings for passwords.',
                       'Synopsis',
                       '  mk1pass [-alnsu] [-c COUNT] [-e PREFIX] [-f SUFFIX] [LENGTH] ',
                       '  mk1pass [--version --license [-h | --help]]',
                       'Description',
                       '  -a, --avoid: Avoid misleading letters. (l, I, O, o, 0)',
                       '  -c, --count: Count of random strings.',
                       '  -e, --prefix: Add prefix string to random strings.',
                       '  -f, --suffix: Add suffix string to random strings.',
                       '  -l, --lower: Lowercase strings.',
                       '  -n, --numeric: Numeric strings.',
                       '  -s, --special: Special charactors.',
                       '  -u, --upper: Uppercase strings.',
                       '  -h, --help: Show Help message.',
                       '  --version: Show version.',
                       '  --license: Show License.',
                       '',
                       'e.g.',
                       '  $ mk1pass 8',
                       '    Output 1 row of 8 random strings(--upper, --lower, --numeric, --avoid)',
                       '  $ mk1pass --lower 8',
                       '    Output 1 row of 8 random lowercase strings',
                       '  $ mk1pass --numeric 8',
                       '    Output 1 row of 8 random numeric strings',
                       '  $ mk1pass --lower --upper 8',
                       '    Output 1 row of 8 random lowercase and uppercase strings',
                       '  $ mk1pass --avoid --lower --upper 8',
                       '    Output 1 row of 8 random lowercase and uppercase strings, avoiding mis-leading letter.',
                       '  $ mk1pass -c 10 8',
                       '    Output 10 rows of 8 random strings(--upper, --lower, --numeric, --avoid)',
                       '']
        if scr_fname == '':
            raise RuntimeError()
        for mes in meses:
            mes = unicodedata.normalize('NFD', mes)
            print(mes)
        return

    @staticmethod
    def show_licence():
        mes: str
        mes = '''mk1pass, Generate random strings for passwords.
Copyright (C) 2023 Mike Turkey All rights reserved.
contact: voice[ATmark]miketurkey.com
license: GPLv3 License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
ADDITIONAL MACHINE LEARNING PROHIBITION CLAUSE
In addition to the rights granted under the applicable license(GPL-3),
you are expressly prohibited from using any form of machine learning,
artificial intelligence, or similar technologies to analyze, process,
or extract information from this software, or to create derivative
works based on this software.
This prohibition includes, but is not limited to, training machine
learning models, neural networks, or any other automated systems using
the code or output of this software.
The purpose of this prohibition is to protect the integrity and
intended use of this software. If you wish to use this software for
machine learning or similar purposes, you must seek explicit written
permission from the copyright holder.
see also 
    GPL-3 Licence: https://www.gnu.org/licenses/gpl-3.0.html.en
    Mike Turkey.com: https://miketurkey.com/ '''
        print(mes)
        return

    @staticmethod
    def randomstring(args: Args_mk1pass) -> str:
        letters: str = ''
        special: str = ''
        errmes: str = ''
        retstr: str = ''
        avoid_letters: str = ''
        special = '!#$%&()*+,-./:;<=>?@[]^_{}~'
        letters = letters + string.ascii_lowercase if args.lower == True else letters
        letters = letters + string.ascii_uppercase if args.upper == True else letters
        letters = letters + string.digits if args.numeric == True else letters
        letters = letters + special if args.special == True else letters
        if args.avoid:
            avoid_letters = 'lIOo0'
            for s in avoid_letters:
                letters = letters.replace(s, '')
        if len(letters) == 0:
            errmes = 'Error: Empty letters in ramdomstring() function'
            print_err(errmes)
            exit(1)
        if args.special:
            while True:
                retstr = Lpyk.randomstrings(
                    args.length, letters=letters, prefix=args.prefix, suffix=args.suffix)
                count_sp = 0
                for s in special:
                    count_sp += retstr.count(s)
                if len(retstr) > count_sp * 7:
                    break
        else:
            retstr = Lpyk.randomstrings(
                args.length, letters=letters, prefix=args.prefix, suffix=args.suffix)
        return retstr


def main_mk1pass():
    errmes: str = ''
    s: str
    i: int = 0
    if sys.version_info.major == 3 and sys.version_info.minor < 6:
        errmes = 'Error: python 3.6 later. [python: {0}]'.format(
            sys.version.split(' ')[0])
        print_err(errmes)
        exit(1)
    args: Args_mk1pass = Args_mk1pass()
    args.analyze()
    args.check()
    for i in range(args.count):
        s = Main_mk1pass.randomstring(args)
        print(s)
    exit(0)


if __name__ == '__main__':
    main_mk1pass()
    exit(0)
