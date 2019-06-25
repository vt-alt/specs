# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg interval
Name: octave-%octpkg
Version: 3.2.0
Release: alt2
Summary: Real-valued interval arithmetic

Group: Sciences/Mathematics
License: GPL-3.0+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(interval) = %version

# SystemRequirements: mpfr (>= 3.1.0) [Debian] libmpfr4 (>= 3.1.0)
BuildRequires: libmpfr-devel >= 3.1.0

# octave module BuildRequires: mpfr (>= 3.1.0) [Debian] libmpfr-dev (>= 3.1.0)
BuildRequires: libmpfr-devel >= 3.1.0 libmpfr-devel >= 3.1.0
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
The interval package for real-valued interval arithmetic allows

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2
- rebuild with octave 5

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2.1.0-alt1
- regenerated from template by package builder

* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- initial import by package builder

