%define _libexecdir %_prefix/libexec
%define _localstatedir %_var
%def_enable introspection
%def_enable systemd
%def_enable qt
%def_enable qt5

Name: lightdm
Version: 1.30.0
Release: alt10
Summary: Lightweight Display Manager
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/lightdm

Source: %name-%version.tar

Patch1:  %name-1.30.0-cancelling.patch
Patch2:  %name-1.30.0-chauthtok.patch
Patch3:  %name-1.30.0-default-session.patch
Patch4:  %name-1.30.0-default-username.patch
Patch5:  %name-1.30.0-login-unknown.patch
Patch6:  %name-1.30.0-switch.patch
Patch7:  %name-1.30.0-alt-env.patch
Patch8:  %name-1.30.0-alt-config.patch
Patch9:  %name-1.30.0-alt-01-Xgreeter.patch
Patch10: %name-1.30.0-alt-02-hide-users.patch
Patch11: %name-1.30.0-alt-03-login-unknown.patch
Patch12: %name-1.30.0-alt-pam.patch
Patch13: %name-1.30.0-alt-polkit.patch
Patch14: %name-1.30.0-alt-shells.patch
Patch15: %name-1.30.0-alt-04-systemd.patch
Patch16: %name-1.30.0-alt-05-tmpfiles.patch
Patch17: %name-1.30.0-alt-i18n.patch

Requires: dm-tool

BuildRequires: gcc-c++ intltool
BuildRequires: pkgconfig(glib-2.0) >= 2.30 pkgconfig(gio-2.0) >= 2.26  pkgconfig(gio-unix-2.0)  pkgconfig(xdmcp)  pkgconfig(xcb)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: libdbus-glib-devel
BuildRequires: gtk-doc yelp-tools itstool
BuildRequires: libpam-devel
BuildRequires: libgcrypt-devel
BuildRequires: libvala-devel vala-tools
BuildRequires: libaudit-devel
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0) >= 2.26 pkgconfig(gio-unix-2.0) pkgconfig(gobject-2.0) pkgconfig(libxklavier) pkgconfig(x11)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_qt:BuildRequires: pkgconfig(QtCore) pkgconfig(QtDBus) pkgconfig(QtGui) /usr/bin/moc-qt4}
%{?_enable_qt5:BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5DBus) pkgconfig(Qt5Gui) /usr/bin/moc-qt5}

%description
LightDM is a lightweight, cross-desktop display manager. Its main features are
a well-defined greeter API allowing multiple GUIs, support for all display
manager use cases, with plugins where appropriate, low code complexity, and
fast performance. Due to its cross-platform nature greeters can be written in
several toolkits, including HTML/CSS/Javascript.

%package -n liblightdm-gobject
Group: System/Libraries
Summary: LightDM GObject Greeter Library
License: LGPLv2+

%description -n liblightdm-gobject
A library for LightDM greeters based on GObject which interfaces with LightDM
and provides common greeter functionality.

%package -n liblightdm-qt
Group: System/Libraries
Summary: LightDM Qt Greeter Library
License: LGPLv2+

%description -n liblightdm-qt
A library for LightDM greeters based on Qt which interfaces with LightDM and
provides common greeter functionality.

%package -n liblightdm-qt5
Group: System/Libraries
Summary: LightDM Qt5 Greeter Library
License: LGPLv2+

%description -n liblightdm-qt5
A library for LightDM greeters based on Qt5 which interfaces with LightDM and
provides common greeter functionality.

%package devel
Group: Development/C
Summary: Development Files for LightDM
Requires: %name

%description devel
This package provides all necessary files for developing plugins, greeters, and
additional interface libraries for LightDM.

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
Contains developer documentation for %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir

%description gir-devel
GObject introspection devel data for the %name

%package -n dm-tool
Summary: Display Manager control utility
Group: Graphical desktop/Other
License: GPLv3+

%description -n dm-tool
dm-tool utility controls a FreeDesktop.org-compatible display
manager via D-Bus.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%ifarch %e2k
# until apx. lcc-1.23.01
sed -i 's,-Werror=pointer-arith,,' configure.ac
%endif

