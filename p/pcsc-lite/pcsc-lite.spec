#undefine XXX__libtoolize
#define unstable 1
%def_disable static
%def_enable polkit
%def_enable systemd

Name: pcsc-lite
Version: 1.8.25
Release: alt1

Summary: PC/SC Lite smart card framework and applications
License: %bsd
Group: System/Servers

URL: https://pcsclite.apdu.fr/

Source: %name-%version.tar

Source1: pcscd.init
Source2: pcsc-lite-pcscd.sysconfig
Source3: pcsc-lite.tmpfiles

Requires: libpcsclite = %version-%release
%{?_enable_polkit:Requires: polkit}

BuildRequires: rpm-build-licenses perl-podlators
BuildRequires: flex
BuildRequires: pkgconfig(libudev)
%{?_enable_polkit:BuildRequires: pkgconfig(polkit-gobject-1) >= 0.111}
%{?_enable_systemd:BuildRequires: pkgconfig(systemd)}

%if_enabled static
BuildRequires: glibc-devel-static
%endif

%description
pcscd is the daemon program for PC/SC Lite. It is a resource
manager that coorinates communications with Smart Card readers and Smart
Cards that are connected to the system.
The purpose of PCSC Lite is to provide a Windows(R) SCard interface
in a very small form factor for communicating to smartcards and readers.
PCSC Lite uses the same winscard api as used under Windows(R)

This package contains the service for PC/SC Lite.

%package -n libpcsclite
Group: System/Libraries
Summary: Libraries for pcscd
#
%description -n libpcsclite
Libraries for pcscd. pcscd is the daemon program
for PC/SC Lite. It is a resource manager that coorinates
communications with Smart Card readers and Smart Cards
that are connected to the system. The purpose of PCSC Lite
is to provide a Windows(R) SCard interface in a very small
form factor for communicating to smartcards and readers.
PCSC Lite uses the same winscard api as used under Windows(R)

%package -n libpcsclite-devel
Group: Development/C
Summary: Haeders and other development files for libpcsclite
Requires: libpcsclite = %version-%release
#
%description -n libpcsclite-devel
Haeders and other development files for libpcsclite

%package -n libpcsclite-devel-static
Group: Development/C
Summary: Static libraries for libpcsclite
Requires: libpcsclite-devel = %version-%release
#
%description -n libpcsclite-devel-static
Static libraries for libpcsclite

%prep
%setup
subst 's|AC_PREREQ(\[2.69\])|AC_PREREQ(\[2.68\])|' configure.ac

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable polkit} \
    --enable-debugatr \
    --enable-ipcdir=/var/run/pcscd \
    --enable-usbdropdir=%_libdir/pcsc/drivers \
    --with-systemdsystemunitdir=%_unitdir

%make_build

# pdf
%make_build -C doc

%install
%makeinstall_std

install -pDm755 %SOURCE1 %buildroot/%_initdir/pcscd
install -pDm644 %SOURCE2 %buildroot/%_sysconfdir/sysconfig/pcscd

mkdir -p %buildroot%_sysconfdir/reader.conf.d
mkdir -p %buildroot/var/run/pcscd
mkdir -p %buildroot%_libdir/pcsc/drivers

# enable pcscd socket activation
mkdir -p %buildroot%_unitdir/sockets.target.wants
ln -s ../pcscd.socket %buildroot%_unitdir/sockets.target.wants
mkdir -p %buildroot/lib/tmpfiles.d
install -pDm644 %SOURCE3 %buildroot/lib/tmpfiles.d/pcsc-lite.conf

%preun
%preun_service pcscd

%post
%post_service pcscd

%files
%doc AUTHORS COPYING HELP NEWS README* SECURITY TODO doc/README.DAEMON doc/README.polkit
%dir %_sysconfdir/reader.conf.d
%config(noreplace) %_sysconfdir/sysconfig/pcscd
%_initdir/pcscd
%if_enabled systemd
%_unitdir/pcscd.*
%_unitdir/sockets.target.wants/*
%endif
/lib/tmpfiles.d/pcsc-lite.conf
%_sbindir/pcscd
#_bindir/make_hash_link.sh
%_man5dir/*
%_man8dir/*
%dir %_libdir/pcsc
%dir %_libdir/pcsc/drivers
%{?_enable_polkit:%_datadir/polkit-1/actions/*.policy}
%ghost %dir /var/run/pcscd

# NB: .so belongs here, see ALT#25275
%files -n libpcsclite
%_libdir/libpcsclite.so.*
%_libdir/libpcsclite.so

%files -n libpcsclite-devel
%doc ChangeLog
%_bindir/pcsc-spy
%_libdir/libpcscspy.so*
%_includedir/PCSC/
%_libdir/pkgconfig/libpcsclite.pc
%_man1dir/pcsc-spy.*

%if_enabled static
%files -n libpcsclite-devel-static
%_libdir/libpcsclite.a
%endif

%changelog
* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 1.8.25-alt1
- New version.

* Thu Dec 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.23-alt1
- New version.

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.22-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.21-alt1
- New version

* Thu May 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.20-alt3
- Fixed realloc usage.

* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 1.8.20-alt2
- BOOTSTRAP: introduce polkit, systemd knobs (on by default)

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.20-alt1
- new version 1.8.20

* Fri Dec 30 2016 Lenar Shakirov <snejok@altlinux.ru> 1.8.18-alt2
- Requires: polkit added (closes: #32950)

* Thu Sep 15 2016 Andrey Cherepanov <cas@altlinux.org> 1.8.18-alt1
- new version 1.8.18

* Wed Jun 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.17-alt1
- 1.8.17

* Thu Aug 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.14-alt1
- 1.8.14

* Wed Jul 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.13-alt2
- add patches from upstream master

* Thu Nov 13 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.13-alt1
- 1.8.13

* Fri Oct 03 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.12-alt1
- 1.8.12

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.11-alt1
- 1.8.11

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 1.8.8-alt1
- 1.8.8

* Wed Aug 15 2012 Michael Shigorin <mike@altlinux.org> 1.8.5-alt2
- added systemd support (shaba@)
- moved libpcsclite.so to libpcsclite subpackage, thx ab@ (#25275)

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.5-alt1
- 1.8.5
- add preun/post service scripts

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.7.4-alt3
- disabled verbose logs by default (sysconfig)

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 1.7.4-alt2
- fixed initscript
- minor spec cleanup

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.4-alt1
- [1.7.4]

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 1.6.1-alt1
- [1.6.1]
  + Dropped update-reader.conf
- Disabled libhal, enabled libusb

* Thu Sep 10 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.5-alt1
- [1.5.5] (closes: #21489)
- Dropped testpcsc (test tool)
- IPC directory moved to /var/run/pcscd
- Packaged driver directory

* Tue Apr 28 2009 Andriy Stepanov <stanv@altlinux.ru> 1.5.2-alt1
- New version

* Thu Jan 17 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt3
- fix initscript daemon startup options (#14023)

* Mon Oct 01 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt2
- add description to initscript

* Wed Sep 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt1
- new version

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.1-alt1
- new version

* Tue Feb 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt2
- fix default /etc/sysconfig/pcscd

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt1
- new version

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt5
- add patches from PLD

* Mon Dec 01 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt4
- remove *.la

* Mon Sep 29 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt3
- move config to %_sysconfdir
- fix build requires
- WITHOUT_RC_COMPAT=1 in initscript

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.1-alt2
- fix requires

* Tue Oct 22 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.1-alt1
- initial spec

