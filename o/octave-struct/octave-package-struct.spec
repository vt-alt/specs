# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg struct
Epoch: 1
Name: octave-%octpkg
Version: 1.0.16
Release: alt2
Summary: Structure Handling.

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(struct) = %version
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Additional structure manipulation functions.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION NEWS COPYING
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.16-alt2
- rebuild with octave 5

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.16-alt1
- regenerated from template by package builder

* Mon Feb 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:1.0.15-alt2
- rebuild fixed

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.14-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1:1.0.14-alt2
- regenerated from template by package builder

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.14-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.13-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.12-alt1
- initial import by package builder

