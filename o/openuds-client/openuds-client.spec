%add_python3_lib_path %_libexecdir/UDSClient
%allow_python3_import_path %_libexecdir/UDSClient

Name: openuds-client
Version: 3.0.0
Release: alt1
Summary: Client for Universal Desktop Services (UDS) Broker
License: BSD3
Group: Networking/Remote access
URL: https://github.com/dkmstr/openuds
Provides: udsclient = %EVR

Source0: %name-%version.tar
#Patch: %name-%version.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-xdg rpm-build-python3

%description
This package provides the required components
to allow connection to services offered by UDS Broker.

%prep
%setup
#%patch -p1

sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' \
    $(find . -name '*.py')

%install
pushd linux
%makeinstall_std
popd

%files
%_libexecdir/UDSClient
%_desktopdir/UDSClient.desktop

%changelog
* Thu Nov 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0 Release

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt0.1.git.d7e30d14
- Initial build for ALT

