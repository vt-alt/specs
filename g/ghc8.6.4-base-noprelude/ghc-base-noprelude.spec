%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name base-noprelude
%define f_pkg_name base-noprelude
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 4.12.0.0
Release: alt1
License: BSD-3-Clause
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/hvr/base-noprelude
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: "base" package sans "Prelude" module

BuildPreReq: haskell(abi) = %ghc_version


%description
This package simplifies defining custom "Prelude"s without having to use
@-XNoImplicitPrelude@ by re-exporting the full module-hierarchy of the
base-4.12.0.0 package /except/ for the "Prelude" module.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
mkdir -p %buildroot%pkg_libdir
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Sep 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 4.12.0.0-alt1
- Spec created by cabal2rpm 0.20_11
