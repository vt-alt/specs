Name:     state-change-notify
Version:  0.1.0
Release:  alt3

Summary:  System state transition notifications helper
License:  GPL-3.0-or-later
Group:    System/Configuration/Other
Url:      http://git.altlinux.org/people/manowar/packages/state-change-notify.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: ronn

%description
The package provides the 'state-change-notify' wrapper script
to help to run system state change (boot-up, reboot, sleep, shutdown)
notification handlers.

The corresponding systemd services and handlers are provided
separately in other packages.

%package postfix
Summary:  Send mail on system state transitions
Group:    System/Configuration/Other
Requires: %name(action:mail)
Requires: postfix
Requires: %name >= %version
Provides: %name(service:mta)

%description postfix
The package provides a systemd(8) unit that reacts
to system state changes such as initialization, reboot, sleep or
shutdown. When such transition is in progress, network connectivity
is present and the 'postfix.service' is active the service invokes
the 'mail' handler (state-change-notify-mail(5)) to send notifications
about the event.

%package mail
Summary: E-Mail notification handler for %name
Group:    System/Configuration/Other
Requires: %name(service:mta)
Provides: %name(action:mail)

%description mail
The 'mail' notification handler uses mail(1) command to send
notifications about system state transitions by E-Mail.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%dir %_sysconfdir/%name
%_sysconfdir/%name/default.conf
%_sbindir/%name
%_man8dir/%name.8*

%files postfix
%config(noreplace) %_unitdir/%name-postfix.service
%_man8dir/%name-postfix.8*

%files mail
%config(noreplace) %_sysconfdir/%name/mail.conf
%config(noreplace) %_sysconfdir/%name/actions.d/mail
%_man8dir/%name-mail.8*
%_man5dir/%name-mail.5*

%changelog
* Mon Nov 25 2019 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Fix/improve: Flush the Postfix mail queue after notification.

* Mon Nov 25 2019 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Initial version for ALT.
