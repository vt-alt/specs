# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave /usr/bin/octave-config gcc-fortran makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg optiminterp
Name: octave-%octpkg
Version: 0.3.6
Release: alt1
Summary: optiminterp

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(optiminterp) = %version
# Depends: octave (>= 2.9.9)
Requires: octave >= 2.9.9


%description
An optimal interpolation toolbox for octave. This package provides functions to perform a n-dimensional optimal interpolations of arbitrarily distributed data points.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 0.3.6-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt2
- rebuild with octave 5

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1
- initial import by package builder

