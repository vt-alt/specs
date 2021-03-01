Name:     touchegg-gce
Version:  1.3.1
Release:  alt1.git6f75e4c

Summary:  A graphical user interface for touchegg
License:  GPL-3.0
Group:    Other
Url:      https://github.com/Raffarti/Touchegg-gce

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): qt5-base-devel
BuildRequires: gcc-c++
BuildRequires: qt5-tools

Requires: touchegg

%description
%summary

%prep
%setup

%build
lrelease-qt5 %name.pro
qmake-qt5 %name.pro PREFIX=%_prefix CONFIG_PATH=%_sysconfdir 
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/*
%_desktopdir/%name.desktop
%_iconsdir/%name.*
%_datadir/%name

%changelog
* Sat Feb 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.git6f75e4c
- Initial build for Sisyphus
