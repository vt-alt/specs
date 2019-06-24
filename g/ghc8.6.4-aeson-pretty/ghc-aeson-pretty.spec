%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name aeson-pretty
%define f_pkg_name aeson-pretty
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.8.7
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://github.com/informatikr/aeson-pretty
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: JSON pretty-printing library and command-line tool.

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-aeson
BuildPreReq: ghc%ghc_version-scientific
BuildPreReq: ghc%ghc_version-unordered-containers
BuildPreReq: ghc%ghc_version-vector
BuildPreReq: ghc%ghc_version-base-compat


%description
A JSON pretty-printing library compatible with aeson as well as a
command-line tool to improve readabilty of streams of JSON data.

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
* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.8.7-alt1
- Spec created by cabal2rpm 0.20_11
