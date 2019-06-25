# BEGIN SourceDeps(oneline):
BuildRequires: fontconfig-devel libXcursor-devel libXext-devel libXfixes-devel libXft-devel libXinerama-devel libXrender-devel makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg image-acquisition
Name: octave-%octpkg
Version: 0.2.2
Release: alt5
Summary: Image Acquisition

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
Provides: octave(image-acquisition) = %version

# octave module BuildRequires: libv4l-dev (>= 0.8.8), libfltk1.1-dev (>= 1.1.0)
BuildRequires: libv4l-devel >= 0.8.8 libfltk-devel >= 1.1.0
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
The Octave-forge Image Aquisition package provides functions

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
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt5
- rebuild with octave 5

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt4
- fixed build

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 0.2.2-alt2
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- initial import by package builder

