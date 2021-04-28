Name: libva-utils
Version: 2.11.1
Release: alt1
Summary: Tools for VAAPI (including vainfo)
License: MIT and BSD
Group: Graphical desktop/Other
Url: https://01.org/linuxmedia
#git https://github.com/01org/libva-utils
Source0: %name-%version.tar

BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libdrm-devel
BuildRequires: libpciaccess-devel
BuildRequires: libva-devel
BuildRequires: libEGL-devel
BuildRequires: libGL-devel
BuildRequires: libGLES-devel
BuildRequires: wayland-devel
BuildRequires: gcc-c++
BuildRequires: pkgconfig(wayland-client) >= 1
BuildRequires: pkgconfig(wayland-scanner) >= 1
BuildRequires: pkgconfig(wayland-server) >= 1

%description
The libva-utils package contains tools that are provided as part
of libva, including the vainfo tool for determining what (if any)
libva support is available on a system.

%prep
%setup
autoreconf -fisv

%build
%configure --disable-static \
	--enable-glx \
	%nil

%make_build

%install
%makeinstall

%files
%doc CONTRIBUTING.md README.md COPYING
%_bindir/vainfo
%_bindir/avcstreamoutdemo
%_bindir/vp8enc
%_bindir/vavpp
%_bindir/vp9enc
%_bindir/loadjpeg
%_bindir/jpegenc
%_bindir/avcenc
%_bindir/h264encode
%_bindir/hevcencode
%_bindir/mpeg2vldemo
%_bindir/mpeg2vaenc
%_bindir/putsurface
%_bindir/putsurface_wayland
%_bindir/sfcsample
%_bindir/vacopy
%_bindir/vppscaling_n_out_usrptr
%_bindir/vppblending
%_bindir/vppchromasitting
%_bindir/vppdenoise
%_bindir/vppscaling_csc
%_bindir/vppsharpness


%changelog
* Tue Apr 13 2021 Anton Farygin <rider@altlinux.org> 2.11.1-alt1
- 2.11.1

* Sun Mar 28 2021 Anton Farygin <rider@altlinux.org> 2.11.0-alt1
- 2.11.0

* Thu Dec 31 2020 Anton Farygin <rider@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Tue Sep 15 2020 Anton Farygin <rider@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Mon Jun 29 2020 Anton Farygin <rider@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Wed Apr 08 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Aug 16 2019 Anton Farygin <rider@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Thu Feb 21 2019 Anton Farygin <rider@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Sat Jul 08 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt1
- new version

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- first build for ALT , based on RH spec

