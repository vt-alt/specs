Name: distro_info
Version: 1.8
Release: alt1

Summary: Get various info about a system and used distro

License: Public domain
Group: System/Configuration/Packaging
Url: https://github.com/Etersoft/distro_info

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/distro_info.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

%description
Get various info about a system and used distro.
Used in Etersoft EPM and rpm-build-altlinux-compat projects.

%prep
%setup

%install
install -m0755 -D bin/distro_info %buildroot%_bindir/distro_info
install -m0644 -D man/distro_info.1 %buildroot%_man1dir/distro_info.1

%files
%doc README.md
%_bindir/distro_info
%_man1dir/*

%changelog
* Wed Jan 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- distro_info: set rolling version for ArchLinux
- distro_info: use /etc/os-release firstly, drop obsoleted code
- distro_info: set pretty name if PRETTY_NAME is empty
- move package manager detection to distro_info (-g option)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- distro_info: add --debian-arch

* Mon Oct 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- distro_info: improve ALT c8 support
- add --distro-arch support (returns distro depended arch name)

* Sun Oct 11 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- distro_info: add -c: print number of available CPU cores
- distro_info: cosmetic improvements

* Wed Oct 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- fix for catching up p9 branches (thanks, iv@)

* Tue Oct 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- distro_info: add support for c8 and c9

* Tue Nov 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- improve virtualization detection
- drop upstart detection
- add --pretty option to print pretty name of the distro

* Thu Nov 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- add -i: print virtualization type
- add -y: print running service manager

* Thu Nov 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
