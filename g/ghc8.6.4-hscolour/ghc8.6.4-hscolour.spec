%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hscolour
%define f_pkg_name hscolour
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.24.4
Release: alt1

Summary: Colourise Haskell code.

License: GPL
Group: Development/Haskell
Url: https://hackage.haskell.org/package/hscolour

Source: %name-%version.tar

# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc8.6.4-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc8.6.4 ghc8.6.4-doc

%description
hscolour is a small Haskell script to colourise Haskell code. It currently
has six output formats: ANSI terminal codes (optionally XTerm-256colour
codes), HTML 3.2 with <font> tags, HTML 4.01 with CSS, HTML 4.01 with CSS
and mouseover annotations, XHTML 1.0 with inline CSS styling, LaTeX, and
mIRC chat codes.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Jul 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.24.4-alt1
- Build new version for ghc8.6.4.

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.20.3-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.20.3-alt1
- Spec created by cabal2rpm 0.20_08
