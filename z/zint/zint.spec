Name:      zint
Version:   2.8.0
Release:   alt2
Summary:   A barcode generator and library
Summary(ru_RU.UTF-8): Генератор штрихкодов и библиотека
License:   GPLv3+
URL:       http://www.zint.org.uk
Source:    %name-%version.tar
Source10:  %{name}_ru.qm
Group:     Graphics

Patch: zint-alt-include-header.patch
Patch10: zint-alt-use-l10n.patch

BuildRequires: cmake
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: qt5-base-devel qt5-tools-devel-static
BuildRequires: desktop-file-utils

%description
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the library.
Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and 
  Kanji character sets.
- Full GS1 support including data verification and automated insertion of 
  FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0) characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in the following file formats: PNG, GIF, EPS, WMF, BMP, TIF, SVG.
- Verification stage for SBN, ISBN and ISBN-13 data.

%description -l ru_RU.UTF-8
Zint — это библиотека C для кодирования данных в виде различных штрихкодов.
Встроенная утилита командной строки обеспечивает простой интерфейс к
библиотеке.
Возможности библиотеки:
- Более 50 символик, включая все стандарты ISO/IEC (например, QR-коды).
- Преобразование Юникода для символик, которые поддерживают наборы символов
  Latin-1 и Kanji.
- Поддержка полного GS1, включая проверку данных и автоматическую
  вставку символов FNC1.
- Поддержка кодирования двоичных данных, включая символы NULL (ASCII 0).
- Возможность создания штрихкодов медико-фармацевтической промышленности
  (HIBC).
- Сохранение в следующих форматах файлов: PNG, GIF, EPS, WMF, BMP, TIF, SVG.
- Этап проверки для данных SBN, ISBN и ISBN-13.

%package -n zint-devel
Summary:       Library and header files for %name
Summary(ru_RU.UTF-8): Библиотека и заголовочные файлы для %name
Group:         System/Libraries
Requires:      %name = %version-%release

%description -n zint-devel 
C library and header files needed to develop applications using %name.
The API documentation can be found ont the project website:
http://www.zint.org.uk/zintSite/Manual.aspx

%description -n zint-devel -l ru_RU.UTF-8
Библиотека C и заголовочные файлы, необходимые для разработки приложений
с помощью %name.
Документация программного интерфейса (API) доступна на веб-сайте проекта:
http://www.zint.org.uk/zintSite/Manual.aspx

%package -n zint-qt
Summary:       Zint Barcode Studio GUI and library
Summary(ru_RU.UTF-8): Графический интерфейс и библиотека Zint Barcode Studio
Group:         Graphics
Requires:      %name = %version-%release

%description -n zint-qt
Zint Barcode Studio is a Qt-based GUI which allows desktop users to generate 
barcodes which can then be embedded in documents or HTML pages, and a library 
which can be used to incorporate barcode generation functionality into other 
software.

%description -n zint-qt -l ru_RU.UTF-8
Zint Barcode Studio — это основанный на Qt графический интерфейс, который
позволяет пользователям настольных компьютеров создавать штрихкоды для
последующего внедрения в документы или HTML-страницы, а также библиотека,
которую можно использовать для обеспечения функциональности генерации
штрихкодов в других программах.

%package -n zint-qt-devel
Summary:       Library and header files for %name-qt
Summary(ru_RU.UTF-8): Библиотека и заголовочные файлы для %name-qt
Group:         System/Libraries
Requires:      %name-devel = %version-%release
Requires:      %name-qt = %version-%release

%description -n zint-qt-devel 
C library and header files needed to develop applications using %name-qt.

%description -n zint-qt-devel -l ru_RU.UTF-8
Библиотека C и заголовочные файлы, необходимые для разработки приложений
с помощью %name-qt.

%prep
%setup -q
%patch -p 1
%patch10 -p 1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
install -D -p -m 644 %name.png %buildroot%_datadir/pixmaps/%name.png
install -D -p -m 644 %SOURCE10 %buildroot%_qt5_translationdir/%{name}_ru.qm
desktop-file-install --dir %buildroot%_datadir/applications %name-qt.desktop

%files
%doc COPYING README
%_bindir/%name
%_libdir/libzint.so.*

%files -n %name-devel
%_includedir/%name.h
%_libdir/libzint.so

%files -n %name-qt
%_bindir/%name-qt
%_libdir/libQZint.so.*
%_datadir/applications/%name-qt.desktop
%_datadir/pixmaps/%name.png
%_qt5_translationdir/%{name}_*.qm

%files -n %name-qt-devel
%_includedir/qzint.h
%_libdir/libQZint.so


%changelog
* Tue Jun 29 2021 Ivan Razzhivin <underwit@altlinux.org> 2.8.0-alt2
- Add russian translation

* Thu Jun 24 2021 Ivan Razzhivin <underwit@altlinux.org> 2.8.0-alt1
- New version 2.8.0

* Wed Jun 16 2021 Ivan Razzhivin <underwit@altlinux.org> 2.6.3-alt1
- Initial build
