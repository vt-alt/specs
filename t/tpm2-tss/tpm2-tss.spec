%define udevrules_prefix 60-
%define soname 0
Name: tpm2-tss
Version: 2.3.1
Release: alt2
Summary: TPM2.0 Software Stack
# The entire source code is under BSD except implementation.h and tpmb.h which
# is under TCGL(Trusted Computing Group License).
License: BSD and TCGL
Url: https://github.com/tpm2-software/tpm2-tss
Source0: %name-%version.tar
Source1: %name.watch
Group: System/Configuration/Hardware
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: autoconf-archive
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: libsystemd-devel
BuildRequires: libgcrypt-devel
BuildRequires: openssl-devel

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package -n lib%{name}%{soname}
Summary: TPM2.0 Software Stack
Group: System/Configuration/Hardware
Requires: lib%{name}-common = %EVR


%description -n lib%{name}%{soname}
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package -n lib%{name}-common
Summary: Common files for TPM2.0 Software Stack
Group: System/Configuration/Hardware

%description -n lib%{name}-common
This package contains common files required to work witj libtpm2-tss.

%package -n lib%{name}-devel
Summary: Headers and libraries for building apps that use tpm2-tss
Group: Development/C
Requires: lib%{name}%{soname} = %EVR

%description -n lib%{name}-devel
This package contains headers and libraries required to build applications that
use tpm2-tss.


%prep
%setup

%build
./bootstrap
%autoreconf
# Use built-in tpm-udev.rules, with specified installation path and prefix.
%configure --disable-static --disable-silent-rules --with-udevrulesdir=%_udevrulesdir --with-udevrulesprefix=%udevrules_prefix

%make_build

%install
%makeinstall_std

%pre -n lib%{name}-common
%_sbindir/groupadd -r -f tss >/dev/null 2>&1 ||:
%_sbindir/useradd -g tss -c 'TPM2 Software Stack User' \
    -d /var/empty -s /dev/null -r -l -M tss >/dev/null 2>&1 ||:

%files -n lib%{name}%{soname}
%_libdir/libtss2-mu.so.%{soname}
%_libdir/libtss2-sys.so.%{soname}
%_libdir/libtss2-esys.so.%{soname}
%_libdir/libtss2-rc.so.%{soname}
%_libdir/libtss2-tctildr.so.%{soname}
%_libdir/libtss2-tcti-device.so.%{soname}
%_libdir/libtss2-tcti-mssim.so.%{soname}
%_libdir/libtss2-mu.so.%{soname}.*
%_libdir/libtss2-sys.so.%{soname}.*
%_libdir/libtss2-esys.so.%{soname}.*
%_libdir/libtss2-rc.so.%{soname}.*
%_libdir/libtss2-tctildr.so.%{soname}.*
%_libdir/libtss2-tcti-device.so.%{soname}.*
%_libdir/libtss2-tcti-mssim.so.%{soname}.*

%files -n lib%{name}-common
%doc README.md CHANGELOG.md LICENSE
%_udevrulesdir/%{udevrules_prefix}tpm-udev.rules

%files -n lib%{name}-devel
%_includedir/tss2/
%_libdir/libtss2-mu.so
%_libdir/libtss2-sys.so
%_libdir/libtss2-esys.so
%_libdir/libtss2-rc.so
%_libdir/libtss2-tctildr.so
%_libdir/libtss2-tcti-default.so
%_libdir/libtss2-tcti-device.so
%_libdir/libtss2-tcti-mssim.so
%_libdir/pkgconfig/tss2-mu.pc
%_libdir/pkgconfig/tss2-sys.pc
%_libdir/pkgconfig/tss2-esys.pc
%_libdir/pkgconfig/tss2-rc.pc
%_libdir/pkgconfig/tss2-tctildr.pc
%_libdir/pkgconfig/tss2-tcti-device.pc
%_libdir/pkgconfig/tss2-tcti-mssim.pc
%_mandir/man3/*.3.*
%_mandir/man7/tss2*.7.*

%changelog
* Tue Nov 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.1-alt2
- add tss user and group (ALT #37279)

* Mon Sep 16 2019 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- first build for ALT, based on specfile from Fedora

