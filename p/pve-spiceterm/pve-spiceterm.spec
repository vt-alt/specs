%define sname spiceterm
%define pname %sname-pve

Name: pve-%sname
Summary: SPICE Terminal Emulator
Version: 3.1.1
Release: alt4
License: GPLv2
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64

Source0: %sname.tar.xz
Patch0: spiceterm-keymaps.patch

BuildRequires: glib2-devel libspice-server-devel perl-podlators

%description
With spiceterm you can start commands and export its standard input and
output to any SPICE client (simulating a xterm Terminal).

%prep
%setup -q -n %sname
%patch0 -p1 -b .kvm

sed -i 's|\ -Werror||' src/Makefile

%build
%make -C src

%install
%make -C src VERSION=%version DESTDIR=%buildroot install

%files
%_bindir/%sname
%_man1dir/%sname.1*

%changelog
* Mon Jan 18 2021 Valery Inozemtsev <shrek@altlinux.ru> 3.1.1-alt4
- fixed keymaps path (closes: #39553)

* Sun Mar 22 2020 Valery Inozemtsev <shrek@altlinux.ru> 3.1.1-alt3
- fixed build

* Wed Aug 28 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.1.1-alt2
- rebuild with system library

* Mon Aug 05 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.1.1-alt1
- 3.1-1

* Wed Nov 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.5-alt1
- 3.0-5

* Tue Nov 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.4-alt1.2
- rebuild

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.0.4-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 3.0.4-alt1
- 3.0-4

* Tue Jun 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt2
- fixed keymaps path

* Mon Mar 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- initial release

