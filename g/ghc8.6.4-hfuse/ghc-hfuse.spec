%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name HFuse
%define f_pkg_name hfuse
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.5.1
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/m15k/hfuse
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: HFuse is a binding for the Linux FUSE library.

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-base-compat
BuildPreReq: pkgconfig(fuse)


%description
Bindings for the FUSE library, compatible with Linux, OSXFUSE and FreeBSD.

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
* Tue Apr 23 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.2.5.1-alt1
- Spec created by cabal2rpm 0.20_11 from actual sources:
  https://github.com/altlinuxteam/hfuse/
