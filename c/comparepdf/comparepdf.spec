Name: comparepdf
Version: 1.0.1
Release: alt3
License: GPLv2
Summary: Compare two PDF files
Group: Publishing
Url: http://www.qtrac.eu/comparepdf.html
Source: %name-%version.tar.gz
Patch1: alt-qt5.patch

# /*G*/ Can't be found by findreq :(
#BuildRequires:	libpoppler-cpp-devel

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: fontconfig libpoppler3-qt4 libqt4-core libqt4-devel libqt4-gui libqt4-xml libstdc++-devel
BuildRequires: qt5-base-devel libpoppler-qt5-devel

%description
The default comparison mode is text mode where the text of each
corresponding pair of pages is compared. As soon as a difference is
detected the program terminates with a message (unless -v0 is set) and
an indicative return code.

%prep
%setup
%patch1 -p1

%build
%qmake_qt5
%make

%install
install -D %name %buildroot%_bindir/%name
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt3
- Port to Qt5

* Tue Apr 09 2013 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Rebuild with new libpoppler

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1
- BuildRequires fix

* Tue Oct 11 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from scratch

