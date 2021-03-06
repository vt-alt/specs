%def_disable clang

Name: deepin-system-monitor
Version: 5.8.8
Release: alt1
Summary: A more user-friendly system monitor
License: GPL-3.0+
Group: Monitoring
Url: https://github.com/linuxdeepin/deepin-system-monitor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): desktop-file-utils
BuildRequires: cmake
BuildRequires: dtk5-widget-devel
# BuildRequires: dtk5-wm-devel
BuildRequires: libprocps-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXtst-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-linguist
BuildRequires: libpcap-devel
BuildRequires: libcap-devel
BuildRequires: libncurses-devel
BuildRequires: qt5-tools-devel
BuildRequires: libicu-devel
BuildRequires: deepin-gettext-tools
BuildRequires: libxcbutil-icccm-devel
BuildRequires: dtk5-common
BuildRequires: libnl-devel
Requires: icon-theme-hicolor
#Recommends:     deepin-manual

%description
%summary.

%prep
%setup
# Workaround build failure with GCC 10
# sed -e 's|print_err|print_err_system|g' -i src/process/system_stat.cpp
# sed -e 's|print_err|print_err_process|g' -i src/process/process_stat.cpp
# sed -e 's|print_err|print_err_desktop|g' -i src/process/desktop_entry_stat.cpp

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DLIB_INSTALL_DIR=%_libdir \
    -DAPP_VERSION=%version \
    -DVERSION=%version
%cmake_build

%install
%cmake_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name/
%_datadir/deepin-manual/manual-assets/application/%name/system-monitor/*/*

%changelog
* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.8-alt1
- New version (5.8.8).

* Wed May 19 2021 Arseny Maslennikov <arseny@altlinux.org> 5.8.6-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.6-alt1
- New version (5.8.6) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.0.27-alt1
- New version (5.8.0.27) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.0.9-alt1
- New version (5.8.0.9) with rpmgs script.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.7-alt1
- New version (5.8.0.7) with rpmgs script.
- Fixed build with gcc10.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.4-alt1
- New version (5.8.0.4) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.1-alt1
- New version (5.8.0.1) with rpmgs script.

* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.12-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
