%set_verify_elf_method unresolved=strict
%def_enable gui
%def_enable docs
%def_disable jsoncpp_bootstrap
%def_without check

Name: cmake
Version: 3.16.3
Release: alt1

Summary: Cross-platform, open-source make system

License: BSD
Group: Development/Tools
Url: http://cmake.org/

Packager: L.A. Kostis <lakostis@altlinux.org>

# Source-git: https://gitlab.kitware.com/cmake/cmake.git
Source: %name-%version.tar
Source1: %name.macros
Source2: CMakeCache.txt
Patch: %name-%version-%release.patch
Patch1: alt-fallback-modules-dir.patch

BuildRequires(pre): rpm-build-xdg
BuildRequires: bzlib-devel gcc-c++ libarchive-devel >= 2.8.4
BuildRequires: libcurl-devel libexpat-devel libncurses-devel libxml2-devel
BuildRequires: liblzma-devel jsoncpp-devel doxygen graphviz zlib-devel
BuildRequires: librhash-devel libuv-devel
BuildRequires: shared-mime-info rpm-build-vim
%{?!_disable_docs:BuildRequires: python-module-sphinx-devel}
%{?!_disable_gui:BuildRequires: qt5-base-devel}

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc gcc-fortran java-devel cvs subversion mercurial git-core}}

Obsoletes: cpack < 2.4.5-alt3
Provides: cpack = %version-%release

Requires: %name-modules = %version-%release
Requires: rpm-macros-%name = %version-%release

%define _unpackaged_files_terminate_build 1

%add_findreq_skiplist %_datadir/%name/Templates/cygwin-package.sh.in


%description
CMake is used to control the software compilation process using
simple platform and compiler independent configuration files.
CMake generates native makefiles and workspaces that can be
used in the compiler environment of your choice. CMake is quite
sophisticated: it is possible to support complex environments
requiring system configuration, pre-processor generation, code
generation, and template instantiation.


%package modules
Summary: Standard CMake modules
Group: Development/Tools
BuildArch: noarch

%description modules
CMake is used to control the software compilation process using
simple platform and compiler independent configuration files.

This package contains the standard modules from the CMake distribution.


%package -n ccmake
Summary: Curses interface for CMake
Group: Development/Tools
Requires: %name = %version-%release

%description -n ccmake
The "ccmake" executable is the CMake curses interface. Project
configuration settings may be specified interactively through this GUI.
Brief instructions are provided at the bottom of the terminal when the
program is running.


%package -n ctest
Summary: CMake test driver program
Group: Development/Tools
Requires: %name = %version-%release

%description -n ctest
The ctest executable is the CMake test driver program. CMake-generated
build trees created for projects that use the ENABLE_TESTING and
ADD_TEST commands have testing support. This program will run the tests
and report results.


%package gui
Summary: Qt interface for CMake
Group: Development/Tools
Requires: %name = %version-%release

%description gui
The "cmake-gui" executable is the CMake GUI.  Project configuration settings
may be specified interactively.  Brief instructions are provided at the
bottom of the window when the program is running.


%package doc
Summary: CMake docs
Group: Documentation
BuildArch: noarch

%description doc
This package contains CMake docs in DocBook, html and txt formats.


%package -n vim-plugin-%name
Summary: Vim plugins for CMake files
Group: Editors
BuildArch: noarch

%description -n vim-plugin-%name
This package contains updated indent and syntax Vim plugins for CMake files.

%package -n bash-completion-%name
Summary: bash completion for CMake
Group: Shells
BuildArch: noarch

%description -n bash-completion-%name
bash completion for CMake


%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging applications that use cmake
Group: Development/Other
Conflicts: cmake = 2.8.0-alt1
Conflicts: rpm-build-compat <= 1.5.1-alt1

%description -n rpm-macros-%name
Set of RPM macros for packaging applications that use cmake.


%prep
%setup
%patch -p1
%patch1 -p1

%build
mkdir build
pushd build
install -m644 %SOURCE2 ./

CFLAGS="%optflags" CXXFLAGS="%optflags" ../bootstrap \
	--verbose \
	--parallel=%__nprocs \
	--system-libs \
%if_enabled gui
	--qt-gui \
%endif
%if_enabled docs
	--sphinx-man \
	--sphinx-html \
