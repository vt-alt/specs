%def_disable snapshot

Name: webrtc-audio-processing
Version: 0.3
Release: alt2

Summary: WebRTC Audio Processing library
License: BSD
Group: System/Libraries
Url: https://freedesktop.org/software/pulseaudio/%name/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

%if_disabled snapshot
Source: %url/%name-%version.tar.xz
%else
#VCS: https://anongit.freedesktop.org/git/pulseaudio/%name
Source: %name-%version.tar
%endif
Patch: webrtc-fix-typedefs-on-other-arches.patch

BuildRequires: gcc-c++

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc
Summary: WebRTC Audio Processing library
Group: System/Libraries

%description -n libwebrtc
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-devel
Summary: WebRTC Audio Processing library and header files
Group: Development/C
Requires: libwebrtc = %version-%release

%description -n libwebrtc-devel
libwebrtc-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup
%patch -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%files -n libwebrtc
%_libdir/*.so.*
%doc NEWS README.md

%files -n libwebrtc-devel
%_includedir/webrtc_audio_processing/
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed May 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt2
- Restored patch for generic arch support.

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3 from freedesktop.org

* Fri Sep 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt2
- Fixed build on non-x86 architectures.

* Sun May 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release
