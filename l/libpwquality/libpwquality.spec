%define _name pwquality

Name: lib%_name
Version: 1.4.1
Release: alt1

Summary: A library for password generation and password quality checking
License: BSD or GPL+
Group: System/Libraries
Url: https://github.com/%name/%name/

Source: %url/releases/download/%name-%version/%name-%version.tar.bz2

Provides: pam_%_name = %version-%release
Requires: cracklib-words pam
BuildRequires: cracklib-devel pam-devel python-devel
BuildRequires: rpm-build-python3 python3-devel

%description
This is a library for password quality checks and generation of random
passwords that pass the checks.
This library uses the cracklib and cracklib dictionaries to perform some
of the checks.

%package devel
Group: Development/C
Summary: Develompent files for %name
Requires: %name = %version-%release

%description devel
Files needed for development of applications using the %name library.
See the pwquality.h header file for the API.

%package -n python-module-%_name
Group: Development/Python
Summary: Python bindings for the %name library
Requires: %name = %version-%release

%description -n python-module-%_name
This is %_name Python module that provides Python bindings for the
%name library. These bindings can be used for easy password
quality checking and generation of random pronounceable passwords from
Python applications.

%package -n python3-module-%_name
Group: Development/Python
Summary: Python3 bindings for the %name library
Requires: %name = %version-%release

%description -n python3-module-%_name
This is %_name Python3 module that provides Python3 bindings for the
%name library. These bindings can be used for easy password
quality checking and generation of random pronounceable passwords from
Python3 applications.


%prep
%setup -a0
mv %name-%version py3build

%build
%define opts --with-securedir=%_pam_modules_dir --disable-static
%configure \
	%opts \
	--with-python-rev=2.7 \
	--with-pythonsitedir=%python_sitelibdir
%make_build

pushd py3build
%configure \
	%opts \
	--with-python-binary=python3 \
	--with-pythonsitedir=%python3_sitelibdir
%make_build
popd

%install
%makeinstall_std

pushd py3build
%makeinstall_std
popd

# relocate %name.so.1 to %_lib
mkdir -p %buildroot/%_lib
mv %buildroot/%_libdir/%name.so.1* %buildroot/%_lib/
ln -sf ../../%_lib/%name.so.1 %buildroot%_libdir/%name.so

%find_lang %name

%check
%make check

%files -f libpwquality.lang
%_bindir/pwmake
%_bindir/pwscore
%_pam_modules_dir/pam_pwquality.so
/%_lib/%name.so.*
%config(noreplace) %_sysconfdir/security/%_name.conf
%_man1dir/*
%_man5dir/*
%_man8dir/*
%doc COPYING README NEWS AUTHORS

%exclude %_pam_modules_dir/*.la

%files devel
%_includedir/%_name.h
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%_man3dir/pwquality.3.*

%files -n python-module-%_name
%python_sitelibdir/%_name.so
%python_sitelibdir/*.egg-info

%files -n python3-module-%_name
%python3_sitelibdir/%{_name}*.so
%python3_sitelibdir/*.egg-info

%changelog
* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri Mar 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue May 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Jul 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Mon Aug 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4
- new python3 subpackage

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Mon Aug 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Jun 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus

