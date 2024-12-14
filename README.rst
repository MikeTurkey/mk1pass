

mk1pass 
********************************

| mk1pass created by MikeTurkey
| Version 0.0.5, 14 Dec 2024
| 2023-2024, COPYRIGHT MikeTurkey, All Right Reserved.
| ABSOLUTELY NO WARRANTY. The Licence is based on GPLv3 Licence.
| URL: https://miketurkey.com

Summary
=======

Generate random strings for passwords.

Synopsis
========

| mk1pass [-alnsu] [-c COUNT] [-e PREFIX] [-f SUFFIX] [LENGTH] 
| mk1pass [--version --license [-h | --help]]

Description
=============

*  -a, --avoid: Avoid misleading letters. (l, I, O, o, 0) 
*  -c, --count: Count of random strings.
*  -e, --prefix: Add prefix string to random strings.
*  -f, --suffix: Add suffix string to random strings.
*  -l, --lower: Lowercase strings.
*  -n, --numeric: Numeric strings.
*  -s, --special: Special charactors.
*  -u, --upper: Uppercase strings.
*  -h, --help: Show Help message.
*  --version: Show version.
*  --license: Show License.

e.g.
  $ mk1pass 8
    Output 1 row of 8 random strings(--upper, --lower, --numeric, --avoid)
  $ mk1pass --lower 8
    Output 1 row of 8 random lowercase strings
  $ mk1pass --numeric 8
    Output 1 row of 8 random numeric strings
  $ mk1pass --lower --upper 8
    Output 1 row of 8 random lowercase and uppercase strings
  $ mk1pass --avoid --lower --upper 8
    Output 1 row of 8 random lowercase and uppercase strings, avoiding mis-leading letter.
  $ mk1pass -c 10 8
    Output 10 rows of 8 random strings(--upper, --lower, --numeric, --avoid)

Quick Install(Experimental)
============================

Install via pypi(python3)

.. code-block:: console

   $ python3 -m pip install mk1pass

Install via github

.. code-block:: console

   $ cd tmp
   $ git clone https://github.com/MikeTurkey/mk1pass.git
   $ sudo mk1pass/install.sh

Install via miketurkey.com

.. code-block:: console

  $ curl -O https://miketurkey.com/get-mk1pass.sh
  $ sh get-mk1pass.sh
  $ sudo mk1pass/install.sh

  
