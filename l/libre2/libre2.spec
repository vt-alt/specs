%define oldname re2
Name: libre2
Version: 20200706
Release: alt1
Summary: C++ fast alternative to backtracking RE engines
Group: System/Libraries
License: BSD
Url: http://github.com/google/re2/
# repack from git
Source0: %name-%version.tar
BuildRequires: gcc-c++
Provides: re2 = %EVR

%description
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g back references and generalized assertions).

%package devel
Summary: C++ header files and library symbolic links for re2
Group: Development/Other
Requires: %name = %EVR
Provides: re2-devel = %EVR

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for %oldname. If you would like to develop programs using %oldname,
you will need to install %name-devel.

%prep
%setup

%build
%make_build  CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" includedir=%_includedir libdir=%_libdir

%install
%makeinstall_std includedir=%_includedir libdir=%_libdir 

# Suppress the static library
find %buildroot -name '%name.a' -delete

%check
make shared-test

%files
%doc LICENSE
%doc AUTHORS CONTRIBUTORS README
%_libdir/%name.so.*

%files devel
%_includedir/%oldname
%_libdir/%name.so
%_libdir/pkgconfig/%oldname.pc

%changelog
* Thu Jul 16 2020 Anton Farygin <rider@altlinux.ru> 20200706-alt1
- new version

* Fri Jun 05 2020 Anton Farygin <rider@altlinux.ru> 20200601-alt1
- new version

* Wed Apr 01 2020 Anton Farygin <rider@altlinux.ru> 20200401-alt1
- new version

* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 20200101-alt1
- new version

* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 20191201-alt1
- 20191201

* Wed Nov 13 2019 Anton Farygin <rider@altlinux.ru> 20191101-alt1
- 20191101

* Wed Sep 18 2019 Anton Farygin <rider@altlinux.ru> 20190901-alt1
- 20190901

* Fri Aug 09 2019 Anton Farygin <rider@altlinux.ru> 20190801-alt1
- updated to 20190801

* Wed Jun 26 2019 Anton Farygin <rider@altlinux.ru> 20190601-alt1
- updated to 20190601
- cleanup specfile

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_3
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_5
- update to new release by fcimport

* Sun Dec 21 2014 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_3
- new version

