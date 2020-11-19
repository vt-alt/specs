# spec file for package openvpn (Version 2.3)
#

%def_with systemd
%def_with plugins
%def_with devel
%def_with syslog

%def_with management
%def_with pkcs11
%def_with http_proxy
%def_with socks
%def_with multihome
%def_with port_share
%def_with x509_alt_username

Name: openvpn
Version: 2.4.9
Release: alt1

Summary: a full-featured SSL VPN solution
Summary(ru_RU.UTF-8): полнофункциональное решение VPN на базе SSL

License: %gpl2only
Group: System/Servers
Url: http://www.openvpn.net

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-2.4.2-alt-pkcs11_pin_prompt.patch

Source1: %name.init
Source2: %name-startup
Source3: %name.sysconfig
Source4: %name.chroot.lib
Source5: %name.chroot.conf
Source6: %name.chroot.all
Source7: %name-README.ALT.utf-8
Source8: %name-server.conf
Source9: %name-client.conf
Source10: %name.tmpfiles

# Because of /etc/syslog.d/ feature
Conflicts: syslogd < 1.4.1-alt11

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Mon Nov 16 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libpkcs11-helper libssl-devel perl pkg-config python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: cmake git-core glibc-devel-static iproute2 liblz4-devel liblzo2-devel libselinux-devel net-tools

%{?_with_systemd:BuildRequires: libsystemd-devel}
%{?_with_pkcs11:BuildRequires: pkcs11-helper-devel}
%{?_with_plugins:BuildRequires: libpam-devel}


%description
OpenVPN is a full-featured SSL VPN solution which can accomodate
a wide range  of configurations,  including road warrior access,
home/office/campus  telecommuting,  WiFi security, secure branch
office  linking,  and enterprise-scale  remote access  solutions
with load balancing, failover, and fine-grained access-controls.

%description -l ru_RU.UTF-8
OpenVPN  -  полнофункциональное решение для VPN с использованием
SSL, с помощью которого можно решить широкий круг задач, включая
подключения  для удалённых  пользователей,  телекоммуникации для
дома и офиса,  безопасные  подключения  для  беспроводных сетей,
безопасную связь  с удалёнными офисами,  решения  для удалённого
доступа масштаба предприятий с поддержкой балансировки нагрузки,
отказоустойчивости и четко разграниченным контролем доступа.

%if_with plugins
%package plugins
Summary: external plugins for OpenVPN
Summary(ru_RU.UTF-8): внешние расширения для OpenVPN
Group: System/Servers
Requires: %name = %version-%release

%description plugins
OpenVPN is a full-featured SSL VPN solution.
This package contains OpenVPN plugins for user authentication
via PAM and to allow run a down script with root privileges.

%description plugins -l ru_RU.UTF-8
OpenVPN - полнофункциональное решение для VPN на базе SSL.
Данный пакет содержит расширения (plugins) для авторизации
пользователей через  PAM и  запуска при разрыве соединений
скрипта с привилегиями root.
%endif

%package docs
Summary: OpenVPN documentation
Summary(ru_RU.UTF-8): документация к OpenVPN
Group: System/Servers
Requires: %name = %version-%release
BuildArch: noarch

%description docs
OpenVPN is a full-featured SSL VPN solution.

This package contains OpenVPN documentation,
sample configs and scripts.

%description docs -l ru_RU.UTF-8
OpenVPN - полнофункциональное решение для VPN на базе SSL.

Данный пакет содержит документацию, примеры конфигурации и
скриптов для OpenVPN.

%if_with devel
%package devel
Summary: Headers for OpenVPN plugins
Group: Development/C
Requires: %name = %version-%release
BuildArch: noarch

%description devel
OpenVPN is a full-featured SSL VPN solution.

This package contains OpenVPN header file
for third-party plugin development.
%endif


%define openvpn_root   %_localstatedir/%name
%define openvpn_cache  %openvpn_root/cache
%define ovpn_user      openvpn
%define ovpn_group     openvpn

%prep
%setup -n %name-%version
%patch0 -p1

%patch1 -p1

cp -- %SOURCE7 README.ALT.utf-8
cp -- %SOURCE8 server.conf
cp -- %SOURCE9 client.conf

%build
%autoreconf

