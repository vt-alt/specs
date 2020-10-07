Name: qpxtool
Version: 0.8.0
Release: alt2

Summary: QPxTool - CD/DVD quality check utility with QT GUI
License: GPLv2
Group: System/Configuration/Hardware

Url: http://qpxtool.sourceforge.net
Source: http://dl.sf.net/%name/%name-%version.tar.bz2
Source100: qpxtool.watch
Patch: qpxtool-0.8.0-alt-werror.patch
Patch1: alt-qt5.15.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ extra-cmake-modules qt5-base-devel qt5-tools-devel libpng-devel

%add_debuginfo_skiplist %_libdir/%name/*.so*
# didn't work for #250273:
# 	x86_64: NEW unmet dependencies detected:
# qpxtool-debuginfo#0.8.0-alt1	debug64(libqpxpioneer.so.0)
# qpxtool-debuginfo#0.8.0-alt1	debug64(libqpxplextor.so.0)
# qpxtool-debuginfo#0.8.0-alt1	debug64(libqpxscan.so.0)
# qpxtool-debuginfo#0.8.0-alt1	debug64(libqpxtransport.so.0)
# qpxtool-debuginfo#0.8.0-alt1	debug64(libqpxyamaha.so.0)
%global __find_debuginfo_files %nil

%description
QPxTool is the Linux way to get full control over your CD/DVD drives.
It is the Open Source Solution which intends to give you access to all
available Quality Checks (Q-Checks) on written and blank media, that are
available for your drive. This will help you to find the right media and
the optimized writing speed for your hardware, which will increase the
chance for a long data lifetime. See supported drives to get a list of
the currently supported hardware.

%package -n lib%name
Summary: Library files for %name
Group: Development/C

%description -n lib%name
This package contains the library files for %name

%package -n lib%name-devel
Summary: Development environment for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel
Obsoletes: %name-devel

%description -n lib%name-devel
This package contains the include files for %name

%prep
%setup
%patch -p1
%patch1 -p1

%build
export PATH="%_qt5_bindir:$PATH"
# NB: not autoconf but hand-made configure script
./configure \
	--prefix=%_prefix \
	--bindir=%_bindir \
	--sbindir=%_sbindir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	#
%make_build

%install
export PATH="%_qt5_bindir:$PATH"
%makeinstall_std

%files
%doc AUTHORS ChangeLog README TODO
%_libdir/%name/
%_bindir/cdvdcontrol
%_bindir/f1tattoo
%_bindir/qpxtool
%_bindir/qscan
%_bindir/qscand
%_bindir/readdvd
%_sbindir/pxfw
%_man1dir/*
%_man8dir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_datadir/%name/

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib*.so

%changelog
* Thu Oct 01 2020 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- fix compile with Qt-5,15

* Sun Feb 09 2020 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0 built against qt5 (thx Boris Pek for heads-up)
- dropped patches
- added debian watch file
- fixed License:
- spec cleanup
- dropped debuginfo due to unmets generated

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.1-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libqpxtool
  * postun_ldconfig for libqpxtool
  * post_ldconfig for qpxtool
  * postun_ldconfig for qpxtool
  * update_menus for qpxtool
  * postclean-05-filetriggers for spec file

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt4
- update requires

* Thu Apr 24 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt3
- fix x86_64 build
- remove COPYING
- split libraries to standalone package, rename devel package to lib*-devel

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt2
- apply patch for kernel above 2.6.23
- fix build

* Wed Sep 19 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version for Sisyphus

* Mon Sep 17 2007 Motsyo Gennadi <drool@altlinux.ru> 0.6.1-alt0.M40.1
- new version build for M40

* Mon Jun 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0.9-alt1
- new version 0.6.0.9, fix build process, fix textrels
- fix typo in summary (bug #11795)

* Sun Aug 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt0.1
- initial build for Sisyphus
