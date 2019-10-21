#define module Source-Text-Dependency-Analyser
%define module RPM-Source-Dependency-Analyzer
# useful for testexpect updates
#define _without_test 1

Name: perl-%module
Version: 0.074
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for finding build dependencies from software sources
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

Conflicts: perl-RPM-Source-Editor < 0.909

BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl-Source-Bundle perl-RPM-Source-Editor perl(Pod/Strip.pm)
BuildRequires: perl-DistroMap perl-Marpa-R2


%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# TODO! distrodb!
install -Dm644 stdheaders.txt %buildroot%_datadir/%module/headers-ignore/stdheaders.txt

%files
%doc Changes
%perl_vendor_privlib/R*
%_datadir/%module
%_bindir/buildreq-*
%_man1dir/buildreq-*
%_bindir/sourcedep-resolve
%_man1dir/sourcedep-resolve*

%changelog
* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.074-alt1
- new version

* Wed Apr 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.073-alt1
- new version

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.072-alt1
- new version

* Sun Mar 03 2019 Igor Vlasenko <viy@altlinux.ru> 0.071-alt1
- new version

* Thu Feb 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.070-alt1
- new version

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.069-alt1
- new version

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.068-alt1
- new version

* Fri Feb 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.067-alt1
- new version

* Mon Jan 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.066-alt1
- new version

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.065-alt1
- new version

* Tue May 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.064-alt1
- new version

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.063-alt1
- new version

* Thu Jan 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.062-alt1
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.061-alt1
- stable release

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.060-alt1
- bugfix release

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.059-alt1
- bugfix release

* Mon Feb 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.058-alt1
- development release

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.057-alt1
- development release

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.056-alt1
- development release

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.055-alt1
- development release

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.054-alt1
- development release

* Fri Jan 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.053-alt1
- development release

* Sun Jan 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.052-alt1
- development release

* Wed Jan 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.051-alt1
- new TransformContainer support

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.050-alt1
- bugfix release

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1
- bugfix release

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.048-alt1
- new BR Storage support

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- bugfix release

* Mon Oct 24 2016 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- development release

* Thu Oct 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.045-alt1
- development release

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- python fixes

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1
- python support

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- proper languages in CMake

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- stable release

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- stable release

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- development release

* Sun Apr 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- development release

* Sat Apr 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- development release

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- development release

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- development release

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- development release

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- stable release

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- stable release

* Fri Mar 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- development release

* Thu Mar 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- development release

* Wed Mar 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1
- support for components in cmake

* Wed Mar 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- development release

* Tue Mar 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- stable release

* Wed Mar 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- stable release

* Tue Mar 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- bugfix release

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- stable release

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- stable release

* Sun Mar 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- development release

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- stable release

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- stable release

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- bugfix release

* Tue Mar 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- development release

* Tue Mar 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- development release

* Tue Mar 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- stable release

* Mon Feb 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- stable release

* Sun Feb 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- stable release

* Sat Feb 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- development release

* Fri Feb 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- development release

* Mon Feb 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- development release

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- development release

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- development release

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- bugfix release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- bugfix release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- development release

* Fri Jan 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- development release

* Fri Jan 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- bugfix release

* Wed Dec 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- development release

* Tue Dec 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version

