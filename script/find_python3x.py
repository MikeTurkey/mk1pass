#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk1pass, Generate random strings for passwords.
# Copyright (C) 2023 Mike Turkey All rights reserved.
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

import sys

if sys.version_info.major == 3 and sys.version_info.minor < 5:
    errmes = "Error: Need python 3.5 later. [python: {0}]".format(
        sys.version.split(" ")[0]
    )
    print(errmes, file=sys.stderr)
    exit(1)
import os
import subprocess


class Main_common(object):
    @staticmethod
    def show_version():
        scr_version = "0.0.1"
        scr_date = "12 Nov 2023"
        scr_fname = "find_python3x.py"
        meses = [
            "{0} Version {1}, {2}".format(scr_fname, scr_version, scr_date),
            "2023, COPYRIGHT MikeTurkey, All Right Reserved.",
            "ABSOLUTY NO WARRANTY, SHACKSUM LICENCE",
            "The license is based on GPLv3 License.",
            "",
            "Summary",
            "  Find executable python command.",
            "",
        ]
        if scr_fname == "":
            raise RuntimeError()
        for mes in meses:
            print(mes)
        return

    @staticmethod
    def print_namedtuple(t: tuple):
        k: str
        d: dict = t._asdict()
        for k, v in d.items():
            print("k:", k, "v:", v)
        return

    @staticmethod
    def is_pythonversion(python_version: str, minver: str) -> bool:
        chklist: list
        errmes: str = ""
        tmplist1: list[str] = []
        tmplist2: list[str] = []
        major: int = 0
        minor: int = 0
        minver_major: int = 0
        minver_minor: int = 0
        debug_printvalue: bool = False
        chklist = [(python_version, str, "python_version"), (minver, str, "minver")]
        for v, vtype, vname in chklist:
            if isinstance(v, vtype) != True:
                errmes = "{0} variable is NOT string type.".format(vname)
                raise TypeError(errmes)
        tmplist1 = python_version.split(" ", maxsplit=1)
        tmplist2 = tmplist1[1].split(".")
        major = int(tmplist2[0])
        minor = int(tmplist2[1])
        tmplist1 = minver.split(".")
        minver_major = int(tmplist1[0])
        minver_minor = int(tmplist1[1])
        if debug_printvalue:
            print("major:", major)
            print("minor:", minor)
            print("minver_major:", minver_major)
            print("minver_minor:", minver_minor)
        if major != minver_major:
            return False
        if minor < minver_minor:
            return False
        return True


def main_common():
    on_pyver = False
    pyver = ""
    for arg in sys.argv[1:]:
        if on_pyver:
            pyver = arg
            on_pyver = False
            continue
        if arg == "--version":
            Main_common.show_version()
            exit(0)
        if arg == "--pyver":
            on_pyver = True
            continue
    if pyver == "":
        pyver_major = 3
        pyver_minor = 6
        pyver = "3.6"
    else:
        tmplist = pyver.split(".")
        pyver_major = int(tmplist[0])
        pyver_minor = int(tmplist[1])
        pyver = "{0}.{1}".format(pyver_major, pyver_minor)
    if pyver_major != 3:
        errmes = "Error: the script find python version 3 command only."
        print(errmes, file=sys.stderr)
        exit(1)
    if pyver_minor >= 100:
        errmes = "Error: Max version is 3.99. [{0}]".format(pyver_minor)
        print(errmes, file=sys.stderr)
        exit(1)
    tmplist = os.environ["PATH"].split(":")
    cmdpaths = [f for f in tmplist if os.path.isdir(f) == True]
    pythoncmdlist = list()
    for d in cmdpaths:
        for f in os.listdir(d):
            fpath = os.path.normpath(os.path.join(d, f))
            if os.path.isfile:
                if f.startswith("python3"):
                    pythoncmdlist.append(fpath)
    is_pythonversion = Main_common.is_pythonversion
    for i in range(99, 6, -1):
        s = "python3.{0}".format(i)
        for f in pythoncmdlist:
            basename = os.path.basename(f)
            if basename == s:
                retproc = subprocess.run([f, "--version"], capture_output=True)
                if retproc.returncode == 0:
                    if is_pythonversion(str(retproc.stdout), pyver):
                        print(f)
                        exit(0)
    s = "python3"
    for f in pythoncmdlist:
        basename = os.path.basename(f)
        if basename == s:
            retproc = subprocess.run([f, "--version"], capture_output=True)
            if retproc.returncode == 0:
                if is_pythonversion(str(retproc.stdout), pyver):
                    print(f)
                    exit(0)
    exit(1)


def main_findpython3():
    main_common()
    return


if __name__ == "__main__":
    main_findpython3()
    exit(0)
