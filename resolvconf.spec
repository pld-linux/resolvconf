Summary:	nameserver information handler
Name:		resolvconf
Version:	1.37
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.debian.org/debian/pool/main/r/resolvconf/%{name}_%{version}.tar.gz
# Source0-md5:	d6aec9e204674de97b272384305eb320
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_sbindir}}
cp -a etc/* $RPM_BUILD_ROOT%{_sysconfdir}
install bin/resolvconf $RPM_BUILD_ROOT%{_sbindir}
install bin/list-records $RPM_BUILD_ROOT%{_libdir}/resolvconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/resolvconf
%attr(755,root,root) %{_sbindir}/resolvconf
%dir %{_sysconfdir}/resolvconf
%dir %{_sysconfdir}/resolvconf/resolv.conf.d
%dir %{_sysconfdir}/resolvconf/update.d
%{_sysconfdir}/resolvconf/interface-order
%{_sysconfdir}/resolvconf/resolv.conf.d/base
%{_sysconfdir}/resolvconf/resolv.conf.d/head
%{_sysconfdir}/resolvconf/update.d/bind
%{_sysconfdir}/resolvconf/update.d/dnscache
%{_sysconfdir}/resolvconf/update.d/libc
