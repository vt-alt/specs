%define rname kdsoap
%define sover 1
%define libkdsoap libkdsoap%sover
%define libkdsoap_server libkdsoap-server%sover

Name: kde5-%rname
Version: 1.9.1
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: Qt-based client-side and server-side SOAP component
Url: https://www.kdab.com/products/kd-soap
# https://github.com/KDAB/KDSoap
License: (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only AND AGPL-3.0-only

Source: %rname-%version.tar
Patch1: alt-lib-sover.patch

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Mon Aug 17 2020 (-bi)
# optimized out: ca-trust cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt5-core libqt5-gui libqt5-network libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-dev qt5-base-common qt5-base-devel rpm-build-python3 sh4
BuildRequires: boost-devel cmake qt5-base-devel
#BuildRequires: boost-devel cmake qt5-svg-devel qt5-wayland-devel qt5-webengine-devel

%description
KD Soap is a Qt-based client-side and server-side SOAP component.
It can be used to create client applications for web services and also provides
the means to create web services without the need for any further component
such as a dedicated web server.
KD Soap targets C++ programmers who use Qt in their applications.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package -n %libkdsoap
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkdsoap
%name library

%package -n %libkdsoap_server
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkdsoap_server
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt5-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn %rname-%version
#%patch1 -p1

%build
%K5build \
    -DCMAKE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang --with-kde --all-name %name

mkdir -p %buildroot/%_K5archdata/mkspecs/features/
mv %buildroot/%_datadir/mkspecs/features/* %buildroot/%_K5archdata/mkspecs/features/

%files common -f %name.lang

%files -n %libkdsoap
%_libdir/libkdsoap.so.%sover
%_libdir/libkdsoap.so.*
%files -n %libkdsoap_server
%_libdir/libkdsoap-server.so.%sover
%_libdir/libkdsoap-server.so.*

%files devel
%doc kdsoap.pri kdwsdl2cpp.pri
%_K5bin/kdwsdl2cpp
%_K5lib/cmake/KDSoap/
%_K5inc/KDSoap*/
%_K5link/lib*.so
%_K5archdata/mkspecs/features/kdsoap.prf

%changelog
* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt1
- new version

* Mon Aug 17 2020 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- initial build
