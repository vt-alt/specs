%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name aeson
%define f_pkg_name aeson
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.4.3.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/bos/aeson
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Fast JSON parsing and encoding

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-attoparsec
BuildPreReq: ghc%ghc_version-dlist
BuildPreReq: ghc%ghc_version-hashable
BuildPreReq: ghc%ghc_version-primitive
BuildPreReq: ghc%ghc_version-scientific
BuildPreReq: ghc%ghc_version-tagged
BuildPreReq: ghc%ghc_version-th-abstraction
BuildPreReq: ghc%ghc_version-time-locale-compat
BuildPreReq: ghc%ghc_version-unordered-containers
BuildPreReq: ghc%ghc_version-uuid-types
BuildPreReq: ghc%ghc_version-vector
BuildPreReq: ghc%ghc_version-base-compat


%description
A JSON parsing and encoding library optimized for ease of use and high
performance.

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
* Mon Jun 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.3.0-alt1
- updated with the help of cabal2gear.

* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.2.0-alt1
- Spec created by cabal2rpm 0.20_11
