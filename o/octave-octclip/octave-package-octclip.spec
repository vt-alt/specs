# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg octclip
Name: octave-%octpkg
Version: 1.0.8
Release: alt4
Summary: GNU Octave clipping polygons tool

Group: Sciences/Mathematics
License: GPLv3+, modified BSD
URL: http://davis.wpi.edu/~matt/courses/clipping/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(octclip) = %version
# Depends: Octave (>= 2.9.7)
Requires: octave >= 2.9.7


%description
This package allows to do boolean operations with polygons using

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
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt4
- rebuild with octave 5

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.0.8-alt2
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.0.3-alt3
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.3-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- initial import by octave-package-builder

