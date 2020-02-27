# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg io
Epoch: 1
Name: octave-%octpkg
Version: 2.4.13
Release: alt1
Summary: Input/Output

Group: Sciences/Mathematics
License: GPLv3+, simplified BSD
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(io) = %version
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Input/Output in external formats.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION NEWS COPYING doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.4.13-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.4.12-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.4.12-alt1
- regenerated from template by package builder

* Mon May 21 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.4.11-alt1
- New version.

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.4.7-alt1
- regenerated from template by package builder

* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.5-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.3-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:2.2.2-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.2.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.2.2-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.0.2-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.3-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1
- initial import by octave-package-builder

