Name: tgsend
Version: 1.3.3
Release: alt1
License: GPL-2.0-or-later and BSD-3-Clause
Group: Networking/WWW
Summary: Simple Telegram bot sender
Packager: Anton Shevtsov <x09@altlinux.org>
Requires: libssl-devel
Requires: libssl10

Buildrequires(pre): rpm-build-fpc
BuildRequires: fpc upx lazarus libssl10

ExclusiveArch: %ix86 x86_64

Source: tgsend-%version.tar

%description
Simple Telegram bot message/file console sender

%prep
%setup -q
sed -i "s/'libssl.so'/'libssl.so.10'/g;s/'libcrypto.so'/'libcrypto.so.10'/g" synapse/ssl_openssl_lib.pas

%build
%_bindir/lazbuild --verbose synapse/laz_synapse.lpk
%_bindir/fpc  -MObjFPC -Scgi -CX -Cg -Os3 -XX -l -vewnhibq -Fu./synapse/lib/%fpc_arch -Fu%_libdir/lazarus/packager/units/%fpc_arch -Fu./ -o./%name -Fr%_libdir/fpc/msg/errore.msg %name.lpr

%_bindir/upx %_builddir/%name-%version/tgsend

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_defaultdocdir/%name-%version

install -m 755 tgsend %buildroot%_bindir
install -m 644 tgsend.conf %buildroot%_sysconfdir/tgsend.conf.example

%files
%doc CREDITS
%_bindir/tgsend
%_sysconfdir/tgsend.conf.example

%changelog
* Tue Dec 17 2019  Anton Shevtsov <x09@altlinux.org> 1.3.3-alt1
- Fix Synapse library for ALT p9 build
- Change license to GPL-2.0-or-later and BSD-3-Clause

* Tue Dec 5 2019 Anton Shevtsov <x09@altlinux.org> 1.3.2-alt1
- Help page fixed

* Thu Nov 26 2019 Anton Shevtsov <x09@altlinux.org> 1.3.1-alt1
- Initial build
