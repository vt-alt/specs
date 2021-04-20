Name: make-initrd-busybox
Version: 1.32.1
Release: alt3

Summary: Busybox for make-initrd
License: GPL-2.0-or-later
Group: System/Base

Source0: %name-%version.tar

BuildRequires: libtirpc-devel

%description
Busybox (%version) for make-initrd.

%prep
%setup

%build
sed -r \
	-e 's#@includedir@#%{_includedir}#g' \
	busybox-config > busybox/.config
cd busybox
%make_build

%install
mkdir -p -- %buildroot/lib/initrd/var/run

cd busybox
%make install CONFIG_PREFIX=%buildroot/lib/initrd

%files
/lib/initrd/*

%changelog
* Tue Mar 30 2021 Alexey Gladkov <legion@altlinux.ru> 1.32.1-alt3
- Add start-stop-daemon.

* Mon Jan 11 2021 Alexey Gladkov <legion@altlinux.ru> 1.32.1-alt2
- Fix build under srpm_cleanup (mike@).

* Sat Jan 02 2021 Alexey Gladkov <legion@altlinux.ru> 1.32.1-alt1
- New busybox version (1.32.1).
- Update License tag.

* Wed Apr 17 2019 Alexey Gladkov <legion@altlinux.ru> 1.28.1-alt2
- Add switch_root.

* Mon Mar 26 2018 Alexey Gladkov <legion@altlinux.ru> 1.28.1-alt1
- New busybox version (1.28.1).

* Thu Mar 16 2017 Alexey Gladkov <legion@altlinux.ru> 1.24.2-alt2
- Add setsid, timeout utilities.

* Tue May 03 2016 Alexey Gladkov <legion@altlinux.ru> 1.24.2-alt1
- New busybox version (1.24.2).

* Wed Nov 18 2015 Alexey Gladkov <legion@altlinux.ru> 1.24.1-alt1
- New busybox version (1.24.1).

* Fri Jul 04 2014 Alexey Gladkov <legion@altlinux.ru> 0.2-alt1
- Add more utilities.

* Wed Mar 13 2013 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial.

