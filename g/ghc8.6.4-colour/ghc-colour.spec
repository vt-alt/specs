%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name colour
%define f_pkg_name colour
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.3.5
Release: alt1
License: MIT
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://www.haskell.org/haskellwiki/Colour
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A model for human colour/color perception

BuildPreReq: haskell(abi) = %ghc_version


%description
This package provides a data type for colours and transparency. Colours can
be blended and composed. Various colour spaces are supported. A module of
colour names ("Data.Colour.Names") is provided.

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
* Mon Jul 01 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.3.5-alt1
- Spec created by cabal2rpm 0.20_11
