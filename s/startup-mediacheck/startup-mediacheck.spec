Name: startup-mediacheck
Version: 0.2.4
Release: alt1

Summary: The system startup scripts for mediacheck (warning!)
License: GPL
Group: System/Base

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar

BuildArch: noarch
Requires: console-vt-tools isomd5sum

%description
This package contains scripts to check live/installation media.
/etc/rc.d/rc might need to be emptied for this one to work,
see mkimage-profiles.git::features.in/mediacheck for example.

WARNING: you DO NOT want this package on your own system!

%prep
%setup

%install
mkdir -p -- %buildroot%_sysconfdir/rc.d
install -pm644 inittab.mediacheck %buildroot%_sysconfdir/
install -pm755 rc.sysinit.mediacheck %buildroot%_sysconfdir/rc.d/

%files
%_sysconfdir/inittab.mediacheck
%_sysconfdir/rc.d/rc.sysinit.mediacheck

%changelog
* Wed Dec 16 2020 Anton Midyukov <antohami@altlinux.org> 0.2.4-alt1
- Port on POSIX shell
- Fix log level

* Tue Nov 10 2015 Michael Shigorin <mike@altlinux.org> 0.2.3-alt1
- fixed verifying USB flash media ("sdb1 vs sdb")
- added debug shell at tty11 if check failed

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- explain timeouts beforehand

* Tue Apr 01 2014 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- slightly more legible output

* Tue Apr 01 2014 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- look for 'mediacheck=1' in cmdline, not just 'mediacheck'
- display .disk/info too

* Mon Mar 31 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on startup-rescue 0.15-alt1)

