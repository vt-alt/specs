# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg image
Name: octave-%octpkg
Version: 2.12.0
Release: alt1
Summary: Image Processing

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
Provides: octave(image) = %version
# Depends: octave (>= 4.2.0)
Requires: octave >= 4.2.0


%description
The Octave-forge Image package provides functions for

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
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.10.0-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.10.0-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.6.2-alt1
- initial import by package builder

