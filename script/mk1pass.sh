#!/bin/sh
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

T=$(dirname $0)
SCRDIR=$(cd $T; pwd);
PYSCR=mk1pass.py
FINDPY="$SCRDIR"/find_python3x.py
get_executableabspath(){
    local _NAME _BINDIR _OPTBINDIR 
    _NAME=$1
    _BINDIR="$(echo "$PATH" | tr ':' ' ')"
    _OPTBINDIR=/opt/local/bin
    : ${_BINDIR:='/sbin /bin /usr/sbin /usr/bin /usr/local/sbin /usr/local/bin'}
    if test -d "$_OPTBINDIR" ; then
	_BINDIR="$_BINDIR /opt/local/bin" ; fi 
    find $_BINDIR -type f -name "$_NAME" 2> /dev/null | head -n 1
    return
}
find_python3path(){
    local PNAME PYTHONPATH
    PNAME="python3"
    PYTHONPATH=$(get_executableabspath $PNAME)
    if ! test -z "$PYTHONPATH" ; then
	echo "$PYTHONPATH"
	return; fi
    for N in $(seq 6 29); do
	PNAME="python3.$N"
	PYTHONPATH=$(get_executableabspath $PNAME)
	if ! test -z "$PYTHONPATH" ; then
	    break; fi
    done
    echo "$PYTHONPATH"
    return
}
PYTHON3=$(find_python3path)
if ! $PYTHON3 --version >> /dev/null; then
    echo 'Error: Not found python.'; exit 1; fi
PYTHON3X=$($PYTHON3 $FINDPY)
if test -z "$PYTHON3X"; then
    echo 'Error: python 3.6 later'; exit 1; fi
exec $PYTHON3X $SCRDIR/$PYSCR $@

