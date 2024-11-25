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
SCRDIR=$(cd $T; pwd)
CONF=$SCRDIR/preinstall.conf
MODE_POSTINSTALL='No'
FIND_PYTHONSCR=$SCRDIR/../script/find_python3x.py
CREATECMD_PYTHONSCR=$SCRDIR/createcmd_shellwrapper.py
get_executableabspath(){
    local _NAME _BINDIR _OPTBINDIR _D
    _NAME=$1
    _BINDIR="$(echo "$PATH" | tr ':' ' ')"
    _OPTBINDIR=/opt/local/bin
    : ${_BINDIR:='/sbin /bin /usr/sbin /usr/bin /usr/local/sbin /usr/local/bin'}
    if test -d "$_OPTBINDIR" ; then
	_BINDIR="$_BINDIR /opt/local/bin" ; fi 
    find $_BINDIR -name "$_NAME" 2> /dev/null | head -n 1
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
find_python37later(){
    local _PYTHON _PYTHON37LATER
    _PYTHON=$(find_python3path)
    _PYTHON37LATER=$($_PYTHON $FIND_PYTHONSCR)
    if ! "$_PYTHON37LATER" --version > /dev/null 2>&1; then
	echo 'Error: Not found python3.7 later.'; exit 1; fi
    return
}
check_rootuser(){
    local ARGSUSER TMP_USER
    ARGSUSER='root'
    TMP_USER=$(id -p | grep uid | awk '{print $2}')
    if test "$ARGSUSER" != "$TMP_USER"; then
        echo 'Error: Not root user.' " [uid: $TMP_USER]"
        exit 1
    fi
    return
}
for ARG in $@; do
    if test "$ARG" == '--postinstall'; then
	MODE_POSTINSTALL='YES'; continue; fi
done
if ! test -f "$CONF"; then
    echo 'Error: Not found config file.' " [$CONF]"; exit 1; fi
. "$CONF"
if test "$MODE_POSTINSTALL" != 'YES'; then
    if ! $PYTHON --version > /dev/null 2>&1; then
        find_python37later
    fi
    case $(uname -s) in
	'Darwin' | 'FreeBSD')
	    true;;
	*)
	    echo 'Warning: Unsupport OS';;
    esac
    check_rootuser
    if ! test -d "$INSTALL_BIN"; then
	echo 'Error: Not found INSTALL_BIN directory.' "[$INSTALL_BIN]"; exit 1; fi
    if ! test -d "$INSTALL_DIR"; then
	if ! mkdir -p "$INSTALL_DIR"; then
	    echo 'Error: Not make the directory.' "[$INSTALL_DIR]"; exit 1; fi
    fi
    exit 0    
elif test "$MODE_POSTINSTALL" == 'YES'; then
    if ! test -x "$PYTHON"; then
	PYTHON=$(find_python3path); fi
    if ! $PYTHON --version > /dev/null 2>&1; then
	echo 'Error: Not find python3 command'; exit 1; fi
    $PYTHON "$CREATECMD_PYTHONSCR" --cmdname "$CMDNAME"\
	    --sh "$CMDSHELL" --basedir "$INSTALL_DIR" --dstcmdname "$DSTCMDNAME" "$INSTALL_BIN" || exit 1
    exit 0
fi
exit 1

