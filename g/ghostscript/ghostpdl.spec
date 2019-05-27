Name: ghostscript
Version: 9.27
Release: alt1

%define ijsver	0.35
%global origver %version
%define esp_name esp-ghostscript
%define gnu_name gnu-ghostscript

Url: http://www.ghostscript.com

# Included CMap data is Redistributable, no modification permitted,
License: GPLv3+ and Redistributable, no modification permitted

Summary: PostScript interpreter and renderer, most printer drivers
Group: Publishing

Source: ghostpdl-%version.tar.gz
Source1: repatch_spec.sh
Source2: ghostscript.unused
Source3: README.patches

## FC patches
Patch1: FC-cve-2019-6116.patch
Patch2: FC-subclassing-devices-fix-put_image-method.patch
Patch3: FC-cve-2019-3835.patch
Patch4: FC-cve-2019-3838.patch
Patch5: FC-9.23-100-run-dvipdf-securely.patch

## Ubuntu patches
Patch101: Ubuntu-2001_docdir_fix_for_debian.patch
Patch102: Ubuntu-2002_gs_man_fix_debian.patch
Patch103: Ubuntu-2003_support_multiarch.patch
Patch104: Ubuntu-2004_remove_non-Debian_paths_from_docs.patch
Patch105: Ubuntu-2005_fix_Debian_paths_in_docs.patch
Patch106: Ubuntu-2006_suggest_install_ghostscript-doc_in_docs.patch
Patch107: Ubuntu-2007_suggest_install_ghostscript-doc_in_code.patch
Patch108: Ubuntu-2008_mention_ghostscript-x_in_docs.patch
Patch109: Ubuntu-2010_add_build_timestamp_setting.patch
Patch110: Ubuntu-020181126-96c381c-ps2write-move-the-page-level-save-restore-wrapper.patch
Patch111: Ubuntu-020181205-fae21f16-subclassing-devices-fix-put-image-method.patch
Patch112: Ubuntu-CVE-2019-6116.patch
Patch113: Ubuntu-lp1815339.patch
Patch114: Ubuntu-lp1815339-2.patch
Patch115: Ubuntu-CVE-2019-3835-pre1.patch
Patch116: Ubuntu-CVE-2019-3835-pre2.patch
Patch117: Ubuntu-CVE-2019-3835-1.patch
Patch118: Ubuntu-CVE-2019-3835-2.patch
Patch119: Ubuntu-CVE-2019-3838-1.patch
Patch120: Ubuntu-CVE-2019-3838-2.patch
Patch121: Ubuntu-CVE-2019-3839-1.patch
Patch122: Ubuntu-CVE-2019-3839-2.patch

## ALT patches
Patch500: ghostscript-alt-ijs-version.patch
Patch501: alt-urw-fonts-naming.patch

#compatibility requires
Requires: %name-classic = %version-%release
Provides: %esp_name = %version, %gnu_name = %version
Obsoletes: %gnu_name, %esp_name

# Automatically added by buildreq on Mon Aug 27 2018
# optimized out: at-spi2-atk fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libICE-devel libSM-devel libX11-devel libXext-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel libpng-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server perl pkg-config python-base python-modules python3 python3-base sh3 xorg-proto-devel zlib-devel
BuildRequires: docbook-utils-print ghostscript-utils glibc-devel-static imake libXt-devel libcups-devel libexpat-devel libgtk+3-devel libjpeg-devel libopenjpeg2.0-devel libpaper-devel libtiff-devel xorg-cf-files

# Eliminate libpng12-devel
BuildRequires: libpng-devel

%package module-X
Summary: PostScript interpreter and renderer (additional support for X)
Group: Publishing
Requires: %name-classic = %version-%release
Provides: %esp_name-module-X = %version, %gnu_name-module-X = %version
Obsoletes: %gnu_name-module-X, %esp_name-module-X

%package utils
Summary: Additional tools for configuring printers
Group: Publishing
Requires: %name-classic = %version-%release
Provides: %esp_name-utils = %version, %gnu_name-utils = %version
Obsoletes: %gnu_name-utils, %esp_name-utils
BuildArch: noarch

%package -n libgs
Summary: Shared library for %name
Group: Publishing
Provides: %esp_name-lib = %version, %gnu_name-lib = %version, %name-lib = %version
Obsoletes: %gnu_name-lib, %esp_name-lib, %name-lib

