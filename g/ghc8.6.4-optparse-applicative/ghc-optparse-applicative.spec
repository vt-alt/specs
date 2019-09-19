%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name optparse-applicative
%define f_pkg_name optparse-applicative
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.14.3.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/pcapriotti/optparse-applicative
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Utilities and combinators for parsing command line options

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-ansi-wl-pprint
BuildPreReq: ghc%ghc_version-transformers-compat


%description
optparse-applicative is a haskell library for parsing options on the
command line, providing a powerful applicative interface for composing
these options.

optparse-applicative takes care of reading and validating the arguments
passed to the command line, handling and reporting errors, generating a
usage line, a comprehensive help screen, and enabling context-sensitive
bash completions.

See the included README for detailed instructions and examples, which is
also available on github
<https://github.com/pcapriotti/optparse-applicative>.

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
* Mon Jul 01 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.14.3.0-alt1
- Spec created by cabal2rpm 0.20_11
- Add build dependency to ansi-wl-pprint and transformers-compat
