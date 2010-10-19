#!/bin/sh

case "$reason" in
	PREINIT|STOP|RELEASE)
		/sbin/resolvconf -d "${interface}.inet" 2>&1 \
			| logger -p daemon.err -t dhclient-script
		;;
esac
