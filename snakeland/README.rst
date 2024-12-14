
snakeland
********************************

| snakeland created by MikeTurkey
| Version 0.0.2, 26 Nov 2024
| 2023-2024, COPYRIGHT MikeTurkey, All Right Reserved.
| ABSOLUTELY NO WARRANTY. The Licence is based on GPLv3.
| URL: https://miketurkey.com

Summary
=======

Instant Python3 script installer.

Synopsis
========

| snakeland --version | --help | --license'
| snakeland install [CONFIG]
| snakeland findpy3 [--later 3.xx] | [--older 3.xx] | --latest | [--range 3.xx-3.yy] | [--order 3.x,..,3.yy]

QUICK START
--------------

Install by config

.. code-block:: console

   $ snakeland install snakeland-APP.conf

Find python3 command.

.. code-block:: console

   $ snakeland findpy3 --later 3.8
     /usr/bin/python3.12
   $ snakeland findpy3 --older 3.11
     /usr/bin/python3.9
   $ snakeland findpy3 --latest
     /usr/bin/python3.12
   $ snakeland range 3.5-3.10
     /usr/bin/python3.9
   $ snakeland range --order 3.13,3.12,3.11,3.10,3.9
     /usr/bin/python3.12   
     
DESCRIPTION
------------

snakeland is instant python3 script installer.
The script wrapper is make on /usr/local/bin as cui command.

ARGUMENT
------------

.. .. option:: --version, --help, --license
.. | Print version, help message, license.

--version, --help, --license
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   Print version, help message, license.

--latest
^^^^^^^^

.. code-block:: text
   
   findpy3 sub command only
   Print latest python3 command path.
	    
--later [PYTHONVERSION]
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   findpy3 sub command only
   Print PYTHONVERSION later command path.

--older [PYTHONVERSION]
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   findpy3 sub command only
   Print PYTHONVERSION older command path.

--range 3.xx-3.yy
^^^^^^^^^^^^^^^^^^

.. code-block:: text
		
   findpy3 sub command only
   Print latest python command path in 3.xx - 3.yy.

--order 3.x,...,3.yy
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text
		
   findpy3 sub command only
   Print first matched python command path.

CONFIG
------------

The Config is in restricted toml format.

OSCHECK:  
^^^^^^^^^

.. code-block:: text

   Describe OS names. The string is similar to 'uname -s' cmd.
   default section, optional key.
     Darwin: Mac OS
     Linux: Linux based OS
     FreeBSD: FreeBSD OS
     e.g.
       OSCHECK = ['Darwin', 'Linux', 'FreeBSD']

     
DSTBASEDIR:
^^^^^^^^^^^^

.. code-block:: text
		
   Destination Base Directory.
   Recommend path is '/usr/local/libexec/CMDNAME'.
   default section, essential key.

INSTALLCMD:
^^^^^^^^^^^^

.. code-block:: text

   Install command path. default path is '/usr/local/bin'.
   default section, optional key.

	     
CMDNAME:
^^^^^^^^^

.. code-block:: text

   The command name. The command file is made on INSTALLCMD directory.
   default section, essential key.

TARGETPY3:
^^^^^^^^^^^

.. code-block:: text

   The python3 script path. The script is executed by python3.xx cmd.
   default section, optional key.
   (Either of TARGETPY3, TARGETCMD is always required.)

SHEBANG:
^^^^^^^^^

.. code-block:: text

   The shebang of CMDNAME file. default path is '/bin/sh'.
   default section, optional key.

PY3VERSION:
^^^^^^^^^^^^

.. code-block:: text

   Execute python3 of the version.
   The string is similar to 'findpy3' options.
   default section, optional key.
     '3.x later'  : python 3.x later.
     '3.x older'  : python 3.x older.
     'latest'     : Latest python3 
     '3.xx - 3.yy': Latest python3 in 3.xx - 3.yy.
     '3.6 3.7 3.8': First found python3 in 3.6, 3.7, 3.8.
   
DSTDIR:
^^^^^^^^

.. code-block:: text

   Relative path of DSTBASEDIR.
   You cannot set it to a directory above the DSTBASEDIR.
   source file section, essential key.

	 
FMODE:
^^^^^^^

.. code-block:: text

   File mode of the section file. default mode is 644.
   source file section, optional key.

Example of config
^^^^^^^^^^^^^^^^^^

.. code-block:: text
		
   DSTBASEDIR = '/usr/local/libexec/CMDNAMEAPP/'
   CMDNAME   = 'CMDNAMEAPP'
   TARGETPY3 = '/usr/local/libexec/CMDNAMEAPP/CMDNAMEAPP.py'
   [script/CMDNAMEAPP.py]
       DSTDIR = '.'

Bugs
----

Please report bugs to the e-mail: <voice[ATmark]miketurkey.com>

   
Author
------

Mike Turkey <voice[ATmark]miketurkey.com>

License
-------

| GPLv3 LICENSE
| 2023 Copyright Mike Turkey
| ABSOLUTELY NO WARRANTY
|

This software is licensed under the terms of the GNU General Public License, version 3 (GPLv3), with an additional clause prohibiting the use of this software for machine learning purposes. Please refer to the LICENSE file for the complete license text and additional terms.

|
|  See also
|    GPL-3 Licence, https://www.gnu.org/licenses/gpl-3.0.html.en
|    Mike Turkey.com, https://miketurkey.com
  

