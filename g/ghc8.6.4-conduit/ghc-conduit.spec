%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name conduit
%define f_pkg_name conduit
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.3.1.1
Release: alt1
License: MIT
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/conduit
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Streaming data processing library.

BuildRequires: ghc8.6.4 ghc8.6.4-doc
BuildRequires: ghc8.6.4-exceptions
BuildRequires: ghc8.6.4-mono-traversable
BuildRequires: ghc8.6.4-primitive
BuildRequires: ghc8.6.4-resourcet
BuildRequires: ghc8.6.4-unliftio-core
BuildRequires: ghc8.6.4-vector


%description
`conduit` is a solution to the streaming data problem, allowing for
production, transformation, and consumption of streams of data in constant
memory. It is an alternative to lazy I\/O which guarantees deterministic
resource handling.

For more information about conduit in general, and how this package in
particular fits into the ecosystem, see [the conduit
homepage](https://github.com/snoyberg/conduit#readme).

Hackage documentation generation is not reliable. For up to date
documentation, please see: <http://www.stackage.org/package/conduit>.

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
* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.1.1-alt1
- Build new version for ghc8.6.4.
