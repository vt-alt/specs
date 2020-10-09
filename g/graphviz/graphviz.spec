%def_without bootstrap

%if_without bootstrap
# help is welcome to re-enable, fix packaging and test
%def_enable  guile
%def_enable lua
%def_disable ocaml
%def_disable php
%def_disable python2
%def_enable python3
%def_disable ruby
%def_enable tcl
%endif

%define gvdatadir %_datadir/%name
%define gvlibdir %_libdir/%name
%define gvtcldir %_libexecdir/%name/tcl

Name: graphviz
Version: 2.41.2
Release: alt4

Summary: Graphs visualization tools
License: EPL-1.0 and GPL-2.0+ with Bison-exception and CPL-1.0
Group: Publishing
Packager: Fr. Br. George <george@altlinux.org>
Url: https://www.graphviz.org
Vcs: https://gitlab.com/graphviz/graphviz
Source0: %name-%version.tar
Source2: graphviz-dot-x11-preview.desktop

Patch0:  graphviz-2.24.0-alt-perl-5.12.patch
Patch1:  graphviz-2.28.0-alt-string_h_trhow.patch
Patch2:  graphviz-2.38.0-gs-9.18-fix.patch
Patch3:  graphviz-2.41.2-alt-add-riscv64.patch

# From Fedora:
Patch40:                 graphviz-2.40.1-visio.patch
Patch41:                 graphviz-2.40.1-python3.patch
# https://gitlab.com/graphviz/graphviz/issues/1367
Patch42:                 graphviz-2.40.1-CVE-2018-10196.patch
# rhbz#1505230
Patch43:                 graphviz-2.40.1-dotty-menu-fix.patch
Patch44:                 graphviz-2.40.1-coverity-scan-fixes.patch

Requires: lib%name = %version-%release
Provides: libdotneato = %version
Obsoletes: libdotneato < %version

# Automatically added by buildreq on Wed Apr 23 2014 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gnu-config guile18 libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXext-devel libXmu-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcloog-isl4 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgmp-devel libgtk+2-devel libltdl7-devel libpango-devel libpangox-compat libpangox-compat-devel libpng-devel libqt4-core libqt4-devel libqt4-gui libstdc++-devel libwayland-client libwayland-server perl-devel pkg-config python-base rpm-build-tcl tcl tcl-devel tk xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: flex gcc-c++ groff-base imake libXaw-devel libXpm-devel libann-devel libexpat-devel libgd2-devel swig tk-devel xorg-cf-files libltdl-devel

