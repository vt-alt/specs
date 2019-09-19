%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name ansi-terminal
%define f_pkg_name ansi-terminal
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.9.1
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/feuerbach/ansi-terminal
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Simple ANSI terminal support, with Windows compatibility

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-colour


%description
ANSI terminal support for Haskell: allows cursor movement, screen clearing,
color output, showing or hiding the cursor, and changing the title. Works
on UNIX and Windows.

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
* Mon Jul 01 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.9.1-alt1
- Spec created by cabal2rpm 0.20_11
- Add build dependency to colour
