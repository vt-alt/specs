%define upstreamname vdpau-video

Name: libva-driver-vdpau
Version: 0.7.4
Release: alt5

Summary: VDPAU-based backend for VA API
License: GPL-2.0+
Group: System/Libraries
Url: http://www.freedesktop.org/wiki/Software/vaapi

Source: %upstreamname-%version.tar
Patch0: libva-vdpau-driver-0.7.4-glext-85.patch
Patch1: libva-vdpau-driver-0.7.4-drop-h264-api.patch
Patch2: libva-vdpau-driver-0.7.4-fix_type.patch
# Reported in https://bugs.freedesktop.org/58836 and http://bugs.debian.org/748294
Patch3: sigfpe-crash.patch
# chromium-vaapi specific patches
Patch4: implement-vaquerysurfaceattributes.patch
# Fix build
Patch5: Change-struct-v4l2-to-uintptr_t.patch

BuildRequires: libvdpau-devel libva-devel libX11-devel libGL-devel

%description
A VDPAU-based backend for VA-API.

%prep
%setup -q -n %upstreamname-%version
%patch0 -p1
#patch1 -p1
#patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules \
	--enable-glx

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/dri/*.la

%files
%doc AUTHORS NEWS
%_libdir/dri/*.so

%changelog
* Thu Apr 09 2020 Andrey Cherepanov <cas@altlinux.org> 0.7.4-alt5
- Return to Siyphus.
- Apply patches from Fedora.
- Fix License tag according to SPDX.

* Fri Oct 13 2017 L.A. Kostis <lakostis@altlinux.ru> 0.7.4-alt4
- Rebuild w/ libva 2.x.
- vdpau_decode: remove deprecated VAProfileH264Baseline profile.

* Thu Dec 08 2016 L.A. Kostis <lakostis@altlinux.ru> 0.7.4-alt3.1
- Merge w/ sbolshakov@.
- Compile fixes w/ recent libva.

* Thu Nov 20 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.4-alt3
- fixed build with recent libvdpau

* Wed Nov 19 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.4-alt2
- rebuilt with libva 1.4

* Fri Jan 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Tue Dec 11 2012 L.A. Kostis <lakostis@altlinux.ru> 0.7.4-alt1
- 0.7.4 release.

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.1
- Fixed build

* Wed Mar 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.3-alt1
- 0.7.3 release

* Sat Feb 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.3-alt0.pre6
- 0.7.3.pre6

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.3-alt0.pre4
- 0.7.3.pre4

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Wed Aug 25 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.10-alt1
- 0.6.10 release.

* Thu Mar 18 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.6-alt1
- 0.6.6 release.

* Thu Jan 28 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.3-alt1
- 0.6.3 release.

* Wed Jan 27 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.2-alt1
- 0.6.2 release.

* Fri Oct 09 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1
- 0.5.0 release.

* Tue Sep 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.1-alt1
- 0.4.1 release.

* Fri Apr 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.3.1-alt1
- 0.3.1 release.

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.3.0-alt1
- Initial build for ALT Linux.

