%define oname lua
%global major_version 5.3
# no tests for 5.3.5
%global test_version 5.3.4

Name: lua%major_version
Version: %major_version.5
Release: alt2

Summary: Powerful light-weight programming language
License: MIT
Group: Development/Other

Url: http://www.lua.org/
# repackaged tarball http://www.lua.org/ftp/lua-%version.tar.gz
Source0: lua-%version.tar
# repackaged tarball http://www.lua.org/tests/lua-%test_version-tests.tar.gz
Source1: lua-%test_version-tests.tar
Source2: lua.source0.watch
Source3: lua.source1.watch
# multilib
Source4: luaconf.h
# copied from readme.html
Source5: COPYRIGHT
Source44: import.info
Patch0: %oname-5.3.0-autotoolize.patch
Patch1: %oname-5.3.0-idsize.patch
#Patch2:         %%{oname}-5.3.0-luac-shared-link-fix.patch
Patch3: %oname-5.2.2-configure-linux.patch
Patch4: %oname-5.3.0-configure-compat-module.patch
Patch5: CVE-2019-6706-use-after-free-lua_upvaluejoin.patch

BuildRequires: automake-common autoconf-common libtool-common readline-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
Provides: lua(abi) = %major_version
Requires: liblua = %version
Provides: lua = %EVR
Provides: lua5 = %EVR
Conflicts: lua5 <= 5.1.5-alt2

%define common_descr \
Lua is a powerful light-weight programming language designed for\
extending applications. Lua is also frequently used as a\
general-purpose, stand-alone language. Lua is free software.\
Lua combines simple procedural syntax with powerful data description\
constructs based on associative arrays and extensible semantics. Lua\
is dynamically typed, interpreted from bytecodes, and has automatic\
memory management with garbage collection, making it ideal for\
configuration, scripting, and rapid prototyping.

%description
%common_descr

%package doc
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description doc
%common_descr

This package contains documantaion for %oname

%package -n lib%name-devel
Summary: Development files for %oname
Group: Development/C
Requires: %name = %version
Provides: lua-devel = %EVR
Provides: lua%major_version-devel = %EVR
Provides: liblua-devel = %EVR
Provides: liblua5-devel = %EVR
Obsoletes: liblua5-devel < %EVR
Conflicts: liblua5-devel < %EVR
Conflicts: liblua4-devel < %version
Conflicts: liblua-devel < %version

%description -n lib%name-devel
%common_descr

This package contains development files for %oname.

%package -n lib%name
Group: Development/Other
Summary: Libraries for %oname
Provides: liblua = %EVR
Provides: liblua5 = %EVR

%description -n lib%name
%common_descr

This package contains the shared libraries for %oname.

%package -n lib%name-devel-static
Summary: Static library for %oname
Group: Development/C
Requires: %name%{?_isa} = %version-%release
Provides: lua-static = %EVR
Provides: lua-devel-static = %EVR
Provides: liblua5-devel-static = %EVR
Obsoletes: liblua5-devel-static < %EVR
Conflicts: liblua5-devel-static < %EVR
Conflicts: liblua4-devel-static < %version

%description -n lib%name-devel-static
%common_descr

This package contains the static version of liblua for %oname.

%prep
%setup -n %oname-%version -a 1
cp -a %SOURCE5 .
mv src/luaconf.h src/luaconf.h.template.in
%patch0 -p1 -E -z .autoxxx
%patch1 -p1 -z .idsize
#%% patch2 -p1 -z .luac-shared
%patch3 -p1 -z .configure-linux
%patch4 -p1 -z .configure-compat-all
%patch5 -p1

%build
%autoreconf
%configure --with-readline --with-compat-module
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Autotools give me a headache sometimes.
sed -i 's|@pkgdatadir@|%_datadir|g' src/luaconf.h.template

# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
%make_build LIBS="-lm -ldl"
# only /usr/bin/lua links with readline now #luac_LDADD="liblua.la -lm -ldl"

%check
cd lua-%test_version-tests

# Removing tests that fail under mock/koji
sed -i.orig -e '
    /db.lua/d;
    /errors.lua/d;
    ' all.lua
LD_LIBRARY_PATH=%buildroot/%_libdir %buildroot/%_bindir/lua -e"_U=true" all.lua

