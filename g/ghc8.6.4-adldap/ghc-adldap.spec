%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name adldap
%define f_pkg_name adldap
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.0.0
Release: alt1
License: BSD-3-Clause
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/altlinuxteam/adldap
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: High level interface to Active Directory via LDAP

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-ldap
BuildPreReq: ghc%ghc_version-asn1-encoding
BuildPreReq: ghc%ghc_version-asn1-types
BuildPreReq: ghc%ghc_version-aeson
BuildPreReq: ghc%ghc_version-aeson-pretty
BuildPreReq: ghc%ghc_version-attoparsec
BuildPreReq: ghc%ghc_version-base64-bytestring
BuildPreReq: libldap-devel


%description
High level interface to Active Directory via LDAP

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
* Thu Jun 06 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt1
- Initial from upstream with Spec created by cabal2rpm 0.20_11
