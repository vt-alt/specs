Name: gutenprint
Version: 5.3.4
Release: alt1
Epoch: 1
Summary: Gutenprint Printer Drivers
License: GPL-2.0+
Group: Publishing
Requires: lib%name = %EVR, ghostscript
Url: http://gimp-print.sourceforge.net/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.watch
Source2: ru.po

Patch0: gutenprint-5.3.1-alt-fixes.patch
Patch1: gutenprint-5.2.9-alt-makefile.patch
Patch2: gutenprint-alt-LFS.patch
Patch3: gutenprint-alt-link-plugins-with-libraries.patch

BuildRequires: flex foomatic-db-engine libcups-devel libgimp-devel libreadline-devel
BuildRequires: libusb-devel
BuildRequires: chrpath

%description
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.
Gutenprint was formerly called Gimp-Print.

%package -n lib%name
Summary: Shared libraries for high-quality image printing
Group: Publishing

%description -n lib%name
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains gutenprint shared libraries.

%package -n lib%name-devel
Summary: Library development files for gutenprint
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains header files and libraries required to build
gutenprint-based software.

%package -n gimp-plugin-%name
Summary: GIMP plug-in for %name
Group: Publishing
Requires: %name = %EVR gimp

%description -n gimp-plugin-%name
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains the gutenprint GIMP plug-in.

%package cups
Summary: CUPS drivers for Canon, Epson, HP and compatible printers
Group: System/Configuration/Hardware
Provides: %name-CUPS = %EVR
Obsoletes: %name-CUPS < %EVR
Requires: %name = %EVR

%description cups
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains native CUPS support for a wide range of Canon,
Epson, HP and compatible printers.

%package cups-ppds
Summary: PPDs for CUPS drivers for Canon, Epson, HP and compatible printers
Group: System/Configuration/Hardware
Requires: %name-cups = %EVR
BuildArch: noarch

%description cups-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains PPDs for gutenprint-cups.

%prep
%setup
%patch0 -p2
%patch1 -p1
%patch2 -p2
%patch3 -p2
rm -rf gutenprint/po/*.gmo
install %SOURCE2 po/ru.po

%build
%undefine _configure_gettext
# remove old versions of standard macros
find m4* -type f -name \*.m4 -print0 |
	xargs -r0 grep -lxZ 'dnl Copyright (C) .* Free Software Foundation, Inc\.' -- |
	xargs -r0 rm -v --
#rm m4*/libtool.m4
%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	--disable-rpath \
	--with-modules=dlopen \
	--with-cups \
	--with-gimp2 \
	--with-gimp2-as-gutenprint \
	--enable-libgutenprintui2 \
	--enable-cups-ppds \
	--enable-cups-level3-ppds \
	--enable-cups-ppds-at-top-level

%make_build

%install
%makeinstall_std
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%_docdir
mv %buildroot%_datadir/%name/doc %buildroot%docdir
find %buildroot%_libdir/%name/ -name \*.la -delete
chmod +rx %buildroot%_prefix/lib/cups/backend/gutenprint*+usb

# Remove standard library path from rpath
for file in \
  %buildroot%_bindir/* \
  %buildroot%_sbindir/cups-genppd.5.3 \
  %buildroot%_libdir/gimp/*/plug-ins/* \
  %buildroot%_libdir/*.so.* \
  %buildroot%_libexecdir/cups/driver/* \
  %buildroot%_libexecdir/cups/filter/* 
do \
  chrpath --delete ${file}
done

%find_lang %name
%set_verify_elf_method strict

%triggerpostun cups -- %name-cups < %version
cups=%_initdir/cups
if [ -x $cups ] && %_sbindir/cups-genppdupdate | grep -Fqs Restart; then
	$cups condreload
fi

%files -f %name.lang
%_bindir/escputil
%_bindir/testpattern
%_datadir/%name/
%_man1dir/*.1*
%exclude %_datadir/locale/*/gutenprint_*.po
%dir %docdir
%docdir/[AFNR]*
%docdir/gutenprint-users-manual.pdf
%exclude %docdir/gutenprint-users-manual.odt
%exclude %docdir/C*

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name

