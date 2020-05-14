Name: vmware-view-preinstall
Version: 5.4.1
Release: alt2

Summary: VMware Horizon Client pre-installation scripts
License: public domain
Group: System/Configuration/Other

Url: http://altlinux.org/vmware-view
ExclusiveArch: %ix86 x86_64

Requires: python-modules-sqlite3
Requires: python-modules-xml
Requires: python-modules-logging

Requires: libgtk+3
Requires: libgst-plugins0.10-base
Requires: libXScrnSaver
Requires: libalsa
Requires: libavutil56
Requires: libdbus
Requires: libgcrypt20
Requires: libnss
Requires: libsane
Requires: libudev0
Requires: libusb
Requires: libva
Requires: libva1
Requires: libxkbfile
Requires: libxml2

BuildArch: noarch

%description
Install this package if you plan to deploy
VMware-Horizon-Client-%version bundle on this system.

%files

%changelog
* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2
- Does not require python2-base.

* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- Update requirements for new version.

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt4
- Make package noarch.

* Thu Mar 14 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt3
- Update requirements from VMware Horizon Client 4.10.0.

* Tue Mar 12 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt2
- Build for i586 and x86_64.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- New version of VMware-Horizon-Client uses bundled libssl and libcrypto.

* Tue Apr 04 2017 Michael Shigorin <mike@altlinux.org> 3.4.0-alt4
- made "64-bit" package "require" i586-libXScrnSaver
  like skype-preinstall (closes: #33325);
  thanks cas@ for the hint

* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt3
- moved scripts to vmware-view-userinstall so this package
  is a pristine preinstall one

* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- made noarch with runtime getconf(1) instead of build-time %%_lib
- added desktop file and an icon beforehand

* Fri Sep 18 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- initial release

