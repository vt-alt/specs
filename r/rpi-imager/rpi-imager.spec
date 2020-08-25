Name:           rpi-imager
Version:        1.4
Release:        alt1
Summary:        Raspberry Pi Imaging Utility
Group:          System/Configuration/Other

License:        Apache-2.0
URL:            https://github.com/raspberrypi/rpi-imager
Source:         %name-%version.tar
Patch:          %name-%version-alt.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel qt5-declarative-devel qt5-tools-devel
BuildRequires: libarchive-devel libcurl-devel libssl-devel lsblk
BuildRequires: cmake gcc-c++

Requires: qt5-quickcontrols2
Requires: udisks2

%description
Graphical user-interface to write disk images and format SD cards.
Use Raspberry Pi Imager for an easy way to install Raspberry Pi OS and other
operating systems to an SD card ready to use with your Raspberry Pi.

%prep
%setup -n %name-%version
%patch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/metainfo/rpi-imager.metainfo.xml


%changelog
* Tue Aug 18 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.4-alt1
- Update to new release 1.4
- Add support ALT images list directly from:
  https://getalt.org/raspi/os_list_imagingutility_alt.json
  It will work until the "Add ALT image link" issue closes:
  https://github.com/raspberrypi/rpi-imager/issues/95

* Fri Jul 17 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.3-alt1
- Fix version and update to official release

* Sat May 30 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.3-alt1.git.f3bc47a309
- Initial build for Sisyphus

