%def_disable snapshot

%define ver_major 0.51
%define libname mesonbuild
# pkexec may be used to "gain elevated privileges" during install
%def_without polkit
%def_disable check

Name: meson
Version: %ver_major.2
Release: alt1.1

Summary: High productivity build system
Group: Development/Python3
License: ASL 2.0
Url: http://mesonbuild.com/

%if_disabled snapshot
Source: https://github.com/mesonbuild/meson/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name.macros
Source2: %name.env

BuildArch: noarch

%define python_ver 3.5
Requires: python3 >= %python_ver
Requires: ninja-build

#grep -n "from __main__" -r *
#mesonbuild/minstall.py:23:from __main__ import __file__ as main_file
%add_python3_req_skip __main__
%{?_with_polkit:Requires: polkit}

BuildRequires(pre): rpm-build-python3
BuildRequires: ninja-build python3-devel >= %python_ver python3-module-setuptools
%{?_with_polkit:BuildRequires: libpolkit-devel}
%if_enabled check
BuildRequires: gcc gcc-c++ gcc-fortran gcc-objc gcc-objc++
BuildRequires: java-devel /proc
BuildRequires: mono-core mono-devel
BuildRequires: boost-devel
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: qt5-base-devel
BuildRequires: vala
BuildRequires: libwxGTK3.0-devel
BuildRequires: flex bison
BuildRequires: gnustep-base-devel
BuildRequires: git
BuildRequires: pkgconfig(protobuf) protobuf-c-compiler
BuildRequires: pkgconfig(gobject-introspection-1.0) python3-module-pygobject3 gtk-doc
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-module-Cython
%endif

%description
Meson is a build system designed to optimize programmer productivity.
It aims to do this by providing simple, out-of-the-box support for modern
software development tools and practices, such as unit tests, coverage
reports, Valgrind, CCache and the like.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -Dpm 0644 %SOURCE1 %buildroot%_rpmmacrosdir/%name
install -Dpm 0755 %SOURCE2 %buildroot%_rpmmacrosdir/%name.env

%check
export LC_ALL=en_US.utf8
MESON_PRINT_TEST_OUTPUT=1 ./run_tests.py

%files
%_bindir/%name
%python3_sitelibdir/%libname/
%python3_sitelibdir/%name-%ver_major.*-*.egg-info/
%{?_without_polkit:%exclude %_datadir/polkit-1/actions/com.mesonbuild.install.policy}
%_man1dir/%name.1.*
%_rpmmacrosdir/%name
%_rpmmacrosdir/%name.env
%doc COPYING README.*


%changelog
* Fri Aug 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.51.2-alt1.1
- meson.macros: fixed %%meson_test to allow run tests via wrapper
  like xvfb-run or dbus-run-session

* Tue Aug 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.51.2-alt1
- 0.51.2

* Wed Jul 10 2019 Yuri N. Sedunov <aris@altlinux.org> 0.51.1-alt1
- 0.51.1
- removed obsolete patches

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.50.1-alt2
- applied again dedup.patch to fix gnome-builder build
- updated e2k support by mcst (https://github.com/mesonbuild/meson/pull/5284)

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.50.1-alt1
- 0.50.1

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.49.2-alt3
- backported fix for https://github.com/mesonbuild/meson/issues/2150

* Thu Feb 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.49.2-alt2
- meson.macros: %%meson_build: use %%_smp_mflags to specify number of
  parallel jobs from NPROCS environment variable or from %%__nprocs
  (see ninja bug https://github.com/ninja-build/ninja/issues/1278)

* Wed Feb 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.49.2-alt1
- 0.49.2

* Thu Jan 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.49.1-alt1
- 0.49.1

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 0.49.0-alt1
- updated to 0.49.0-10-g88e08969

* Fri Nov 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.48.2-alt1
- 0.48.2

* Thu Oct 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.48.1-alt1
- 0.48.1

* Sat Oct 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.47.2-alt2
- optional libpolkit-devel BR, disabled by default

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.47.2-alt1
- 0.47.2

* Wed Jul 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.47.1-alt1
- 0.47.1

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.46.1-alt1
- 0.46.1

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt2
- updated to 0.46.0-33-gd1e8ae1

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- 0.46.0

* Thu Mar 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.45.1-alt1
- 0.45.1

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.45.0-alt1
- 0.45.0

* Wed Feb 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.44.1-alt1
- 0.44.1
- set locale to en_US.utf8 in meson.env

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Mon Oct 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.43.0-alt1
- 0.43.0

* Sat Oct 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt2
- meson.macros: localstatedir=%%_var

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt1
- 0.42.1

* Tue Aug 15 2017 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.41.2-alt1
- 0.41.2
- meson.macros: set locale to en_US.utf8 to avoid warnings

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt1
- 0.41.1

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Tue May 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1
- 0.40.1

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.39.1-alt1
- 0.39.1

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- 0.39.0

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.1-alt1
- 0.38.1

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.37.1-alt1
- 0.37.1

* Wed Nov 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Tue Oct 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.35.1-alt1
- 0.35.1

* Sun Sep 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Mon Aug 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- first build for Sisyphus
  (based on fc 0.31.0-1 package http://pkgs.fedoraproject.org/cgit/rpms/meson.git/)

