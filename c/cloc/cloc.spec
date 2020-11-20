Name:           cloc
Version:        1.82
Release:        alt2
Summary:        Count lines of code
License:        GPLv2+
Group: Development/Tools
URL:            https://github.com/AlDanial/cloc
Source0:        https://github.com/AlDanial/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-podlators
# Runtime
BuildRequires: gcc-c++ perl(Encode.pm) swig
BuildRequires:  perl(Algorithm/Diff.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Glob.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Parallel/ForkManager.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Regexp/Common.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Text/Tabs.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(warnings.pm)
# Tests only
BuildRequires:  perl-devel
BuildRequires:  perl-Pod-Checker
BuildRequires:  perl(Test/More.pm)

%description
A tool to count lines of code in various languages from a given directory.

%prep
%setup -q -n %{name}-%{version}/Unix

%build
# Nothing to do but run make anyway, in case anything ever changes
%make_build

%install
make install DESTDIR="%{buildroot}"

%files
%doc --no-dereference COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Nov 17 2020 Andrey Cherepanov <cas@altlinux.org> 1.82-alt2
- Initial build for Sisyphus.

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1_5
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1_4
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1_3
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1_2
- update to new release by fcimport

* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1_1
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_8
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_7
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_6
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_5
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_4
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_3
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1_2
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.66-alt1_2
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1_3
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1_2
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1_6
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1_5
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1_4
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.56-alt2_7
- update to new release by fcimport

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 1.56-alt2_6
- rebuild to get rid of unmets

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1_6
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1_5
- fc import