%{?!_with_bootstrap:BuildRequires: ghostscript-utils libfreeglut-devel libglade-devel libgs-devel libgtkglext-devel libgts-devel liblasi-devel librsvg-devel}
%{?_enable_lua:BuildRequires: liblua5-devel}
%{?_enable_guile:BuildRequires: guile-devel}
%if_enabled python3
BuildRequires(pre): rpm-build-python3 python3-devel
%add_python3_path %gvlibdir/python3/
%endif

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %gvdatadir/demo/*.pl
%add_findreq_skiplist %gvdatadir/demo/*.tcl
%add_findreq_skiplist %_bindir/vimdot

%description
Graphviz is a set of graph drawing tools originally developed
at AT&T Research.

Graph drawing addresses the problem of visualizing structural
information by constructing geometric representations of abstract
graphs and networks.  Automatic generation of graph drawings has
important applications in key technologies such as database
design, software engineering, VLSI and network design and visual
interfaces in other domains.

# {{{ subpackages
%package -n lib%name
Summary: Shared libraries for %name
Group: System/Libraries

%description -n lib%name
This package includes shared libraries for %name

%package -n lib%name-devel
Summary: Header files and C programming manual for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-devel
This package includes header files for %name

%package doc
Summary: Documentation for %name
Group: Publishing
Requires: %name = %version-%release
BuildArch: noarch

%description doc
This package contains most of documentation for %name

%package graphs
Summary: Demo graphs for graphviz
Group: Graphics
Requires: %name = %version-%release
BuildArch: noarch

%description graphs
This package provides some example graphs for %name.

%package guile
Summary: Guile bindings to %name
Group: Development/Other
Requires: %name = %version-%release

%description guile
This package makes %name functionality accessible from Guile

%package lua
Summary: Lua bindings to %name
Group: Development/Other
Requires: %name = %version-%release

%description lua
This package makes %name functionality accessible from Lua

%package perl
Summary: Perl bindings to %name
Group: Development/Perl
Requires: %name = %version-%release

%description perl
This package makes %name functionality accessible from Perl

%package python3
Summary: Python bindings to %name
Group: Development/Python
Requires: %name = %version-%release

%description python3
This package makes %name functionality accessible from Python

%package ruby
Summary: Ruby bindings to %name
Group: Development/Ruby
Requires: %name = %version-%release

%description ruby
This package makes %name functionality accessible from Ruby

%package tcl
Summary: Tcl bindings to %name
Group: Development/Tcl
Requires: %name = %version-%release
Requires: tcl >= 8.4.0-alt1
Provides: tcl-tkspline = %version tcl-gd = %version
Obsoletes: tcl-tkspline < %version tcl-gd < %version

%description tcl
This package makes %name functionality accessible from Tcl

# }}}

%prep
%setup
%patch0 -p1
#patch1
%patch2 -p1
%patch3 -p1

#patch40 -p1 -b .visio
#patch41 -p1 -b .python3
#patch42 -p1 -b .CVE-2018-10196
%patch43 -p1 -b .dotty-menu-fix
%patch44 -p1 -b .coverity-scan-fixes

# XXX Hack out #!/usr/bin/lua
for N in tclpkg/gv/demo/*lua; do
	sed -i 's@#!/usr/bin/lua@#!/usr/bin/env lua@' $N
done

%ifarch %e2k
# 2.41 got hardwired arch list for libsuffix there :-/
sed -i 's,sparc64,& | e2k,' configure.ac
%endif

%build
./autogen.sh NOCONFIG
%add_optflags -DNDEBUG
# altbug #34101
sed -i 's,-Wall -ffast-math,-Wall,' configure*

# skip internal libltdl
rm -rf libltdl/ m4/ltdl.m4
subst 's|^LT|dnl LT|' configure.ac
export LIBLTDL=-lltdl

# http://lists.gnu.org/archive/html/libtool/2008-10/msg00010.html
%autoreconf --no-recursive
%configure \
	--disable-static \
	--with-pangocairo \
	--with-x \
	--with-gdk-pixbuf \
	--without-gnomeui \
	--with-gtk \
	--without-qt \
	--with-ipsepcola \
	--with-sfdp \
	--with-smyrna \
	%{subst_enable guile } \
	%{subst_enable lua } \
	%{subst_enable ocaml } \
	%{subst_enable php } \
	%{subst_enable python2 } \
	%{subst_enable python3 } \
	%{subst_enable ruby } \
	%{subst_enable tcl } \
	--disable-python \
	--disable-java \
	--disable-sharp

%make_build

%install
%makeinstall_std

# avoid %%doc, install by hand
mkdir -p %buildroot%_defaultdocdir
mv %buildroot%gvdatadir/doc %buildroot%_defaultdocdir/%name-%version
cp -a AUTHORS COPYING cpl1.0.txt ChangeLog NEWS %buildroot%_defaultdocdir/%name-%version

%if_enabled tcl
##mkdir -p %buildroot%_tcldatadir/{%name,gd,tkspline}
##cat <<EOF > %buildroot%_tcldatadir/gd/pkgIndex.tcl
##package ifneeded Gdtclft %version "load [file join \$dir .. .. .. lib tcl libgdtclft.so.0] Gdtclft"
##EOF
##cat <<EOF > %buildroot%_tcldatadir/%name/pkgIndex.tcl
##package ifneeded Tcldot %version "load [file join \$dir .. .. .. lib tcl libtcldot.so.0] Tcldot"
##package ifneeded Tclpathplan %version "load [file join \$dir .. .. .. lib tcl libtclplan.so.0] Tclpathplan"
##EOF
##cat <<EOF > %buildroot%_tcldatadir/tkspline/pkgIndex.tcl
##package ifneeded Tkspline %version "
##	package require Tk 8.3
##        load [file join \$dir .. .. .. lib tcl libtkspline.so.0] Tkspline"
##EOF

# argh, #21967
if [ ! -d %buildroot%gvtcldir ]; then
	mkdir -p "$(dirname %buildroot%gvtcldir)"
	mv %buildroot{%_libdir/%name/tcl,%gvtcldir} ||:
fi
%endif

install -m0644 -D %SOURCE2 %buildroot%_desktopdir/graphviz-dot-x11-preview.desktop

# created by %%_bindir/dot -c
touch %buildroot%gvlibdir/config

rm -f %buildroot%gvlibdir/*/lib*.la
rm -f %buildroot%gvtcldir/lib*.la
rm -f %buildroot%gvlibdir/libgvplugin_*.la
rm -fv %buildroot%_datadir/graphviz/demo/modgraph.py

