
%def_enable sctp
%def_enable nss
%def_enable openssl
%def_disable kronosnetd
%def_enable libnozzle
%def_enable zlib
%def_enable lz4
%def_enable lzo2
%def_enable lzma
%def_enable bzip2
%def_enable zstd
%def_enable installtests

Name: kronosnet
Summary: Multipoint-to-Multipoint VPN daemon
Version: 1.16
Release: alt1
License: GPLv2+ and LGPLv2+
Group: Networking/Other
Url: https://kronosnet.org
# vcs-git: https://github.com/kronosnet/kronosnet
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: libqb-devel libxml2-devel doxygen
%{?_enable_sctp:BuildRequires: lksctp-tools liblksctp-devel}
%{?_enable_nss:BuildRequires: libnss-devel libnspr-devel}
%{?_enable_openssl:BuildRequires: libssl-devel}
%{?_enable_kronosnetd:BuildRequires: pam-devel}
%{?_enable_libnozzle:BuildRequires: libnl-devel}
%{?_enable_zlib:BuildRequires: zlib-devel}
%{?_enable_lz4:BuildRequires: liblz4-devel}
%{?_enable_lzo2:BuildRequires: liblzo2-devel}
%{?_enable_lzma:BuildRequires: liblzma-devel}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_zstd:BuildRequires: libzstd-devel}

%description
Kronosnet, often referred to as knet, is a network abstraction layer designed
for High Availability use cases, where redundancy, security, fault tolerance
and fast fail-over are the core requirements of your application.

%package -n kronosnetd
License: GPLv2+
Group: System/Servers
Summary: Multipoint-to-Multipoint VPN daemon

%description -n kronosnetd
The kronosnet daemon is a bridge between kronosnet switching engine
and kernel network tap devices, to create and administer a
distributed LAN over multipoint-to-multipoint VPNs.
The daemon does a poor attempt to provide a configure UI similar
to other known network devices/tools (Cisco, quagga).
Beside looking horrific, it allows runtime changes and
reconfiguration of the kronosnet(s) without daemon reload
or service disruption.

%package -n libnozzle1
License: LGPLv2+
Summary: Simple userland wrapper around kernel tap devices
Group: System/Libraries

%description -n libnozzle1
This is an over-engineered commodity library to manage a pool
of tap devices and provides the basic
pre-up.d/up.d/down.d/post-down.d infrastructure.

%package -n libnozzle-devel
Summary: Simple userland wrapper around kernel tap devices (developer files)
Group: Development/C
Requires: libnozzle1 = %EVR

%description -n libnozzle-devel
This is an over-engineered commodity library to manage a pool
of tap devices and provides the basic
pre-up.d/up.d/down.d/post-down.d infrastructure.

%package -n libknet1
License: LGPLv2+
Summary: Kronosnet core switching implementation
Group: System/Libraries

%description -n libknet1
The whole kronosnet core is implemented in this library.
Please refer to the not-yet-existing documentation for further
information.

%package -n libknet-devel
Summary: Kronosnet core switching implementation (developer files)
Group: Development/C
Requires: libknet1 = %EVR

%description -n libknet-devel
The whole kronosnet core is implemented in this library.
Please refer to the not-yet-existing documentation for further
information.

%package -n libknet1-crypto-nss-plugin
License: LGPLv2+
Summary: libknet1 nss support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-crypto-nss-plugin
NSS crypto support for libknet1.

%package -n libknet1-crypto-openssl-plugin
License: LGPLv2+
Summary: libknet1 openssl support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-crypto-openssl-plugin
OpenSSL crypto support for libknet1.

%package -n libknet1-crypto-plugins-all
License: LGPLv2+
Summary: libknet1 crypto plugins meta package
Group: System/Libraries
%{?_enable_nss:Requires: libknet1-crypto-nss-plugin}
%{?_enable_openssl:Requires: libknet1-crypto-openssl-plugin}

%description -n libknet1-crypto-plugins-all
meta package to install all of libknet1 crypto plugins

%package -n libknet1-compress-zlib-plugin
License: LGPLv2+
Summary: libknet1 zlib support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-compress-zlib-plugin
zlib compression support for libknet1.

%package -n libknet1-compress-lz4-plugin
License: LGPLv2+
Summary: libknet1 lz4 and lz4hc support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-compress-lz4-plugin
lz4 and lz4hc compression support for libknet1.

%package -n libknet1-compress-lzo2-plugin
License: LGPLv2+
Summary: libknet1 lzo2 support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-compress-lzo2-plugin
lzo2 compression support for libknet1.

%package -n libknet1-compress-lzma-plugin
License: LGPLv2+
Summary: libknet1 lzma support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-compress-lzma-plugin
lzma compression support for libknet1.

%package -n libknet1-compress-bzip2-plugin
License: LGPLv2+
Summary: libknet1 bzip2 support
Group: System/Libraries
Requires: libknet1 = %version-%release

%description -n libknet1-compress-bzip2-plugin
bzip2 compression support for libknet1.

%package -n libknet1-compress-zstd-plugin
License: LGPLv2+
Group: System/Libraries
Summary: libknet1 zstd support
Requires: libknet1 = %version-%release

%description -n libknet1-compress-zstd-plugin
 zstd compression support for libknet1.

