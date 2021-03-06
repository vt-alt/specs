# Created by pyp2rpm-1.0.1
%global pypi_name singledispatch

Name:           python-module-%{pypi_name}
Version:        3.4.0.3
Release:        alt2
Summary:        This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3
Group:          Development/Python

License:        MIT
URL:            http://docs.python.org/3/library/functools.html#functools.singledispatch
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-ordereddict python-module-setuptools

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-six

Requires:       python-module-six
Requires:       python-module-ordereddict
#BuildRequires:  python-module-ordereddict

%description
PEP 443 proposed to expose a mechanism in the functools standard library
module in Python 3.4 that provides a simple form of generic programming 
known as single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove /usr/bin/env python from scripts
sed -i '1d' singledispatch.py
sed -i '1d' singledispatch_helpers.py

%build
%python_build

%install
%python_install

# %check
# %{__python} setup.py test

%files
%doc README.rst
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelibdir}/%{pypi_name}.py*
%{python_sitelibdir}/%{pypi_name}_helpers.py*

%changelog
* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 3.4.0.3-alt2
- Stopped Python3 package build.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.4.0.3-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.4.0.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.3-alt1
- Version 3.4.0.3

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt1.1
- Added module for Python 3

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 3.4.0.2-alt1
- First build for ALT (based on Fedora 3.4.0.2-3.fc21.src)

