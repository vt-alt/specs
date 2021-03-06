%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name th-abstraction
%define f_pkg_name th-abstraction
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.1.0
Release: alt1
License: ISC
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/glguy/th-abstraction
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Nicer interface for reified information about data types

BuildPreReq: haskell(abi) = %ghc_version


%description
This package normalizes variations in the interface for inspecting datatype
information via Template Haskell so that packages and support a single,
easier to use informational datatype while supporting many versions of
Template Haskell.

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
* Sat Jun 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.3.1.0-alt1
- updated with the help of cabal2gear.

* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.2.11.0-alt1
- Spec created by cabal2rpm 0.20_11
