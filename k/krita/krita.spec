# obsoleted koffice version
%define koffice_ver 4:2.3.70

%define sover 18
%define libkritacommand libkritacommand%sover
%define libkritaimpex libkritaimpex%sover
%define libkritalibkis libkritalibkis%sover
%define libkritalibkra libkritalibkra%sover
%define libkritaqml libkritaqml%sover
%define libkritawidgetutils libkritawidgetutils%sover
%define libkritametadata libkritametadata%sover
%define libkritaglobal libkritaglobal%sover
%define libkritaversion libkritaversion%sover
%define libkritabasicflakes libkritabasicflakes%sover
%define libkritastore libkritastore%sover
%define libkritaimage libkritaimage%sover
%define libkritalibbrush libkritalibbrush%sover
%define libkritawidgets libkritawidgets%sover
%define libkritaflake libkritaflake%sover
%define libkritaundo2 libkritaundo2%sover
%define libkritatextlayout libkritatextlayout%sover
%define libkritaui libkritaui%sover
%define libkritaplugin libkritaplugin%sover
%define libkritapsd libkritapsd%sover
%define libkritaodf libkritaodf%sover
%define libkritalibpaintop libkritalibpaintop%sover
%define libkritapigment libkritapigment%sover
%define libkritacolor libkritacolor%sover
%define libkritacolord libkritacolord%sover
%define libkritatext libkritatext%sover

Name: krita
Version: 4.2.7.1
Release: alt1
%K5init no_altplace

Group: Graphics
Summary: A creative sketching and painting application
Url: http://krita.org/
License: GPLv3

AutoReq: yes, nopython
AutoProv: yes, nopython nopython3
%add_python3_path %_libdir/krita-python-libs
%add_python3_path %_datadir/krita/pykrita
%add_python3_req_skip PyKrita pykrita
#Requires: kde5-kross-python
Requires: create-resources

Provides: calligra-krita = %EVR
Obsoletes: calligra-krita < %EVR
Provides: koffice-krita = %koffice_ver
Obsoletes: koffice-krita < %koffice_ver

Source: krita-%version.tar
Patch1: alt-find-pyqt.patch
Patch2: alt-py3-syntax-error.patch

# Automatically added by buildreq on Thu Nov 16 2017 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils fontconfig gcc-c++ glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache ilmbase-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgpg-error liblcms2-devel libpoppler-devel libpoppler1-qt5 libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base python3-module-yieldfrom qt5-base-common qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: appstream boost-devel eigen3 extra-cmake-modules git-core kf5-karchive-devel kf5-kcrash-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kwindowsystem-devel libXres-devel libexiv2-devel libfftw3-devel libgomp-devel libgsl-devel libjpeg-devel libpng-devel libpoppler-qt5-devel libquadmath-devel libraw-devel libssl-devel libtiff-devel libxcbutil-devel openexr-devel python-module-google python3-dev python3-module-zope qt5-multimedia-devel qt5-svg-devel qt5-wayland-devel qt5-x11extras-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-python3 rpm-build-kf5
BuildRequires: zlib-devel libssl-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-multimedia-devel qt5-svg-devel qt5-wayland-devel qt5-x11extras-devel
BuildRequires: python3-devel python3-module-PyQt5-devel python3-module-sip-devel
BuildRequires: boost-devel eigen3 libfftw3-devel libgomp-devel libgsl-devel
#BuildRequires: libgif-devel
BuildRequires: libquazip-qt5-devel
#BuildRequires: libquadmath-devel
BuildRequires: libopencolorio-devel
BuildRequires: libXres-devel libxcbutil-devel
BuildRequires: libjpeg-devel libpng-devel libpoppler-qt5-devel libraw-devel libtiff-devel openexr-devel
BuildRequires: libexiv2-devel liblcms2-devel libheif-devel
BuildRequires: kf5-karchive-devel kf5-kcrash-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kwindowsystem-devel

%description
Krita is a free and open source digital painting application.
It is for artists who want to create professional work from start to end.
Krita is used by comic book artists, illustrators, concept artists, matte
and texture painters and in the digital VFX industry.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
%description devel
Header files and libraries needed for %name development

%package -n %libkritatext
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritatext
%name library.

%package -n %libkritacolord
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritacolord
%name library.

%package -n %libkritacolor
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritacolor
%name library.

%package -n %libkritapigment
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritapigment
%name library.

%package -n %libkritalibpaintop
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritalibpaintop
%name library.

%package -n %libkritaodf
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaodf
%name library.

%package -n %libkritapsd
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritapsd
%name library.

%package -n %libkritaplugin
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaplugin
%name library.

%package -n %libkritaui
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaui
%name library.

%package -n %libkritatextlayout
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritatextlayout
%name library.

%package -n %libkritaundo2
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaundo2
%name library.

%package -n %libkritaflake
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaflake
%name library.

%package -n %libkritawidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritawidgets
%name library.

%package -n %libkritalibbrush
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritalibbrush
%name library

%package -n %libkritaimage
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaimage
%name library

%package -n %libkritastore
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritastore
%name library

%package -n %libkritabasicflakes
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritabasicflakes
%name library

%package -n %libkritaversion
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaversion
%name library

%package -n %libkritaglobal
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaglobal
%name library

%package -n %libkritawidgetutils
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritawidgetutils
%name library

%package -n %libkritacommand
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritacommand
%name library

