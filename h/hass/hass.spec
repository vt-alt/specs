Name: hass
Version: 2021.6.6
Release: alt1

Summary: Home automation platform
License: APL
Group: System/Servers
Url: https://www.home-assistant.io/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%package core
Summary: Home automation platform
Group: System/Servers
Requires: python3-module-yaml >= 5.4.1
Requires: python3-module-pip >= 8.0.3
Requires: python3-module-astral >= 2.2
Requires: python3-module-aiohttp >= 3.7.4
Requires: python3-module-voluptuous >= 0.12.1
Requires: python3-module-text-unidecode >= 1.3
Requires: python3-module-websocket-client >= 0.56.0
Requires: python3-module-hass-frontend >= 20210603.0

%package -n python3-module-hass
Summary: Home automation platform
Group: System/Servers
AutoReq: no

%define desc Home Assistant is a home automation platform running on Python 3.\
It is able to track and control all devices at home and offer a platform \
for automating control.

%description
%desc

%description core
%desc
This package contains core modules only.

%description -n python3-module-hass
%desc
This package contains most of Home Assistant modules.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -pm0644 -D hass.service %buildroot%_unitdir/hass.service
install -pm0644 -D hass.sysconfig %buildroot%_sysconfdir/sysconfig/hass
mkdir -p %buildroot%_localstatedir/hass

find %buildroot%python3_sitelibdir/homeassistant/components -type f -name manifest.json |\
	fgrep -vf precious |sed -re 's,^%buildroot(/.+)/manifest.json,%exclude \1,' > core.files
sed -re 's,%exclude ,,' < core.files > rest.files

%pre core
%_sbindir/groupadd -r -f _hass &> /dev/null
%_sbindir/useradd -r -g _hass -d %_localstatedir/hass -s /dev/null \
	-c 'Home Assistant' -n _hass &> /dev/null ||:

%set_python3_req_method strict
# optional
%add_python3_req_skip av
%add_python3_req_skip colorlog colorlog.escape_codes
%add_python3_req_skip custom_components
%add_python3_req_skip hbmqtt.broker
%add_python3_req_skip importlib_metadata
# deprecated
%add_python3_req_skip homeassistant.components.zwave

%files core -f core.files
%_sysconfdir/sysconfig/hass
%_unitdir/hass.service
%_bindir/hass

%python3_sitelibdir/homeassistant
%python3_sitelibdir/homeassistant-%version-*-info

%dir %attr(0770,root,_hass) %_localstatedir/hass

%files -n python3-module-hass -f rest.files

%changelog
* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.6.6-alt1
- 2021.6.6 released

* Wed Apr 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.4.6-alt1
- 2021.4.6 released

* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.4.4-alt1
- 2021.4.4 released

* Fri Apr 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.4.1-alt1
- 2021.4.1 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.3.4-alt1
- 2021.3.4 released

* Thu Feb 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.2.3-alt3
- get rid of deprecated zwave dependency

* Thu Feb 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.2.3-alt2
- interdependencies corrected

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.2.3-alt1
- 2021.2.3 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.1.5-alt1
- 2021.1.5-alt1 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.118.2-alt1
- 0.118.2 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.117.2-alt1
- 0.117.2 released

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.116.4-alt1
- 0.116.4 released

* Wed Sep 30 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.115.6-alt1
- 0.115.6 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.115.2-alt1
- 0.115.2 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.114.2-alt1
- 0.114.2 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.112.5-alt1
- 0.112.5 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.112.1-alt1
- 0.112.1-alt1 released

* Mon May 04 2020 Stanislav Levin <slev@altlinux.org> 0.106.5-alt2
- Dropped runtime dependency on importlib_metadata.

* Wed Mar 04 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.106.5-alt1
- 0.106.5 released

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.105.3-alt1
- 0.105.3 released

* Wed Jan 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.3-alt1
- 0.104.3 released

* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.2-alt1
- 0.104.2 released

* Fri Jan 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.1-alt1
- 0.104.1 released

* Thu Jan 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.104.0-alt1
- 0.104.0 released

* Sat Jan 11 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.103.6-alt1
- 0.103.6 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.102.2-alt1
- initial
