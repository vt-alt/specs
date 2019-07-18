Name: skiboot
Version: 6.3.1
Release: alt1
Summary: OPAL Processor Recovery Diagnostics Daemon

Group: System/Servers
License: Apache-2.0
Url: http://github.com/open-power/skiboot
ExclusiveArch: ppc64le

BuildRequires: libssl-devel

# http://git.altlinux.org/gears/s/skiboot.git
Source: %name-%version.tar

%description
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.

%package -n opal-prd
Summary: %summary
Group: System/Servers

%description -n opal-prd
This package provides a daemon to load and run the OpenPower firmware's
Processor Recovery Diagnostics binary. This is responsible for run time
maintenance of OpenPower Systems hardware.

%package -n opal-utils
Summary: OPAL firmware utilities
Group: System/Configuration/Hardware

%description -n opal-utils
This package contains utility programs.

The 'gard' utility can read, parse and clear hardware gard partitions
on OpenPower platforms. The 'getscom' and 'putscom' utilities provide
an interface to query or modify the registers of the different chipsets
of an OpenPower system. 'pflash' is a tool to access the flash modules
on such systems and update the OpenPower firmware.

%package -n opal-firmware
Summary: OPAL firmware
Group: System/Kernel and hardware
BuildArch: noarch

%description -n opal-firmware
OPAL firmware, aka skiboot, loads the bootloader and provides runtime
services to the OS (Linux) on IBM Power and OpenPower systems.

%prep
%setup

%build
export SKIBOOT_VERSION=%version
export OPAL_PRD_VERSION=%version
export GARD_VERSION=%version
export PFLASH_VERSION=%version
export XSCOM_VERSION=%version
export CROSS=
export MAKEFLAGS="${MAKEFLAGS:+$MAKEFLAGS }V=1"
export HOSTCFLAGS='%optflags' OPTS='%optflags' CFLAGS='%optflags'
%make_build
%make_build -C external/opal-prd
%make_build -C external/gard
%make_build -C external/pflash
%make_build -C external/xscom-utils

%install
make -C external/opal-prd install DESTDIR=%buildroot prefix=/usr
make -C external/gard install DESTDIR=%buildroot prefix=/usr
make -C external/xscom-utils install DESTDIR=%buildroot prefix=/usr
make -C external/pflash install DESTDIR=%buildroot prefix=/usr

mkdir -p %buildroot%_unitdir
install -m 644 -p external/opal-prd/opal-prd.service %buildroot%_unitdir/opal-prd.service

mkdir -p %buildroot%_datadir/qemu
install -m 644 -p skiboot.lid %buildroot%_datadir/qemu/skiboot.lid

%post
%post_service opal-prd

%preun
%preun_service opal-prd

%files -n opal-prd
%doc README.md LICENCE
%_sbindir/opal-prd
%_unitdir/opal-prd.service
%_mandir/man8/*

%files -n opal-utils
%doc README.md LICENCE
%_sbindir/opal-gard
%_sbindir/getscom
%_sbindir/putscom
%_sbindir/getsram
%_sbindir/pflash
%_mandir/man1/*

%files -n opal-firmware
%doc README.md LICENCE
%_datadir/qemu/

%changelog
* Thu Jul 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.3.1-alt1
- Initial build.
