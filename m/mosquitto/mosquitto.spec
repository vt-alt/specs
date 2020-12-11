%define mosquitto_user      mosquitto
%define mosquitto_group     mosquitto
%define lname     libmosquitto

Name: mosquitto
Version: 1.6.9
Release: alt1

Summary: Mosquitto is an open source implementation of a server for version 3.1 and 3.1.1 of the MQTT protocol

License: This project is dual licensed under the Eclipse Public License 1.0 and the Eclipse Distribution License 1.0 as described in the epl-v10 and edl-v10 files
Group: Development/C++
Url: http://mosquitto.org

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: http://mosquitto.org/files/source/%name-%version.tar.gz
Source: %name-%version.tar
Source1: %name
Source2: %name.sysconf
Source3: %name.conf

# Automatically added by buildreq on Mon Feb 01 2016
# optimized out: libcom_err-devel libkrb5-devel libstdc++-devel
BuildRequires: gcc-c++ libcares-devel libssl-devel libuuid-devel docbook-style-xsl xsltproc
Requires: %lname = %version-%release

%description
The Mosquitto project has been created to provide a light weight, open-source
implementation, of an MQTT broker to allow new, existing, and emerging
applications for Machine-to-Machine (M2M) and Internet of Things (IoT).

%package -n %lname
Group: Development/C
Summary: Libraries for mosquitto

%description -n %lname
Libraries for mosquitto

%package -n %lname-devel
Group: Development/C
Summary: Libraries needed to develop for mosquitto
Requires: %lname = %version-%release
Obsoletes: %name-devel

%description -n %lname-devel
Libraries needed to develop for mosquitto

%prep
%setup 

subst 's|Invalid memory_limit value (%%ld)|Invalid memory_limit value (%%zd)|g' src/conf.c

%build
subst 's|prefix?=/usr/local|prefix=/usr|g' config.mk
subst 's|stylesheet/docbook-xsl/manpages/docbook.xsl|xsl-stylesheets/manpages/docbook.xsl|g' man/manpage.xsl man/html.xsl
%make_build

%install
export LIB_SUFFIX='%_libsuff'
%makeinstall_std

chmod a-x %buildroot%_includedir/*.h

mkdir -p %buildroot/%_initdir
cp %SOURCE1 %buildroot%_initdir/

mkdir -p %buildroot/%_sysconfdir/sysconfig
cp %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot/%_sysconfdir/%name
cp %SOURCE3 %buildroot%_sysconfdir/%name

%pre
%_sbindir/groupadd -r -f %mosquitto_group 2>/dev/null ||:
%_sbindir/useradd -M -r -g %mosquitto_group -c 'Mosquitto daemon' -s /dev/null -d /dev/null %mosquitto_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name
        
%files
%dir %_sysconfdir/%name
%config %dir %_sysconfdir/%name/*
%config %_sysconfdir/sysconfig/%name
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man3dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*
%_initdir/*

%files -n %lname
%_libdir/*.so.*

%files -n %lname-devel
%_includedir/*.h
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.9-alt1
- Updated to upstream version 1.6.9 (Fixes: CVE-2019-11778, CVE-2019-11779).

* Mon Jun 24 2019 Pavel Vainerman <pv@altlinux.ru> 1.6.3-alt1
- new version (1.6.3) with rpmgs script

* Wed Apr 24 2019 Pavel Vainerman <pv@altlinux.ru> 1.6.0-alt1
- new version (1.6.0) with rpmgs script

* Tue Apr 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.6-alt2
- Fixed build on other architectures with %%_lib != lib.

* Mon Feb 11 2019 Pavel Vainerman <pv@altlinux.ru> 1.5.6-alt1
- new version (1.5.6) with rpmgs script
- fix CVE-2018-12551, CVE-2018-12550, CVE-2018-12546

* Sun Nov 25 2018 Pavel Vainerman <pv@altlinux.ru> 1.5.4-alt1
- new version (1.5.4) with rpmgs script

* Thu Sep 27 2018 Pavel Vainerman <pv@altlinux.ru> 1.5.3-alt1
- new version (1.5.3) with rpmgs script
- fix CVE-2018-12543

* Fri Sep 07 2018 Pavel Vainerman <pv@altlinux.ru> 1.5.1-alt2
- fix libdir for build for x86_64

* Sun Aug 26 2018 Pavel Vainerman <pv@altlinux.ru> 1.5.1-alt1
- new version (1.5.1) with rpmgs script

* Thu Jan 25 2018 Pavel Vainerman <pv@altlinux.ru> 1.4.14-alt1
- new version (1.4.14) with rpmgs script
- add LSB headers to init-scipt
- fix bug #34480

* Thu Jun 01 2017 Pavel Vainerman <pv@altlinux.ru> 1.4.12-alt1
- new version (1.4.12) with rpmgs script

* Sat Feb 25 2017 Pavel Vainerman <pv@altlinux.ru> 1.4.11-alt2
- up build

* Fri Feb 24 2017 Pavel Vainerman <pv@altlinux.ru> 1.4.11-alt1
- new version (1.4.11) with rpmgs script

* Fri Sep 30 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.10-alt1
- build new version

* Tue Jun 21 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.9-alt1
- build new version

* Mon Mar 07 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.8-alt2
- make libmosquitto and libmosquitto-devel packages

* Sat Feb 20 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.8-alt1
- build new version (ChangeLog.txt):
Broker:
- Wills published by clients connected to a listener with mount_point defined
  now correctly obey the mount point. This was a potential security risk
  because it allowed clients to publish messages outside of their restricted
  mount point. This is only affects brokers where the mount_point option is in
  use. Closes #487178.
- Fix detection of broken connections on Windows. Closes #485143.
- Close stdin etc. when daemonised. Closes #485589.
- Fix incorrect detection of FreeBSD and OpenBSD. Closes #485131.

Client library:
- mosq->want_write should be cleared immediately before a call to SSL_write,
  to allow clients using mosquitto_want_write() to get accurate results.

* Mon Feb 08 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt4
- set default bind address 'localhost'

* Mon Feb 08 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt3
- remove /var/lib/mosquitto (not used)

* Mon Feb 08 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt2
- fixed homepage in spec
- set home to /dev/null for mosquitto user

* Sun Feb 07 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt1
- fixed header files attributes
- add service file for init.d
- create mosquitto_user and group 
- add sysconfig/mosquitto

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt0.4
- test build for x86_64

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt0.3
- test build

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt0.2
- initial build
