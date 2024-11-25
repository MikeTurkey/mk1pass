
INSTALL_DIR=/usr/local/share/mk1pass
# INSTALL_MANDIR=/usr/local/share/man/man1
PREINSTALL_SCRIPT=tools/preinstall.sh

install: script/find_python3x.py script/printdv.py script/mk1pass.sh script/mk1pass.py 
	${PREINSTALL_SCRIPT}
	install -d -m 755 ${INSTALL_DIR}
	install -m 755 -S script/find_python3x.py script/printdv.py script/mk1pass.sh script/mk1pass.py ${INSTALL_DIR}
	@# install -d -m 755 ${INSTALL_MANDIR}
	@# install -m 644 -S man/mk1pass.1 ${INSTALL_MANDIR}
	${PREINSTALL_SCRIPT} --postinstall

testexec:
	@mk1pass --version > /dev/null
	@mk1pass 30        > /dev/null
	@mk1pass -c 5 15   > /dev/null
	@echo 'Success: testexec'


