%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hreg
%define f_pkg_name hreg
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: hreg
Version: 0.0.1
Release: alt1
License: BSD-3-Clause
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/hreg
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Group Policy Objects storage Parser/Generator

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-attoparsec
BuildPreReq: ghc%ghc_version-base-noprelude
BuildPreReq: ghc%ghc_version-bytestring-encoding
BuildPreReq: ghc%ghc_version-cereal
BuildPreReq: ghc%ghc_version-co-log
BuildPreReq: ghc%ghc_version-conduit
BuildPreReq: ghc%ghc_version-exceptions
BuildPreReq: ghc%ghc_version-filemanip
BuildPreReq: ghc%ghc_version-relude
BuildPreReq: ghc%ghc_version-optparse-applicative
BuildPreReq: ghc%ghc_version-unix-compat


%description
This application provides ability to Export/Import from policy files
of group policy objects and registry files, Apply policy files as
filesystem tree and compare exported registry files.


%prep
%setup
%patch -p1

%build
%hs_configure2 --disable-shared
%hs_build

%install
%hs_install
rm -rf %buildroot/%_libdir/%hsc_name-%hsc_version/
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Tue Sep 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus
- Spec created by cabal2rpm 0.20_11
