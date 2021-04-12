%define oname attr
%define pkgname attrs
%def_with python3

Name: python-module-%pkgname
Version: 19.3.0
Release: alt1

Summary: Python attributes without boilerplate

License: MIT
Group: Development/Python
Url: https://attrs.readthedocs.io

Source: %pkgname-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%setup_python_module %oname

%description
attrs is an MIT-licensed Python package with class decorators that ease the
chores of implementing the most common attribute-related object protocols.

%if_with python3
%package -n python3-module-%pkgname
Summary: Python attributes without boilerplate (Python 3)
Group: Development/Python3

%description -n python3-module-%pkgname
attrs is an MIT-licensed Python package with class decorators that ease the
chores of implementing the most common attribute-related object protocols.
%endif


%prep
%setup -n %pkgname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%pkgname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
