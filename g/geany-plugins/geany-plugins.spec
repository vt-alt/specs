Name: geany-plugins
Version: 1.35
Release: alt1
%define geany_ver %version

Summary: Plugins for Geany

License: GPLv2
Group: Development/Tools
Url: http://plugins.geany.org/

Source: %name-%version.tar.bz2

BuildRequires(pre): geany geany-devel intltool
# Hack out self-providing symbols
%add_python_req_skip app
%add_python_req_skip dialogs
%add_python_req_skip document
%add_python_req_skip encoding
%add_python_req_skip filetypes
%add_python_req_skip glog
%add_python_req_skip highlighting
%add_python_req_skip keybindings
%add_python_req_skip main
%add_python_req_skip msgwindow
%add_python_req_skip navqueue
%add_python_req_skip prefs
%add_python_req_skip project
%add_python_req_skip scintilla
%add_python_req_skip search
%add_python_req_skip ui_utils
%add_python_req_skip templates

Requires: geany-plugins-vc

# Automatically added by buildreq on Wed Feb 27 2019
# optimized out: fontconfig fontconfig-devel geany glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXext-devel libatk-devel libcairo-devel libcrypt-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgpg-error-devel libgtk+2-devel libjavascriptcoregtk2-devel liblua5.1-devel libpango-devel libsoup-devel perl perl-XML-Parser pkg-config python-base python-devel python-module-docutils python-module-pygobject-devel python-modules python-modules-distutils sh4 vala xorg-proto-devel zlib-devel
BuildRequires: cppcheck geany-devel intltool libGConf-devel libcheck-devel libenchant-devel libgit2-devel libgpgme-devel libgtkspell-devel libvte-devel libwebkitgtk2-devel libwnck-devel libxml2-devel python-module-pygtk-devel libctpl-devel

BuildRequires: liblua5.1-devel

%description
This is Geany plugin collection

%package common
Group: Development/Tools
Requires: geany = %geany_ver
Summary: Localization and other platform independent stuff of geany-plugins
BuildArch: noarch

%description common
Common files of geany-plugins, including localization

%package vc
Group: Development/Tools
Requires: geany-plugins-common = %version-%release
Summary: Geany VC integration plugin

%description vc
Various VCS integration (Git, SVN, ...) for Geany

%prep
%setup
sed -i '/^geanyluadir/s@.*@geanyluadir = %_libdir/geany@' geanylua/Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name

%files
%doc %_defaultdocdir/%name
%_libdir/geany/*
%_libdir/lib*
%_datadir/geany-plugins/*
#dir #_libexecdir/geany-plugins
#_libexecdir/geany-plugins/*
#_iconsdir/hicolor/*/apps/*
%exclude %_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la
#exclude %_libdir/geany-plugins/*/*.la

%files common -f %name.lang
%files vc
%_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la

%changelog
* Wed May 22 2019 Fr. Br. George <george@altlinux.ru> 1.35-alt1
- Autobuild version bump to 1.35

* Wed Feb 27 2019 Fr. Br. George <george@altlinux.ru> 1.34.1-alt0.1
- Autobuild version bump to 1.34
- Build with Geany 1.34.1

* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 1.33-alt1
- Autobuild version bump to 1.33

* Tue Sep 26 2017 Fr. Br. George <george@altlinux.ru> 1.31-alt2
- Rebuild with new libgit2

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 1.31-alt1
- Autobuild version bump to 1.31

* Fri Mar 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.30-alt1.1
- rebuilt against libgit2.so.25

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.30-alt1
- Autobuild version bump to 1.30

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1.1
- NMU: rebuild with new lua

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 1.28-alt1
- Autobuild version bump to 1.28

* Tue Jul 05 2016 Fr. Br. George <george@altlinux.ru> 1.27-alt1
- Autobuild version bump to 1.27
- Build additional modules

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.24-alt1
- Autobuild version bump to 1.24

* Thu May 23 2013 Fr. Br. George <george@altlinux.ru> 1.23-alt2
- Rebuild with geany 1.23.1

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 1.23-alt1
- Autobuild version bump to 1.23
- GDB and noarch plugins vanished

* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 1.22-alt1
- Autobuild version bump to 1.22
- Update BuildRequires for more plugins to build

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt2
- Remove release dependency

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt1
- Autobuild version bump to 0.21.1

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
- Add unpackaged files

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt4
- trying to fix build

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt3
- split by plugins

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt2
- first build for ALT Linux
