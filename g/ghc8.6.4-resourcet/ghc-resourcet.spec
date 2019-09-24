%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name resourcet
%define f_pkg_name resourcet
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.2
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/resourcet
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Deterministic allocation and freeing of scarce resources.

BuildRequires: ghc8.6.4 ghc8.6.4-doc
BuildRequires: ghc8.6.4-exceptions ghc8.6.4-primitive ghc8.6.4-unliftio-core


%description
Hackage documentation generation is not reliable. For up to date
documentation, please see: <http://www.stackage.org/package/resourcet>.

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Build new version for ghc8.6.4.
