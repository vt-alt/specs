%define module Logoved-Stream

Name: perl-%module
Version: 0.027
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Stream parser library for rpmbuild -v, hasher, beehive logs.
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/Logoved-Stream.git

BuildRequires: perl-devel perl(Moo.pm) perl(MooX/Singleton.pm) perl(autodie.pm) perl(Source/Shared/CLI.pm)
Requires: perl(MooX/Singleton.pm)

%description
Perl stream parser library for rpmbuild -v, hasher, beehive logs.

%package Listener-Repocop
Summary: Repocop listener for Logoved-Stream beehive log parser.
Group: Development/Perl

%description Listener-Repocop
Repocop listener for Logoved-Stream beehive log parser.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/Logoved*
%exclude %perl_vendor_privlib/Logoved/Stream/Listener/Factory/Repocop*
%exclude %perl_vendor_privlib/Logoved/Role/Stream/Out/Listener/Repocop*
%exclude %perl_vendor_privlib/Logoved/Stream/Out/Listener/Repocop*

# demo
#%_bindir/*
%exclude %_bindir/*
#%exclude %_bindir/*-repocop

%files Listener-Repocop
%_bindir/*-repocop
%perl_vendor_privlib/Logoved/Stream/Listener/Factory/Repocop*
%perl_vendor_privlib/Logoved/Role/Stream/Out/Listener/Repocop*
%perl_vendor_privlib/Logoved/Stream/Out/Listener/Repocop*

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- support for rpm-build-4.0.4-alt163

* Fri May 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- new version

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- new version

* Sat Apr 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- new version

* Wed Apr 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- new version

* Wed Apr 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- new version

* Fri Dec 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- new version

* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- new version

* Fri Apr 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- new version

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- new version

* Mon Jan 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- new version

* Sat Jan 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- new version

* Wed Oct 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- new version

* Fri Oct 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- new version

* Wed Sep 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- manually added Requires: perl(MooX/Singleton.pm)
- TODO: fix problem in perl.req

* Tue Sep 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- new version

* Mon Sep 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- added status of the main stream

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- rpmbuild::write conflict fixed

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- added versioning

* Fri Aug 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- added hasher::timeout section

* Thu Aug 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added hasher::chroot::file_conflict section

* Wed Aug 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- corrections for error status

* Tue Aug 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- added section status

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- added repocop listeners

* Sun Aug 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Wed Aug 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- beehive support

* Mon Aug 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial rpm build

