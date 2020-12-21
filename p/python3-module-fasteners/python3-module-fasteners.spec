%define oname fasteners

Name: python3-module-fasteners
Version: 0.15
Release: alt1

Summary: A python package that provides useful locks

Group: Development/Python3
License: ASL 2.0
Url: https://github.com/harlowja/fasteners

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six python3-module-monotonic

# tests
BuildRequires: python3-module-testtools
BuildRequires: python3-module-nose
BuildRequires: python-module-futures

%description
A python package that provides useful locks.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%check
nosetests3

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info/


%changelog
* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- separate build python3 module version 0.15
- cleanup spec

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.13.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- Initial package.

