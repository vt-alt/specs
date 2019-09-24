%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name unliftio-core
%define f_pkg_name unliftio-core
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.2.0
Release: alt1
License: MIT
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/unliftio-core
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: The MonadUnliftIO typeclass for unlifting monads to IO

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
Please see the documentation and README at
<https://www.stackage.org/package/unliftio-core>

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.2.0-alt1
- Build new version for ghc8.6.4.
