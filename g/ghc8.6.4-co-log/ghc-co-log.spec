%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name co-log
%define f_pkg_name co-log
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.0.0
Release: alt1
License: MPL-2.0
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/co-log
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Composable Contravariant Comonadic Logging Library

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-ansi-terminal
BuildPreReq: ghc%ghc_version-chronos
BuildPreReq: ghc%ghc_version-co-log-core
BuildPreReq: ghc%ghc_version-contravariant
BuildPreReq: ghc%ghc_version-typerep-map
BuildPreReq: ghc%ghc_version-markdown-unlit


%description
The default implementation of logging based on
[co-log-core](http://hackage.haskell.org/package/co-log-core).

The ideas behind this package are described in the following blog post:

* [co-log: Composable Contravariant Combinatorial Comonadic Configurable
Convenient Logging](https://kowainik.github.io/posts/2018-09-25-co-log)
homepage: https://github.com/kowainik/co-log

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
rm -f %buildroot%_bindir/*
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Sep 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.3.0.0-alt1
- Spec created by cabal2rpm 0.20_11