%package -n libgs-devel
Summary: Development library for %name
Group: Development/C

%package classic
Summary: classic edition of %name
Group: Publishing
Requires: %name-common = %version-%release
Provides: %esp_name-classic = %version, %gnu_name-classic = %version, %name-minimal = %version
Obsoletes: %gnu_name-classic, %esp_name-classic, %name-minimal

%package gtk
Summary: %name with gtk
Group: Publishing
Provides: %esp_name-gtk = %version, %gnu_name-gtk = %version
Obsoletes: %gnu_name-gtk, %esp_name-gtk

%package -n libijs
Summary: Dynamic library for the IJS printer driver plug-in interface
Version: %{ijsver}_%version
Group: Publishing
Provides: libespijs = %version, libgnuijs = %version
Obsoletes: libgnuijs, libespijs

%package -n libijs-devel
Summary: Headers and links for compiling against
Group: Development/C
Requires: libijs = %version-%release
Provides: libespijs-devel = %version, libgnuijs-devel = %version
Obsoletes: libgnuijs-devel, libespijs-devel

%package common
Version: %origver
Summary: Common files for the %name
Group: Publishing
Requires: urw-fonts >= 1.1
Requires: %name-classic = %version-%release
Provides: %esp_name-common = %version, %gnu_name-common = %version
Obsoletes: %gnu_name-common, %esp_name-common
BuildArch: noarch

%description
Ghostscript is a set of software that provides a PostScript(TM) interpreter,
a set of C procedures (the Ghostscript library, which implements the
graphics capabilities in the PostScript language) and an interpreter for
Portable Document Format (PDF) files. Ghostscript translates PostScript code
into many common, bitmapped formats, like those understood by your printer
or screen. Ghostscript is normally used to display PostScript files and to
print PostScript files to non-PostScript printers.
Most applications use PostScript for printer output.

In addition, the package contains filters which transfer the raw
bitmap of GhostScript into the protocol of some additional printer
models.

You should install ghostscript if you need to display PostScript files, or
if you have a non-PostScript printer.

%description module-X
Ghostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many printer
formats (including support for colour printers), and popular graphics
file formats.
This version enhances ghostscript with X windows support.

%description utils
Tools for printer maintenance: Setting default options for most laser
printers (PJL-capable printers), cartridge changing and head aligning
for inkjet winprinters.

%description -n libijs
This is the API library for programs using the IJS printer driver
plug-in interface. Printer drivers using this interface can be added
to GhostScript (6.53 or newer) without needing to rebuild
GhostScript. Application programs providing an IJS interface can make
use of IJS printer drivers directly, without needing GhostScript.

%description -n libijs-devel
This package contains the static library and the header files needed
to compile applications using this library.

%description -n libgs
Shared library for %name

%description -n libgs-devel
Development library for %name

%description classic
Classic edition of %name

%description gtk
%name with gtk

%description common
Common files for the %name

%prep
%setup -n ghostpdl-%version

rm -rf expat freetype icclib jasper jpeg lcms lcms2 libpng openjpeg zlib cups/libs

## FC apply patches
#patch1 -p1
##patch2 -p1
#patch3 -p1
#patch4 -p1
%patch5 -p1

## Ubuntu apply patches
%patch101 -p1
#patch102 -p1
#patch103 -p1
%patch104 -p1
#patch105 -p1
#patch106 -p1
#patch107 -p1
#patch108 -p1
%patch109 -p1
#patch110 -p1
#patch111 -p1
#patch112 -p1
#patch113 -p1
#patch114 -p1
#patch115 -p1
#patch116 -p1
#patch117 -p1
#patch118 -p1
#patch119 -p1
#patch120 -p1
#patch121 -p1
#patch122 -p1

## ALT apply patches
%patch500 -p1
%patch501 -p1

%build
export CFLAGS=-DA4
%autoreconf
cd ijs; %autoreconf; cd -

%configure --enable-dynamic \
	   --with-system-libtiff \
           --with-ijs \
	   --with-drivers=ALL \
	   --disable-compile-inits \
	   --with-fontpath=/usr/share/fonts/default:\
/usr/share/fonts/type1:\
/usr/share/fonts/type1/urw:\
/usr/share/fonts:\
%_datadir/ghostscript/conf.d \

cd ijs; %configure --enable-shared --disable-static; cd -

%make_build experimental

