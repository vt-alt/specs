Name: spice-protocol
Version: 0.14.3
Release: alt1
Epoch: 1
Summary: Spice protocol header files
Group: Development/C
License: BSD
Url: http://www.spice-space.org/

# VCS-git: https://gitlab.freedesktop.org/spice/spice-protocol.git
Source: %name-%version.tar
#Patch: %name-%version.patch

BuildArch: noarch
BuildRequires(pre): meson

%description
Header files describing the spice protocol and the para-virtual graphics card QXL.

%prep
%setup
#%%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING README.md CHANGELOG.md
%_includedir/*
%_datadir/pkgconfig/*.pc

%changelog
* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.14.3-alt1
- new version 0.14.3

* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.14.2-alt1
- new version 0.14.2

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.14.1-alt1
- new version 0.14.1

* Fri May 31 2019 Alexey Shabalin <shaba@altlinux.org> 1:0.14.0-alt1
- 0.14.0

* Tue Apr 23 2019 Alexey Shabalin <shaba@altlinux.org> 1:0.12.15-alt2
- downgrade to 0.12.15

* Tue Apr 16 2019 Alexey Shabalin <shaba@altlinux.org> 0.14.0-alt1
- 0.14.0

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 0.12.15-alt1
- 0.12.15

* Mon Jul 09 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.14-alt1
- 0.12.4

* Mon Sep 04 2017 Alexey Shabalin <shaba@altlinux.ru> 0.12.13-alt1
- 0.12.13

* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.12.12-alt1
- 0.12.12

* Tue May 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.12.11-alt1
- 0.12.11

* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.12.10-alt1
- 0.12.10

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.12.8-alt1
- 0.12.8

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt2
- upstream git snapshot fb50e86680083edff3bce7789f97b62d86d7e9a4

* Wed May 21 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt1
- 0.12.7

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12.6-alt2.git58c1b4
- upstream git snapshot 58c1b4aeb85167c44fea0813771d1c33c9acacb7

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.6-alt1
- 0.12.6

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt2
- git snapshot 4f868cc354b617f55a0983fd2b2eafcb223b5772

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt1
- 0.12.5

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Nov 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue May 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt2
- upstream/0.8 snapshot with fixes from upstream/master

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sat Nov 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
