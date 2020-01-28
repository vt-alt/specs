Name:     integrity-notifier
Version:  0.6.1
Release:  alt4

Summary:  Integrity event notifier
License:  GPL v2+
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/integrity-notifier.git

Packager: Denis Medvedev <nbr@altlinux.org>
BuildArch: noarch

Requires: runit /bin/tai64n

Source:   %name-%version.tar

%description
Integrity violations happen when a user starts a damaged program.
This script notifies users and optionally administrators about that.

%prep
%setup

%build

%install
install -D -m0755 bin/inotifier-functions.sh \
                  %buildroot/%_bindir/inotifier-functions.sh

install -D -m0755 sbin/notifier.sh %buildroot/%_sbindir/integrity-notifier
install -D -m0755 sbin/scanner.sh %buildroot/%_sbindir/integrity-scanner

install -D -m0755 bin/integrity-notifier.sh \
                  %buildroot/%_bindir/integrity-notifier
install -D -m0644 autostart/integrity-notifier.desktop \
        %buildroot/%_sysconfdir/xdg/autostart/integrity-notifier.desktop

install -D -m0644 etc/message %buildroot/%_sysconfdir/integrity/message
install -D -m0644 etc/desktop_message %buildroot/%_sysconfdir/integrity/desktop_message
install -D -m0644 etc/also %buildroot/%_sysconfdir/integrity/also

install -D -m0644 unit/integrity-notifier.service \
        %buildroot/%_unitdir/integrity-notifier.service
install -D -m0644 unit/integrity-scanner.service \
        %buildroot/%_unitdir/integrity-scanner.service

install -D -m0644 log/config %buildroot/%_logdir/integrityd/config

%files
%doc README.en README
%_sbindir/*
%dir %_sysconfdir/integrity
%config(noreplace) %_sysconfdir/integrity/message
%config(noreplace) %_sysconfdir/integrity/desktop_message
%config(noreplace) %_sysconfdir/integrity/also
%config(noreplace) %_unitdir/integrity-notifier.service
%config(noreplace) %_unitdir/integrity-scanner.service
%config(noreplace) %_logdir/integrityd/config
%_bindir/*
%config(noreplace) %_sysconfdir/xdg/autostart/*

%changelog
* Wed May 29 2019 Denis Medvedev <nbr@altlinux.org> 0.6.1-alt4
- build to c8.1

* Tue May 28 2019 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt3
- Fix: Require /bin/tai64n.

* Sat May 25 2019 Denis Medvedev <nbr@altlinux.org> 0.6.1-alt2
- READMEs updated.

* Mon Apr 29 2019 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt1
- Improve: Use the separate desktop message config file with title
  and message.
- Ignore comments in /etc/integrity/also.
- Fix: Line-buffered grep.
- Fix: Don't collapse on an unknown UID.
- Compare timestamps with the program start time (that's against possible
  dupes).

* Fri Apr 26 2019 Paul Wolneykien <manowar@altlinux.org> 0.6-alt1
- Added desktop notifier.
- Precise timestamps in the records.
- Reworked system notifier service.
- Separate scanner service.

* Fri Mar 15 2019 Denis Medvedev <nbr@altlinux.org> 0.5-alt2
- fixed service and real_notifier is a configurable thing now.

* Tue Mar 12 2019 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
- Initial release.
