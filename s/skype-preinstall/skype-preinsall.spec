Name:     skype-preinstall
Version:  8.45.0.41
Release:  alt1
Summary:  Compatible layer for install official Skype package
License:  Public Domain
Group:    Networking/Instant messaging
Packager: Andrey Cherepanov <cas@altlinux.org>
 
ExclusiveArch: x86_64
  
Requires: libGConf
Requires: libXScrnSaver
Requires: libXrender
Requires: libXtst
Requires: libalsa
Requires: libdbus
Requires: libexpat
Requires: libfreetype
Requires: libgcc1
Requires: libgtk+2
Requires: libgtk+3
Requires: libnss
Requires: libsecret
Requires: libstdc++6
Requires: libxcb
Requires: libxkbfile

%description
%summary

%files

%changelog
* Thu May 16 2019 Andrey Cherepanov <cas@altlinux.org> 8.45.0.41-alt1
- Rewrite package for preinstall skypeforlinux. Tested on 8.45.0.41-1.

* Wed Oct 28 2015 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- Added explicit R: libqt4 libqt4-x11 so rpminstall is enough

* Tue Sep 02 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
