Name: installer-feature-cleanup-kernel-stage3
Version: 0.1
Release: alt1

Summary: Purge kernels except running
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%define hookdir %_datadir/install2/postinstall.d

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 98-cleanup-kernel.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Sun Jun 07 2020 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
