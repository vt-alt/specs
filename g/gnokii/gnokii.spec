%define _unpackaged_files_terminate_build 1

Name: gnokii
Version: 0.6.31
Release: alt3

Summary: Unix tool suite for Nokia mobile phones
Group: Communications
License: GPL-2.0-or-later
Url: https://www.gnokii.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: %name-0.6.31-alt-mysql8-transition.patch

Requires: lib%name = %EVR

# Automatically added by buildreq on Fri Oct 10 2008 (-bi)
BuildRequires: flex intltool libMySQL-devel libXpm-devel libbluez-devel libgtk+2-devel libical-devel libncurses-devel libpcsclite-devel libsqlite3-devel libreadline-devel libusb-compat-devel postgresql-devel

%description
Gnokii is a Unix tool suite for Nokia mobile phones.

You should be in 'uucp' group to use it with serial cables.

%package -n x%name
Summary: Unix tool suite for Nokia mobile phones
Group: Communications
Requires: %name = %EVR
Requires: gnokii-artwork

%description -n x%name
xgnokii is a graphical tool for Nokia mobile phones

%package -n lib%name
Summary: Library for gnokii
Group: System/Libraries

%description -n lib%name
You will need libgnokii to run gnokii.

%package -n lib%name-devel
Summary: Development files for gnokii
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Install gnokii-devel if you want to develop or compile applications using
gnokii API.

%package smsd
Summary: Daemon for handling incoming and outgoing SMSes using libgnokii
Group: Communications
Requires: lib%name = %EVR

%description smsd
The SMSD (SMS daemon) program is intended for receiving and sending
SMSes with plain file plugin.

%package smsd-mysql
Summary: MySQL plugin for gnokii-smsd
Group: Communications
Requires: %name-smsd = %EVR

%description smsd-mysql
MySQL plugin for gnokii-smsd.

%package smsd-pq
Summary: PostgreSQL plugin for gnokii-smsd
Group: Communications
Requires: %name-smsd = %EVR

%description smsd-pq
PostgreSQL plugin for gnokii-smsd.

%package smsd-sqlite
Summary: SQLite plugin for gnokii-smsd
Group: Communications
Requires: %name-smsd = %EVR

%description smsd-sqlite
SQLite plugin for gnokii-smsd.

%prep
%setup
%patch -p1
%patch1 -p0

%build
# SMP-incompatible
%define __nprocs 1
#add_optflags %optflags_shared
export lt_cv_prog_cc_static_works=no

%add_optflags -fgnu89-inline
%autoreconf
%configure \
	--disable-static \
	--disable-rpath \
	--with-x \
	--enable-nls \
	--enable-security \
	--enable-libusb \
	--enable-irda \
	--enable-bluetooth \
	--enable-libical \
	--enable-libpcsclite \
	--enable-smsd \
	#
%make_build

pushd xgnokii
%make_build
popd

%install
%makeinstall_std

pushd xgnokii
%makeinstall_std
popd

mv %buildroot%_defaultdocdir/%name %buildroot%_docdir/%name-%version
install -pm644 ChangeLog %buildroot%_docdir/%name-%version/