# Dereference manual symlinks
mv %buildroot%_man1dir/* %buildroot%_man3dir/
cp -aL %buildroot%_man3dir/*.1 %buildroot%_man1dir/
rm -f %buildroot%_man3dir/*.1

%post
[ ! -x %_bindir/dot ] || %_bindir/dot -c >&/dev/null

%files
%_bindir/*
%_desktopdir/*.desktop
%dir %gvdatadir/
%gvdatadir/gvpr
%gvdatadir/lefty
%if_without bootstrap
#gvdatadir/gvedit
%gvdatadir/smyrna
%endif
%ghost %gvlibdir/config
%_man1dir/*
%_man7dir/*
%dir %_defaultdocdir/%name-%version/
%_defaultdocdir/%name-%version/AUTHORS
%_defaultdocdir/%name-%version/COPYING
%_defaultdocdir/%name-%version/cpl1.0.txt
%_defaultdocdir/%name-%version/ChangeLog
%_defaultdocdir/%name-%version/NEWS

%files -n lib%name
%_libdir/lib*.so.*
%dir %gvlibdir/
%gvlibdir/lib*.so.*
%gvlibdir/libgvplugin_*.so

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_man3dir/*
%exclude %_man3dir/*tcl*

%files doc
%_defaultdocdir/%name-%version/
%exclude %_defaultdocdir/%name-%version/AUTHORS
%exclude %_defaultdocdir/%name-%version/COPYING
%exclude %_defaultdocdir/%name-%version/cpl1.0.txt
%exclude %_defaultdocdir/%name-%version/ChangeLog
%exclude %_defaultdocdir/%name-%version/NEWS
%{?!_with_bootstrap:%gvdatadir/examples}

%files graphs
%gvdatadir/graphs

%if_enabled guile
%files guile
%dir %gvlibdir/guile/
%gvlibdir/guile/*.so
%endif

%if_enabled lua
%files lua
%dir %gvlibdir/lua/
%gvlibdir/lua/*.so
%_libdir/lua/*/*.so
%gvdatadir/demo/modgraph.lua
%endif

%files perl
%dir %gvlibdir/perl/
%gvlibdir/perl/gv.pm
%gvlibdir/perl/gv.so
%gvlibdir/perl/libgv_perl.so
%perl_vendor_archlib/gv.pm
%perl_vendor_archlib/gv.so
%gvdatadir/demo/modgraph.pl

