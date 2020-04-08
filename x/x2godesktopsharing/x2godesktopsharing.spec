Name: x2godesktopsharing
Version: 3.2.0.0
Release: alt3
Summary: Desktop Sharing for X2Go

Group: Communications
License: GPLv2+
Url: http://www.x2go.org
Packager: Oleg Solovyov <mcpain@altlinux.org>

Source: %name-%version.tar
Patch1: alt-fix-trayicon-hide.patch
Patch2: alt-fix-quit.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: desktop-file-utils

%description
With the desktop sharing function of X2go you can gain full-access to
the desktop of another computer, similar to programs such as Remote Desktop,
TeamViewer, and LogMeIn. You can see an X2go session from somebody else,
but you can also see a normal desktop.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
lrelease-qt5 x2godesktopsharing.pro
%qmake_qt5 x2godesktopsharing.pro
%make_build

%pre
# Needed for sharing a desktop with another user
getent group x2godesktopsharing >/dev/null || groupadd -r x2godesktopsharing

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/x2go/versions
mkdir -p %buildroot%_datadir/%name/icons
mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,64x64,128x128}/apps
cp -p %name %buildroot%_bindir/
desktop-file-install --dir %buildroot%_desktopdir %name.desktop
install -p -m 644 icons/%name.xpm %buildroot%_datadir/%name/icons/%name.xpm
install -p -m 644 icons/128x128/%name.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -p -m 644 icons/16x16/%name.png %buildroot%_miconsdir/%name.png
install -p -m 644 icons/64x64/%name.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -p -m 644 icons/32x32/%name.png %buildroot%_niconsdir/%name.png
install -p -m 644 VERSION.x2godesktopsharing %buildroot%_datadir/x2go/versions/VERSION.x2godesktopsharing
cp -rp man %buildroot%_datadir/

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_man1dir/%name.1.xz
%_datadir/x2go/versions/VERSION.x2godesktopsharing

%changelog
* Thu Apr 02 2020 Oleg Solovyov <mcpain@altlinux.org> 3.2.0.0-alt3
- don't quit on MATE when confirmation dialog is closed

* Wed Mar 11 2020 Oleg Solovyov <mcpain@altlinux.org> 3.2.0.0-alt2
- release bump (autoimports had bigger version)

* Tue Feb 25 2020 Oleg Solovyov <mcpain@altlinux.org> 3.2.0.0-alt1
- initial build