# XXX no libgpd.so in 9.27
%if "%version" == "9.27"
%make_build so || :
sed 's#-o ./bin/gpdl#-shared -Wl,-soname=libgpdl.so.9 -o ./sobin/libgpdl.so.%{version}#
s#./[^/]*obj/realmain.o ##' < obj/gpdlldt.tr > soobj/gpdlldt.tr
%endif
sh soobj/gpdlldt.tr

%make_build so

cd ijs; %make_build; cd -

%install
make install soinstall \
	prefix=$RPM_BUILD_ROOT%prefix \
	mandir=$RPM_BUILD_ROOT%_mandir \
	datadir=$RPM_BUILD_ROOT%_datadir \
	gsincludedir=$RPM_BUILD_ROOT%_includedir/ghostscript/ \
	bindir=$RPM_BUILD_ROOT%_bindir \
	libdir=$RPM_BUILD_ROOT%_libdir \
	docdir=$RPM_BUILD_ROOT%_docdir/%name-%version \
	gsdir=$RPM_BUILD_ROOT%_datadir/%name \
	gsdatadir=$RPM_BUILD_ROOT%_datadir/%name/%version \
	gssharedir=$RPM_BUILD_ROOT%_libdir/%name/%version \
	CUPSSERVERROOT=$RPM_BUILD_ROOT`cups-config --serverroot` \
	CUPSSERVERBIN=$RPM_BUILD_ROOT`cups-config --serverbin` \
	CUPSDATA=$RPM_BUILD_ROOT`cups-config --datadir`

# XXX upstream soinstall is incomplete!
cp -ap sobin/lib* %buildroot%_libdir/
for N in sobin/g*c; do T="`basename $N`"; T="${T%%c}"; install $N %buildroot%_bindir/$T; done

# XXX upstream soinstall junk
rm %buildroot%_bindir/gsc

cd ijs
    %makeinstall
cd -

rm -rf -- %buildroot%_mandir/de
rm -rf -- %buildroot%_datadir/ghostscript/%version/Resource/Font
rm -f  -- %buildroot%_bindir/ijs_{client,server}_example

# X11.so always gets loaded, even with 'gs --help'
mkdir -p %buildroot/etc/buildreqs/packages/ignore.d
echo %name-module-X >%buildroot/etc/buildreqs/packages/ignore.d/%name-module-X

mkdir -p %buildroot/%_datadir/ghostscript/conf.d
cp -a examples %buildroot%_docdir/%name-%version

%files
%files common
%doc %_docdir/%name-%version
%_datadir/ghostscript
%_datadir/ghostscript/conf.d
%_bindir/pdf2dsc
%_bindir/pdf2ps
%_bindir/gsnd

%files classic
%doc pcl/examples
%doc xps/tools
%_bindir/gs
%_bindir/gxps
%_bindir/gpcl6
%_bindir/gpdl

%files gtk
%_bindir/gsx

