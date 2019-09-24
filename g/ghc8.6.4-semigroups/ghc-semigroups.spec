%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name semigroups
%define f_pkg_name semigroups
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.18.5
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://github.com/ekmett/semigroups/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Anything that associates

BuildPreReq: haskell(abi) = %ghc_version


%description
In mathematics, a semigroup is an algebraic structure consisting of a set
together with an associative binary operation. A semigroup generalizes a
monoid in that there might not exist an identity element. It also
(originally) generalized a group (a monoid with all inverses) to a type
where every element did not have to have an inverse, thus the name
semigroup.

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
* Wed Sep 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.18.5-alt1
- Spec created by cabal2rpm 0.20_11
