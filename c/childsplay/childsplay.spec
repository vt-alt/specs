%define realname childsplay_sp
%define alphabet_dir %_datadir/%name/alphabet-sounds

Name: childsplay
Version: 3.4
Release: alt1

License: GPLv3+
Group: Games/Educational
Url: http://www.schoolsplay.org/

Summary: Suite of educational games for young children

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.savannah.gnu.org/releases/childsplay/%name-%version.tar

Source1: %name.desktop

BuildArch: noarch

%add_python_lib_path %_datadir/%name/

BuildRequires: python-devel >= 2.6
BuildRequires: python-module-pygtk-devel >= 2.0
BuildRequires: python-module-numpy libnumpy-devel
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-pygame-devel >= 1.7
BuildRequires: libSDL-devel >= 1.2
BuildRequires: libSDL_image-devel >= 1.2
BuildRequires: libSDL_ttf-devel >= 2.0
BuildRequires: libSDL_mixer-devel >= 1.2
BuildRequires: libogg-devel
BuildRequires: gettext-tools

Requires: python-module-SQLAlchemy

Provides:      childsplay_sp = %version-%release
Provides:      childsplay_plugins = %version-%release
Obsoletes:     childsplay_plugins <= 0.90

%description
Childsplay is a suite of educational games for young children. It's
written in Python and uses the SDL-libraries. The aim is to be
educational and at the same time be fun to play.

Some activities make use of language dependent voice samples, these sounds are
available as childsplay-alphabet_sounds packages. For those you'll have to
install the childsplay-alphabet_sounds package for the languages you intend to
use. For example childsplay-alphabet_sounds_nl.
Available alphabet sounds packages:
childsplay-alphabet_sounds_bg
childsplay-alphabet_sounds_ca
childsplay-alphabet_sounds_de
childsplay-alphabet_sounds_el
childsplay-alphabet_sounds_es
childsplay-alphabet_sounds_fr
childsplay-alphabet_sounds_it
childsplay-alphabet_sounds_nl
childsplay-alphabet_sounds_pt
childsplay-alphabet_sounds_ro
childsplay-alphabet_sounds_ru
childsplay-alphabet_sounds_sk
childsplay-alphabet_sounds_sl
childsplay-alphabet_sounds_sv


%package alphabet_sounds_bg
Summary:        Bulgarian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_bg
Bulgarian alphabet sounds for Childsplay

%package alphabet_sounds_ca
Summary:        Czech  alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_ca
Czech  alphabet sounds for Childsplay

%package alphabet_sounds_cs
Summary:        Catalan alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_cs
Catalan alphabet sounds for Childsplay

%package alphabet_sounds_de
Summary:        German alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_de
German alphabet sounds for Childsplay

%package alphabet_sounds_el
Summary:        New Greek alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_el
new Greek alphabet sounds for Childsplay

%package alphabet_sounds_en_GB
Summary:        British English alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_en_GB
British English alphabet sounds for Childsplay

%package alphabet_sounds_es
Summary:        Spanish alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_es
Spanish alphabet sounds for Childsplay

%package alphabet_sounds_fr
Summary:        French alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_fr
French alphabet sounds for Childsplay

%package alphabet_sounds_gl
Summary:        Galician alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_gl
Galician alphabet sounds for Childsplay

%package alphabet_sounds_hr
Summary:        Croatian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_hr
Croatian alphabet sounds for Childsplay

%package alphabet_sounds_it
Summary:        Italian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_it
Italian alphabet sounds for Childsplay

%package alphabet_sounds_lt
Summary:        Lithuanian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_lt
Lithuanian alphabet sounds for Childsplay

%package alphabet_sounds_nb
Summary:        Norwegian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_nb
Norwegian alphabet sounds for Childsplay

%package alphabet_sounds_nl
Summary:        Dutch alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_nl
Dutch alphabet sounds for Childsplay

%package alphabet_sounds_pt
Summary:        Portuguese alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_pt
Portuguese alphabet sounds for Childsplay

%package alphabet_sounds_pt_BR
Summary:        Portuguese Brazil alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_pt_BR
Portuguese Brazil alphabet sounds for Childsplay

%package alphabet_sounds_ro
Summary:        Romanian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_ro
Romanian alphabet sounds for Childsplay

%package alphabet_sounds_ru
Summary:        Russian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_ru
Russian alphabet sounds for Childsplay

%package alphabet_sounds_sk
Summary:        Slovak alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_sk
Slovak alphabet sounds for Childsplay

