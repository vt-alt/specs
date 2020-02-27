# BEGIN SourceDeps(oneline):
BuildRequires: libblas-devel libgomp-devel makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg nan
Name: octave-%octpkg
Version: 3.4.5
Release: alt1
Summary: The NaN-toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://pub.ist.ac.at/~schloegl/matlab/NaN

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(nan) = %version
# Depends: octave (> 3.2.0)
Requires: octave > 3.2.0


%description
A statistics and machine learning toolbox for data with and w/o missing values

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
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.5-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt2
- rebuild with octave 5

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1
- regenerated from template by package builder

* Mon Mar 28 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- new version
- added missing buildrequires

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 2.5.9-alt1
- updated by octave-package-builder

