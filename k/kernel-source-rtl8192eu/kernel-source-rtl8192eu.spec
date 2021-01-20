Name: kernel-source-rtl8192eu
Version: 5.2.19.1
Release: alt5

Summary: Realtek rtl8192eu official Linux driver
License: MIT
Group: Development/Kernel
URL: https://github.com/clnhub/rtl8192eu-linux
Packager: Dmitry Terekhin <jqt4@altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
This driver is based on the (latest) official Realtek v5.2.19.1 driver
with fixes and improvements to support the latest kernels (up to 5.10).

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Thu Dec 17 2020 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt5
- Add support for kernel 5.10(+) *_fs removal
- Improve aarch64 support

* Tue Sep 01 2020 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt4
- Add kernel 5.8(+) support frame management/sha256 offloading
- Provide aarch64 support

* Thu Apr 16 2020 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt3
- Fixed kernel 5.6(+) (mcc) proc_ops support
- Add kernel 5.6(+) proc_ops support
- Disable debug mode
- Fix kernel 5.4(+) date-time compilation errors on older distributions
- Add kernel 5.3(+) .policy support
- Add Mercusys MW300UM support

* Fri Jul 19 2019 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt2
- Add kernel 5.2.0(+) (fallback arg removed) support

* Wed Jul 10 2019 Dmitry Terekhin <jqt4@altlinux.org> 5.2.19.1-alt1
- Initial build
