%define ver_major 5.2
%def_with emacs

Name: gnuplot
Version: 5.2.8
Release: alt2
Epoch: 1

Summary: A program for plotting mathematical expressions and data
License: gnuplot and MIT
Group: Sciences/Other
URL: http://www.gnuplot.info/

# git://git.code.sf.net/p/gnuplot/gnuplot-main
Source0: %name-%version.tar
Source2: http://www.gnuplot.info/faq/%name-faq.html.bz2
Source3: %name.desktop
Source4: %name.menu

Source10: %name.16.png
Source11: %name.32.png
Source12: %name.48.png

Source14: gnuplot-emacs.el

Patch1: %name-alt.patch
Patch2: gnuplot-5.0.6-gentoo-no-picins.patch

BuildRequires(pre): rpm-build-tex
BuildPreReq: desktop-file-utils
BuildRequires: gcc-c++ ghostscript-module-X groff-base libXt-devel libncurses-devel libreadline-devel xorg-cf-files zlib-devel libgd3-devel libpng-devel libjpeg-devel libgif-devel
BuildRequires: texinfo latex2html
BuildRequires: dblatex
%{?_with_emacs:BuildRequires: emacs-common}

# for wxt terminal
BuildRequires: libwxGTK-devel libcairo-devel libpango-devel libgtk+2-devel
# for qt terminal
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools
# for lua/TikZ
BuildRequires: lua-devel tex(pgf.sty)

Requires(post,postun): desktop-file-utils
Requires: fonts-ttf-dejavu
Requires: %name-common-x11 = %EVR

Summary(ru_RU.UTF-8): Программа для построения графиков математических выражений и данных

%package common
Group: Sciences/Other
Summary: The common gnuplot parts
BuildArch: noarch
Conflicts: %name < %EVR

%package common-x11
Group: Sciences/Other
Summary: The common-x11 gnuplot parts
Requires: %name-common = %EVR
Conflicts: %name < %EVR

%package minimal
Group: Sciences/Other
Summary: Minimal version of program for plotting mathematical expressions and data
Requires: %name-common = %EVR

%package qt
Group: Sciences/Other
Summary: Qt interface for gnuplot
Requires: %name-common-x11 = %EVR

%package doc
Group: Documentation
Summary: Documentation of bindings for the gnuplot main application
BuildArch: noarch

%package demo
Group: Sciences/Other
Summary: Demo gnuplot applications
BuildArch: noarch

%description
Gnuplot is a command-line driven, interactive function plotting program
especially suited for scientific data representation. Gnuplot can be used to
plot functions and data points in both two and three dimensions and in many
different formats.

Install gnuplot if you need a graphics package for scientific data
representation.

%description -l ru_RU.UTF-8
Gnuplot это интерактивная программа, предназначенная для построения
графиков.  Она особенно хорошо подходит для представления научных 
данных.  Gnuplot может строить 2-х и 3-х мерные графики функций 
и числовых данных во множестве различных графических форматов.

%description common
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

This subpackage contains common parts needed for arbitrary version of gnuplot

%description common-x11
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

This subpackage contains common-x11 parts needed for arbitrary version of gnuplot

%description minimal
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.


%description qt
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

This package provides a Qt based terminal version of gnuplot

%description doc
The gnuplot-doc package contains the documentation related to gnuplot
plotting tool

%description demo
The gnuplot-demo package contains the demo applications related to gnuplot
plotting tool

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
#export CFLAGS="$RPM_OPT_FLAGS -fno-fast-math"
%ifarch %e2k
# lcc 1.23.12 is -std=c++03 by default but c++11 capable;
# src/qtterminal/qt_term.cpp compilation needs that
export CXXFLAGS+=-std=c++11
%endif

%define configure_opts --with-readline=gnu --with-png --with-pdf --enable-history-file --without-linux-vga --without-row-help --enable-thin-splines --with-texdir=%_texmfmain/%name --with-lua --with-gihdir=%name/%ver_major

sh prepare
%autoreconf

# at first create minimal version of gnuplot for server SIG purposes
mkdir minimal
cd minimal
ln -s ../configure .
%configure %configure_opts --disable-wxwidgets --without-cairo --without-qt --without-x
%make_build
cd -

# create full version of gnuplot
mkdir wx
cd wx
ln -s ../configure .
%configure %configure_opts --without-qt
%make_build
cd -

mkdir qt
cd qt
ln -s ../configure .
%configure %configure_opts --disable-wxwidgets --enable-qt
%make_build
cd -


install -p -m644 %SOURCE2 .
bunzip *.html.bz2

