Name:		nitroshare
Release:	alt1
Version:	0.3.4
Summary:	Transfer files from one device to another made extremely simple
License:	MIT
Group:		Networking/File transfer
Url:		https://%name.net

Source0:	%name-%version.tar.gz
Source1:	%name-uk_UA.ts

Patch0:		%name-0.3.4-QStyle.patch

# Automatically added by buildreq on Sun Sep 20 2020 (-bi)
# optimized out: cmake-modules elfutils fontconfig fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libatk-devel libcairo-devel libdbusmenu-devel libdbusmenu-gtk2 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgtk+2-devel libharfbuzz-devel libpango-devel libqt5-core libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-xml libsasl2-3 libstdc++-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-tools rpm-build-gir rpm-build-python3 sh4 xz
BuildRequires: cmake libappindicator-devel libnotify-devel libqhttpengine-devel libqmdnsengine-devel libssl-devel python-modules-compiler python3-dev qt5-svg-devel qt5-tools-devel

%description
A cross-platform network file transfer application designed to make
transferring any file to any device as painless as possible.
Features
    Runs on Windows / Mac OS X / Linux
    Automatic discovery of devices on the local network
    Simple and intuitive user interface
    Transfer entire directories
    Completely free and open-source

%prep
%setup
%patch0 -p1

%build
cp -a %SOURCE1 src/data/ts/uk_UA.ts
mkdir build && cd build
cmake ../. \
		-DCMAKE_INSTALL_PREFIX=%prefix \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
cd build
%make_install DESTDIR=%buildroot install

%files
%doc README.md LICENSE.txt
%_bindir/%name
%_man1dir/%name.1*
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/scalable/apps/%{name}*.svg
%_datadir/icons/breeze*/apps/*/%{name}*.svg
%_datadir/icons/ubuntu*/apps/*/%{name}*.svg
%_datadir/icons/gnome/24x24/apps/%{name}*.png
%_datadir/icons/ubuntu*/apps/*/%{name}*.png

# #%files extension-nautilus
%_datadir/nautilus-python/extensions/%name.py*

# #%files extension-nemo
%_datadir/nemo-python/extensions/%name.py*

# #%files extension-caja
%_datadir/caja-python/extensions/%name.py*

# #%files console
%_bindir/%name-send

# #%files kservice
%_datadir/kservices5/%{name}_addtoservicemenu.desktop

%changelog
* Sun Sep 20 2020 Motsyo Gennadi <drool@altlinux.ru> 0.3.4-alt1
- initial build
