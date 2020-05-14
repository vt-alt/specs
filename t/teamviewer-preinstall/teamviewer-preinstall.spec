Name: teamviewer-preinstall
Version: 15.0
Release: alt1

Summary: TeamViewer pre-installation scripts
Group: Networking/WWW
License: Public domain
Url: http://www.teamviewer.com

Source: %name-%version.tar

BuildArch: noarch

Requires: libalsa
Requires: libSM libXext libXtst libXau
Requires: libXdamage libXfixes libXrender
Requires: libXinerama libXrandr
Requires: libdbus
Requires: libqt5-webkitwidgets libqt5-x11extras qt5-quickcontrols
Requires: bash4

%build

%description
TeamViewer pre-installation package.
See http://www.teamviewer.com and https://www.altlinux.org/TeamViewer

Download teamviewer_15.5.tar.xz, untar, 'cd' to it, run ./teamviewer as user
Run this, if your default shell is bash3:

$ find . -type f -print0 | xargs -0 sed -i 's!#\!/bin/bash!#\!/bin/bash4!g'
$ find . -type f -print0 | xargs -0 sed -i 's!#\!/bin/sh!#\!/bin/sh4!g'

%post
echo "Download teamviewer_15.5.tar.xz, untar, 'cd' to it, run ./teamviewer as user"  >&2
echo "See https://www.altlinux.org/TeamViewer" >&2

if [ "${BASH_VERSINFO[0]}" -lt 4 ];then
	echo "Run this, if your default shell is bash3:"  >&2
	echo "$ find . -type f -print0 | xargs -0 sed -i 's!#\!/bin/bash!#\!/bin/bash4!g'" >&2
	echo "$ find . -type f -print0 | xargs -0 sed -i 's!#\!/bin/sh!#\!/bin/sh4!g'" >&2
fi

%files

%changelog
* Fri May 01 2020 Lenar Shakirov <snejok@altlinux.org> 15.0-alt1
- preinstall packages for native teamviewer_15.5.tar.xz

* Thu Jan 26 2017 Andrey Cherepanov <cas@altlinux.org> 11.0-alt2
- Add glibc-nss to requirements

* Mon Jul 11 2016 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1
- Adapt for new Arepo: package symlinks to 32-bit kibraries

* Fri Mar 16 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- build only for i586 (use arepo for i586-teamviewer-preinstall)

* Thu Mar 01 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- fix requires for both x86_64 and i586

* Mon Jan 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- initial build for ALT Linux Sisyphus
