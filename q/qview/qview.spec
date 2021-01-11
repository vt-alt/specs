%define _unpackaged_files_terminate_build 1

Name: qview
Version: 4.0
Release: alt1

Summary: Practical and minimal image viewer
License: GPLv3
Group: Graphics

Url: https://github.com/jurplel/qView
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires: qt5-base-devel

%description
qView is an image viewer designed with minimalism and usability in mind.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.h' -print0 |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
export PREFIX=/usr
qmake-qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
# NB: it's not %%_licensedir
rm -rf %buildroot%_datadir/licenses/%name

%files
%_bindir/%name
%_desktopdir/qView.desktop
%_datadir/metainfo/%name.appdata.xml
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%doc LICENSE

%changelog
* Wed Jan 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 4.0-alt1
- Updated to version 4.0

* Thu Jan 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.0-alt1
- New version

* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Mon May 27 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.0-alt1
- Initial build for ALT
