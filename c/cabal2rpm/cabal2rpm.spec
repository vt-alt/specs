Name: cabal2rpm
Version: 0.20.10
Release: alt1
License: GPL2+
Group: Development/Haskell
Source: %name-%version.tar
Summary: converts Haskell Cabal descriptions into RPM specs
Url: http://community.moertel.com/ss/space/Cabal2rpm

BuildArch: noarch

%description
This tool converts Haskell Cabal package-descriptions (.cabal files)
into RPM spec files.  It makes reasonable guesses at what should go
in the specs, but because "Cabalized" tarballs presently do not have a
standardized layout and naming conventions, you may need to make some
adjustments.

%prep
%setup

%build
%install
install -D -m755 cabal2rpm %buildroot%_bindir/cabal2rpm
install -D -m755 cabal2gear %buildroot%_bindir/cabal2gear

%files
%_bindir/cabal2rpm
%_bindir/cabal2gear

%changelog
* Thu Feb 28 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.20.10-alt1
- Update spec template to newest rpm-build-haskel supports haskell(abi)

* Fri Feb 22 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.20.09-alt1
- Remove version of compiler from spec filename
- Rename pkg_libdir to compiler directory as it prefer in newest ghc versions
- Update spec with build require to rpm-build-haskell supported new ghc versions
- Fix gear2rpm with trim white spaces from the right side of rpm_version

* Thu Nov 26 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.20.08-alt12
- cabal2gear conceptual enhancements:
  + separated maintainer's tweaks and automatic results in the Git repo
    (this way a new run of the robot won't spoil the maintainer's tweaks;
     a third branch is used: upstream_/AUTO/cabal2rpm);
  + implemented updating the gear-repos with new sources (and/or by new
    cabal2rpm rules if that ever happens);
  + for compatibility with gear-repos created by earlier versions of cabal2gear,
    updating an old repo would fake upstream_/AUTO/cabal2rpm with cabal2rpm
    (ideally, this should be the old cabal2rpm and cabal2gear rules, but
    fortunately, the content generated by them hasn't changed yet).
  (This code needs cleanup and more documentation, but works and is
  used already. The old usage for creating initial gear-repos remains
  almost without user-visible changes: all the generated content is
  the same, only a new Git branch is added.)

* Thu Nov 26 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.20.08-alt11
- cabal2gear: make the remote config consistent with git-remote
  (like in ALT bug 31479).

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt10
- autocreate watch file
- simplify spec-file
- fix Url tag

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt9
- fix spec creation for packages with executables

* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt8
- cabal2gear -- ghc version autodetect
- haddock fix

* Tue Mar 27 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt7
- fix working in non-english locales
- change gear repo structure

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt6
- ghc 7.4.1 support

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt5
- add Url tag

* Tue Sep 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt4
- use new macro from rpm-build-haskell

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt3
- fix changelog
- add cabal2gear utility

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt2
- fix for ghc 6.12

* Wed Sep 08 2010 Denis Smirnov <mithraen@altlinux.ru> 0.20.08-alt1
- first build for Sisyphus
