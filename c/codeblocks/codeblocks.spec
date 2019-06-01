Name: codeblocks
# Don't forget to make a new parallel branch with upstream sources, when you
# will update codeblocks for a new version. In sisyphus branch windows blobs
# should be cleared.
Version: 17.12
Release: alt7

Summary: Code::Blocks is open source, cross platform free C++ IDE
Summary(ru_RU.UTF-8): Code::Blocks это кросс-платформенная свободная среда разработки для C++ с открытым исходным кодом

License: GPLv3
Group: Development/C++
Url: http://www.codeblocks.org

Packager: Grigory Ustinov <grenka@altlinux.ru>

Source0: %name-%version.tar
Source1: %name-8.02-alt-icons.tar
Source3: %name.desktop
Source4: %name.po

Patch0: codeblocks-language-detection-from-locale.patch
Patch1: codeblocks-ebuild.conf.patch

# should be checked in next release
Patch2: %name-%version-FortranProject_autotools_build.patch
Patch3: %name-%version-FortranProject_fix_build_gcc7_failed.patch

Requires: automake >= 1.7 wxGTK gcc gcc-c++ gdb xterm gamin mythes-en

BuildRequires: boost-devel gcc-c++ libICE-devel libgamin-devel libgtk+2-devel
BuildRequires: libhunspell-devel libwxGTK-contrib-gizmos-devel libwxGTK-devel
BuildRequires: tinyxml-devel zip zlib-devel bzlib-devel

%description
Code::Blocks is a free C++ IDE built specifically to meet the most
demanding needs of its users. It was designed, right from the start,
to be extensible and configurable. Built around a plugin framework,
Code::Blocks can be extended with plugin DLLs.
It includes a plugin wizard so you can compile your own plugins!

%description -l ru_RU.UTF-8
Code::Blocks это свободная IDE для C++, которая создана для
удовлетворения множества требований её пользователей.
Она разрабатывалась с самого начала, как расширяемая
и легко настраиваемая. Собранная с поддержкой плагинов
Code::Blocks может быть расширена с помощью подключаемых библиотек.

%package contrib
Summary: Code::Blocks contrib plugins
Summary(ru_RU.UTF-8): Дополнительные плагины для Code::Blocks
Group: Development/C++
Requires: codeblocks = %EVR

%description contrib
Additional Code::Blocks plugins.

%description contrib -l ru_RU.UTF-8
Набор дополнительных плагинов для среды разработки Code::Blocks.

%package devel
Summary: Code::Blocks SDK
Group: Development/C++
Requires: codeblocks = %EVR

%description devel
Code::Blocks SDK to develop your own plugins.

%description devel -l ru_RU.UTF-8
SDK для создания собственных плагинов к среде разработки Code::Blocks.

%prep
%setup -a1
cp %SOURCE3 src/mime/
cp %SOURCE4 .

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
msgfmt %name.po -o %name.mo
./bootstrap

%configure --with-contrib-plugins=all \
           --with-boost-libdir=%_libdir
%make_build

