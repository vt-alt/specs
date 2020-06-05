Name: boomaga
Version: 3.0.0
Release: alt1.1
Group: System/Configuration/Printing
License: GPLv2 and LGPLv2+

Summary: A virtual printer for viewing a document before printing
Url: http://boomaga.github.io/
# Source: https://github.com/Boomaga/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch1: boomaga-alt-workaround-for-ALT_38564.patch
BuildRequires: cmake libcups-devel libpoppler-cpp-devel qt5-tools-devel zlib-devel

Requires(pre): ghostscript
Requires(pre): a2ps
Requires(pre): cups
Requires(pre): cups-filters
Requires(pre): foomatic-db
Requires: libsnappy
Requires(preun): cups-common
Requires(post): libpaper

%description
Boomaga (BOOklet MAnager) is a virtual printer for viewing a document
before printing it out using the physical printer. The program is very
simple to work with. Running any program, click "print" and select
"Boomaga" to see in several seconds (CUPS takes some time to respond)
the Boomaga window open. If you print out one more document,
it gets added to the previous one, and you can also print them
out as one. Regardless of whether your printer supports duplex
printing or not, you would be able to easily print on both sides
of the sheet. If your printer does not support duplex printing,
point this out in the settings, and Booklet would ask you to turn
over the pages half way through printing your document.

The program can also help you get your documents prepared a bit
before printing. At this stage Boomaga makes it possible to:

 * Paste several documents together.
 * Print several pages on one sheet.
 * 1, 2, 4, 8 pages per sheet
 * Booklet. Folding the sheets in two, you'll get a book.

%prep
%setup
%patch1 -p2

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_datadir/%name/scripts
install -m 755 scripts/installPrinter.sh %buildroot%_datadir/%name/scripts/
chmod +x %buildroot%_datadir/%name/scripts/installPrinter.sh
mkdir -p %buildroot%_cachedir/%name

%find_lang %name

%pre
/sbin/service cups condrestart ||:

%post
# Install the printer to cups backends
if [ $1 = 1 ]; then
    sh %_datadir/%name/scripts/installPrinter.sh
fi

%preun
# Uninstall the printer
lpadmin -x "Boomaga" || :

%files -f %name.lang
%dir %_datadir/%name
%dir %_datadir/%name/scripts
%dir %_datadir/%name/translations
%_bindir/%name
%attr(700,root,root) %_prefix/lib/cups/backend/%name
%dir %_cachedir/%name
%_datadir/dbus-1/services/org.%name.service
%_man1dir/%name.1.xz
%_datadir/ppd/%name/
%_datadir/%name/scripts/installPrinter.sh
%_desktopdir/boomaga.desktop
%_iconsdir/hicolor/*/apps/boomaga.png
%_datadir/mime/packages/boomaga.xml
%_datadir/%name/translations/*.qm

%changelog
* Sun May 31 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- FTBFS: fix build by strictly set DEF_CUPS_BACKEND_DIR (see ALT bug 38564)

* Mon May 20 2019 Oleg Solovyov <mcpain@altlinux.org> 3.0.0-alt1
- version 3.0.0 (Closes ALT#36748)

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.3.0-alt1
- Initial build for ALT

