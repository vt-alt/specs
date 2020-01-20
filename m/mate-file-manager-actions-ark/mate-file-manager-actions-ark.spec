Summary: Simple scripts for pack and unpack files with ark and caja
Name: mate-file-manager-actions-ark
Version: 2
Release: alt1
Group: Graphical desktop/MATE
License: GPL-2.0-or-later

Url: https://git.altlinux.org/people/lvol/packages/mate-file-manager-actions-ark

Packager: Leontiy Volodin <lvol@altlinux.org>

BuildRequires: mate-file-manager-actions gnome-icon-theme
Requires: mate-file-manager-actions gnome-icon-theme kde5-profile kde5-ark zenity

BuildArch: noarch

Source: %name-%version.tar
Source1: caja-archive-ark
Source2: caja-extract-ark
Source11: caja-archive-ark.desktop
Source12: caja-extract-ark.desktop

%description
The package adds Ark archive support for Caja, the MATE file manager

%prep
%setup

%build
%install
mkdir -p %buildroot%_bindir
cp -a %SOURCE1 %buildroot%_bindir/
cp -a %SOURCE2 %buildroot%_bindir/

mkdir -p %buildroot%_iconsdir/gnome/48x48/actions
ln -s %_iconsdir/gnome/48x48/actions/document-open.png %buildroot%_iconsdir/gnome/48x48/actions/document-open.png
ln -s %_iconsdir/gnome/48x48/actions/document-save.png %buildroot%_iconsdir/gnome/48x48/actions/document-save.png

mkdir -p %buildroot%_datadir/file-manager/actions
cp -a %SOURCE11 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE12 %buildroot%_datadir/file-manager/actions/

%files
#%%doc README
%_bindir/*
%dir %_datadir/file-manager/actions
%_datadir/file-manager/actions/*.desktop
%exclude %_iconsdir/gnome/48x48/actions/document-open.png
%exclude %_iconsdir/gnome/48x48/actions/document-save.png

%changelog
* Thu Dec 26 2019 Leontiy Volodin <lvol@altlinux.org> 2-alt1
- Rewritten extract script because native dialog doesn't work.

* Wed Dec 25 2019 Leontiy Volodin <lvol@altlinux.org> 1-alt1
- Initial build for ALT Sisyphus.
