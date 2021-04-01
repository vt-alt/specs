Name: kodi-addon-pvr-iptvsimple
Version: 19.0
Release: alt4

Summary: IPTVSimple addon for Kodi
License: GPL
Group: Video
Url: https://github.com/kodi-pvr/pvr.iptvsimple/

Source: %name-%version.tar

ExclusiveArch: armh aarch64 %ix86 x86_64

BuildRequires: cmake gcc-c++ kodi-devel
BuildRequires: libkodiplatform-devel libpugixml-devel zlib-devel

%description
%summary

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir/kodi
%make_build

%install
%makeinstall_std

%files
%_libdir/kodi/addons/pvr.iptvsimple
%_datadir/kodi/addons/pvr.iptvsimple

%changelog
* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- updated up to 7.4.2-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 7.0.0-Matrix

* Fri Oct 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- follow addon API changes

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- updated for kodi 19.0 Matrix

* Fri Feb 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.0-alt2
- NMU: added URL

* Mon Feb 06 2017 Anton Farygin <rider@altlinux.ru> 17.0-alt1
- new version

* Mon Nov 28 2016 Anton Farygin <rider@altlinux.ru> 16.0-alt1
- initial build for ALT