# Docs don't build properly out of tree
%configure  %configure_opts --with-tutorial
ln -s ../wx/src/gnuplot src/
export PERL5LIB=$(pwd)/docs:$(pwd)/docs/htmldocs
ln -s ../VERSION docs/VERSION
make -C docs html pdf
export GNUPLOT_PS_DIR=../../term/PostScript
make -C docs/psdoc ps_symbols.ps ps_fontfile_doc.pdf
rm -rf docs/htmldocs/images.idx
make -C tutorial
make -C docs gih

%install
# install wx
%makeinstall_std -C wx
# rename binary
mv %buildroot%_bindir/%name %buildroot%_bindir/%name-wx

# install qt
%makeinstall_std -C qt
# rename binary
mv %buildroot%_bindir/%name %buildroot%_bindir/%name-qt

# install minimal binary
install -p -m 755 minimal/src/%name %buildroot%_bindir/%name-minimal

# install docs
%makeinstall_std -C docs

# Add alternatives for gnuplot
mkdir -p %buildroot%_altdir
printf '%_bindir/%name\t%_bindir/gnuplot-minimal\t10\n' > %buildroot%_altdir/%name-minimal
printf '%_bindir/%name\t%_bindir/gnuplot-wx\t20\n' > %buildroot%_altdir/%name-wx
printf '%_bindir/%name\t%_bindir/gnuplot-qt\t30\n' > %buildroot%_altdir/%name-qt

# menus
install -D -pm644 %SOURCE3  %buildroot%_desktopdir/%name.desktop

# icon
install -D -pm644 %SOURCE10  %buildroot/%_miconsdir/%name.png
install -D -pm644 %SOURCE11  %buildroot/%_niconsdir/%name.png
install -D -pm644 %SOURCE12  %buildroot/%_liconsdir/%name.png

# help data
cp docs/%{name}.gih %buildroot%_datadir/%name/%ver_major/

# cleanup before add to doc
rm -f demo/Makefile*
rm -f demo/html/Makefile*

%files
%_bindir/gnuplot-wx
%_altdir/%name-wx

