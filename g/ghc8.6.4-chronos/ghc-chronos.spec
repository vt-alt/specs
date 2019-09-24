%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name chronos
%define f_pkg_name chronos
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.7
Release: alt2
License: BSD-3-Clause
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/andrewthad/chronos
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A performant time library

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-aeson
BuildPreReq: ghc%ghc_version-attoparsec
BuildPreReq: ghc%ghc_version-clock
BuildPreReq: ghc%ghc_version-hashable
BuildPreReq: ghc%ghc_version-primitive
BuildPreReq: ghc%ghc_version-semigroups
BuildPreReq: ghc%ghc_version-torsor
BuildPreReq: ghc%ghc_version-vector


%description
Chronos is a performance-oriented time library for Haskell, with a
straightforward API. The main differences between this and the
time library are: * Chronos uses machine integers where possible.
This means that time-related arithmetic should be faster, with the
drawback that the types are incapable of representing times that
are very far in the future or the past (because Chronos provides
nanosecond, rather than picosecond, resolution).

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
* Thu Sep 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.7-alt2
- Fix build on 32-bits platforms

* Wed Sep 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.7-alt1
- Spec created by cabal2rpm 0.20_11
