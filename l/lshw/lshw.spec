Name: lshw
Version: B.02.19.2
Release: alt2

Summary: Hardware Lister
License: GPL-2.0
Group: System/Kernel and hardware
Url: http://ezix.org/project/wiki/HardwareLiSter

Source: %name-%version.tar
Source100: lshw-icons.tar.bz2
Source102: lshw-gtk.1

Patch1: lshw-fix-desktop.patch
Patch2: lshw-2.13-gcc43.patch
# fc (rhbz #1332486)
Patch10: lshw-non-root.patch
Patch11: lshw-B.02.19.2-cmake.patch
Patch12: lshw-B.02.18-scandir.patch
Patch13: lshw-fix-mmc.patch
Patch14: lshw-fix-segfault-in-apfs-volume-code.patch

Requires: pciids usbids

BuildRequires(pre): cmake rpm-build-ninja
BuildRequires: gcc-c++ libgtk+2-devel libsqlite3-devel

%description
lshw (Hardware Lister) is a small tool to provide detailed informaton on the
hardware configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems, on some PowerPC
machines (PowerMac G4 is known to work) and AMD64.

Information can be output in plain text, XML or HTML.

%package gui
Summary: Graphical hardware lister
Group: System/Kernel and hardware
Requires: pciids usbids
Requires: lshw = %version-%release

%description gui
lshw (Hardware Lister) is a small tool to provide detailed informaton on the
hardware configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems, on some PowerPC
machines (PowerMac G4 is known to work) and AMD64.

This package provides graphical (GTK+) front-end to lshw.

%prep
%setup -a 100
%patch2 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%cmake -DNOLOGO=ON -DHWDATA=OFF -DPOLICYKIT=ON -DBUILD_SHARED_LIBS=OFF -GNinja
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
patch -p0 -d %buildroot < %PATCH1

ln -s gtk-lshw %buildroot%_sbindir/lshw-gui

install -Dp -m644 lshw.png %buildroot%_pixmapsdir/lshw.png
install -Dp -m644 lshw-16x16.png %buildroot%_miconsdir/lshw.png
install -Dp -m644 lshw-32x32.png %buildroot%_niconsdir/lshw.png
install -Dp -m644 lshw-48x48.png %buildroot%_liconsdir/lshw.png

# Install man page
install -Dpm0644 %SOURCE102 %buildroot%_man1dir/lshw-gtk.1

%find_lang lshw

%files -f lshw.lang
%doc README.md
%_sbindir/lshw
%_man1dir/lshw.1*

%files gui
%_bindir/lshw-gui
%_sbindir/gtk-lshw
%_sbindir/lshw-gui
%dir %_datadir/lshw
%_datadir/lshw/ui/
%_datadir/lshw/artwork/
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_desktopdir/*
%_man1dir/lshw-gtk.1*
%_datadir/appdata/*.appdata.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> B.02.19.2-alt2
- Fix build with rpm-build-ninja.

* Tue May 12 2020 Andrey Cherepanov <cas@altlinux.org> B.02.19.2-alt1
- New version.
- Fix License tag according to SPDX.
- Use polkit for privilege escalation instead of consolehelper.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.18-alt2
- Fix race condition in build.

* Wed Jun 08 2016 Yuri N. Sedunov <aris@altlinux.org> 2.18-alt1
- 2.18 (B.02.18-6-gcb3c299)

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 2.17-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jan 01 2014 Yuri N. Sedunov <aris@altlinux.org> 2.17-alt1
- 2.17

* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 2.16-alt1
- 2.16

* Thu Oct 07 2010 Victor Forsiuk <force@altlinux.org> 2.15-alt1
- 2.15
- Build with experimental SQLite support.
- Run lshw-gui via consolehelper.

* Tue Feb 24 2009 Victor Forsyuk <force@altlinux.org> 2.14-alt1
- 2.14

* Wed Nov 05 2008 Victor Forsyuk <force@altlinux.org> 2.13-alt2
- Fix FTBFS with gcc4.3.

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 2.13-alt1
- 2.13

* Wed Oct 10 2007 Victor Forsyuk <force@altlinux.org> 2.12-alt1
- 2.12

* Thu Aug 09 2007 Victor Forsyuk <force@altlinux.org> 2.11.01-alt1
- 2.11.01
- Binaries moved to /usr/bin.
- manuf.txt and oui.txt aren't used at all, so we have no reason to package them.
- We now depend on pciids and usbids packages for pci.ids and usb.ids
  respectively.

* Wed Mar 21 2007 Victor Forsyuk <force@altlinux.org> 2.10-alt1
- 2.10

* Tue Nov 07 2006 Victor Forsyuk <force@altlinux.org> 2.09-alt1
- 2.09
- Rename GUI frontend: lshw-gtk looks more logical than gtk-lshw.
- Move all artwork to gui package.
- Added freedesktop-style menu.

* Wed May 10 2006 Victor Forsyuk <force@altlinux.ru> 2.08.01-alt1
- 2.08.01

* Mon Nov 21 2005 Victor Forsyuk <force@altlinux.ru> 2.06-alt1
- 2.06

* Wed Jul 20 2005 Victor Forsyuk <force@altlinux.ru> 2.05-alt1
- New version.

* Sat Jun 25 2005 Victor Forsyuk <force@altlinux.ru> 2.04-alt1
- Initial build.
