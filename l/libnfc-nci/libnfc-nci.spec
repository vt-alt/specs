%define _unpackaged_files_terminate_build 1
%def_with secure_P2P
%def_without debug

Name: libnfc-nci
Version: 2.4.1
Release: alt1

Summary: Linux NFC stack for NCI based NXP NFC Controllers.
License: Apache-2.0
Group: System/Libraries

Url: https://www.nxp.com/docs/en/application-note/AN11697.pdf
# Git: https://github.com/NXPNFCLinux/linux_libnfc-nci
Source: %name-%version.tar
Source1: 42-pn5xx_i2c.rules

Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Jul 25 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libstdc++-devel perl pkg-config python-base python-modules sh4
BuildRequires: gcc-c++

%if_with secure_P2P
Buildrequires: libssl-devel
%endif

%description
Linux NFC stack for NCI based NXP NFC Controllers.

%package devel
Summary: Development libraries for libnfc-nci
Group: Development/C
Requires: %name = %version-%release
Requires: pkgconfig

%description devel
The libnfc-nci-devel package contains header files necessary for
developing programs using libnfc-nci.

%package example
Summary: Example using libnfc-nci
Group: System/Libraries
Requires: %name = %version-%release

%description example
The libnfc-nci-example package contains example demonstrating the functionality
of libnfc-nci.

%prep
%setup
%patch0 -p1

%build
./bootstrap

%if_with secure_P2P
# use system openssl and therefore treat the path respectively
sed -i 's|-L\$(openssldir)/lib|-L\$(openssldir)/lib%_libsuff|g' Makefile.am
export openssldir=%_prefix 
%endif

%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif

export exec_prefix=%_prefix
%configure \
	--disable-static \
%if_with debug
	--enable-debug \
%endif
%if_with secure_P2P
	--enable-llcp1_3 \
%endif
	--enable-i2c

%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -delete
mv %buildroot%_sbindir %buildroot%_bindir
install -pDm644 %SOURCE1 %buildroot%_udevrulesdir/42-pn5xx_i2c.rules

%files
%doc README.md LICENSE.txt
%config(noreplace) %_sysconfdir/libnfc-n*.conf
%_libdir/libnfc_nci_linux-1.so.*

%files devel
%_libdir/libnfc_nci_linux.so
%_includedir/*
%_libdir/pkgconfig/*.pc
%doc doc/*

%files example
%_bindir/*
# bring udev rule for NFC chip device node user access only for test purposes
%_udevrulesdir/*.rules

%changelog
* Mon Dec 07 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.4.1-alt1
- fix FTBFS by GCC10 with default -fno-common
- switch to build from tag R2.4.1 which is exactly the same as R2.4+git20190613
- fix license tag

* Thu Nov 07 2019 Michael Shigorin <mike@altlinux.org> 2.4-alt2.dev.git20190613
- E2K: explicit -std=c++11
- minor spec cleanup

* Thu Jul 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.4-alt1.dev.git20190613
- initial build for OS ALT