%build
%ifarch %e2k
export CXXFLAGS="%optflags -std=gnu++11"
%endif
%autoreconf
%configure \
	%{subst_enable introspection} \
	--disable-static \
	--disable-tests \
	--enable-gtk-doc \
	%{?_enable_qt:--enable-liblightdm-qt} \
	%{?_enable_qt5:--enable-liblightdm-qt5} \
	--libexecdir=%_libexecdir \
	--with-greeter-user=_ldm \
	--with-greeter-session=%name-default-greeter

%make_build

%install
%make DESTDIR=%buildroot install

# We don't ship AppAmor
rm -rf %buildroot%_sysconfdir/apparmor.d/
# omit upstart support
rm -rf %buildroot%_sysconfdir/init

mkdir -p %buildroot%_sysconfdir/%name/lightdm.conf.d
mkdir -p %buildroot%_datadir/%name/lightdm.conf.d
mkdir -p %buildroot%_datadir/%name/sessions
mkdir -p %buildroot%_datadir/%name/remote-sessions
mkdir -p %buildroot%_localstatedir/log/%name
mkdir -p %buildroot%_localstatedir/cache/%name
mkdir -p %buildroot%_localstatedir/lib/lightdm-data

%if_disabled systemd
sed -i '/pam_systemd.so/d' %buildroot%_sysconfdir/pam.d/%name-greeter
%endif

%find_lang --with-gnome %name

%pre
%_sbindir/groupadd -r -f _ldm >/dev/null 2>&1 || :
%_sbindir/useradd -M -r -d %_localstatedir/lib/ldm -s /bin/false -c "LightDM daemon" -g _ldm _ldm >/dev/null 2>&1 || :

%post
if [ $1 -eq 1 ] ; then
        SYSTEMCTL=/sbin/systemctl
        # Initial installation
        $SYSTEMCTL preset %name.service > /dev/null 2>&1 ||:
fi

%preun
if [ $1 -eq 0 ] ; then
        SYSTEMCTL=/sbin/systemctl
        # Package removal, not upgrade
        $SYSTEMCTL --no-reload disable %name.service > /dev/null 2>&1 ||:
        $SYSTEMCTL stop %name.service > /dev/null 2>&1 ||:
fi


