# BEGIN SourceDeps(oneline):
BuildRequires: libportaudio2-devel makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg ltfat
Name: octave-%octpkg
Version: 2.3.1
Release: alt2
Summary: The Large Time-Frequency Analysis Toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://ltfat.github.io/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(ltfat) = %version

# octave module BuildRequires: fftw3 [Debian] libfftw3-3, lapack [Debian] liblapack3,
BuildRequires: libfftw3-devel liblapack-devel
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
The Large Time/Frequency Analysis Toolbox (LTFAT) is a

%prep
%setup -q -n %{octpkg}

%build
%octave_build

%install
%octave_install

%files
%doc COPYING DESCRIPTION NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2.2.0-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1
- initial import by package builder

