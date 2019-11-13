%define dbus_user      messagebus
%define dbus_group     messagebus

%define system_socket_dir /run/dbus
%define session_socket_dir %system_socket_dir/users
%define system_socket %system_socket_dir/system_bus_socket
%define	systemdsystemunitdir /lib/systemd/system
%define systemdsessionunitdir %_prefix/lib/systemd/user

Name: dbus
Version: 1.12.16
Release: alt2

Summary: D-BUS is a simple IPC framework based on messages.
License: AFL/GPL
Group: System/Servers
Url: http://www.freedesktop.org/Software/dbus

Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: shadow-utils
Requires: lib%name = %version-%release

BuildRequires: autoconf-archive doxygen gcc-c++ libexpat-devel libSM-devel libX11-devel xmlto libselinux-devel libaudit-devel libcap-ng-devel
BuildRequires: libsystemd-daemon-devel libsystemd-login-devel libsystemd-journal-devel

Source: %name-%version.tar
Patch: %name-%version.patch

%description
D-BUS is a system for low-latency, low-overhead, easy to use interprocess
communication (IPC). In more detail:

  o D-BUS is low-latency because it is designed to avoid round trips and
    allow asynchronous operation, much like the X protocol.

  o D-BUS is low-overhead because it uses a binary protocol, and does not
    have to convert to and from a text format such as XML. Because D-BUS is
    intended for potentially high-resolution same-machine IPC, not primarily
    for Internet IPC, this is an interesting optimization.

  o D-BUS is easy to use because it works in terms of messages rather than
    byte streams, and automatically handles a lot of the hard IPC issues.
    Also, the D-BUS library is designed to be wrapped in a way that lets
    developers use their framework's existing object/type system, rather
    than learning a new one specifically for IPC.

This package contains D-BUS daemon and system utilities.

%package tools
Summary: D-BUS user helper tools
Group: Monitoring
Requires: %name = %version-%release
Provides: dbus-userhelpers = %version-%release
Obsoletes: dbus-userhelpers

%description tools
This package includes user tools for launching D-BUS service on session startup

%package tools-gui
Summary:  D-BUS user helper tools
Group: Monitoring
Requires: %name = %version-%release

%description tools-gui
This package includes user tools for launching D-BUS service on session startup

%package -n lib%name
Summary: D-BUS shared libraries
Group: System/Libraries

%description -n lib%name
This package contains D-BUS shared libraries

%package -n lib%name-devel
Summary: D-BUS development files
Group: Development/C
Requires: lib%name = %version-%release
%description -n lib%name-devel
This package contains D-BUS development files (headers and libraries links)

