%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name transformers-compat
%define f_pkg_name transformers-compat
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.5
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/transformers-compat
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A small compatibility shim for the transformers library

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
This package includes backported versions of types that were added to
transformers in transformers 0.3, 0.4, and 0.5 for users who need strict
transformers 0.2 or 0.3 compatibility to run on old versions of the
platform, but also need those types.

Those users should be able to just depend on @transformers >= 0.2@ and
@transformers-compat >= 0.3@.

Note: missing methods are not supplied, but this at least permits the types
to be used.

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.5-alt1
- Build new version for ghc8.6.4.
