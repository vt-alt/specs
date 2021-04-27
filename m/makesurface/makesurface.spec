%def_disable check

Name: makesurface
Version: 0.2.14
Release: alt2
Summary: Create vector datasets from raster surfaces
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/makesurface/

# https://github.com/mapbox/make-surface.git
Source0: https://pypi.python.org/packages/7d/a8/d6b3561d36bc45eaa6aba7b05624b9fa351430be7ac4b05cbb5d1c0958af/%{name}-%{version}dev.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-click python3-module-fiona
BuildRequires: python3-module-numpy python3-module-rasterio
BuildRequires: python3-module-shapely python3-module-scipy
BuildRequires: python3-module-mercantile python3-module-pyproj

%py3_provides %name
%py3_requires click fiona numpy rasterio shapely scipy mercantile pyproj

%description
Raster -> vector surface creation tools in python.

%prep
%setup -q -n %{name}-%{version}dev

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Thu Oct 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.14-alt2
- Transfer on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.14-alt1
- automated PyPI update

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.git20150218
- Initial build for Sisyphus