%files -f %name.lang
%doc NEWS
%config %_sysconfdir/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/lightdm.conf.d
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/pam.d/*
%_sbindir/%name
%_unitdir/%name.service
%exclude %_man1dir/dm-tool.*
%dir %_datadir/%name/sessions
%dir %_datadir/%name/remote-sessions
%dir %_datadir/%name/lightdm.conf.d
%_man1dir/*
%_libexecdir/*
%attr(775,root,_ldm) %dir %_localstatedir/log/%name
%attr(775,_ldm,_ldm) %dir %_localstatedir/cache/%name
%attr(750,_ldm,_ldm) %dir %_localstatedir/lib/ldm
%attr(640,_ldm,_ldm) %_localstatedir/lib/ldm/.pam_environment
%attr(750,_ldm,_ldm) %dir %_localstatedir/lib/lightdm-data
/lib/tmpfiles.d/%name.conf
%_datadir/polkit-1/rules.d/%name.rules
%_datadir/polkit-1/actions/org.freedesktop.DisplayManager.AccountsService.policy
%_datadir/accountsservice/interfaces/org.freedesktop.DisplayManager.AccountsService.xml
%_datadir/dbus-1/interfaces/org.freedesktop.DisplayManager.AccountsService.xml
%exclude %_datadir/bash-completion/completions/dm-tool
%_datadir/bash-completion/completions/*
%_controldir/*
%_sysconfdir/X11/*.lightdm

%files -n liblightdm-gobject
%_libdir/liblightdm-gobject-?.so.*

%if_enabled introspection
%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir
%endif

%if_enabled qt
%files -n liblightdm-qt
%_libdir/liblightdm-qt-?.so.*
%endif

%if_enabled qt5
%files -n liblightdm-qt5
%_libdir/liblightdm-qt5-?.so.*
%endif

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*

%files devel-doc
%_datadir/gtk-doc/html/*

%files -n dm-tool
%_bindir/dm-tool
%_datadir/bash-completion/completions/dm-tool
%_man1dir/dm-tool.*

%changelog
* Wed Jul 01 2020 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt10
- Added patch to read the locale configuration from /etc/sysconfig/i18n
  (closes: 38640).

* Thu Jun 04 2020 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt9
- Remove the explicit relationship to the accountsservice package
  (closes: 38573).

* Wed Apr 15 2020 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt8
- Fix: Restore the default (false) value of user-authority-in-system-dir
  (related to altbug 38336).

* Fri Mar 13 2020 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt7
- Added patches to install the ALT-specific files.
- Split the patches.

* Mon Aug 12 2019 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt6
- Use the first available session config as default.

* Tue Aug 06 2019 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt5
- Don't configure "default" user session explicitly.

* Fri Aug 02 2019 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt4
- Fix: Don't try to own extra files in /etc/X11.
- Fix: get rid of the extra xinitrc dependency.

* Wed Jul 31 2019 Paul Wolneykien <manowar@altlinux.org> 1.30.0-alt3
- Use a greeter startup wrapper script with keyboard setup (closes:
  #36933).

* Thu May 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.30.0-alt2
- remove wayland session support form lightdm.conf

* Fri May 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.30.0-alt1
- 1.30.0

* Wed May 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.28.0-alt1
- 1.28.0

* Tue Jan 15 2019 Ivan A. Melnikov <iv@altlinux.org> 1.16.7-alt24
- Replace 'Conflicts <>' with auxiliary package

* Mon Jan 14 2019 Ivan A. Melnikov <iv@altlinux.org> 1.16.7-alt23
- Remove MEMLOCK limit in systemd unit file (closes: #35844).

* Sat Aug 04 2018 Fr. Br. George <george@altlinux.ru> 1.16.7-alt22
- Fix lightdm-greeter-hide-users typo

* Thu Jul 26 2018 Michael Shigorin <mike@altlinux.org> 1.16.7-alt21
- Drop E2K suffix, this package has no e2k-specific patches.
- Uncommented R: accountsservice (closes: #32670)

* Fri May 11 2018 Mikhail Efremov <sem@altlinux.org> 1.16.7-alt20.E2K.1
- Fix build on e2k.
- Use %%e2k macro.

* Tue Mar 27 2018 Arseny Maslennikov <arseny@altlinux.org> 1.16.7-alt20
- Re-apply -alt18 changes accidentally lost in -alt19.

* Tue Mar 27 2018 Arseny Maslennikov <arseny@altlinux.org> 1.16.7-alt19
- x-server-xvnc.c: close connection socket on Xvnc shutdown.

* Fri Mar 23 2018 Ivan Zakharyaschev <imz@altlinux.org> 1.16.7-alt18
- in "Remove X authority": Ignore any error & don't exit, continue
  closing the session (PAM etc.), otherwise the PAM sessiosn might be
  left open, resources not unmounted/freed, etc.

* Mon Mar 12 2018 Fr. Br. George <george@altlinux.ru> 1.16.7-alt17.1
- Fix lightdm-greeter-hide-users control filename

* Fri Dec 22 2017 Ivan Zakharyaschev <imz@altlinux.org> 1.16.7-alt17
- Show the messages from PAM translated.
- Stricter compatibility requirements for client libs.

* Thu Nov 09 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt16
- Fix: Properly report the PAM result before exit the password
  change session.

* Tue Oct 31 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt14
- Fix: Don\'t try to authenticate a user without using a greeter
  on switch-to-user.

* Mon Oct 30 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt13
- Make use of 'default-username' when starting new login session.
- Fixed syntax in lightdm-login-unknown.control.
- Add 'default-username' to the global config too.
- Add 'default-username' seat property.
- Lookup 'login-unknown' first in the seat configuration, then in
  the global section.
- Added control for 'greeter-hide-users' configuration parameter.

* Tue Oct 24 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt12
- Support the 'reset' argument of the CHANGE_PASS message. Use
  "reset-pass-envvar" configuration parameter to set the environment
  variable or set "PAM_RESET_AUTHTOK=1" by default.
- Add "in_chauthtok" property.
- Fix: Clean the 'cancelling' state when the session is complete.
- Fix: Don\'t disconnect signals on cancel before the session
  actually ends.

* Thu Oct 19 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt11
- Added 'lightdm_greeter_change_pass()' and 'CHANGE_PASS' greeter
  message.

* Wed Oct 04 2017 Michael Shigorin <mike@altlinux.org> 1.16.7-alt10
- reverted last change, not needed anymore

* Tue Oct 03 2017 Michael Shigorin <mike@altlinux.org> 1.16.7-alt9
- E2K: add -std=c++11 explicitly (for qt5-enabled build with lcc).

* Tue Aug 08 2017 Michael Shigorin <mike@altlinux.org> 1.16.7-alt8
- BOOTSTRAP: introduce systemd knob (on by default).
- E2K: avoid problematic option.

* Tue Aug 08 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt7
- Extract the "dm-tool" utility into a separate package.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt6
- Fix the control script: Resolve the links because sed -i replaces
  the files.

* Fri Jul 21 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt5
- Added control script 'lightdm-login-unknown'.

* Wed Jul 12 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt4
- Add the 'login-unknown' configuration option.
- Package the bash completion scripts.

* Thu Jun 22 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt3
- When is switching to the greeter, unconditionally use an existing
  one, if any, trying to reset it to the new user name.

* Tue Jun 20 2017 Paul Wolneykien <manowar@altlinux.org> 1.16.7-alt2
- Fixed "Error writing to daemon: Broken pipe".

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.7-alt1
- 1.16.7

* Fri Oct 09 2015 Sergey V Turchin <zerg@altlinux.org> 1.14.0-alt1.1
- NMU: rebuild with new libgcrypt (ALT#31350)

* Tue May 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Nov 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Thu Sep 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.9-alt1
- 1.11.9

* Tue Jul 01 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.4-alt1
- 1.11.4
- add systemd unit

* Tue May 06 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.1-alt1
- 1.11.1

* Fri Apr 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.9.13-alt1.1
- NMU: fix plymouth support
- NMU: fix to use /etc/X11/xinit/xserverrc

* Mon Mar 31 2014 Alexey Shabalin <shaba@altlinux.ru> 1.9.13-alt1
- 1.9.13

* Tue May 28 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Tue Apr 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Mon Feb 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- make greeter and user sessions inherit the system default locale
  (patch from opensuse)

* Thu Jan 31 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt2
- don't require accountservices
- requires any greeter

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Jul 05 2012 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1.1
- NMU: lightdm-greeter-session expects dbus-launch (closes: #27438)

* Thu May 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Mar 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.7-alt1
- 1.1.7
- Add patch and wrapper script to launch dbus for the greeter so that
  we can safely kill it when the greeter ends. (import from ubuntu)

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Thu Feb 16 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Dec 13 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- 1.0.6
- fixed CVE-2011-4105, CVE-2011-3153
- patches from ubuntu

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- set ignore unknown options

* Tue Oct 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- fix PATH env

* Fri Sep 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Sep 20 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.7-alt2
- add alternatives for greeters
- fix dir for lightdm-set-defaults
- define XSESSION_DIR for ALTLinux

* Mon Sep 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Mon Sep 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt2
- fix: package hook for wms-methods.d

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Fri Sep 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt2
- add hook for wms-methods.d based on gdm

* Mon Aug 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Tue May 17 2011 Mykola Grechukh <gns@altlinux.ru> 0.3.3-alt2.2
- hacked to run Xsession with session name not exec (it's ALT Linux
  here, kids...)

* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt2
- add pam config file

* Thu May 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- initial package

