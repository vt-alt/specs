Summary: Simple scripts for encrypt and digest files with openssl and caja
Name: mate-file-manager-actions-gost
Version: 5.1
Release: alt1
Group: Graphical desktop/MATE
License: GPL-2.0-or-later

Url: https://git.altlinux.org/people/lvol/packages/mate-file-manager-actions-gost

Packager: Leontiy Volodin <lvol@altlinux.org>

BuildRequires: mate-file-manager-actions gnome-icon-theme
Requires: mate-file-manager-actions gnome-icon-theme fonts-ttf-google-droid-sans-mono diffutils openssl-gost-engine

BuildArch: noarch

Source: %name-%version.tar
Source1: caja-encrypt-gost
Source2: caja-decrypt-gost
Source3: caja-digest-gost
Source4: caja-digest-md5
Source5: caja-digest-sha1
Source6: caja-digest-sha256
Source11: caja-encrypt-gost.desktop
Source12: caja-decrypt-gost.desktop
Source13: caja-digest-gost.desktop
Source14: caja-digest-md5.desktop
Source15: caja-digest-sha1.desktop
Source16: caja-digest-sha256.desktop

%description
The package adds gost-grasshopper encryption and digest for Caja, the MATE file manager

%prep
%setup

%build
%install
mkdir -p %buildroot%_bindir
cp -a %SOURCE1 %buildroot%_bindir/
cp -a %SOURCE2 %buildroot%_bindir/
cp -a %SOURCE3 %buildroot%_bindir/
cp -a %SOURCE4 %buildroot%_bindir/
cp -a %SOURCE5 %buildroot%_bindir/
cp -a %SOURCE6 %buildroot%_bindir/

mkdir -p %buildroot%_iconsdir/gnome/48x48/status
ln -s %_iconsdir/gnome/48x48/status/changes-prevent.png %buildroot%_iconsdir/gnome/48x48/status/changes-prevent.png
ln -s %_iconsdir/gnome/48x48/status/changes-allow.png %buildroot%_iconsdir/gnome/48x48/status/changes-allow.png
ln -s %_iconsdir/gnome/48x48/status/dialog-information.png %buildroot%_iconsdir/gnome/48x48/status/dialog-information.png

mkdir -p %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE11 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE12 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE13 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE14 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE15 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE16 %buildroot%_datadir/file-manager/actions/

#%%post
#control openssl-gost enabled

%files
%doc README
%_bindir/*
%dir %_datadir/file-manager/actions
%_datadir/file-manager/actions/*.desktop
%exclude %_iconsdir/gnome/48x48/status/changes-prevent.png
%exclude %_iconsdir/gnome/48x48/status/changes-allow.png
%exclude %_iconsdir/gnome/48x48/status/dialog-information.png

%changelog
* Mon Dec 23 2019 Leontiy Volodin <lvol@altlinux.org> 5.1-alt1
- Fixed incorrect interface behavior when canceling operation (ALT #37666, #37667).

* Tue Dec 17 2019 Leontiy Volodin <lvol@altlinux.org> 5-alt1
- Disabled output the password.
- Added README file.

* Thu Dec 12 2019 Leontiy Volodin <lvol@altlinux.org> 4-alt2
- Added openssl-gost-engine to Requires.
- Translated desktop files.

* Fri Nov 22 2019 Leontiy Volodin <lvol@altlinux.org> 4-alt1
- Added md5, sha1 and sha256 checksum calculation.
- Added comparison of selected files.
- File name processing implemented without IFS override.
- Expanded encrypt script.

* Wed Nov 20 2019 Leontiy Volodin <lvol@altlinux.org> 3-alt1
- Fixed checksum calculation for files with spaces in names.

* Tue Nov 19 2019 Leontiy Volodin <lvol@altlinux.org> 2-alt1
- Fixed encryption of files with spaces in names.
- The spec was simplified.

* Fri Nov 15 2019 Leontiy Volodin <lvol@altlinux.org> 1-alt1
- Initial build for ALT Sisyphus.
