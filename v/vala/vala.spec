# Vala is written in Vala itself. To solve bootstrap problem we pre-compile it to C
# and use those C sources during bootstrap phase. Next package rebuilds must be done
# without bootstrap define.
%def_disable snapshot
%def_enable check
%{?_enable_snapshot:%def_with bootstrap}
%define ver_major 0.44
%define api_ver 0.44

Name: vala
Version: %ver_major.4
Release: alt1

Summary: Vala is a programming language which makes GNOME programming easy
Group: Development/C
License: LGPL
Url: https://wiki.gnome.org/Projects/Vala

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
%if_with bootstrap
Patch: %name-%version-%release-pregenerated.patch
%endif
Patch1: %name-0.39.7-alt-fixes.patch

Requires(pre): rpm-build-vala vapi-common = %version-%release

BuildRequires: flex libgio-devel >= 2.40.0 xsltproc help2man dbus-tools-gui gobject-introspection-devel
BuildRequires: /proc rpm-build-vala
# since 0.37
BuildRequires: libgraphviz-devel
%if_without bootstrap
BuildRequires: vala >= 0.39.5.8
%endif

%description
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

Vala is designed to allow access to existing C libraries, especially GObject-based
libraries, without the need for runtime bindings. Each to be used library requires a Vala
API file at compile-time, containing the class and method declarations in Vala
syntax. Vala currently comes with experimental bindings for GLib and GTK+. It's planned to
provide generated bindings for the full GNOME Platform at a later stage.

%package -n vapi-common
Summary: Common empty package with dir for vapi files
Group: Development/Other
BuildArch: noarch
Provides: %_datadir/vala/vapi

%description -n vapi-common
Common empty package with dir for vapi files.

%package -n lib%name-devel
Summary: Development files for embedding Vala translator
Group: Development/C
Requires: %name = %version-%release

%description -n lib%name-devel
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

This package contains infrastructure files to embed Vala translator into your programs

%package doc
Summary: Documentation for Vala programming language
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description doc
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

This package contains Vala documentation for GNOME DevHelp.

%package tools
Summary: Tools for creating Vala API specifications and new projects
Group: Development/C
Requires: %name = %version-%release

%description tools
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

This packages contains additional tools to generate Vala projects and API specifications
for existing C and C++ libraries.

%package -n valadoc
Summary: Vala documentation generator
Group: Development/Other
Conflicts: %name < %version

%description -n valadoc
Valadoc is a documentation generator for Vala projects. It extracts
source code from Vala source files and can output various formats of
documentation like GTK-Doc or GIR documentation.

%package -n valadoc-devel
Summary: Vala documentation generator (devel package)
Group: Development/Other
Requires: valadoc = %version-%release

%description -n valadoc-devel
Development files for Valadoc.

%prep
%setup
%patch1 -p1 -b .alt_fixes

# Automake now requires to have ChangeLog and m4, fake them
[ ! -f ChangeLog ] && touch ChangeLog
[ ! -d m4 ] && mkdir m4

# version in .tarball-version file
%{?_with_bootstrap:echo "%version" > .tarball-version}

# whether external bootstrapping is in use or not we always want to build
# a compiler with the compiler itself. So first compile an intermediate
# (bootstrapping) compiler in a separate directory

%if_with bootstrap
# create a copy of sources. it's not that neat but otherwise
# our bootstrapping patch would "taint" sources used for
# the final build

mkdir bootstrap-build
# copy everythig but bootstrap-build recursively to bootstrap-build
find ./ -mindepth 1 -maxdepth 1 \( -name 'bootstrap-*' -prune -o \
	-exec cp -pr {} bootstrap-build \; \)
cd bootstrap-build
# apply pregenerated patch
%patch0 -p1
cd ..
%else
# use the directory for the "off-source" build
mkdir bootstrap-build
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf

# build an intermediate version of the compiler
BSINSTALL=$(pwd)/bootstrap-install
mkdir "$BSINSTALL"

cd bootstrap-build

%if_with bootstrap
autoreconf -v --install
./configure --prefix="$BSINSTALL"