%package alphabet_sounds_sl
Summary:        Slovenian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_sl
Slovenian alphabet sounds for Childsplay

%package alphabet_sounds_sv
Summary:        Swedish alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_sv
Swedish alphabet sounds for Childsplay

%prep
%setup

# due unknown Mail module
rm -fv SPDebugDialog.py
rm -fv SPWidgets/test.py
%__subst "s|import SpDebugDialog||" SPMainCore.py

# set pathes
cat <<EOF >SPBasePaths.py
# This module holds all paths needed for %name.
DOCDIR = '%_datadir/doc/%name-%version'
#PYTHONCPDIR = '%python_sitelibdir/%realname'
BASEDIR = '%_datadir/%name'
SHARELIBDATADIR = '%_datadir/%name/lib'
ALPHABETDIR = '%alphabet_dir'
LOCALEDIR = '%_datadir/locale'
WWWDIR = 'www/backend'
EOF

%install
mkdir -p %buildroot%_bindir/
cat <<EOF >%buildroot%_bindir/%name
#!/bin/sh
cd %_datadir/%name/
python childsplay.py
EOF
chmod a+x %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/locale/
mkdir -p %buildroot%_datadir/%name/

cp -a *.py lib SPWidgets %buildroot%_datadir/%name/
cp sp_content.db %buildroot%_datadir/%name/lib/
cp -a alphabet-sounds %buildroot%_datadir/%name/
cp -a locale/* %buildroot%_datadir/locale/

mkdir -p %buildroot%_desktopdir/
install -m644 %SOURCE1 %buildroot%_desktopdir/
mkdir -p %buildroot%_datadir/icons/hicolor/64x64/apps/
install -m644 lib/SPData/themes/childsplay/logo_cp_64x64.png %buildroot%_datadir/icons/hicolor/64x64/apps/%name.png

%find_lang %name

%files -f %name.lang
%doc Changelog COPYING db.dev
%_bindir/%name
%dir %_datadir/%name/
%dir %alphabet_dir/
%_datadir/%name/*.py*
%_datadir/%name/lib/
%_datadir/%name/SPWidgets/
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png

%files alphabet_sounds_bg
%alphabet_dir/bg/

%files alphabet_sounds_ca
%alphabet_dir/ca/

%files alphabet_sounds_cs
%alphabet_dir/cs/

%files alphabet_sounds_de
%alphabet_dir/de/

%files alphabet_sounds_el
%alphabet_dir/el/

%files alphabet_sounds_en_GB
%alphabet_dir/en_GB/

%files alphabet_sounds_es
%alphabet_dir/es/

%files alphabet_sounds_fr
%alphabet_dir/fr/

%files alphabet_sounds_gl
%alphabet_dir/gl/

%files alphabet_sounds_hr
%alphabet_dir/hr/

%files alphabet_sounds_it
%alphabet_dir/it/

%files alphabet_sounds_lt
%alphabet_dir/lt/

%files alphabet_sounds_nb
%alphabet_dir/nb/

%files alphabet_sounds_nl
%alphabet_dir/nl/

%files alphabet_sounds_pt
%alphabet_dir/pt/

%files alphabet_sounds_pt_BR
%alphabet_dir/pt_BR/

%files alphabet_sounds_ro
%alphabet_dir/ro/

%files alphabet_sounds_ru
%alphabet_dir/ru/

%files alphabet_sounds_sk
%alphabet_dir/sk/

%files alphabet_sounds_sl
%alphabet_dir/sl/

%files alphabet_sounds_sv
%alphabet_dir/sv/


%changelog
* Thu May 23 2019 Leontiy Volodin <lvol@altlinux.org> 3.4-alt1
- new version 3.4

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3 (with rpmrb script)

* Sat Oct 01 2016 Vitaly Lipatov <lav@altlinux.ru> 2.6.5-alt1
- new version (2.6.5) with rpmgs script
- fix requires (ALT bug #26630)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-2.7

* Thu Aug 18 2011 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version 1.6 (thanks kostyalamer) (closes: #26072)
- Put alphabet sounds in separate packages

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.90.2-alt1.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.90.2-alt1
- new version 0.90.2 (with rpmrb script)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.90.1-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for childsplay

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.90.1-alt2.1
- Rebuilt with python-2.5.

* Tue Dec 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.90.1-alt2
- add patch for fix bug #13571 (thanks to Slava Semushin php-coder@)
- fix desktop file permissions

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.90.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

