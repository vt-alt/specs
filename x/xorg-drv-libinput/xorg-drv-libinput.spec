%def_disable snapshot

%define _name xf86-input-libinput
%define _xconfdir %_sysconfdir/X11/xorg.conf.d

Name: xorg-drv-libinput
Version: 0.29.0
Release: alt1

Summary: Xorg libinput input driver
Group: System/X11
License: MIT/X11
Url: http://www.x.org

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: ftp://ftp.x.org/pub/individual/driver/%_name-%version.tar.bz2
%endif
Patch: xf86-input-libinput-0.14.0-alt-include.patch

%define libinput_ver 1.7

Requires(pre): XORG_ABI_XINPUT = %get_xorg_abi_xinput
Requires: libinput >= %libinput_ver
Requires: xkeyboard-config

BuildRequires(pre): xorg-sdk >= 1.14
BuildRequires: libinput-devel >= %libinput_ver xorg-proto-devel

%description
This is an X driver based on libinput. It is a thin wrapper around libinput,
so while it does provide all features that libinput supports it does little
beyond.

***WARNING: misconfiguration of an X input driver may leave you without
usable input devices in your X session. Use with caution.***

%package devel
Summary: Xorg libinput input driver development package
Group: Development/C
Requires: %name = %version-%release

%description devel
Xorg libinput input driver development files.

%prep
%setup -n %_name-%version
%patch

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure --disable-static \
	--with-xorg-module-dir=%_x11modulesdir \
	--with-xorg-conf-dir=%_xconfdir
%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_xconfdir/40-libinput.conf
%_x11modulesdir/input/libinput_drv.so
%_man4dir/libinput.4*
%doc README.* COPYING

%exclude %_x11modulesdir/input/libinput_drv.la

%files devel
%_pkgconfigdir/xorg-libinput.pc
%_includedir/xorg/libinput-properties.h

%changelog
* Tue Aug 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1
- 0.29.0

* Mon Feb 04 2019 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Mon Oct 15 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Wed Jul 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Fri Apr 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.27.1-alt1
- 0.27.1

* Fri Mar 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.27.0-alt1
- updated to 0.27.0-1-g0db8221

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.1-alt1
- updated to 0.25.1-1-g8772a59

* Fri Mar 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Sat Feb 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Mon Dec 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Fri Oct 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0 (0.22.0-1-gbf7fffd)

* Sun Oct 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- 0.19.1

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Sat Apr 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Tue Jan 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Fri Nov 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.15.0-alt2
- rebuild for XORG_ABI_XINPUT = 22.1

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15.0-alt1
- updated to 0.15.0-1-gc8861d2

* Sat Sep 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt2
- updated to 0.14.0_6abd3412
- mv {90,99}-libinput.conf to overlap 95-input-keyboard.conf

* Mon Aug 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Sun Aug 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0_9563334

* Thu Jul 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- first build for Sisyphus

