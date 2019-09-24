%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name exceptions
%define f_pkg_name exceptions
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.10.3
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/exceptions
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Extensible optionally-pure exceptions

BuildRequires: ghc8.6.4 ghc8.6.4-doc ghc8.6.4-transformers-compat


%description
Extensible optionally-pure exceptions.

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.10.3-alt1
- Build new version for ghc8.6.4.
