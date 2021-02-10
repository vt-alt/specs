%define rname kcolorpicker

%define sover 0
%define libkcolorpicker libkcolorpicker%sover

Name: kde5-%rname
Version: 0.1.5
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: QToolButton with color popup menu with lets you select a color
Url: https://github.com/ksnip/kcolorpicker
License: LGPL-3.0

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Feb 05 2021 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libqt5-core libqt5-gui libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel rpm-build-python3 sh4
#BuildRequires: cmake python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake qt5-svg-devel qt5-wayland-devel qt5-webengine-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcolorpicker
Group: System/Libraries
Summary: KF5 library
#Requires: %name-common = %version-%release
%description -n %libkcolorpicker
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K5install
#find_lang %name --with-kde --all-name

%files devel
%_includedir/kColorPicker/
%_libdir/cmake/kColorPicker/
%_K5link/lib*.so

%files -n %libkcolorpicker
%doc LICENSE* README.md
%_K5lib/libkColorPicker.so.%sover
%_K5lib/libkColorPicker.so.*

%changelog
* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 0.1.5-alt1
- initial build
