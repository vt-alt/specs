# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg gsl
Name: octave-%octpkg
Version: 2.1.1
Release: alt2
Summary: GNU Scientific Library.

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(gsl) = %version

# octave module BuildRequires: gsl-devel
BuildRequires: libgsl-devel
# Depends: octave (>= 2.9.7)
Requires: octave >= 2.9.7


%description
Octave bindings to the GNU Scientific Library

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc COPYING NEWS AUTHORS DESCRIPTION
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- initial import by package builder

