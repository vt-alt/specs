%add_findprov_skiplist %python_sitelibdir/blink/*

Name:    blink-qt
Version: 3.2.1
Release: alt0.1

Summary: Blink SIP Client
License: GPL-3.0+
Group:   Other
URL:     http://icanblink.com/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: libvncserver-devel
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-application >= 2.0.0
BuildRequires: python-module-cjson
BuildRequires: python-module-Cython
BuildRequires: python-module-enum34
BuildRequires: python-module-eventlib
BuildRequires: python-module-gnutls
BuildRequires: python-module-google-api-client >= 1.6.5
BuildRequires: python-module-lxml
BuildRequires: python-module-oauth2client
BuildRequires: python-module-PyQt5 >= 5.0
BuildRequires: python-module-sipsimple >= 3.0.0
BuildRequires: python-module-twisted-core
BuildRequires: python-module-zope.interface

%py_requires service_identity twisted.names

Source:  %name-%version.tar
Patch1:  alt-desktop-l10n.patch

%description
Fully featured, easy to use SIP client with a Qt based UI Blink is a
fully featured SIP client written in Python and built on top of SIP
SIMPLE client SDK with a Qt based user interface. Blink provides real
time applications based on SIP and related protocols for Audio, Video,
Instant Messaging, File Transfers, Desktop Sharing and Presence.

%prep
%setup -n %name-%version
%patch1 -p1

%build
%python_build

%install
%python_install
install -Dm 0644 debian/blink.desktop %buildroot%_desktopdir/blink.desktop
install -Dm 0644 debian/blink.xpm %buildroot%_pixmapsdir/blink.xpm
install -Dm 0644 debian/blink.1 %buildroot%_man1dir/blink.1

%files
%doc README LICENSE TODO
%_bindir/blink
%_datadir/blink
%_desktopdir/blink.desktop
%_pixmapsdir/blink.xpm
%python_sitelibdir/blink/
%python_sitelibdir/*.egg-info
%_man1dir/blink.1*

%changelog
* Fri Nov 20 2020 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt0.1
- cleanup provides

* Thu Mar 05 2020 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.
- Fix license tag according to SPDX.

* Wed Feb 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Wed Mar 07 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt2
- Add desktop file, pixmap and man page

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- Initial build in Sisyphus
