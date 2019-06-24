%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name scientific
%define f_pkg_name scientific
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.6.2
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/basvandijk/scientific
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Numbers represented using scientific notation

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-hashable
BuildPreReq: ghc%ghc_version-integer-logarithms
BuildPreReq: ghc%ghc_version-primitive


%description
"Data.Scientific" provides the number type 'Scientific'. Scientific numbers
are arbitrary precision and space efficient. They are represented using
<http://en.wikipedia.org/wiki/Scientific_notation scientific notation>. The
implementation uses a coefficient @c :: 'Integer'@ and a base-10 exponent
@e :: 'Int'@. A scientific number corresponds to the 'Fractional' number:
@'fromInteger' c * 10 '^^' e@.

Note that since we're using an 'Int' to represent the exponent these
numbers aren't truly arbitrary precision. I intend to change the type of
the exponent to 'Integer' in a future release.

The main application of 'Scientific' is to be used as the target of parsing
arbitrary precision numbers coming from an untrusted source. The advantages
over using 'Rational' for this are that:

* A 'Scientific' is more efficient to construct. Rational numbers need to
be constructed using '%%' which has to compute the 'gcd' of the 'numerator'
and 'denominator'.

* 'Scientific' is safe against numbers with huge exponents. For example:
@1e1000000000 :: 'Rational'@ will fill up all space and crash your program.
Scientific works as expected:

>>> read "1e1000000000" :: Scientific 1.0e1000000000

* Also, the space usage of converting scientific numbers with huge
exponents to @'Integral's@ (like: 'Int') or @'RealFloat's@ (like: 'Double'
or 'Float') will always be bounded by the target type.

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
* Wed Apr 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.3.6.2-alt1
- Spec created by cabal2rpm 0.20_11