chmod +x %buildroot%_bindir/*

mkdir -p %buildroot%_datadir/xgnokii
mkdir -p %buildroot%_sysconfdir
sed 's,/usr/local/sbin,%_sbindir,g' \
	< Docs/sample/gnokiirc \
	> %buildroot%_sysconfdir/gnokiirc

rm %buildroot%_libdir/smsd/*.la

%find_lang %name

%files -f %name.lang
%docdir %_defaultdocdir/%name-%version
%dir %_defaultdocdir/%name-%version
%doc %_defaultdocdir/%name-%version/*
%config(noreplace) %_sysconfdir/gnokiirc
%_bindir/gnokii
%_bindir/gnokiid
%_bindir/sendsms
%_sbindir/mgnokiidev
%_man1dir/gnokii.1*
%_man1dir/sendsms.1*
%_man8dir/gnokiid.8*
%_man8dir/mgnokiidev.8*

%files -n x%name
%_bindir/xgnokii
%dir %_datadir/xgnokii
%_desktopdir/xgnokii.desktop
%_man1dir/xgnokii.1*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/gnokii.h
%_includedir/%name/*
%_libdir/lib%name.so
%_pkgconfigdir/gnokii.pc
%_pkgconfigdir/xgnokii.pc

%files smsd
%doc smsd/README
%doc smsd/sms.tables.mysql.sql
%doc smsd/sms.tables.pq.sql
%doc smsd/sms.tables.sqlite.sql
%_bindir/smsd
%_man8dir/smsd.8*
%dir %_libdir/smsd
%_libdir/smsd/libsmsd_file.so

%files smsd-mysql
%_libdir/smsd/libsmsd_mysql.so

%files smsd-pq
%_libdir/smsd/libsmsd_pq.so

%files smsd-sqlite
%_libdir/smsd/libsmsd_sqlite.so

%changelog
* Wed Feb 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.31-alt3
- Fixed build with new gettext.

* Thu Feb 07 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.6.31-alt2
- Fix FTBFS against libmysqlclient.so.21

* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.31-alt1
- Updated to upstream version 0.6.31.

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.6.29-alt3
- rebuilt against libical.so.1

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.29-alt2.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Wed Sep 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.6.29-alt2
- [0.6.29-61-g8509de9] (closes: #23896)
  + SQLite smsd backend

* Wed Aug 04 2010 Alexey I. Froloff <raorn@altlinux.org> 0.6.29-alt1
- [0.6.29-40-g1fdd05f]
  + See ChangeLog for details

* Sun Jan 10 2010 Alexey I. Froloff <raorn@altlinux.org> 0.6.28-alt1
- [0.6.28-166-gebe7f6e]
  + See ChangeLog for details
- spec cleanup

* Fri Oct 10 2008 Sir Raorn <raorn@altlinux.ru> 0.6.27-alt1
- [0.6.27]
 + New memory types: Status Reports, Drafts, and Outbox
 + Bluetooth channel autodetection
- Packaged smsd with file, MySQL and PostgreSQL storage drivers
- Packaged xgnokii.pc (may be needed for xgnokiidir)
- spec cleanup

* Fri Jul 04 2008 Sir Raorn <raorn@altlinux.ru> 0.6.26-alt1
- [0.6.26]
 + PC/SC SIM smart card support
 + gnokiid moved to /usr/bin
- Enabled iCal support

* Sun Nov 25 2007 Sir Raorn <raorn@altlinux.ru> 0.6.22-alt1
- [0.6.22]

* Sun Oct 28 2007 Sir Raorn <raorn@altlinux.ru> 0.6.20-alt1
- [0.6.20]

* Mon Oct 08 2007 Sir Raorn <raorn@altlinux.ru> 0.6.19-alt1
- [0.6.19]

* Tue Jul 31 2007 Sir Raorn <raorn@altlinux.ru> 0.6.18-alt1
- [0.6.18]
 + todologo, ppm2nokia and waitcall removed by upstream
- gnokii-artwork packaged separately
- Cleaned up pkgconfig file
- Fixed ldif export (closes: #9994)

* Mon Sep 11 2006 Sir Raorn <raorn@altlinux.ru> 0.6.14-alt2
- Fixed --setdatetime argument parsing

* Tue Aug 29 2006 Sir Raorn <raorn@altlinux.ru> 0.6.14-alt1
- [0.6.14]
 + new utility - waitcall

* Thu Jul 13 2006 Sir Raorn <raorn@altlinux.ru> 0.6.13-alt1
- [0.6.13]
 + new libusb driver for DKU-2 cable (connection = dku2libusb)
 + SONAME changed for libgnokii
- Updated build requires
- Use %%update_menus in xgnokii

* Fri May 19 2006 Sir Raorn <raorn@altlinux.ru> 0.6.12-alt1
- [0.6.12]

* Tue Feb 28 2006 Sir Raorn <raorn@altlinux.ru> 0.6.11-alt1
- [0.6.11]
- spec **cleanup**
- Really enable bluetooth support
- Fix some 6310i problems (closes: #9161)

* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 0.6.10-alt1
- 0.6.10
- spec *cleanup*

* Mon May 02 2005 Denis Smirnov <mithraen@altlinux.ru> 0.6.5-alt1
- 0.6.5 (major feature enhancements)
- bluetooth support

* Fri Apr 16 2004 Michael Shigorin <mike@altlinux.ru> 0.6.1-alt1
- 0.6.1 (major feature enhancements)
- removed patch0

* Fri Jan 02 2004 Michael Shigorin <mike@altlinux.ru> 0.5.8-alt1
- 0.5.8 (minor bugfixes)
- fixed manpage installation
- seperated xgnokii

* Tue Nov 11 2003 Michael Shigorin <mike@altlinux.ru> 0.5.5-alt2
- %optflags_shared

* Wed Oct 08 2003 Michael Shigorin <mike@altlinux.ru> 0.5.5-alt1
- 0.5.5 (minor feature enhancements)

* Tue Sep 23 2003 Michael Shigorin <mike@altlinux.ru> 0.5.4-alt1
- 0.5.4 (major bugfixes)
- enabled security options (e.g. PIN change)
- spec cleanup

* Tue Jul 08 2003 Michael Shigorin <mike@altlinux.ru> 0.5.2-alt1
- built for ALT Linux
- adapted from ASPLinux contribs (incl. patch and .desktop)
- package libification
- lockdir patch
- spec cleanup

* Mon Jun 16 2003 Leonid Kanter <leon@asplinux.ru>
- 0.5.2

* Wed Jun 11 2003 Leonid Kanter <leon@asplinux.ru>
- 0.5.1
- add gnokii-devel package
- build with bluetooth support

* Wed Mar 05 2003 Leonid Kanter <leon@asplinux.ru>
- rewrote spec (fix permissions)
- create desktop file

* Fri Feb 07 2003 Hugo Monteiro <hmmm@fct.unl.pt>
- rebuilt for version 0.5.0pre5
- spec file cleanup

* Fri Sep 06 2002 Hugo Monteiro <hmmm@fct.unl.pt>
- rebuilt for version 0.4.3

* Wed Aug 02 2000 Than Ngo <than@redhat.de>
- update to 0.3.2
- fix non-standard-gid (Bug #15041)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat May 27 2000 Ngo Than <than@redhat.de>
- rebuild for 7.0

* Wed Jan 05 2000 Ngo Than <than@redhat.de>
- initial RPM for powertools 6.2

