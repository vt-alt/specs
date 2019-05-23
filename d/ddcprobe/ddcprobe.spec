Name: 	ddcprobe
Version: 3.0
Release: alt1.qa2
Summary: Tool for reading EDID from DDC
Summary(ru_RU.UTF-8): Утилита для чтения EDID из DDC
License: LGPL
Group: System/Configuration/Hardware

ExclusiveArch: %ix86 x86_64
Conflicts: xresprobe
BuildRequires: libx86-devel
Requires: libx86

Source: %name-%version.tar

%description
ddcprobe is a tool for reading and parsing EDID from DDC.

%prep
%setup -q

%define _optlevel s

%build
%make_build EXTRA_CFLAGS="%optflags"

%install
%makeinstall DESTDIR=%buildroot LIBDIR=%_libdir

%files
%_sbindir/*

%changelog
* Thu May 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0-alt1.qa2
- Added ExclusiveArch: %%ix86 x86_64.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Sep 17 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.0-alt1
- rewrite code (closes: #21481, #21482, #21483)
- use libx86
- remove libvbe library

* Wed Nov 26 2008 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- fixed build on x86_64

* Wed Nov 26 2008 Anton Farygin <rider@altlinux.ru> 2.0.4-alt1
- fixed build for Sisyphus (processor flags changed for new glibc-kernheaders)

* Wed Nov 26 2008 Anton Farygin <rider@altlinux.ru> 2.0.3-alt2
- libvbe description fixed (#9779)

* Fri May 12 2006 Anton Farygin <rider@altlinux.ru> 2.0.3-alt1
- -Werror added
- fixed build with gcc-4.1

* Mon Apr 03 2006 Anton Farygin <rider@altlinux.ru> 2.0.2-alt1
- fixed build with new binutils

* Fri Feb 10 2006 Kachalov Anton <mouse@altlinux.ru> 2.0.1-alt1
- do VBIOS chksum
- disable LRMI code due segfault (#8192)
- print modeline for dtiming
- group modes by depth in output

* Fri Jul 01 2005 Kachalov Anton <mouse@altlinux.ru> 2.0-alt1
- so-name change: vbe_info struct fix (introduced memory leak :)
- VBIOS chksum skip

* Tue Jun 28 2005 Anton D. Kachalov <mouse@altlinux.org> 1.0-alt1
- merged with latest monitor-edid from MDK

* Wed Jun 08 2005 Anton Farygin <rider@altlinux.ru> 0.1.1-alt2
- added conflicts witch xresprobe

* Tue May 24 2005 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- removed error messages from libvbe

* Tue May 03 2005 Anton Farygin <rider@altlinux.ru> 0.1-alt1
- first build for Sisyphus

