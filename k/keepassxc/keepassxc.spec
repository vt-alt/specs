Name: keepassxc
Version:  2.6.2
Release:  alt1

Summary: KeePassXC Password Safe - light-weight cross-platform password manager
License: GPLv2+
Group: File tools

Url: http://www.keepassxc.org/
#Source: https://github.com/keepassxreboot/keepassxc/releases/download/%version/%name-%version-src.tar.xz
Source: %name-%version.tar

%def_without yubikey
# requires asciidoctor
%def_enable docs

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest gcc-c++
BuildRequires: qt5-base-devel >= 5.2.0 qt5-tools-devel >= 5.2.0 qt5-svg-devel
BuildRequires: libgcrypt-devel >= 1.7.0
BuildRequires: libargon2-devel
BuildRequires: libsodium-devel >= 1.0.12
BuildRequires: zlib-devel >= 1.2.0
BuildRequires: libqrencode4-devel
BuildRequires: libquazip-qt5-devel
# Optional for Auto-Type on X11/Linux:
BuildRequires: libXi-devel, libXtst-devel, qt5-x11extras-devel
# Optional for YubiKey support
%if_with yubikey
BuildRequires: libyubikey-devel, ykpers-devel
%endif
%if_enabled docs
BuildRequires: asciidoctor
%endif

%description
KeePassXC is a community fork of KeePassX, a native cross-platform port of
KeePass Password Safe, with the goal to extend and improve it with new features
and bugfixes to provide a feature-rich, fully cross-platform and modern
open-source password manager.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake \
  -DWITH_CXX11=ON \
  -DWITH_XC_BROWSER=ON \
  -DWITH_XC_NETWORKING=ON \
  -DWITH_XC_AUTOTYPE=ON \
  -DWITH_XC_SSHAGENT=ON \
  -DWITH_XC_KEESHARE=ON \
  -DWITH_XC_KEESHARE_SECURE=ON \
  -DWITH_XC_UPDATECHECK=OFF \
  -DWITH_XC_FDOSECRETS=ON \
%if_enabled docs
  -DWITH_XC_DOCS=ON \
%else
  -DWITH_XC_DOCS=OFF \
%endif
%if_with yubikey
  -DWITH_XC_YUBIKEY=ON
%endif

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/%name
%_desktopdir/org.%name.KeePassXC.desktop
%_datadir/metainfo/org.%name.KeePassXC.appdata.xml
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/*/*
%_datadir/%name
%if_enabled docs
%_mandir/man?/*
%endif

%changelog
* Thu Oct 22 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.2-alt1
- Updated to v2.6.2.

* Thu Aug 20 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.1-alt1
- Updated to v2.6.1.

* Tue Jul 07 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.0-alt1
- Updated to v2.6.0.
- add asciidoctor as a build requirement to build documentation

* Fri Apr 10 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.4-alt1
- Updated to v2.5.4.

* Sun Feb 09 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.3-alt1
- Updated to v2.5.3.

* Mon Jan 13 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.2-alt1
- Updated to v2.5.2.

* Tue Nov 12 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.1-alt1
- Updated to v2.5.1.

* Sat Oct 27 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.0-alt1
- Updated to v2.5.0.
- enable support for Freedesktop.org secret storage DBus protocol

* Wed Jun 12 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.3-alt1
- Updated to v2.4.3.

* Mon Jun 03 2019 Michael Shigorin <mike@altlinux.org> 2.4.2-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Sat Jun 01 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.2-alt1
- Updated to v2.4.2.

* Sun Apr 14 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.1-alt1
- Updated to v2.4.1.
- Check for updates disabled.

* Wed Mar 20 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.0-alt1
- Updated to v2.4.0.
- KeeShare support enabled
- new dependencies: libqrencode, qt5svg, libquazip-qt5

* Thu Aug 23 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.3.4-alt1
- Updated to v2.3.4.

* Sat Jun 16 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.3.3-alt1
- Updated to v2.3.3.

* Mon Oct 23 2017 Pavel Vyazovoy <paulelms@altlinux.org> 2.2.2-alt1
- Updated to v2.2.2.

* Sun Oct 15 2017 Pavel Vyazovoy <paulelms@altlinux.org> 2.2.1-alt1
- Initial build v2.2.1.
