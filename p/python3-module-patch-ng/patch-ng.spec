%define oname patch-ng

Name: python3-module-%oname
Version: 1.17.4
Release: alt1

Summary: Library to parse and apply unified diffs

License: MIT
Group: Development/Python3
Url: https://github.com/conan-io/python-patch-ng

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%description
Library to parse and apply unified diffs.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/patch_ng*
%python3_sitelibdir/__pycache__/*


%changelog
* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.17.4-alt1
- new version 1.17.4 (with rpmrb script)
- build from tarball

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.17.1-alt1
- Initial build

