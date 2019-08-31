# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(Getopt/Long.pm)
# END SourceDeps(oneline)
%define module RPM-Source-Convert

Name: perl-%module
Version: 0.676
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM-Source-Editor perl-RPM-Source-Dependency-Analyzer perl(RPM/Vercmp.pm) perl-DistroMap perl(Source/Package/Comparators/Raw.pm)
Requires: perl-RPM-Source-Editor > 0.9235

# for srpmbackport 
Requires: distromap-altlinux-sisyphus-altlinux-branch
Conflicts: perl-RPM-Source-Editor < 0.73

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
#doc README
%_bindir/srpmbackport
%_bindir/srpmconvert-*
%perl_vendor_privlib/RPM*

%changelog
* Fri Aug 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.676-alt1
- new version

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.675-alt1
- new version

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.674-alt1
- new version

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.673-alt1
- new version

* Fri Mar 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.672-alt1
- new version

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.671-alt1
- new version

* Thu Feb 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.670-alt1
- new version

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.669-alt1
- new version

* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.668-alt1
- new version

* Sat Oct 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.667-alt1
- new version

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.666-alt1
- new version

* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.665-alt1
- new version

* Mon Jun 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.664-alt1
- new version

* Tue May 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.663-alt1
- new version

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.662-alt1
- new version

* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.661-alt1
- new version

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.660-alt1
- new version

* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.659-alt1
- new version

* Thu Mar 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.658-alt1
- new version

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.657-alt1
- new version

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.656-alt1
- new version

* Sun Mar 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.655-alt1
- new version

* Fri Feb 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.654-alt1
- new version

* Mon Jan 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.653-alt1
- new version

* Thu Dec 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.652-alt1
- new version

* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.651-alt1
- new version

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.650-alt1
- new version

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.649-alt1
- bugfix release

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.648-alt1
- new version

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.647-alt1
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.646-alt1
- bugfix release

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.645-alt1
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.644-alt1
- new version

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.643-alt1
- new version

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.642-alt1
- new version

* Sat Oct 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.641-alt1
- new version

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.640-alt1
- new version

* Sun Apr 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.639-alt1
- new version

* Mon Mar 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.638-alt1
- bugfix release

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.637-alt1
- new version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.636-alt1
- new version

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.635-alt1
- new version

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.634-alt1
- new version

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.633-alt1
- new version

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.632-alt1
- new version

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.631-alt1
- new version

* Mon Jan 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.630-alt1
- new version

* Sun Jan 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.629-alt1
- new version

* Wed Jan 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.628-alt1
- new version
