Name: nemo-sendto-clamtk
Version: 0.05
Release: alt1.git0430c5c
Summary: Simple virus scanning extension for Nemo
License: GPL+ or Artistic 2.0
Group: Graphical desktop/GNOME
Url: https://bitbucket.org/davem_/nemo-sendto-clamtk

Source: https://bitbucket.org/davem_theunsub/nemo-sendto-clamtk/downloads/nemo-sendto-clamtk-%version.tar.xz
BuildArch: noarch

Requires: nemo, clamtk >= 5.00

%description
It is a simple plugin to allow a right-click, context menu scan of files or folders in nemo, the file manager for Cinnamon.

ClamTk is a front-end for ClamAV.
It is meant to be lightweight and easy to use.

%prep
%setup

%build
%install
mkdir -p %buildroot%_datadir/nemo/actions
cp -a nemo-sendto-clamtk.nemo_action %buildroot%_datadir/nemo/actions/

%files
%doc CHANGES DISCLAIMER LICENSE README.md
%_datadir/nemo/actions/%name.nemo_action

%changelog
* Wed Sep 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.05-alt1.git0430c5c
- Initial build for ALT Sisyphus.
- Built from git with commit 0430c5c.

