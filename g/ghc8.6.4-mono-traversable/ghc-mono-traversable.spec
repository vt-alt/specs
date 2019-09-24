%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name mono-traversable
%define f_pkg_name mono-traversable
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.12.0
Release: alt1
License: MIT
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/mono-traversable
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Type classes for mapping, folding, and traversing monomorphic containers

BuildRequires: ghc8.6.4 ghc8.6.4-doc
BuildRequires: ghc8.6.4-hashable
BuildRequires: ghc8.6.4-split
BuildRequires: ghc8.6.4-unordered-containers
BuildRequires: ghc8.6.4-vector
BuildRequires: ghc8.6.4-vector-algorithms


%description
%summary.

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.12.0-alt1
- Build new version for ghc8.6.4.
