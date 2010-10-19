#!/bin/sh

make_resolv_conf() {
	if [ -n "$new_domain_name" -o -n "$new_domain_name_servers" ]; then

		echo -n > $my_resolv_conf

		if [ -n "$new_domain_name" ]; then
			R="search $new_domain_name\n"
		fi

		if [ -n "$new_domain_name_servers" ]; then
			for nameserver in $new_domain_name_servers; do
				R="${R}nameserver $nameserver\n"
			done
		fi

		echo "$R" \
			| /sbin/resolvconf -a "${interface}".inet \
			| logger -p daemon.err -t dhclient-script
	fi
}
