Name: R-base
Version: 3.6.1
Release: alt1

Summary: A language for data analysis and graphics
License: GPL
Group: Sciences/Mathematics
Packager: Kirill Maslinsky <kirill@altlinux.org>

URL: http://www.r-project.org
Source: R-%version.tar
Patch: R-%version-%release.patch

# Automatically added by buildreq on Thu Mar 03 2011
BuildRequires: bzlib-devel gcc-c++ gcc-fortran libXmu-devel libjpeg-devel liblzma-devel libpango-devel libpcre-devel libpng-devel libreadline-devel libtiff-devel texlive-collection-latex texlive-dist tk-devel zlib-devel makeinfo texi2dvi libcurl-devel libcairo-devel libtre-devel rpm-build-java java-devel-default

BuildPreReq: liblapack-devel libicu-devel libgomp8-devel

%description
R is `GNU S' - A language and environment for statistical computing
and graphics. R is similar to the award-winning S system, which was
developed at Bell Laboratories by John Chambers et al. It provides a
wide variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be
linked and called at run time.

S is the statistician's Matlab and R is to S what Octave is to Matlab.

%prep
%setup -q -n R-%version
%patch -p1
rm src/extra/blas/*.f src/modules/lapack/*.f

%build
%define verid %(v=%version; IFS=.; set $v; echo "$1.$2")
%define Rhome %_libdir/R
%define Rbindir %Rhome/bin
%define Rdocdir %_docdir/R-%verid
export	lt_cv_prog_cc_static_works=no \
	ac_cv_path_R_ZIPCMD=zip ac_cv_path_R_UNZIPCMD=unzip \
	ac_cv_path_R_BROWSER=firefox ac_cv_path_R_PDFVIEWER=evince \
	ac_cv_path_PAGER='less -isR' ac_cv_prog_R_PRINTCMD=lpr
%add_optflags -fno-strict-aliasing
%configure \
	--enable-prebuilt-html \
	--enable-R-shlib --with-x \
    --disable-rpath \
	--with-system-tre \
    --with-gnu-ld \
	--with-blas=openblas --with-lapack=lapack \
	--with-tcl-config=%_libdir/tclConfig.sh --with-tk-config=%_libdir/tkConfig.sh \
	--libdir='${prefix}/%_lib' rincludedir='${prefix}/include/R' \
	rdocdir='${prefix}/share/doc/R-%verid' 

%make_build
%make_build pdf info

%install
%makeinstall_std install-pdf install-info

mv %buildroot{%Rhome/lib,%_libdir}/libR.so

# this symlink is needed for R-studio
ln -s $(relative %_libdir/libR.so %Rhome/lib/libR.so) %buildroot%Rhome/lib/libR.so

# make compatibility symlink and provides
ln -s libR.so %buildroot%_libdir/libR-2.11.so
%filter_from_provides /^libR\.so/{p;s/R/R-2.11/}

ln -s `relative %Rdocdir %Rhome/doc` %buildroot%Rhome/doc
ln -s `relative %_includedir/R %Rhome/include` %buildroot%Rhome/include

cmp %buildroot%_bindir/R %buildroot%Rhome/bin/R
ln -snfv `relative %Rhome/bin/R %_bindir/R` %buildroot%_bindir/R
cmp %buildroot%_bindir/Rscript %buildroot%Rhome/bin/Rscript
ln -snfv `relative %Rhome/bin/Rscript %_bindir/Rscript` %buildroot%_bindir/Rscript

fgrep -r %buildroot %buildroot && exit 1

mkdir -p %buildroot/etc/R
mv %buildroot%Rhome/etc/* %buildroot/etc/R/
rmdir %buildroot%Rhome/etc
ln -s `relative /etc/R %Rhome/etc` %buildroot%Rhome/etc

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=R
Comment=R - a language for statistical computing
Icon=R
Exec=R
Terminal=true
Categories=Science;Math;
EOF

# use system libtool
[ -f %buildroot%Rhome/bin/libtool ]
ln -snfv `relative %_bindir/libtool %Rhome/bin/libtool` %buildroot%Rhome/bin/libtool

%define _perl_lib_path %Rhome/share/perl
%add_findprov_skiplist %Rhome/share/perl/*.pl

rm -fv %buildroot%_infodir/dir*

%check
export TZ=""
make check

%files 
	%doc doc/NEWS README
	%_bindir/R
	%_bindir/Rscript
	%_man1dir/R.*
	%_man1dir/Rscript.*
	%_libdir/libR.so
	%_libdir/libR-2.11.so
	%_desktopdir/%name.desktop

%dir	%Rhome
%dir	%Rhome/lib
	%Rhome/lib/*

%dir	%Rbindir
	%Rbindir/R
	%Rbindir/Rscript

	%Rbindir/BATCH
	%Rbindir/Rcmd
	%Rbindir/Rd2pdf
	%Rbindir/Rdconv
	%Rbindir/Rprof
	%Rbindir/pager
	%Rbindir/Stangle
	%Rbindir/Sweave
	%Rbindir/javareconf
	%Rbindir/rtags

%dir	%Rbindir/exec
	%Rbindir/exec/R

%dir	/etc/R
%config(noreplace) /etc/R/*
	%Rhome/etc

%define R_library_path %Rhome/library
%dir	%R_library_path

%define R_library() \
%dir	%R_library_path/%1 \
	%R_library_path/%1/* \
%doc	%R_library_path/%1/html 

# avoid dependency on R-devel
%add_findreq_skiplist %R_library_path/*/include/*.h

# Priority: base
	%R_library base
	%R_library datasets
	%R_library grDevices
	%R_library graphics
	%R_library grid
	%R_library methods
	%R_library splines
	%R_library stats
	%R_library stats4
	%R_library tools
	%R_library utils
	%R_library compiler
# Priority: recommended
	%R_library KernSmooth
	%R_library MASS
	%R_library Matrix
	%R_library boot
	%R_library class
	%R_library cluster
	%R_library codetools
	%R_library foreign
	%R_library lattice
	%R_library mgcv
	%R_library nlme
	%R_library nnet
	%R_library rpart
	%R_library spatial
	%R_library survival
	%R_library parallel

	%R_library_path/translations

%dir	%Rhome/modules
	%Rhome/modules/*.so*
%dir	%Rhome/share
	%Rhome/share/*

%dir	%Rdocdir
%doc	%Rdocdir/[A-Z]*
%exclude %Rdocdir/COPYING*
	%Rhome/doc

%package -n R-full
Summary: Meta-package that installs all components of R Statitical Environment
Group: Development/Other
Requires: R-devel = %version-%release R-tcltk = %version-%release R-doc-html = %version-%release gcc-c++ gcc-fortran liblapack-devel make
BuildArch: noarch

%description -n R-full
Meta-package that installs all components of R Statitical Environment

%files -n R-full

%package -n R-devel
Summary: Development files for the R Statistical Environment
Group: Development/Other
Requires(pre,postun): R-base = %version-%release

%description -n R-devel
R is `GNU S' - A language and environment for statistical computing
and graphics. R is similar to the award-winning S system, which was
developed at Bell Laboratories by John Chambers et al. It provides a
wide variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

