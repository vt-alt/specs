Name: perl-RPM-uscan
Version: 0.20.2.18.4
Release: alt1

Summary: Perl library for querying debian watch files
Source0: %name-%version.tar

License: %gpl2plus
Group: Development/Perl
URL: http://www.altlinux.org/Watch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses 
BuildRequires: rpm-build-perl perl-libwww perl-devel perl-LWP-Protocol-https perl(RPM/Vercmp.pm) perl-Dpkg gnupg
Requires: gnupg

%description
RPM::uscan is a perl library for querying debian watch files on RPM platform.

%package -n uscan-query
Summary: a tool for querying debian watch files on RPM platform
Group: Development/Tools
Requires: %name = %version-%release

%description -n uscan-query
uscan-query is a tool for querying debian watch files on RPM platform.

%prep
%setup

%build

%install
mkdir -p %buildroot/%perl_vendorlib/RPM
install -m 644 uscan.pm %buildroot/%perl_vendorlib/RPM/uscan.pm

mkdir -p %buildroot/%_bindir
install -m 755 uscan-query %buildroot/%_bindir/

%files
%perl_vendorlib/R*

%files -n uscan-query
%_bindir/uscan-query

%changelog
* Mon Oct 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.20.2.18.4-alt1
- new version

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.19.2.17.11-alt1
- download bugfixes

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.18.2.17.11-alt1
- new version

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.18.2.17.10-alt1
- watch version=4 support (closes: #33673)

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.12.2.14.4-alt2
- indirect RPM BR: 

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.12.2.14.4-alt1
- use RPM::Vercmp

* Sat Aug 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.11.4.14.4-alt1
- bugfix release

* Sat Aug 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.11.3.14.4-alt1
- bugfix release

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.2.14.4-alt1
- restored tgz unpack support; sync'ed

* Sun Jun 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.2.14.4-alt1
- sync with rpm-uscan 0.15.2.14.4

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.2.14.4-alt1
- sync with rpm-uscan 0.14.2.14.4

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.14.4-alt1
- sync with rpm-uscan 0.11.2.14.4

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.2.14.4-alt1
- debug support
- timeout support
- options override support

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.2.14.4-alt1
- sync with rpm-uscan 0.11.2.14.4

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2.14.4-alt1
- sync with rpm-uscan 0.10.2.14.4

* Sun Jun 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2.14.4-alt1
- renamed to perl-RPM-uscan

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.14.4-alt1
- sync with rpm-uscan 0.8.2.14.4

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.13.3-alt1
- sync with rpm-uscan 0.8.2.13.3

* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.2.11.6-alt1
- improved any-archive

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.6-alt2
- more option checks

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.6-alt1
- sync with rpm-uscan 0.6.2.11.6
- interface 0.3 to return options

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.3-alt1
- sync with rpm-uscan 0.6.2.11.3

* Tue Nov 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.1-alt2
- synced versort with rpm-uscan 0.6.2.11.1 - (closes: 26651)

* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.1-alt1
- sync with rpm-uscan 0.6.2.11.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2.11.1-alt1
- sync with rpm-uscan 0.4.2.11.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2.11.1-alt1
- sync with rpm-uscan 0.3.2.11.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2.11.1-alt1
- sync with rpm-uscan 0.2.2.11.1

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2.11.1-alt1
- sync with uscan 2.11.1

* Mon Oct 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1
- restored copyright notices, bugfixes

* Fri Oct 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- multiple bugfixes

* Mon Dec 10 2007 Avramenko Andrew <liks@altlinux.ru> 0.1-alt1
- First draft

