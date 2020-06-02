Name: qelectrotech
Version: 0.61
Release: alt3
Epoch: 1

Summary: An electric diagrams editor
# Prog is GPLv2 - Symbols/Elements are Creative Commons Attribution
License: GPLv2+
Group: Engineering

Url: http://qelectrotech.org/
Source0: qelectrotech-%version-src.tar.gz
Source1: %name.watch
Patch: %name-fix-build-with-qt5.11.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools
BuildRequires: libqt5-xml
BuildRequires: libqt5-svg
BuildRequires: libqt5-network
BuildRequires: libqt5-widgets
BuildRequires: libqt5-printsupport

Requires: qelectrotech-symbols = %EVR
Requires: qt5-translations

Summary(ar): مُحرّر مخططات كهربائية
Summary(ca): Editar esquemes elèctrics
Summary(cs): Editor výkresů elektrických obvodů
Summary(de): Zeichenprogramm für Schaltpläne
Summary(el): Επεξεργασία ηλεκτρικών διαγραμμάτων
Summary(es): Un editor de esquemas eléctricos
Summary(fr): Un éditeur de schémas électriques
Summary(hr): Uredi elektro sheme
Summary(it): Un programma per disegnare schemi elettrici
Summary(pl): Edytor schematów elektrycznych
Summary(pt): Um editor de esquemas eléctricos
Summary(ru): Редактор электрических схем

%description
QElectroTech is a Qt4 application to design electric diagrams. It uses XML
files for elements and diagrams, and includes both a diagram editor and an
element editor.

%description -l cs
QElectroTech je aplikací Qt4 určenou pro návrh nákresů elektrických obvodů.
Pro prvky a nákresy používá soubory XML, a zahrnuje v sobě jak editor nákresů,
tak editor prvků.

%description -l el
Το QElectroTech είναι μια εφαρμογή Qt4 για σχεδίαση ηλεκτρικών διαγραμμάτων.
Χρησιμοποιεί αρχεία XML για στοιχεία και διαγράμματα, και περιλαμβάνει
επεξεργαστή διαγραμμάτων καθώς και επεξεργαστή στοιχείων.

%description -l es
QElectroTech es una aplicación Qt4 para diseñar esquemas eléctricos.
Utiliza archivos XML para los elementos y esquemas, e incluye un editor
de esquemas y un editor de elemento.

%description -l fr
QElectroTech est une application Qt4 pour réaliser des schémas électriques.
QET utilise le format XML pour ses éléments et ses schémas et inclut un
éditeur de schémas ainsi qu'un éditeur d'élément.

%description -l it
QElectroTech è una applicazione fatta in Qt4 per disegnare schemi elettrici.
QET usa il formato XML per i suoi elementi e schemi, includendo anche un
editor per gli stessi.

%description -l pl
QElectroTech to aplikacja napisana w Qt4, przeznaczona do tworzenia schematów
elektrycznych. Wykorzystuje XML do zapisywania plików elementów i projektów.
Posiada edytor schematów i elementów.

%description -l pt
QElectroTech é uma aplicação baseada em Qt4 para desenhar esquemas eléctricos.
QET utiliza ficheiros XML para os elementos e para os esquemas e inclui um
editor de esquemas e um editor de elementos.

%description -l ru
QElectroTech - приложение, написанное на Qt4 и предназначенное для разработки
электрических схем. Оно использует XML-файлы для элементов и схем и включает
как редактор схем, так и редактор элементов.

%package symbols
Summary: Elements collection for QElectroTech
Summary(cs): Sbírka prvků pro QElectroTech
Summary(el): Συλλογή στοιχείων του QElectroTech
Summary(es): Collección de elementos para QElectroTech
Summary(fr): Collection d'éléments pour QElectroTech
Summary(it): Collezione di elementi per QElectroTech
Summary(pl): Kolekcja elementów QElectroTech
Summary(pt): Colecção de elementos para QElectroTech
Summary(ru): Коллекция элементов для QElectroTech
Group: Engineering
License: CC-BY
BuildArch: noarch
Requires: qelectrotech = %EVR

%description symbols
Elements collection for QElectroTech.

%description -l cs symbols
Sbírka prvků pro QElectroTech.

%description -l el symbols
Συλλογή στοιχείων του QElectroTech.

%description -l es symbols
Collección de elementos para QElectroTech.

%description -l fr symbols
Collection d'éléments pour QElectroTech.

%description -l it symbols
Collezione di elementi per QElectroTech.

%description -l pl symbols
Kolekcja elementów QElectroTech.

%description -l pt symbols
Colecção de elementos para QElectroTech.

%description -l ru symbols
Коллекция элементов для QElectroTech.

%prep
%setup -n %name-%version-src
%patch -p2

sed -e s,/usr/local/,%prefix/, \
    -e /QET_MAN_PATH/s,'man/','share/man', \
    -e /QET_MIME/s,../,, \
    -i %name.pro

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.cc' -o -name '*.h' |
	xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

lrelease-qt5 %name.pro
qmake-qt5 %name.pro

%build
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

# We only provides UTF-8 files
rm -rf %buildroot/usr/doc/%name \
       %buildroot%_datadir/%name/examples \
       %buildroot%_mandir/fr.ISO8859-1 \
       %buildroot%_mandir/fr

# Fix excessive categories in desktop file
subst 's/^Categories=.*$/Categories=Graphics;Engineering;/' %buildroot%_desktopdir/%name.desktop

mv %buildroot%_mandir/fr.UTF-8 %buildroot%_mandir/fr

# QT translation provided by QT.
rm -f %buildroot%_datadir/%name/lang/qt_*.qm

%find_lang --output=%name.lang --with-qt --with-man qet qelectrotech

%files -f %name.lang
%doc CREDIT LICENSE examples
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_datadir/mime/application/x-qet-*.xml
%_datadir/mime/packages/%name.xml
%_datadir/mimelnk/application/x-qet-*.desktop
%_iconsdir/hicolor/*/*/*.png
%dir %_datadir/%name
%dir %_datadir/%name/lang
%_man1dir/%name.*

%files symbols
%doc ELEMENTS.LICENSE
%_datadir/%name/elements
%_datadir/%name/titleblocks

%changelog
* Mon Jun 01 2020 Anton Midyukov <antohami@altlinux.org> 1:0.61-alt3
- Add missing main categorie (Graphics) for desktop entry file

* Mon Sep 30 2019 Michael Shigorin <mike@altlinux.org> 1:0.61-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- spec cleanup

* Sun Jan 13 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.61-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.6-alt2.qa1
- NMU: applied repocop patch

* Wed Oct 03 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.6-alt2
- Fix build with Qt 5.11.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.6-alt1
- New version.

* Fri Dec 11 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.5-alt1
- New version

* Tue Dec 09 2014 Andrey Cherepanov <cas@altlinux.org> 1:0.4-alt0.rc1
- New version

* Tue Jan 14 2014 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1
- Import in Sisyphus from Fedora
