Name: mount-efivars
Version: 0.1
Release: alt1

Summary: Mount /sys/firmware/efi/efivars

License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://altlinux.org

Packager: Anton Midyukov <antohami@altlinux.org>

Source0: %name.init

BuildArch: noarch

%description
%summary

%install
install -pD -m755 %SOURCE0 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name

%changelog
* Sun Mar 14 2021 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
