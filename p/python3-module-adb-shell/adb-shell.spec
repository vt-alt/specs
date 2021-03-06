Name: python3-module-adb-shell
Version: 0.3.4
Release: alt1

Summary: ADB shell and FileSync functionality implemented in Python 
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/adb-shell/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/adb_shell
%python3_sitelibdir/adb_shell-%version-*-info

%changelog
* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.4-alt1
- 0.3.4 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- 0.2.1 released

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
