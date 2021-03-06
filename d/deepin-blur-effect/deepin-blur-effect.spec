%define repo blur-effect

Name: deepin-blur-effect
Version: 1.1.3
Release: alt2.git1d96617
Summary: Offscreen image blurring tool for Deepin
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/blur-effect
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildPreReq: rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libdrm-devel
BuildRequires: libgbm-devel
BuildRequires: libglvnd-devel
BuildRequires: libglfw3-devel libGLEW-devel
# BuildRequires: libpcre-devel libffi-devel libpng-devel libtiff-devel libmount-devel libblkid-devel libselinux-devel

%description
%summary.

%prep
%setup -n %repo-%version
# sed -i 's|#include <gdk-pixbuf/gdk-pixbuf.h>|#include <gdk-pixbuf-2.0/gdk-pixbuf/gdk-pixbuf.h>|' src/main.cc

%build
export CFLAGS+="-Wall -pedantic"
%cmake \
    -GNinja \
    -DBUILD_DEMO=on \
#
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/blur_image
%_bindir/blur-exp

%changelog
* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 1.1.3-alt2.git1d96617
- Added experimental blur for WM.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.3-alt1.git1d96617.1
- NMU: spec: adapted to new cmake macros.

* Mon Mar 29 2021 Leontiy Volodin <lvol@altlinux.org> 1.1.3-alt1.git1d96617
- Initial build for ALT Sisyphus.
- Built from commit 1d96617c21d54e40bd157eea87ef541a28543972.
