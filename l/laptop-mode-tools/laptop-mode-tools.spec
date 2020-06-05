Name: 	  laptop-mode-tools
Version:  1.73.1
Release:  alt1

Summary:  Tools for power savings based on battery/AC status
License:  GPL-2.0+
Group:    System/Base
URL:      http://rickysarraf.github.io/laptop-mode-tools/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
# VCS:    https://github.com/rickysarraf/laptop-mode-tools
Patch1:   support-condrestart-in-initscript.patch

BuildArch: noarch
%filter_from_requires \,^/lib/udev/hotplug\.functions,d;\,^systemd$,d

%description
Laptop mode is a Linux kernel feature that allows your laptop to save
considerable power, by allowing the hard drive to spin down for longer
periods of time. This package contains the userland scripts that are
needed to enable laptop mode. It includes support for automatically
enabling laptop mode when the computer is working on batteries. In
addition, it provides a set of modules which allow you to apply
various other power savings.

%prep
%setup -q
%patch1 -p1

%build
DESTDIR=%buildroot INIT_D=%buildroot%_initdir MAN_D=%_mandir INSTALL=install TMPFILES_D=%_tmpfilesdir ./install.sh

%preun
%preun_service laptop-mode

%post
%post_service laptop-mode

%files
%doc COPYING Documentation/*.txt README.md
%_sbindir/*
%config %_sysconfdir/acpi/actions/lm_*.sh
%config %_sysconfdir/acpi/events/lm_*
%config(noreplace) %_sysconfdir/laptop-mode/
%config %_initdir/laptop-mode
%_unitdir/*.service
%_unitdir/*.timer
/lib/udev/lmt-udev
/lib/udev/rules.d/99-laptop-mode.rules
%_sysconfdir/apm/event.d/*
%_sysconfdir/power/scripts.d/*
%_sysconfdir/power/event.d/*
%_datadir/laptop-mode-tools
%_libexecdir/pm-utils/sleep.d/*
%_tmpfilesdir/laptop-mode.conf
%_datadir/polkit-1/actions/org.linux.lmt.gui.policy
%_man8dir/*

%changelog
* Tue Jan 14 2020 Andrey Cherepanov <cas@altlinux.org> 1.73.1-alt1
- New version.
- Fix License according to SPDX.

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.72.2-alt1
- New version.

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.71-alt1
- new version 1.71

* Thu Oct  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.70-alt4
- (.spec) do own %_datadir/laptop-mode-tools

* Thu Oct  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.70-alt3
- (.spec, non-visible) make %%filter_from_requires more readable

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 1.70-alt2
- Fix project homepage (ALT #32576)
- Support condrestart and condstop in initscript (ALT #32577)

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.70-alt1
- New version 1.70
- Remove systemd requirement

* Sun Feb 14 2016 Andrey Cherepanov <cas@altlinux.org> 1.68.1-alt2
- Bump release number to correct upgrade from Autoimports to Sisyphus

* Sun Jan 31 2016 Andrey Cherepanov <cas@altlinux.org> 1.68.1-alt1
- Inital build in Sisyphus

