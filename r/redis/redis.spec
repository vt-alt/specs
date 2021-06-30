Name: redis
Version: 6.2.4
Release: alt1

Summary: Redis is an advanced key-value store

Group: System/Libraries
License: New BSD License
URL: http://redis.io/
#URL: https://github.com/antirez/redis

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source2: redis-benchmark.1
Source3: redis-cli.1
Source4: redis-server.1
Source5: redis-cli.bash_completion
Source6: redis-server.logrotate
Source7: redis.init
Source8: redis.sysconfig
Source9: redis.service
Source10: redis-sentinel.service

Patch1: %name-6.2.3-alt-mips32.patch

# for check section
BuildPreReq: tcl >= 8.5

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: gem-power-assert glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4 tcl tk
BuildRequires: gcc-c++ git-core tcl-devel xsltproc

%description
Redis is an advanced key-value store. It is similar to memcached but
the dataset is not volatile, and values can be strings, exactly like in
memcached, but also lists, sets, and ordered sets. All this data types can
be manipulated with atomic operations to push/pop elements, add/remove
elements, perform server side union, intersection, difference between
sets, and so forth. Redis supports different kind of sorting abilities.

In order to be very fast but at the same time persistent the whole dataset
is taken in memory, and from time to time saved on disc asynchronously
(semi persistent mode) or alternatively every change is written into an
append only file (fully persistent mode). Redis is able to rebuild the
append only file in background when it gets too big.

Redis supports trivial to setup master-slave replication, with very
fast non-blocking first synchronization, auto reconnection on net split,
and so forth.

Redis is written in ANSI C and works in most POSIX systems like Linux,
*BSD, Mac OS X, Solaris, and so on. Redis is free software released under
the very liberal BSD license. Redis is reported to compile and work
under WIN32 if compiled with Cygwin, but there is no official support
for Windows currently.

%define redis_user      _redis
%define redis_group     _redis

%prep
%setup
%patch0 -p1
%patch1

sed -e 's|\$(CCOPT) \$(DEBUG) \$(OBJ)|\$(OBJ) \$(CCOPT) \$(DEBUG)|g' -i src/Makefile

%build

# For e2k - force use libc malloc instead jemalloc (see #35473)
USE_MALLOC=
%ifarch %e2k
USE_MALLOC="MALLOC=libc"
%endif

%make_build CXXFLAGS="%{optflags}" CFLAGS="%{optflags}" $USE_MALLOC

%ifndef __BTE
    # make check needs network
    make test
%endif

%install
%makeinstall_std PREFIX=%buildroot%prefix
mkdir -p %buildroot%_sbindir/
mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%_bindir/redis-server %buildroot%_sbindir/
mv %buildroot%_bindir/redis-sentinel %buildroot%_sbindir/
ln -nsf ../sbin/redis-server %buildroot%_bindir/redis-check-aof
ln -nsf ../sbin/redis-server %buildroot%_bindir/redis-check-rdb

mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

mkdir -p %buildroot%_man1dir
install -m 644 %SOURCE2 %buildroot%_man1dir/
install -m 644 %SOURCE3 %buildroot%_man1dir/
install -m 644 %SOURCE4 %buildroot%_man1dir/

# Tune default configuration
sed -e '/^timeout[[:blank:]]/ s/0/300/' \
    -e '/^daemonize[[:blank:]]/ s/no/yes/' \
    -e '/^supervised[[:blank:]]/ s/no/auto/' \
    -e '/^pidfile[[:blank:]]/ s^_6379.pid^/redis-server.pid^' \
    -e '/^logfile[[:blank:]]/ s^""^"/var/log/redis/redis-server.log"^' \
    -e '/^dir[[:blank:]]/ s^\./^/var/lib/redis^' \
    -i %name.conf
install -m644 %name.conf %buildroot%_sysconfdir/%name/
install -m644 sentinel.conf %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -m 644 %SOURCE5 %buildroot%_sysconfdir/bash_completion.d/redis-cli

mkdir -p %buildroot%_logrotatedir
install -m 640 %SOURCE6 %buildroot%_logrotatedir/redis-server

mkdir -p  %buildroot%_initdir
install -m 0755 %SOURCE7 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0640 %SOURCE8 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE9  %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE10 %buildroot%_unitdir/%name-sentinel.service

mkdir -p  %buildroot%_tmpfilesdir
echo 'd /var/run/%name 0775 root %redis_group' >> %buildroot%_tmpfilesdir/%name.conf

%pre
# Add the "_redis" user
%_sbindir/groupadd -r -f %redis_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %redis_group -c 'Redis daemon' \
        -s /dev/null -d /var/lib/redis %redis_user 2>/dev/null ||:

%post
%post_service %name
%post_service %name-sentinel

