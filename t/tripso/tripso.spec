Name: tripso
Version: 1.1
Release: alt1

Summary: Translation of IPv4 Security Options (IPSO) Labels
License: GPLv2
Group: System/Kernel and hardware
Requires: iptables

Url: https://github.com/vt-alt/tripso
Source0: %name-%version.tar

BuildPreReq: rpm-build-kernel
BuildPreReq: kernel-headers-modules-std-def
BuildRequires: libiptables-devel

%description
Translate between CISPO and Astra Linux security labels (userspace part).

%package -n kernel-source-%name
Summary: Translate between CISPO and Astra Linux security labels (source)
Group: Development/Kernel
BuildArch: noarch
%description -n kernel-source-%name
Translate between CISPO and Astra Linux security labels (source).

%prep
%setup -q

%build
make libxt_TRIPSO.so VERSION=%version CFLAGS="%optflags"

%install
make install-lib DESTDIR=%buildroot
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar

%check
# do dummy build of the module
make KDIR=$(echo /lib/modules/*/build) VERSION=%version xt_TRIPSO.ko

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md
/%_lib/iptables/*.so

%changelog
* Wed Feb 05 2020 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Compatibility drop v3.19, add v5.3.

* Tue Oct 01 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt3
- Fix build of kernel module.

* Mon Sep 30 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt2
- Fix debuginfo which did not contain source code
- Build with system CFLAGS

* Tue Mar 06 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1
- Sisyphus package.
