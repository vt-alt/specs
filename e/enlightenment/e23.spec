%def_disable snapshot

%define ver_major 0.23
%define beta %nil
%define efl_ver_major 1.22
%define efl_ver %efl_ver_major.3

%def_enable bluetooth
%def_enable wayland
%def_enable xwayland
%def_enable wl_drm
%def_enable wl_x11
%def_enable systemd
%def_enable connman
%def_enable packagekit
%def_enable install_sysactions
%def_with suid_binaries
# for silly lightdm
%def_disable wmsession

Name: enlightenment
Version: %ver_major.0
Release: alt1
Epoch: 1

Summary: The Enlightenment window manager
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: https://download.enlightenment.org/rel/apps/%name/%name-%version%beta.tar.xz
%endif

Source1: E.png
Source2: start_%name
Source3: %name.wmsession
Source8: %name.desktop
%{?_enable_install_sysactions:Source11: %name-alt-sysactions.conf}

# revert it for patch enlightenment-0.19.0-alt-pam-helper.patch
Patch: enlightenment-0.22.2-up-auth.patch
Patch1: e17-0.17.0-alt-g-s-d_path.patch
Patch2: enlightenment-0.22.4-alt-e_sys_nosuid.patch
Patch3: auto-ptrace-disable.patch
Patch4: enlightenment-0.19.0-alt-pam-helper.patch

Provides: e19 = %EVR
# Obsoletes/Provides old eNN
Obsoletes: e17 e18
Provides: e17 = %EVR
Provides: e18 = %EVR
Provides: %name-default
Obsoletes: e17-default e18-default
Provides: e17-default = %EVR
Provides: e18-default = %EVR

# default terminal
Requires: terminology
# default image viewer
Requires: ephoto
# default media player
Requires: rage
# for menu
Requires: gnome-icon-theme
Requires: wm-common-freedesktop
Requires: altlinux-freedesktop-menu-%name >= 0.55
Requires: udisks2
Requires: pulseaudio-daemon
Requires: geoclue2
Requires: connman
# for the evrything module calculator mode
Requires: bc
%{?_enable_xwayland:Requires: xorg-xwayland xorg-drv-libinput}
%{?_enable_bluetooth:Requires: bluez %_sbindir/rfkill}
%{?_enable_connman:Requires: connman}
%{?_enable_packagekit:Requires: packagekit}

BuildRequires(pre): meson rpm-build-xdg
BuildRequires: efl-libs-devel >= %efl_ver libelementary-devel >= %efl_ver
BuildRequires: libpam-devel libalsa-devel libudev-devel libxcbutil-keysyms-devel
BuildRequires: libdbus-devel libp11-kit-devel xorg-xproto-devel libxcbutil-keysyms-devel
BuildRequires: libuuid-devel libpulseaudio-devel
BuildRequires: xkeyboard-config-devel libxkbcommon-devel libdrm-devel libgbm-devel
BuildRequires: doxygen
# for sysv
BuildRequires: pm-utils
%{?_enable_bluetooth:BuildRequires: libbluez-devel %_bindir/l2ping %_sbindir/rfkill}
%{?_enable_wayland:BuildRequires: libwayland-server-devel >= 1.3.0 libpixman-devel libEGL-devel libwayland-egl-devel wayland-protocols}
%{?_enable_xwayland:BuildRequires: xorg-xwayland}
%{?_enable_systemd:BuildRequires: systemd-devel}

%description
Enlightenment is a window manager.

%package devel
Summary: Development headers for Enlightenment.
Group: Development/C
Requires: %name = %EVR
# Obsoletes/Provides old eNN
Obsoletes: e17-devel e18-devel
Provides: e17-devel = %EVR
Provides: e18-devel = %EVR

%description devel
Development headers for Enlightenment.

%prep
%setup -n %name-%version
#%patch -p1 -R -b .auth
%patch1 -p1 -b .gsd
%{?_without_suid_binaries:%patch2 -p1 -b .nosuid}
%patch3 -p2 -b .ptrace

# fix logic
sed -i "s/\(if config_h\.has('HAVE_WAYLAND') == \)false/\1true/" data/session/meson.build

