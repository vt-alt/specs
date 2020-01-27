%define pypi_name pecan

Name: python-module-%pypi_name
Version: 1.3.3
Release: alt1
Summary: A lean WSGI object-dispatching web framework
Group: Development/Python

License: BSD
Url: http://github.com/pecan/pecan
Source0: %pypi_name-%version.tar.gz
BuildArch: noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-webob >= 1.2
BuildRequires: python-module-simplegeneric >= 0.8
BuildRequires: python-module-mako >= 0.4.0
BuildRequires: python-module-singledispatch
BuildRequires: python-module-webtest >= 1.3.1
BuildRequires: python-module-logutils >= 0.3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-webob >= 1.2
BuildRequires: python3-module-simplegeneric >= 0.8
BuildRequires: python3-module-mako >= 0.4.0
BuildRequires: python3-module-singledispatch
BuildRequires: python3-module-webtest >= 1.3.1
BuildRequires: python3-module-logutils >= 0.3

Requires: python-module-singledispatch
Requires: python-module-logutils >= 0.3
Requires: python-module-webob >= 1.2
Requires: python-module-mako >= 0.4.0

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%package -n python3-module-%pypi_name
Summary: A lean WSGI object-dispatching web framework
Group: Development/Python3
Requires: python3-module-singledispatch
Requires: python3-module-logutils >= 0.3
Requires: python3-module-webob >= 1.2
Requires: python3-module-mako >= 0.4.0

%description -n python3-module-%pypi_name
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%package tests
Summary: Tests for %pypi_name
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %pypi_name.

%package -n python3-module-%pypi_name-tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: python3-module-%pypi_name = %EVR

%description -n python3-module-%pypi_name-tests
This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

rm -rf ../python3
cp -a . ../python3

%build
pushd ../python3
%python3_build
popd

%python_build

%install
%python_install
for f in $(ls -1 %buildroot%_bindir)
    do mv %buildroot%_bindir/$f %buildroot%_bindir/$f.py2
done

pushd ../python3
%python3_install
popd

# ?
rm -rf %buildroot%python_sitelibdir/%pypi_name/tests/config_fixtures/bad
rm -rf %buildroot%python3_sitelibdir/%pypi_name/tests/config_fixtures/bad

%files
%doc LICENSE README.rst
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing.py
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/+package+/tests

%files tests
%python_sitelibdir/*/testing.py
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/+package+/tests

%files -n python3-module-%pypi_name
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing.py
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/+package+/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/*/testing.py
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/+package+/tests

%changelog
* Wed Jan 22 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.3-alt1
- 1.3.3
- update requires

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.3.2-alt2
- Dropped dependency on python argparse (use stdlib's one).

* Fri Jan 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.2-alt1
- 1.3.2
- add tests packages

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt2.1
- NMU: Use buildreq for BR.

* Mon Nov 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt2
- update R:

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3
- add python3 package
- delete tests

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.5-alt1
- First build for ALT (based on Fedora 0.4.5-4.fc21)

