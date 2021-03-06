%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name regex-base
%define f_pkg_name regex-base
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.94.0.0
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/regex-base
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Replaces/Enhances Text.Regex

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
Interface API for regex-posix,pcre,parsec,tdfa,dfa

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
* Mon Jun 22 2020 Denis Smirnov <mithraen@altlinux.ru> 0.94.0.0-alt1
- 0.94.0.0

* Fri Aug 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.93.2-alt1
- Build new version for ghc8.6.4.