%endif
	--prefix=%prefix \
	--datadir=/share/%name \
	--mandir=/share/man \
	--docdir=/share/doc/%name-%version \
%if_enabled jsoncpp_bootstrap
	--no-system-jsoncpp \
%endif
	#

export LD_LIBRARY_PATH=$PWD/Source:$PWD/Source/kwsys/:$PWD/Source/CursesDialog/form%{?_enable_jsoncpp_bootstrap::$PWD/Utilities/cmjsoncpp}
%make_build VERBOSE=1
popd


%install
pushd build
export LD_LIBRARY_PATH=$PWD/Source:$PWD/Source/kwsys/:$PWD/Source/CursesDialog/form%{?_enable_jsoncpp_bootstrap::$PWD/Utilities/cmjsoncpp}
%makeinstall_std
popd
#install -m644 ChangeLog.manual %buildroot%_docdir/%name-%version
mv %buildroot/usr/lib %buildroot%_libdir || :
%if_enabled jsoncpp_bootstrap
cp build/Utilities/cmjsoncpp/libcmjsoncpp.so %buildroot%_libdir/
%endif
%if_with gui
for i in 32 128; do
    install -pD -m644 Source/QtDialog/CMakeSetup$i.png %buildroot%_iconsdir/hicolor/${i}x$i/apps/CMakeSetup.png
done
%endif
mkdir -p %buildroot{%vim_indent_dir,%vim_syntax_dir,%_sysconfdir/bash_completion.d}
install -m644 Auxiliary/vim/indent/%name.vim %buildroot%vim_indent_dir/%name.vim
install -m644 Auxiliary/vim/syntax/%name.vim %buildroot%vim_syntax_dir/%name.vim
rm -rf %buildroot%_datadir/%name/editors/vim
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name

mv -f %buildroot%_datadir/%name/completions %buildroot%_sysconfdir/bash_completion.d/%name

install -p  build/Source/kwsys/libcmsys.so  %buildroot%_libdir/libcmsys.so
install -p  build/Source/kwsys/libcmsys_c.so  %buildroot%_libdir/libcmsys_c.so
install -p  build/Source/libCMakeServerLib.so %buildroot%_libdir/

%check
%if_with check
# CTest.UpdateGIT fails, see #20884
unset GIT_DIR
unset GIT_INDEX_FILE
unset GIT_OBJECT_DIRECTORY
unset DISPLAY
pushd build
export LD_LIBRARY_PATH=%buildroot%_libdir
%make_build test ARGS="--output-on-failure -E 'CMake.FileDownload|CTestTestUpload'"
popd
%endif

%files
%_bindir/cmake
%_bindir/cpack
%_libdir/libCMakeLib.so
%_libdir/libCPackLib.so
%_libdir/libCMakeServerLib.so
%_libdir/libcmsys.so
%_libdir/libcmsys_c.so
%_datadir/%name/
%_aclocaldir/*
%if_enabled docs
%_man1dir/cmake*.*
%_man1dir/cpack.*
%_man7dir/*
%endif
%dir %_docdir/%name-%version/
#_docdir/%name-%version/ChangeLog.manual
%_docdir/%name-%version/Copyright.txt
%_docdir/%name-%version/cmsys/
%exclude %_datadir/%name/Modules/
%if_enabled jsoncpp_bootstrap
%_libdir/libcmjsoncpp.so
%endif

%files modules
%dir %_datadir/%name/
%_datadir/%name/Modules/


%files -n ccmake
%_bindir/ccmake
#_libdir/libcmForm.so
%if_enabled docs
%_man1dir/ccmake.*
%endif


%files -n ctest
%_bindir/ctest
%_libdir/libCTestLib.so
%if_enabled docs
%_man1dir/ctest.*
%endif


%if_enabled gui
%files gui
%_bindir/cmake-gui
%_desktopdir/cmake-gui.desktop
%_xdgmimedir/packages/cmakecache.xml
%_iconsdir/*/*/*/CMakeSetup.png
#_pixmapsdir/*
%endif


%if_enabled docs
%files doc
%dir %_docdir/%name-%version
#_docdir/%name-%version/ccmake.*
#_docdir/%name-%version/cmake*
#_docdir/%name-%version/cpack*
#_docdir/%name-%version/ctest.*
%_docdir/%name-%version/html
%endif


%files -n vim-plugin-%name
%vim_indent_dir/*
%vim_syntax_dir/*

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/*

%files -n rpm-macros-%name
%_rpmmacrosdir/*

%filter_from_requires /^gnustep-Backbone.*/d

