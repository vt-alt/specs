%define oname ezcf

Name: python3-module-%oname
Version: 0.2.1
Release: alt1

Summary: Import JSON/YAML like importing .py files
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ezcf/
# https://github.com/laike9m/ezcf.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: disable-failed-tests.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml
BuildRequires: python3-module-coverage 
BuildRequires: python3-module-configobj
BuildRequires: python3-module-xmltodict

%py3_provides %oname
%py3_requires yaml json


%description
ezcf stands for easy configuration, it allows you to import JSON/YAML
like importing .py files, which is very useful for reading conf files
with these formats.

%prep
%setup
%patch0 -p1

%build
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
export LC_ALL=en_US.UTF-8

%python3_install

%check
export LC_ALL=en_US.UTF-8

export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 setup.py test
pushd tests
%__python3 -m unittest discover -v
popd

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt1
- Version updated to 0.2.1.

* Mon Nov 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.1-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1.dev1.git20150324.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.dev1.git20150324.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.dev1.git20150324
- Initial build for Sisyphus