# Systemd password request utility and systemd directories:
%if_with systemd
export SYSTEMD_ASK_PASSWORD=/sbin/systemd-ask-password
export TMPFILES_DIR=%_tmpfilesdir
export SYSTEMD_UNIT_DIR=%_unitdir
cp -f -- %SOURCE10 distro/systemd/tmpfiles-openvpn.conf
%endif

%configure \
    --enable-iproute2 \
    --with-iproute-path=/sbin/ip \
    --enable-password-save \
    --enable-lzo \
    %{?_with_plugins:--enable-plugins --enable-plugin-auth-pam --enable-plugin-down-root} \
    %{?_with_management:--enable-management} \
    %{?_with_pkcs11:--enable-pkcs11} \
    %{?_with_socks:--enable-socks} \
    %{?_with_http_proxy:--enable-http-proxy} \
    %{?_with_multihome:--enable-multihome} \
    %{?_with_port_share:--enable-port-share} \
    %{?_with_x509_alt_username:--enable-x509-alt-username} \
    %{?_with_systemd:--enable-systemd} \
    %nil

%make_build
subst 's|nobody|%ovpn_user|' sample/sample-config-files/*

%if_with plugins
# Building 'simple' plugin
pushd sample/sample-plugins/simple
CPPFLAGS="${CPPFLAGS:--I../../../include}" ./build simple
mv -- simple.so %name-plugin-simple.so
popd

# Building 'defer' plugin
pushd sample/sample-plugins/defer
CPPFLAGS="${CPPFLAGS:--I../../../include}" ./build simple
mv -- simple.so %name-plugin-defer.so
popd

# Building 'log_v3' plugin
pushd sample/sample-plugins/log
CPPFLAGS='-I../../../include' ./build log_v3
mv -- log_v3.so %name-plugin-log.so
popd
%endif

%ifndef __BTE
   # make check hangs inside hasher
   make check
%endif

%install
%make_install DESTDIR=%buildroot install

# Removing automatically installed docs
rm -rf -- %buildroot%_datadir/doc/%name

# Gzip ChangeLog
gzip ChangeLog

# Configuration
install -m 0750 -d -- %buildroot%_sysconfdir/%name
install -m 0750 -d -- %buildroot%_sysconfdir/%name/keys
install -m 0750 -d -- %buildroot%_sysconfdir/%name/client
install -m 0750 -d -- %buildroot%_sysconfdir/%name/server
ln -s -- ../..%openvpn_root%_sysconfdir/%name/ccd  %buildroot%_sysconfdir/%name/ccd

# Chroot environment
install -m 0755 -d -- %buildroot%openvpn_root
install -m 0755 -d -- %buildroot%openvpn_root%_sysconfdir
install -m 0755 -d -- %buildroot%openvpn_root/%_lib
install -m 0755 -d -- %buildroot%openvpn_root%_sysconfdir/%name
install -m 0755 -d -- %buildroot%openvpn_root%_sysconfdir/%name/ccd
install -m 0755 -d -- %buildroot%openvpn_root/tmp
install -m 0755 -d -- %buildroot%openvpn_cache

# SysInit and systemd startup scripts
mkdir -p -- %buildroot/%_initdir
mkdir -p -- %buildroot/%_sysconfdir/sysconfig
install -m 0755 -- %SOURCE1 %buildroot%_initdir/%name
install -m 0750 -- %SOURCE2 %buildroot%_sysconfdir/%name
install -m 0640 -- %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

# update_chrooted files
install -p -m 0750 -D -- %SOURCE4 %buildroot%_sysconfdir/chroot.d/%name.lib
install -p -m 0750 -D -- %SOURCE5 %buildroot%_sysconfdir/chroot.d/%name.conf
install -p -m 0750 -D -- %SOURCE6 %buildroot%_sysconfdir/chroot.d/%name.all

mv -f -- COPYRIGHT.GPL COPYRIGHT.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYRIGHT.GPL) COPYRIGHT.GPL

%if_with plugins
# Install plugins
for pi in defer log simple; do
    [ -f sample/sample-plugins/$pi/README ] && \
        mv -f -- sample/sample-plugins/$pi/README sample/sample-plugins/README.$pi
    [ -x sample/sample-plugins/$pi/%name-plugin-$pi.so ] && \
        install -c -m 0755 -- sample/sample-plugins/$pi/%name-plugin-$pi.so %buildroot%_libdir/%name/plugins/%name-plugin-$pi.so
done

mkdir -- plugins
mv -f -- doc/README.plugins  plugins/README.plugins
mv -f -- sample/sample-plugins/README* plugins/
%endif

%if_with syslog
# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
mkdir -p -- %buildroot%openvpn_root/dev
/usr/bin/mksock %buildroot%openvpn_root/dev/log
mkdir -p -m700 -- %buildroot%_sysconfdir/syslog.d
ln -s -- %openvpn_root/dev/log %buildroot%_sysconfdir/syslog.d/%name
%endif

%pre
# Add the "openvpn" user
%_sbindir/groupadd -r -f %ovpn_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %ovpn_group -c 'OpenVPN daemon' \
        -s /dev/null -d /dev/null %ovpn_user 2>/dev/null ||:

%post
%_sysconfdir/chroot.d/%name.all
%post_service %name

%preun
%preun_service %name


%files
%doc AUTHORS CONTRIBUTING.rst ChangeLog.gz PORTS README COPYING
%doc README.IPv6 TODO.IPv6
%doc --no-dereference COPYRIGHT.GPL
%doc README.ALT.utf-8 server.conf client.conf
%if_with management
%doc doc/management-notes.txt
%endif

%_sbindir/%name
%_mandir/man?/*

%attr(0750,root,%ovpn_group) %dir %_sysconfdir/%name
%attr(0750,root,%ovpn_group) %dir %_sysconfdir/%name/keys
                                  %_sysconfdir/%name/ccd
%attr(0750,root,%ovpn_group) %dir %_sysconfdir/%name/client
%attr(0750,root,%ovpn_group) %dir %_sysconfdir/%name/server
%attr(0750,root,%ovpn_group) %dir %openvpn_root
                             %dir %openvpn_root/etc
                             %dir %openvpn_root/etc/openvpn
                             %dir %openvpn_root/etc/openvpn/ccd
%attr(0770,root,%ovpn_group) %dir %openvpn_root/tmp
                             %dir %openvpn_root/%_lib
%attr(0750,%ovpn_user,%ovpn_group) %dir %openvpn_cache

%config(noreplace)  %_sysconfdir/%name/%name-startup
%config(noreplace)  %_sysconfdir/sysconfig/%name
%config             %_sysconfdir/chroot.d/%name.*
%config             %_initdir/%name

%if_with systemd
%_unitdir/%name-*.service
%_tmpfilesdir/%name.conf
%endif

%if_with syslog
%attr(0710,root,%ovpn_group) %dir %openvpn_root/dev
%ghost %attr(0666,root,root)      %openvpn_root/dev/log

%_sysconfdir/syslog.d/%name
%endif


%if_with plugins
%files plugins
%doc plugins/*
%doc src/plugins/*/README.*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
     %_libdir/%name/plugins/%name-*.so