%changelog
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.16.3-alt1
- new version 3.16.3 (with rpmrb script)

* Sun Oct 20 2019 Vitaly Lipatov <lav@altlinux.ru> 3.15.4-alt1
- new version 3.15.4 (with rpmrb script)

* Wed May 15 2019 Dmitry V. Levin <ldv@altlinux.org> 3.13.4-alt3
- NMU.
- macros: fixed bug in definitions of %%cmake and %%cmake_insource
  introduced in the previous release.

* Sat May 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.13.4-alt2
- macros: use %%_libsuff macro.
- spec: add knobs useful for bootstrap.

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 3.13.4-alt1
- new version 3.13.4 (with rpmrb script)
- treat "No source or binary directory provided" as warning (ALT bug 36051)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.13.3-alt1
- new version 3.13.3 (with rpmrb script) (ALT bug 36041)

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 3.13.1-alt1
- Updated to upstream version 3.13.1 (ALT bug 35702)

* Thu Jul 19 2018 Grigory Ustinov <grenka@altlinux.org> 3.11.2-alt2
- Fixed FTBS (Add missing rpm-build-xdg).

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.2-alt1
- Updated to upstream version 3.11.2.

* Wed Feb 28 2018 Alexey Shabalin <shaba@altlinux.ru> 3.10.2-alt1
- 3.10.2
- backport support boost-1.66 from cmake-3.11.0-rc2

* Tue Oct 31 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9.2-alt1
- autogen: Don't use AUTOMOC_MOC_OPTIONS in moc-predefs command (ALT bug 34055)

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 3.9.2-alt0.4
- search old sharedir CMake directory too

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 3.9.2-alt0.3
- NMU: set cmake sharedir to %%_datadir/ cmake, not CMake

* Wed Sep 13 2017 Alexey Shabalin <shaba@altlinux.org> 3.9.2-alt0.2
- Set optimization for RELEASE to ALTLinux default.
- FindBoost: Add version 1.65.1 (thx Roger Leigh).
- FindBoost: Add Boost 1.65 dependencies (thx Roger Leigh).
- FindBoost: Add option to prevent finding DEBUG/RELEASE Boost-libs (thx Deniz Bahadir).

* Tue Sep 12 2017 L.A. Kostis <lakostis@altlinux.ru> 3.9.2-alt0.1
- 3.9.2:
  + enable server mode by default.
  + update buildreq (added librhash and libuv).

* Fri Jan 20 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.6.3-alt0.2
- FindBoost.cmake: added support of boost 1.62 and 1.63.

* Tue Dec 13 2016 L.A. Kostis <lakostis@altlinux.ru> 3.6.3-alt0.1
- Updated to 3.6.3.
- .spec cleanup for new rpm.

* Sun Oct 23 2016 L.A. Kostis <lakostis@altlinux.ru> 3.6.2-alt0.2
- Added some patches from debian:
  - FindBoost_add_-lpthread_#563479.diff: Add -lpthread when using Boost::Thread.
  - qt_import_dir_variable.diff: FindQt4: define QT_IMPORTS_DIR variable 
    even if it is not present on the system.

* Sat Oct 22 2016 L.A. Kostis <lakostis@altlinux.ru> 3.6.2-alt0.1
- test build of 3.6.2.

* Mon Jun 13 2016 L.A. Kostis <lakostis@altlinux.ru> 3.4.3-alt0.1
- test build of 3.4.3.

* Wed Sep 02 2015 Sergey V Turchin <zerg@altlinux.org> 3.2.2-alt3.1
- remove variable dereference from FindPkgConfig

