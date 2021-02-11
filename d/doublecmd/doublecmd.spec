%def_with gtk

Name: doublecmd
Summary: Twin-panel (commander-style) file manager
Version: 0.9.10
Release: alt1
Epoch:   1
Url: https://doublecmd.sourceforge.io

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source1: %name-qt.desktop
License: GPLv2+ and LGPLv2+ and Expat and MPL-1.1 and MPL-2.0 and Apache-2.0 and BSD and Expat and Zlib
Group: File tools

BuildRequires: fpc >= 2.6.2
BuildRequires: fpc-src
%if_with gtk
# lcl_gtk3 is still unstable in Lazarus
BuildRequires: libgtk+2-devel
%endif
BuildRequires: lazarus >= 1.0.10
BuildRequires: qt5pas-devel
BuildRequires: ImageMagick-tools
BuildRequires: libdbus-devel
BuildRequires: bzlib-devel
BuildRequires: /proc

Patch0: doublecmd-use-default-terminal.patch
Patch1: doublecmd-not-install-zdli.patch
Patch2: doublecmd-alt-build-in-one-thread.patch

ExclusiveArch: x86_64 aarch64

%description
Double Commander is a cross platform open source file manager with two panels
side by side. It is inspired by Total Commander and features some new ideas.

%if_with gtk
%package -n %name-gtk
Summary: Twin-panel (commander-style) file manager (GTK)
Group: File tools
Requires: %name-common
Provides: %name
Obsoletes: %name < 0.6.1

%description -n %name-gtk
Double Commander GTK is a cross platform open source file manager with
two panels side by side.  It is inspired by Total Commander and features
some new ideas.
%endif

%package -n %name-qt
Summary: Twin-panel (commander-style) file manager (Qt5)
Group: File tools
Requires: %name-common

%description -n %name-qt
Double Commander Qt5 is a cross platform open source file manager with
two panels side by side.  It is inspired by Total Commander and features
some new ideas.

%package -n %name-common
Summary: Common files for Double Commander
Group: File tools

%description -n %name-common
Common files for Double Commander

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
export MAKEOPTS="-XX"
lcl=qt5 ./build.sh beta
cp ./%name ./%name-qt
%if_with gtk
./clean.sh
lcl=gtk2 ./build.sh beta
%endif

%ifarch %ix86
# To fix ... "oblom" ... when processing install ;)
%set_verify_elf_method textrel=relaxed
%endif

%install
%ifarch aarch64
export CPU_TARGET=x86_64
%endif
install/linux/install.sh --install-prefix=%buildroot
install -d %buildroot%_bindir
install -Dpm0755 ./%name-qt %buildroot%_libdir/%name/%name-qt
ln -s ../%_lib/%name/%name-qt %buildroot%_bindir/%name-qt
# Adapt polkit rule for doublecmd-qt
cp %buildroot%_datadir/polkit-1/actions/org.doublecmd{,-qt}.root.policy
subst 's|%_bindir/%name|%_bindir/%name-qt|' %buildroot%_datadir/polkit-1/actions/org.doublecmd-qt.root.policy
%if_without gtk
rm -f %buildroot%_libdir/%name/%name \
      %buildroot%_bindir/%name \
      %buildroot%_desktopdir/%name.desktop \
      %buildroot%_datadir/polkit-1/actions/org.doublecmd.root.policy
%endif
install -Dpm0644 %SOURCE1 %buildroot%_desktopdir/%name-qt.desktop

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 pixmaps/mainicon/alt/256px-dcfinal.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 pixmaps/mainicon/alt/256px-dcfinal.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 pixmaps/mainicon/alt/256px-dcfinal.png %buildroot%_miconsdir/%name.png

%if_with gtk
%files -n %name-gtk
%_bindir/%name
%_libdir/%name/%name
%_desktopdir/%name.desktop
%_datadir/polkit-1/actions/org.doublecmd.root.policy
%endif

%files -n %name-qt
%_bindir/%name-qt
%_libdir/%name/%name-qt
%_desktopdir/%name-qt.desktop
%_datadir/polkit-1/actions/org.doublecmd-qt.root.policy

%files -n %name-common
%doc doc/README.txt
%exclude %_libdir/%name/%name-qt
%exclude %_bindir/%name-qt
%if_with gtk
%exclude %_libdir/%name/%name
%exclude %_bindir/%name
%endif
%_libdir/%name
%_datadir/%name
%_man1dir/%name.*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_pixmapsdir/%name.png

%changelog
* Mon Feb 08 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.9.10-alt1
- New version.

* Fri Oct 16 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.9.9-alt2
- Build on aarch64, do not build on i586.

* Mon Oct 05 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.9.9-alt1
- Downgrade to last stable version.
- Build with gtk backend (ALT #38835).
- Write out all used licenses in License tag.

* Sun Jul 05 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt0.1.rev9483
- New version (rev 9483).
- Build in one thread.

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt0.1.rev9424
- New version (rev 9424).

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1.rev9357.1
- New version from trunk (rev 9357).
- Build without gtk backend.
- Package README.txt.
- Fix license tag according to SPDX.

* Wed Mar 11 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version.

* Wed Sep 25 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version.

* Wed Mar 14 2018 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt2
- fix build with new Lazarus

* Mon Mar 05 2018 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Mon Feb 27 2017 Motsyo Gennadi <drool@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Mon Dec 26 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Fri Dec 02 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Mon May 30 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Thu Mar 31 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Thu Mar 17 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sat Oct 17 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sun Aug 16 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Jul 14 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Mon Jun 15 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Tue May 12 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Fri May 08 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.1-alt2
- fix BuildRequires

* Fri May 01 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.1-alt1
- 0.6.1
- build Qt4 version

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version

* Mon Dec 30 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.8-alt0.rev.5390
- build for Sisyphus (thank for src.rpm to Anatoly Chernov)

* Sat Sep 28 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.7-alt0.rev.5310
- build for Sisyphus (thank for src.rpm to Anatoly Chernov)

* Tue Mar 26 2013 Andrey Cherepanov <cas@altlinux.org> 0.5.4-alt2
- Fix build by commented out unused assignment

* Wed Feb 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.4-alt1
- build for Sisyphus

* Mon Oct 22 2012 - Anatoly Chernov <aichernov@umail.ru>
- New beta release 0.5.4-3.3 (beta 16.10.2012) with no problem ... :)

* Sun Jun 24 2012 - Anatoly Chernov <aichernov@umail.ru>
- Initial package, version 0.5.4 beta (with new Lazarus) and fix the problem:
- at first:... (hi!)
- /usr/bin/ld: warning: creating a DT_TEXTREL in a shared object.
- ... (skip about 3000 lines) ...
- and later on: ...
- verify-elf: ERROR: ... : TEXTREL entry found: 0x00000000
- RPM build errors: ... ;)
- ...
- assembler ... "blin"
- see http://lists.altlinux.org/pipermail/devel/2012-June/194625.html

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6
