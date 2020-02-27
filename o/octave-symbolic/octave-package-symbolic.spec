# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octave_pkg_name symbolic
Name: octave-%octave_pkg_name
Version: 2.8.0
Release: alt1
Summary: Octave Symbolic Package using SymPy

Group: Sciences/Mathematics
License: GPL-3.0+
URL: http://github.com/cbm755/octsympy

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(symbolic) = %version

# SystemRequirements: python, sympy (>= 1.0)
BuildRequires: python sympy >= 1.0
# Depends: octave (>= 4.0)
Requires: octave >= 4.0


%description
The Octave-Forge Symbolic package adds symbolic calculation

%prep
%setup -q -n %{octave_pkg_name}-%{version}

%build
octave -q -H --no-window-system --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
%if_with _octave_arch
octave -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-$(octave -H --no-window-system --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"
%else
octave -q -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-any-none.tar.gz"
%endif

%files
%doc DESCRIPTION matlab_smt_differences.md CONTRIBUTORS README.md COPYING NEWS
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Wed Feb 19 2020 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version.

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1
- initial import by package builder

