Name:		wally
Summary:	Qt4 wallpaper changer
Version:	2.4.4
Release:	alt1
License:	GPLv2+
Group:		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://code.google.com/p/wally/
Source0:	http://wally.googlecode.com/files/%name-%version.tar.gz
Source1:	%name.desktop
Patch0:		%name-2.4.4-alt-DSO.diff

BuildRequires: /usr/bin/convert cmake gcc-c++ glib2-devel libSM-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libqt4-devel

%description
Wally is a Qt4 wallpaper changer, using multiple sources like files, folders,
FTP remote folders, Flickr, Yahoo!, Panoramio, Pikeo, Ipernity, Photobucket,
Buzznet, Picasa, Smugmug and Bing images. It runs under Linux, Win32, and MacOSX,
and it's available in many languages.

Supported Window Managers: - Win32 - MacOSX (using OSA scripts) - KDE3 - KDE4
(using WallyPlugin) - Gnome - XFCE4 - Fluxbox - Blackbox - FVWM (unstable) - WindowMaker

%prep
%setup
%patch0 -p1

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 res/images/%name.xpm %buildroot%_miconsdir/%name.png
convert -resize 32x32 res/images/%name.xpm %buildroot%_niconsdir/%name.png
convert -resize 48x48 res/images/%name.xpm %buildroot%_liconsdir/%name.png

install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/wally.desktop

%files
%doc DISCLAIMER README.* LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.2-alt0.2.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.3.2-alt0.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for wally
  * freedesktop-desktop-file-proposed-patch for wally
  * postclean-03-private-rpm-macros for the spec file

* Fri May 14 2010 Motsyo Gennadi <drool@altlinux.ru> 2.3.2-alt0.2
- fix build

* Mon May 03 2010 Motsyo Gennadi <drool@altlinux.ru> 2.3.2-alt0.1
- test build for ALT Linux
