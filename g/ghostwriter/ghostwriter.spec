Name: ghostwriter
Version: 1.8.1
Release: alt2

Summary: Cross-platform, aesthetic, distraction-free Markdown editor

Group: Graphics
License: GPLv3+ and CC-BY and CC-BY-SA and MPLv1.1 and BSD and LGPLv3 and MIT and ISC
Url: https://github.com/wereturtle/ghostwriter

# Source-url: %url/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Patch: ghostwriter-qt5.15-fix.patch

BuildRequires: qt5-base-devel libqt5-core libqt5-network libqt5-gui libqt5-dbus
BuildRequires: qt5-webengine-devel qt5-svg-devel qt5-tools

#BuildRequires: cmake(Qt5LinguistTools)
#BuildRequires: cmake(Qt5XmlPatterns)
#BuildRequires: cmake(Qt5WebEngine)
#BuildRequires: cmake(Qt5X11Extras)
#BuildRequires: cmake(Qt5Network)
#BuildRequires: cmake(Qt5Core)
#BuildRequires: cmake(Qt5DBus)
#BuildRequires: cmake(Qt5Help)
#BuildRequires: cmake(Qt5Gui)
#BuildRequires: cmake(Qt5Svg)
#BuildRequires: cmake(Qt5Xml)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: libhunspell-devel
BuildRequires: gcc-c++

#Requires: hicolor-icon-theme

BuildRequires(pre): rpm-macros-qt5-webengine
# Required qt5-qtwebengine is not available on some arches.
ExclusiveArch: %qt5_qtwebengine_arches

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber's website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%setup
%patch -p2
sed -i 's@appdata/@metainfo/@g' %name.pro

%build
%qmake_qt5 PREFIX=%prefix .
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot
#find_lang %name --with-qt

%files
# -f %name.lang
%doc CHANGELOG.md CONTRIBUTING.md CREDITS.md README.md COPYING
%_bindir/%name
%_man1dir/%name.1*
 %_datadir/ghostwriter
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_pixmapsdir/%name.xpm
%_datadir/metainfo/%name.appdata.xml

%changelog
* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt2
- fix build with Qt 5.15+

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- initial build for ALT Sisyphus
