Name: wxMaxima
Version: 21.01.0
Release: alt1

Summary: GUI for the computer algebra system Maxima
License: GPL-2.0+
Group: Sciences/Mathematics

Url: https://wxmaxima-developers.github.io/wxmaxima
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source5: wxmaxima-ru.po.bz2
Patch:   %name-alt-help-path.patch

Requires: maxima

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ libwxGTK3.1-devel libpango-devel libxml2-devel zlib-devel makeinfo
BuildRequires: po4a doxygen
BuildRequires: libgomp-devel
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: ccache

ExclusiveArch: %ix86 x86_64 armh aarch64 %e2k

Provides: wxmaxima = %EVR
Obsoletes: wxmaxima < %EVR

%description
wxMaxima is a wxWidgets GUI for the computer algebra system Maxima.

Since it is written with wxWidgets, it runs on multiple platforms
in native widget sets.  Most of maxima functions are accessible through
menus, some have dialogs.  The input line has command history (up-key,
down-key) and completion based on previous input (tab-key).
wxMaxima provides 2d formated display of maxima output.


%prep
%setup
bzcat %SOURCE5 >locales/wxMaxima/ru.po
#patch -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.h' | xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%cmake -GNinja
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
# icons
install -pD -m644 data/wxmaxima-16.xpm %buildroot%_miconsdir/%name.xpm
install -pD -m644 data/wxmaxima-32.xpm %buildroot%_niconsdir/%name.xpm
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS.md README.md
%_bindir/wxmaxima
%_desktopdir/*%name.desktop
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/*wxMaxima.appdata.xml
%_datadir/bash-completion/completions/wxmaxima
%_datadir/pixmaps/wxmaxima*
%_datadir/pixmaps/*wxma*svg
%_datadir/mime/packages/x-wxmathml.xml
%_datadir/mime/packages/x-wxmaxima-batch.xml
%_docdir/wxmaxima/
%_man1dir/wxmaxima.1*
%_mandir/de/man1/wxmaxima.1*
%_pixmapsdir/*%name.png

%changelog
* Sun Jan 24 2021 Andrey Cherepanov <cas@altlinux.org> 21.01.0-alt1
- New version.

* Fri Jan 01 2021 Andrey Cherepanov <cas@altlinux.org> 20.12.2-alt1
- New version.

* Tue Dec 29 2020 Andrey Cherepanov <cas@altlinux.org> 20.12.1-alt1
- New version.

* Mon Dec 28 2020 Andrey Cherepanov <cas@altlinux.org> 20.12.0-alt1
- New version.

* Sun Nov 22 2020 Andrey Cherepanov <cas@altlinux.org> 20.11.1-alt1
- New version.

* Tue Nov 03 2020 Andrey Cherepanov <cas@altlinux.org> 20.11.0-alt1
- New version.

* Sun Sep 13 2020 Andrey Cherepanov <cas@altlinux.org> 20.09.0-alt1
- New version.

* Tue Jul 28 2020 Andrey Cherepanov <cas@altlinux.org> 20.07.0-alt1
- New version.
- Complete Russian translations (thanks Olesya Gerasimenko).

* Sat Jun 20 2020 Andrey Cherepanov <cas@altlinux.org> 20.06.6-alt1
- New version.
- Add optional requirements.
- Build by ninja-build.
- Build with wxGTK3.1.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 20.06.1-alt1
- New version.

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 20.04.0-alt1
- New version.

* Mon Mar 23 2020 Andrey Cherepanov <cas@altlinux.org> 20.03.1-alt1
- New version.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 20.03.0-alt1
- New version.

* Tue Feb 25 2020 Andrey Cherepanov <cas@altlinux.org> 20.02.4-alt1
- New version.

* Fri Feb 14 2020 Andrey Cherepanov <cas@altlinux.org> 20.02.1-alt1
- New version.
- Complete Russian translations (thanks Olesya Gerasimenko).

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 20.02.0-alt1
- New version.

* Mon Jan 13 2020 Andrey Cherepanov <cas@altlinux.org> 20.01.2-alt1
- New version.
- Complete Russian translations (thanks Olesya Gerasimenko).

* Thu Jan 02 2020 Andrey Cherepanov <cas@altlinux.org> 20.01.1-alt1
- New version.

* Sun Dec 29 2019 Andrey Cherepanov <cas@altlinux.org> 19.12.4-alt1
- New version.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 19.12.2-alt1
- New version.
- Provides wxmaxima.
- Complete Russian translations (thanks Olesya Gerasimenko).

* Wed Dec 11 2019 Andrey Cherepanov <cas@altlinux.org> 19.12.1-alt1
- New version.

* Wed Dec 04 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.12.0-alt2
- add armh to exclusive arches, there is nothing exclusive about it

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 19.12.0-alt1
- New version.
- Fix license according to SPDX.

* Thu Nov 14 2019 Andrey Cherepanov <cas@altlinux.org> 19.11.0-alt1
- New version.

* Sun Oct 13 2019 Andrey Cherepanov <cas@altlinux.org> 19.10.0-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 19.09.1-alt1
- New version.

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 19.09.0-alt1
- New version.

* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.1-alt1
- New version.

* Fri Aug 16 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.0-alt1
- New version.

* Wed Jul 31 2019 Michael Shigorin <mike@altlinux.org> 19.07.0-alt3
- E2K: strip UTF-8 BOM for lcc < 1.24; explicit -std=c++11

* Thu Jul 25 2019 Andrey Cherepanov <cas@altlinux.org> 19.07.0-alt2
- Complete Russian localization (thanks Olesya Gerasimenko).

* Fri Jul 05 2019 Andrey Cherepanov <cas@altlinux.org> 19.07.0-alt1
- New version.
- Build only for x86 and aarch64.

* Fri Jul 05 2019 Andrey Cherepanov <cas@altlinux.org> 19.05.7-alt2
- Fix path to help files.

* Thu Jun 06 2019 Andrey Cherepanov <cas@altlinux.org> 19.05.7-alt1
- New version.

* Sun Feb 17 2019 Andrey Cherepanov <cas@altlinux.org> 19.02.0-alt2
- Return some source files ignored by .gitignore.

* Sat Feb 16 2019 Andrey Cherepanov <cas@altlinux.org> 19.02.0-alt1
- New version (ALT #36096).
- Build by cmake.

* Thu Feb 14 2019 Leontiy Volodin <lvol@altlinux.org> 17.05.0-alt3
- Fixed links to url (ALT #36097)
- Built with aarch64 support

* Fri Sep 21 2018 Anton Midyukov <antohami@altlinux.org> 17.05.0-alt2
- rebuilt with libwxGTK3.0
- exclude aarch64

* Tue Jun 20 2017 Ilya Mashkin <oddity@altlinux.ru> 17.05.0-alt1
- 17.05.0

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 16.04.2-alt2
- Use upstream desktop file
- Package info file

* Sun Jul 03 2016 Ilya Mashkin <oddity@altlinux.ru> 16.04.2-alt1
- 16.04.2

* Tue Dec 01 2015 Ilya Mashkin <oddity@altlinux.ru> 15.08.2-alt1
- 15.08.2
- missing files added

* Mon Jan 12 2015 Ilya Mashkin <oddity@altlinux.ru> 14.12.1-alt1
- 14.12.1

* Tue Sep 30 2014 Ilya Mashkin <oddity@altlinux.ru> 14.09.0-alt1
- 14.09.0

* Fri Nov 15 2013 Ilya Mashkin <oddity@altlinux.ru> 13.04.2-alt1
- 13.04.2

* Sat Sep 14 2013 Ilya Mashkin <oddity@altlinux.ru> 13.04.1-alt1
- 13.04.1

* Fri Mar 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.09.0-alt1.1
- Rebuilt (ALT #28734)

* Sun Dec 16 2012 Ilya Mashkin <oddity@altlinux.ru> 12.09.0-alt1
- 12.09.0

* Sat Jun 02 2012 Ilya Mashkin <oddity@altlinux.ru> 12.04.0-alt1
- 12.04.0

* Tue Aug 16 2011 Ilya Mashkin <oddity@altlinux.ru> 11.08.0-alt1
- 11.08.0

* Thu Jun 16 2011 Ilya Mashkin <oddity@altlinux.ru> 11.04.0-alt1
- 11.04.0

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.6-alt0.M51.1
- Build for 5.1

* Thu Sep 23 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Sat Sep 04 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.5-alt2
- update Russian translation (Closes: #23838)

* Wed Jun 02 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.3-alt2
- fix icons locations

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.3-alt1
- 0.8.3
- fix desktop file

* Mon Apr 20 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.2-alt1
- Version 0.8.2

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Dec 09 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.0-alt1
- 0.8.0
- apply repocop patch

* Wed Sep 10 2008 Ilya Mashkin <oddity@altlinux.ru> 0.7.5-alt0.1
- 0.7.5

* Tue Jan 01 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.4-alt1
- Version 0.7.4.

* Sun Sep 23 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.3a-alt1
- Vaersion 0.7.3a.
- Remove Russian description and summary.
- Desktop menu entry changed to Science;Math;

* Sun May 06 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.2-alt1
- Version 0.7.2.

* Fri Dec 22 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.1-alt1
- Version 0.7.1. 

* Sat Oct 14 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.0-alt2
- Rebuilt with new toolchain.

* Fri Sep 01 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.0-alt1
- Version 0.7.0.

* Sun May 07 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.5-alt1
- Version 0.6.5.

* Sat Apr 01 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.4-alt3
- Desktop menu file.

* Tue Nov 29 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.4-alt2
- Requires: maxima.

* Sat Nov 26 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.4-alt1
- Maxima 5.9.2 comptibility fixes.

* Sun Nov 06 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.2-alt1
- Initial ALT Linux release.
