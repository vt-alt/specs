
%define _libexecdir %prefix/libexec
%add_findreq_skiplist %_datadir/sddm/scripts/Xsession

%define sddm_user sddm
%define x11confdir %_sysconfdir/X11
%define sddm_confdir %x11confdir/sddm

Name: sddm
Version: 0.18.1
Release: alt3
%K5init no_altplace man

Group: Graphical desktop/KDE
Summary: Lightweight QML-based display manager
Url: https://github.com/sddm/sddm
License: GPLv2+

Requires: xinitrc >= 2.4.43 xauth /usr/share/design/current
Requires: qt5-quickcontrols

Source: %name-%version.tar
Source1: sddm.conf
Source2: tmpfiles-sddm.conf
Source10: sddm.pam
Source11: sddm-autologin.pam
Source12: sddm-greeter.pam
Source20: Xsetup
Source21: Xstop
# upstream
# SuSE
Patch10: create_pid_file.patch
# github issues
# ALT
Patch100: alt-defaults.patch
Patch101: alt-branding-faces.patch
Patch102: alt-wmsession.patch
Patch103: alt-systemctl-path.patch
Patch104: alt-fix-desktop-session-name.patch
Patch105: alt-branding-background.patch
Patch106: alt-systemd-unit.patch
Patch107: alt-def-breeze.patch
Patch108: alt-show-avatars.patch
Patch109: alt-expired-password-handling.patch
Patch110: alt-sddm-etc.locale.conf.patch
Patch111: alt-sddm-ignore-locales.patch
Patch112: alt-sddm-etc.sysconfig.i18n.patch
Patch113: alt-sddm-greeter-swbackend.patch
Patch114: alt-detect-keyboard.patch
#
Patch200: alt-fix-unable-handle-request.patch
Patch201: alt-new-breeze-theme-compat.patch
Patch202: alt-dbus-sessionchange.patch
Patch203: alt-sddm-fix-pw-do-not-match.patch
Patch204: alt-sddm-visual-fixes.patch
Patch205: alt-smartcard-pin-login.patch
Patch206: alt-renew-font-color.patch

# Automatically added by buildreq on Thu Apr 02 2015 (-bi)
# optimized out: cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-test libqt5-xml libstdc++-devel libxcb-devel pkg-config python-base python-module-BeautifulSoup python-module-PyStemmer python-module-Pygments python-module-google python-module-google-apputils python-module-matplotlib python-module-numpy python-module-pyExcelerator python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-zope.interface python-modules python-modules-compiler python-modules-email python-modules-encodings qt5-base-devel qt5-tools
#BuildRequires: cmake gcc-c++ glibc-devel-static libpam-devel libsystemd-devel nss-ldapd python-module-Reportlab python-module-cssselect python-module-docutils python-module-ecdsa python-module-ed25519 python-module-html5lib python-module-nss python-module-polib python-module-protobuf python-module-pycparser python-module-pycrypto python-module-pygobject3 python-module-pygraphviz python-module-xlwt qt5-declarative-devel qt5-tools-devel ruby ruby-stdlibs time xsetroot
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: cmake extra-cmake-modules glibc-devel
BuildRequires: libpam-devel libsystemd-devel libudev-devel
BuildRequires: libxcb-devel libXau-devel libXdmcp-devel
BuildRequires: qt5-declarative-devel qt5-tools-devel
BuildRequires: python3-module-docutils

%description
SDDM is a modern display manager for X11 aiming to be fast, simple and beatiful.
It uses modern technologies like QtQuick, which in turn gives the designer the
ability to create smooth, animated user interfaces.


%prep
%setup -n %name-%version
%patch10 -p1
#
%patch100 -p1 -b .defaults
#%patch101 -p1
%patch102 -p1 -b .wmsession
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1

%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p2
%patch204 -p1
%patch205 -p3
%patch206 -p1

sed -i 's|rst2man2.py|rst2man.py3|' data/man/CMakeLists.txt

