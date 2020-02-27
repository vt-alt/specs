%def_with qt5

%ifarch %ix86
# libinterp/corefcn/eig.cc-tst segfaults
%def_disable check
%endif

Name: octave
Version: 5.2.0
Release: alt1

%define docdir %_defaultdocdir/%name-%version

Summary: GNU Octave -- a high-level language for numerical computations
License: GPLv3
Group: Sciences/Mathematics

Url: http://www.octave.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version-%release.tar
Source1: octave.filetrigger
Source2: %name.watch

Patch0: octave-include-pcre.patch
Patch1: octave-alt-desktop-l10n.patch
Patch2: octave-alt-fix-build.patch
Patch3: octave-alt-fix-doc-build.patch
Patch4: assume-blas-integer-size.patch

BuildRequires: flex gcc-c++ gcc-fortran libcurl-devel libfftw3-devel libglpk-devel
BuildRequires: libhdf5-devel liblapack-devel libncurses-devel libpcre-devel
BuildRequires: libreadline-devel libstdc++-devel libtinfo-devel libX11-devel libXext-devel
BuildRequires: libSM-devel libICE-devel liblcms-devel bzlib-devel libltdl-devel
BuildRequires: libGraphicsMagick-c++-devel libGL-devel libGLU-devel libfreetype-devel
BuildRequires: libftgl-devel zlib-devel desktop-file-utils gnuplot less
BuildRequires: texlive-base-bin texlive-generic-recommended
BuildRequires: libarpack-ng-devel libXcursor-devel
%if_with qt5
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-tools-devel
BuildRequires: libqscintilla2-qt5-devel
%else
BuildRequires: libqt4-devel
BuildRequires: libqscintilla2-qt4-devel
%endif
BuildRequires: icoutils librsvg-utils
BuildPreReq: libqhull-devel fontconfig-devel libfltk-devel
BuildPreReq: libqrupdate-devel libsuitesparse-devel gperf libXft-devel
BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel
BuildPreReq: libXfixes-devel
BuildPreReq: java-devel-default libX11-devel libgl2ps-devel libncurses-devel libpcre-devel libsuitesparse-devel libtinfo-devel llvm-devel pkgconfig(fontconfig) pkgconfig(freetype2) pkgconfig(portaudio-2.0) pkgconfig(sndfile) pkgconfig(xft) texinfo

Provides:  qtoctave = %EVR
Obsoletes: qtoctave < %EVR
Requires: gnuplot

%package devel
Summary: GNU Octave -- development part
Group: Development/C
Requires: %name = %version-%release

%package doc
Summary: GNU Octave -- documentation
Group: Development/Other
BuildArch: noarch

Summary(ru_RU.UTF-8): GNU Octave -- высокоуровневый язык для численных методов

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%description devel
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

This package contains development libraries and header files.

%description doc
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

This package contains extra documentation for GNU Octave.

%description -l ru_RU.UTF-8
GNU Octave является высокоуровневым языком, в первую очередь предназначенным
для численных методов. Он предоставляет удобный командно-строчный интерфейс
для решения линейных и нелинейных задач в численном виде, а также для иных
численных экспериментов с применением языка, в основном совместимого с Matlab.
Также может применяться для неинтерактивных расчётов.

Octave имеет широкий набор средств для решения общих численных задач
линейной алгебры, нахождения корней нелинейных уравнений, интегрирования
ординарных функций, манипулирования полиномами, а также интегрирования
ординарных дифференциальных и дифференциально-алгебраических уравнений.
Легко расширяется и подстраивается при помощи определяемых пользователем
функций, написанных на собственном языке Octave, или с применением
динамически загружаемых модулей, написанных на C++, C, Fortran или
иных языках.

%description -l ru_RU.UTF-8 devel
GNU Octave является высокоуровневым языком, в первую очередь предназначенным
для численных методов. Он предоставляет удобный командно-строчный интерфейс
для решения линейных и нелинейных задач в численном виде, а также для иных
численных экспериментов с применением языка, в основном совместимого с Matlab.
Также может применяться для неинтерактивных расчётов.

Этот пакет содержит библиотеки и заголовки для разработки.

%description -l ru_RU.UTF-8 doc
GNU Octave является высокоуровневым языком, в первую очередь предназначенным
для численных методов. Он предоставляет удобный командно-строчный интерфейс
для решения линейных и нелинейных задач в численном виде, а также для иных
численных экспериментов с применением языка, в основном совместимого с Matlab.
Также может применяться для неинтерактивных расчётов.

Этот пакет содержит дополнительную документацию для GNU Octave.

%define _libexecdir %_libdir

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch4 -p1

%build
%add_optflags $(pkg-config hdf5-seq --cflags) $(pcre-config --cflags)
%add_optflags $(pkg-config fontconfig --cflags) -fpermissive -lm
%undefine _configure_gettext
%autoreconf
patch -p2 < %PATCH3
%configure \
	--with-blas=openblas \
	--enable-dl \
	--enable-shared \
	--disable-static