%package -n libknet1-compress-plugins-all
License: LGPLv2+
Summary: libknet1 compress plugins meta package
Group: System/Libraries
%{?_enable_zlib:Requires: libknet1-compress-zlib-plugin}
%{?_enable_lz4:Requires: libknet1-compress-lz4-plugin}
%{?_enable_lzo2:Requires: libknet1-compress-lzo2-plugin}
%{?_enable_lzma:Requires: libknet1-compress-lzma-plugin}
%{?_enable_bzip2:Requires: libknet1-compress-bzip2-plugin}
%{?_enable_zstd:Requires: libknet1-compress-zstd-plugin}

%description -n libknet1-compress-plugins-all
Meta package to install all of libknet1 compress plugins

%package -n libknet1-plugins-all
License: LGPLv2+
Summary: Provides libknet1 plugins meta package
Group: System/Libraries
Requires: libknet1-compress-plugins-all
Requires: libknet1-crypto-plugins-all

%description -n libknet1-plugins-all
Meta package to install all of libknet1 plugins

%package tests
License: GPLv2+
Group: System/Libraries
Summary: Provides kronosnet test suite
Requires: libknet1 = %version-%release

%description tests
This package contains all the libknet and libnozzle test suite

%prep
%setup
%patch -p1

echo %version > .version
cp .version .tarball-version

%build
%autoreconf

%configure \
	--enable-man \
	%{?_enable_sctp:--enable-libknet-sctp} \
	%{?_enable_nss:--enable-crypto-nss} \
	%{?_enable_openssl:--enable-crypto-openssl} \
	%{?_enable_zlib:--enable-compress-zlib} \
	%{?_enable_lz4:--enable-compress-lz4} \
	%{?_enable_lzo2:--enable-compress-lzo2} \
	%{?_enable_lzma:--enable-compress-lzma} \
	%{?_enable_bzip2:--enable-compress-bzip2} \
	%{?_enable_zstd:--enable-compress-zstd} \
	%{?_enable_installtests:--enable-install-tests} \
	%{subst_enable kronosnetd} \
	%{subst_enable libnozzle} \
	--with-initdefaultdir=%_sysconfdir/sysconfig \
	--with-systemddir=%_unitdir \
	--with-initddir=%_initdir

%make_build

%install
%makeinstall_std

# tree cleanup
# remove static libraries
find %buildroot -name "*.a" -exec rm {} \;
# remove libtools leftovers
find %buildroot -name "*.la" -exec rm {} \;

# remove docs
rm -rf %buildroot/usr/share/doc/kronosnet


%post -n kronosnetd
%post_service kronosnetd

%preun -n kronosnetd
%preun_service kronosnetd

%if_enabled kronosnetd
%files -n kronosnetd
%doc COPYING.* COPYRIGHT
%dir %_sysconfdir/kronosnet
%config(noreplace) %dir %_sysconfdir/kronosnet/*
%config(noreplace) %_sysconfdir/sysconfig/kronosnetd
%config(noreplace) %_sysconfdir/pam.d/kronosnetd
%config(noreplace) %_logrotatedir/kronosnetd
%_unitdir/kronosnetd.service
%_initdir/kronosnetd
%_sbindir/*
%_man8dir/*
%endif

%if_enabled libnozzle
%files -n libnozzle1
%doc COPYING.* COPYRIGHT
%_libdir/libnozzle.so.*

%files -n libnozzle-devel
%doc COPYING.* COPYRIGHT
%_libdir/libnozzle.so
%_includedir/libnozzle.h
%_pkgconfigdir/libnozzle.pc
%_man3dir/nozzle*.3*
%endif

%files -n libknet1
%doc COPYING.* COPYRIGHT
%_libdir/libknet.so.*
%dir %_libdir/kronosnet

%files -n libknet-devel
%doc COPYING.* COPYRIGHT
%_libdir/libknet.so
%_includedir/libknet.h
%_pkgconfigdir/libknet.pc
%_man3dir/knet*.3*

%if_enabled nss
%files -n libknet1-crypto-nss-plugin
%_libdir/kronosnet/crypto_nss.so
%endif

%if_enabled openssl
%files -n libknet1-crypto-openssl-plugin
%_libdir/kronosnet/crypto_openssl.so
%endif

%files -n libknet1-crypto-plugins-all

%if_enabled zlib
%files -n libknet1-compress-zlib-plugin
%_libdir/kronosnet/compress_zlib.so
%endif

%if_enabled lzo2
%files -n libknet1-compress-lzo2-plugin
%_libdir/kronosnet/compress_lzo2.so
%endif

%if_enabled lz4
%files -n libknet1-compress-lz4-plugin
%_libdir/kronosnet/compress_lz4.so
%_libdir/kronosnet/compress_lz4hc.so
%endif

%if_enabled lzma
%files -n libknet1-compress-lzma-plugin
%_libdir/kronosnet/compress_lzma.so
%endif

%if_enabled bzip2
%files -n libknet1-compress-bzip2-plugin
%_libdir/kronosnet/compress_bzip2.so
%endif

%if_enabled zstd
%files -n libknet1-compress-zstd-plugin
%_libdir/kronosnet/compress_zstd.so
%endif

%if_enabled installtests
%files tests
%_libdir/kronosnet/tests
%endif

%files -n libknet1-compress-plugins-all

%files -n libknet1-plugins-all

%changelog
* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.16-alt1
- 1.16

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.14-alt1
- 1.14

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.13-alt1
- 1.13

* Fri Oct 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.12-alt1
- 1.12

* Mon Jun 17 2019 Alexey Shabalin <shaba@altlinux.org> 1.10-alt1
- 1.10

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.7-alt2
- fixed show version

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.7-alt1
- initial build for ALT