%if_enabled python3
%files python3
%gvlibdir/python3/
%python3_sitelibdir/*
#gvdatadir/demo/modgraph.py
%endif

%if_enabled ruby
%files ruby
%dir %gvlibdir/ruby/
%gvlibdir/ruby/gv.so
%endif

%if_enabled tcl
%files tcl
%dir %gvtcldir/
%gvtcldir/lib*tcl*.so*
%gvtcldir/*.tcl
%_libdir/tcl*/*
%gvdatadir/demo/*.tcl
%gvdatadir/demo/pathplan*
%gvdatadir/demo/*.README
%gvdatadir/demo/*.html
%_man3dir/*tcl*
%endif

# TODO:
# - enable/fix/test language bindings

%changelog
* Tue Sep 29 2020 Michael Shigorin <mike@altlinux.org> 2.41.2-alt4
- E2K: hardwired arch list workaround for libsuffix
  (patch proposed upstream)

* Thu Mar 19 2020 Nikita Ermakov <arei@altlinux.org> 2.41.2-alt3
- Add riscv64 support.

* Sun Mar 08 2020 Dmitry V. Levin <ldv@altlinux.org> 2.41.2-alt2
- Reintroduced python3 subpackage lost in the previous package release.

* Thu Feb 27 2020 Fr. Br. George <george@altlinux.ru> 2.41.2-alt1
- update version from git release tag
- build lua and tcl modules

* Wed Jul 31 2019 Andrey Savchenko <bircoph@altlinux.org> 2.40.1-alt8
- remove e2k hack as it is needed no longer

* Wed Jul 10 2019 Sergey V Turchin <zerg@altlinux.org> 2.40.1-alt7
- build with python3

* Tue Apr 16 2019 Vitaly Lipatov <lav@altlinux.ru> 2.40.1-alt6
- add desktop file for dot -Txlib (ALT bug 27583)
- remove obsoleted linking patch

* Tue Apr 16 2019 Vitaly Lipatov <lav@altlinux.ru> 2.40.1-alt5
- build without internal libltdl (ALT bug 36596)
- applied patches from Fedora
- CVE-2018-10196

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.40.1-alt4.1
- rebuild with new perl 5.28.1

* Mon Aug 13 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.40.1-alt4
- rebuilt with recent guile

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 2.40.1-alt3
- disable build gvedit (uses qt4 and was packed in the main package)

* Sun Jun 10 2018 Michael Shigorin <mike@altlinux.org> 2.40.1-alt2
- disable -ffast-math (closes: #34101, but maybe not; thx lav@)
- E2K:
  + support e2kv4
  + prepare for lcc-1.23+
- minor spec cleanup

* Fri Jan 12 2018 Andrew Savchenko <bircoph@altlinux.org> 2.40.1-alt1.1.1.2
- E2K: binaries must be compiled with -lcxa, because plugins use
  C++ and may engage cxa.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.40.1-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.40.1-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Jan 11 2017 Michael Shigorin <mike@altlinux.org> 2.40.1-alt1.1
- BOOTSTRAP: add the knob to disable extra BRs
- E2K: drop an option unsupported by lcc

* Wed Jan 11 2017 Michael Shigorin <mike@altlinux.org> 2.40.1-alt1
- 2.40.1
  + disabled patch1
  + introduced tcl knob (off by default: disruptive spline changes)

* Tue Dec 27 2016 Michael Shigorin <mike@altlinux.org> 2.38.0-alt3
- fix build against ghostscript-9.18+ (upstream #0002604)
- drop xterm dependency (closes: #32948)

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.38.0-alt2.1
- rebuild with new perl 5.22.0

* Wed Feb 18 2015 Michael Shigorin <mike@altlinux.org> 2.38.0-alt2
- reenabled python bindings (closes: #30756)

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.38.0-alt1.1
- rebuild with new perl 5.20.1

* Wed Apr 23 2014 Michael Shigorin <mike@altlinux.org> 2.38.0-alt1
- 2.38.0
- moved tcl bindings into arch-independent prefix (closes: #21967)

* Sat Dec 07 2013 Michael Shigorin <mike@altlinux.org> 2.34.0-alt1
- 2.34.0
  + added %gvdatadir/gvpr/ scripts
- NB: there was 2.30.1-alt1 build but it wasn't pushed to sisyphus
  back then due to being potentially disruptive to p7/branch formation

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.28.0-alt5
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.28.0-alt4
- rebuilt for perl-5.16

* Fri Jul 27 2012 Fr. Br. George <george@altlinux.ru> 2.28.0-alt3
- Fix string.h incorrect functions redefinition

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 2.28.0-alt2
- rebuilt against current liblasi

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 2.28.0-alt1.1
- rebuilt for perl-5.14

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sun Mar 13 2011 Michael Shigorin <mike@altlinux.org> 2.26.3-alt2
- (re)added zlib, lipbng buildreqs (overoptimization+depdrift ate 'em?)

* Sun Mar 13 2011 Michael Shigorin <mike@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.0-alt1.3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.24.0-alt1.2
- rebuilt with perl 5.12
- added patch to fix linking

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.0-alt1.1
- rebuild with libgs.so.9

* Sat Oct 31 2009 Michael Shigorin <mike@altlinux.org> 2.24.0-alt1
- 2.24.0
  + dropped patches (merged upstream)
- enabled:
  + gtkgl, gtkglext, glade, ghostscript, gts libraries
  + sfdp neato layout engine
  + smyrna OpenGL large graph viewer
  + guile bindings
- graphs subpackage made noarch
- description cleanup

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt2.2
- noarch doc subpackage
- added gvpr.1 patch so file(1) would understand it's a manpage
  and brp-compress would brp-compress would kindly process it too

* Wed Jun 03 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt2.1
- dropped obsolete patches (weren't even applied)
- added vimdot patch per led@'s advice so as to avoid
  requisite vim dependency (and enhancing it along the way)

* Fri Apr 17 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt2
- adapted repocop patch

* Sun Apr 05 2009 Michael Shigorin <mike@altlinux.org> 2.22.2-alt1
- 2.22.2
- doc subpackage now actually contains something (#18601)
- mann pages went man3
- added liblasi support (unicode postscript output, #6489)
- extended build environment with what else was missing:
  librsvg-devel, libgtkglext-devel, libglade-devel, groff, ps2pdf
- enabled SMP build
- spec cleanup

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 2.20.3-alt3
- applied repocop patch

* Sun Nov 09 2008 Michael Shigorin <mike@altlinux.org> 2.20.3-alt2
- rebuilt against current libXaw-devel

* Sat Oct 25 2008 Michael Shigorin <mike@altlinux.org> 2.20.3-alt1
- 2.20.3: fixes for CVE-2008-4555 (boundary error in .dot parser);
  thank ldv@ for heads-up, sorry for being a bit slow with update

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 2.20.2-alt2
- added missing Provides:/Obsoletes: to tcl subpackage,
  thanks Alexei V. Mezin for stumbling upon and reporting

* Mon Sep 08 2008 Michael Shigorin <mike@altlinux.org> 2.20.2-alt1
- 2.20.2
- fixed License: (text was already included in the package but header was wrong)
- suppressed requires for demo scripts
- started reworking dynamic enabling of bindings subpackages
  + adapted perl, tcl support
  + merged tcl-gd, tcl-tkspline subpackages into -tcl
  + disabled lua, ocaml, php, python, ruby support by now
    (broken build, need to fix first)
  + split -demos and merged those into language-dependent subpackages
  + introduced -graphs subpackage (following PLD 2.20.2-0.1 spec)
- hopefully fixed #16015
- huge thanks goto led@ for finding the cause for %%add_findreq_skiplist
  to miss the given patterns (which were containing "//" after expanding
  a carefully crafted macro)

* Thu Feb 14 2008 Michael Shigorin <mike@altlinux.org> 2.16.1-alt1
- 2.16.1 (#9078, #9278)
  + removed patches
  + dotneato-config disappeared
  + tcl bindings well might have broke: moved to %gvlibdir/tcl/
- tossed in parts of Debian 2.16-3 and PLD 2.14.1-2 packages
  + added lua, perl, python, ruby bindings (could mispackage)
  + didn't add guile, java, ocaml, php, C# bindings yet
- moved %_defaultdocdir/%name to %_defaultdocdir/%name-%version
- despammed descriptions
- spec macro abuse cleanup

* Fri Nov 02 2007 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt4
- fix building

* Fri Nov 02 2007 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt3
- rebuild

* Thu Aug 02 2007 Slava Semushin <php-coder@altlinux.ru> 2.2.1-alt2.1
- NMU
- Directory /usr/share/graphviz now belongs to package (#8702)
- Spec cleanup

* Mon Jul 03 2006 Denis Smirnov <mithraen@altlinux.ru> 2.2.1-alt2
- fix build with -Wl,--as-needed

* Mon Jun 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb  9 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2
- merged dotneato in, no external consumers remain
- rest of old patches dropped, recent libgd doesn't needs them

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt3
- Moved dotneato library to separate subpackage (#4947).
- Rebuilt with libgd2-2.0.28.

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- fixed font handling via gd, see #4269

* Tue Apr 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12
- Tkspline packaged separately

* Thu Dec 11 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt2
- built with system libgd2
- .la removed from devel subpackage

* Sat Sep 20 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.10-alt1
- 1.10

* Fri May 23 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.9-alt1
- 1.9

* Mon Jan 13 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.8.10-alt3
- rebuilt in new env

* Mon Nov 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.8.10-alt2
- libgd2 now in separate package
- rebuilt with (new) system libgd2

* Mon Oct 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.8.10-alt1
- 1.8.10
- additional packages separated:
  - libgd2
  - libgd2-devel
  - tcl-gd

* Thu Jul 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.8.8-alt1
- 1.8.8

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.7.4-alt2
- rebuilt with libpng.so.3

* Wed Jul 11 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> 1.7.4-alt1
- ALT Linux adaptations.

* Thu Mar 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.7.4-3mdk
- fix word.c

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.7.4-2mdk
- bzip2 sources & diff

* Thu Jan  4 2001 Pixel <pixel@mandrakesoft.com> 1.7.4-1mdk
- initial spec

