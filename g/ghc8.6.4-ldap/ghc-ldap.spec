%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name LDAP
%define f_pkg_name ldap
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.12
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/ezyang/ldap-haskell
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Haskell binding for C LDAP API

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: libldap-devel libsasl2-devel

Requires: libsasl2-plugin-gssapi


%description
This package provides LDAP interface code for Haskell programs, binding to
the C LDAP API.

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
* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.6.12-alt1
- Spec created by cabal2rpm 0.20_11 from actual sources:
  https://github.com/altlinuxteam/ldap-haskell
- Add build dependencies to libldap-devel libsasl2-devel
- Add dependency to libsasl2-plugin-gssapi
