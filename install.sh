#!/bin/sh

T=$(dirname "$0")
SCRDIR=$(cd "$T"; pwd)
CONF="$SCRDIR"/snakeland-mk1pass.conf
INSTALLSNAKE="$SCRDIR"/tools/install-snakeland.sh

### Function ###
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

### Main ###
check_rootuser

for F in "$CONF" "$INSTALLSNAKE"; do
    if ! test -r "$F"; then
	echo 'Error: Not found the file.' " [$F]" > /dev/stderr; exit 1; fi
done

if ! snakeland --version > /dev/null 2>&1; then
    "$INSTALLSNAKE" || exit 1
fi

snakeland install "$CONF"  || exit 1

