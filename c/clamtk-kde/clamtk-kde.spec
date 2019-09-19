Name: clamtk-kde
Version: 0.18
Release: alt1
Summary: Simple virus scanning extension for Dolphin and Konqueror
License: GPL+ or Artistic 2.0
Group: Graphical desktop/KDE
Url: https://bitbucket.org/davem_/clamtk-kde

Source: https://bitbucket.org/davem_/clamtk-kde/downloads/clamtk-kde-%version.tar.xz
BuildArch: noarch

Requires: kf5-filesystem, clamtk >= 5.00

%description
It allows for right-click virus scanning within the Konqueror or Dolphin file browsers.

ClamTk is a front-end for ClamAV.
It is meant to be lightweight and easy to use.

%prep
%setup

%build
%install
mkdir -p %buildroot%_datadir/kservices5/ServiceMenus
cp -a clamtk-kde.desktop %buildroot%_datadir/kservices5/ServiceMenus/

%files
%doc CHANGES LICENSE README.md
%_datadir/kservices5/ServiceMenus/%name.desktop

%changelog
* Wed Sep 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.18-alt1
- Initial build for ALT Sisyphus.

