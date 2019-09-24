%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name typerep-map
%define f_pkg_name typerep-map
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.2
Release: alt2
License: MIT
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/typerep-map
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Efficient implementation of a dependent map with types as keys

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-primitive
BuildPreReq: ghc%ghc_version-vector
BuildRequires: chrpath


%description
A dependent map from type representations to values of these types.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
chrpath -d %buildroot%hs_libdir/libHS*.so
if [ -d %f_pkg_name.pkg ]; then
    mkdir -p %buildroot%hs_pkgconfdir
    for f in %f_pkg_name.pkg/*; do
        pkgname=$(grep ^name: $f | sed 's/name:\s*\(.*\)/\1/')
        pkgver=$(grep ^version: $f | sed 's/version:\s*\(.*\)/\1/')
        install -m 755 $f %buildroot%pkg_libdir/$pkgname.pkg
        test "$pkgname" != "%f_pkg_name" ||
            install -D -m 644 $f %buildroot%hs_pkgconfdir/$pkgname-$pkgver.conf
    done
fi
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Thu Sep 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.3.2-alt2
- Fix build on 32-bits platforms

* Wed Sep 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.3.2-alt1
- Spec created by cabal2rpm 0.20_11
- Remove RUNPATH section from dynamic libraries
- Install package.conf from directory
