Name:       dmenu-wl
Version:    0.1
Release:    alt1
Summary:    Dynamic menu for wayland
Group:      Graphical desktop/Other

License:    MIT
URL:        https://github.com/nyyManni/dmenu-wayland
Source0:    %name-%version.tar

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

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
%doc LICENSE README.md
%_bindir/*
%_man1dir/*

%changelog
* Wed Aug 07 2019 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- New version (0.1).
