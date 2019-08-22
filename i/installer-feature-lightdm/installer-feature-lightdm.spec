Name: installer-feature-lightdm
Version: 0.0.1
Release: alt1

Summary: Installer hook for lightdm configuration
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Installer hook for lightdm configuration.

%package stage3
Summary: Installer stage 3 hook for lightdm configuration
License: GPL
Group: System/Configuration/Other

Requires: lightdm

%description stage3
Installer hook for lightdm configuration.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage3
%hookdir/*

%changelog
* Thu Aug 22 2019 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- Initial build.