%install
%makeinstall_std
rm -f %buildroot/%_libdir/%name/plugins/*.la
rm -f %buildroot/%_libdir/%name/wxContribItems/*.la

install -m 644 -D alt-icons/16x16/%name.png %buildroot%_miconsdir/%name.png
install -m 644 -D alt-icons/32x32/%name.png %buildroot%_niconsdir/%name.png
install -m 644 -D alt-icons/48x48/%name.png %buildroot%_liconsdir/%name.png
install -m 644 -D alt-icons/64x64/%name.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -m 644 -D %name.mo %buildroot%_datadir/%name/locale/ru_RU/%name.mo

%files
%doc README COPYING AUTHORS BUGS COMPILERS TODO NEWS ChangeLog
%_bindir/%name
%_bindir/cb_console_runner
%_libdir/lib%name.so.*
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_man1dir/*
%exclude %_man1dir/codesnippets.1.xz
%exclude %_datadir/%name/images/16x16/fproject*
%exclude %_datadir/%name/images/fproject*

%dir %_datadir/%name
%dir %_datadir/%name/locale/ru_RU
%_datadir/%name/locale/ru_RU/codeblocks.mo

%_datadir/appdata/%name.appdata.xml

%_datadir/%name/abbreviations.zip
%_datadir/%name/Astyle.zip
%_datadir/%name/autosave.zip
%_datadir/%name/classwizard.zip
%_datadir/%name/codecompletion.zip
%_datadir/%name/compiler.zip
%_datadir/%name/debugger.zip
%_datadir/%name/defaultmimehandler.zip
%_datadir/%name/IncrementalSearch.zip
%_datadir/%name/manager_resources.zip
%_datadir/%name/resources.zip
%_datadir/%name/scriptedwizard.zip
%_datadir/%name/start_here.zip
%_datadir/%name/todo.zip
%_datadir/%name/Valgrind.zip
%_datadir/%name/tips.txt
%_datadir/%name/icons
%dir %_datadir/%name/images
%_datadir/%name/images/*.png
%_datadir/%name/images/16x16
%_datadir/%name/images/codecompletion
%_datadir/%name/images/settings
%_datadir/%name/compilers
%_datadir/%name/lexers
%_datadir/%name/locale
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libabbreviations.*
%_libdir/%name/plugins/libAstyle.*
%_libdir/%name/plugins/libautosave.*
%_libdir/%name/plugins/libclasswizard.*
%_libdir/%name/plugins/libcodecompletion.*
%_libdir/%name/plugins/libcompiler.*
%_libdir/%name/plugins/libdebugger.*
%_libdir/%name/plugins/libdefaultmimehandler.*
%_libdir/%name/plugins/libIncrementalSearch.*
%_libdir/%name/plugins/libscriptedwizard.*
%_libdir/%name/plugins/libtodo.*
%_libdir/%name/plugins/libValgrind.*
%_datadir/%name/scripts
%_datadir/%name/templates

%_iconsdir/hicolor/48x48/mimetypes/application-x-codeblocks-workspace.png
%_iconsdir/hicolor/48x48/mimetypes/application-x-codeblocks.png
%_iconsdir/hicolor/64x64/apps/codeblocks.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png

%files contrib
%_bindir/cb_share_config
%_libdir/libwxsmithlib.so*
%_libdir/%name/wxContribItems
%_man1dir/codesnippets.1.xz
%_datadir/appdata/%name-contrib.metainfo.xml

%_datadir/%name/AutoVersioning.zip
%_datadir/%name/BrowseTracker.zip
%_datadir/%name/byogames.zip
%_datadir/%name/cb_koders.zip
%_datadir/%name/Cccc.zip
%_datadir/%name/codesnippets.zip
%_datadir/%name/CppCheck.zip
%_datadir/%name/codestat.zip
%_datadir/%name/copystrings.zip
%_datadir/%name/Cscope.zip
%_datadir/%name/DoxyBlocks.zip
%_datadir/%name/dragscroll.zip
%_datadir/%name/EditorTweaks.zip
%_datadir/%name/EditorConfig.zip
%_datadir/%name/envvars.zip
%_datadir/%name/exporter.zip
%_datadir/%name/FileManager.zip
%_datadir/%name/FortranProject.zip
%_datadir/%name/help_plugin.zip
%_datadir/%name/HexEditor.zip
%_datadir/%name/headerfixup.zip
%_datadir/%name/keybinder.zip
%_datadir/%name/lib_finder.zip
%_datadir/%name/MouseSap.zip
%_datadir/%name/NassiShneiderman.zip
%_datadir/%name/occurrenceshighlighting.zip
%_datadir/%name/openfileslist.zip
%_datadir/%name/projectsimporter.zip
%_datadir/%name/ProjectOptionsManipulator.zip
%_datadir/%name/Profiler.zip
%_datadir/%name/RegExTestbed.zip
%_datadir/%name/ReopenEditor.zip
%_datadir/%name/SmartIndent*.zip
%_datadir/%name/SpellChecker.zip
%_datadir/%name/SymTab.zip
%_datadir/%name/ThreadSearch.zip
%_datadir/%name/ToolsPlus.zip
%_datadir/%name/wxsmith.zip
%_datadir/%name/wxSmithAui.zip
%_datadir/%name/wxsmithcontribitems.zip

%_datadir/%name/images/codesnippets
%_datadir/%name/images/DoxyBlocks
%_datadir/%name/images/fortranproject
%_datadir/%name/images/16x16/fproject*
%_datadir/%name/images/fproject*
%_datadir/%name/images/ThreadSearch
%_datadir/%name/images/wxsmith
%_datadir/%name/lib_finder
%_datadir/%name/SpellChecker

%_libdir/%name/plugins/libAutoVersioning.*
%_libdir/%name/plugins/libBrowseTracker.*
%_libdir/%name/plugins/libbyogames.*
%_libdir/%name/plugins/libcb_koders.*
%_libdir/%name/plugins/libCccc.*
%_libdir/%name/plugins/libcodesnippets.*
%_libdir/%name/plugins/libcodestat.*
%_libdir/%name/plugins/libcopystrings.*
%_libdir/%name/plugins/libCppCheck.*
%_libdir/%name/plugins/libCscope.*
%_libdir/%name/plugins/libDoxyBlocks.*
%_libdir/%name/plugins/libdragscroll.*
%_libdir/%name/plugins/libEditorTweaks.*
%_libdir/%name/plugins/libEditorConfig.*
%_libdir/%name/plugins/libenvvars.*
%_libdir/%name/plugins/libexporter.*
%_libdir/%name/plugins/libFileManager.*
%_libdir/%name/plugins/libFortranProject.*
%_libdir/%name/plugins/libhelp_plugin.*
%_libdir/%name/plugins/libHexEditor.*
%_libdir/%name/plugins/libheaderfixup.*
%_libdir/%name/plugins/libkeybinder.*
%_libdir/%name/plugins/liblib_finder.*
%_libdir/%name/plugins/libMouseSap.*
%_libdir/%name/plugins/libNassiShneiderman.*
%_libdir/%name/plugins/liboccurrenceshighlighting.*
%_libdir/%name/plugins/libopenfileslist.*
%_libdir/%name/plugins/libprojectsimporter.*
%_libdir/%name/plugins/libProjectOptionsManipulator.*
%_libdir/%name/plugins/libProfiler.*
%_libdir/%name/plugins/libRegExTestbed.*
%_libdir/%name/plugins/libReopenEditor.*
%_libdir/%name/plugins/libSmartIndent*.*
%_libdir/%name/plugins/libSpellChecker.*
%_libdir/%name/plugins/libSymTab.*
%_libdir/%name/plugins/libThreadSearch.*
%_libdir/%name/plugins/libToolsPlus.*
%_libdir/%name/plugins/libwxsmith.*
%_libdir/%name/plugins/libwxSmithAui.*
%_libdir/%name/plugins/libwxsmithcontribitems.*

%files devel
%_includedir/%name
%_includedir/wxsmith
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc
%_libdir/pkgconfig/cb_wx*.pc
%_libdir/pkgconfig/wxsmith.pc
%_libdir/pkgconfig/wxsmithaui.pc
%_libdir/pkgconfig/wxsmith-contrib.pc

%changelog
* Wed May 29 2019 Grigory Ustinov <grenka@altlinux.org> 17.12-alt7
- Significant update russian localization (Closes: #36007).
- Build with system bzlib (Closes: #36434).

* Fri Feb 08 2019 Grigory Ustinov <grenka@altlinux.org> 17.12-alt6
- Turned on automatical detection of language from user locale.
- Built with tinyxml.

* Thu Dec 13 2018 Grigory Ustinov <grenka@altlinux.org> 17.12-alt5
- Add dependency on gamin (Closes: #35764).
- Add dependency on mythes-en (Closes: #35765).

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 17.12-alt4
- Fixed FTBFS (removed xdg macro).
- Fixed bogus date in changelog.

* Thu Jun 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12-alt3
- NMU: rebuilt with boost-1.67.0.

* Tue May 08 2018 Grigory Ustinov <grenka@altlinux.org> 17.12-alt2
- Add patches for fix FortranProject plugin (Closes: #34891).

* Mon Jan 22 2018 Grigory Ustinov <grenka@altlinux.org> 17.12-alt1
- Build new version (Closes: #34437).
- Removed default config from /etc/skel, because it's not good idea
  to make russian interface, when user have not russian locale.

* Thu Jan 28 2016 Denis Kirienko <dk@altlinux.org> 16.01-alt1
- 16.01 release

* Fri Jan 17 2014 Denis Kirienko <dk@altlinux.org> 13.12-alt1
- 13.12 release

* Fri Jun 21 2013 Denis Kirienko <dk@altlinux.org> 12.11.9158-alt1
- SVN snapshot 9158

* Sun Dec 09 2012 Denis Kirienko <dk@altlinux.org> 12.11-alt1
- 12.11 release (SVN 8629)

* Fri Nov 23 2012 Denis Kirienko <dk@altlinux.org> 12.11-alt0.2
- 12.11 RC2 (SVN 8598)

* Wed Nov 14 2012 Denis Kirienko <dk@altlinux.org> 10.05.8549-alt1
- 12.11 RC1 (SVN 8549)

* Sun Nov 04 2012 Denis Kirienko <dk@altlinux.org> 10.05.8500-alt1
- SVN snapshot 8500

* Sun Oct 21 2012 Denis Kirienko <dk@altlinux.org> 10.05.8466-alt1
- SVN snapshot 8466

* Fri Oct 19 2012 Denis Kirienko <dk@altlinux.org> 10.05.8455-alt2
- Added default config in /etc/skel

* Sat Oct 13 2012 Denis Kirienko <dk@altlinux.org> 10.05.8455-alt1
- SVN snapshot 8455

* Wed Oct 10 2012 Denis Kirienko <dk@altlinux.org> 10.05.8438-alt1
- SVN snapshot 8438
  Added SmartIndent plugins

* Thu Aug 23 2012 Denis Kirienko <dk@altlinux.org> 10.05.8247-alt1
- SVN snapshot 8247
- Added EditorConfig plugin

* Wed Jul 11 2012 Denis Kirienko <dk@altlinux.org> 10.05.8086-alt1
- SVN snapshot 8086

* Thu May 17 2012 Denis Kirienko <dk@altlinux.org> 10.05.7966-alt1
- SVN snapshot 7966

* Tue Apr 17 2012 Denis Kirienko <dk@altlinux.org> 10.05.7932-alt1
- SVN snapshot 7932

* Sat Apr 07 2012 Denis Kirienko <dk@altlinux.org> 10.05.7917-alt1
- SVN snapshot 7917

* Sat Jan 07 2012 Denis Kirienko <dk@altlinux.org> 10.05.7678-alt1
- SVN snapshot 7678

* Sat Aug 27 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7385-alt1
- SVN snapshot 7385
- Added SpellChecker plugin

* Fri Jul 22 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7289-alt1
- SVN snapshot 7289

* Thu Jun 30 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7259-alt1
- SVN snapshot 7259

* Sun May 15 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7143-alt1
- SVN snapshot 7143

* Sun Apr 03 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7075-alt1
- SVN snapshot 7075

* Fri Mar 11 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7040-alt1
- SVN snapshot 7040

* Wed Feb 23 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7017-alt1
- SVN snapshot 7017
- Added FileManager and ToolsPlus plugins

* Wed Jan 26 2011 Denis Kirienko <dk@altlinux.ru> 10.05.6931-alt1
- SVN snapshot 6931
- Added ReopenEditor plugin

* Fri Dec 24 2010 Denis Kirienko <dk@altlinux.ru> 10.05.6900-alt2
- Fixed bug in the CodeComplition plugin
- Added EditorTweaks plugin

* Sun Dec 19 2010 Denis Kirienko <dk@altlinux.ru> 10.05.6900-alt1
- SVN snapshot 6900
- Fixed license (closes: 23731)

* Sun Nov 14 2010 Denis Kirienko <dk@altlinux.ru> 10.05.6846-alt1
- SVN snapshot 6846
- Added new plugins: abbreviations, Cscope, DoxyBlocks, NassiShneiderman
- Updated russian translation

* Mon Jun 21 2010 Denis Kirienko <dk@altlinux.ru> 10.05-alt1
- New version 10.05
- Updated russian translation

* Sun May 23 2010 Denis Kirienko <dk@altlinux.ru> 8.02.6271-alt1
- SVN snapshot 6271

* Sun Feb 28 2010 Denis Kirienko <dk@altlinux.ru> 8.02.6181-alt1
- SVN snapshot 6181
- Updated russian translation

* Sat Feb 13 2010 Denis Kirienko <dk@altlinux.ru> 8.02-alt24
- SVN snapshot 6155
- Updated russian translation

* Wed Jan 13 2010 Denis Kirienko <dk@altlinux.ru> 8.02-alt23
- SVN snapshot 6080
- Added Cccc and CppCheck plugins
- Updated russian translation

* Wed Nov 11 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt22
- SVN snapshot 5911
- Updated russian translation

* Sun Oct 18 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt21
- Updated russian translation

* Sat Oct 10 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt20
- SVN snapshot 5859
- Updated russian translation
- Added MouseSap plugin

* Sun Sep 27 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt19
- Updated russian translation

* Sun Sep 06 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt18
- Updated russian translation

* Mon Aug 24 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt17
- Rebuid with wxGTK-2.8.10-alt2 (see #20451)

* Sun Aug 23 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt16
- Updated russian translation
- Added dependencies to gcc, gcc-c++, gdb, xterm

* Sat Aug 22 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt15
- Added russian translation (yet unfinished)

* Tue Aug 18 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt14
- SVN snapshot 5731

* Thu Jul 30 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt13
- SVN snapshot 5716
- Added wxSmithAui plugin to codeblocks-contrib package

* Sun Jun 21 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt12
- SVN snapshot 5678

* Mon Jun 15 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt11
- Rebuild with wxGTK-2.8.9-alt2 (fix #20450)

* Sat Jun 06 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt10
- SVN snapshot 5616

* Tue May 19 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt9
- SVN snapshot 5602

* Sat May 02 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt8
- SVN snapshot 5535
- Added copystrings plugin to codeblocks-contrib package

* Sun Apr 12 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt7
- SVN snapshot 5489

* Sun Feb 15 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt6
- SVN snapshot 5456
- Removed QtWorkbench plugin (see http://code.google.com/p/qtworkbench/issues/detail?id=20)

* Sat Feb 07 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt5
- SVN snapshot 5432
- Compressed ChangeLog

* Fri Jan 09 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt4
- SVN snapshot 5382
- Added IncrementalSearch and Valgrind plugins to codeblocks package
- Added HexEditor and headerfixup plugins to codeblocks-contrib package
- QtWorkbench plugin updated to version 0.6.0-alpha (SVN 146)

* Sat Nov 29 2008 Denis Kirienko <dk@altlinux.ru> 8.02-alt3
- Really updated codeblocks.desktop

* Mon Nov 24 2008 Denis Kirienko <dk@altlinux.ru> 8.02-alt2
- Spec cleanup
- Updated codeblocks.desktop

* Sun Mar 02 2008 Denis Kirienko <dk@altlinux.ru> 8.02-alt1
- Stable release 8.02
- Added BrowseTracker plugin

* Sun Jan 13 2008 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4807
- New SVN snapshot
- Added ThreadSearch plugin

* Sat Dec 22 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4742
- New SVN snapshot
- Added openfilelist plugin
- Added AutoVersioning plugin

* Sat Sep 08 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4439
- New SVN snapshot
- Added QtWorkbench plugin

* Sun Aug 26 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4405
- New SVN snapshot

* Sat Aug 04 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4346
- New SVN snapshot
- Added projectsimporter plugin

* Sat Jun 30 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4193
- New SVN snapshot

* Sun Jun 17 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4101
- New SVN snapshot
- Removed wxRE_ADVANCED patch (no more needed)

* Tue May 01 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3910
- New SVN snapshot
- Updated patches
- Added patch that fixes undefined symbol wxRE_ADVANCED error during build
- Added libwxsmith as a contrib package

* Wed Jan 10 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3450
- New SVN snapshot
- Automatical creation of revision.m4 file before configure
- Added --enable-contrib option to the configure
- Splitted into three separate packages: codeblocks, codeblocks-contrib, codeblocks-devel
- Added set of icons according to requirements of new iconpaths policy

* Fri Nov 24 2006 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3258
- New SVN snapshot

* Fri Oct 06 2006 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3025
- New SVN snapshot

* Thu Sep 14 2006 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn2975
- New maintainer
- New SVN snapshot
- Fixed Icon parameter in the desktop file
- Fixed Qt4 application wizard

* Wed Jan 04 2006 php-coder <php-coder@altlinux.ru> 1.0-alt0.svn1652
- Initial build for ALT Linux Sisyphus
- Added patch which fixes some warnings from compiler
