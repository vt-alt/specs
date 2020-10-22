%define _unpackaged_files_terminate_build 1
%define oname pallets-sphinx-themes

Name: python-module-%oname
Version: 1.1.3
Release: alt2

Summary: Sphinx themes for Pallets and related projects.
License: BSD-3-Clause
Group: Development/Python
Url: https://www.palletsprojects.com/
# https://github.com/pallets/pallets-sphinx-themes
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel


%description
Themes for the Pallets projects. If you're writing an extension, use the
appropriate theme to make your documentation look consistent.

%package -n python3-module-%oname
Summary: Sphinx themes for Pallets and related projects.
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%oname
Themes for the Pallets projects. If you're writing an extension, use the
appropriate theme to make your documentation look consistent.

%prep
%setup

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.rst LICENSE.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- NMU: Fix license.

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus
