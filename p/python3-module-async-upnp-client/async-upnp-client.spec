Name: python3-module-async-upnp-client
Version: 0.18.0
Release: alt1

Summary: UPnP Client library for Python/asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/async-upnp-client/

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
%doc LICENSE.* README.*
%_bindir/upnp-client
%python3_sitelibdir/async_upnp_client
%python3_sitelibdir/async_upnp_client-%version-*-info

%changelog
* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.0-alt1
- 0.18.0 released

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.0-alt1
- 0.16.0 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.15-alt1
- 0.14.15 released

* Tue Jan 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.12-alt1
- initial
