Summary:	Nameserver information handler
Summary(pl.UTF-8):	Program obsługujący informacje o serwerach nazw
Name:		resolvconf
Version:	1.43
Release:	5
License:	GPL v2
Group:		Base
Source0:	http://ftp.debian.org/debian/pool/main/r/resolvconf/%{name}_%{version}.tar.gz
# Source0-md5:	15faef2aba7b99782f3b0b8b5d30f80a
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}-dhclient-enter-hook.sh
Source4:	%{name}-dhclient-exit-hook.sh
Patch0:		%{name}-pld.patch
Patch1:		resolv.conf-mode.patch
Requires:	dhcp-client-dirs
Requires:	rc-scripts >= 0.4.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir			/lib

%description
Resolvconf is a framework for keeping track of the system's
information about currently available nameservers. It sets itself up
as the intermediary between programs that supply nameserver
information and programs that use nameserver information.

%description -l pl.UTF-8
resolvconf to narzędzie do śledzenia informacji systemu o aktualnie
dostępnych serwerach nazw. Program wstawia się jako pośrednik między
programami dostarczającymi informacje o serwerach nazw a programami
wykorzystującymi te informacje.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
touch etc/resolvconf/resolv.conf.d/tail

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig,rc.d/init.d},%{_sysconfdir}/%{name}/run/interface,%{_libdir}/%{name},%{_sbindir},%{_mandir}/{ru/,}man{5,8}}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/dhclient-enter-hooks.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/dhclient-exit-hooks.d

cp -a etc/%{name}/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p bin/resolvconf $RPM_BUILD_ROOT%{_sbindir}
install -p bin/list-records $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a man/interface-order.5 $RPM_BUILD_ROOT%{_mandir}/man5
cp -a man/resolvconf.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install -p %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/dhclient-enter-hooks.d/resolvconf
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/dhclient-exit-hooks.d/resolvconf
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/run/resolv.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/run/enable-updates

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/resolvconf
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %{_libdir}/resolvconf
%attr(755,root,root) %{_libdir}/resolvconf/list-records
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/resolv.conf.d
%dir %{_sysconfdir}/%{name}/update.d
%dir %{_sysconfdir}/%{name}/update-libc.d
%dir %{_sysconfdir}/%{name}/run
%dir %{_sysconfdir}/%{name}/run/interface
%ghost %{_sysconfdir}/%{name}/run/resolv.conf
%ghost %{_sysconfdir}/%{name}/run/enable-updates
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/interface-order
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/resolv.conf.d/base
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/resolv.conf.d/head
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/resolv.conf.d/tail
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dhclient-enter-hooks.d/resolvconf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dhclient-exit-hooks.d/resolvconf
%attr(755,root,root) %{_sysconfdir}/%{name}/update.d/bind
%attr(755,root,root) %{_sysconfdir}/%{name}/update.d/dnscache
%attr(755,root,root) %{_sysconfdir}/%{name}/update.d/libc
%{_mandir}/man5/interface-order.5*
%{_mandir}/man8/resolvconf.8*
