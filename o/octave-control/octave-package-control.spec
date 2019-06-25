# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg control
Epoch: 1
Name: octave-%octpkg
Version: 3.2.0
Release: alt2
Summary: Computer-Aided Control System Design

Group: Sciences/Mathematics
License: GPLv3+
URL: http://www.slicot.org

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(control) = %version
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Computer-Aided Control System Design (CACSD) Tools for GNU Octave, based on the proven SLICOT Library

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc COPYING NEWS DESCRIPTION doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.2.0-alt2
- rebuild with octave 5

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.2.0-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.1.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1:3.0.0-alt2
- regenerated from template by package builder

* Sun Mar 27 2016 Anton Midyukov <antohami@altlinux.org> 1:3.0.0-alt1
- New version
- Added missing buildrequires.

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.6.5-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.6.5-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.6.1-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.4.5-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:2.4.5-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:2.4.1-alt1
- updated by octave-package-builder

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Built with OpenBLAS instead of GotoBLAS2

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1
- initial import by octave-package-builder

