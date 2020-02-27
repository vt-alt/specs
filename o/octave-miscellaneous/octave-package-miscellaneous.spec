# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg miscellaneous
Epoch: 4
Name: octave-%octpkg
Version: 1.3.0
Release: alt1
Summary: Miscellaneous functions

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
Provides: octave(miscellaneous) = %version

# SystemRequirements: units
BuildRequires: units

# octave module BuildRequires: termcap-devel [Debian] libncurses5-dev
BuildRequires: libtinfo-devel libncurses-devel
# Depends: octave (>= 3.6.0), general (>= 1.3.1)
Requires: octave >= 3.6.0 octave(general) >= 1.3.1


%description
Miscellaneous tools that don't fit somewhere else.

%prep
%setup -q -n %{octpkg}-%{version}
# Fix shebang for python script
subst 's,/usr/bin/python,%__python,' inst/physical_constant.py

%build
%octave_build

%install
%octave_install

%files
%doc NEWS COPYING DESCRIPTION
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 4:1.3.0-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4:1.2.1-alt4
- rebuild with octave 5

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 4:1.2.1-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 4:1.2.1-alt2
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 4:1.2.1-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 4:1.2.0-alt5
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:1.2.0-alt4.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 4:1.2.0-alt4
- Rebuild with the next version of Octave: 3.8.0

* Wed Jan 09 2013 Paul Wolneykien <manowar@altlinux.ru> 4:1.2.0-alt3
- updated by octave-package-builder

* Wed Jan 09 2013 Paul Wolneykien <manowar@altlinux.ru> 3:1.2.0-alt2
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt1
- initial import by octave-package-builder

