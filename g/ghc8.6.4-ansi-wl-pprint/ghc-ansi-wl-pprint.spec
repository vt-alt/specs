%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name ansi-wl-pprint
%define f_pkg_name ansi-wl-pprint
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.9
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://github.com/ekmett/ansi-wl-pprint
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: The Wadler/Leijen Pretty Printer for colored ANSI terminal output

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-ansi-terminal


%description
This is a pretty printing library based on Wadler's paper "A Prettier Printer".
It has been enhanced with support for ANSI terminal colored output using the
ansi-terminal package.

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
* Mon Jul 01 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.6.9-alt1
- Spec created by cabal2rpm 0.20_11
- Add build dependency to ansi-terminal
