# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg database
Name: octave-%octpkg
Version: 2.4.4
Release: alt1
Summary: Database.

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz
Patch: database-2.4.3-octave5.patch

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(database) = %version

# octave module BuildRequires: Postgresql (>= 8.3)
BuildRequires: postgresql-devel >= 8.3
# Depends: octave (>= 3.6.2), struct (>= 1.0.12)
Requires: octave >= 3.6.2 octave(struct) >= 1.0.12


%description
Interface to SQL databases, currently only postgresql using libpq.

%prep
%setup -q -n %{octpkg}-%{version}
%patch -p1

%build
%octave_build

%install
%octave_install

%files
%doc COPYING DESCRIPTION NEWS doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 2.4.4-alt1
- New version.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.4.3-alt3
- rebuild with octave 5

* Fri Apr 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.4.3-alt2
- fixed build

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.3-alt1
- initial import by package builder