%files -n lib%name-devel
%_includedir/%{name}*
%_libdir/*.so
%_pkgconfigdir/*.pc
%dir %docdir
%docdir/%name.pdf
%docdir/reference-html

%files -n gimp-plugin-%name
%_libdir/gimp/2.0/plug-ins/%name

%files cups
%_sysconfdir/cups/*
%_bindir/cups-*
%_sbindir/cups-*
%_prefix/lib/cups/backend/gutenprint*+usb
%_prefix/lib/cups/driver/%{name}*
%_prefix/lib/cups/filter/*
%_datadir/cups/usb/net.sf.gimp-print.usb-quirks
%_datadir/cups/calibrate.ppm
%_man8dir/*.8*

%files cups-ppds
%_datadir/cups/model/Global

%changelog
* Thu Dec 17 2020 Andrey Cherepanov <cas@altlinux.org> 1:5.3.4-alt1
- New version.
- Package watch file.

* Tue Dec 03 2019 Andrey Cherepanov <cas@altlinux.org> 1:5.3.3-alt1
- New version.

* Thu Oct 31 2019 Lenar Shakirov <snejok@altlinux.ru> 1:5.3.1-alt2
- Make gutenprint-cups-ppds noarch

* Mon Dec 17 2018 Andrey Cherepanov <cas@altlinux.org> 1:5.3.1-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.2.14-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 1:5.2.14-alt1
- New version (ALT #34674).
- Rename gutenprint-CUPS to gutenprint-cups.
- Enable support of CUPS dyesub USB backend.
- Enable localized ppds.
- Removed Foomatic data generator and the Ghostscript IJS driver.
- Put all PPDs to package gutenprint-cups-ppds.

* Wed Mar 20 2013 Fr. Br. George <george@altlinux.ru> 1:5.2.9-alt1
- Version up
- Fix i586 FILE64 build

* Sat Jun 16 2012 Michael Shigorin <mike@altlinux.org> 1:5.2.8-alt1
- 5.2.8
  + updated patch
  + fixed build with current binutils
- buildreq

* Sat Dec 03 2011 Dmitry V. Levin <ldv@altlinux.org> 1:5.2.7-alt2
- Fixed build, updated build dependencies.
- Fixed packaging of documentation.
- Cleaned up descriptions.
- Disabled build of static libraries.
- Built %name-foomatic as noarch.

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.7-alt1
- 5.2.7

* Tue Nov 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.6-alt2
- rebuild

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.6-alt1
- 5.2.6

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.5-alt1
- 5.2.5

* Thu Sep 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.4-alt2
- added trigger for update PPD (closes: #20952)

* Fri Jul 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.4-alt1
- 5.2.4

* Mon May 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.3-alt2
- fixed headers install

* Tue Dec 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.3-alt1
- 5.2.3

* Thu Nov 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.2-alt1
- 5.2.2

* Tue Oct 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.1-alt1.M41.1
- build for branch 4.1

* Tue Oct 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.1-alt2
- added russian translation (Alexandre Prokoudine)

* Wed Oct 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.1-alt1
- 5.2.1

* Tue Oct 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.0-alt0.M41.1.rc1
- build for branch 4.1

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.0-alt1.rc1
- 5.2.0 RC1

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.7-alt1
- 5.1.7

* Fri Feb 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.6-alt2
- relocation all filters to gutenprint subpackage (close #14690)

* Sat Jan 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.6-alt1
- 5.1.6

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.4-alt1
- 5.1.4

* Thu Nov 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt3.M40.1
- build for branch 4.0

* Thu Nov 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt4
- put "A4" at the beginning to get it as default size

* Tue Oct 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt3
- drop update-printers-db in %%post from %name-CUPS and %name-foomatic

* Sat Sep 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt2
- not install gutenprintui.pc (close #12969)

* Sat Jun 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt1
- 5.0.1 stable release

* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.3-alt1
- 5.1.3

* Sun Jun 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.2-alt1
- 5.1.2
- fixed prereq for %name-{foomatic,CUPS}

* Wed May 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.1-alt3
- fixed provides/obsoletes

* Wed May 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.1-alt2
- added requires lib%name-%%version-%%release for %name
- spec cleanup

* Mon May 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.1-alt1
- 5.1.1
- disable static

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.7-alt4.0
- Automated rebuild.

* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt4
- rebuild with cups-1.2

* Fri Mar 24 2006 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt3
- rebuild with new ijs

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.7-alt2.1.1
- Rebuilt with libreadline.so.5.

* Wed Jun 29 2005 Anton D. Kachalov <mouse@altlinux.org> 4.2.7-alt2.1
- multilib hack

* Fri Jan 28 2005 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt2
- added update-printers-db in post script

* Wed Sep 22 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt1
- 4.2.7

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.6-alt2.1.1.1
- Rebuilt with libtiff.so.4.

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.6-alt2.1.1
- Rebuilt with openssl-0.9.7d.

* Fri May 07 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt2.1
- rebuild without plugin for old gimp

* Fri Apr 02 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt2
- added russian translation by Valia V. Vaneeva

* Wed Feb 11 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt1
- final

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt0.2
- gimp-print-foomatic requires latest foomatic (>=3.0.1) (was changes id's in xml files)

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt0.1
- 4.2.6-pre2

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.5-alt3
- fix building in hasher

* Mon Mar 31 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.5-alt2
- Apply patch for foomatic database (from MDK)

* Thu Feb 27 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.5-alt1
- 4.2.5

* Thu Jan 09 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.4-alt1
- update to latest stable

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.2-alt1
- 4.2.2
- port to subst from 'perl -pi'

* Wed Jun 26 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.1-alt3
- Enable IJS driver

* Tue Jun 18 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.1-alt2
- resurrected foomatic files

* Tue Apr 02 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt7
- Added two patches from MDK (to use drivers for more printers and 
  support for small papers on Epson Stylus Pro printers)

* Wed Feb 20 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt6
- Buildreq updated

* Tue Feb 19 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt5
- added patch.

* Wed Feb 13 2002 AEN <aen@logic.ru> 4.2.0-alt4
- rebuilt with new gimp

* Mon Dec 17 2001 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt3
- added requires to gimp-print-foomatic

* Mon Dec 10 2001 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt2
- added buildreqs, fix docs

* Thu Nov 15 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt6
- rc1

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt5
- b2

* Thu Sep 06 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt4
- new snapshot.

* Mon Aug 13 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt3
- Splited again: common files (filters,docs); CUPS only drivers, foomatic only drivers.

* Fri Aug 10 2001 AEN <aen@logic.ru> 4.1.99-alt2
- added plugin package
- a2

* Mon Aug 06 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt1
- Initial release for ALT Linux.
- Now we are splitting cups-drivers into separate packages.
