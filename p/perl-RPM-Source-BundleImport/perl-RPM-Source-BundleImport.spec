%define module RPM-Source-BundleImport
%define _unpackaged_files_terminate_build 1

Name: perl-%module
Version: 0.075
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: RPM-Source-Editor extension for converting tarballs to SRPMs
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM-Source-Editor perl-Source-Bundle perl-Source-Package perl-RPM-Source-Dependency-Analyzer perl(Pod/PlainText.pm)
Requires: perl-Source-Package > 0.176
Requires: perl-RPM-Source-Editor > 0.9231

%description
%summary

%package Perl
Summary: RPM-Source-BundleImport plugin for Perl source code
Group: Development/Perl
Conflicts: perl-RPM-Source-BundleImport < 0.040
# for evalMakefilePL
BuildRequires: perl(ExtUtils/Depends.pm) perl(YAML/Any.pm)
# Recommends: for meaningful eval
Requires: perl-devel perl(Module/Build.pm) perl(Module/Build/Tiny.pm) perl(ExtUtils/MakeMaker.pm) 
# TODO not implemented
# perl(Module/Install.pm)

%description Perl
RPM-Source-BundleImport plugin for Perl source code

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/RPM*
%exclude %perl_vendor_privlib/RPM/Source/BundleImport/Perl*

%files Perl
%exclude %_bindir/evalMakefilePL.pl
%_bindir/metadump-helper-perl-cpan2rpm
%perl_vendor_privlib/RPM/Source/BundleImport/Perl

%changelog
* Tue Oct 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.075-alt1
- new version

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.074-alt1
- new version

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.073-alt1
- new version

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.072-alt1
- new version

* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.071-alt1
- new version

* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.070-alt1
- new version

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.069-alt1
- new version

* Fri Feb 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.068-alt1
- new version

* Thu Jan 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.067-alt1
- lazy distromap matcher (API change)

* Thu Jan 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.066-alt1
- new version

* Sun Jan 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.065-alt1
- new version

* Fri Jan 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.064-alt1
- new version

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.063-alt1
- new version

* Sat Jan 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.062-alt1
- TeXlive support

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.061-alt1
- stable release

* Sat Oct 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.060-alt1
- development release

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.059-alt1
- development release

* Tue May 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.058-alt1
- development release

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.057-alt1
- development release

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.056-alt1
- development release

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.055-alt1
- development release

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.054-alt1
- development release

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.053-alt1
- development release

* Thu Jan 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.052-alt1
- development release

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.051-alt1
- development release

* Sun Jan 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.050-alt1
- development release

* Sat Jan 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1
- development release

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.048-alt1
- development release

* Wed Jan 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- development release

* Sun Jan 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- development release

* Sun Jan 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.045-alt1
- new version

* Sat Dec 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- stable release

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1
- development release

* Wed Dec 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- development release

* Sat Dec 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- development release

* Thu Oct 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- added perl plugin

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- bugfix release

* Mon Jul 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- development release

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- development release

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- bugfix release

* Mon May 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- development release

* Thu Apr 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- development release

* Sat Apr 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- development release

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- development release

* Mon Apr 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- development release

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- development release

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1
- development release

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- development release

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- development release

* Wed Feb 24 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- bugfix release

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- development release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- development release

* Sun Feb 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- development release

* Thu Oct 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- development release

* Tue May 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- development release

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- development release

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- bugfix release

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- development release

* Tue Apr 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- bugfix release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- development release

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- development release

* Fri Oct 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- bugfix release

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- development release

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- development release

* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- development release

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- development release

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- development release

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- development release

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- development release

* Wed Aug 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- development release

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- development release

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- development release

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- development release

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial release
