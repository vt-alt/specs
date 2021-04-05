Name: alt-csp-cryptopro
Version: 0.1.1
Release: alt1

Group: File tools
Summary: CryptoPRO GUI tool
License: GPL-2.0-or-later

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: libprocps-devel
BuildRequires: quazip-qt5-devel
BuildRequires: qt5-tools-devel

Provides: alt-csp-cryptopro-mate = %EVR
Obsoletes: alt-csp-cryptopro-mate < %EVR
Provides: alt-csp-cryptopro-kde = %EVR
Obsoletes: alt-csp-cryptopro-kde < %EVR

%description
CryptoPRO GUI tool

%prep
%setup

%build
%cmake
%cmake_build

%install
%make install -C BUILD DESTDIR=%buildroot
mkdir -p %buildroot/%_qt5_translationdir/
install -m 0644 BUILD/*.qm %buildroot/%_qt5_translationdir/
%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/alt-csp-cryptopro
%_desktopdir/alt-csp-cryptopro.desktop
%_K5srv/ServiceMenus/alt-csp-cryptopro.desktop
%_datadir/file-manager/actions/alt-csp-cryptopro.desktop

%changelog
* Mon Apr 05 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt1
- fix regression
- report no errors

* Sun Apr 04 2021 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- improve UI

* Sun Apr 04 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.6-alt1
- new version

* Mon Feb 01 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.5-alt1
- new version (Closes: 39484, 39547, 39548, 39557)

* Fri Jan 15 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.4-alt1
- new version

* Tue Jan 12 2021 Sergey V Turchin <zerg at altlinux dot org> 0.0.3-alt1
- rearrange UI

* Sat Dec 26 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.2-alt1
- new version

* Fri Dec 04 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt1
- Initial build

