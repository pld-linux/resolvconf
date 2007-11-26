Summary:	nameserver information handler
Name:		resolvconf
Version:	1.37
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.debian.org/debian/pool/main/r/resolvconf/%{name}_%{version}.tar.gz
# Source0-md5:	d6aec9e204674de97b272384305eb320
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Resolvconf is a framework for keeping track of the system's
information about currently available nameservers. It sets itself up
as the intermediary between programs that supply nameserver
information and applications that need nameserver information.

%prep
%setup -q
iconv -fKOI8R -tutf8 < man/interface-order.ru.5 > man/interface-order.ru-utf8.5
iconv -fKOI8R -tutf8 < man/resolvconf.ru.8  > man/resolvconf.ru-utf8.8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/%{name},%{_sbindir},%{_mandir}/{ru/,}man{5,8}}
cp -a etc/* $RPM_BUILD_ROOT%{_sysconfdir}
install bin/resolvconf $RPM_BUILD_ROOT%{_sbindir}
install bin/list-records $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a man/interface-order.5 $RPM_BUILD_ROOT%{_mandir}/man5
cp -a man/resolvconf.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -a man/interface-order.ru-utf8.5 $RPM_BUILD_ROOT%{_mandir}/ru/man5/interface-order.5
cp -a man/resolvconf.ru-utf8.8 $RPM_BUILD_ROOT%{_mandir}/ru/man8/resolvconf.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/resolvconf
%dir %{_libdir}/resolvconf
%attr(755,root,root) %{_libdir}/resolvconf/list-records
%dir %{_sysconfdir}/resolvconf
%dir %{_sysconfdir}/resolvconf/resolv.conf.d
%dir %{_sysconfdir}/resolvconf/update.d
%{_sysconfdir}/resolvconf/interface-order
%{_sysconfdir}/resolvconf/resolv.conf.d/base
%{_sysconfdir}/resolvconf/resolv.conf.d/head
%{_sysconfdir}/resolvconf/update.d/bind
%{_sysconfdir}/resolvconf/update.d/dnscache
%{_sysconfdir}/resolvconf/update.d/libc
%{_mandir}/man5/interface-order.5*
%{_mandir}/man8/resolvconf.8*
%lang(ru) %{_mandir}/ru/man5/interface-order.5*
%lang(ru) %{_mandir}/ru/man8/resolvconf.8*
