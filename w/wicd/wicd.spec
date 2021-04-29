Name:                wicd
Version:             1.7.4
Release:             alt4
Summary:             Wireless and wired network connection manager

Group:               System/Base
License:             GPLv2+
URL:                 https://launchpad.net/wicd/
Source0:             https://launchpad.net/wicd/1.7/%{version}/+download/%{name}-%{version}.tar.gz
Source1:             org.wicd.daemon.service

Patch0:              wicd-1.7.3-remove-WHEREAREMYFILES.patch
Patch1:              wicd-1.7.3-dbus-failure.patch
Patch2:              wicd-1.7.2.4-dbus-policy.patch
Patch3:              wicd-1.7.3-DaemonClosing.patch
Patch4:              wicd-1.7.3-unicode.patch
Patch5:              wicd-1.7.3-sanitize.patch
# debian patches
Patch13: 03-import-wpath.patch
Patch14: 04-bytes-vs-strings-in-setup.py.patch
Patch26: 26-support_etc-network_scripts.patch
Patch32: 32-prefer_pkexec.patch
Patch34: 34-newer_urwid.patch
Patch35: 35-fix_ValueError_None_is_not_in_list.patch
Patch36: 36-fix_wrongly_displayed_keybinding.patch
Patch37: 37-fix_IndexError_list_index_out_of_range.patch
Patch38: 38-fix_typo_for_pedantic_wpa_supplicant_2.6.patch
Patch39: 39-add_wpa-peap_without_domain.patch
Patch40: 40-initialize_wicd-gtk_wifi-on-off-button.patch
Patch41: 41-fix_wicd-manager-settings.conf_5_man_page_wrt_wired_connect_mode.patch
Patch42: 42-fix_documentation_wrt_generated_dhclient.conf.patch
Patch43: 43-fix-wrong-Galician-translation.patch
Patch44: 44-fix_wicd-curses_AttributeError_in_keypress-function.patch
Patch45: 45-update_systemd_service_file.patch
Patch46: 46-dhcpcd_is_now_dhcpcd5.patch
Patch47: 47-fix-833929-no-autoconnect-when-GUI-is-open.patch

BuildRequires(pre):  rpm-build-python
BuildRequires:       python-devel
BuildRequires:       desktop-file-utils
BuildRequires:       gettext
BuildRequires:       /usr/bin/pybabel
BuildRequires:       pm-utils

Requires:            %{name}-common = %{version}-%{release}
BuildArch:	     noarch

# TMP HACK
#Requires: wicd-gtk = %version-%release
%filter_from_requires /^python2.7.configscript./d
# END HACK


%description
Wicd is designed to give the user as much control over behavior of network
connections as possible.  Every network, both wired and wireless, has its
own profile with its own configuration options and connection behavior.
Wicd will try to automatically connect only to networks the user specifies
it should try, with a preference first to a wired network, then to wireless.

This package provides the architecture-dependent components of wicd.

%package common
Summary:             Wicd common files
Group:               System/Base
BuildArch:           noarch
Requires:            dbus
Requires:            dhcpcd
Requires:            ethtool
Requires:            iproute
Requires:            logrotate
Requires:            net-tools
Requires:            wireless-tools
Requires:            wpa_supplicant

%description common
This package provides the main wicd daemon and the wicd-cli front-end.

%package curses
Summary:             Curses client for wicd
Group:               File tools
BuildArch:           noarch
Requires:            %{name}-common = %{version}-%{release}
Requires:            %{name}-gtk = %{version}-%{release}

%description curses
Client program for wicd that uses a curses interface.

%package gtk
Summary:             GTK+ client for wicd
Group:               Networking/WWW
BuildArch:           noarch
Requires:            %{name}-common = %{version}-%{release}
Requires:            notify-python

%description gtk
Client program for wicd that uses a GTK+ interface.

%prep
%setup -q

# Remove the WHEREAREMYFILES and resetting of ~/.wicd/WHEREAREMYFILES
# This is pointless.  The documentation can just provide WHEREAREMYFILES,
# which we do in this package.
%patch0 -p1

# Handle D-Bus connection failures a little better
%patch1 -p1

# Allow users at the console to control wicd
%patch2 -p1

# Work around bug in DaemonClosing() calls
%patch3 -p1

# Unicode string handling problems
%patch4 -p1 -b .orig

# Prevent crash when saving network settings
# Upstream bug report and patch:
# https://bugs.launchpad.net/wicd/+bug/993912
%patch5 -p1

# debian fixes
%patch13 -p1
# %patch14 -p1
%patch26 -p1
%patch32 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
# %patch46 -p1
%patch47 -p1

# Set correct python2 executable in shebang and scripts
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *)
subst 's|/usr/bin/python|%__python|' wicd/wpath.py

%build
rm -f po/ast.po
export LANG=POSIX
%{__python} setup.py configure \
    --distro redhat \
    --python %__python \
    --lib %{_libdir} \
    --share %{_datadir}/wicd \
    --etc %{_sysconfdir}/wicd \
    --bin %{_bindir} \
    --log %{_var}/log \
    --systemd %{_unitdir} \
    --no-install-init \
    --no-install-pmutils \
    --no-install-gnome-shell-extensions
%python_build
%__python setup.py compile_translations

%install
export LANG=POSIX
%python_build_install
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/backends/be-external.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/backends/be-ioctl.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/cli/wicd-cli.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/curses/curses_misc.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/curses/netentry_curses.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/curses/prefs_curses.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/daemon/wicd-daemon.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/gtk/gui.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/gtk/prefs.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/gtk/wicd-client.py

