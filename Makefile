
INSTALL_DIR=/usr/local/share/mk1pass
# INSTALL_MANDIR=/usr/local/share/man/man1
PREINSTALL_SCRIPT=tools/preinstall.sh

INSTALL_SCRIPT=install.sh

install: script/find_python3x.py script/printdv.py script/mk1pass.sh script/mk1pass.py
	${INSTALL_SCRIPT}

testexec:
	@mk1pass --version > /dev/null
	@mk1pass 30        > /dev/null
	@mk1pass -c 5 15   > /dev/null
	@echo 'Success: testexec'


