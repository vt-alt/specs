# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg signal
Epoch: 2
Name: octave-%octpkg
Version: 1.4.1
Release: alt2
Summary: Signal Processing

Group: Sciences/Mathematics
License: GPLv3+, public domain
URL: https://octave.sourceforge.io/signal/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(signal) = %version
# Depends: octave (>= 3.8), control (>= 2.4)
Requires: octave >= 3.8 octave(control) >= 2.4


%description
Signal processing tools, including filtering, windowing and display functions.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc NEWS DESCRIPTION COPYING
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2:1.4.1-alt2
- rebuild with octave 5

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 2:1.4.1-alt1
- regenerated from template by package builder

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 2:1.4.0-alt1
- regenerated from template by package builder

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2:1.3.2-alt2
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.3.2-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 2:1.3.0-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:1.3.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 2:1.3.0-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.2-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1
- initial import by octave-package-builder

