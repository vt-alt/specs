# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg zeromq
Name: octave-%octpkg
Version: 1.5.0
Release: alt1
Summary: ZeroMQ Toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sourceforge.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(zeromq) = %version

# SystemRequirements: zmq
BuildRequires: libzeromq-devel
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
ZeroMQ bindings for GNU Octave

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
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- rebuild with octave 5

* Fri Apr 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.2.1-alt2
- regenerated from template by package builder

* Fri Jan 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.1
- rebuild

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- initial import by package builder

