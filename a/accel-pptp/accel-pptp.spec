%define ppp_ver %((%{__awk} '/^#define VERSION/ { print $NF }' /usr/include/pppd/patchlevel.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')

Name: accel-pptp
Version: 0.8.5
Release: alt3
Summary: PPTP VPN plugin for pppd
License: GPLv2
Group: System/Servers
Url: http://accel-pptp.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: ppp = %ppp_ver

Source0: %name-%version.tar.bz2
Patch0: %name-%version-alt-make.patch

BuildRequires: ppp-devel

%description
The  PPTP  plugin for pppd performs interaction with pptp kernel module
and has built-in call manager (client part of PPTP).  It pasees  neces-
sary  paremeters  from options into kernel module to configure ppp-pptp
channel. If it runs in client  mode,  then  additionally  call  manager
starts up. PPTPD daemon automaticaly invokes this plugin in server mode
and passes  necessary  options,  so  additional  configuration  is  not
needed.

%prep
%setup
%patch0 -p1

%build
cd pppd_plugin
%autoreconf
%configure \
	--disable-static

%make_build

%install
cd pppd_plugin
%make DESTDIR=%buildroot install

%files
%_libdir/pppd/%ppp_ver/*.so
%_man8dir/*.8*

%changelog
* Tue Mar 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.5-alt3
- rebuild with ppp 2.4.8

* Mon Jan 19 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt2
- rebuild with ppp 2.4.7

* Thu Jan 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt1
- initial release

