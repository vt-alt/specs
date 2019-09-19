Name: thunar-sendto-clamtk
Version: 0.06
Release: alt1
Summary: Simple virus scanning extension for Thunar
License: GPL+ or Artistic 2.0
Group: Graphical desktop/XFce
Url: https://bitbucket.org/davem_/thunar-sendto-clamtk

Source: https://bitbucket.org/davem_/thunar-sendto-clamtk/downloads/thunar-sendto-clamtk-%version.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: thunar, clamtk >= 5.00

%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.

ClamTk is a front-end for ClamAV.
It is meant to be lightweight and easy to use.

%prep
%setup

%build
%install
desktop-file-install --vendor "" \
	--dir %buildroot%_datadir/Thunar/sendto \
	%name.desktop

%files
%doc CHANGES DISCLAIMER LICENSE README
%_datadir/Thunar/sendto/%name.desktop

%changelog
* Wed Sep 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.06-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

