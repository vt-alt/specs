%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.2
%define api_ver 0.2
%define spa_api_ver 0.1
%define gst_api_ver 1.0

%def_enable gstreamer
%def_enable systemd
%def_enable docs
%def_enable man
%def_disable jack

Name: pipewire
Version: %ver_major.7
Release: alt1

Summary: Media Sharing Server
Group: System/Servers
License: LGPLv2.1
Url: https://pipewire.org/

%if_disabled snapshot
Source: http://freedesktop.org/software/%name/releases/%name-%version.tar.gz
%else
# VCS: https://github.com/PipeWire/pipewire.git
Source: %name-%version.tar
%endif

Requires: %name-libs = %version-%release
Requires: rtkit

%define gst_ver 1.10

BuildRequires(pre): meson
BuildRequires: libgio-devel libudev-devel libdbus-devel
BuildRequires: libalsa-devel libv4l-devel
BuildRequires: libavformat-devel libavcodec-devel libavfilter-devel
%{?_enable_jack:BuildRequires: libjack-devel}
BuildRequires: libsbc-devel
%if_enabled gstreamer
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-plugins-base-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-net-%gst_api_ver)
BuildRequires: pkgconfig(gstreamer-allocators-%gst_api_ver)
%endif
%{?_enable_systemd:BuildRequires: libsystemd-devel}
%{?_enable_docs:BuildRequires: doxygen graphviz fonts-type1-urw}
%{?_enable_man:BuildRequires: xmltoman}

%description
PipeWire is a multimedia server for Linux and other Unix like operating
systems.

%package libs
Summary: Libraries for PipeWire clients
Group: System/Libraries

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PipeWire media server.

%package libs-devel
Summary: Headers and libraries for PipeWire client development
Group: Development/C
Requires: %name-libs = %version-%release

%description libs-devel
Headers and libraries for developing applications that can communicate with
a PipeWire media server.

%package libs-devel-doc
Summary: PipeWire media server documentation
Group: Documentation
# https://bugzilla.altlinux.org/34101
BuildArch: noarch
Conflicts: %name-libs-devel < %version

%description libs-devel-doc
This package contains documentation for the PipeWire media server.

%package utils
Summary: PipeWire media server utilities
Group: System/Servers
Requires: %name-libs = %version-%release

%description utils
This package contains command line utilities for the PipeWire media server.

%prep
%setup
#find ./ -type f -name "*.[c,h]" -print0 | \
#xargs -r0 sed -i "s|<asoundlib.h>|<alsa/asoundlib.h>|" --

%build
%meson \
	%{?_enable_docs:-Ddocs=true} \
	%{?_enable_man:-Dman=true} \
	%{?_enable_gstreamer:-Dgstreamer=enabled}
	%{?_disable_systemd:-Dsystemd=false}
%meson_build

%install
%meson_install

%check
%meson_test

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -n -g %name -d / \
	-s /dev/null -c "PipeWire System Daemon" %name 2>/dev/null ||:

%files
%_bindir/%name
%{?_enable_gstreamer:%_libdir/gstreamer-%gst_api_ver/libgst%name.so}
%dir %_sysconfdir/%name/
%_sysconfdir/%name/%name.conf
%if_enabled systemd
%_prefix/lib/systemd/user/pipewire.service
%_prefix/lib/systemd/user/pipewire.socket
%endif
%if_enabled man
%_man1dir/%name.1*
%_man5dir/%name.conf.5*
%endif
%doc README NEWS

%files libs
%_libdir/lib%name-%api_ver.so.*
%_libdir/%name-%api_ver/
%_libdir/spa/

%files libs-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name/
%_includedir/spa/
%_pkgconfigdir/lib%name-%api_ver.pc
%_pkgconfigdir/libspa-%spa_api_ver.pc

%if_enabled docs
%files libs-devel-doc
%_datadir/doc/%name/html
%endif

%files utils
%_bindir/%name-monitor
%_bindir/%name-cli
%_bindir/spa-monitor
%_bindir/spa-inspect
%if_enabled man
%_man1dir/%name-monitor.1*
%_man1dir/%name-cli.1*
%endif

%changelog
* Fri Sep 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- updated to 0.2.6-1-g37613b67

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1.2
- fixed build without docs

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1.1
- fixed build without mans

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- updated to 0.2.5-2-gf8b156ac

* Fri Nov 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Fri Sep 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- updated to 0.2.3-7-g58efa8c2

* Sat Aug 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt2
- rebuilt with ffmpeg-4.0

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus

