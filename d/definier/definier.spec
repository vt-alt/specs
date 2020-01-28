Name:     definier
Version:  0.2
Release:  alt2

Summary:  A graphical interface for defining nrpe checks for check_timed_logs.pl
License:  GPLv2+
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/definier.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
Requires: Xdialog

%description
A graphical interface for defining nrpe checks for check_timed_logs.pl. Check_timed_logs.pl is also included

%prep
%setup

%install
install -Dm 0755 definier %buildroot%_sbindir/definier

%files
%_sbindir/*
%doc *.md

%changelog
* Tue Jan 21 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt2
- build for sisyphus

* Thu Aug 08 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt0.M80C.2
- cleaned up version that generates /etc/nrpe-logs/definier
with data needed for monitoring.

* Wed Aug 07 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt0.M80C.1
- to c8

* Thu Jul 25 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt1
Initial release