%exclude %_libdir/%name/plugins/%name-*.la
%endif

%files docs
%doc INSTALL
%doc sample/sample-config-files*
%doc sample/sample-keys*
%doc sample/sample-scripts*

%if_with devel
%files devel

%_includedir/openvpn-plugin.h
%_includedir/openvpn-msg.h
%endif

%changelog
* Mon Nov 16 2020 Nikolay A. Fetisov <naf@altlinux.org> 2.4.9-alt1
- New version
- Security fixes:
  + CVE-2020-11810: race condition allowes one client kills other
    client session via false client floating (Closes: 39122)

* Fri May 31 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.7-alt2
- Dropped BR: libssl10.

* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.4.7-alt1
- New version
- Use system liblz4 (thanks Mikhail Efremov, @sem) (Closes: 36389)

* Thu Sep 06 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.4.6-alt2
- Rebuild with openssl 1.1.0i

* Thu May 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.4.6-alt1
- New version

* Sun Mar 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.4.5-alt1
- New version
- Updating patch for PKCS11 PIN prompt bug

* Sat Nov 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.4.4-alt1
- New version
- Security fixes:
  +  CVE-2017-12166: Buffer overflow when using (obsolete) '--key-method 1'

* Wed Jun 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.4.3-alt1
- New version
- Security fixes:
  + CVE-2017-7522 Post-authentication --x509-track remote DoS
  + CVE-2017-7521 Post-authentication remote-triggerable memory leaks
  + CVE-2017-7521 Potential post-authentication remote code execution
                  on servers that use the --x509-username-field option
  + CVE-2017-7520 Pre-authentication remote crash / information disclosure
                  for clients
  + CVE-2017-7508 Remotely-triggerable ASSERT() on malformed IPv6 packet
