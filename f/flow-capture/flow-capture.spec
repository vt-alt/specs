%define name flow-capture
%define flowdir %_logdir/%name
%define piddir /run/%name
%define fuser _flow

Name: %name
Version: 0.1
Release: alt3

Summary: Flow-capture in Netflow collector program
License: GPL-2.0-or-later
Group: Monitoring
Source0: %name.init
Source1: %name.sysconfig

BuildArch: noarch

Provides: flow-capture-collector
Requires: flow-tools su

%description
Flow-capture in Netflow collector program.

NOTE: This package DOES NOT contain flow-capture binary itself (it
belong to flow-tools package). This package contain addition componets
(SySV init script and config), to enable you gather netflow statistics
with some netflow sensor (ipcad, fprobe or other).

This daemon will be run by %fuser user.

%prep

%build
%install
mkdir -p %buildroot%_initdir
install %SOURCE0 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig
install %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%flowdir
mkdir -p %buildroot%piddir

# create tmpfiles config
mkdir -p %buildroot%_tmpfilesdir
cat >%buildroot%_tmpfilesdir/%name.conf<<END
d %piddir 1775 root %fuser -
END

%pre
/usr/sbin/useradd -r -d %flowdir -s /dev/null %fuser >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr (1775,root,%fuser) %flowdir
#dir %attr (1775,root,%fuser) %piddir
%_tmpfilesdir/%name.conf

%changelog
* Mon Dec 16 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt3
- Add lsb-header for init script
- replace /var/run to /run
- create tmpfiles config
- change license GPL-2.0-or-later

* Sat Dec  1 2007 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt2.2
- Dir permission fixed according policy (see http://docs.altlinux.ru/alt/devel/ch01s03.html#id2884290)

* Tue Nov 20 2007 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt2.1
- Requires to "su" added (See #11359, #13439)
- spec macro abuse cleanup

* Tue Jun 12 2007 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt2
- Startup race with fprobe-ulog fixed

* Mon Sep 25 2006 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt1
- Build for Sisyphus
- Running from pseudouser

* Mon Aug 21 2006 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt0.C30.1
- Initial build for C30
