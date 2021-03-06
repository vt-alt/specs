%define oname attr
%define pkgname attrs

Name: python-module-%pkgname
Version: 19.3.0
Release: alt2

Summary: Python attributes without boilerplate

License: MIT
Group: Development/Python
Url: https://attrs.readthedocs.io

Source: %pkgname-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%setup_python_module %oname

%description
attrs is an MIT-licensed Python package with class decorators that ease the
chores of implementing the most common attribute-related object protocols.


%prep
%setup -n %pkgname-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%changelog
* Fri Sep 4 2020 Vladimir Didenko <cow@altlinux.org> 19.3.0-alt2
- Build Python 3 version as separate package

* Wed Nov 13 2019 Vladimir Didenko <cow@altlinux.org> 19.3.0-alt1
- New version

* Wed Mar 13 2019 Vladimir Didenko <cow@altlinux.org> 19.1.0-alt1
- New version

* Tue Oct 9 2018 Vladimir Didenko <cow@altlinux.org> 18.2.0-alt1
- New version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 18.1.0-alt1
- New version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.org> 17.4.0-alt1
- New version

* Fri Jun 9 2017 Vladimir Didenko <cow@altlinux.org> 17.2.0-alt1
- New version

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.org> 16.3.0-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.org> 16.2.0-alt1
- Initial build for Sisyphus

* Mon Jul 24 2016 Vladimir Didenko <cow@altlinux.org> 16.0.0-alt1
- Initial build for Sisyphus
