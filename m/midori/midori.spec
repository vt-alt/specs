%def_disable snapshot

%define api_ver 0.6
%define xdg_name org.midori_browser.Midori

Name: midori
Version: 9.0
Release: alt1

Summary: Midori is a lightweight web browser
License: LGPLv2.1+
Group: Networking/WWW
Url: http://www.midori-browser.org/

%if_disabled snapshot
Source: https://github.com/midori-browser/core/releases/download/v%version/%name-v%version.tar.gz
%else
# VCS: https://github.com/midori-browser/core
Source: %name-%version.tar
%endif

Requires: gcr

BuildRequires(pre): cmake
BuildRequires: gcc-c++ vala-tools intltool libappstream-glib-devel desktop-file-utils xmllint
BuildRequires: libwebkit2gtk-devel libpeas-devel libjson-glib-devel gcr-libs-devel gcr-libs-vala
BuildRequires: libarchive-devel libsoup-gnome-devel libsqlite3-devel
BuildRequires: libwebkit2gtk-gir-devel libpeas-gir-devel

%description
Midori is a lightweight yet powerful web browser which runs just as well
on little embedded computers named for delicious pastries as it does on
beefy machines with a core temperature exceeding that of planet earth.
And it looks good doing that, too. Oh, and of course it's free software.

%prep
%setup -n %name-v%version

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build

%install
%cmakeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_libdir/libmidori-core.so*
%_typelibdir/Midori-%api_ver.typelib
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.appdata.xml
%_iconsdir/hicolor/*/*/*.*
%doc README* CHANGELOG*

%exclude %_girdir/Midori-%api_ver.gir
%exclude %_docdir/%name

%changelog
* Fri Aug 02 2019 Yuri N. Sedunov <aris@altlinux.org> 9.0-alt1
- 9.0

* Sat Mar 02 2019 Yuri N. Sedunov <aris@altlinux.org> 8.0-alt1
- 8.0

* Fri Mar 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.12-alt0.1
- built snapshot from webKitTwoOnly branch

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt1
- 0.5.11

* Mon Dec 09 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5.6-alt1
- 0.5.6
- build with libgranite (Closes: #29341)
- switch to Gtk3
- added ALTLinux package search (Closes: #29342)

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5.5-alt1
- 0.5.5 (Closes: #29301)

* Fri Jul 26 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5.4-alt1
- 0.5.4
- updated url and source (project switched from git to bzr)

* Tue Apr 09 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Thu Feb 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.4.8-alt1
- 0.4.8

* Fri Sep 21 2012 Vladimir Lettiev <crux@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.4.5a-alt1
- 0.4.5a

* Thu Mar 22 2012 Michael Shigorin <mike@altlinux.org> 0.4.4-alt1
- 0.4.4 (thx iZEN for a hint)

* Sun Dec 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Tue Nov 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.2-alt1
- 0.4.2
- dropped patch for incorrectly written protocol

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt2
- rebuild with libwebkitgtk2-1.6.1

* Mon Oct 10 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon Aug 15 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1
- 0.4.0
- added some new search providers as suggested by Mykola Grechukh
  (Closes: #26037)

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 0.3.6-alt2
- devel subpackage disabled by default

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 0.3.6-alt1
- New version 0.3.6

* Mon Mar 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.3-alt1
- New version 0.3.3

* Sun Feb 20 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt1
- New version 0.3.2

* Mon Jan 31 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.0-alt1
- New version 0.3.0

* Tue Jan 11 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.9-alt2
- Fixed case of incorrectly written protocol (same behaviour as
  firefox) (Closes: #24894)

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.9-alt1
- New version 0.2.9

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.8-alt2
- Rebuild with libwebkitgtk2

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.8-alt1
- New version 0.2.8

* Tue Aug 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.7-alt1
- New version 0.2.7

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.6-alt1
- New version 0.2.6

* Tue May 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.5-alt1
- New version 0.2.5 (Closes: #23492)
- Add devel subpackage ('External Applications' extension)

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.4-alt1
- New version 0.2.4

* Fri Mar 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.3-alt1
- New version 0.2.3

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt2
- add missing adblock config
- add libnotify-devel build req

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1
- New version 0.2.2

* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.0-alt1
- New version

* Mon Sep 07 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.9-alt1
- New version

* Tue Jul 21 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.8-alt1
- New version (3201370)

* Wed Jun 17 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.7-alt1
- New version
- build user docs

* Sat May 02 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.6-alt1
- New version
- removed patch0

* Tue Apr 07 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.5-alt1
- New version

* Wed Jan 28 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt2
- Fix build on x86_64

* Mon Jan 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt1
- New version
- Fix TEXTREL in extensions

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 0.0.21-alt1
- New version

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 0.0.20-alt1
- Initial build for Sisyphus