%build
%K5build \
    -DDATA_INSTALL_DIR=%_datadir/sddm \
    -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir/sddm \
    -DLIBEXEC_INSTALL_DIR=%_libexecdir/sddm \
    -DSYSTEMD_SYSTEM_UNIT_DIR=%_unitdir \
    -DENABLE_PAM:BOOL=ON \
    -DENABLE_JOURNALD=ON \
    -DMINIMUM_VT=1 \
    -DSESSION_COMMAND="/etc/X11/Xsession" \
    -DBUILD_MAN_PAGES=ON \
    -DSTATE_DIR="%_localstatedir/sddm" \
    -DRUNTIME_DIR="%_runtimedir/sddm" \
    -DPID_FILE="%_runtimedir/sddm.pid" \
    -DCONFIG_FILE="%sddm_confdir/sddm.conf" \
    -DQT_IMPORTS_DIR="%_qt5_qmldir" \
    -DDBUS_CONFIG_FILENAME="sddm_org.freedesktop.DisplayManager.conf" \
    -DUID_MIN=500 \
    -DUID_MAX=32000 \
    #

%install
%K5install

install -Dm 0644 %SOURCE1 %buildroot/%sddm_confdir/sddm.conf
install -Dpm 0644 %SOURCE2 %buildroot/lib/tmpfiles.d/sddm.conf
install -d %buildroot/%_runtimedir/sddm
install -d %buildroot/%_localstatedir/sddm

install -m 0755 %SOURCE20 %buildroot/%sddm_confdir/
install -m 0755 %SOURCE21 %buildroot/%sddm_confdir/
rm -f %buildroot/%_datadir/sddm/scripts/X*

install -p -m 0644 %SOURCE10 %buildroot%_sysconfdir/pam.d/sddm
install -p -m 0644 %SOURCE11 %buildroot%_sysconfdir/pam.d/sddm-autologin
#install -p -m 0644 %SOURCE12 %buildroot%_sysconfdir/pam.d/sddm-greeter

# create default theme
#cp -ar %buildroot/%_datadir/sddm/themes/maui %buildroot/%_datadir/sddm/themes/default
#sed -i 's|^background=.*|background=%_datadir/design/current/backgrounds/xdm.png|' %buildroot/%_datadir/sddm/themes/default/theme.conf
#sed -i 's|^\(Name=.*\)|\1 Default|' %buildroot/%_datadir/sddm/themes/default/metadata.desktop
#sed -i 's|^\(Description=.*\)|\1 Default|' %buildroot/%_datadir/sddm/themes/default/metadata.desktop

%pre
/usr/sbin/useradd -c 'SDDM service' -s /sbin/nologin -d %_localstatedir/sddm -r %sddm_user 2> /dev/null || :

