%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name async
%define f_pkg_name async
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.2.2
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/simonmar/async
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Run IO operations asynchronously and wait for their results

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-hashable


%description
This package provides a higher-level interface over threads, in which an
@Async a@ is a concurrent thread that will eventually deliver a value of
type @a@. The package provides ways to create @Async@ computations, wait
for their results, and cancel them.

Using @Async@ is safer than using threads in two ways:

* When waiting for a thread to return a result, if the thread dies with an
exception then the caller must either re-throw the exception ('wait') or
handle it ('waitCatch'); the exception cannot be ignored.

* The API makes it possible to build a tree of threads that are
automatically killed when their parent dies (see 'withAsync').

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
* Sat Jun 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.2-alt1
- updated with the help of cabal2gear.

* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.2.1-alt1
- Spec created by cabal2rpm 0.20_11
