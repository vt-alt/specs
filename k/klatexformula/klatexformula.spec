Name: klatexformula
Version: 4.1.0
Release: alt1

Summary: Generating images from LaTeX equations
License: GPLv2
Group: Publishing

Url: http://klatexformula.sourceforge.net/
Source: %name-%version.tar.gz
Patch: klatexformula-4.0.0-alt-qt-5.11.patch
Patch1: klatexformula-4.1.0-alt-qt-5.15.patch

BuildRequires(pre): rpm-build-xdg

# Automatically added by buildreq on Thu Aug 09 2018
# optimized out: cmake-modules fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libX11-devel libgpg-error libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libwayland-server python-base python-modules qt5-base-devel qt5-tools qt5-tools-devel sh3 xorg-proto-devel
BuildRequires: cmake doxygen fonts-ttf-xorg graphviz libssl-devel qt5-svg-devel qt5-tools-devel-static qt5-x11extras-devel

%description
KLatexFormula is an easy-to-use graphical application for generating
images (that you can drag and drop, copy and paste or save to disk) from
LaTeX equations.

# TODO KLFOpenOfficeorg

%package devel
Group: Development/KDE and QT
Summary: Development environment for %name
%description devel
%summary
TODO: make shared version of %name-devel.

%prep
%setup
%patch -p2
%patch1 -p1

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%cmake	\
	-DKLF_LIBKLFBACKEND_AUTO_STATIC=False \
	..

%cmake_build all doc

%install
%cmakeinstall_std
for N in %buildroot/%_datadir/pixmaps/kla*.png; do
  SZ="${N##*-}"; SZ="${SZ%%.*}"
  install -D $N %buildroot%_iconsdir/hicolor/${SZ}x${SZ}/apps/%name.png
done

%files
%_bindir/*
%_libdir/lib*.so.*
%_iconsdir/hicolor/*/apps/*.png
%_pixmapsdir/*.png
%_desktopdir/*
%_xdgmimedir/*
%_datadir/%name

%files devel
%doc %_defaultdocdir/%name
%_includedir/*
%_libdir/lib*.so

%changelog
* Fri Sep 25 2020 Sergey V Turchin <zerg@altlinux.org> 4.1.0-alt1
- new version

* Wed Jun 19 2019 Michael Shigorin <mike@altlinux.org> 4.0.0-alt4
- E2K: explicit -std=c++11

* Wed Oct 17 2018 Fr. Br. George <george@altlinux.ru> 4.0.0-alt3
- Fix icon paths

* Tue Oct 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt2
- NMU: fixed build with qt-5.11.

* Thu Aug 09 2018 Fr. Br. George <george@altlinux.ru> 4.0.0-alt1
- Autobuild version bump to 4.0.0
- Switch to qt5

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 3.2.11-alt3
- Fix FTBFS (Add missing rpm-build-xdg).

* Mon Jan 25 2016 Fr. Br. George <george@altlinux.ru> 3.2.11-alt2
- Fix build

* Wed Aug 20 2014 Fr. Br. George <george@altlinux.ru> 3.2.11-alt1
- Autobuild version bump to 3.2.11
- Fix build and patch

* Tue May 13 2014 Fr. Br. George <george@altlinux.ru> 3.2.9-alt1
- Autobuild version bump to 3.2.9
- Devel now uses shared libraries

* Thu Feb 27 2014 Fr. Br. George <george@altlinux.ru> 3.2.8-alt1
- Autobuild version bump to 3.2.8
- Fix good old RU_ru LC_NUMERIC in postscript files

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 3.2.7-alt1
- Autobuild version bump to 3.2.7
- Fix requires

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 3.2.6-alt1
- Autobuild version bump to 3.2.6
- DSO list completion

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 3.2.5-alt1
- Autobuild version bump to 3.2.5

* Thu Oct 13 2011 Fr. Br. George <george@altlinux.ru> 3.2.4-alt1
- Initial build from scratch

