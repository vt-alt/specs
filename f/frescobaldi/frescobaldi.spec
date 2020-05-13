Name: frescobaldi
Version: 3.1.2
Release: alt1

Summary: LilyPond music score editor
License: %gpl2plus
Group: Publishing

Url: http://www.frescobaldi.org/

BuildRequires(pre): rpm-build-licenses

BuildRequires: ImageMagick-tools
BuildRequires: librsvg-utils python3-module-setuptools

BuildArch: noarch

Requires: lilypond

AutoProv:yes,nopython,nopython3

# Source-url: https://github.com/wbsoft/frescobaldi/archive/v%version.tar.gz
Source: %name-%version.tar

%description
Frescobaldi is a LilyPond music score editor, with following features:

* Enter LilyPond scores, build and preview them with a mouseclick
* Point-and-click support: click on notes or error messages to jump to the
  correct position
* A powerful Score Wizard to quickly setup a musical score
* Editing tools to:
  - manipulate the rhythm
  - hyphenate lyrics
  - quickly enter or add articulations and other symbols to existing music
  - run the document through convert-ly to update it to a newer LilyPond version
  - translate pitch names
* Context sensitive autocomplete, helping you to quickly enter LilyPond commands
* Expansion manager to enter larger snippets of LilyPond input using short
  mnemonics
* A powerful Rumor plugin, using the Rumor program to quickly enter music by
  playing it on a MIDI keyboard or even your computer keyboard
* Quick buttons to open, send, play or print LilyPond-generated files.
* Built-in comprehensive User Guide
* Translated into Dutch, English, French, German, Italian, Czech, Russian,
  Spanish, Turkish and Polish.

%prep
%setup

%build
%python3_build
cd linux && %make_build

%install
%python3_install
install -d %buildroot%_liconsdir/
rsvg-convert -w 48 -h 48  \
%buildroot%_iconsdir/hicolor/scalable/apps/org.frescobaldi.Frescobaldi.svg \
  -o %buildroot%_liconsdir/org.frescobaldi.Frescobaldi.png

%files
%doc README.md
%_bindir/%name
%python3_sitelibdir_noarch/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/org.frescobaldi.Frescobaldi.metainfo.xml
%_liconsdir/*.png
%_man1dir/*

%changelog
* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt1
- new version 3.1.2 (with rpmrb script)

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- build new python3 version

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script
- build from tarball

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.1
- Rebuild with Python-2.7

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 1.0.2-alt1
- update to 1.0.2

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 1.0.1-alt1
- update to 1.0.1

* Sun Dec 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.0.0-alt1
- update to 1.0.0

* Mon Dec 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.17-alt1
- update to 0.7.17

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.15-alt1.svn1604.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.15-alt1.svn1604
- update to svn1604

* Wed Oct 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.15-alt1
- update to v0.7.15

* Sun Oct 11 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.14-alt1.svn1513
- update to svn1513

* Mon Aug 17 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.7.14-alt1.svn1456
- initial build for Sisyphus (svn1456)