%build
%{?_enable_wayland:%add_optflags $(pkg-config --cflags uuid)}
%meson \
	-Dfiles=true \
	-Dpam=true \
	%{?_enable_wayland:-Dwl=true} \
	%{?_enable_xwayland:-Dxwayland=true -Dxwayland-bin=%_bindir/Xwayland} \
	%{?_disable_wl_drm:-Dwl-drm=false} \
	%{?_disable_wl_x11:-Dwl-x11=false} \
	%{?_disable_install_sysactions:-Dinstall-sysactions=flase} \
	%{?_disable_connman:-Dconnman=false} \
	%{?_disable_packagekit:-Dpackagekit=false} \
	%nil
%meson_build

%install
%meson_install

mkdir -p %buildroot%_rpmmacrosdir
cat > %buildroot%_rpmmacrosdir/%name <<_EOF_
%%enlightenment_version		%version
_EOF_

# Install icon
install -pD -m644 %SOURCE1 %buildroot%_liconsdir/E-18.png

# PAM-config
mkdir -p %buildroot%_sysconfdir/pam.d
cat > %buildroot%_sysconfdir/pam.d/%name << _PAM_
#%%PAM-1.0

auth		include		system-auth
account		required	pam_deny.so
password	required	pam_deny.so
session		required	pam_deny.so
_PAM_

# replace original sysaction.conf
cp %SOURCE11 %buildroot%_sysconfdir/%name/sysactions.conf

# replace original menus by symlink to our enlightenment.menu
ln -sf %name.menu %buildroot/%_xdgmenusdir/e-applications.menu

%if_enabled wmsession
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir/X11/wmsession.d
install -D -pm 644 %SOURCE3 %buildroot%_sysconfdir/X11/wmsession.d/05Enlightenment
# replace original desktop file
install -pD -m 644 %SOURCE8 %buildroot%_desktopdir/%name.desktop
%endif

# fix Name in session desktop files
sed -i 's/^\(Name.*=Enlightenment\)$/\1 on Xorg/' %buildroot%_datadir/xsessions/%name.desktop
sed -i 's/^\(Name.*=Enlightenment\)$/\1 on Wayland/' %buildroot%_datadir/wayland-sessions/%name.desktop
# rename xsession file
mv %buildroot%_datadir/xsessions/%name.desktop %buildroot%_datadir/xsessions/%name-xorg.desktop

# use start_enlighttenment instead of enlightenment_start for lightdm
install -p -m755 %SOURCE2 %buildroot%_bindir/
sed -i 's/\(enlightenment\)_start/start_\1/' %buildroot%_datadir/xsessions/%name-xorg.desktop

%find_lang %name

%files -f %name.lang

