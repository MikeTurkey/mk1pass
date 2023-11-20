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


# Copyright

# plan
# createcmd_sha-checksum.py --cmdname sha-checksum --sh /bin/sh
#                           --basedir /usr/local/share/shacksum --dstcmdname shacksum.sh /usr/local/bin

### History

import sys;
if sys.version_info.major == 3 and sys.version_info.minor < 5:
    errmes = 'Error: Need python 3.5 later. [python: {0}]'.format(sys.version.split(' ')[0]);
    print(errmes, file=sys.stderr); exit(1);

import os;
# import time;
# import re;
import subprocess;
# import shutil;
# import stat;
# import string; 
    
class Main_common(object):
    @staticmethod
    def show_version():
        scr_version = '0.01';
        scr_date  = '14 Nov 2023';
        scr_fname = 'createcmd_shellwrapper.py';
        
        meses = ['{0} written by Mike Turkey.'.format(scr_fname),
                 'Version {0}, {1}'.format(scr_version, scr_date),
                 '2023, Copyright T.Watanabe, All Right Reserved.',
                 'ABSOLUTELY NO WARRANTY, SHACKSUM LICENSE(Based GPL-3 License)', 
                 '',
                 'Summary',
                 '  Create sha-checksum.py execute command.',
                 'e.g.',
                 '{0} --cmdname sha-checksum --sh /bin/sh --basedir /usr/local/share/sha-checksum --dstcmdname sha-checksum.sh /usr/local/bin'.format(scr_fname),
                 ''];

        if scr_fname == '':
            raise RuntimeError()
        
        for mes in meses:
            print(mes);
        return;

    @staticmethod
    def print_namedtuple(t: tuple):
        '''
        recipe 
        class Point(types.NamedTuple):
            x: int = 10
            y: int = 30
        p = Point()
        print_namedtuple(p);
        '''
        k: str; 
        d: dict = t._asdict();

        for k, v in d.items():
            print('k:', k, 'v:', v);
        return;


def main_common():
    # sudo python3 script/createcmd_sha-checksum.py --cmdname sha-checksum --sh /bin/sh --basedir /usr/local/share/borgmie/ /usr/local/bin
    # --dstcmdname shacksum.py 
    cmdname='';    on_cmdname = False;
    shcmd = '';    on_shcmd   = False;
    basedir = '';  on_basedir = False;
    dstcmdname=''; on_dstcmdname = False;
    targetdir = '';
    for arg in sys.argv[1:]:
        if arg == '--version':
            Main_common.show_version(); exit(0);

        if on_basedir:
            basedir = arg; on_basedir = False; continue;
        if on_cmdname:
            cmdname = arg; on_cmdname = False; continue;
        if on_shcmd:
            shcmd = arg; on_shcmd = False; continue;
        if on_dstcmdname:
            dstcmdname = arg; on_dstcmdname = False; continue;

        if arg == '--basedir':
            on_basedir = True; continue;
        if arg == '--cmdname':
            on_cmdname = True; continue;
        if arg == '--sh':
            on_shcmd = True; continue;
        if arg == '--dstcmdname':
            on_dstcmdname = True; continue;
            
        if targetdir == '':
            targetdir = arg; continue;

        errmes = 'Error: Invalid argument. [{0}]'.format(arg);
        print(errmes, file=sys.stderr); exit(1);

    if os.path.isdir(targetdir) != True:
        errmes = 'Error: Not directory. [{0}]'.format(targetdir);
        print(errmes, file=sys.stderr); exit(1);

    s = os.path.expanduser(basedir);
    basedir = os.path.abspath(s) if os.path.isabs(s) != True else s;
    s = os.path.expanduser(targetdir);
    targetdir = os.path.abspath(s) if os.path.isabs(s) != True else s;
    
    shascriptpath = os.path.normpath('{0}/{1}'.format(basedir, dstcmdname));
    create_str = '#!{0}\nexec {1} "$@"\n'.format(shcmd, shascriptpath);

    targetfpath = os.path.normpath('{0}/{1}'.format(targetdir, cmdname));
    with open(targetfpath, 'wt') as fp:
        fp.write(create_str);

    # chmod 755 targetfpath
    os.chmod(targetfpath, 0o755);

    exit(0)

                                     

                                     

        
    
    cmdpaths = os.environ['PATH'].split(':');

    pythoncmdlist = list()
    # ptn1 = r'python3$'
    # ptn2 = r'python3[.][0-9]?[0-9]+';
    for d in cmdpaths:
        for f in os.listdir(d):
            fpath = os.path.normpath(os.path.join(d, f))
            if os.path.isfile:
                if f.startswith('python3'):
                    pythoncmdlist.append(fpath);

    # Find python3.xx
    for i in range(99, 6, -1):
        s = 'python3.{0}'.format(i);
        for f in pythoncmdlist:
            basename = os.path.basename(f)
            if basename == s:
                retproc = subprocess.run([f, '--version'], capture_output=True);
                if retproc.returncode == 0:
                    print(f); exit(0);

    # Find python3
    s = 'python3'
    for f in pythoncmdlist:
        basename = os.path.basename(f)
        if basename == s:
            retproc = subprocess.run([f, '--version'], capture_output=True);
            if retproc.returncode == 0:
                print(f); exit(0);

    exit(1)
                
            
    
    
def main_findpython3():
    main_common();
    return;

if __name__ == '__main__':
    # t = time.time();
    # Main routine
    main_findpython3();

    # t = time.time() - t; 
    # print(f'\nexecutetime: {t} sec');
    exit(0);
    
    