%files -n R-devel
%dir	%Rbindir
	%Rbindir/COMPILE
	%Rbindir/INSTALL
	%Rbindir/LINK
	%Rbindir/REMOVE
	%Rbindir/Rdiff
	%Rbindir/SHLIB
	%Rbindir/build
	%Rbindir/check
	%Rbindir/config
	%Rbindir/libtool
	%Rbindir/mkinstalldirs

%dir	%_includedir/R
	%_includedir/R/*.h
%dir	%_includedir/R/R_ext
	%_includedir/R/R_ext/*.h
	%Rhome/include

%dir	%Rhome

	%_pkgconfigdir/libR.pc

%package -n R-tcltk
Summary: Tcl/Tk Interface for the R Statistical Environment
Group: Sciences/Mathematics
Requires: R-base = %version-%release

%description -n R-tcltk
R is `GNU S' - A language and environment for statistical computing
and graphics. R is similar to the award-winning S system, which was
developed at Bell Laboratories by John Chambers et al. It provides a
wide variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

This package provides access to the platform-independent Tcl scripting
language and Tk GUI elements.

%files -n R-tcltk
%add_tcl_lib_path %R_library_path/tcltk
%dir	%R_library_path
	%R_library tcltk

%package -n R-doc-html
Summary: HTML manuals for the R Statistical Environment
Group: Sciences/Mathematics
Requires: R-base = %version-%release
BuildArch: noarch

%description -n R-doc-html
R is `GNU S' - A language and environment for statistical computing
and graphics. R is similar to the award-winning S system, which was
developed at Bell Laboratories by John Chambers et al. It provides a
wide variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

%files -n R-doc-html
%dir	%Rdocdir
%dir	%Rdocdir/html/
%doc	%Rdocdir/html/*
%dir	%Rdocdir/manual/
%doc	%Rdocdir/manual/*.html
%dir    %Rdocdir/manual/images/
%doc    %Rdocdir/manual/images/*.png


%package -n R-doc-pdf
Summary: PDF manuals for the R Statistical Environment
Group: Sciences/Mathematics
Conflicts: R-base > %version, R-base < %version
BuildArch: noarch

%description -n R-doc-pdf
R is `GNU S' - A language and environment for statistical computing
and graphics. R is similar to the award-winning S system, which was
developed at Bell Laboratories by John Chambers et al. It provides a
wide variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

%files -n R-doc-pdf
%dir	%Rdocdir
%dir	%Rdocdir/manual/
%doc	%Rdocdir/manual/*.pdf

%package -n R-doc-info
Summary: Info manuals for the R Statistical Environment
Group: Sciences/Mathematics
Conflicts: R-base > %version, R-base < %version
BuildArch: noarch

%description -n R-doc-info
R is `GNU S' - A language and environment for statistical computing
and graphics. R is similar to the award-winning S system, which was
developed at Bell Laboratories by John Chambers et al. It provides a
wide variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

%files -n R-doc-info
%_infodir/R-*.info*

%changelog
* Mon Oct 07 2019 Kirill Maslinsky <kirill@altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Sat Apr 27 2019 Kirill Maslinsky <kirill@altlinux.org> 3.6.0-alt1
- Version 3.6.0
- Built with OpenMP support

* Tue Mar 12 2019 Kirill Maslinsky <kirill@altlinux.org> 3.5.3-alt1
- Version 3.5.3
- R-full metapackage is marked as noarch

* Wed Jan 09 2019 Kirill Maslinsky <kirill@altlinux.org> 3.5.2-alt1
- Version 3.5.2

* Fri Oct 26 2018 Kirill Maslinsky <kirill@altlinux.org> 3.5.1-alt1
- Version 3.5.1
- add dependency on make to R-full
- add localization files

* Fri Jun 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt2
- Provided compatibility symlink for R-studio.

* Mon May 21 2018 Kirill Maslinsky <kirill@altlinux.org> 3.5.0-alt1
- Version 3.5.0
- change meta-package name to R-full since #34737 is still unresolved
- add dependencies on gcc-fortran, gcc-c++, liblapack-devel to R-full 
  to make installation of R packages easier for less profcient users 
  (these are the most common tools required to build R packages that are 
  commonly missing in a user's system by default).

* Thu Mar 22 2018 Kirill Maslinsky <kirill@altlinux.org> 3.4.4-alt1
- Version 3.4.4
- Add meta-package R that installs all major components 
  (R-base, R-devel, R-tcltk)
- Rebuilt with texlive-2017

* Sun Jan 14 2018 Kirill Maslinsky <kirill@altlinux.org> 3.4.3-alt1
- Version 3.4.3

* Thu May 04 2017 Kirill Maslinsky <kirill@altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Wed Mar 29 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.3.3-alt1
- Version 3.3.3

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.3.2-alt2
- NMU: rebuilt against Tcl/Tk 8.6
- Dropped a test which could not be passed from time to time

* Thu Dec 22 2016 Kirill Maslinsky <kirill@altlinux.org> 3.3.2-alt1
- Version 3.3.2

* Mon Jun 27 2016 Kirill Maslinsky <kirill@altlinux.org> 3.3.1-alt1
- Version 3.3.1

* Mon Feb 15 2016 Kirill Maslinsky <kirill@altlinux.org> 3.2.3-alt2
- rebuilt with libicu 5.6

* Sat Dec 12 2015 Kirill Maslinsky <kirill@altlinux.org> 3.2.3-alt1
- Version 3.2.3

* Wed Feb 11 2015 Kirill Maslinsky <kirill@altlinux.org> 3.1.2-alt1
- Version 3.1.2

* Mon Sep 08 2014 Kirill Maslinsky <kirill@altlinux.org> 3.1.1-alt1
- Version 3.1.1

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.15.1-alt3
- Rebuilt with icu 5.1

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.15.1-alt2
- Rebuilt with libpng15

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.15.1-alt1
- Version 2.15.1
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jan 17 2012 Kirill Maslinsky <kirill@altlinux.org> 2.14.1-alt1
- 2.12.2 -> 2.14.1

* Wed Dec 14 2011 Dmitry V. Levin <ldv@altlinux.org> 2.12.2-alt1.qa4
- Fixed coexistance with pcre >= 8.13.  Note that this queer project
  relies on PCRE internal function _pcre_valid_utf8() so it can
  suddenly break again.
- Dropped %Rhome/lib/libR.so compatibility symlink.
- Moved "make check" to %%check section.

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.12.2-alt1.qa3
- fixed misprint in desktop file category

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.12.2-alt1.qa2
- NMU: converted menu to desktop file

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt1.1
- Built with GotoBLAS2 instead of ATLAS

* Sun Feb 27 2011 Alexey Tourbin <at@altlinux.ru> 2.12.2-alt1
- 2.12.0 -> 2.12.2

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Version 2.12.0 (ALT #24511)

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 2.11.1-alt2
- Rebuilt for liblzma.so.5.

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 2.11.1-alt1
- 2.10.1 -> 2.11.1

* Sat Dec 26 2009 Alexey Tourbin <at@altlinux.ru> 2.10.1-alt1
- 2.9.2 -> 2.10.1
- enable static html pages

* Wed Sep 30 2009 Alexey Tourbin <at@altlinux.ru> 2.9.2-alt1
- 2.9.1 -> 2.9.2

* Fri Jul 17 2009 Alexey Tourbin <at@altlinux.ru> 2.9.1-alt1
- 2.9.0 -> 2.9.1
- removed install_info scriptlets

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 2.9.0-alt1
- 2.8.1 -> 2.9.0
- packaged Matrix (new library)

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 2.8.1-alt1
- 2.8.0 -> 2.8.1

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 2.8.0-alt1
- 2.7.2 -> 2.8.0
- set default R_PRINTCMD to "lpr" (#17625)

* Fri Sep 12 2008 Alexey Tourbin <at@altlinux.ru> 2.7.2-alt1
- 2.7.1 -> 2.7.2

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 2.7.1-alt1
- 2.6.2 -> 2.7.1
- set default web browser to firefox, default pdf viewer to evince
- build with external perl-Text-DelimMatch module
- made R-doc-* subpackages noarch

* Mon Mar 17 2008 Alexey Tourbin <at@altlinux.ru> 2.6.2-alt1
- 2.4.1 -> 2.6.2

* Mon Feb 19 2007 Alexey Tourbin <at@altlinux.ru> 2.4.1-alt1
- 2.3.1 -> 2.4.1
- imported sources into git and adapted for gear
- split the package into subpackages: R-base, R-devel, R-tcltk,
  R-doc-html, R-doc-pdf, R-doc-info
- relocated /usr/lib/R/doc/ to /usr/share/doc/R-2.4/,
  /usr/lib/R/include/ to /usr/include/R/, /usr/lib/R/etc/ to /etc/R/;
  provided compatibility symbolic links

* Sun Jun 04 2006 Alexey Tourbin <at@altlinux.ru> 2.3.1-alt1
- 2.3.0 -> 2.3.1 
- built with gfortran
- eliminated libtool and texi2dvi copies in %Rhome/bin/

* Wed Apr 26 2006 Alexey Tourbin <at@altlinux.ru> 2.3.0-alt1
- picked up from oprphaned
- major revision, revamped specfile
- removed menu icons (icons suck)
- removed %%post doc index update (no cran packages yet)
- relocated libR.so to %_libdir, soname=libR-2.3.so.0
- built against system zlib (#8243) and bzlib (#8249)
- also built against system BLAS and LAPACK shared libraries

* Sun Aug 01 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Mon Mar 22 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.8.1-alt1
- a new version

* Thu Oct 16 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.8.0-alt1
- a new version, library path fixed.

* Mon Jun 23 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Feb 26 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Mon Feb 10 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6.1-alt3
- new autoreq

* Tue Dec 10 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 2:1.6.1-alt2
- Building in new perl
- New snapshot path

* Thu Nov 14 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Tue Oct 16 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6.0-alt1
- 1.6.0
- gcc-3.2, automake-2.5

* Thu Jun 13 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt2
- rebuilt in new env

* Fri Mar 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Fri Dec 21 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Oct 11 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.1-alt2
- Rebuild with new libpng

* Mon Oct 01 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Jul 09 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Thu May 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.2.3-alt1
- 1.2.3. Spec cleanup.

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Fri Dec 22 2000 Giuseppe Ghib? <ghibo@mandrakesoft.com> 1.2.0-4mdk
- added PDF of Reference Manual.
- added tcl, tk in BuildRequires.

* Tue Dec 19 2000 Giuseppe Ghib? <ghibo@mandrakesoft.com> 1.2.0-3mdk
- removed stdout output in post scripts.

* Tue Dec 19 2000 David BAUDENS <baudens@mandrakesoft.com> 1.2.0-2mdk
- ExcludeArch: ppc

* Tue Dec 19 2000 Giuseppe Ghib? <ghibo@mandrakesoft.com> 1.2.0-1mdk
- new fresh release.

* Tue Dec 19 2000 Giuseppe Ghib? <ghibo@mandrakesoft.com> 1.1.1-3mdk
- fixed broken macros (aargh!).

* Sun Oct 28 2000 David BAUDENS <baudens@mandrakesoft.com> 1.1.1-2mdk
- Use %%make macro
- bzip2 patch

* Fri Sep 01 2000 Giuseppe Ghib? <ghibo@mandrakesoft.com> 1.1.1-1mdk
- initial mandrake release.
- added BuildRequires.
- added -fno-fast-math, otherwise R doesn't passes the arith checks.
- switched order of make check and make pdf.

* Wed Aug 16 2000 Martyn Plummer <plummer@iarc.fr>
- R 1.1.1 released. Removed R-1.1.0-cofig.sub-alpha.patch since
  this version uses up to date config.sub.

* Fri Jun 16 2000 Martyn Plummer <plummer@iarc.fr>
- Added patch R-1.1.0-cofig.sub-alpha.patch from Naoki Takebayashi

* Thu Jun 15 2000 Martyn Plummer <plummer@iarc.fr>
- Removed dependencies on egcs egcs-g77

* Tue Feb 29 2000 Martyn Plummer <plummer@iarc.fr
- Changed the description to match
  http://developer.r-project.org/R-description-short.txt

* Mon Feb 28 2000 Martyn Plummer <plummer@iarc.fr>
- Added egcs, egcs-g77 and perl as requirements. People who want to install
  their own R packages need a working build environment.

* Fri Feb 11 2000 Martyn Plummer <plummer@iarc.fr>
- Remove latex versions of help pages, to save a bit of space.
- PDF files installed in top level doc directory.
- Included R-0.99.0-fixes patch for some serious bugs

* Tue Feb  8 2000 Martyn Plummer <plummer@iarc.fr>
- Added patch R-refman.patch which prevents building the reference manual

* Fri Feb  4 2000 Martyn Plummer <plummer@iarc.fr>
- Updated in preparation for R-0.99.0.
- Now install manual in pdf format.

* Wed Dec 15 1999 Martyn Plummer <plummer@iarc.fr>
- R-0.90.1. Removed Naoki's memory profile patch

* Fri Dec 3 1999 Tim Powers <timp@redhat.com>
- move configure into build section
- quiet scripts
- built for Powertools-6.2

* Mon Nov 29 1999 Martyn Plummer <plummer@iarc.fr>
- Added patch from Naoki to fix problem with memory profile.
  (will be folded in to next R version).

* Mon Nov 22 1999 Martyn Plummer <plummer@iarc.fr>
- R 0.90.0 Naoki's patch for FFT bug no longer necessary.
- Updated URL tag to www.r-project.org

* Thu Oct 28 1999 Martyn Plummer <plummer@iarc.fr>
- RHCN is officially dead. Changed the Packager field
  back to my name and removed the Distribution field.

* Thu Oct 14 1999 Martyn Plummer <plummer@iarc.fr>
- Set CFLAGS and FFLAGS to be RPM_OPT_FLAGS. Thanks to
  Timothy H. Keitt <keitt@nceas.ucsb.edu>
- Simplified file list.

* Fri Oct 8 1999 Martyn Plummer <plummer@iarc.fr>
- Added patch from Naoki Takebayashi to fix FFT bug on Alpha
  (also found on Sparc).

* Tue Sep 7 1999 Martyn Plummer <plummer@iarc.fr>
  [R-base-0.65.0-1]
- RHOME is now R_HOME. Changed sed scripts accordingly.
- TASKS file is no longer in file list.