%{?_enable_wmsession:%config %_sysconfdir/X11/wmsession.d/*}
%config %_sysconfdir/%name/sysactions.conf
%config(noreplace) %_sysconfdir/pam.d/%name
%dir %_libdir/%name/
%_libdir/%name/modules/
%{?_enable_wayland:%_libdir/%name/gadgets/}
%dir %_libdir/%name/utils
%_libdir/%name/utils/%{name}_alert
%_libdir/%name/utils/%{name}_elm_cfgtool
%_libdir/%name/utils/%{name}_fm
%_libdir/%name/utils/%{name}_fm_op
%_libdir/%name/utils/%{name}_static_grabber
%_libdir/%name/utils/%{name}_thumb
# suid bit apps
%_libdir/%name/utils/%{name}_backlight
%_libdir/%name/utils/%{name}_sys
%_libdir/%name/utils/%{name}_ckpasswd
%_liconsdir/*.png
%_bindir/emixer
%_bindir/%name
%_bindir/%{name}_askpass
%_bindir/%{name}_filemanager
%_bindir/%{name}_imc
%_bindir/%{name}_open
%_bindir/%{name}_remote
%_bindir/%{name}_start
%_bindir/start_%name
%_datadir/%name/
%_datadir/xsessions/%name-xorg.desktop
%{?_enable_wayland:%_datadir/wayland-sessions/%name.desktop}
%_datadir/pixmaps/emixer.png
%_pixmapsdir/%name-askpass.png
%_desktopdir/*.desktop
%{?_enable_systemd:%_prefix/lib/systemd/user/%name.service}
%_xdgmenusdir/e-applications.menu
%doc AUTHORS COPYING README

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_pkgconfigdir/everything.pc
%_rpmmacrosdir/%name

%changelog
* Sat Aug 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.23.0-alt1
- 0.23.0
- enabled wayland support

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.23.0-alt0.1
- 0.23.0-alpha (v0.22.0-394-g4d6a47374) with disabled wayland support

* Wed Jun 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.4-alt2.1
- renamed /usr/share/xsessions/enlightenment.desktop to enlightenment-xorg.desktop

* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.4-alt2
- disabled  %%wmsession, replaced enlighttenment_start by
  start_enlightenment in xsession file (ALT #36913)

* Thu Sep 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.4-alt1
- 0.22.4
- used own pam-helper

* Thu Mar 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.2-alt1
- 0.22.2

* Thu Nov 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.1-alt2
- restored /etc/X11/wmsession.d/05Enlightenment especially for lightdm

* Wed Nov 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.1-alt1
- 0.22.1

* Fri Nov 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.0-alt2
- updated to v0.22.0-20-g2f3d147
- updated dependencies

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.22.0-alt1
- 0.22.0

* Sat Oct 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.10-alt1
- 0.21.10

* Thu Aug 17 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.9-alt1
- 0.21.9

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.8-alt2
- rebuilt against efl-libs-1.20.2

* Sat May 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.8-alt1
- 0.21.8

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.7-alt2
- rebuilt against efl-1.19.0 libraries

* Thu Mar 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.7-alt1
- 0.21.7

* Tue Dec 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.5-alt1
- 0.21.5

* Sun Dec 04 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.4-alt1
- 0.21.4

* Thu Oct 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.3-alt1
- 0.21.3

* Mon Aug 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.2-alt1
- 0.21.2

* Thu Aug 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.21.1-alt1
- 0.21.1

* Fri Jul 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.10-alt1
- 0.20.10

* Wed Jun 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.9-alt1
- 0.20.9

* Tue May 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.8-alt1
- 0.20.8

* Fri Apr 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.7-alt1
- 0.20.7

* Thu Feb 04 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.5-alt1
- 0.20.5

* Tue Feb 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.4-alt1
- 0.20.4

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.3-alt1
- 0.20.3

* Mon Dec 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.2-alt1
- 0.20.2

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.1-alt1
- 0.20.1

* Tue Dec 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.0-alt1
- 0.20.0 release

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.0-alt0.5
- 0.20.0-rc

* Thu Oct 29 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.20.0-alt0.1
- v0.20.0-beta-6-g5469c3b

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.99.0-alt0.6
- 0.19.99.0_6bef668a

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.99.0-alt0.5
- 0.19.99.0_dddbe2a5
- built with efl/elementary-1.15.0 release

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.99.0-alt0.4
- 0.19.99.0_aae280bf
- built with efl/elementary-1.15.0-beta3

* Tue Jul 14 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.99.0-alt0.3
- 0.19.99.0_964fabe6
- built with efl/elementary-1.15.0-beta1
- updated buildreqs

* Wed Jun 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.99.0-alt0.2
- 0.19.99_1734fcaa
- disabled wayland drm module (requires efl from master)

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.99.0-alt0.1
- 0.19.99_96ba030e

* Tue Mar 03 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.4-alt1
- 0.19.4

* Thu Jan 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.3-alt1
- 0.19.3

* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.2-alt1
- 0.19.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.1-alt1
- 0.19.1

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1:0.19.0-alt1
- 0.19.0 preview

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1:0.18.3-alt2
- 0.18.3

* Fri Jan 17 2014 Paul Wolneykien <manowar@altlinux.org> 1:0.18.2-alt2
- Exclude the extra *.la files.
- Fix the connman module detection (patch).

* Sat Dec 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.18.2-alt1
- 0.18.2

* Sun Dec 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.18.0-alt2
- 0.18 release

* Fri Dec 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.18.0-alt1.rc2
- 0.18.0-rc2

* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.18.0-alt1.rc1
- 0.18.0-rc1

* Thu Dec 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.18.0-alt1.alpha4
- post 0.18.0-alpha4 snapshot

* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.5-alt1
- 1.7.5

* Wed Oct 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.4-alt2
- git snapshot (b23cebb26)

* Fri Sep 06 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.4-alt1.1
- sysactions.conf: don't use systemctl for poweroff and reboot

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.4-alt1
- 0.17.4
- sysactions.conf: 's/halt/poweroff/'

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.3-alt1
- 0.17.3

* Wed Apr 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.2.1-alt1
- 0.17.2.1
- starte17: run empower in background (ALT #28823)

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.1-alt4
- starte17: run empower if logind is running
- added %%e17_version rpm macros for modules

* Thu Apr 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.1-alt3
- applied e17-0.17.1-alt-e_sys_nosuid.patch,
  applied custom sysactions.conf, added empower to rqs (ALT #28291)

* Wed Apr 03 2013 Led <led@altlinux.ru> 1:0.17.1-alt2
- with pam helper (ALT#28277)

* Mon Feb 04 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.1-alt1
- Fresh up to v0.17.1.

* Fri Feb 01 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.0-alt6
- Disable tracing automatically if enlightenment has suid/sgid
  bit set.

* Fri Jan 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt5
- required evas_generic_loaders (especially for .svg)
- required gnome-icon-theme for menus (ALT #28311)
- required terminology as a default terminal
- fixed path to gnome-settings-daemon
- prepared pam-config for screenlock
- prepared (not applied) e17-0.17.0-alt-e_sys_nosuid.patch
- prepared (not applied) a draft of custom sysactions.conf

* Fri Jan 18 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.0-alt4
- Make the keylabels bigger, 14 pt (patch).
- Add missing SVN files as the separate tar source.
- Patch the default configuration placing systray gadget on the
  panel/shelf by default.

* Wed Jan 16 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.17.0-alt3
- Do not assume systray must be on a shelf (patch).
- Build with additional debugging flags (-g -ggdb3).

* Sat Dec 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt2
- 0.17.0 final release (zero)
- provides e17-default

* Tue Dec 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.omega
- - 0.17.0 beta (omega)

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.lucky
- 0.17.0 beta (lucky)

* Wed Nov 28 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha6
- 0.17.0 alpha6

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha5
- 0.17.0 alpha5
- requires altlinux-freedesktop-menu-enlightenment >= 0.55

* Fri Nov 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha3
- 0.17.0 alpha3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.17.0-alt1.alpha2
- 0.17.0 alpha2

* Mon Oct 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.77927-alt1
- 0.16.999.77927

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.76015-alt1
- 0.16.999.76015

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.70492-alt1
- 0.16.999.70492

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.65643-alt1
- 0.16.999.65643

* Sun May 01 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.55225-alt2
- set default_system_menu to enlightenment-applications.menu,
  requires wm-common-freedesktop and altlinux-freedesktop-menu-enlightenment (ALT #16132)

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.55225-alt1
- 0.16.999.55225

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.54504-alt1
- 0.16.999.54504

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.52995-alt1
- new snapshot

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.063-alt1
- new version

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.062-alt1
- new version
- removed obsolete %%update_wms calls
- icons moved in proper location

* Thu Nov 13 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.050-alt2
- new e17-gnome package to be gnome-wm as metacity or sawfish. Install this package and do
  "gconftool-2 --set --type string /desktop/gnome/session/required_components/windowmanager enlightenment" to take effect
- install desktop-file instead old menu-file
- remove post{,un}_ldconfig, {update,clean}_menus calls

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.050-alt1
- 0.16.999.050
- added serial due to version downgrade
- don't use bundled vera font, it doesn't support national glyphs

* Wed Sep 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070918
- CVS from 20070918.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070731
- CVS from 20070731.

* Wed May 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070516
- CVS from 20070516.

* Thu May 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070509
- CVS from 20070509.
- Fix BuildRequires.
- Fix --as-needed problems.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 0.17.0.pre10-alt1.20060920
- 20060910 -> 20060920

* Tue Sep 12 2006 Igor Zubkov <icesik@altlinux.org> 0.17.0.pre10-alt1.20060910
- update from cvs (20060327 -> 20060910)
- buildreq

* Mon Apr 10 2006 Igor Zubkov <icesik@altlinux.ru> 0.17.0.pre10-alt1.20060327
- update from cvs

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050530
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050516
- updated from cvs.


* Mon May 16 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17.0.pre10-alt1.1.20050428
-  small fixes in the spec (wmsession.d path corrected).
-  %_menudir filesystem intersections repaired.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050428
- updated from cvs.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050421
- updated from cvs.

* Mon Apr 11 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0_pre10-alt1.cvs20050420
- Initial build from CVS

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 1:0.16.999-alt0.1_003_20050329
- updated from cvs.
- added serial due to version downgrade
- added lib%name and lib%name-devel packages

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_pre10_20050122
- updated from cvs.

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_20030613
- Updated from cvs.
- Moved to /usr/X11 dir
- added check to fam

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_20030530
- Updated from cvs.
- Fix borders
- Fix font link
- Add menu-method support
- Change standart font borzoib.ttf for n019003l.ttf (val-ttf)
- Added requires to efsd, imlib2_loaders

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.17.0-alt0.1_20021123
- First build for Sisyphus.
