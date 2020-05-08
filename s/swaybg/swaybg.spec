%define _unpackaged_files_terminate_build 1

Name: swaybg
Version: 1.0
Release: alt1
Summary: Wallpaper tool for Wayland compositors 
License: MIT
Url: https://github.com/swaywm/swaybg
Group: Graphical desktop/Other

Source0: %name-%version.tar

BuildRequires: libcairo-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libwayland-client-devel
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: wayland-protocols

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE
%doc README.md
%_bindir/swaybg
%_man1dir/*

%changelog
* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- Initial build
