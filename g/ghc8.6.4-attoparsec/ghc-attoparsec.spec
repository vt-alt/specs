%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name attoparsec
%define f_pkg_name attoparsec
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.13.2.2
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/bos/attoparsec
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Fast combinator parsing for bytestrings and text

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-scientific


%description
A fast parser combinator library, aimed particularly at dealing efficiently
with network protocols and complicated text/binary file formats.

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
* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.13.2.2-alt1
- Spec created by cabal2rpm 0.20_11
