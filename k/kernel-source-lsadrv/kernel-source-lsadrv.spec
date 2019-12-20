%define module_name lsadrv
%define module_version 1.2.3
%define module_release	alt2

%define module_source	%module_name-%module_version.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Epoch: 1

Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name modules sources for Hitachi StarBoard.
License: GPL-3.0+
Group: Development/Kernel
URL: http://www.charmexdocs.com/int/software/SBS0962_LINUX.zip
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name modules sources for Linux kernel.
This is usable for Hitachi StarBoard interactive whiteboard.
    FX-63/77(G)/82(WG) Wired
    FX-DUO-63/77/88W Wired
    FX-TRIO-77/77(S)/88W

%prep
%setup -n %module_name-%module_version

%install
mkdir -p %kernel_srcdir
cd ..
mv %module_name-%module_version kernel-source-%module_name-%module_version
tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
	%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Wed Dec 11 2019 Vitaly Chikunov <vt@altlinux.org> 1:1.2.3-alt2
- Fix compilation for std-def (warranty void)
- Update license tag to GPL-3.0+

* Fri Feb 19 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.2.3-alt1
- New version (ALT #31825)
- Change project homepage

* Sat Feb 5 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt5
- tar.xz replaceb by tar

* Sat Feb 5 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt4
- added provides section

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt3
- added interactive whiteboard to description

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt2
- changed packager to Kernel Maintainer Team

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt1
- initial build
