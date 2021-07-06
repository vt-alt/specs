Name:    ktechlab
Version: 0.50.0
Release: alt1

Summary: Development and simulation of micro-controllers and electronic circuits
License: GPL-2.0
Group:   Engineering

URL: https://github.com/ktechlab/ktechlab
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-ninja
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-khtml-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjs-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel
BuildRequires: glib2-devel
BuildRequires: libgpsim-devel
BuildRequires: readline-devel
BuildRequires: desktop-file-utils

# Ktechlab requires gputils for PIC simulation.
Requires: gputils sdcc

%description
KTechlab is a development and simulation environment for
micro-controllers and electronic circuits. KTechlab consists of several
well-integrated components: A circuit simulator, capable of simulating
logic, linear devices and some nonlinear devices. Integration with
gpsim, allowing PICs to be simulated in circuit. A schematic editor,
which provides a rich real-time feedback of the simulation. A flowchart
editor, allowing PIC programs to be constructed visually. MicroBASIC; a
BASIC-like compiler for PICs, written as a companion program to
KTechlab. An embedded Kate part, which provides a powerful editor for
PIC programs. Integrated assembler and disassembler via gpasm and
gpdasm.

%prep
%setup

%build
%K5init no_altplace
%K5cmake -GNinja
%ninja_build -C BUILD
# TODO
echo "Comment[ru]=Среда разработки микроконтроллеров и электронных компонентов" >> src/org.kde.ktechlab.desktop

%install
%ninja_install -C BUILD
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README
%doc %_K5doc/en/%name
%_bindir/%name
%_bindir/microbe
%_datadir/%name
%_K5xmlgui/%name
%_datadir/metainfo/*.xml
%_K5xdgmime/*.xml
%_K5cfg/%name.kcfg
%_datadir/katepart5/syntax/microbe.xml
%_desktopdir/kf5/*.desktop
%_iconsdir/hicolor/*/*/*.png

%changelog
* Thu Jul 01 2021 Andrey Cherepanov <cas@altlinux.org> 0.50.0-alt1
- Ressurection of the package (ALT #40340).
- Fix upstream URL and License tag.

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt4.20090304
- rebuilt against gcc5-built qt3

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt3.20090304
- Rebuild with new verison of gpsim

* Thu Feb 12 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt2.20090304
- Fix desktop file and its icon

* Wed Feb 11 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt1.20090304
- Build in Sisyphus from Fedora
