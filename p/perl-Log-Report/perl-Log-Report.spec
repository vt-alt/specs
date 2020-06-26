%define _unpackaged_files_terminate_build 1
%define dist Log-Report
Name: perl-%dist
Version: 1.29
Release: alt1

Summary: Report a problem, pluggable handlers and language support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Log-Log4perl perl-PPI perl-Test-Pod perl(Devel/GlobalDestruction.pm) perl-Log-Report-Optional perl(Mojo/Base.pm) perl(DBIx/Class/Storage/Statistics.pm) perl(Dancer/Logger/Abstract.pm) perl(Dancer2/Core/Types.pm)

%description
Handling messages to users can be a hassle, certainly when the same
module is used for command-line and in a graphical interfaces, and
has to cope with internationalization at the same time; this set of
modules tries to simplify this.  Log::Report combines gettext features
with Log::Dispatch-like features.  However, you can also use this
module to do only translations or only message dispatching.

%package Dancer
Group: Development/Perl
Summary: %dist plugin for Dancer

%description Dancer
%dist plugin for Dancer

%package Dancer2
Group: Development/Perl
Summary: %dist plugin for Dancer2

%description Dancer2
%dist plugin for Dancer2

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

# XXX Can't locate object method "new" via package "Log::Report::Dispatcher"
%add_findreq_skiplist */Log/Report/Dispatcher/*

# XXX Can't locate object method "new" via package "Log::Report::Translator::POT"
%add_findreq_skiplist */Log/Report/Translator/*

%add_findreq_skiplist */Dancer2/Plugin/LogReport*

%files
%doc ChangeLog README examples README.md
%perl_vendor_privlib/Log
%perl_vendor_privlib/MojoX/Log

%files Dancer
%perl_vendor_privlib/Dancer/Logger/LogReport.pm
%perl_vendor_privlib/Dancer/Logger/LogReport.pod

%files Dancer2
%perl_vendor_privlib/Dancer2/Logger/LogReport.pm
%perl_vendor_privlib/Dancer2/Logger/LogReport.pod
%perl_vendor_privlib/Dancer2/Plugin/LogReport.pm
%perl_vendor_privlib/Dancer2/Plugin/LogReport.pod
%perl_vendor_privlib/Dancer2/Plugin/LogReport/Message.pm
%perl_vendor_privlib/Dancer2/Plugin/LogReport/Message.pod

%changelog
* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Wed Oct 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.998-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.997-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.996-alt1
- automated CPAN update

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.993-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.92-alt1
- 0.28 -> 0.92

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Thu Jan 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version 0.20 (with rpmrb script)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- initial build for ALT Linux Sisyphus