%preun
%preun_service %name
%preun_service %name-sentinel

%files
%doc COPYING 00-RELEASENOTES README.md BUGS MANIFESTO

%attr(0750,root,%redis_group) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/redis.conf
%config(noreplace) %_sysconfdir/%name/sentinel.conf

%config %_logrotatedir/redis-server
%config %_sysconfdir/bash_completion.d/redis-cli
%attr(0750,root,%redis_group) %config(noreplace) %_sysconfdir/sysconfig/%name
%config %_initdir/%name
%_unitdir/*.service
%_tmpfilesdir/%name.conf

%_bindir/redis-check-aof
%_bindir/redis-check-rdb
%_bindir/redis-cli
%_bindir/redis-benchmark
%_sbindir/redis-server
%_sbindir/redis-sentinel

%_man1dir/*

%attr(0770,root,%redis_group) %dir %_localstatedir/%name
%attr(1770,root,%redis_group) %dir %_logdir/%name


%changelog
* Mon Jun 28 2021 Nikolay A. Fetisov <naf@altlinux.org> 6.2.4-alt1
- New major version (Closes: 40279)

* Sun May 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.0.12-alt1
- New version
- Security fixes:
  + CVE-2021-21309: integer overflow on 32-bit systems
- Fix NMU: move local codebase changes to a patch

* Mon Mar 29 2021 Ivan A. Melnikov <iv@altlinux.org> 5.0.8-alt2
- Link with libatomic on %%mips32

* Tue Mar 31 2020 Nikolay A. Fetisov <naf@altlinux.org> 5.0.8-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 5.0.5-alt1
- New version
  * Fix AOF bug (possible data loss when fsync police is set to 'everysec')
  * Fix memleak in bitfieldCommand
  * Fix memleak when rewriting config file
  * Fix non critical bugs in diskless replication

* Fri May 10 2019 Nikolay A. Fetisov <naf@altlinux.org> 5.0.4-alt1
- New version
- Use libc malloc for e2k arch (Closes: 35473)

* Sun Aug 05 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.11-alt1
- New version

* Sat Jun 16 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.10-alt1
- New version
  * Fix security issues related to the Lua scripting engine
  * Fix a bug with SCAN/SSCAN/HSCAN/ZSCAN, that may not return all the elements
  * Fix a PSYNC2 bug that can affect partial resynchronization

* Sat Apr 14 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.9-alt1
- New version

* Fri Mar 02 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.8-alt1
- New version

* Sat Jan 27 2018 Nikolay A. Fetisov <naf@altlinux.org> 4.0.7-alt1
- New version

* Wed Dec 27 2017 Nikolay A. Fetisov <naf@altlinux.org> 4.0.6-alt1
- New version

* Sun Jun 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2.9-alt1
- New version

* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2.8-alt1
- New version

* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.2.6-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.2.5-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.7-alt1
- New version

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.6-alt1
- New version

* Sat Dec 19 2015 Terechkov Evgenii <evg@altlinux.org> 3.0.5-alt2.1
- Change mode of /var/log/redis to 1770 according to ALT Secure Packaging Policy

* Fri Nov 27 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.5-alt2
- Fix unit file access rights (Closes: #31545)

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.5-alt1
- New version (3.0.5)

* Wed Sep 23 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.4-alt1
- New version (3.0.4)

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.3-alt1
-  New version (3.0.3)

* Sat Jun 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.2-alt1
- New version (3.0.2): critical security issue fix

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.0.1-alt1
- New version (3.0.1)
- Fix pid file name (Closes: #30859)

* Wed Feb 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.6.10-alt1
- new version (2.6.10) (ALT #28374)
- create temporary dir

* Tue May 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.7-alt2
- add systemd unit file (ALT #27334)

* Mon Feb 13 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.7-alt1
- new version (2.4.7)

* Sun Jan 29 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.6-alt1
- new version (2.4.6) (Closes: #26869)

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.5-alt1
- new version (2.4.5) (Closes: #26782)

* Mon Oct 24 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.4.1-alt1
- new version (2.4.1) (Closes: #26496)
- adding init script
- adding logrotate script
- moving default config file to the /etc/redis/

* Fri Sep 02 2011 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt1
- new version (2.2.12) with rpmbs script (ALT bug #26131)

* Wed Apr 13 2011 Mykola Grechukh <gns@altlinux.ru> 2.2.4-alt1
- new version 2.2.4

* Tue Nov 09 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script) (ALT bug #24507)

* Sat Oct 16 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script) (ALT bug #24322)

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script) (ALT bug #24222)

* Mon Sep 13 2010 Nick S. Grechukh <gns@altlinux.ru> 2.0.1-alt1
- new stable version

* Sun Dec 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.91-alt1
- initial build for ALT Linux Sisyphus
