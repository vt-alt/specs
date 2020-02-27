# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg econometrics
Name: octave-%octpkg
Version: 1.1.2
Release: alt1
Summary: Econometrics.

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
Provides: octave(econometrics) = %version
# Depends: octave (>= 2.9.7), optim
Requires: octave >= 2.9.7 octave(optim)


%description
Econometrics functions including MLE and GMM based techniques.

%prep
%setup -q -n %{octpkg}

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
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt6
- rebuild with octave 5

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt5
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.1.1-alt4
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3
- regenerated from template by package builder

* Wed Jan 15 2014 Cronport Service <cronport@altlinux.org> 1.1.1-alt1.M70T.1
- backport

* Wed Oct 16 2013 Cronport Service <cronport@altlinux.org> 1.1.1-alt0.M70T.1
- backport

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- initial import by octave-package-builder

