%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name split
%define f_pkg_name split
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.3.3
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/split
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Combinator library for splitting lists.

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
A collection of various methods for splitting lists into parts, akin to the
\"split\" function found in several mainstream languages. Here is its tale:

Once upon a time the standard "Data.List" module held no function for
splitting a list into parts according to a delimiter. Many a brave
lambda-knight strove to add such a function, but their striving was in
vain, for Lo, the Supreme Council fell to bickering amongst themselves what
was to be the essential nature of the One True Function which could cleave
a list in twain (or thrain, or any required number of parts).

And thus came to pass the split package, comprising divers functions for
splitting a list asunder, each according to its nature. And the Supreme
Council had no longer any grounds for argument, for the favored method of
each was contained therein.

To get started, see the "Data.List.Split" module.

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.3.3-alt1
- Build new version for ghc8.6.4.
