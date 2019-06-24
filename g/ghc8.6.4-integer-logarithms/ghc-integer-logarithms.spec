%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name integer-logarithms
%define f_pkg_name integer-logarithms
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.3
Release: alt1
License: MIT
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/Bodigrim/integer-logarithms
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Integer logarithms.

BuildPreReq: haskell(abi) = %ghc_version


%description
"Math.NumberTheory.Logarithms" and "Math.NumberTheory.Powers.Integer" from
the arithmoi package.

Also provides "GHC.Integer.Logarithms.Compat" and
"Math.NumberTheory.Power.Natural" modules, as well as some additional
functions in migrated modules.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.3-alt1
- Spec created by cabal2rpm 0.20_11
