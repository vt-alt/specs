# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# Based on rpm/SPECS/python-schedutils.spec
# Other versions provided by Autoimports

Name: python3-module-schedutils
Group: Development/Python3
Summary: Python interface for the Linux scheduler functions
Version: 0.6
Release: alt2
License: GPL-2.0-only
Url: https://rt.wiki.kernel.org/index.php/Tuna
Vcs: https://git.kernel.org/pub/scm/libs/python/python-schedutils/python-schedutils.git/

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Python interface for the Linux scheduler sched_{get,set}{affinity,scheduler}
functions and friends.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc COPYING README
%_bindir/pchrt
%_bindir/ptaskset
%_man1dir/pchrt.1*
%_man1dir/ptaskset.1*
%python3_sitelibdir/schedutils*

%changelog
* Mon Oct 05 2020 Vitaly Chikunov <vt@altlinux.org> 0.6-alt2
- Increase release to be higher than Autoimports package.

* Sat Oct 03 2020 Vitaly Chikunov <vt@altlinux.org> 0.6-alt1
- First import of 0.6 to Sisyphus.

