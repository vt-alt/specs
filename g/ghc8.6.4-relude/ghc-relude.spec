%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name relude
%define f_pkg_name relude
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.0
Release: alt1
License: MIT
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/relude
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Custom prelude from Kowainik

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-hashable
BuildPreReq: ghc%ghc_version-unordered-containers


%description
== Goals

* Avoid all partial functions (like @head :: [a] -> a@). The types of
partial functions lie about their behavior and usage of such functions can
lead to the unexpected bugs. Though you can still use some unsafe functions
from @Relude.Unsafe@ module, but they are not exported by default.

* Type-safety. We like to make invalid states unrepresantable. And if
it's possible to express this concept through the types then we will do it.

* Performance. Prefer Text over [String], use spaceleak-free functions
(like our custom sum and product).

* Minimalism (low number of dependencies). We don't force users of
relude to stick to some specific lens or text formatting or logging
library.

* Convenience (like lifted to @MonadIO@ functions, more reexports). But
we want to bring common types and functions (like containers and
bytestrng) into scope because they are used in almost every application
anyways.

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
* Tue Sep 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.5.0-alt1
- Spec created by cabal2rpm 0.20_11
