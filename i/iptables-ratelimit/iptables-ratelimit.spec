Name: iptables-ratelimit
Version: 0.3
Release: alt2
Summary: ipt-ratelimit module implements traffic policing
Group: System/Libraries

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: https://github.com/aabc/ipt-ratelimit
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: iptables-devel
BuildPreReq: rpm-build-kernel

%description
ipt-ratelimit module implements traffic policing (i.e. limiting traffic bit
rate) using, standard for this purpose, token bucket filter (TBF) algorithm.
Particular implementation is based on FreeBSD's implementation of Cisco's TBF
with extended burst value (which is used to implement RED-like drop
behavior)

%package -n kernel-source-%name
Summary: Kernel module for ipt-ratelimit
License: GPLv2
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Provide ipt-ratelimit kernel module


%prep
%setup
%patch0 -p1
tar -cjf ../%name-%version.tar.bz2 ../%name-%version

%build

make libxt_ratelimit.so

%install
make linstall DESTDIR=%buildroot

mkdir -p %kernel_srcdir
install -pDm0644 ../%name-%version.tar.bz2 %kernel_srcdir/%name-%version.tar.bz2

%files
%doc CREDITS NEWS README
/%_lib/iptables/*.so

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Dec 24 2019 Alexei Takaseev <taf@altlinux.org> 0.3-alt2
- Rebuild with new iptables

* Tue May 23 2017 Alexei Takaseev <taf@altlinux.org> 0.3-alt1
- 0.3

* Mon Nov 16 2015 Alexei Takaseev <taf@altlinux.org> 0.2-alt1
- 0.2

* Sun Sep 27 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt2
- fix compilation for kernels > 3.18

* Fri Sep 25 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt1
- Initial RPM release
