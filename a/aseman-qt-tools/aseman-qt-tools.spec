Name: aseman-qt-tools
Version: 1.0.0
Release: alt2
Summary: Shared tools and functions, used in the aseman's projects

License: GPLv3+
Group:   System/Configuration/Other
Url: https://github.com/Aseman-Land/aseman-qt-tools
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

# https://github.com/Aseman-Land/aseman-qt-tools/commit/47412ddb26acf227ee6cb6950f6e9ded01f3375c
# Patch1: 0001-add-plugin-definition-in-qmldir.patch
# https://github.com/Aseman-Land/aseman-qt-tools/commit/8e21628b38078d0b25b37d6fbd853dd2fd3002ad
# Patch2: 0001-chmod-x-on-all-sources.patch
Patch3: alt-qt5.15.patch

BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Fri Apr 21 2017
# optimized out: gcc-c++ libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-sensors libqt5-widgets libstdc++-devel
# python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-xmlpatterns-devel

BuildRequires: libqtkeychain-qt5-devel qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-sensors-devel qt5-serialport-devel
BuildRequires: qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-websockets-devel qt5-x11extras-devel qt5-declarative-devel
BuildRequires: qt5-location-devel
#qt5-quick1-devel qt5-webengine-devel qt5-webkit-devel python3-module-zope


%description
%summary.

%prep
%setup -n %name-%version

# %%patch1 -p1
# %%patch2 -p1
%patch3 -p1

%build
%qmake_qt5       \
      ASEMAN_BUILD_DEST=build \
      QT+=widgets     \
      QT+=multimedia  \
      QT+=dbus        \
      QT+=sensors     \
      QT+=positioning \

%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

%files
%doc LICENSE
%_qt5_qmldir/AsemanTools/

%changelog
* Tue Sep 29 2020 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- Fix compile with Qt-5.15
- Fix build requires

* Sat Apr 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0-alt1.0.git_fb538c7
- Update ftom git fb538c7

* Fri Apr 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 24 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-5
- Trivial fixes

* Sun Jul 24 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-4
- Replace BR with proper qt5-qtdeclarative

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-3
- Remove executable flag from files

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-2
- Backport critical patch

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-1
- Initial package
