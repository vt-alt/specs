%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name asn1-encoding
%define f_pkg_name asn1-encoding
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.9.5
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://github.com/vincenthz/hs-asn1
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: ASN1 data reader and writer in RAW, BER and DER forms

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-asn1-types
BuildPreReq: ghc%ghc_version-hourglass


%description
ASN1 data reader and writer in raw form with supports for high level forms
of ASN1 (BER, and DER).

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
* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.9.5-alt1
- Spec created by cabal2rpm 0.20_11
