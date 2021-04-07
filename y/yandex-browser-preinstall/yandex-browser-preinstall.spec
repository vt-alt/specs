Name: yandex-browser-preinstall
Version: 0.4
Release: alt4

Summary: Set correct environment for Yandex.Browser
License: GPLv3
Group: Networking/WWW

Url: http://git.altlinux.org/people/nenderus/packages/yandex-browser-preinstall.git
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: yandex-browser
Source1: yandex-browser-beta

Requires: jq

%description
Set correct environment for Yandex.Browser

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_sysconfdir/default/yandex-browser
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/default/yandex-browser-beta

%files
%_sysconfdir/default/yandex-browser
%_sysconfdir/default/yandex-browser-beta

%changelog
* Mon Apr 05 2021 Nazarov Denis <nenderus@altlinux.org> 0.4-alt4
- Add require on jq (ALT #39880)

* Tue Jan 15 2019 Nazarov Denis <nenderus@altlinux.org> 0.4-alt3
- Drop macro ubt (ALT #35904)

* Thu Mar 15 2018 Nazarov Denis <nenderus@altlinux.org> 0.4-alt2
- No arch

* Thu Mar 15 2018 Nazarov Denis <nenderus@altlinux.org> 0.4-alt1
- Temporary remove fix playable video with H.264 codec

* Sat Oct 28 2017 Nazarov Denis <nenderus@altlinux.org> 0.3-alt2
- Fix post-install unowned files

* Sat Oct 28 2017 Nazarov Denis <nenderus@altlinux.org> 0.3-alt1
- Fix playable video with H.264 codec
- Remove require on libgcrypt11 (now use libgcrypt20)

* Sat Jul 02 2016 Nazarov Denis <nenderus@altlinux.org> 0.2-alt1
- Add require on libgcrypt11

* Thu Oct 30 2014 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial release for ALT Linux
