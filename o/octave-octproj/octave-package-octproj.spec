# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg octproj
Name: octave-%octpkg
Version: 1.1.5
Release: alt5
Summary: GNU Octave bindings to PROJ.4

Group: Sciences/Mathematics
License: GPLv3+
URL: http://trac.osgeo.org/proj/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(octproj) = %version

# SystemRequirements: libproj-dev (>= 4.5.0) (Debian system)
BuildRequires: libproj-devel >= 4.5.0
# Depends: Octave (>= 2.9.7)
Requires: octave >= 2.9.7


%description
This package allows to call functions of PROJ.4 library for

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
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt5
- rebuild with octave 5

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.1.5-alt4
- rebuild with libproj 5.2.2

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.1.5-alt2
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1
- initial import by package builder

