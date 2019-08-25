# some online tests
%def_disable check

Name: libgit2
Version: 0.28.3
Release: alt1

Summary: linkable library for Git
License: GPLv2 with linking exception

Group: System/Libraries
Url: https://github.com/%name

Source: %url/%name/archive/v%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake python-modules zlib-devel libssl-devel libssh2-devel

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing you
to write native speed custom Git applications in any language which
supports C bindings.

%package devel
Group: Development/C
Summary: linkable library for Git - development files
Requires: %name = %version-%release

%description devel
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing you
to write native speed custom Git applications in any language which
supports C bindings.
This package contains development files.

%prep
%setup
rm -rf deps/{regex,zlib}
sed -i 's/LIB_INSTALL_DIR lib/LIB_INSTALL_DIR lib${LIB_SUFFIX}/' CMakeLists.txt
sed -i 's/@CMAKE_INSTALL_PREFIX@\///' %name.pc.in

%build
%cmake -DTHREADSAFE:BOOL=ON \
       -DUSE_SHA1DC:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%check
%make -C BUILD test

%files
%_libdir/%name.so.*
%doc README.md AUTHORS COPYING

%files devel
%_includedir/git2
# exclude headers for windows
%exclude %_includedir/git2/inttypes.h
%exclude %_includedir/git2/stdint.h
%_includedir/git2.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Aug 14 2019 Yuri N. Sedunov <aris@altlinux.org> 0.28.3-alt1
- 0.28.3

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Fri Feb 15 2019 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Tue Jan 29 2019 Yuri N. Sedunov <aris@altlinux.org> 0.27.8-alt1
- 0.27.8

* Tue Nov 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.27.7-alt1
- 0.27.7

* Sun Nov 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.8-alt1
- 0.26.8

* Fri Oct 12 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.7-alt1
- 0.26.7 (fixed CVE-2018-17456)

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.5-alt2
- rebuilt with openssl-1.1

* Tue Jul 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.5-alt1
- 0.26.5 (fixed CVE-2018-11235, CVE-2018-10887, CVE-2018-10888)

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.3-alt1
- 0.26.3

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.2-alt1
- 0.26.2

* Thu Mar 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Tue Jul 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.1-alt1
- 0.25.1

* Thu Jan 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.24.6-alt1
- 0.24.6

* Tue Dec 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.5-alt1
- 0.24.5

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.3-alt1
- 0.24.3 (fixed CVE-2016-8568, CVE-2016-8569)

* Thu Oct 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt1
- 0.24.2

* Fri Apr 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Wed Mar 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.4-alt1
- 0.23.4

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.3-alt1
- 0.23.3

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.2-alt1
- 0.23.2

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.2-alt1
- 0.22.2

* Sun Jan 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0
- enabled ssh support via libssh2

* Wed Jan 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.4-alt1
- 0.21.4

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.2-alt1
- 0.21.2

* Tue Jul 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt2
- built as threadsafe

* Mon Jun 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0_16e7596d

* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Jul 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Sun Oct 21 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17.0-alt1.c497a6
- git snapshot c497a6

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17.0-alt1
- initial release
