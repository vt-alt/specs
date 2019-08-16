%define prefix /
%define exec_prefix /
%define _prefix /
%define soname 13
Name: ipset
Version: 7.3
Release: alt1

Summary: Tools for managing sets of IP or ports with iptables
License: GPLv2
Group: System/Kernel and hardware
Url: http://ipset.netfilter.org/

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildRequires: libmnl-devel

%description
IP sets are a framework inside the Linux kernel, which can be administered by 
the ipset utility. Depending on the type, currently an IP set may store IP addresses,
(TCP/UDP) port numbers or IP addresses with MAC addresses in a way,
which ensures lightning speed when matching an entry against a set.

ipset may be the proper tool for you, if you want to
 * store multiple IP addresses or port numbers and match against the
   collection by iptables at one swoop;
 * dynamically update iptables rules against IP addresses or ports
   without performance penalty;
 * express complex IP address and ports based rulesets with one single
   iptables rule and benefit from the speed of IP sets

%package -n lib%{name}%{soname}
Summary: Dynamic library for %name
License: LGPLv2+
Group: Development/C

%description -n lib%{name}%{soname}
The lib%{name}%{soname} package contains the dynamic libraries needed for 
applications to use the %name framework.

%package -n lib%{name}-devel
Summary: Header files for lin%name
License: LGPLv2+
Group: Development/C
Requires: lib%{name}%{soname} = %version-%release

%description -n lib%{name}-devel
The lib%{name}6 package contains the header files needed for
developing applications that need to use the %name framework libraries.


%package -n kernel-source-ipset
Summary: Linux ipset modules sources
License: GPLv2+
Group: Development/Kernel
BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description -n kernel-source-ipset
Kernel source modules ipset.

%prep
%setup -q
%patch0 -p1
autoreconf -fisv

%build
%configure --without-kbuild --without-ksource
%make_build LIBDIR=/%_lib/ BINDIR=/sbin/
%install
%makeinstall prefix=%buildroot/ exec_prefix=%buildroot/ sbindir=%buildroot/sbin libdir=%buildroot/%_lib pkgconfigdir=%buildroot/%_pkgconfigdir
mkdir -p $RPM_BUILD_ROOT/%_libdir

pushd $RPM_BUILD_ROOT/%_libdir
LIBNAME=`basename \`ls $RPM_BUILD_ROOT/%{_lib}/libipset.so.%{soname}.*.*\``
ln -s ../../%{_lib}/$LIBNAME libipset.so
popd


tar xvf %SOURCE0
mv %name-%version kernel-source-%name-%version

mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%name-%version.tar.bz2 kernel-source-%name-%version

%files
%doc ChangeLog ChangeLog.ippool README
/sbin/*
%_man8dir/*

%files -n lib%{name}%{soname}
%attr(755,root,root) /%{_lib}/libipset.so.%{soname}*

%files -n lib%{name}-devel
%_includedir/lib%name/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n kernel-source-ipset
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar.bz2

%changelog
* Thu Aug 08 2019 Anton Farygin <rider@altlinux.ru> 7.3-alt1
- 7.3

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 7.1-alt1
- 7.1

* Tue Nov 13 2018 Anton Farygin <rider@altlinux.ru> 7.0-alt1
- 7.0

* Tue May 22 2018 Anton Farygin <rider@altlinux.ru> 6.38-alt1
- 6.38

* Tue Jan 23 2018 Anton Farygin <rider@altlinux.ru> 6.35-alt1
- new version

* Mon Mar 13 2017 Anton Farygin <rider@altlinux.ru> 6.32-alt1
- new version

* Mon Mar 13 2017 Anton Farygin <rider@altlinux.ru> 6.32-alt1
- new version

* Thu Nov 24 2016 Anton Farygin <rider@altlinux.ru> 6.30-alt1
- new version

* Sun Oct 02 2016 Anton Farygin <rider@altlinux.ru> 6.29-alt3.git.caaa86
- add pkgconfig files (closes: #32543)
- devel package renamed

* Tue Jul 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.29-alt2.git.caaa86
- updated for kernel 4.7 support

* Tue Jun 28 2016 Anton Farygin <rider@altlinux.ru> 6.29-alt1
- new version

* Tue Sep 29 2015 Anton Farygin <rider@altlinux.ru> 6.26-alt1
- new version

* Wed Feb 11 2015 Anton Farygin <rider@altlinux.ru> 6.24-alt1
- new version

* Wed Sep 24 2014 Anton Farygin <rider@altlinux.ru> 6.23-alt1
- new version

* Mon Mar 24 2014 Anton Farygin <rider@altlinux.ru> 6.21.1-alt1
- new version

* Fri Nov 15 2013 Anton Farygin <rider@altlinux.ru> 6.20.1-alt3
- repack kernel-source-package for new ipset modules build scheme

* Wed Nov 13 2013 Anton Farygin <rider@altlinux.ru> 6.20.1-alt2
- fixed buildrequires

* Tue Nov 05 2013 Anton Farygin <rider@altlinux.ru> 6.20.1-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 6.19-alt1
- new version

* Wed Jun 06 2012 Anton Farygin <rider@altlinux.ru> 6.12.1-alt1
- new version

* Mon Sep 19 2011 Anton Farygin <rider@altlinux.ru> 6.9.1-alt2
- revert back kernel-source-ipset

* Mon Sep 19 2011 Anton Farygin <rider@altlinux.ru> 6.9.1-alt1
- new version

* Tue Aug 02 2011 Anton Farygin <rider@altlinux.ru> 6.8-alt1
- new version

* Mon Apr 18 2011 Anton Farygin <rider@altlinux.ru> 4.5-alt1
- new version

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new version
- build kernel-source from this package

* Fri Mar 12 2010 Igor Zubkov <icesik@altlinux.org> 4.1-alt2
- move binaries from /usr/sbin/ to /sbin/ and
  libraries from /usr/lib/ to /lib/

* Wed Dec 23 2009 Igor Zubkov <icesik@altlinux.org> 4.1-alt1
- 3.2 -> 4.1

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 3.2-alt1
- 2.4.5 -> 3.2

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 2.4.5-alt1
- 2.4.4 -> 2.4.5

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.4.4-alt1
- 2.4.3 -> 2.4.4

* Sun Oct 26 2008 Igor Zubkov <icesik@altlinux.org> 2.4.3-alt1
- 2.3.0 -> 2.4.3

* Wed Jul 09 2008 Igor Zubkov <icesik@altlinux.org> 2.3.0-alt1
- 2.2.9 -> 2.3.0
- update and cleanup kernel headers in package

* Thu Jun 28 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 2.2.9-alt1
- rebuild for ALTLinux.
- fix link problem (tnx to ldv@ for simular fix in iptables).

* Fri Aug  4 2006 Samir Bellabes <sbellabes@n4.mandriva.com> 2.2.9-1mdv2007.0
- new release.
- use mkrel tag
- include kernel headers in the package.

* Wed Aug 31 2005 Couriousous <couriousous@mandriva.org> 2.2.2-4mdk
- Fix plugin loading on x86_64

* Wed Aug 10 2005 Samir Bellabes <sbellabes@mandriva.com> 2.2.2-3mdk
- Fix missing PREFIX

* Tue Aug  2 2005 Olivier Blin <oblin@mandriva.com> 2.2.2-2mdk
- fix libdir on x86_64

* Fri Jul 29 2005 Samir Bellabes <sbellabes@mandriva.com> 2.2.2-1mdk
- first release
