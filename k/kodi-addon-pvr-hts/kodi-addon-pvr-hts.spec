Name: kodi-addon-pvr-hts
Version: 19.0
Release: alt4

Summary: PVR TVheadend addon for Kodi
License: GPLv2
Group: Video

ExclusiveArch: armh aarch64 %ix86 x86_64

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libcec-platform-devel libkodiplatform-devel >= 18.0

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
%_libdir/kodi/addons/pvr.hts
%_datadir/kodi/addons/pvr.hts

%changelog
* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- updated up to 8.2.2-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 8.1.0-Matrix

* Fri Oct 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- follow addon API changes

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- updated for kodi 19.0 Matrix

* Tue Aug 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt2
- updated for Leia up to 4.4.18

* Thu Jan 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Thu Nov 29 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- initial