%package -n %libkritaimpex
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaimpex
%name library

%package -n %libkritalibkis
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritalibkis
%name library

%package -n %libkritalibkra
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritalibkra
%name library

%package -n %libkritaqml
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritaqml
%name library

%package -n %libkritametadata
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkritametadata
%name library

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i 's|sip_bin:.*|sip_bin:%_bindir/sip3")|' cmake/modules/FindSIP.py
sed -i 's|default_sip_dir:.*|default_sip_dir:%_datadir\/sip3")|' cmake/modules/FindSIP.py

%build
%K5build \
    -DRELEASE_BUILD=ON \
    -DFOUNDATION_BUILD=OFF \
    #

%install
%K5install
%K5install_move data color-schemes

# remove InitialPreference
for f in %buildroot/%_K5xdgapp/*.desktop ; do
    sed -i '/^InitialPreference=/d' $f
done

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc AUTHORS README*
%_K5icon/*/*/mimetypes/application-x-krita.*

%files
%config(noreplace) %_K5xdgconf/kritarc
%_K5bin/krita*
%_libdir/kritaplugins/
%_libdir/krita-python-libs/
%_K5qml/org/krita/
%_datadir/krita/
%_datadir/kritaplugins/
%_datadir/color/icc/krita/
#%_K5plug/krita/
%_K5xdgapp/*krita*.desktop
%_K5icon/*/*/apps/krita.*
%_K5data/color-schemes/*
%_datadir/metainfo/*krita*.xml

#%files devel
#%_K5link/lib*.so
#%_K5inc/krita/
#%_K5inc/*.h

%files -n %libkritacommand
%_libdir/libkritacommand.so.%sover
%_libdir/libkritacommand.so.*
%files -n %libkritaimpex
%_libdir/libkritaimpex.so.%sover
%_libdir/libkritaimpex.so.*
%files -n %libkritalibkis
%_libdir/libkritalibkis.so.%sover
%_libdir/libkritalibkis.so.*
%files -n %libkritalibkra
%_libdir/libkritalibkra.so.%sover
%_libdir/libkritalibkra.so.*
%files -n %libkritaqml
%_libdir/libkritaqml.so.%sover
%_libdir/libkritaqml.so.*

%files -n %libkritatext
%_libdir/libkritatext.so.%sover
%_libdir/libkritatext.so.*

%files -n %libkritacolord
%_libdir/libkritacolord.so.%sover
%_libdir/libkritacolord.so.*

%files -n %libkritacolor
%_libdir/libkritacolor.so.%sover
%_libdir/libkritacolor.so.*

%files -n %libkritapigment
%_libdir/libkritapigment.so.%sover
%_libdir/libkritapigment.so.*

%files -n %libkritaodf
%_libdir/libkritaodf.so.%sover
%_libdir/libkritaodf.so.*

%files -n %libkritalibpaintop
%_libdir/libkritalibpaintop.so.%sover
%_libdir/libkritalibpaintop.so.*

%files -n %libkritapsd
%_libdir/libkritapsd.so.%sover
%_libdir/libkritapsd.so.*

%files -n %libkritaplugin
%_libdir/libkritaplugin.so.%sover
%_libdir/libkritaplugin.so.*

%files -n %libkritaui
%_libdir/libkritaui.so.%sover
%_libdir/libkritaui.so.*

%files -n %libkritatextlayout
%_libdir/libkritatextlayout.so.%sover
%_libdir/libkritatextlayout.so.*

#%files -n %libkritaundo2
#%_libdir/libkritaundo2.so.%sover
#%_libdir/libkritaundo2.so.*

%files -n %libkritaflake
%_libdir/libkritaflake.so.%sover
%_libdir/libkritaflake.so.*

%files -n %libkritawidgets
%_libdir/libkritawidgets.so.%sover
%_libdir/libkritawidgets.so.*

%files -n %libkritalibbrush
%_libdir/libkritalibbrush.so.%sover
%_libdir/libkritalibbrush.so.*

%files -n %libkritaimage
%_libdir/libkritaimage.so.%sover
%_libdir/libkritaimage.so.*

%files -n %libkritastore
%_libdir/libkritastore.so.%sover
%_libdir/libkritastore.so.*

%files -n %libkritabasicflakes
%_libdir/libkritabasicflakes.so.%sover
%_libdir/libkritabasicflakes.so.*

%files -n %libkritaversion
%_libdir/libkritaversion.so.%sover
%_libdir/libkritaversion.so.*

%files -n %libkritaglobal
%_libdir/libkritaglobal.so.%sover
%_libdir/libkritaglobal.so.*

%files -n %libkritawidgetutils
%_libdir/libkritawidgetutils.so.%sover
%_libdir/libkritawidgetutils.so.*

%files -n %libkritametadata
%_libdir/libkritametadata.so.%sover
%_libdir/libkritametadata.so.*

%changelog
* Tue Oct 08 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.7.1-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.5-alt1
- new version

* Mon Jul 01 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Jun 21 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt1
- new version (ALT#36818)

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 4.1.8-alt1
- new version (ALT#36336)

* Thu Sep 13 2018 Sergey V Turchin <zerg@altlinux.org> 4.1.1-alt2
- fix to build witn new libraw

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 4.1.1-alt1
- new version

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.2-alt2
- NMU: rebuilt with boost-1.67.0

* Wed Nov 15 2017 Sergey V Turchin <zerg@altlinux.org> 3.3.2-alt1
- initial build
