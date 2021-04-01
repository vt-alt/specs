Name: kodi-addon-inputstream-adaptive
Version: 19.0
Release: alt3

Summary: Adaptive stream addon for Kodi
License: GPLv2
Group: Video
Url: https://github.com/peak3d/inputstream.adaptive/

ExclusiveArch: armh aarch64 %ix86 x86_64

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libkodiplatform-devel >= 18.0
BuildRequires: libexpat-devel

%description
%summary

%prep
%setup

%build
cmake . -DCMAKE_CXX_FLAGS='%optflags -Wno-error=return-type' \
	-DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir/kodi
%make_build

%install
%makeinstall_std

%files
%_libdir/kodi/addons/*
%_datadir/kodi/addons/*

%changelog
* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 2.6.7-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- updated up to 2.6.4-Matrix

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- updated for kodi 19.0 Matrix

* Mon Aug 05 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt3
- updated for Leia

* Thu Feb 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 18.0-alt2
- NMU: fixed build with gcc-8.

* Fri Feb 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.5-alt1.1
- NMU: added URL

* Sat Nov 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.5-alt1
- 2.0.19

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- initial
