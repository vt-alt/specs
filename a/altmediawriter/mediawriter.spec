%define sname mediawriter
%define oname ALTMediaWriter

Name:           altmediawriter
Version:        0.4.4
Release:        alt1
Summary:        ALT Media Writer
Group:          System/Configuration/Other

License:        GPLv2+
URL:            https://github.com/altlinux/ALTMediaWriter
Source:         %oname-%version.tar

BuildRequires:  libGConf
BuildRequires:  libappstream-glib
BuildRequires:  liblzma-devel
BuildRequires:  libnss-mdns
BuildRequires:  libyaml-cpp-devel
BuildRequires:  qt5-declarative-devel
BuildRequires:  qt5-x11extras-devel

Requires:       qt5-quickcontrols
Requires:       qt5-quickcontrols2
Requires:       polkit
Requires:       udisks2

%description
A tool to write images of ALT media to portable drives
like flash drives or memory cards.

%prep
%setup -n %oname-%version

%build
%qmake_qt5 PREFIX=%_prefix LIBEXECDIR=%_libexecdir/%name MEDIAWRITER_NAME=%name MEDIAWRITER_VERSION=%version-%release
%make_build

%install
make install INSTALL_ROOT=%buildroot
if [ "%name" != "%sname" ]; then
    for i in %buildroot%_datadir/icons/hicolor/*/apps/%sname.png; do
        mv "$i" "$(dirname $i)/%name.png"
    done
    mv %buildroot%_datadir/applications/%sname.desktop %buildroot%_datadir/applications/%name.desktop
    mv %buildroot%_datadir/appdata/%sname.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml
    sed -i 's/=%sname$/=%name/g' %buildroot%_datadir/applications/%name.desktop
    sed -i 's/%sname\.desktop/%name.desktop/' %buildroot%_datadir/appdata/%name.appdata.xml
fi

%check
appstream-util validate-relax --nonet %buildroot/%_datadir/appdata/%name.appdata.xml

%files
%_bindir/%name
%_libexecdir/%name/
%_datadir/appdata/%name.appdata.xml
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png


%changelog
* Fri May 01 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.4-alt1
- Added qt5-quickcontrols requirement (closes: 38072)
- Updated BuildRequires according to gear-buildreq output
- Changed make to %make_build

* Wed Apr 15 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.3-alt1
- Added missing SSL dll's to windows build

* Wed Apr 15 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.2-alt1
- Removed build instructions from README
- Fixed Unknown architecture text going outside button

* Wed Apr 15 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.1-alt1
- Fixed incorrect encoding of Russian text on Windows
- Improved Windows build.sh so that latest version is displayed
- Fixed MD5 check failing on large files on some 32bit platforms

* Wed Apr 08 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.0-alt1
- Changed metadata and image assets to yaml files from getalt.org
- Turned off md5 check for compressed images
- Added Simply variant
- Added Live releases to some variants

* Tue Mar 10 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.3.0-alt1
- Added generate_releases.sh
- Cleaned up releasesmanager.h by removing unused and unneded fields/logic
- Maked local json loading more obvious
- Added Simply variant
- Increased frontpage row height for Russian text that can span 4 lines
- Added info about rootfs'able image types
- Added a check of whether an image type is supported

* Fri Feb 28 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.2.0-alt1
- Fixed Russian translation
- Added translation source files
- Added automatic metadata generation from getalt.org sources
- Improved win builds
- Changed win build to create 32bit executable
- Removed unneeded Raspberry Pi board drop-down menu

* Tue Nov 05 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
