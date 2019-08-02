Name: ubridge
Version: 0.9.16
Release: alt1

Summary: Bridge for UDP tunnels, Ethernet, TAP and VMnet interfaces
License: GPLv3
Group: Networking/Other
Url: https://github.com/GNS3/ubridge

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc libpcap-devel

%description
uBridge is a simple application to create user-land bridges between various
technologies. Currently bridging between UDP tunnels, Ethernet and TAP
interfaces is supported. Packet capture is also supported.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
cp %name %buildroot%_bindir

%post
setcap cap_net_admin,cap_net_raw=ep %_bindir/%name

%files
%doc LICENSE README.rst
%_bindir/%name

%changelog
* Wed Jul 31 2019 Anton Midyukov <antohami@altlinux.org> 0.9.16-alt1
- new version 0.9.16

* Fri Jun 29 2018 Anton Midyukov <antohami@altlinux.org> 0.9.14-alt1.1
- Rebuilt for aarch64

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 0.9.14-alt1
- new version 0.9.14

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 0.9.13-alt1
- new version 0.9.13

* Thu Feb 23 2017 Anton Midyukov <antohami@altlinux.org> 0.9.11-alt1
- new version 0.9.11

* Sun Dec 11 2016 Anton Midyukov <antohami@altlinux.org> 0.9.8-alt1
- New version 0.9.8

* Mon Aug 08 2016 Anton Midyukov <antohami@altlinux.org> 0.9.4-alt1
- Initial build for ALT Linux Sisyphus.