%files utils
%_bindir/*
#common excludes
%exclude %_bindir/gs
%exclude %_bindir/gsx
%exclude %_bindir/pdf2dsc
%exclude %_bindir/pdf2ps
%exclude %_bindir/gsnd
%exclude %_bindir/gxps
%exclude %_bindir/gpcl6
%exclude %_bindir/gpdl
%_man1dir/*

%files module-X
%_libdir/ghostscript
/etc/buildreqs/packages/ignore.d/%name-module-X

%files -n libgs
%_libdir/lib*.so.*
%exclude %_libdir/libijs*

%files -n libgs-devel
%_libdir/lib*.so
%_includedir/%name
%exclude %_libdir/libijs*

%files -n libijs
%_libdir/libijs.so.*

%files -n libijs-devel
%doc ijs/README
%_libdir/pkgconfig/*
%_libdir/libijs.so
%_includedir/ijs

%changelog
* Mon May 06 2019 Fr. Br. George <george@altlinux.ru> 9.27-alt1
- Autobuild version bump to 9.27
- Update patchset
- Manually hack upstream to build libgpdl.so

* Thu Apr  4 2019 Ivan Zakharyaschev <imz@altlinux.org> 9.26-alt3
- (.spec) make Provides and Requires match (on %%name-lib = %%version)
  (Otherwise, there would be an unmet dep when rebuilt and interpreted
  by rpm-4.13.0.1-alt6 and rpm-build with the corresponding fix.)

* Mon Jan 28 2019 Fr. Br. George <george@altlinux.ru> 9.26-alt2
- Update patchset (CVE-2019-6116)

* Wed Dec 05 2018 Fr. Br. George <george@altlinux.ru> 9.26-alt1
- Autobuild version bump to 9.26

* Thu Sep 20 2018 Fr. Br. George <george@altlinux.ru> 9.25-alt2
- More font renaming resurrected

* Tue Sep 18 2018 Fr. Br. George <george@altlinux.ru> 9.25-alt1
- Autobuild version bump to 9.25
- Resurrect font renaming patch (Closes: #35361)

* Wed Sep 05 2018 Fr. Br. George <george@altlinux.ru> 9.24-alt1
- Autobuild version bump to 9.24

* Thu Aug 23 2018 Fr. Br. George <george@altlinux.ru> 9.23-alt1
- Autobuild version bump to 9.23
- Switch to ghostpdl sources
- Introduce gspcl6 and gxps

* Thu Mar 09 2017 Fr. Br. George <george@altlinux.ru> 9.20-alt2
- Rebuild with libpng15 (Closes: #33220)

* Mon Nov 28 2016 Fr. Br. George <george@altlinux.ru> 9.20-alt1
- Autobuild version bump to 9.20
- Freshen third-party patches

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 9.19-alt1
- Autobuild version bump to 9.19
- Freshen third-party patches

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 9.16-alt1
- Autobuild version bump to 9.16
- Freshen third-party patches

* Mon Sep 29 2014 Fr. Br. George <george@altlinux.ru> 9.15-alt1
- Autobuild version bump to 9.15
- Freshen third-party patches

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 9.14-alt1
- Autobuild version bump to 9.14
- Freshen third-party patches
- Provide semi-automatic FC and Ubuntu patch sucker

* Fri Nov 08 2013 Andriy Stepanov <stanv@altlinux.ru> 9.10-alt2
- Fix version definition

* Fri Nov 01 2013 Andriy Stepanov <stanv@altlinux.ru> 9.10-alt1
- New version

* Mon Apr 22 2013 Fr. Br. George <george@altlinux.ru> 9.07-alt1
- Autobuild version bump to 9.07
- Update FC patchset
- Build with system freetype

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.05-alt1.1
- Rebuilt with libpng15

* Wed Feb 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 9.05-alt1
- 9.05

* Thu Sep 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.04-alt2
- resurrect ghostscript-alt-gstoraster-avoid-buidroot.patch (ALT #25465)

* Wed Aug 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.04-alt1
- 9.04
- update fedora patches

* Mon Aug 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.02-alt3
- add %_datadir/%name/conf.d to fontpath (ALT #25997)

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.02-alt2
- avoid buildroot-ed paths in gstoraster (ALT #25465)

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.02-alt1
- 9.02
- update fedora patches
- add ghostscript-classic to ghostscript-common Requires (ALT #25373)

* Thu Mar 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.01-alt2
- add libpng-devel to BuildRequires

* Mon Feb 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.01-alt1
- 9.01
- update fedora patches

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.00-alt2
- Add fedora patches:
    ghostscript-rh-gdevcups-691733.patch (ALT #24832)
    ghostscript-rh-icc-fix.patch
    ghostscript-rh-scan_token.patch

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 9.00-alt1
- 9.00
- CVE-2010-2055

* Sat Mar 13 2010 Stanislav Ievlev <inger@altlinux.org> 8.71-alt1
- 8.71

* Mon Nov 02 2009 Stanislav Ievlev <inger@altlinux.org> 8.70-alt3
- fix deps:
  * drop unused ghostscript-rip provides
  * module-X and utils subpackage now require ghostscript-classic instead of ghostscript-rip

* Thu Oct 01 2009 Stanislav Ievlev <inger@altlinux.org> 8.70-alt2
- fix header files names in ghostscript devel library

* Mon Sep 14 2009 Stanislav Ievlev <inger@altlinux.org> 8.70-alt1
- 8.70
- join minimal and classic subpackages
- drop espgs-alt-visibility patch, because X11.so driver uses some
  internal symbols from the library

* Fri Apr 17 2009 Stanislav Ievlev <inger@altlinux.org> 8.64-alt4
- CVE-2009-0196, CVE-2009-0792

* Fri Mar 20 2009 Stanislav Ievlev <inger@altlinux.org> 8.64-alt3
- CVE-2009-0583, CVE-2009-0584

* Wed Mar 11 2009 Kirill Maslinsky <kirill@altlinux.ru> 8.64-alt2
- rebuilt to eliminate dependency on tetex-dvips (closes: #19128)
- removed calls to %%post(un)_ldconfig

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 8.64-alt1
- 8.64

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 8.63-alt1.1
- A4 definition added

* Fri Oct 03 2008 Stanislav Ievlev <inger@altlinux.org> 8.63-alt1
- 8.63

* Thu May 08 2008 Stanislav Ievlev <inger@altlinux.org> 8.62-alt1
- 8.62
- rename ghostscript-lib to libgs, add devel part

* Thu Mar 27 2008 Stanislav Ievlev <inger@altlinux.org> 8.60-alt3
- build for Sisyphus with changes from at@: spec: ghostscript-module-X11 ignore file for buildreq

* Thu Feb 28 2008 Stanislav Ievlev <inger@altlinux.org> 8.60-alt2
- CVE-2008-0411

* Thu Nov 08 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt1
- remove deps on ghostscript-drivers

* Mon Aug 06 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt0.3
- improve latest hack

* Mon Aug 06 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt0.2
- fix build on i586

* Fri Aug 03 2007 Stanislav Ievlev <inger@altlinux.org> 8.60-alt0.1
- 8.60 (test build)
- disable jasper library (ghostscript can work with internal copy of library)

* Thu Jun 28 2007 Kirill A. Shutemov <kas@altlinux.ru> 8.15.4-alt1.1
- Drop BuildPreReq: kernel-headers-std

* Thu Mar 15 2007 Stanislav Ievlev <inger@altlinux.org> 8.15.4-alt1
- 8.15.4 (bugfix release)

* Thu Jan 25 2007 Stanislav Ievlev <inger@altlinux.org> 8.15.3-alt0.3
- apply 64 fix from RH (bug #177763 in bugzilla.redhat.com)

* Fri Dec 29 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.3-alt0.2
- Change default visibility for the libraries (avm)

* Fri Oct 13 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.3-alt0.1
- 8.15.3

* Wed May 24 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.2-alt0.1
- 8.15.2

* Thu Mar 23 2006 Stanislav Ievlev <inger@altlinux.org> 8.15.1-alt0.1
- 8.15.1

* Fri May 13 2005 Stanislav Ievlev <inger@altlinux.org> 8.15.0-alt0.1
- 8.15
- all additional drivers are in separate package now

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 7.07.1-alt6.1
- Rebuilt with libstdc++.so.6.

* Thu Oct 07 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt6
- turn off fontconfig patch (author of this patch RH has been discovered some strange problems)

* Wed Sep 22 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt5
- driver updates

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 7.07.1-alt4.1.1
- Rebuilt with libtiff.so.4.

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 7.07.1-alt4.1
- Rebuilt with openssl-0.9.7d.

* Tue May 11 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt4
- fix bootstrap

* Wed May 05 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt3
- added ppmtomd driver
- added support for KRGB (from hpijs 1.6)
- don't build cat files (was problems with building in hasher)

* Mon Mar 15 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt2
- update epsonepl driver to add support for EPL6200L

* Fri Feb 13 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt1
- fix requires (urw-fonts) in common package.

* Tue Feb 10 2004 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.4
- rename back to ghostscript (to minor problems on update)
- added pentaxpj driver for Pentax PocketJet printers

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.3
- correct fontpath (was problems with printing Japanese)
- added lexmark Z11 driver

* Tue Dec 02 2003 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.2
- added epsonepl driver
- Daedalus release

* Thu Nov 06 2003 Stanislav Ievlev <inger@altlinux.org> 7.07.1-alt0.1
- 7.07.1
- change font path
- fix requires module-X and drivers (added virtual providing %name-rip)

* Fri May 16 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.8
- added pnm2ppa and pbm2ppa (old version of pnm2ppa) drivers for HP PPA WinPrinters
- fix requires (classic doesn't need lib)

* Wed May 07 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.7
- added CID support

* Wed Apr 30 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.6
- added module X11 feature
- pdf2dsc, pdf2ps moved to common like in gnu ghostscript (gv need it)
- added ml85p driver (Samsung ML-85G and QL-85G winprinters)

* Mon Apr 07 2003 Stanislav Ievlev <inger@altlinux.ru> 7.05.6-alt0.5
- Initial release

