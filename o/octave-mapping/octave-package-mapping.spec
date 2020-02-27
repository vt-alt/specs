# BEGIN SourceDeps(oneline):
BuildRequires: libgdal-devel makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg mapping
Name: octave-%octpkg
Version: 1.4.0
Release: alt1
Summary: Mapping Functions

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
Provides: octave(mapping) = %version
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Simple mapping and GIS .shp and raster file functions.

%prep
%setup -q -n %{octpkg}-%{version}

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
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4
- rebuild with octave 5

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.2.1-alt2
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.0.7-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.7-alt2
- Rebuild with the next version of Octave: 3.8.0

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1
- initial import by octave-package-builder

