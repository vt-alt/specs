Name: kodi-addon-inputstream-ffmpegdirect
Version: 19.0
Release: alt4

Summary: FFmpeg stream addon for Kodi
License: GPL
Group: Video
Url: https://github.com/xbmc/inputstream.ffmpegdirect/

AutoReqProv: yes, nopython

ExclusiveArch: armh aarch64 %ix86 x86_64

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libcec-platform-devel
BuildRequires: libavcodec-devel libavfilter-devel libavformat-devel
BuildRequires: libavutil-devel libswscale-devel libswresample-devel
BuildRequires: libpostproc-devel bzlib-devel zlib-devel

%description
%summary

%prep
%setup

%build
cmake . -DCMAKE_CXX_FLAGS='%optflags' \
	-DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir/kodi
%make_build

%install
%makeinstall_std

%files
%_libdir/kodi/addons/*
%_datadir/kodi/addons/*

%changelog
* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- updated up to 1.19.2-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 1.17.0-Matrix

* Fri Oct 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- follow addon API changes

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- initial
