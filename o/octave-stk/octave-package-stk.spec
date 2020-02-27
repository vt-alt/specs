# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg stk
Name: octave-%octpkg
Version: 2.6.1
Release: alt1
Summary: STK: A Small Toolbox for Kriging

Group: Sciences/Mathematics
License: GPLv3+
URL: https://sourceforge.net/projects/kriging/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(stk) = %version
# Depends: octave (>= 3.6.0)
Requires: octave >= 3.6.0


%description
The STK is a (not so) Small Toolbox for Kriging. Its primary

%prep
%setup -q -n %{octpkg}

%build
%octave_build

%install
%octave_install

%files
%doc NEWS ChangeLog COPYING DESCRIPTION doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2.4.2-alt1
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.4-alt1
- initial import by package builder

