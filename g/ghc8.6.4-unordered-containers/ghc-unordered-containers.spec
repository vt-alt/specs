%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name unordered-containers
%define f_pkg_name unordered-containers
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.10.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/tibbe/unordered-containers
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Efficient hashing-based container types

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-hashable


%description
Efficient hashing-based container types. The containers have been optimized
for performance critical use, both in terms of large data quantities and
high speed.

The declared cost of each operation is either worst-case or amortized, but
remains valid even if structures are shared.

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
* Sat Jun 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.2.10.0-alt1
- Spec created by cabal2rpm 0.20_11
