%def_disable snapshot
Name: mobile-broadband-provider-info
Version: 20190618
Release: alt1

Summary: Mobile Broadband Service Provider Database
Group: System/Configuration/Networking
License: Creative Commons Public Domain
Url: https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

# for check
BuildRequires: xmllint xsltproc

%description
This package contains listings of mobile broadband (3G) providers and
associated network and plan information.

%prep
%setup
# subst date as version for git snapshot
%{?_enable_snapshot:sed -i -e 's|, [0-9]*,|, %version,|' configure.ac}

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_datadir/%name/
%_datadir/pkgconfig/*
%doc COPYING README

%changelog
* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 20190618-alt1
- 20190618

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 20190116-alt1
- 20190116

* Fri Mar 10 2017 Yuri N. Sedunov <aris@altlinux.org> 20170310-alt1
- updated to 20170310 ftp release

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 20151214-alt1
- updated to 20151214 ftp release

* Tue Aug 11 2015 Yuri N. Sedunov <aris@altlinux.org> 20150608-alt1
- uptaed to git snapshot (4c6b2437b71)

* Thu Jun 14 2012 Yuri N. Sedunov <aris@altlinux.org> 20120614-alt1
- updated to 20120614 ftp release

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 20110511-alt1
- updated to 20110511 ftp release

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 20110218-alt1
- updated to 20110218 ftp release

* Mon May 10 2010 Yuri N. Sedunov <aris@altlinux.org> 20100510-alt1
- updated to 20100510 ftp release

* Sat Jan 23 2010 Yuri N. Sedunov <aris@altlinux.org> 20100122-alt1
- updated to 20100122 ftp release

* Sat Sep 19 2009 Yuri N. Sedunov <aris@altlinux.org> 20090918-alt1
- updated to 20090918 ftp release

* Tue Jul 07 2009 Yuri N. Sedunov <aris@altlinux.org> 20090707-alt1
- updated to 20090707 ftp release
- changed source url

* Tue Apr 21 2009 Yuri N. Sedunov <aris@altlinux.org> 20090309-alt1
- updated to current rev. 95 (ALT#19711)

* Thu Sep 04 2008 Yuri N. Sedunov <aris@altlinux.org> 20080822-alt1.1
- move *.pc to %%_datadir/pkgconfig

* Thu Sep 04 2008 Yuri N. Sedunov <aris@altlinux.org> 20080822-alt1
- first build for Sisyphus.