%install
%makeinstall_std
rm %buildroot%_libdir/*.la
mkdir -p %buildroot%_libdir/lua/%major_version
mkdir -p %buildroot%_datadir/lua/%major_version

mv %buildroot%_bindir/lua{,-%major_version}
mv %buildroot%_bindir/luac{,-%major_version}
ln -s lua-%major_version %buildroot%_bindir/lua
ln -s luac-%major_version %buildroot%_bindir/luac
ln -s lua-%major_version %buildroot%_bindir/lua%major_version
ln -s luac-%major_version %buildroot%_bindir/luac%major_version
mv %buildroot%_man1dir/lua{,-%major_version}.1
mv %buildroot%_man1dir/luac{,-%major_version}.1
ln -s lua-%major_version.1 %buildroot%_man1dir/lua.1
ln -s lua-%major_version.1 %buildroot%_man1dir/luac.1
ln -s lua-%major_version.1 %buildroot%_man1dir/lua%major_version.1
ln -s lua-%major_version.1 %buildroot%_man1dir/luac%major_version.1

# Rename luaconf.h to luaconf-<arch>.h to avoid file conflicts on
# multilib systems and install luaconf.h wrapper
mv %buildroot%_includedir/luaconf.h %buildroot%_includedir/luaconf-%_arch.h
install -pm644 %SOURCE4 %buildroot%_includedir/luaconf.h

%ifarch %ix86
if ! [ -e %buildroot/%_includedir/luaconf-i386.h ]; then
  pushd %buildroot/%_includedir/
  ln -s luaconf-%_arch.h  luaconf-i386.h
  popd
fi
%endif

%ifarch %e2k
if ! [ -e %buildroot/%_includedir/luaconf-e2k.h ]; then
  pushd %buildroot/%_includedir/
  ln -s luaconf-%_arch.h  luaconf-e2k.h
  popd
fi
%endif

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo lua-devel >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/lib%name-devel
echo lua-devel-static >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/lib%name-devel-static

%files
%_bindir/lua*
%_bindir/luac*
%_man1dir/lua*.1*

%files doc
%doc doc/*.html doc/*.css doc/*.gif doc/*.png

%files -n lib%name
%doc COPYRIGHT README
%_libdir/liblua-%major_version.so
%dir %_libdir/lua/%major_version
%dir %_datadir/lua/%major_version

%files -n lib%name-devel
%_includedir/l*.h
%_includedir/l*.hpp
%_libdir/liblua.so
%_libdir/pkgconfig/*.pc
%config %_sysconfdir/buildreqs/packages/substitute.d/lib%name-devel

%files -n lib%name-devel-static
%_libdir/*.a
%config %_sysconfdir/buildreqs/packages/substitute.d/lib%name-devel-static

%changelog
* Fri Aug 16 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.5-alt2
- Fixed luaconf wrapper for armh arch (thnx Sergey Bolshakov).

* Thu Aug 08 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.5-alt1
- 5.3.5.
- Applied CVE-2019-6706-use-after-free-lua_upvaluejoin.patch.
- Added conflict with lua5 <= 5.1.5-alt2.

* Tue Oct 30 2018 Michael Shigorin <mike@altlinux.org> 5.3.4-alt3
- fix e2kv4 support (imz@'s suggestion didn't work,
  go kludge it alike to x86 then)

* Tue Sep 12 2017 Michael Shigorin <mike@altlinux.org> 5.3.4-alt2
- e2k support
- spec cleanup

* Thu May 04 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.4-alt1
- 5.3.4

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.3.3-alt6
- added Provides: lua5.3-devel
- added bin,man for lua-5.3 luac-5.3

* Wed Feb 01 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt5
- made symlinks to lua5.3 and luac5.3 binary and manpages.
- removed conflicts and obsoletes to previous version of lua5.
- removed needless provides in liblua5-devel.
- reverted lua modules paths in liblua5.3 package.

* Wed Dec 21 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt4
- added extra provides to devel packages
- fixed provides in liblua5-devel-static
- fixed groups in devel packages
- cleaned up spec file

* Tue Dec 20 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt3
- fixed liblua5-devel provides and conflicts

* Tue Dec 20 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt2
- separated doc package.
- added watch files.
- packaged updated COPYRIGHT instead of mit.txt.
- moved %%{_libdir}/lua5 and %%{_datadir}/lua5 to liblua5.3 package.
- moved lua/%%{major_version} to lua5 in %%{_libdir} and %%{_datadir}.
- renamed -devel and liblua5.3-devel-static packages.
- removed bootstrap.
- packaged repackaged tarballs.

* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt1_3
- converted for ALT Linux by srpmconvert tools

