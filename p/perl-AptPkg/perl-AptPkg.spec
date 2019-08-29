# if debug isn't enabled, %%perl_vendor_build ignores %%optflags
%def_enable debug

Name: perl-AptPkg
Version: 0.1.26
Release: alt5

Summary: Perl interface to libapt-pkg
License: GPLv2+
Group: Development/Perl

URL: http://packages.debian.org/unstable/perl/libapt-pkg-perl
Source: libapt-pkg-perl-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Wed Oct 12 2011
BuildRequires: apt gcc-c++ libapt-devel perl-devel

%description
A Perl interface to APT's libapt-pkg which provides modules
for configuration file/command line parsing, version comparison,
inspection of the binary package cache and source package details.

%prep
%setup -n libapt-pkg-perl-%version
%patch -p1
cp -a /etc/apt/* t/cache/etc/

%build
%ifarch %e2k
%add_optflags -std=c++14
%endif
%perl_vendor_build INC=-I%_includedir/rpm ||:

%install
%perl_vendor_install

%files
%doc	README debian/changelog examples
	%perl_vendor_archlib/AptPkg.pm
%dir	%perl_vendor_archlib/AptPkg
	%perl_vendor_archlib/AptPkg/*.pm
%doc	%perl_vendor_archlib/AptPkg/*.pod
%dir	%perl_vendor_autolib/AptPkg
	%perl_vendor_autolib/AptPkg/AptPkg.so

%changelog
* Thu Jul 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.26-alt5
- Rebuilt with new Apt

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.26-alt4.qa1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.26-alt4.qa1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.26-alt4.qa1.1
- rebuild with new perl 5.24.1

* Tue Nov 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.26-alt4.qa1
- Rebuilt with libapt-pkg-libc6.9-6.so.6.

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.26-alt3.1.1.1.1
- rebuild with new perl 5.22.0

* Thu May 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.26-alt3.1.1.1
- Rebuilt for:
 + libapt-pkg-libc6.9-6.so.5.
 + gcc5 C++11 ABI.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.26-alt3.1.1
- rebuild with new perl 5.20.1

* Wed Sep 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.26-alt3.1
- Rebuilt with libapt-pkg-libc6.9-6.so.4.

* Tue Mar 11 2014 Dmitry V. Levin <ldv@altlinux.org> 0.1.26-alt3
- Rebuilt.

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.1.26-alt2
- built for perl 5.18

* Fri Jan 11 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1.26-alt1
- 0.1.25 -> 0.1.26

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.1.25-alt2
- rebuilt for perl-5.16

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 0.1.25-alt1
- 0.1.24 -> 0.1.25
- built for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.1.24-alt1.1.1
- rebuilt with perl 5.12

* Mon Dec 21 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1.24-alt1.1
- NMU:
  + rebuilt with apt 0.5.15lorg2-alt31.1
  + AptPkg::PkgRecords::lookup(): also return raw changelog text

* Fri Nov 27 2009 Alexey Tourbin <at@altlinux.ru> 0.1.24-alt1
- 0.1.22 -> 0.1.24

* Sat Aug 30 2008 Alexey Tourbin <at@altlinux.ru> 0.1.22-alt1
- 0.1.20 -> 0.1.22

* Sat Jan 06 2007 Alexey Tourbin <at@altlinux.ru> 0.1.20-alt2
- rebuilt with new libapt-pkg/glibc

* Sat Jun 17 2006 Alexey Tourbin <at@altlinux.ru> 0.1.20-alt1
- 0.1.12 -> 0.1.20

* Tue Aug 10 2004 Alexey Tourbin <at@altlinux.ru> 0.1.12-alt1
- initial revision
- fc-rpm.patch: fix build
- license: GPL
