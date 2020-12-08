Name: blacklist-pcspkr
Version: 0.1
Release: alt1
Summary: Disable PC speacker
License: GPLv2+
Group: System/Kernel and hardware

BuildArch: noarch

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/modprobe.d
echo 'blacklist pcspkr' > %buildroot%_sysconfdir/modprobe.d/blacklist-pcspkr.conf

%files
%_sysconfdir/modprobe.d/blacklist-pcspkr.conf

%changelog
* Thu Sep 19 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT
