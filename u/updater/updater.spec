Name:     updater
Version:  1.2
Release:  alt1

Summary:  Updater of packages for distros with security and integrity
License:  GPL v2+
Group:    Other
Url:      http://git.altlinux.org/gears/u/updater.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Some distros are using technologies like SE and ima/evm.
Updating packages in them needs correct procedure to follow.
Scripts in this distro are needed to ensure that correct procedure.

%prep
%setup

%install
mkdir -p /lib/systemd/system
install -Dm 0750 updater-after %buildroot%_sbindir/updater-after
install -Dm 0750 updater-main %buildroot%_sbindir/updater-main
install -Dm 0750 updater-start %buildroot%_bindir/updater-start
install -Dm 0750 updater-signing %buildroot%_sbindir/updater-signing
install -Dm 0750 updater-utils %buildroot%_sbindir/updater-utils
install -Dm 0750 integrity-applier %buildroot%_bindir/integrity-applier
install -Dm 0640 updater-after.service %buildroot/lib/systemd/system/updater-after.service
install -Dm 0640 updater-main.service %buildroot/lib/systemd/system/updater-main.service
install -Dm 0640 updater-signing.service %buildroot/lib/systemd/system/updater-signing.service
install -Dm 0750 parser-bootloader-data.awk %buildroot%_sbindir/parser-bootloader-data.awk

%files
%doc README
%_sbindir/*
%_bindir/*
/lib/systemd/system/*

%changelog
* Fri Jul 26 2019 Denis Medvedev <nbr@altlinux.org> 1.2-alt1
- fixed not needed deps on selinux, grub. Audit log now
renamed after update
to prevent audit from being disabled after update.

* Thu Jun 06 2019 Denis Medvedev <nbr@altlinux.org> 1.1-alt2
- fix for integrity-applier not generating grub

* Wed May 29 2019 Denis Medvedev <nbr@altlinux.org> 1.1-alt1
- added integrity-applier that correctly sign system

* Mon May 27 2019 Denis Medvedev <nbr@altlinux.org> 1.0-alt1
- e2k grub tolerance.

* Sun May 26 2019 Denis Medvedev <nbr@altlinux.org> 0.9-alt5
- changed temporary exec dir to /var/tmp

* Sun May 26 2019 Denis Medvedev <nbr@altlinux.org> 0.9-alt4
- keyring magic in systemd

* Sun May 26 2019 Denis Medvedev <nbr@altlinux.org> 0.9-alt3
- fix wrong startup unit

* Sun May 26 2019 Denis Medvedev <nbr@altlinux.org> 0.9-alt2
- syntax error fixing in main script

* Sun May 26 2019 Denis Medvedev <nbr@altlinux.org> 0.9-alt1
- added extra step for signing

* Sat May 25 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt5
- program logic fixes

* Fri May 24 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt4
- Regexp fixed, scripts enhanced and fixed

* Fri May 24 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3
- graphical state management code written.

* Fri May 24 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt2
- added needed spaces

* Fri May 24 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt1
- e2k fixes

* Mon May 13 2019 Denis Medvedev <nbr@altlinux.org> 0.7-alt1
- rewrote grub editing

* Fri Apr 26 2019 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
- apt-get and sign features

* Fri Apr 26 2019 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
Initial release
