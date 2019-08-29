%define _name python-efl
%define efl_ver 1.22.0

Name: python-module-efl
Version: 1.22.0
Release: alt1

Summary: Python bindings for EFL libraries
Group: Development/Python
License: LGPLv2+
Url: http://trac.enlightenment.org/e/wiki/Python

Source: http://download.enlightenment.org/rel/bindings/python/%_name-%version.tar.xz
#Source: %_name-%version.tar

%setup_python_module ecore
%setup_python_module edbus
%setup_python_module edje
%setup_python_module elementary
%setup_python_module emotion
%setup_python_module ethumb
%setup_python_module evas

Obsoletes: python-module-ecore < 1.8.0
Provides: python-module-ecore = %version-%release
Obsoletes: python-module-eldbus < 1.8.0
Provides: python-module-eldbus = %version-%release
Obsoletes: python-module-edje < 1.8.0
Provides: python-module-edje = %version-%release
Obsoletes: python-module-elementary < 1.8.0
Provides: python-module-elementary = %version-%release
Obsoletes: python-module-emotion < 1.8.0
Provides: python-module-emotion = %version-%release
Obsoletes: python-module-ethumb < 1.8.0
Provides: python-module-ethumb = %version-%release
Obsoletes: python-module-evas < 1.8.0
Provides: python-module-evas = %version-%release

BuildPreReq: efl-libs-devel >= %efl_ver libelementary-devel >= %efl_ver
BuildRequires: python-module-Cython python-module-dbus-devel
BuildRequires: rpm-build-python3 python3-devel python3-module-Cython
# for check
BuildRequires: python-modules-unittest

%description
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

This package provides Enlightenment Foundation Libraries bindings for use
with Python programms.

%package -n python3-module-efl
Summary: Python3 bindings for EFL libraries
Group: Development/Python3

%description -n python3-module-efl
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

This package provides Enlightenment Foundation Libraries bindings for use
with Python3 programms.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%python_build
pushd py3build
%python3_build
popd

%install
%python_install
pushd py3build
%python3_install
popd

%files
%python_sitelibdir/efl/
%python_sitelibdir/python_efl-*.egg-info
%doc AUTHORS README* ChangeLog

%exclude %python_sitelibdir/efl/utils/setup.py*

%files -n python3-module-efl
%python3_sitelibdir/efl/
%python3_sitelibdir/python_efl-*.egg-info
%doc AUTHORS README* ChangeLog

%exclude %python3_sitelibdir/efl/utils/setup.py*

%changelog
* Sun Apr 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.21.0-alt1
- 1.21.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.20.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0

* Mon Aug 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Thu Apr 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt2
- exclude utils/setup.py that can be used only by other apps
  in the setup.py script (ALT #32010)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.17.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Feb 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Tue Feb 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt2
- rebuilt against 1.17.0 e-libraries

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Nov 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt2
- rebuilt against newest 1.16.0-beta3 e-libraries (ALT #31444)

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Thu Jul 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sun Jan 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt2
- updated buildreqs

* Mon Dec 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for sisyphus

