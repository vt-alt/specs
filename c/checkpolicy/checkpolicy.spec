%define _unpackaged_files_terminate_build 1

Name: checkpolicy
Epoch: 1
Version: 3.1
Release: alt1
Summary: SELinux policy compiler
Group: System/Configuration/Other
License: GPLv2
Url: https://github.com/SELinuxProject/selinux

Source: %name-%version.tar

BuildRequires: flex
BuildRequires: libselinux-devel >= %version
BuildRequires: libsepol-devel >= %version
BuildRequires: libsepol-devel-static >= %version

%description
Security-enhanced Linux is a patch of the Linux(R) kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement(R), Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.
Only required for building policies.

%prep
%setup

%build
%make_build LIBDIR=%_libdir CFLAGS="%optflags"

%install
%makeinstall_std LIBSEPOLA=%_libdir/libsepol.a
for f in dis{mod,pol}; do
	install test/$f %buildroot%_bindir/se$f
done

%find_lang --with-man --all-name %name

%files -f %name.lang
%_bindir/*
%_man8dir/*

%changelog
* Fri Jul 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.1-alt1
- Updated to upstream version 3.1.

* Mon Mar 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0-alt1
- Updated to upstream version 3.0.

* Tue Apr 30 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt2
- Updated man pages translation by Olesya Gerasimenko.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt1
- Updated to upstream version 2.9.

* Mon Dec 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt2
- Added man pages translation by Olesya Gerasimenko.

* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt1
- Updated to upstream version 2.8.

* Mon Feb 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt1
- Updated to upstream version 2.7.

* Thu Oct 27 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt1
- new version

* Thu Sep 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:2.3-alt1
- downgraded due regression (closes: #32254)

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- new version

* Thu Feb 05 2015 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- New version

* Thu Jun 27 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.12-alt1
- New version

* Mon Sep 24 2012 Led <led@altlinux.ru> 2.1.11-alt1
- 2.1.11
- cleaned up spec
- fixed License
- added test utils

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.23-alt1
- Updated to 2.0.23.

* Wed Aug 25 2010 Mikhail Efremov <sem@altlinux.org> 2.0.22-alt1
- 2.0.22
- drop Packager from spec.
- fix Url.
- use %%optflags.

* Thu Mar 04 2010 Mikhail Efremov <sem@altlinux.org> 2.0.21-alt1
- new version

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.19-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.18-alt1
- new version

* Sat Dec 20 2008 Anton Farygin <rider@altlinux.ru> 2.0.16-alt1
- new (development) version
- specfile cleanup

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.34.5-alt1
- Initial build