* Thu Jun  4 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.2.2-alt3
- rebuild with c++11 ABI

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt2
- Avoid requirement on gnustep-Backbone (ALT #30978)

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt1
- Version 3.2.2 (ALT #30677)

* Tue Nov 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.12.1-alt2
- Revert changes in cmake.macros and add new macros %%_cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=ON

* Thu Nov 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.12.1-alt1
- 2.8.12.1
- Added additional macros in cmake.macros (ALT#27879)
- Change in cmake.macros CMAKE_SKIP_RPATH to CMAKE_SKIP_INSTALL_RPATH
  look the discussion http://public.kitware.com/pipermail/cmake-developers/2012-February/003254.html

* Thu May 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.11-alt1
- 2.8.11

* Tue Mar 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.10.2-alt1
- 2.8.10.2

* Tue Nov 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.10.1-alt1
- 2.8.10.1

* Sat Oct 06 2012 Dmitry V. Levin <ldv@altlinux.org> 2.8.9-alt1.2
- Reverted previous change, it was a no longer needed workaround
  for make-3.82-alt4 quotation bug.

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.9-alt1.1
- Avoid tests with spaces in names of files and directories

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.9-alt1
- 2.8.9
- Add subpackage bash-completion-cmake

* Wed Jun 27 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt3
- Really fix FindPkgConfig.cmake regression (closes: #27499)

* Mon Jun 25 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt2
- Fix FindPkgConfig.cmake regression (closes: #27499)

* Sat Jun 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt1
- 2.8.8
- add %%cmake_build, %%cmake_install and %%cmakeinstall_std macros (closes: #24229)

* Tue Jan 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.7-alt1
- 2.8.7

* Sat Oct 08 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.6-alt1
- 2.8.6

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.5-alt1
- 2.8.5
- Disable test CTestTestUpload

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.4-alt1
- 2.8.4
- Update spec: add necessary LD_LIBRARY_PATH for build process (thanks real@)
- Remove build type and add flags for Fortran (thanks real@)

* Sat Jan 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue Jul 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.8.2-alt1
- 2.8.2
- add/restore VCS tests by adding the necessary buildreqs
- add an additional #20884 workaround needed for new gear --commit

* Tue May 11 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt3
- fix %%cmake_insource (sin@, closes: #23459)

* Mon Mar 29 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8.1-alt2
- Fixed and reenabled %%check.

* Sun Mar 28 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1
- disable tests (CTestTestTimeout fails in hasher)

* Tue Nov 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.0-alt2
- move macros to the separate package according to the policy

* Mon Nov 16 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.0-alt1
- 2.8.0
- add %%cmake and %%cmake_insource macros (closes: #22209)

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt2
- add workarounds for buffer overflows

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Fri Mar 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.3-alt2
- package Vim plugins (closes: #19158)

* Fri Mar 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.3-alt1
- 2.6.3
- fix Group:
- cmake-doc: don't require cmake

* Thu Dec 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt3
- package docdir into the main package (repocop)

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt2
- remove update_*/clean_* invocations

* Sat Sep 27 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Aug 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fix .desktop file according to desktop-file-validate
- move CMakeSetup.png from _pixmapsdir to _niconsdir
- make -doc subpackage noarch and split noarch -modules subpackage

* Sun May 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.0-alt1
- 2.6.0
- package html and txt docs separately

* Sat Feb 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon Jul 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Fri Mar 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.6-alt2
- rebuild with libcurl.so.4

* Sat Jan 13 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt4
- build in separate dir
- use optflags

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt3
- merge cpack package into cmake, since it is required by (almost?)
  all cmake builds (#10577)

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt2
- remove globbing of /usr/lib/qt-3* from FindQt3.cmake, which caused
  incorrect buildreq output for projects using FIND_PACKAGE(Qt3)

* Sat Dec 09 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt1
- 2.4.5
- fix x86_64 build (damir@)

* Sun Dec 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt0.2
- separate packages for ccmake, cpack and ctest

* Sat Dec 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt0.1
- 2.4.5 RC4
- fix search for libxmlrpc

* Thu Nov 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.3-alt2
- build with system libs
- build bundled libs as shared
- invoke make test

* Thu Aug 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.3-alt1
- new version

* Thu Jul 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt0.1
- new version 2.4.2 (with rpmrb script) (fix bug #9776)

* Tue May 09 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt0.1
- new version (2.4.1)

* Wed Jan 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt0.1
- new version
- fix rpath using

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- first release for ALT Linux Sisyphus

* Tue Nov 23 2004 Gaetan LEHMANN <gaetan.lehmann@jouy.inra.fr> 2.0.5-1mdk
- 2.0.5

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.6.7-2mdk
- Rebuild

* Thu Jul 17 2003 Austin Acton <aacton@yorku.ca> 1.6.7-1mdk
- 1.6.7

* Thu Jan 9 2003 Austin Acton <aacton@yorku.ca> 1.4.7-1mdk
- initial package