rm -f %{buildroot}%{_var}/lib/wicd/WHEREAREMYFILES
rm -rf %{buildroot}%{_datadir}/doc
find %{buildroot} -type f -name ".empty_on_purpose" | xargs rm

for lib in %{buildroot}%{python_sitelibdir_noarch}/wicd/*.py ; do
    sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done

mkdir -p %{buildroot}%{_datadir}/dbus-1/system-services
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/dbus-1/system-services/org.wicd.daemon.service

mv %{buildroot}%{_sysconfdir}/logrotate.d/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/wicd.desktop

desktop-file-install \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/wicd-tray.desktop

%find_lang %{name}

%post common
%post_service wicd

%preun common
%preun_service wicd

%files
%doc AUTHORS CHANGES LICENSE NEWS README other/WHEREAREMYFILES

%files common -f %{name}.lang
%dir %{python_sitelibdir_noarch}/wicd
%dir %{_sysconfdir}/wicd
%dir %{_sysconfdir}/wicd/encryption
%dir %{_sysconfdir}/wicd/encryption/templates
%dir %{_sysconfdir}/wicd/scripts
%dir %{_sysconfdir}/wicd/scripts/postconnect
%dir %{_sysconfdir}/wicd/scripts/postdisconnect
%dir %{_sysconfdir}/wicd/scripts/preconnect
%dir %{_sysconfdir}/wicd/scripts/predisconnect
%{_sysconfdir}/acpi/resume.d/80-wicd-connect.sh
%{_sysconfdir}/acpi/suspend.d/50-wicd-suspend.sh
%config(noreplace) %{_sysconfdir}/logrotate.d/wicd
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/wicd.conf
%config(noreplace) %{_sysconfdir}/wicd/dhclient.conf.template.default
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/active
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/active_wired
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/eap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/eap-tls
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/leap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/peap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/peap-tkip
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/psu
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/ttls
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wep-hex
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wep-passphrase
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wep-shared
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wired_8021x
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa-psk
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa-psk-hex
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa-peap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa-peap-wo-domain
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa2-leap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa2-peap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa2-peap-wo-domain
%{_unitdir}/wicd.service
%{python_sitelibdir_noarch}/wicd/*
%{python_sitelibdir_noarch}/wicd-%{version}*.egg-info
%{_bindir}/wicd-cli
%{_bindir}/wicd-client
%{_sbindir}/wicd
%{_datadir}/applications/wicd.desktop
%{_datadir}/dbus-1/system-services/org.wicd.daemon.service
%{_datadir}/man/man1/wicd-client.1*
%{_datadir}/man/man5/wicd-manager-settings.conf.5*
%{_datadir}/man/man5/wicd-wired-settings.conf.5*
%{_datadir}/man/man5/wicd-wireless-settings.conf.5*
%{_datadir}/man/man8/wicd-cli.8*
%{_datadir}/man/man8/wicd.8*
%lang(nl) %{_datadir}/man/nl/man1/wicd-client.1*
%lang(nl) %{_datadir}/man/nl/man5/wicd-manager-settings.conf.5*
%lang(nl) %{_datadir}/man/nl/man5/wicd-wired-settings.conf.5*
%lang(nl) %{_datadir}/man/nl/man5/wicd-wireless-settings.conf.5*
%lang(nl) %{_datadir}/man/nl/man8/wicd.8*
%dir %{_datadir}/wicd
%dir %{_datadir}/wicd/backends
%dir %{_datadir}/wicd/cli
%dir %{_datadir}/wicd/daemon
%{_datadir}/wicd/backends/*
%{_datadir}/wicd/cli/*
%{_datadir}/wicd/daemon/*
%dir %{_var}/lib/wicd
%dir %{_var}/lib/wicd/configurations

%files curses
%dir %{_datadir}/wicd/curses
%{_datadir}/wicd/curses/*
%{_bindir}/wicd-curses
%{_datadir}/man/man8/wicd-curses.8*
%lang(nl) %{_datadir}/man/nl/man8/wicd-curses.8*

%files gtk
%dir %{_datadir}/wicd/gtk
%{_sysconfdir}/xdg/autostart/wicd-tray.desktop
%{_datadir}/wicd/gtk/*
%{_bindir}/wicd-gtk
%{_datadir}/icons/hicolor/*/apps/wicd-gtk.png
%{_datadir}/icons/hicolor/scalable/apps/wicd-gtk.svg
%{_datadir}/pixmaps/wicd-gtk.xpm
%dir %{_datadir}/wicd/icons
%{_datadir}/wicd/icons/*

%changelog
* Mon Apr 12 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.4-alt4
- Fixed startup error in wicd-curses (ALT #39843)
- Many bug fixes and improvements (thanks debian for the patches)

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt3
- Set correct python2 executable in shebang and scripts.

* Thu Mar 07 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.4-alt2
- Fixed FTBFS, added /usr/bin/pybabel to BR (Closes: #36223).

* Fri Nov 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1
- New version

* Thu Oct 08 2015 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt2
- Rebuild with fixed python-module-babel

* Sat May 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.7.3-alt1
- New version
- Remove dependency on pm-utils (https://bugzilla.redhat.com/show_bug.cgi?id=1208313)

* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.7.2.4-alt2
- Initial build in Sisyphus (ALT #30838)

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_12
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_9
- update to new release by fcimport

* Tue Dec 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_8
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_7
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_6
- update to new release by fcimport

* Sun Mar 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_5
- use post/un_service for service-only packages

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_4
- update to new release by fcimport

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.2.4-alt1_2
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.2.1-alt1_2
- new release

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.2.1-alt1_1
- update to new fc release

