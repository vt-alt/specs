%define origname gwenhywfar
%def_with qt5

Name:     libgwenhywfar
Version:  5.1.2
Release:  alt1

Summary:  A multi-platform helper library for other libraries
Group:    System/Libraries
License:  LGPLv2+
URL:      http://www2.aquamaniac.de/sites/download/packages.php
# VCS:    http://git.aqbanking.de/git/gwenhywfar.git

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %origname-%version.tar
Patch1:   %name-pthread.patch
Patch2:   %name-fix-build-with-qt5.patch

BuildRequires: gcc-c++ glibc-devel graphviz libcom_err-devel 
BuildRequires: libgnutls-devel libssl-devel tzdata
BuildRequires: libqt4-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
%if_with qt5
BuildRequires: qt5-base-devel qt5-tools
%endif
BuildRequires: zlib-devel libgcrypt-devel ncurses-devel
BuildRequires: ca-certificates

Requires: ca-certificates

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
www.libchipcard.de and OpenHBCI-TNG (The Next Generation)
www.openhbci.de.

Check http://www.freesource.info/wiki/Altlinux/Policy/TLS
for ALT Linux TLS/SSL policy

%package  gtk2
Summary:  Gwenhywfar support for GTK+ 2.x
Group:    System/Libraries
Requires: %name = %version-%release

%description gtk2
Gwenhywfar support for GTK+ 2.x.

%package  gtk3
Summary:  Gwenhywfar support for GTK+ 3.x
Group:    System/Libraries
Requires: %name = %version-%release

%description gtk3
Gwenhywfar support for GTK+ 3.x.

%package  qt4
Summary:  Gwenhywfar support for Qt4
Group:    System/Libraries
Requires: %name = %version-%release

%description qt4
Gwenhywfar support for Qt4

%if_with qt5
%package  qt5
Summary:  Gwenhywfar support for Qt5
Group:    System/Libraries
Requires: %name = %version-%release

%description qt5
Gwenhywfar support for Qt5
%endif

%package  devel
Summary:  Gwenhywfar development kit
Group:    Development/C
Requires: %name = %version-%release
Requires: %name-gtk2 = %version-%release
Requires: %name-qt4  = %version-%release
%if_with qt5
Requires: %name-qt5  = %version-%release
%endif

%description devel
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup -q -n %origname-%version
%patch1 -p1
%patch2 -p1

%build
%undefine _configure_gettext
%autoreconf
%if_with qt5
export PATH=$PATH:%_qt5_bindir
%endif
%configure \
	--disable-static \
	--with-openssl-libs=%_libdir \
%if_with qt5
	--with-guis="gtk2 gtk3 qt4 qt5" \
	--with-qt5-qmake=%_bindir/qmake-qt5 \
	--with-qt5-moc=%_bindir/moc-qt5 \
	--with-qt5-uic=%_bindir/uic-qt5 \
%else
	--with-guis="gtk2 gtk3 qt4" \
%endif
	--with-qt4-libs="%_libdir"

%make_build

%install
%makeinstall_std
%find_lang %origname

# Use system-wide ca-certificates
rm -f %buildroot%_datadir/gwenhywfar/ca-bundle.crt
ln -s %_datadir/ca-certificates/ca-bundle.crt %buildroot%_datadir/gwenhywfar/ca-bundle.crt

%files -f %origname.lang
%doc AUTHORS README TODO
%_bindir/gct-tool
%_bindir/gsa
%_libdir/*.so.*
%exclude %_libdir/libgwengui-gtk2.so.*
%exclude %_libdir/libgwengui-gtk3.so.*
%exclude %_libdir/libgwengui-qt4.so.*
%if_with qt5
%exclude %_libdir/libgwengui-qt5.so.*
%endif
%_libdir/%origname/
%_datadir/gwenhywfar/ca-bundle.crt
%_datadir/gwenhywfar/dialogs/*.dlg

%files gtk2
%_libdir/libgwengui-gtk2.so.*

%files gtk3
%_libdir/libgwengui-gtk3.so.*

%files qt4
%_libdir/libgwengui-qt4.so.*

%if_with qt5
%files qt5
%_libdir/libgwengui-qt5.so.*
%endif

%files devel
%_bindir/%origname-config
%_bindir/xmlmerge
%_bindir/mklistdoc
%_bindir/typemaker
%_bindir/typemaker2
%_libdir/*.so
%_includedir/gwenhywfar5/
%_pkgconfigdir/*
%_datadir/%origname/typemaker2/*
%_datadir/aclocal/gwenhywfar.m4
%_libdir/cmake/*

%changelog
* Tue Feb 04 2020 Andrey Cherepanov <cas@altlinux.org> 5.1.2-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 4.99.22rc6-alt0.1
- New version.

* Thu Aug 29 2019 Andrey Cherepanov <cas@altlinux.org> 4.20.2-alt1
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.20.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.20.1-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 4.20.0-alt2
- Build gtk3 bindings.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 4.20.0-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.19.0-alt1
- New version.
- Build with Qt5.

* Tue Aug 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.18.0-alt1
- New version

* Thu Mar 02 2017 Andrey Cherepanov <cas@altlinux.org> 4.17.0-alt1
- New version

* Tue Jun 21 2016 Andrey Cherepanov <cas@altlinux.org> 4.15.3-alt1
- New version

* Sun Dec 27 2015 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt3
- Update watch file after upstream site reconstruction
- Fix build with new gnutls
- Package cmake files

* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt2
- Do not use strict extension for man pages

* Wed May 27 2015 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt1
- new version 4.14.0

* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 4.13.1-alt1
- new version 4.13.1

* Wed Nov 28 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt1
- new version 4.3.3

* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version 4.3.1
- Add watch file

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version 4.2.1
- Use system-wide ca-certificates (closes: #10901)

* Thu Mar 03 2011 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version 4.0.7
- Exclude qt4 and gtk+ libraries in separate packages

* Mon Oct 04 2010 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt2
- rebuild with new openssl

* Fri Apr 02 2010 Andrey Cherepanov <cas@altlinux.org> 3.11.3-alt1
- new version 3.11.3

* Wed Apr 15 2009 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- new version 3.8.0 (with rpmrb script)

* Mon Nov 24 2008 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt1
- new version 3.5.2 (with rpmrb script)

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- cleanup spec, move gct-tool to original dir
- fix bug #10901 (use ca-bundle.crt from datadir/ca-certificates/)

* Tue Apr 22 2008 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version 3.2.0 (with rpmrb script)
- update buildreqs

* Wed Apr 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version 2.5.4
- do not pack /etc/gwen-public-ca.crt
- update buildreq, fix x86_64 build (use --with-openssl-libs (thanks at@))

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt0.1
- new version 2.4.0
- update buildreq

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt0.1
- new version

* Mon Dec 19 2005 Vitaly Lipatov <lav@altlinux.ru> 1.19.2-alt0.1
- new version

* Mon Aug 22 2005 Igor Muratov <migor@altlinux.org> 1.16.0-alt1
- new version

* Wed Aug 10 2005 Igor Muratov <migor@altlinux.org> 1.14.0-alt1
- new version

* Sun Mar 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- first build for ALT Linux Sisyphus

