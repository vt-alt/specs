%def_disable snapshot
%def_enable gui

Name: calf
Version: 0.90.3
Release: alt1

Summary: Audio plugins pack
Group: Sound
License: LGPLv2+
Url: http://calf-studio-gear.org/

%if_disabled snapshot
Source: http://calf-studio-gear.org/files/%name-%version.tar.gz
%else
# VCS: https://github.com/calf-studio-gear/calf.git
Source: %name-%version.tar
%endif

Patch: calf-0.90.1-alt-link.patch

BuildRequires: gcc-c++ desktop-file-utils
BuildRequires: glib2-devel libexpat-devel libfftw3-devel libfluidsynth-devel
BuildRequires: libjack-devel liblash-devel lv2-devel
%{?_enable_gui:BuildRequires: libcairo-devel libgtk+2-devel}

%description
The Calf project aims at providing a set of high quality open source audio
plugins for musicians. All the included plugins are designed to be used with
multitrack software, as software replacement for instruments and guitar stomp
boxes.

The plugins are available in LV2 and Standalone JACK formats.
This package contains the common files and the Standalone JACK plugin.

%package gui
Summary: JACK wrapper for Calf plugins
Group: Sound
Provides: %{name}jackhost = %version-%release
Requires: %name = %version-%release
Requires: jack-audio-connection-kit

%description gui
The Calf project aims at providing a set of high quality open source audio
plugins for musicians. All the included plugins are designed to be used with
multitrack software, as software replacement for instruments and guitar stomp
boxes.

This package contains JACK wrapper for Calf plugins with gui.


%package plugins
Summary: Calf plugins in LV2 format
Group: Sound
Requires: %name = %version-%release
Requires: lv2

%description plugins
The Calf project aims at providing a set of high quality open source audio
plugins for musicians. All the included plugins are designed to be used with
multitrack software, as software replacement for instruments and guitar stomp
boxes.

This package contains LV2 synthesizers and effects, MIDI I/O and GUI
extensions.


%prep
%setup
%patch

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%define _optlevel 3
%autoreconf
%configure \
	--enable-static=no \
	--with-lv2-dir=%_libdir/lv2 \
	--enable-experimental=yes \
%ifarch x86_64 %ix86
	--enable-sse
%endif

%make_build

%install
%makeinstall_std

%files
%_libdir/%name/
%_datadir/%name/sf2/
%_man7dir/%{name}*
%doc %_docdir/%name
%doc AUTHORS ChangeLog README TODO

%if_enabled gui
%files gui
%_bindir/%{name}*
%_datadir/%name/
%exclude %_datadir/%name/sf2
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/bash-completion/completions/%name
%_man1dir/%{name}*
%endif

%files plugins
%_libdir/lv2/%name.lv2/


%changelog
* Wed Jul 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.90.3-alt1
- 0.90.3

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.90.2-alt1
- 0.90.2

* Sun Feb 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.90.1-alt3
- fixed build with libtool_2.4-2.4.2-alt8 (ALT #36162)

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.90.1-alt2
- rebuilt against libfluidsynth.so.2

* Thu Aug 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.90.1-alt1
- 0.90.1

* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.90.0-alt1.1
- rebuilt for aarch64

* Sat Apr 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.90.0-alt1
- 0.90.0-38-gb6513eb



