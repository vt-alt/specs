%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: lightdm-gtk-greeter
Version: 2.0.7
Release: alt2
Summary: LightDM GTK+ Greeter
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/lightdm-gtk-greeter
#To get source code use the command "bzr branch lp:lightdm-gtk-greeter"
Source: %name-%version.tar
Patch1: %name-%version-alt-fixes.patch
Patch2: %name-%version-advanced.patch

Requires: lightdm >= 1.16.7-alt11
Requires: gnome-icon-theme gnome-icon-theme-symbolic gnome-themes-standard
Requires: /usr/share/design/current

Provides: lightdm-greeter

BuildRequires: gcc-c++ intltool gnome-common gobject-introspection-devel
BuildRequires: glib2-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: pkgconfig(liblightdm-gobject-1) >= 1.3.5
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: lightdm-devel >= 1.16.7-alt11 lightdm-gir-devel >= 1.16.7-alt11
BuildRequires: /usr/bin/exo-csource

%description
This package provides a GTK+-based LightDM greeter engine. In contrast
to the conventional "lightdm-gtk-greeter" package this version is
directly controlled by PAM prompts and messages.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
	%{subst_enable introspection} \
	--disable-static \
	--disable-libindicator \
	--disable-indicator-services-command \
	--enable-at-spi-command="/usr/libexec/at-spi-bus-launcher --launch-immediately" \
	--with-libxklavier \
	--enable-maintainer-mode \
	--libexecdir=%_libexecdir

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

cd %buildroot
# Add alternatives for xgreeters
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-gtk-greeter.desktop\t100\n' >./%_altdir/lightdm-gtk-greeter

%files -f %name.lang
%_altdir/lightdm-gtk-greeter
%_sbindir/lightdm-gtk-greeter
%_datadir/xgreeters/lightdm-gtk-greeter.desktop
%_datadir/doc/lightdm-gtk-greeter/sample-lightdm-gtk-greeter.css
%_datadir/icons/hicolor/scalable/places/*.svg
%config(noreplace) %_sysconfdir/lightdm/lightdm-gtk-greeter.conf

%changelog
* Thu Feb 25 2021 Paul Wolneykien <manowar@altlinux.org> 2.0.7-alt2
- Added "enter-username" config param to explicitly ask for a
  username before authentication starts (closes: 38544).

* Mon Mar 16 2020 Paul Wolneykien <manowar@altlinux.org> 2.0.7-alt1
- Fresh up to v2.0.7.

* Mon Nov 11 2019 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt15
- Russian translation of some prompts and titles (thx Oleg Zenin).
- Translate the prompts and messages (thx Oleg Zenin).

* Thu Aug 22 2019 Nikita Ermakov <arei@altlinux.org> 2.0.1-alt14
- NMU: Update to correspond new lightdm API.

* Mon Mar 18 2019 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt13
- Fix/improve: Restart the authentication session with empty username
  when the user selector is set to "Other...".

* Mon Mar 18 2019 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt12
- Fix: Restart the authentication session with empty username and
  don't use the last authenticated user name when the greeter-hide-users
  hint is set to true (closes: #36293).

* Mon Jan 21 2019 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt11
- A prompt-driven greeter.
- Workaround: Use the theme\'s default foreground color for the
  prompt instead of the special question color because the latter is
  defined in only a few themes.
- A better layout for error messages.
- Load CSS from file ("css-path" config. option).
- Support Pnago markup for error messages.
- Automatically start new authentication session when the password
  is successfully changed.
- Make the login and cancel button labels configurable.
- Use CSS to style the prompt and error messages.
- Conditional change pass (PIN) button.
- Use configurable default info text.
- Clear error when the auth. session is started by the button.
- Append the error messages until user responds.
- Hide cancel button when authentication completes.

* Wed Aug 22 2018 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt10
- Fixed rebuilding: Ignore the "format-nonliteral" warning/error.

* Fri Sep 08 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt9
- Fixed switch-to-user with newly created greeter.

* Wed Jul 12 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt8
- Fix/improve: Start the session with the named user when switching.

* Thu Jun 22 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt7
- Fix: Don\'t claim the greeter as resettable leaving the "reset"
  callback registered.

* Tue Jun 20 2017 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt6
- Make the greeter resettable. On reset, select the provided username
  and start authentication.
- Trying to workaround the weird bug in GTK+3 #710888 related to
  the info_bar.
- Workaround possible race with message label cleanup.
- Hide the message label when it is NULL or empty.

* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt5
- fixed showing messages after empty message showing

* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt4
- fixed showing message about failed login(closes: #33148)

* Fri Feb 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt3
- memory leak fixed

* Fri Feb 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0.1-alt2
- Show multiple PAM messages to user (closes: #33116)

* Thu Mar 03 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed May 13 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Fri Sep 19 2014 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Mar 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Wed Apr 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- enable show-language-selector
- define logo, background, icon-theme-name

* Mon Oct 15 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4
- initial package
