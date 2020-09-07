Name: xsane
Version: 0.999
Release: alt6

Summary: XSane is a graphical frontend for scanners. It uses the library SANE
Summary(ru_RU.UTF-8): Xsane -- это графическая программа для сканирования, использующая библиотеку SANE

License: GPL
Group: Graphics
Url: http://www.xsane.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.xsane.org/download/%name-%version.tar
Source1: %name-16x16.xpm
Source3: %name-%version.ru.po
Patch: %name-0.99-debian.patch
Patch1: %name-0.996-ubuntu.patch
Patch2: %name-0.998-alt-libpng15.patch
Patch3: xsane-0.999-lcms2.patch
Patch4: xsane-0.999-alt-fix-broken-icon.patch

BuildPreReq: libjpeg-devel libusb-devel libpng-devel

# Automatically added by buildreq on Fri Jul 10 2009
BuildRequires: libgimp-devel libgphoto2-devel libjpeg-devel liblcms2-devel libsane-devel libtiff-devel

# for po recoding
BuildPreReq: recode
# for help
#Requires: webclient

%description
XSane is a graphical frontend for SANE library,
which provides access to scanners, digital cameras,
and other capture devices.  XSane is written in GTK+
and provides control for performing the scan and
then manipulating the captured image.
Install this if you want a graphical frontend for
sane for use in the X Window System.

%description -l ru_RU.UTF-8
XSane -- это графический интерфейс к библиотеке SANE,
которая предоставляет доступ к сканерам, цифровым камерам и другим
устройствам ввода изображения. XSane написана на GTK+ и позволяет
управлять сканированием и обработкой полученного изображения.
Установите XSane, если вы хотите получить графическую оболочку
для sane, работающую в системе X Window.

%package gimp2
Summary: A GIMP2 plug-in which provides the SANE scanner interface
Summary(ru_RU.UTF-8): 	Модуль для GIMP2, позволяющий сканировать через SANE.
Group: Graphics
Provides: %name-gimp
Requires: %name = %version-%release, gimp2

%description gimp2
This package provides the regular XSane frontend for the SANE scanner
nterface, but it works as a GIMP2 plug-in.  You must have GIMP2
installed to use this package.

%description gimp2 -l ru_RU.UTF-8
Этот пакет предоставляет обычный фронтенд XSane для сканирования
через интерфейс SANE, который работает как модуль для GIMP2.
Вам потребуется установить GIMP2 для использования этого пакета.

%package doc
Summary: Documentation for XSANE
Summary(ru_RU.UTF-8): Документация для XSANE
Group: Graphics
BuildArch: noarch
Requires: %name = %version-%release
Requires: sane-doc

%description doc
Documentation for XSANE

%description doc -l ru_RU.UTF-8
Документация для XSANE

%prep
%setup
%patch -p1
#%patch1 -p1
%patch2 -p2
%patch3 -p1
%patch4 -p2
cp -f %SOURCE3 po/ru.po
#__subst "s|\"/usr/local/share/sane/|\"%_docdir/sane/|" doc/sane-backends-doc.html

# Set browser by default
%__subst 's|BROWSER "netscape|BROWSER "url_handler.sh|g' src/xsane.h

%build
%configure --enable-gtk2 --enable-gimp --enable-lcms
%make_build xsanedocdir=%_docdir/%name

%install
%makeinstall_std xsanedocdir=%_docdir/%name

install -d %buildroot/%_libdir/gimp/2.0/plug-ins
ln -s %_bindir/%name %buildroot/%_libdir/gimp/2.0/plug-ins/%name

install -p -m644 -D %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -p -m644 -D src/%name-32x32.xpm %buildroot%_niconsdir/%name.xpm
install -p -m644 -D src/%name-48x48.xpm %buildroot%_liconsdir/%name.xpm

install -p -m644 -D %name.desktop %buildroot%_desktopdir/%name.desktop

# use modern backends list from SANE project
rm -f %buildroot/%_docdir/%name/sane-backends-doc.html
ln -s %_docdir/sane-backends/sane-backends.html %buildroot/%_docdir/%name/sane-backends-doc.html


%find_lang %name