- Force to use built-in PIN prompt with PKCS11 regardless
  of systemd presence (OpenVPN bug 538)

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.4.2-alt1
- New version
- Security fixes:
  + CVE-2017-7478  Don't assert out on receiving too-large control packets
  + CVE-2017-7479  Drop packets instead of assert out if packet id rolls over

* Thu Mar 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.4.1-alt1
- New version

* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.4.0-alt1
- New version
- Adding /dev/urandom into chroot (Closes: 32840)

* Fri Sep 09 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.12-alt1
- New version
- Creating PID directory for the systemd units (Closes: 31145)
- Adding openvpn-devel subpackage with header file (Closes: 31085)
- Adding /etc/openvpn/{client,server}/ dirs for systemd units
- Enabling support for systemd-ask-password utility (Closes: 32204)

* Fri Jun 12 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.7-alt1
- New version 2.3.7

* Thu Jan 15 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.6-alt1
- New version 2.3.6
- CVE-2014-8104 (Closes: 30529)
- Adding pkcs11 support (Closes: 30614)
- Adding systemd service files (Closes: 28071)

* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.2.2-alt1
- New version 2.2.2

* Thu Jun 23 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.2.0-alt1
- New version 2.2.0

* Mon Nov 29 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.4-alt1
- New version 2.1.4

* Sat Oct 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.3-alt1
- New version 2.1.3
- Removing bashisms from the init.d script

* Thu Dec 31 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.1-alt1
- New version 2.1.1 (Closes: 19934)
- Disabling service by default (Closes: 17218)
- Building with liblzo2
- Fixing Requies/Obsoletes

* Thu Jun 04 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.9-alt2
- Adding 'lladdr' support (thanks Mykola S. Grechukh, (gns@))
- Adding LSB header into init.d script

* Wed Apr 18 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.9-alt1
- New version 2.0.9
-- Fix some issues in Windows-related code
- Adding lib64/ in chroot environment (#10164)
- Adding note to README.ALT about #11016
- Spec file cleanup

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.8-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.8-alt1
- New version 2.0.8
-- Fix in Windows installer, no changes into source code
- Fix small mistakes in README.ALT

* Fri Sep 01 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.7-alt1
- New version 2.0.7
-- small bugfixes
- Fix typos in openvpn.init (#9870)
- Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature (#9945)
- Move documentation to separate package openvpn-docs
- Sample config files with ALT Linux specific comments added (#9367)

* Sat Apr 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.6-alt2
- Fix init.d script for run openvpn-startup/openvpn-shutdown scripts
- Plugins packed to separate package openvpn-plugins.

* Mon Apr 06 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.6-alt1
- New version 2.0.6
-- Security fixes for CVE-2005-3393, CVE-2005-3409, CVE-2006-1629
-- several minor bug fixes and improvements, see ChangeLog for details
- Adding README.ALT
- Updating init.d script
- Building and packaging plugins

* Thu Aug 25 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.2-alt1
- New version 2.0.2:
  -- Security fix for several DoS attacks: CAN-2005-2531; CAN-2005-2532;
     CAN-2005-2533; CAN-2005-2534.
  -- Several minor bug fixes and improvements, see ChangeLog for details
- Run in chroot by default

* Wed Apr 27 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.0-alt1
- First build for Sisyphus

* Fri Apr 22 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.0-alt0
- First build of 2.0 release

* Mon Jan 10 2005 - Nikolay A. Fetisov <naf@nat.net.ru> 1.0.3-naf1.rc6
- Updating to version 2.0_rc6

* Sun Dec 26 2004 - Nikolay A. Fetisov <naf@nat.net.ru> 1.0.3-naf1
- Initial build