%files
%doc docs/*.md ChangeLog LICENSE* README* CONTRIBUTORS
%dir %sddm_confdir
%config(noreplace) %sddm_confdir/*
%config(noreplace) %_sysconfdir/pam.d/sddm*
%config(noreplace) %_sysconfdir/dbus-1/system.d/sddm_org.freedesktop.DisplayManager.conf
%_libexecdir/sddm/
%_bindir/sddm
%_bindir/sddm-greeter
%_K5qml/*
%_datadir/sddm/
%_man1dir/*.*
%_man5dir/*.*
%attr(0711,root,%sddm_user) %dir %_runtimedir/sddm
%attr(0775,%sddm_user,root) %dir %_localstatedir/sddm
%_unitdir/sddm.service
/lib/tmpfiles.d/sddm.conf

%changelog
* Wed Feb 12 2020 Oleg Solovyov <mcpain@altlinux.org> 0.18.1-alt3
- renewal dialog: make prompts more readable

* Tue Dec 17 2019 Sergey V Turchin <zerg@altlinux.org> 0.18.1-alt2
- build with python3-module-docutils

* Thu Jul 04 2019 Sergey V Turchin <zerg@altlinux.org> 0.18.1-alt1
- new version

* Wed Mar 13 2019 Oleg Solovyov <mcpain@altlinux.org> 0.18.0-alt2
- allow asking PIN-codes from smart-cards

* Tue Feb 05 2019 Sergey V Turchin <zerg@altlinux.org> 0.18.0-alt1
- new version

* Fri Nov 30 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt9
- fix hardware keyboard detection

* Fri Nov 30 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt8
- fix crash with previous changes

* Wed Nov 28 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt7
- fix hardware keyboard detection

* Tue Nov 20 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt6
- enable virtual keyboard if no hardware detected (ALT#35617)

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt5
- add SoftwareRenderer configuration option (thanks sbolshakov@alt)

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt4
- update tmpfiles config
- don't set software QML renderer by default

* Fri Nov 09 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt3
- set software QML renderer by default (thanks sbolshakov@alt)

* Fri Mar 23 2018 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt2%ubt
- prevent race with systemd-logind service

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 0.17.0-alt1%ubt
- new version

* Thu Nov 30 2017 Oleg Solovyov <mcpain@altlinux.org> 0.16.0-alt2%ubt
- fix password renew for domain users

* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 0.16.0-alt1%ubt
- new version

* Mon Aug 21 2017 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt18%ubt
- fix requires (ALT#33786)

* Fri Aug 11 2017 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt17%ubt
- add fix for github issue 786 (ALT#33728)

* Tue Aug 08 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt16%ubt
- support for changing sessions from D-Bus

* Thu Jun 08 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt15%ubt
- compatibility with new breeze theme

* Thu Jun 01 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt14%ubt
- elarun, maldives: renewal dialogs are replacing login dialogs
- /etc/sysconfig/i18n is now primary locale config

* Mon May 22 2017 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt13%ubt
- add fixes for github issues: 701,708,725,735

* Thu Apr 20 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt12%ubt
- /etc/sysconfig/i18n is now used instead /etc/locale.conf if latter is missing
- ru and en locales are supported locales only, others are being ignored

* Mon Apr 17 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt11%ubt
- Added i18n support for PAM submodules (ru only)

* Mon Apr 03 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt10%ubt
- Fixed "Unable to handle Auth request" (ALT#33248)

* Fri Mar 24 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt9%ubt
- revert previous revert (ALT#33248 - not sddm bug)

* Fri Mar 17 2017 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt8%ubt
- revert previous changes (ALT#33248)

* Tue Mar 14 2017 Oleg Solovyov <mcpain@altlinux.org> 0.14.0-alt7
- added support for expired password changing

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt5.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt6
- use user icons from AccountsService first

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt4.M80P.1
- build for M80P

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt5
- fix to show user avatars (ALT#32629)

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt4
- try Breeze theme by default first

* Mon Aug 29 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt2
- fix build requires

* Mon Aug 29 2016 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt1
- new version

* Fri Aug 05 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt9
- decrease MAX_UID to 32000

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt8
- fix systemd service order

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt7
- add upstream fix to set focus on primary screen

* Thu Apr 28 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt6
- better handle plymouth

* Thu Apr 07 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt5
- fix requires

* Tue Mar 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt4
- hardcode HideShells from default config file

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt3
- add upstream fix for config reader (ALT#31737)

* Wed Jan 27 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt2
- fix crash on read config

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt1
- new version

* Mon Sep 07 2015 Sergey V Turchin <zerg@altlinux.org> 0.12.0-alt1
- new version
- using /usr/share/xsessions

* Thu Sep 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt7
- fix wm sessions list

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt6
- fix pam KWallet support

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt5
- fix pam KWallet support

* Fri Aug 07 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt4
- fix path to systemctl
- setup default theme
- hide nologin users
- don't setup initial backgroung color

* Mon Apr 20 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt3
- don't uppercase xdg session name

* Fri Apr 03 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt2
- fix apply patch

* Thu Apr 02 2015 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt1
- inittial build
