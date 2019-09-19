%set_verify_elf_method rpath=relaxed

%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hadfs
%define f_pkg_name hadfs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: hadfs
Version: 0.1.0.0
Release: alt5
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/altlinuxteam/hadfs
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Active Directory File System implemented on Haskell

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: %hsc_namever-adldap
BuildPreReq: %hsc_namever-hfuse
BuildPreReq: %hsc_namever-network
BuildPreReq: %hsc_namever-unix-compat
BuildPreReq: %hsc_namever-optparse-applicative
BuildPreReq: libldap-devel libfuse-devel

Requires: libsasl2-plugin-gssapi

%description
Active Directory File System (ADFS) is administration tool
for LDAP objects via POSIX interface.

%prep
%setup
%patch -p1

%build
%hs_configure2 --disable-shared
%hs_build

%install
%hs_install
rm -rf %buildroot/%_libdir/%hsc_name-%hsc_version/
%hs_gen_filelist
mkdir -p %buildroot/%_man1dir
install -m 0644 doc/hadfs.1 %buildroot/%_man1dir/

%files -f %name-files.all
%_man1dir/hadfs*

%changelog
* Wed Jun 26 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt5
- Add manpage for hadfs
- Update hadfs with options parser

* Fri Jun 21 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt4
- Add requires to GSSAPI SASL2 plugin

* Mon Jun 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt3
- Prepare static build for Sisyphus
- Clean submodules from package sources
- Update project URL

* Thu May 23 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt2
- Rebuild with fixed adldap (fix parsing of ObjectReplicaLink field)
- Build with compatibility patch for ghc-7.6.1

* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt1
- Spec created by cabal2rpm 0.20_11