# Make stamps for pregenerated source code so that Vala build system would not run valac again
for i in vala codegen ccode gee ; do
    touch $i/$i.vala.stamp
done
touch vapigen/{vapigen,vapicheck}.vala.stamp
touch compiler/valac.vala.stamp
%else
../configure --prefix="$BSINSTALL"
%endif

%make
make install
cd ..

# now build a pristine variant of the compiler to be packaged
OLD_PATH="$PATH"
export PATH="$BSINSTALL/bin:$PATH"
%configure
# Delete stamps to force re-generation of C code with bootstrapped valac
find . -name '*.stamp' | xargs -r rm
%make
rm -rf bootstrap-build "$BSINSTALL"
export PATH="$OLD_PATH"

%install
%makeinstall_std
# own this directory for third-party *.vapi files
mkdir -p %buildroot%_datadir/vala/vapi

%check
%make check

%files
%_bindir/valac
%_bindir/valac-%api_ver
%_bindir/vala
%_bindir/vala-%api_ver
%_libdir/lib%name-%api_ver.so.*
%dir %_libdir/%name-%api_ver
%_libdir/%name-%api_ver/libvalaccodegen.so
%_man1dir/valac*
%dir %_datadir/vala-%api_ver
%dir %_datadir/vala-%api_ver/vapi
%_datadir/vala-%api_ver/vapi/*
%_datadir/%name/vapi/lib%name-%api_ver.vapi
%doc AUTHORS COPYING NEWS README THANKS

%exclude %_libdir/%name-%api_ver/*.la

%files -n vapi-common
%dir %_datadir/vala
%dir %_datadir/vala/vapi

%files -n lib%name-devel
%_includedir/vala-%api_ver
%_pkgconfigdir/*.pc
%exclude %_pkgconfigdir/valadoc*.pc
%_libdir/lib%name-%api_ver.so
%_datadir/aclocal/%name.m4
%_datadir/aclocal/vapigen.m4
%exclude %_pkgconfigdir/vapigen*.pc
%exclude %_datadir/aclocal/vapigen.m4

%files doc
%_datadir/devhelp/books/%name-%api_ver

%files tools
%_bindir/vapigen
%_bindir/vapigen-%api_ver
%_bindir/vala-gen-introspect
%_bindir/vala-gen-introspect-%api_ver
# dropped in 0.39.91
#%_bindir/vapicheck
#%_bindir/vapicheck-%api_ver
%_pkgconfigdir/vapigen*.pc
%_datadir/aclocal/vapigen.m4
%_datadir/vala/Makefile.vapigen
%_libdir/vala-%api_ver/gen-introspect-%api_ver
%_man1dir/vala-gen-introspect*
%_man1dir/vapigen*

%files -n valadoc
%_bindir/valadoc
%_bindir/valadoc-%api_ver
%_libdir/libvaladoc-%api_ver.so.*
%dir %_libdir/valadoc
%dir %_libdir/valadoc/doclets
%_libdir/valadoc/doclets/devhelp/
%_libdir/valadoc/doclets/gtkdoc/
%_libdir/valadoc/doclets/html/
%_man1dir/valadoc*.1.*
%_datadir/valadoc/

%exclude %_libdir/valadoc/*/*/*.la

%files -n valadoc-devel
%_includedir/valadoc-%api_ver/
%_libdir/libvaladoc-%api_ver.so
%_pkgconfigdir/valadoc-%api_ver.pc
%_vapidir/valadoc-%api_ver.deps
%_vapidir/valadoc-%api_ver.vapi


%changelog
* Wed Jun 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.44.4-alt1
- 0.44.4

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 0.44.3-alt1
- 0.44.3

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 0.44.2-alt1
- 0.44.2

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.44.1-alt1
- 0.44.1

* Sat Mar 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Sun Mar 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.42.6-alt1
- 0.42.6

* Tue Jan 22 2019 Yuri N. Sedunov <aris@altlinux.org> 0.42.5-alt1
- 0.42.5

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.42.4-alt1
- 0.42.4

* Wed Nov 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.42.3-alt1
- 0.42.3

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.42.2-alt1
- 0.42.2

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt1
- 0.42.1

* Sat Sep 01 2018 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Mon Aug 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.9-alt1
- 0.40.9

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.8-alt1
- 0.40.8

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.7-alt1
- 0.40.7

* Wed May 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.6-alt1
- 0.40.6

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.5-alt1
- 0.40.5

* Mon Apr 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.4-alt1
- 0.40.4

* Sun Apr 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.3-alt1
- 0.40.3

* Wed Mar 28 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.2-alt1
- 0.40.2

* Mon Mar 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1
- 0.40.1

* Sun Mar 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 0.38.8-alt1
- 0.38.8

* Sun Feb 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.38.7-alt1
- 0.38.7

* Tue Jan 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.38.6-alt1
- 0.38.6

* Sun Jan 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.38.5-alt1
- 0.38.5

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.4-alt1
- 0.38.4

* Thu Nov 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.3-alt1
- 0.38.3

* Sun Oct 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.2-alt1
- 0.38.2

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.1-alt1
- 0.38.1

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0
- new valadoc subpackage (buildreqs: +libgraphviz-devel, help2man)
- moved %%check after %%install

* Wed Jul 12 2017 Alexey Shabalin <shaba@altlinux.ru> 0.36.4-alt1
- 0.36.4

* Fri May 05 2017 Alexey Shabalin <shaba@altlinux.ru> 0.36.3-alt1
- 0.36.3

* Mon Apr 03 2017 Alexey Shabalin <shaba@altlinux.ru> 0.36.1-alt1
- 0.36.1

* Mon Mar 20 2017 Alexey Shabalin <shaba@altlinux.ru> 0.36.0-alt1
- 0.36.0

* Thu Mar 09 2017 Alexey Shabalin <shaba@altlinux.ru> 0.34.6-alt1
- 0.34.6

* Fri Mar 03 2017 Alexey Shabalin <shaba@altlinux.ru> 0.34.5-alt1
- 0.34.5

* Wed Dec 07 2016 Alexey Shabalin <shaba@altlinux.ru> 0.34.4-alt1
- 0.34.4

* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.34.3-alt1
- 0.34.3

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 0.34.2-alt1
- 0.34.2

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.34.1-alt1
- 0.34.1

* Tue Sep 20 2016 Alexey Shabalin <shaba@altlinux.ru> 0.34.0-alt1
- 0.34.0

* Wed Jun 22 2016 Alexey Shabalin <shaba@altlinux.ru> 0.32.1-alt1
- 0.32.1

* Tue Mar 22 2016 Alexey Shabalin <shaba@altlinux.ru> 0.32.0-alt1
- 0.32.0

* Mon Feb 01 2016 Alexey Shabalin <shaba@altlinux.ru> 0.30.1-alt1
- 0.30.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1.1
- rebuild

* Fri Sep 18 2015 Alexey Shabalin <shaba@altlinux.ru> 0.30.0-alt1
- 0.30.0

* Thu Aug 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.29.3-alt1
- 0.29.3

* Wed Aug 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.28.1-alt1
- 0.28.1

* Wed Mar 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.28.0-alt1
- 0.28.0

* Tue Feb 24 2015 Alexey Shabalin <shaba@altlinux.ru> 0.27.1-alt1
- 0.27.1

* Tue Jan 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.26.2-alt1
- 0.26.2

* Mon Oct 13 2014 Alexey Shabalin <shaba@altlinux.ru> 0.26.1-alt1
- 0.26.1

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 0.26.0-alt1
- 0.26.0

* Wed Aug 27 2014 Alexey Shabalin <shaba@altlinux.ru> 0.25.2-alt1
- 0.25.2

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.24.0-alt1
- 0.24.0

* Thu Feb 20 2014 Alexey Shabalin <shaba@altlinux.ru> 0.23.3-alt1
- 0.23.3

* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.23.2-alt1
- 0.23.2

* Mon Nov 18 2013 Alexey Shabalin <shaba@altlinux.ru> 0.22.1-alt1
- 0.22.1

* Tue Sep 24 2013 Alexey Shabalin <shaba@altlinux.ru> 0.22.0-alt1
- 0.22.0

* Fri Sep 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.21.2-alt1
- 0.21.2

* Thu Aug 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Wed Mar 20 2013 Alexey Shabalin <shaba@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Wed Nov 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.18.1-alt1
- 0.18.1

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt2
- vapi-common as noarch

* Tue Sep 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Mon Sep 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.7-alt1
- 0.17.7

* Thu Sep 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.6-alt1
- 0.17.6

* Thu Jul 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.3-alt1
- 0.17.3

* Thu Jul 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Mon Mar 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Mar 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt2
- add vapi-common package

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Fri Jun 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt2
- rebuild with rpm-build-vala
- own directory %%_datadir/vala/vapi for third-party *.vapi files

* Thu Jun 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1
- replace vala0.12

* Wed Mar 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Tue Jan 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.3-alt1
- 0.10.3
- update buildreq

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Wed Sep 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Wed Sep 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1
- package doc as noarch

* Thu Apr 22 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun Mar 14 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.10-alt1
- new version

* Fri Jan 15 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.7.9-alt1
- pull Alexey Morozov's changes to build process

* Wed Jan 06 2010 Alexey Morozov <morozov@altlinux.org> 0.7.9-alt0.2
- re-work build process, package the compiler built with the
  bootstrapping compiler of the same version

* Wed Jan 06 2010 Alexey Morozov <morozov@altlinux.org> 0.7.9-alt0.1
- new version

* Mon Dec 07 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.8_67_g3c53cbc-alt1
- most current GIT version

* Sun Dec 06 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.8-alt1
- new version

* Mon Oct 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.7-alt1
- new version

* Fri Sep 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.6-alt2
- get bootstrapping/pregenerated back (with new auto generation script)

* Fri Sep 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.6-alt1
- 0.7.6
- new GEAR repo layout
- turn bootstrapping off (temporary)

* Mon Jun 29 2009 Alexander Bokovoy <ab@altlinux.org> 0.7.4-alt2
- 0.7.4
  + Final upstream 0.7.4

* Sat Jun 13 2009 Alexander Bokovoy <ab@altlinux.org> 0.7.4-alt1
- 0.7.4
  + merge upstream git after switching from svn
  + remove lua5.1.vapi as it is merged upstream already as lua.vapi

* Sun Jan 18 2009 Alexander Bokovoy <ab@altlinux.org> 0.5.7-alt1.r2389
- 0.5.7
  + post-release fixes

* Sun Jan 04 2009 Alexander Bokovoy <ab@altlinux.org> 0.5.4-alt3.r2262
- r2262

* Sat Dec 20 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.4-alt2.r2232
- As vala-gen-project is now part of Vala Toys for gEdit, remove it from the package

* Sat Dec 20 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.4-alt1.r2232
- 0.5.3
  + post-release r2232
  + owned/unowned keywords to mark passing ownership for method returns
    and getters. Syntax might evolve a bit in a future

* Tue Dec 02 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.3-alt1.r2113
- 0.5.2
  + post-release r2113

* Sun Nov 16 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.2-alt2.r2023
- Switch off bootstrap

* Sun Nov 16 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.2-alt1.r2023
- Updated to r2023

* Sat Oct 25 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.1-alt1.r1912
- Updated to r1912
    + Move to post-0.4.0
    + Use bootstrap again (0.4.0+ can't be built with 0.3.6 valac)

* Wed Oct 01 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.6
- Updated to r1816

* Sat Sep 27 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.5
- Updated to r1803
  + Merged upstream dependencies patch (#547569 in GNOME Bugzilla)

* Thu Sep 04 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.4
- Bootstrap is finished, switch to self-hosting builds

* Wed Sep 03 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.3
- Fix GTK+ VAPI (courtesy of Val(a)IDE project)

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.2
- Always perform language self-check tests

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.1
- Use correct version and release to signify in-progress version

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt6
- Fix package maintainership

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt5
- Remove unneeded now bootstrap patch

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt4
- Optimize build requires
- Support build with system-wide valac for future releases

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt3
- Clarify directories' layout
- Add essential documentation

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt2
- First build for Sisyphus

