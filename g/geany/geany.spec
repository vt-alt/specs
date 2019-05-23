# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: geany
Version: 1.35
Release: alt1

Summary: A fast and lightweight IDE using GTK2
License: GPLv2
Group: Development/Tools
Url: http://geany.org

Source: %name-%version.tar.bz2

Requires: libvte
Requires: %name-data = %version
BuildPreReq: desktop-file-utils
# Automatically added by buildreq on Tue Jul 05 2016
# optimized out: fontconfig fontconfig-devel glib2-devel gnu-config libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel libstdc++-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config python-base python-devel python-module-lxml python-modules python-modules-compiler python-modules-encodings xorg-xproto-devel
BuildRequires: gcc-c++ intltool libgtk+2-devel python-module-docutils time

%add_findreq_skiplist %_datadir/%name/templates/files/*

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages. Another goal was to be as
independent as possible from a special Desktop Environment like KDE or
GNOME. So it is using only the GTK2 toolkit and therefore you need
only the GTK2 runtime libraries to run Geany.

%package data
Summary: Data files for Geany IDE
Group: Development/Tools
BuildArch: noarch
Requires: %name = %version

%description data
Architecture-independent data files for Geany IDE.

%package devel
Summary: Header files for building Geany plug-ins
Group: Development/C
Requires: %name = %version

%description devel
This package contains the header files and pkg-config file needed for
building Geany plug-ins. You do not need to install this package to
use Geany.

%prep
%setup

# hack out space in file name
sed -i '/"untitled"/,/^$/s/\([^a-z]\) \([^a-z]\)/\1_\2/g' po/ru.po

# Add some hello world examples
# C++
cat > data/templates/files/hello_world.cpp <<@@@
{fileheader}

#include <iostream>

int main(int argc, char **argv)
{
	std::cout << "Hello world!\n";
	return 0;
}
@@@

# Basic
cat > data/templates/files/hello_world.bas <<@@@
{fileheader}
PRINT "Hello World!"
SLEEP
@@@

# Pascal
cat > data/templates/files/hello_world.pas <<@@@
{fileheader}

program Hello;
begin
  writeln ('Hello, world!');
end.
@@@

%build
NOCONFIGURE=1 ./autogen.sh

%configure --docdir=%_defaultdocdir/%name-%version --enable-html-docs

%make_build --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name
bzip2 %buildroot%_defaultdocdir/%name-%version/ChangeLog

%check
%make check

%files
%_bindir/%name
%_libdir/%name/
%_libdir/*.so.*

%files -f %name.lang data
%_datadir/%name/
%_man1dir/%name.1.*
%_desktopdir/%name.desktop
%_iconsdir/*/*/*/*
%_defaultdocdir/%name-%version/

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_libdir/*.so

%changelog
* Wed May 22 2019 Fr. Br. George <george@altlinux.ru> 1.35-alt1
- Autobuild version bump to 1.35

* Wed Feb 27 2019 Fr. Br. George <george@altlinux.ru> 1.34.1-alt1
- Autobuild version bump to 1.34.1

* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 1.33-alt1
- Autobuild version bump to 1.33

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.32-alt1
- Autobuild version bump to 1.32

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 1.31-alt1
- Autobuild version bump to 1.31

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 1.30.1-alt1
- Autobuild version bump to 1.30.1

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.30-alt1
- Autobuild version bump to 1.30

* Wed Dec 21 2016 Fr. Br. George <george@altlinux.ru> 1.29-alt1
- Autobuild version bump to 1.29

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 1.28-alt1
- Autobuild version bump to 1.28

* Tue Jul 05 2016 Fr. Br. George <george@altlinux.ru> 1.27-alt1
- Autobuild version bump to 1.27
- Build documentation

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.24.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.24.1-alt1
- Autobuild version bump to 1.24.1

* Wed Sep 04 2013 Fr. Br. George <george@altlinux.ru> 1.23.1-alt2
- Add helloworlds and fix space in filemane (Closes: #29297)

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 1.23.1-alt1
- Autobuild version bump to 1.23.1

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 1.23-alt1
- Autobuild version bump to 1.23
- Package additional icons

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 1.22-alt1
- Autobuild version bump to 1.22

* Mon May 21 2012 Fr. Br. George <george@altlinux.ru> 0.21-alt2
- DSO linking (@glebfm)

* Tue Oct 04 2011 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Autobuild version bump to 0.21

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20

* Mon Dec 27 2010 Fr. Br. George <george@altlinux.ru> 0.19.2-alt0.M50P.1
- Rebuild for P5 (release fixed)

* Mon Dec 27 2010 Fr. Br. George <george@altlinux.ru> 0.19.2-alt0.M50p.1
- Rebuild for P5

* Fri Dec 24 2010 Fr. Br. George <george@altlinux.ru> 0.19.2-alt1
- Autobuild version bump to 0.19.2

* Mon Jul 19 2010 Fr. Br. George <george@altlinux.ru> 0.19-alt1
- Version up

* Mon Aug 17 2009 Slava Semushin <php-coder@altlinux.ru> 0.18-alt1
- Updated to 0.18
- Updated Summary and %%description of geany-devel subpackage

* Sun May 03 2009 Slava Semushin <php-coder@altlinux.ru> 0.17-alt1
- Updated to 0.17

* Sat Apr 11 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt3
- Introduced -devel subpackage with files needed to build external
  plugins

* Thu Mar 26 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt2
- Compress ChangeLog (noted by repocop)

* Fri Feb 20 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt1
- Updated to 0.16

* Tue Dec 09 2008 Slava Semushin <php-coder@altlinux.ru> 0.15-alt2
- Moved data files to separated geany-data subpackage (noted by repocop)
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- Removed obsolete %%update_desktopdb/%%clean_desktopdb calls (noted by repocop)
- Changed Group to "Development/Tools"
- More proper License tag

* Mon Oct 20 2008 Slava Semushin <php-coder@altlinux.ru> 0.15-alt1
- Updated to 0.15
- New home page

* Sun Apr 27 2008 Slava Semushin <php-coder@altlinux.ru> 0.14-alt1
- Updated to 0.14 (deb #478126)
- Open local installed HTML documentation when user press F1
- Don't package headers and pkgconfig file
- Replace %%__autoreconf macros to %%autoreconf

* Thu Feb 07 2008 Slava Semushin <php-coder@altlinux.ru> 0.13-alt1
- Updated to 0.13

* Fri Oct 12 2007 Slava Semushin <php-coder@altlinux.ru> 0.12-alt1
- Updated to 0.12
- Don't force -Os gcc optimization for Scintilla (idea from OpenBSD)
- Don't specify full path and extension for Icon tag in desktop file
- Call %%{update,clean}_desktopdb in %%post/%%postun
- More strict Requires

* Sat May 26 2007 Slava Semushin <php-coder@altlinux.ru> 0.11-alt1
- Updated to 0.11
- Call %%update_menus/%%clean_menus in %%post/%%postun
- Removed find_svn_silently patch (applied by upstream)
- Imported into git and built with gear

* Mon Feb 26 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10.2-alt1.1
- NMU based on spec from Slava Semushin <php-coder@>

* Mon Feb 26 2007 Slava Semushin <php-coder@altlinux.ru> 0.10.2-alt1
- Updated to 0.10.2 (bugfix release)
- Removed find_libvte_correctly patch (was backported from svn)

* Thu Feb 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10-alt1.1
- Adapted spec from Slava Semushin <php-coder@>

* Thu Feb 08 2007 Slava Semushin <php-coder@altlinux.ru> 0.10-alt1
- Initial build for ALT Linux Sisyphus
- Applied two patches:
  + find_libvte_correctly (backported from SVN)
  + find_svn_silently (maded by me)