%files -f %name.lang
%doc %name.[A-Z]*
%_bindir/%name
%_datadir/sane/*
%_man1dir/*
%_desktopdir/*
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%_miconsdir/*.xpm
%_pixmapsdir/*.xpm
#%doc %name.*

%files doc
%_docdir/%name/

%files gimp2
%_libdir/gimp/2.0/plug-ins/%name

%changelog
* Thu Sep 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.999-alt6
- fix xsane documentation dir
- add updated ru.po (RM 14250)

* Wed Nov 07 2018 Ivan Razzhivin <underwit@altlinux.org> 0.999-alt5
- fix broken icon

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.999-alt4
- drop webclient require (ALT bug 34574)

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.999-alt3
- make do subpackage noarch

* Thu Apr 03 2014 Vitaly Lipatov <lav@altlinux.ru> 0.999-alt2
- build with liblcms2 (ALT bug #29938)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.999-alt1
- new version 0.999 (with rpmrb script)

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.998-alt2.2
- Rebuilt with libtiff5 & libpng15

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.998-alt2.1
- Fixed build

* Tue Dec 20 2011 Vitaly Lipatov <lav@altlinux.ru> 0.998-alt2
- rebuild with RPATH free sane

* Fri Feb 04 2011 Vitaly Lipatov <lav@altlinux.ru> 0.998-alt1
- new version 0.998 (with rpmrb script)

* Sat Sep 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.997-alt1
- new version 0.997 (with rpmrb script)

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.996-alt1
- new version 0.996 (with rpmrb script)
- update buildreq, apply Ubuntu patches

* Wed Feb 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.995-alt1
- new version 0.995 (with rpmrb script)
- update buildreqs, enable build with lcms (bug #14584)
- cleanup spec

* Sat May 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.994-alt1
- new version 0.994 (with rpmrb script)

* Sat Feb 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.992-alt1
- new version 0.992 (with rpmrb script)

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.991-alt3
- small spec cleanup, update buildreq
- build on x86_64 (fix bug #9644)

* Wed Mar 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.991-alt2
- fix build with new icon macroses
- replace menu file with desktop file

* Sat Jan 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.991-alt1
- new version

* Sat Dec 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt0.1pre2
- new version (prerelease), russian translation is updated

* Tue Dec 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.98b-alt1
- new stable version (ru.po updated)
- remove printf patch (applied in mainstream)
- change /usr/lib to macros

* Sat Oct 29 2005 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt0.1pre
- new version (prerelease)

* Wed Oct 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt2
- add patch from Debian (fix #6825)
- add fix for console output

* Mon Jan 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt1
- new version

* Wed Sep 22 2004 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt1
- release

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot at altlinux.org> 0.96-alt0.1pre1.1
- Rebuilt with libtiff.so.4.

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt0.1pre1
- new version
- CAUTION! You need delete old setting (~/.sane/xsane)
- update russian translation
- set mozilla by default as browser
- split doc package

* Fri Jun 11 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt2
- move docs to right place
- remove sane requires

* Wed May 19 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt1.1
- add recode buildreq

* Sat May 15 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt1
- new version
- removed gimp1 support and add gimp2 support

* Sun Jan 04 2004 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt2
- add libgphoto2-devel to buildrequires
- place plug-in for gimp1 directly in plug-ins dir
- rebuld with gcc 3.3

* Mon Sep 22 2003 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- new version

* Mon Mar 24 2003 Vitaly Lipatov <lav@altlinux.ru> 0.90-alt1.1
- now the package is not owner of datadir/sane

* Tue Jan 07 2003 Vitaly Lipatov <lav@altlinux.ru> 0.90-alt1
- new version
- cleanup spec
- add genericname
- add scrollkeeper in post/postun
- renamed rc-file for gtk1 version (xsane for GIMP 1.2.x)

* Mon Nov 04 2002 Vitaly Lipatov <lav@altlinux.ru> 0.89-alt2
- build with GTK2
- add plugin for GIMP packet (in GTK1), from Mandrake's packet

* Mon Oct 28 2002 Vitaly Lipatov <lav@altlinux.ru> 0.89-alt1
- new version
- update russian translation
- cleanup spec, ready for GTK2

* Tue Sep 17 2002 Vitaly Lipatov <lav@altlinux.ru> 0.88-alt1
- new version

* Thu Sep 05 2002 Vitaly Lipatov <lav@altlinux.ru> 0.87-alt1
- new version
- updated russian translation

* Wed Feb 13 2002 AEN <aen@logic.ru> 0.84-alt1
- new version

* Wed Oct 24 2001 Rider <rider@altlinux.ru> 0.80-alt1
- 0.80
- buildrequires fix

* Fri Oct 12 2001 AEN <aen@logic.ru> 0.79-alt3
- rebuilt with libpng.so.3

* Tue Sep 25 2001 AEN <aen@logic.ru> 0.79-alt2
- added russian translation from John Profic

* Mon Aug 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.79-alt1
- 0.79
- Added menu and icons.
- Specfile cleanup.

* Wed Apr  10 2001 Rider <rider@altlinux.ru>
- 0.75

* Tue Apr  3 2001 Rider <rider@altlinux.ru>
- 0.74

* Thu Jan 09 2001 AEN <aen@logic.ru>
- adopted for RE

* Sun Jan 07 2001 David BAUDENS <baudens@mandrakesoft.com> 0.69-2mdk
- Fix buildRequires
- Fix Requires
- Clean %%files section
- Spec clean up

* Mon Jan 01 2001 Daouda Lo <daouda@mandrakesoft.com> 0.69-1mdk
- release

* Mon Dec 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.68-1mdk
- updated to 0.68

* Fri Dec 08 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.65-1mdk
- updated to 0.65

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.64-1mdk
- new and shiny version.

* Fri Nov 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.63-1mdk
- new and shiny version.

* Sat Jul 15 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.60-1mdk
- new version
- macrosifications

* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.57-2mdk
- fix group

* Thu Mar 16 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- first release for mandrake
