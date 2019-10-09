%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%define rdn_name net.poedit.Poedit

%def_with cpprest
%def_without cld2

Name: poedit
Version: 2.2.4
Release: alt1

Summary: Cross-platform translation files editor
Summary(ru_RU.UTF-8): Кроссплатформенный редактор файлов переводов
Group: Editors
License: MIT
Url: http://www.poedit.net/

%if_disabled snapshot
Source: https://github.com/vslavik/%name/releases/download/v%version-oss/%name-%version.tar.gz
%else
# VCS: https://github.com/vslavik/poedit.git
Source: %name-%version.tar
%endif
Requires: gettext-tools

%define cpprest_ver 2.5
%define wxgtk_ver 3.0.3-alt9
%define boost_ver 1.60

Requires: libwxGTK3.0 >= %wxgtk_ver

BuildPreReq: desktop-file-utils libappstream-glib-devel
BuildRequires: gcc-c++ libwxGTK3.0-devel >= %wxgtk_ver libdb4_cxx-devel libgtkspell3-devel
BuildRequires: libicu-devel liblucene++-devel libpugixml-devel
BuildRequires: boost-locale-devel >= %boost_ver zlib-devel
%{?_with_cpprest:BuildRequires: libcpprest-devel >= %cpprest_ver libsecret-devel}
%{?_with_cld2:BuildRequires: libcld2-devel}

%description
This program is GUI frontend to GNU Gettext utilities and catalogs
editor/source code parser. It helps with translating application into
another language. For details on principles of the solution used, see
GNU Gettext documentation or wxWindows' wxLocale class reference.

%description -l ru_RU.UTF-8
Эта программа является оболочкой для утилит GNU Gettext. С её помощью
удобно переводить сообщения приложений на разные языки. Более подробно
принципы работы описаны в документации для GNU Gettext и класса
wxLocale библиотеки wxWindows.

%prep
%setup

%build
%configure \
	%{subst_with cpprest} \
	%{subst_with cld2}
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_desktopdir/net.poedit.PoeditURI.desktop
%_iconsdir/hicolor/*x*/*/*.png
%_datadir/metainfo/%rdn_name.appdata.xml

%changelog
* Mon Sep 30 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Tue Jan 15 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- 2.2

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt2
- rebuilt with openssl-1.1

* Sun Jul 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt2
- rebuilt against libicu*.so.62

* Tue Jul 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- 2.1

* Thu Jul 12 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.9-alt1
- 2.0.9

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.8-alt1
- 2.0.8

* Fri Jun 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt2
- rebuilt with boost-1.67

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Wed Apr 18 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.6-alt2
- rebuilt with boost-1.66

* Fri Jan 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.6-alt1
- 2.0.6 with cpprest support

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Tue Sep 26 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Thu Aug 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.0.3-alt1.1
- Rebuilt for changed libwxGTK3.0 ABI

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Wed May 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.12-alt1
- 1.8.12

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.11-alt2
- rebuilt with new boost-1.63

* Sat Oct 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.11-alt1
- 1.8.11

* Wed Sep 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.9-alt1
- 1.8.9

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.8-alt1
- 1.8.8

* Sat Mar 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.7.1-alt1
- 1.8.7.1

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.7-alt1
- 1.8.7

* Thu Jan 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.6-alt1
- 1.8.6

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4.6.1-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 05 2010 Slava Semushin <php-coder@altlinux.ru> 1.4.6.1-alt2
- Added gettext-tools to Requires (Closes: #24017)

* Sun May 23 2010 Slava Semushin <php-coder@altlinux.ru> 1.4.6.1-alt1
- Updated to 1.4.6.1

* Wed Feb 10 2010 Slava Semushin <php-coder@altlinux.ru> 1.4.5-alt1
- Updated to 1.4.5

* Sun Sep 20 2009 Slava Semushin <php-coder@altlinux.ru> 1.4.3-alt1
- Updated to 1.4.3
- Fixed Exec entry in desktop file (noted by repocop)

* Wed Aug 26 2009 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt4
- Rebuild (again) with wxGTK to fix crash after start (Closes: #21187)

* Sat Aug 22 2009 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt3
- Rebuild with wxGTK to fix crash after start (Closes: #21187)

* Sat Dec 13 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt2
- Partially fixed desktop file (noted by repocop)
- Removed obsolete %%update_menus/%%update_desktopdb calls (noted by repocop)

* Mon Sep 08 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt1
- Updated to 1.4.2

* Thu Jun 19 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.1-alt2
- Rebuilt with libdb4.7

* Wed Apr 09 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.1-alt1
- Updated to 1.4.1 version

* Thu Mar 13 2008 Slava Semushin <php-coder@altlinux.ru> 1.4-alt1
- Updated to 1.4 version
- Removed desktop-file-utils from post and postun Requires
- Running make with --no-print-directory and --silent options

* Wed Dec 19 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.9-alt1
- Updated to 1.3.9 version (bugfix release for MacOS X)

* Tue Dec 11 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.8-alt1
- Updated to 1.3.8 version

* Sat Oct 20 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.7-alt2
- Rebuilt with wxWidgets 2.8
- Really updated Url tag

* Sat Jul 21 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.7-alt1
- Updated to 1.3.7 version
- Updated Url tag
- Spec cleanup:
  + s/%%setup -q/%%setup/
  + Removed trailing space in %%changelog

* Tue Jan 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3.6-alt1.1
- NMU based on php-coder@ spec.

* Tue Jan 16 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.6-alt1
- 1.3.6 (bugfix release)

* Fri Oct 06 2006 Slava Semushin <php-coder@altlinux.ru> 1.3.5-alt3
- Changed Group to Editors

* Thu Oct 05 2006 Slava Semushin <php-coder@altlinux.ru> 1.3.5-alt2
- Rebuilt with libdb4.4 again
  (during updates BuildRequires I revert libdb back to 4.3)

* Wed Sep 27 2006 Slava Semushin <php-coder@altlinux.ru> 1.3.5-alt1
- 1.3.5
- New maintainer
- Fixed #8255 (sources of libexpat removed from program in upstream)
- Fixed #9159
  + Converted Summary and %%description to CP1251 charset
  + Updated Url
  + Changed License to MIT
  + Removed no_desktop_menus.patch
  + Removed menu-file
- Updated BuildRequires
- Formatted %%description
- Added full url to Source tag
- More strict names in %%files section
- Enable _unpackaged_files_terminate_build
- Using macros %%make_install instead of %%makeinstall
- Using %%{update,clean}_desktopdb for registry MimeType

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.4-alt1.1
- Rebuilt with libdb4.4.

* Thu Dec 01 2005 Andrey Astafiev <andrei@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Mon Apr 18 2005 Andrey Astafiev <andrei@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 1.3.1-alt2
- Rebuilt with unicode support.

* Fri Nov 05 2004 Andrey Astafiev <andrei@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sun Feb 29 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Wed Nov 05 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Fri Jun 20 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.2-alt2
- Rebuilt with new wxGTK.

* Mon May 19 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Wed Apr 23 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.1-alt3
- Fixed Group tag.

* Wed Mar 12 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.1-alt2
- Now builds in Gnome and KDE environment.

* Fri Mar 07 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.1-alt1
- First version of RPM package.
