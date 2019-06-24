Name: qfsm
Version: 0.54.0
Release: alt2

Summary: Graphical tool for designing finite state machine
License: GPL
Group: Education

Url: http://qfsm.sourceforge.net/
Source: %name-%version-Source.tar.bz2
Patch: %name.desktop.patch
Patch1: qfsm-0.54.0-NULL.patch

# Automatically added by buildreq on Thu Jul 26 2012
# optimized out: cmake-modules fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel pkg-config
BuildRequires: cmake gcc-c++ phonon-devel

# cgraph change
#BuildRequires: libgraphviz-devel < 2.30.0

%description
Qfsm is a graphical tool for designing finite state machine.
It is written in C++ using the Qt library.
Features include:

- Drawing, Editing and Printing of states diagrams
- Binary, ASCII or "free text" condition codes
- Multiple windows
- Integrity check
- Interactive simulation
- HDL export in the file formats: AHDL, VHDL, Verilog HDL, KISS
- Diagram export in the formats: EPS and SVG
- State table export in Latex, HTML or plain text format
- Ragel file export (used for C/C++, Java or Ruby code generation)

%prep
%setup -n %name-%version-Source
%patch -p0
%patch1 -p1

# needs porting to cgraph: https://sourceforge.net/p/qfsm/feature-requests/12/
sed -i 's, \${graphviz_[A-Z]*_LIBRARY},,g' CMakeLists.txt

%build
cmake .
%make_build

%install
%makeinstall_std
#mkdir -p %buildroot/usr/
#make package
#cp -rp _CPack_Packages/Linux/TGZ/qfsm-0.51.0-Linux/* %buildroot/usr/
rm -rf %buildroot%_defaultdocdir/%name
ln -s %name-%version/user %buildroot%_defaultdocdir/%name
%find_lang %name

%files -f %name.lang
%doc README TODO
%doc doc/user doc/html examples
%_bindir/%name
%_defaultdocdir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/*.desktop
%_datadir/mimelnk/application/*.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Wed Jun 19 2019 Fr. Br. George <george@altlinux.ru> 0.54.0-alt2
- Fix build

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.54.0-alt1
- Autobuild version bump to 0.54.0

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 0.53.0-alt1.1
- NMU: rebuilt without graphviz (cgraph support missing)

* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 0.53.0-alt1
- Autobuild version bump to 0.53.0

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 0.52.0-alt2
- Fix repocop warnings

* Wed Apr 28 2010 Fr. Br. George <george@altlinux.ru> 0.52.0-alt1
- Version up
- Desktop file fixes
- Use find_lang for .po files

* Mon Mar 30 2009 Fr. Br. George <george@altlinux.ru> 0.51.0-alt1
- Version up

* Mon Oct 15 2007 Fr. Br. George <george@altlinux.ru> 0.45-alt1
- Initial build for ALT
