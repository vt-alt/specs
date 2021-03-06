%def_disable clang

%define repo dde-session-shell

Name: deepin-session-shell
Version: 5.4.13
Release: alt2
Summary: Deepin desktop-environment - Session shell module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-shell
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch1: deepin-session-shell-5.4.5-alt-lightdm-for-lockscreen.patch
Patch2: deepin-session-shell-5.4.13-hide-sleep-and-hibernate.patch

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-tools
BuildRequires: qt5-base-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libpam0-devel
BuildRequires: dtk5-widget-devel
BuildRequires: dtk5-common
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: gsettings-qt-devel
BuildRequires: lightdm-devel
BuildRequires: libgmock-devel
# deepin-gettext-tools dtk5-widget-devel deepin-qt-dbus-factory-devel gsettings-qt-devel libgtk+2-devel lightdm-devel libsystemd-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-multimedia-devel libxcbutil-icccm-devel libXcursor-devel libXtst-devel libpam0-devel qt5-linguist

%description
%summary.

%prep
%setup -n %repo-%version
%patch1 -p1
%patch2 -p1
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/lib|/libexec|' scripts/lightdm-deepin-greeter
sed -i 's|/usr/bin/bash|/bin/bash|' src/dde-shutdown/view/contentwidget.cpp
#sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    src/widgets/fullscreenbackground.cpp \
#    src/session-widgets/userinfo.h
#sed -i 's|/usr/share/backgrounds/deepin/desktop.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    src/session-widgets/lockcontent.cpp \
#    src/dde-shutdown/view/contentwidget.cpp
#sed -i 's|/usr/share/wallpapers/deepin/desktop.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    src/widgets/fullscreenbackground.cpp
#sed -i 's|theme/background/default_background.jpg|theme/background.png|' \
#    src/dde-lock/logintheme.qrc \
#    src/lightdm-deepin-greeter/logintheme.qrc
# We use system-auth instead common-auth on ALT
sed -i 's/common-auth/system-auth/' src/libdde-auth/authagent.cpp
sed -i 's|qdbusxml2cpp|qdbusxml2cpp-qt5|' CMakeLists.txt
sed -i 's|5\.5||' \
    CMakeLists.txt \
    tests/dde-lock/CMakeLists.txt \
    tests/lightdm-deepin-greeter/CMakeLists.txt

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_enabled clang
    -DLLVM_PARALLEL_LINK_JOBS=1 \
    -DLLVM_TARGETS_TO_BUILD="all" \
    -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
    -DLLVM_ENABLE_LIBCXX:BOOL=OFF \
    -DLLVM_ENABLE_ZLIB:BOOL=ON \
%endif
    #
%cmake_build

%install
%cmake_install
chmod +x %buildroot%_bindir/deepin-greeter

%files
%config(noreplace) %_sysconfdir/deepin/greeters.d/00-xrandr
%config(noreplace) %_sysconfdir/deepin/greeters.d/lightdm-deepin-greeter
%_bindir/deepin-greeter
%_bindir/lightdm-deepin-greeter
%_bindir/dde-lock
%_datadir/%repo/
%_desktopdir/dde-lock.desktop
%_datadir/dbus-1/services/*.service
%_datadir/xgreeters/lightdm-deepin-greeter.desktop
%_datadir/glib-2.0/schemas/com.deepin.dde.session-shell.gschema.xml

%changelog
* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt2
- Fixed build with libgmock.so.1.11.0.

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13).

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt4
- Fixed lockscreen.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt3
- Fixed build with dtk 5.4.13.

* Thu Mar 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt2
- Fixed backgrounds.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.45-alt1
- New version (5.3.0.45) with rpmgs script.

* Fri Dec 25 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.41-alt2
- Fixed background.
- Fixed qdbus generations.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.41-alt1
- New version (5.3.0.41) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.24-alt1
- New version (5.3.0.24) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- Initial build for ALT Sisyphus.
