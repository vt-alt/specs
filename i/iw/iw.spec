Name: iw
Version: 5.0.1
Release: alt1

Summary: nl80211 based CLI configuration utility for wireless devices
License: BSD-style
Group: Networking/Other

Url: http://linuxwireless.org/en/users/Documentation/iw

Packager: Evgenii Terechkov <evg@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: libnl-devel

%description
This package contains the `iw' tool which allows you to configure and
show information about wireless networking.
In the future iw will become the canonical command line tool for
wireless configuration and iwconfig/wireless-tools will no longer be
required.

%prep
%setup

%build
export CFLAGS="%optflags"
%make_build V=1

%install
%makeinstall_std V=1

%files
%_sbindir/*
%_man8dir/*
%doc README COPYING

%changelog
* Mon May 20 2019 Alexey Shabalin <shaba@altlinux.org> 5.0.1-alt1
- 5.0.1

* Sun Jul 14 2013 Terechkov Evgenii <evg@altlinux.org> 3.10-alt1
- 3.10

* Sun Feb 17 2013 Terechkov Evgenii <evg@altlinux.org> 3.8-alt2
- Build with libnl3 (thanks to sem@)

* Fri Jan 18 2013 Terechkov Evgenii <evg@altlinux.org> 3.8-alt1
- 3.8

* Mon Sep 10 2012 Terechkov Evgenii <evg@altlinux.org> 3.6-alt1
- 3.6

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.9.20-alt1
- 0.9.20

* Tue Jan 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.19-alt1
- 0.9.19

* Mon Dec 07 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.18-alt1
- initial build