##smp-unaware
#export NPROCS=7
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages

gzip -c ChangeLog >ChangeLog.gz

# Install the filetrigger for packages:
install -pm0755 -D %SOURCE1 %buildroot%_rpmlibdir/%name.filetrigger

# required to suppress verify-elf warnings
mkdir -p %buildroot%_rpmmacrosdir
_octave_libs=
for lib in `ls %buildroot%_libdir/%name/%version/lib*.so.?`; do
    lib=${lib##%buildroot}
    _octave_libs="$_octave_libs $lib"
done
cat > %buildroot%_rpmmacrosdir/%{name}.env <<EOF
export RPM_LD_PRELOAD_octave='$_octave_libs'
export RPM_FILES_TO_LD_PRELOAD_octave='%_libdir/%name/packages/*'
EOF

mkdir -p %buildroot%_datadir/doc/%name-doc-%version

mkdir -p %buildroot%_datadir/appdata
mv %buildroot%_datadir/metainfo/*.xml %buildroot%_datadir/appdata

%check
%make check

%files
%doc BUGS COPYING NEWS* README ChangeLog.gz
%_bindir/%{name}*
%_datadir/%name
%_libdir/%name/%version/*.so*
%_libdir/%name/%version/exec
%_libdir/%name/%version/oct
%exclude %_libdir/%name/%version/*.la*
%dir %_libdir/%name
%dir %_libdir/%name/%version
%dir %_libdir/%name/packages
%_infodir/octave.info*
%_infodir/liboctave.info*
%_man1dir/*
%_desktopdir/*.desktop
%_datadir/appdata/*.appdata.xml
%_datadir/icons/hicolor/*/apps/octave.png
%_datadir/icons/hicolor/*/apps/octave.svg
%_rpmlibdir/%name.filetrigger

%files devel
%_includedir/%name-%version
%_bindir/mkoctfile
%_bindir/mkoctfile-%version
%_rpmmacrosdir/%{name}.env
%_pkgconfigdir/*.pc

%files doc
%doc doc/interpreter/octave.html doc/liboctave/liboctave.html
%doc doc/interpreter/octave.pdf doc/liboctave/liboctave.pdf
%doc doc/refcard/refcard*.pdf

%changelog
* Tue Feb 18 2020 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 5.1.0-alt3
- added Russian package summary/description
- re-enabled %%check section (except for i586 where it fails)
- minor spec cleanup

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt2
- to Sisyphus with octave modules rebuild

* Thu May 30 2019 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt4
- Add Russian localization for Comment in desktop file (ALT #36812).

* Tue Feb 26 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Wed Feb 20 2019 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt3
- Fixed FTBFS (Add libXcursor to BR's).

* Thu Nov 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.1-alt2
- rebuilt with recent GraphickMagick

* Tue Sep 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt1.1
- Rebuild with libarpack-ng 3.6.3.

* Mon Aug 13 2018 Cronbuild Service <cronbuild@altlinux.org> 4.4.1-alt1
- repocop cronbuild 20180813. At your service.

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version.
- Build with Qt5.
- Obsoletes qtoctave.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version.

* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt4
- Rebuilt with libsuitesparse 5.1.2.

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt3
- Rebuilt with qscintilla2 2.10.1.

* Wed Jul 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt2
- Rebuilt with new libsuitesparse

* Thu May 11 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version
- Add Russian localization to desktop file

* Sun Jul 03 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.3-alt1
- repocop cronbuild 20160703. At your service.

* Sun Apr 24 2016 Anton Midyukov <antohami@altlinux.org> 4.0.2-alt2
- change cronbuild_mailto="Anton Midyukov <antohami@altlinux.org>"

* Fri Apr 22 2016 Cronbuild Service <cronbuild@altlinux.org> 4.0.2-alt1
- repocop cronbuild 20160422. At your service.

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2
- added octave.env for proper verfy-elf

* Sun Mar 27 2016 Anton Midyukov <antohami@altlinux.org> 4.0.1-alt1
- New version
- Added missing buildrequires.

* Tue Jun 30 2015 Paul Wolneykien <manowar@altlinux.org> 4.0.0-alt1
- repocop cronbuild 20150630. At your service.

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.8.2-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1.1
- Rebuilt with qscintilla2 2.9

* Mon Oct 06 2014 Paul Wolneykien <manowar@altlinux.org> 3.8.2-alt1
- repocop cronbuild 20141006. At your service.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1.1
- Rebuilt with updated libglpk

* Wed Mar 12 2014 Paul Wolneykien <manowar@altlinux.ru> 3.8.1-alt1
- repocop cronbuild 20140312. At your service.

* Wed Jan 15 2014 Paul Wolneykien <manowar@altlinux.org> 3.8.0-alt2
- Own unowned dirs.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.org> 3.8.0-alt1
- Fix the requirement string splitting (patch).
- Desktop file runs GUI version (patch).
- Build with GUI (QT4).
- Build with the arpack (ng) library.

* Mon Jan 13 2014 Paul Wolneykien <manowar@altlinux.ru> 3.8.0-alt1
- repocop cronbuild 20140113. At your service.

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.4-alt4.1
- Fixed build

* Tue Jul 02 2013 Paul Wolneykien <manowar@altlinux.org> 3.6.4-alt4
- Rebuild with a new version of libhdf5.

* Wed Jun 26 2013 Paul Wolneykien <manowar@altlinux.org> 3.6.4-alt3
- Rebuild with the new version of libfltk: v1.3.0.r9945.

* Fri Jun 21 2013 Paul Wolneykien <manowar@altlinux.org> 3.6.4-alt2
- Rebuild with the new version of libglpk: 4.51.

* Wed Apr 10 2013 Paul Wolneykien <manowar@altlinux.org> 3.6.4-alt1
- Update to the new upstream release 3.6.4 with the help of cronbuild scripts.
- Update the cronbuild scripts to use the update-source-functions package.

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1.1
- Rebuilt with glpk 4.48

* Mon Sep 10 2012 Paul Wolneykien <manowar@altlinux.ru> 3.6.3-alt1
- Remote the fltk patch (already applied).
- Fix/update the pcre.h patch.
- Build v3.6.3 with the help of cronbuild scripts.
- Add cronbuild scripts.
- Move sources to the subdirectory, patches to the top.

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2.3
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2.2
- Fixed build

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2.1
- Rebuilt with libhdf5-7

* Tue Jul 05 2011 Paul Wolneykien <manowar@altlinux.ru> 3.4.0-alt2
- Remove the curl/types.h inclusion.

* Tue Apr 26 2011 Paul Wolneykien <manowar@altlinux.ru> 3.4.0-alt1
- Octave v3.4.0.

* Mon Apr 25 2011 Paul Wolneykien <manowar@altlinux.ru> 3.2.4-alt2.2
- Add filetrigger for packages.

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt2.1
- Built with GotoBLAS2 instead of ATLAS

* Mon Apr 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.4-alt2
- rebuilt with recent ftgl

* Tue Dec 07 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.4-alt1
- 3.2.4 released

* Sun Jan 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.3-alt2
- explicitly claim ownership of %%docdir

* Fri Nov 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.3-alt1
- 3.2.3 released

* Sun May 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.5-alt1
- 3.0.5 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt2
- obsolete by filetriggers macros removed

* Mon Sep 15 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Sun Dec 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt1
- 3.0.0 released

* Sat Nov 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.17-alt2
- octave headers separated to devel subpackage
- redundant reqs on emacsen filtered out

* Thu Nov 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.17-alt1
- 2.9.17 released

* Mon Aug 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.13-alt1
- 2.9.13 released

* Thu Dec 25 2003 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.52-alt1
- New version

* Tue May 06 2003 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.47-alt1
- new version

* Wed Jan 01 2003 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.40-alt1
- new unstable version

* Tue Oct 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.37-alt2
- postscript and html printable docs added, build deps fixed

* Tue Oct 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.37-alt1
- new version (unstable)

* Sun Jan 14 2001 AEN <aen@logic.ru>
- RE adaptation

* Wed Sep 13 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-6mdk
- Rebuild with r-path (octave lib ont in /usr/lib/)

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.16-5mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-4mdk
- Macros, BM, add multiple icons sizes

* Wed Apr 12 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-3mdk
- strip oct file
- add menu entry

* Tue Mar 21 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-2mdk
- corrected for new groups

* Thu Mar 09 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
- v2.0.16

* Fri Oct 23 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.0.13.90

* Thu Jul  9 1998 Jeff Johnson <jbj@redhat.com>
- repackage in powertools.

* Thu Jun 11 1998 Andrew Veliath <andrewtv@usa.net>
- Add %%attr, build as user.

* Mon Jun 1 1998 Andrew Veliath <andrewtv@usa.net>
- Add BuildRoot, installinfo, require gnuplot, description from
  Octave's web page, update to Octave 2.0.13.
- Adapt from existing spec file.

* Tue Dec  2 1997 Otto Hammersmith <otto@redhat.com>
- removed libreadline stuff from the file list

* Mon Nov 24 1997 Otto Hammersmith <otto@redhat.com>
- changed configure command to put things in $RPM_ARCH-rehat-linux,
  rather than genereated one... was causing problems between building
  on i686 build machine.

* Mon Nov 17 1997 Otto Hammersmith <otto@redhat.com>
- moved buildroot from /tmp to /var/tmp

* Mon Sep 22 1997 Mike Wangsmo <wanger@redhat.com>
- Upgraded to version 2.0.9 and built for glibc system

* Thu May 01 1997 Michael Fulbright <msf@redhat.com>
- Updated to version 2.0.5 and changed to build using a BuildRoot
