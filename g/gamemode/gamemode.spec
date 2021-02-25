%define soversion 0

Name: gamemode
Version: 1.6.1
Release: alt1

Summary: Optimise Linux system performance on demand 
License: BSD
Group: Games/Other

Url: https://github.com/FeralInteractive/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

Requires: lib%name%soversion = %EVR

BuildRequires: cmake
BuildRequires: libdbus-devel
BuildRequires: libinih-devel >= r53
BuildRequires: libstdc++-devel
BuildRequires: libsystemd-devel
BuildRequires: meson

%description
GameMode is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process.

GameMode was designed primarily as a stop-gap solution to problems with the Intel and AMD CPU powersave or ondemand governors, but is now host to a range of optimisation features and configurations.

Currently GameMode includes support for optimisations including:
- CPU governor
- I/O priority
- Process niceness
- Kernel scheduler (SCHED_ISO)
- Screensaver inhibiting
- GPU performance mode (NVIDIA and AMD), GPU overclocking (NVIDIA)
- Custom scripts

%package -n lib%name%soversion
Summary: Libraries for GameMode
Group: System/Libraries

%description -n lib%name%soversion
Libraries for GameMode
   
%package -n lib%name-devel
Summary: Development files for GameMode
Group: Development/C

%description -n lib%name-devel
Development files for GameMode

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%__install -Dp -m0644 example/%name.ini %buildroot%_datadir/%name/%name.ini
%__rm -f %buildroot%_libdir/lib%{name}auto.a

%files
%doc LICENSE.txt README.md
%_bindir/%{name}d
%_bindir/%{name}run
%_bindir/%{name}-simulate-game
%dir %_datadir/%name
%_datadir/%name/%name.ini
%_datadir/dbus-1/services/com.feralinteractive.GameMode.service
%_datadir/metainfo/io.github.feralinteractive.%name.metainfo.xml
%_datadir/polkit-1/actions/com.feralinteractive.GameMode.policy
%_libexecdir/cpugovctl
%_libexecdir/gpuclockctl
%_libexecdir/systemd/user/gamemoded.service
%_man1dir/*
%_man8dir/*

%files -n lib%name%soversion
%_libdir/lib%name.so.*
%_libdir/lib%{name}auto.so.*

%files -n lib%name-devel
%_includedir/%{name}_client.h
%_pkgconfigdir/%name.pc
%_pkgconfigdir/lib%{name}auto.pc
%_libdir/lib%name.so
%_libdir/lib%{name}auto.so

%changelog
* Fri Feb 19 2021 Nazarov Denis <nenderus@altlinux.org> 1.6.1-alt1
- Version 1.6.1

* Fri Sep 11 2020 Nazarov Denis <nenderus@altlinux.org> 1.6-alt1
- Version 1.6

* Wed Mar 04 2020 Nazarov Denis <nenderus@altlinux.org> 1.5.1-alt1
- Version 1.5.1
- Use shared inih library

* Tue Feb 18 2020 Nazarov Denis <nenderus@altlinux.org> 1.5-alt1
- Initial build for ALT Linux

