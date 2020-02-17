Name: distro_info
Version: 1.2
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
* Tue Nov 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- improve virtualization detection
- drop upstart detection
- add --pretty option to print pretty name of the distro

* Thu Nov 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- add -i: print virtualization type
- add -y: print running service manager

* Thu Nov 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
