%def_enable seccomp
%def_enable extstore
%def_enable sasl
%def_enable tls

Name: memcached
Version: 1.6.6
Release: alt1

Summary: memcached - memory caching daemon
License: BSD
Group: System/Servers
Url: http://www.memcached.org/
#https://github.com/memcached/memcached.git
Source: %name-%version.tar
Patch: %name-%version.patch

%define pkg_user memcached
%define pkg_group memcached

BuildRequires: libevent-devel perl-devel perl-AnyEvent perl-YAML perl-Term-ReadKey perl-IO-Socket-SSL
%{?_enable_seccomp:BuildRequires: libseccomp-devel}
%{?_enable_sasl:BuildRequires: libsasl2-devel}
%{?_enable_tls:BuildRequires: libssl-devel >= 1.1.0}

%description
memcached is a flexible memory object caching daemon designed to  alle-
viate  database  load in dynamic web applications by storing objects in
specifically  optimized  to  avoid swapping and always use non-blocking
I/O.

%package devel
Summary: Files needed for development using memcached protocol
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description devel
This package contains files needed for development using memcached
protocol.

%package tool
Summary: Stats and management tool for memcached
Group: Development/Tools
BuildArch: noarch

%description tool
memcached-tool is a Perl script used to print statistics from a running
memcached instance.

%prep
%setup
%patch -p1
sed -i 's,`git describe`,"%version-%release",g' version.pl

%build
perl version.pl
%autoreconf
%configure \
	%{subst_enable seccomp} \
	%{subst_enable extstore} \
	%{subst_enable sasl} \
	%{subst_enable tls}

%make_build

%install
%makeinstall_std
install -pD -m755 %name.init %buildroot%_initdir/%name
install -pD -m640 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pD -m644 %name.service %buildroot%_unitdir/%name.service
install -pD -m644 %{name}@.service %buildroot%_unitdir/%{name}@.service

# tool
install -pD -m755 scripts/memcached-tool %buildroot%_bindir/memcached-tool
install -pD -m644 scripts/memcached-tool.1 %buildroot%_man1dir/memcached-tool.1

%check
%make test ||:

%pre
%_sbindir/groupadd -r -f %pkg_group
%_sbindir/useradd -r -g %pkg_group -d /dev/null -s /dev/null -n %pkg_user \
	2> /dev/null > /dev/null ||:
if [ $1 -eq 2 ] && [ ! -f /var/run/%name/%name.pid ] && [ -f /var/run/%name.pid ]; then
   mkdir /var/run/%name/
   mv /var/run/%name.pid /var/run/%name/%name.pid
fi

%post
%post_service %name

%preun
%preun_service %name

%files
%config(noreplace) %attr(640,root,adm) %_sysconfdir/sysconfig/%name
%_bindir/%name
%_man1dir/%name.*
%_initdir/*
%_unitdir/*
%doc AUTHORS doc/CONTRIBUTORS ChangeLog NEWS README.md doc/*.txt

%files devel
%_includedir/*

%files tool
%_bindir/%name-tool
%_man1dir/%name-tool.*

%changelog
* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.6-alt1
- new version 1.6.6

* Sat Apr 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.5-alt1
- new version 1.6.5

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.3-alt1
- new version 1.6.3

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt1
- new version 1.6.2 (ALT #38273)

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- new version 1.6.1.
- enable extstore

* Sun Feb 09 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.22-alt1
- new version 1.5.22

* Sat Jan 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.21-alt1
- new version 1.5.21

* Fri Oct 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.19-alt1
- new version 1.5.19

* Tue Sep 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.17-alt1
- new version 1.5.17

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.16-alt1
- 1.5.16

* Thu May 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.14-alt2
- Fixed build on ppc64le.

* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.14-alt1
- 1.5.14

* Thu Apr 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.13-alt1
- 1.5.13
- build with tls support

* Thu Nov 29 2018 Alexey Shabalin <shaba@altlinux.org> 1.5.12-alt1
- 1.5.12

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 1.5.10-alt1
- 1.5.10

* Fri Jul 27 2018 Alexey Shabalin <shaba@altlinux.org> 1.5.9-alt1
- 1.5.9

* Sun Apr 01 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.7-alt1
- 1.5.7

* Sun Mar 04 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.6-alt1
- 1.5.6
- disable UDP port by default (fixed CVE-2018-1000115)
- drop scripts package
- add tool package
- add memcached@.service for allow start "instanced" version, like 'memcached@11211'

* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Tue Nov 07 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.3-alt1
- 1.5.3
- build with sasl

* Thu Nov 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2
- build with seccomp

* Thu Jul 20 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.39-alt1
- 1.4.39

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.37-alt1
- 1.4.37

* Wed Mar 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.36-alt1
- 1.4.36

* Mon Feb 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.35-alt1
- 1.4.35

* Mon Feb 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.34-alt1
- 1.4.34

* Wed Nov 02 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.33-alt1
- 1.4.33
- fixed CVE-2016-8705,CVE-2016-8704,CVE-2016-8706
- update systemd unit

* Wed Jun 15 2016 Lenar Shakirov <snejok@altlinux.ru> 1.4.13-alt4
- Systemd unit file fixed

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.13-alt3.1
- Fixed build

* Tue May 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.13-alt3
- Fix systemd unit file (ALT #27335)

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.13-alt2
- Add systemd unit file

* Mon Mar 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.13-alt1
- 1.4.13

* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.10-alt1
- 1.4.10

* Mon Sep 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Mon Jun 27 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt6
- Packaged auxiliary scripts in separate subpackage.

* Thu Jun 16 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt5
- Fixed lowering privileges and pidfile writing.
- Rewritten startup script.
- Replaced /etc/memcached.conf with /etc/sysconfig/memcached
- Packaged %name-devel as noarch.

* Tue Jun 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt4
- fix VERSION UNKNOWN error

* Mon Mar 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt3
- Add memcached package to devel's Requires (ALT #25264)

* Mon Nov 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt2
- Fix type-punning issues exposed with GCC 4.5.1

* Wed Oct 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt1
- 1.4.5 (ALT #23996)
- CVE-2010-1152

* Mon Sep 28 2009 Denis Klimov <zver@altlinux.org> 1.4.1-alt1
- new version (Closes: #20835)
- add devel subpackage

* Tue May 05 2009 Denis Klimov <zver@altlinux.org> 1.2.8-alt1
- new version
- critial bug fix leak memory from /proc/self/maps (ALT #19916)
- remove packager tag
- not package needless scripts

* Fri Aug 08 2008 Denis Klimov <zver@altlinux.org> 1.2.6-alt1
- new version
- remove needless -q key for setup macros
- fix use pkg_group instead pkg_user
- remove include sysconfig file in init script

* Sat Jun 02 2007 L.A. Kostis <lakostis@altlinux.ru> 1.2.2-alt1
- new version from 1.2 branch (fix ALT #11932).
- build with threads support.
- add packager field.
- add debug switch for testing purposes (disabled by default).

* Wed Nov 02 2005 LAKostis <lakostis@altlinux.ru> 1.1.12-alt1
- first build for ALTLinux.

