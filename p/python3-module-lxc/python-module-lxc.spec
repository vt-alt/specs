%define _unpackaged_files_terminate_build 1

%define oname lxc

Name: python3-module-%oname
Version: 3.0.4
Release: alt2
Summary: This repository provides python3 bindings for the LXC container API.

License: GPL
Group: Development/Python3
Url: https://github.com/lxc/python3-lxc

Source: lxc-%version.tar.gz
BuildRequires:  python3-devel python3-module-setuptools lxc-devel pkgconfig
BuildRequires:  gcc

%description
Linux Resource Containers provide process and resource isolation
without the overhead of full virtualization. The python3-module-lxc 
package contains the Python3 binding for LXC.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.md examples COPYING
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Alexandr Antonov <aas@altlinux.org> 3.0.4-alt2
- fix url for *.spec

* Tue Nov 03 2020 Alexandr Antonov <aas@altlinux.org> 3.0.4-alt1
- initial build for ALT