%files common
%_mandir/man?/*
%_datadir/%name
%exclude %_datadir/%name/%ver_major/qt
%_desktopdir/*
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%_texmfmain/%name
%dir %_libexecdir/%name
%dir %_libexecdir/%name/%ver_major

%files common-x11
%_libexecdir/%name/%ver_major/%{name}_x11

%files minimal
%_bindir/gnuplot-minimal
%_altdir/%name-minimal

%files qt
%_bindir/%name-qt
%_altdir/%name-qt
%_libexecdir/%name/%ver_major/%{name}_qt
%_datadir/%name/%ver_major/qt

%files doc
%doc ChangeLog Copyright BUGS README NEWS RELEASE_NOTES
%doc tutorial/tutorial.dvi gnuplot-faq.html
%doc docs/psdoc/ps_* docs/gnuplot.pdf docs/htmldocs

%files demo
%doc demo

%changelog
* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 1:5.2.8-alt2
- Fix desktop file (Closes: 37306).

* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 1:5.2.8-alt1
- Build new version 5.2.8.

* Thu May 30 2019 Grigory Ustinov <grenka@altlinux.org> 1:5.2.7-alt1
- Build new version.

* Wed May 08 2019 Michael Shigorin <mike@altlinux.org> 1:5.2.6-alt2
- fixed build with lcc on e2k
- introduced emacs knob (on by default)
- minor spec cleanup

* Sat Jan 05 2019 Grigory Ustinov <grenka@altlinux.org> 1:5.2.6-alt1
- Build new version.

* Mon Oct 08 2018 Grigory Ustinov <grenka@altlinux.org> 1:5.2.5-alt1
- Build new version.

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 1:5.2.4-alt1
- Build new version.

* Fri May 25 2018 Grigory Ustinov <grenka@altlinux.org> 1:5.2.3-alt2
- Removed PDFLib-Lite from build requires (Closes: #33946).

* Fri May 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.2.3-alt1
- Updated to upstream version 5.2.3.

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.0.3-alt1.2
- NMU: build with texlive 2017

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.0.3-alt1.1
- rebuild with new lua 5.3

* Fri May 27 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:5.0.3-alt1
- 5.0.3
- Update with latest relase
- Remove emacs-mode-gnuplot due gnuplot-mode (emacs plugin)
  now maintained as a separate project

* Tue Dec 16 2014 Alexey Shabalin <shaba@altlinux.ru> 1:4.6.6-alt1
- 4.6.6
- fixed gnuplot_qt (ALT#30519)

* Wed Jan 22 2014 Alexey Shabalin <shaba@altlinux.ru> 1:4.6.4-alt2
- add common, common-x11, minimal, qt, doc, demo packages and alternatives
- build with texlive

* Tue Jan 21 2014 Alexey Shabalin <shaba@altlinux.ru> 1:4.6.4-alt1
- 4.6.4
- update fonts paths
- define ttffont as DejaVuSans.ttf
- add fedora patches

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:4.4.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for gnuplot

* Fri Mar 26 2010 Alexey Morsov <swi@altlinux.ru> 1:4.4.0-alt2
- add wxt terminal support
- fix .gih file location

* Thu Mar 18 2010 Alexey Morsov <swi@altlinux.ru> 1:4.4.0-alt1
- new version

* Wed Sep 09 2009 Alexey Morsov <swi@altlinux.ru> 1:4.2.6-alt1
- new version
- fix desktop file

* Thu Aug 20 2009 Alexey Morsov <swi@altlinux.ru> 1:4.2.5-alt2
- fix #21142

* Thu Apr 23 2009 Alexey Morsov <swi@altlinux.ru> 1:4.2.5-alt1
- new version

* Thu Dec 11 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.4-alt1
- new version
- remove deprecated macro from post/postun

* Fri Aug 29 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt4.1
- fix build
  + remove _target_cpu macro
  + put make_build macro back

* Tue Aug 19 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt4
- fix build on i586
  + use make instead make_build macro (no smp)

* Wed Aug 13 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt3
- fix build
  + get support for png/jpeg terminal back

* Tue Jun 24 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt2
- build emacs-mode-gnuplot (obsolute emacs-gnuplot)

* Fri May 16 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt1
- new version
- clean build requires
- fix iconsdir to correspond with policy
- patch desktop file to correspond with policy

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 1:4.2.2-alt1
- version 4.2.2
- bug fixes

* Thu May 03 2007 Alexey Morsov <swi@altlinux.ru> 1:4.2.0-alt2
- add some configure keys for better ploting and
fixing work with help and CLI (by const@)
- create .desktop 

* Mon Mar 05 2007 Alexey Morsov <swi@altlinux.ru> 1:4.2.0-alt1
- new release (4.2)
- disable lisp part totaly

* Fri Dec 15 2006 Alexey Morsov <swi@altlinux.ru> 4.2.rc2-alt1
- new version
- fix spec for tutorial
- fix patch0 for new version

* Wed Nov 02 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 4.0.0-alt3
- [Bug 8361] x86_64 support request

* Wed Jun 22 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 4.0.0-alt2
- bugfix; removed emax-mode-* packages

* Tue May 18 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 4.0.0-alt1
- new version

* Mon Mar 17 2003 Stanislav Ievlev <inger@altlinux.ru> 3.7.3-alt1
- new version

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 3.7.2-alt1
- 3.7.2
- added subpackages for emacs modes
- added packager tag

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.7.1-ipl16mdk
- Rebuilt with libpng.so.3

* Sun Sep 16 2001 Rider <rider@altlinux.ru> 3.7.1-ipl14mdk
- BuildRequires fix

* Sun Aug 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-13mdk
- now should also compile on non x86 arch, /me sucks

* Fri Aug 25 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-12mdk
- removed -ffast-math option to improve reliability

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-11mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.7.1-10mdk
- automatically added BuildRequires

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-9mdk
- BM
- macroweruivieruweiovjzations

* Fri Apr 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-8mdk
- fixed menu entry adding 32x32 icon

* Fri Apr 28 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 3.7.1-7mdk
- added XFree86-devel in BuildPreReq for X11.
- removed bzip2 man pages (done by spec_helper).
- removed gnu-readline and put back minimal-readline otherwise the
  Boer's patch doesn't work.

* Mon Apr 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-6mdk
- fix directory owns.
- now uses gnu readline library instead of minimal built-in readline.

* Mon Apr 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-5mdk
- added icon.

* Thu Mar 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-4mdk
- new groups.
- menu entry.

* Thu Nov 11 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- added Pieter de Boer's patch <ptdeboer@cs.utwent.nl> for splot X11
  interactive rotations.
- added gnuplot-mode documentation.

* Tue Nov  9 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- updated to 3.7.1.
- added gnuplot-faq.html.
- added PDF documentation.

* Mon Nov  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.7.0.2.
- fix license.
- add emacs-mode.
- add some documentation.

* Fri Oct 1 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- Changed the 3.7.0->3.7.0.1 patch to a more recent version because
the previous version has broken the postscript terminal.

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rebuild without svgalib.

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update to 3.7.0.1.

* Tue May 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.7.

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.6beta347

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
