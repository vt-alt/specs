%define gst_api_ver 1.0

Name: clementine
Version: 1.3.1
Release: alt8.git88131ec5
Summary: A music player and library organiser

Group: Sound
License: %lgpl3only
Url: https://www.clementine-player.org/

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: boost-devel-headers gcc-c++
BuildRequires: libgio-devel libglew-devel libgpod-devel liblastfm-devel libmtp-devel
BuildRequires: libqt5-opengl libqt5-sql libqt5-webkit libqt5-xmlpatterns qt5-x11extras-devel
BuildRequires: libtag-devel
BuildRequires: gstreamer%{gst_api_ver}-devel gst-plugins%gst_api_ver-devel gstreamer%gst_api_ver-utils
BuildRequires: libchromaprint-devel
BuildRequires: libcryptopp-devel >= 6
# SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER is available since 3.12
BuildRequires: libsqlite3-devel >= 3.12
BuildRequires: libpulseaudio-devel

BuildRequires: qt5-sql-sqlite3 protobuf-compiler
# Enable Google Drive support
BuildRequires: libgoogle-sparsehash
BuildPreReq: libavcodec-devel libavformat-devel libpcre-devel
BuildPreReq: libprotobuf-devel qjson-qt5-devel libcdio-devel

# Clementine crashes without it
Requires: gst-plugins-base%{gst_api_ver}

%description
Clementine is a modern music player and library organizer

%add_python_req_skip clementine

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc Changelog
%_bindir/clementine
%_bindir/clementine-tagreader
%_desktopdir/clementine.desktop
%_datadir/kservices5/*.protocol
%_datadir/clementine
%_datadir/metainfo/clementine.appdata.xml
%_datadir/icons/hicolor/*/apps/*.png
%_datadir/icons/hicolor/*/apps/*.svg


%changelog
* Wed Sep 25 2019 Vladimir Didenko <cow@altlinux.org> 1.3.1-alt8.git88131ec5
- Update to the lastest qt5 snapshot (closes: #37261)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt7.1
- NMU: autorebuild with libcryptopp.so.7

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt7
- NMU: autorebuild with libcryptopp-6.1.0

* Wed Feb 21 2018 Vladimir Didenko <cow@altlinux.org> 1.3.1-alt6
- fix build with gcc7

* Fri Jan 12 2018 Vladimir Didenko <cow@altlinux.org> 1.3.1-alt5
- rebuild with new libcdio

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt4.1
- NMU: autorebuild with libcryptopp-5.6.5

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt4
- apply fix build with chromaprint >= 1.4

* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt3
- Fix build with gcc-6

* Tue Dec 27 2016 Vladimir Didenko <cow@altlinux.org> 1.3.1-alt2
- Disable vkontakte support (dropped by vk.com)

* Sat Apr 23 2016 Vladimir Didenko <cow@altlinux.org> 1.3.1-alt1
- Version 1.3.1
- Enable FTS3 at runtime (closes: #31978)

* Thu Feb 4 2016 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1.rc1
- Version 1.3rc1

* Wed Aug 5 2015 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt5
- rebuilt with new libcdio

* Tue Jul 7 2015 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt4
- git20150522
- build with gstreamer1.0

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.3-alt3.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Feb 12 2015 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt3
- add gst-plugins-base to requires - clementine crashes without it

* Mon Jul 7 2014 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt2
- add vkontakte support (closes: #29522)

* Mon May 19 2014 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Mon Feb 24 2014 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Fri Dec 13 2013 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Wed Oct 17 2013 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Wed Oct 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1-alt4
- Fixed build with new libav.

* Wed Apr 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt3
- rebuilt against libimobiledevice.so.4

* Sat Jan 12 2013 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt2
- Enable Google Drive support

* Fri Dec 28 2012 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2.qa2
- Removed -Werror compiler flag
- Fixed build with new glib2

* Mon May 30 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2.qa1
- Rebuild for GNOME 3

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2
- Fix patch name

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- New version 0.7.1

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1.svn2877.qa1
- Fix build in Sisyphus (remove nvidia_glx requires)

* Sat Feb 26 2011 Pavel Maleev <rolland@altlinux.org> 0.6-alt1.svn2877
- new version (svn2877)

* Sun Nov 21 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2253
- new version (svn2253)

* Mon Oct 25 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2205
- new version (svn2205)

* Sun Oct 3 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2086
- new version (svn2086)

* Tue Sep 21 2010 Pavel Maleev <rolland@altlinux.org> 0.5-alt1.svn2034
- new version (svn2034)

* Mon Aug 9 2010 Pavel Maleev <rolland@altlinux.org> 0.4-alt1.svn1664
- new version (svn1664)

* Thu Jul 15 2010 Pavel Maleev <rolland@altlinux.org> 0.4-alt1.svn1480
- new version (svn1480)

* Tue Jun 29 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn1386
- new version (svn1093)

* Wed Jun 09 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn1093
- new version (svn1093)

* Sat May 22 2010 Pavel Maleev <rolland@altlinux.org> 0.3-alt1.svn952
- new version (svn952)

* Tue Apr 13 2010 Pavel Maleev <rolland@altlinux.org> 0.2-alt1.svn673
- new version (svn673)

* Tue Apr 06 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.svn586
- new version (svn586)

* Wed Mar 24 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.svn479
- new version (svn479)

* Sun Mar 14 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.svn370
- new version (svn370)
- fix previous changelog entry (changelog author)

* Sun Mar 01 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.svn285
- initial build for ALT Linux Sisyphus (svn285)