%add_findreq_skiplist %_x11sysconfdir/xinit.d/*

%prep
%setup -q
%patch -p1

mkdir -p m4
sed -i 's|@CODE_COVERAGE_RULES@|#CODE_COVERAGE_RULES#|' $(find -name Makefile.am)

%build
%autoreconf
%configure \
	--disable-tests \
	--disable-asserts \
	--enable-xml-docs \
	--enable-doxygen-docs \
	--enable-inotify \
	--enable-libaudit \
	--enable-selinux \
	--enable-systemd \
	--enable-user-session \
	--bindir=/bin \
	--libexecdir=/lib/dbus-1 \
	--with-system-pid-file=/run/messagebus.pid \
	--with-system-socket=%system_socket \
	--with-session-socket-dir=%session_socket_dir \
	--with-systemdsystemunitdir=%systemdsystemunitdir \
	--localstatedir=%_var \
	--disable-static

%make_build

doxygen Doxyfile

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot/{%_lib,%_bindir}
for f in %buildroot%_libdir/lib*.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/
ln -sf ../../bin/dbus-launch %buildroot%_bindir/dbus-launch
ln -sf ../../bin/dbus-send %buildroot%_bindir/dbus-send
ln -sf dbus.service %buildroot/lib/systemd/system/messagebus.service

install -pD -m0755 bus/messagebus.in %buildroot%_initdir/messagebus

cp -a doc/api/html api

mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
mkdir -p %buildroot%_sysconfdir/dbus-1/session.d
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%system_socket_dir
mkdir -p %buildroot%session_socket_dir
mkdir -p %buildroot%_localstatedir/dbus
touch %buildroot%_localstatedir/dbus/machine-id
touch %buildroot%_sysconfdir/machine-id

mkdir -p %buildroot/lib/tmpfiles.d
cat << __EOF__ > %buildroot/lib/tmpfiles.d/%name.conf
d /run/dbus 0755 root root -
d /run/dbus/users 1777 root root -
__EOF__

%pre
%_sbindir/groupadd -r -f %dbus_group 2> /dev/null ||:
%_sbindir/useradd -r -n -g %dbus_group -d %system_socket_dir -s /dev/null -c "D-Bus System User" %dbus_user 2> /dev/null ||:

%post
if [ $1 -eq 1 ] ; then
	/sbin/chkconfig --add messagebus
else
	/sbin/chkconfig messagebus resetpriorities
fi
/bin/dbus-uuidgen --ensure

%preun
%preun_service messagebus

%files
%dir %_sysconfdir/dbus-1
%config(noreplace) %_sysconfdir/dbus-1/*.conf
%dir %_sysconfdir/dbus-1/system.d
%dir %_sysconfdir/dbus-1/session.d
%ghost %_sysconfdir/machine-id
%_initdir/messagebus
%systemdsystemunitdir/*
%systemdsessionunitdir/*
/lib/tmpfiles.d/%name.conf
/bin/dbus-cleanup-sockets
/bin/dbus-daemon
/bin/dbus-uuidgen
/bin/dbus-run-session
/bin/dbus-update-activation-environment
%dir /lib/dbus-1
%attr(4510,root,messagebus) /lib/dbus-1/dbus-daemon-launch-helper
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/system.d
%dir %_datadir/dbus-1/session.d
%dir %_datadir/dbus-1/services
%dir %_datadir/dbus-1/system-services
%_datadir/dbus-1/session.conf
%_datadir/dbus-1/system.conf
#attr(0755,root,root) #dir #system_socket_dir
#attr(1777,root,root) #dir #session_socket_dir
%dir %_localstatedir/dbus
%ghost %_localstatedir/dbus/machine-id
%_man1dir/dbus-cleanup-sockets.1*
%_man1dir/dbus-daemon.1*
%_man1dir/dbus-uuidgen.1*
%_man1dir/dbus-run-session.1*
%_man1dir/dbus-update-activation-environment.1*

%files tools
/bin/dbus-send
/bin/dbus-monitor
%_bindir/dbus-send
%_man1dir/dbus-send.1*
%_man1dir/dbus-monitor.1*

%files tools-gui
%_sysconfdir/X11/xinit.d/*
/bin/dbus-launch
%_bindir/dbus-launch
%_man1dir/dbus-launch.1*

%files -n lib%name
/%_lib/libdbus-1.so.*

%files -n lib%name-devel
/bin/dbus-test-tool
%_datadir/doc/%name
%_includedir/dbus-1.*
%_libdir/libdbus-1.so
%_libdir/dbus-1.*
%_libdir/cmake/DBus1
%_pkgconfigdir/dbus-1.pc
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/interfaces
%_datadir/xml/dbus-1
%_man1dir/dbus-test-tool.1*

%changelog
* Mon Nov 11 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.12.16-alt2
- removed reload during package update (closes: #37461)

* Wed Nov 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.12.16-alt1
- 1.12.16 (Fixes: CVE-2019-12749)

* Mon Feb 11 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.12.12-alt2
- fixed build with new autoconf-archive-2019.01.06

* Wed Dec 05 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.12.12-alt1
- 1.12.12
- syslog is not required in initscript (closes: #35689)

* Wed Sep 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.12.10-alt1
- 1.12.10

* Fri Feb 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.10.24-alt4.S1
- dbus-tools-gui does not require /etc/X11/xinit.d (closes: #34549)

* Wed Feb 14 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.10.24-alt3.S1
- fixed systemctl path (closes: #34515)

* Thu Feb 08 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.10.24-alt2.S1
- reenable user session (closes: #34515)

* Thu Feb 08 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.10.24-alt1.S1
- fix package version for previous release
- disable user session because of problems in mate-session

* Wed Feb 07 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.10.20-alt1.S1
- enable user session (closes: #34515)

* Thu Jul 06 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.10.20-alt1
- 1.10.20

* Mon Oct 10 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.10.12-alt1
- 1.10.12

* Sun Jul 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.10.8-alt1
- 1.10.8
- moved /var/run/dbus to /run/dbus

* Sun Dec 06 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.10.6-alt1
- 1.10.6

* Sat May 16 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.8.18-alt1
- 1.8.18

* Mon Feb 16 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.8.16-alt1
- 1.8.16

* Tue Nov 11 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.8.10-alt1
- 1.8.10

* Sun Sep 21 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.8-alt2
- revert "refuse manual start/stop=yes" for systemd(ALT#30338)
- recovery support condrestart for sysv init script(ALT#30328)
- another fix for upgrade package (ALT#14716)

* Wed Sep 17 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.8.8-alt1
- 1.8.8
- dbus.service: added refuse manual start/stop=yes (closes: #14716)

* Thu Jul 03 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Thu Jun 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon Jun 09 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Thu Jan 23 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Nov 11 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.6.18-alt1
- 1.6.18

* Fri Jun 21 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.6.12-alt1
- 1.6.12

* Thu Apr 25 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.6.10-alt1
- 1.6.10

* Wed Oct 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Thu Jul 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Fri Jun 29 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Wed Jun 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt2
- enabled systemd support

* Wed Jun 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Mar 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.4.20-alt1
- 1.4.20

* Tue Feb 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.4.18-alt1
- 1.4.18

* Sat Jul 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.14-alt1
- 1.4.14

* Sun Jun 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.12-alt1
- 1.4.12

* Wed Jun 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.10-alt1
- 1.4.10

* Tue Apr 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.8-alt1
- 1.4.8

* Fri Feb 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Mon Feb 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt3
- moved binaries to /bin (closes: #24991)

* Wed Feb 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt2
- moved libdbus-1.so.* to /%_lib
- added systemd service file (closes: #24991)

* Tue Dec 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt2
- rebuild

* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Aug 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt0.1
- GIT snapshot 2010-08-07 (ff2325c92c411e6718ae38d6976f54580ed57e86)

* Sat Aug 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.24-alt2
- enabled SELinux support

* Wed Mar 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.24-alt1
- 1.2.24

* Thu Mar 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.22-alt1
- 1.2.22

* Tue Feb 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.20-alt2
- monitor service directories for changes (fdo #23846)

* Thu Feb 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.20-alt1
- 1.2.20

* Wed Feb 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.18-alt2
- fixed compilation in --disable-selinux case

* Tue Feb 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.18-alt1
- 1.2.18

* Fri Dec 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.16-alt3
- fixed memory leak in policy reload

* Fri Aug 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.16-alt2
- patch to increase max method timeout (closes: #20990)

* Wed Jul 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.16-alt1
- 1.2.16

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt2
- dbus contains /var/lib/dbus/machine-id
- libdbus-devel contains /usr/share/dbus-1/interfaces

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt1
- 1.2.14

* Thu Apr 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt3
- fixed CVE-2009-1189

* Wed Mar 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt2
- changed chkconfig 345 33 92 -> 345 10 92

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt0.M41.1
- build for branch 4.1

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt0.M50.1
- build for branch 5.0

* Mon Jan 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Wed Jan 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Tue Dec 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Mon Dec 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.4-alt0.M41.1
- build for branch 4.1

* Tue Oct 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1.M41.1
- build for branch 4.1

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt2
- fixed CVE-2008-3834

* Mon Aug 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Wed Aug 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Jun 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt2
- restart messagebus if version less 1.2.1 (close #15763)

* Sun Apr 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Feb 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.20-alt1
- 1.1.20:
  + fixed CVE-2008-0595

* Fri Jan 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt1
- 1.2.0RC2

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.3-alt1
- 1.2.0RC1

* Tue Jan 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt3
- update git patch
- enable inotify
- disable condrestart

* Wed Dec 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- added lost /etc/dbus-1/session.d

* Sun Dec 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt4
- change chkconfig 345 46 03 -> 345 33 92
- add trigger for update

* Fri Apr 27 2007 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt3
- Add X11 session script to dbus-tools-gui (closes #10079)

* Tue Apr 10 2007 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt2
- clean up spec file
- clean up buildrequires
- shutup useradd and groupadd (closes #8760)
- own /etc/dbus-1/ and /usr/share/dbus-1/ (closes #10365)

* Thu Dec 14 2006 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2 (security bug fix)
- patch dbus-1.0.1-pthread-holder-fix.patch merged in upstream
- CVE-2006-6107 (http://secunia.com/advisories/23373/)

* Mon Dec 04 2006 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt4
- fix init script
- don't make tests

* Sun Nov 26 2006 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt3
- add /var/lib/dbus/ to dbus package
- make tests

* Sun Nov 26 2006 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt2
- update init script

* Sun Nov 26 2006 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt1
- 0.94 -> 1.0.1
- dbus-send-do-not-close-shared-connection-thoenig-01.patch merged in upstream

* Sun Nov 26 2006 Igor Zubkov <icesik@altlinux.org> 0.94-alt2
- merge with Sisyphus dbus

* Sun Nov 26 2006 Igor Zubkov <icesik@altlinux.org> 0.94-alt1
- 0.62 -> 0.94 (aka 1.0 RC2)
- buildreq (also, remove /proc from BuildRequires)
- remove dbus-viewer from dbus-tools-gui (by upstream)
- add new tool -- dbus-uuidgen to dbus package
- remove ALL binding's (by upstream)

* Fri Nov 17 2006 Igor Zubkov <icesik@altlinux.org> 0.62-alt3
- fix build (try 2)

* Fri Nov 17 2006 Igor Zubkov <icesik@altlinux.org> 0.62-alt2
- disable mono bindings
- disable qt4 bindings
- add packager tag

* Tue Jun 20 2006 Anton Farygin <rider@altlinux.ru> 0.62-alt1
- new version

* Mon May 22 2006 Anton Farygin <rider@altlinux.ru> 0.61-alt3
- proc added to BuildReq (need for mono bindings)

* Fri May 19 2006 Anton Farygin <rider@altlinux.ru> 0.61-alt2
- fixed byild with gcc-4.1
- enabled mono bindings (thanks to sin@)

* Tue Apr 11 2006 Anton Farygin <rider@altlinux.ru> 0.61-alt1
- new version

* Wed Sep 07 2005 Anton Farygin <rider@altlinux.ru> 0.50-alt1
- new version

* Tue Aug 30 2005 Anton Farygin <rider@altlinux.ru> 0.36.2-alt1
- new version

* Fri Aug 26 2005 Anton Farygin <rider@altlinux.ru> 0.36.1-alt1
- new version

* Fri Aug 19 2005 Anton Farygin <rider@altlinux.ru> 0.35.2-alt1
- new version

* Wed Aug 17 2005 Anton Farygin <rider@altlinux.ru> 0.34-alt5
- start messagebus after dm

* Tue Aug 16 2005 Anton Farygin <rider@altlinux.ru> 0.34-alt4
- dbus-qt.h moved to libdbus-qt-devel

* Mon Aug 08 2005 Anton Farygin <rider@altlinux.ru> 0.34-alt3
- verbosing post-scripts
- disabled build for mono

* Wed Aug 03 2005 Anton Farygin <rider@altlinux.ru> 0.34-alt2
- requires fixed for devel packages (#7064)
- headers for dbus-qt moved to libdbus-qt-devel (#6311)

* Tue Jul 12 2005 Anton Farygin <rider@altlinux.ru> 0.34-alt1
- new version
- disabled mono for x86_64

* Fri May 13 2005 Anton Farygin <rider@altlinux.ru> 0.23.4-alt1
- updated to new version
- gui tools moved from dbus-tools to dbus-tools-gui

* Sun Feb 06 2005 Alexey Morozov <morozov@altlinux.org> 0.23-alt2
- Finally managed to compile Qt bindings!
  Some issues are unresolved though. Someone can take a look into
  qt/message.cpp and implement Message copy constructor and
  putting QVariant datatypes to dbus messages.

* Thu Jan 20 2005 Alexey Morozov <morozov@altlinux.org> 0.23-alt1
- New version (0.23)
- Patches from Mandrake are in mainstream now
- mono location workaround is applied for install section too
- -userhelpers subpackage is renamed to -tools as #5341 suggests
- python package is built against recent rpm-build-python specs and
  corresponding python-module-Pyrex

* Sat Jan 15 2005 Vital Khilko <vk@altlinux.ru> 0.22-alt2
- added patches from Mandrake Linux

* Tue Sep  7 2004 Alexey Morozov <morozov@altlinux.org> 0.22-alt1
- Initial build.
