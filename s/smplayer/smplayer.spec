%define		svn 9253

%define		rel alt1

Name:		smplayer
Summary:	A great MPlayer/MPV front-end (QT4)
Summary(ru_RU.UTF8): Мощный интерфейс для MPlayer/MPV (QT4)
Summary(uk_UA.UTF8): Потужний інтерфейс для MPlayer/MPV (QT4)
License:	GPLv2
Group:		Video
Url:		http://smplayer.sourceforge.net
Version:	19.10.2
Release:	%rel.%svn
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	http://downloads.sourceforge.net/smplayer/%name-%version.tar.bz2
Patch0:		smplayer-paths-fix-alt.patch
Patch1:		smplayer-18.3-disable_update.patch

BuildRequires:	gcc-c++ libqt4-devel >= 4.2
Provides: %name


%if "%rel" == "alt0.M70T"
Requires: mplayer
%endif
%if "%rel" == "alt0.M60T"
Requires: mplayer
%endif
%if "%rel" == "alt0.M51"
Requires: mplayer
%endif

%description
smplayer intends to be a complete front-end for MPlayer/MPV, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support
for MPlayer/MPV filters and more. One of the main features is the ability to
remember the state of a played file, so when you play it later it will resume
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.
Compiled with Qt4

%description -l ru_RU.UTF8
SMPlayer стремится быть как можно более полным интерфейсом для MPlayer/MPV,
от базовых функций проигрывания видео, DVD, VCDs до самого продвинутого
функционала MPlayer/MPV по поддержке фильтров и т.п. Одна из главных
особенностей - способность запоминать положение проигрываемого файла для
того, чтобы при следующем его открытии Вы могли смотреть его дальше с
того же места и с теми же параметрами настроек. SMPlayer разработан на
инструментарии Qt и является мультиплатформенным.
Скомпилировано с Qt4

%description -l uk_UA.UTF8
SMPlayer направлений на те, щоб стати як можна більш повним інтерфейсом
для MPlayer/MPV, від базових функцій відтворення відео, DVD, VCD до самого
продвинутого функціонала MPlayer/MPV по підтримці фільтрів і т.і. Одна з
головних особливостей - здатність запам'ятовувати положення файлу, що
відтворюється, для того, щоб при наступному його відкритті Ви мали змогу
переглядати його далі з того ж місця і з тими ж параметрами налаштувань.
SMPlayer розробено на інструментарії Qt і є мультиплатформним.
Зібрано з Qt4


%if "%rel" == "alt1"
%package -n %name-mpv
Summary: A great MPV front-end (QT4)
Group: Video
Requires: %name mpv
BuildArch: noarch

%description -n %name-mpv
Virtual package for SMPlayer, requires a MPV

%package -n %name-mplayer
Summary: A great MPlayer front-end (QT4)
Group: Video
Requires: %name mplayer
BuildArch: noarch

%description -n %name-mplayer
Virtual package for SMPlayer, requires a MPlayer
%endif

%if "%rel" == "alt0.M90P"
%package -n %name-mpv
Summary: A great MPV front-end (QT4)
Group: Video
Requires: %name mpv
BuildArch: noarch

%description -n %name-mpv
Virtual package for SMPlayer, requires a MPV

%package -n %name-mplayer
Summary: A great MPlayer front-end (QT4)
Group: Video
Requires: %name mplayer
BuildArch: noarch

%description -n %name-mplayer
Virtual package for SMPlayer, requires a MPlayer
%endif

%if "%rel" == "alt0.M80P"
%package -n %name-mpv
Summary: A great MPV front-end (QT4)
Group: Video
Requires: %name mpv
BuildArch: noarch

%description -n %name-mpv
Virtual package for SMPlayer, requires a MPV

%package -n %name-mplayer
Summary: A great MPlayer front-end (QT4)
Group: Video
Requires: %name mplayer
BuildArch: noarch

%description -n %name-mplayer
Virtual package for SMPlayer, requires a MPlayer
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i 's|DOC_PATH=$(PREFIX)/share/doc/packages/smplayer|DOC_PATH=%_docdir/%name-%version|g' Makefile
sed -i 's|0UNKNOWN|%svn|g' get_svn_revision.sh

%build
export PATH=$PATH:%_qt4dir/bin
export OPTFLAGS="%optflags"
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/%name
%_bindir/simple_web_server
%_desktopdir/*.desktop
%_docdir/%name-%version
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man1dir/*

%if "%rel" == "alt1"
%files -n %name-mpv
%files -n %name-mplayer
%endif
%if "%rel" == "alt0.M90P"
%files -n %name-mpv
%files -n %name-mplayer
%endif
%if "%rel" == "alt0.M80P"
%files -n %name-mpv
%files -n %name-mplayer
%endif

%changelog
* Sun Jan 19 2020 Motsyo Gennadi <drool@altlinux.ru> 19.10.2-alt1.9253
- 19.10.2 (svn9253)

* Sat Jul 13 2019 Motsyo Gennadi <drool@altlinux.ru> 19.5.0-alt1.9225
- 19.5.0 (svn9225)

* Mon Sep 17 2018 Motsyo Gennadi <drool@altlinux.ru> 18.9.0-alt1.9113
- 18.9.0 (svn9113)

* Wed Apr 25 2018 Motsyo Gennadi <drool@altlinux.ru> 18.4.0-alt1.8992
- 18.4.0 (svn8992)

* Sat Apr 21 2018 Motsyo Gennadi <drool@altlinux.ru> 18.3-alt1.8982
- 18.3 version (svn8982)

* Sat Mar 17 2018 Motsyo Gennadi <drool@altlinux.ru> 18.3-alt1.8954
- 18.3 version (svn8954)

* Wed Nov 22 2017 Motsyo Gennadi <drool@altlinux.ru> 17.11.2-alt1.8808
- 17.11.2 version (svn8808)

* Sun Oct 08 2017 Motsyo Gennadi <drool@altlinux.ru> 17.10.0-alt1.8715
- 17.10.0 version (svn8715)

* Wed Aug 30 2017 Motsyo Gennadi <drool@altlinux.ru> 17.9.0-alt1.8641
- 17.9.0 version (svn8641)

* Tue Aug 22 2017 Motsyo Gennadi <drool@altlinux.ru> 17.8.0-alt1.8630
- 17.8.0 version (svn8630)

* Fri Jun 09 2017 Motsyo Gennadi <drool@altlinux.ru> 17.6.0-alt1.8588
- 17.6.0 version (svn8588)

* Sun Feb 12 2017 Motsyo Gennadi <drool@altlinux.ru> 17.2-alt1.8442
- 17.2 version (svn8442)

* Sun Nov 27 2016 Motsyo Gennadi <drool@altlinux.ru> 16.11.0-alt1.8247
- 16.11.0 version (svn8247)

* Mon Sep 19 2016 Motsyo Gennadi <drool@altlinux.ru> 16.9.0-alt1.8152
- 16.9.0 version (svn8152)

* Thu Aug 11 2016 Motsyo Gennadi <drool@altlinux.ru> 16.8.0-alt1.8066
- 16.8.0 version (svn8066)

* Mon May 09 2016 Motsyo Gennadi <drool@altlinux.ru> 16.4.0-alt1.7822
- 16.4.0 version (svn7822)

* Mon Apr 18 2016 Motsyo Gennadi <drool@altlinux.ru> 16.4.0-alt1.7676
- 16.4.0 version (svn7676)

* Sun Apr 17 2016 Motsyo Gennadi <drool@altlinux.ru> 16.4.0-alt1.7665
- 16.4.0 version (svn7665)

* Sun Apr 17 2016 Motsyo Gennadi <drool@altlinux.ru> 16.4.0-alt1.7662
- 16.4.0 version (svn7662)

* Sun Feb 28 2016 Motsyo Gennadi <drool@altlinux.ru> 16.1.0-alt1.7460
- 16.1.0 version (svn7460)

* Sat Feb 06 2016 Motsyo Gennadi <drool@altlinux.ru> 16.1.0-alt1.7387
- 16.1.0 version (svn7387)

* Fri Dec 11 2015 Motsyo Gennadi <drool@altlinux.ru> 15.11.0-alt1.7273
- 15.11.0 version (svn7273)

* Fri Oct 09 2015 Motsyo Gennadi <drool@altlinux.ru> 15.9.0-alt1.7165
- 15.9.0 version (svn7102)

* Sun Sep 06 2015 Motsyo Gennadi <drool@altlinux.ru> 14.9.0-alt1.7102
- svn7102

* Sun Jul 26 2015 Motsyo Gennadi <drool@altlinux.ru> 14.9.0-alt1.7048.1
- update Ukrainian translation (fixed typo)

* Sat Jul 25 2015 Motsyo Gennadi <drool@altlinux.ru> 14.9.0-alt1.7048
- ALT bug #31142
- svn7048

* Mon Feb 23 2015 Motsyo Gennadi <drool@altlinux.ru> 14.9.0-alt1.6748
- svn6748

* Mon Nov 24 2014 Motsyo Gennadi <drool@altlinux.ru> 14.9.0-alt1.6465
- svn6465

* Fri Oct 17 2014 Motsyo Gennadi <drool@altlinux.ru> 14.9.0-alt1.6415
- 14.9.0 svn6415

* Wed Apr 23 2014 Motsyo Gennadi <drool@altlinux.ru> 14.3.0-alt1.6216
- svn6216

* Sat Apr 05 2014 Motsyo Gennadi <drool@altlinux.ru> 14.3.0-alt1.6172
- 14.3.0
- svn 6172

* Sat Aug 17 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.5641
- 0.8.6
- svn 5641

* Wed Aug 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.5-alt1.5629
- svn revision 5629
- disable UpdateChecker by default (alt bug #29204)

* Thu Jul 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.5-alt1.5543
- svn revision 5543

* Wed Jun 12 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.5-alt1.5464
- svn revision 5464

* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Mon Mar 25 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Jan 21 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Tue Sep 25 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun Apr 22 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.4305
- 0.8.0 (svn revision 4305)

* Mon Sep 12 2011 Alexey Morsov <swi@altlinux.ru> 0.6.10-alt1.3615
- new svn version (r3615)

* Sat Nov 20 2010 Alexey Morsov <swi@altlinux.ru> 0.6.10-alt1.3592
- new svn version (r3592)

* Sat Oct 09 2010 Alexey Morsov <swi@altlinux.ru> 0.6.10-alt1.3587
- new svn version (r3587)

* Tue Aug 10 2010 Alexey Morsov <swi@altlinux.ru> 0.6.10-alt1.3575
- new svn version

* Mon Jul 26 2010 Alexey Morsov <swi@altlinux.ru> 0.6.10-alt1.3570
- new svn version (commint 473b5d1bb27820217302d9c32cad76a9d53cfb80)
- remove packages-info-i18n-common

* Tue May 25 2010 Alexey Morsov <swi@altlinux.ru> 0.6.10-alt1.3537
- new svn version (commit 3f7ef5ca044774b3e3f18c418c867eddcfd9a550)

* Wed Mar 10 2010 Alexey Morsov <swi@altlinux.ru> 0.6.9-alt1.3473
- new svn version (commit 9e08ea1e8074bf48e3749c8dd60be27cd4ca2014)

* Thu Oct 08 2009 Alexey Morsov <swi@altlinux.ru> 0.6.8-alt3.svn3286
- new svn version (commit 6c864d434e1e5b3655d860cd2e1bbc00840c865c)

* Tue Sep 22 2009 Alexey Morsov <swi@altlinux.ru> 0.6.8-alt3.svn3270
- new svn version (commit 88ecb91053739018c4a16bc30f8ad661b52ad3d8)

* Mon Sep 07 2009 Alexey Morsov <swi@altlinux.ru> 0.6.8-alt3.svn3261
- new svn version (commint f4169b00b405820770183ef89592ee9de91e8c86)

* Tue Aug 04 2009 Alexey Morsov <swi@altlinux.ru> 0.6.8-alt2
- fix bug no 20935

* Tue Jul 28 2009 Alexey Morsov <swi@altlinux.ru> 0.6.8-alt1
- new version

* Thu Apr 23 2009 Alexey Morsov <swi@altlinux.ru> 0.6.7-alt1.1
- kick out _gl translation file (bug of qt4.5-rc)

* Wed Mar 11 2009 Alexey Morsov <swi@altlinux.ru> 0.6.7-alt1
- new version

* Sat Jan 10 2009 Alexey Morsov <swi@altlinux.ru> 0.6.6-alt1
- new version

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 0.6.5.1-alt1
- new version
- fix spec
  + remove deprecated call in post/postun
- fix desktop file (repocop)

* Sun Nov  2 2008 Alexey Morsov <swi@altlinux.org> 0.6.4-alt1
- new version

* Mon Oct 06 2008 Alexey Morsov <swi@altlinux.ru> 0.6.3-alt1
- new version

* Sun Aug 31 2008 Alexey Morsov <swi@altlinux.ru> 0.6.2-alt0.svn.r1716
- new development version

* Sat Aug 02 2008 Alexey Morsov <swi@altlinux.ru> 0.6.2-alt0.svn.r1594
- new development version

* Sun Jun 15 2008 Alexey Morsov <swi@altlinux.ru> 0.6.1-alt1
- new version

* Wed May 28 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt3
- update .desktop file (drool@)
- fix paths for ttf in help (drool@)
- remove .menu (policy)

* Thu May 15 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt2
- 0.6.0 final

* Wed Apr 23 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt1.rc4
- 0.6.0rc4
- Added support for the mouse XButton1 and XButton2. 
- Added in Preferences->General->Video an option to select
  the default deinterlacer. 

* Sat Apr 05 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt1.rc3
- up to 0.6.0 rc3
- Added new menu Video->Rotate, with options to rotate the image.
- Added new option Play->Jump to, which will show a dialog where 
  you can enter the position (time) to jump.
- Added two new options in the Subtitles menu: 
  "Enable closed caption" and "Forced subtitles only".
- Some multimedia keys should be recognized now in the shortcut editor.

* Sat Mar 22 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt1.996
- Fix: selection of chapters should work again with newer
  versions of mplayer.
- Added rm and swf to the list of extensions.
- Added new menu Video->Rotate, with options to rotate the image.

* Fri Mar 14 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt1.962
- Added two new options in the Subtitles menu: 
  "Enable closed caption" and "Forced subtitles only".
- Add the hue filter if the software equalizer is enabled. 
- Allow the software equalizer to be used with gl/gl2.
- Added flac to the list of audio extensions.
- Now the shortcut editor should recognize some of the 
  multimedia keys.
- Added more help for the subtitle, interface and 
  advanced sections in preferences.
- Added a new dialog to report the mplayer errors.

* Fri Feb 15 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt0.rc2
- up to 0.6.0rc2

* Thu Jan 31 2008 Alexey Morsov <swi@altlinux.ru> 0.6.0-alt0.rc1
- 0.6.0rc1
= Better accuracy on subtitle selection. Fixes problems with mp4 embedded subtitles.
- The cache setting is independent for each type of media.
- Now the H.264 loop filter can be disabled for High Definition videos only (720p and above).
- Possibility to update the video while dragging the time slider.
- Now it's possible to zoom out the video image.
- SSA/ASS subtitles can also be resized during playback.
- New option Video->Add black borders, which replaces the letterbox options in Video->Aspect ratio.

* Thu Jan 03 2008 Alexey Morsov <swi@altlinux.ru> 0.5.63-alt1.svn.r575
- svn r575
- now have man

* Sat Dec 08 2007 Alexey Morsov <swi@altlinux.ru> 0.5.63-alt1.svn.r461
- svn r461

* Wed Nov 28 2007 Alexey Morsov <swi@altlinux.ru> 0.5.63-alt0.vn.r444
- svn r444
- Added support for playlists in format pls

* Sun Nov 18 2007 Alexey Morsov <swi@altlinux.ru> 0.5.62-alt1
- 0.5.62
- minigui added
- Now the floating control shows with an animation!
- Added a new function for the mouse wheel: change playback
speed.

* Wed Oct 10 2007 Alexey Morsov <swi@altlinux.ru> 0.5.61-alt1
- version 0.5.61
- minor fixes, updatet translations

* Thu Sep 20 2007 Alexey Morsov <swi@altlinux.ru> 0.5.60-alt1
- version 0.5.60
- disabled new resize window scheme (sometimes makes window 
  without video played until resized manualy or swithed to
	fullscreen)

* Thu Sep 13 2007 Alexey Morsov <swi@altlinux.ru> 0.5.59-alt1
- version 0.5.59
- Bugfix: when passing only one file through command line, the 
  file wasn't added to the playlist.

* Wed Sep 12 2007 Alexey Morsov <swi@altlinux.ru> 0.5.58-alt1
- version 0.5.58

* Wed Sep 12 2007 Alexey Morsov <swi@altlinux.ru> 0.5.57-alt1
- version 0.5.57
- Fixes in the window resize code. Now resizes should be much smoother.
- Fixed regular expression in core.cpp to identify the DVD drive letter.

* Sat Sep 08 2007 Alexey Morsov <swi@altlinux.ru> 0.5.53-alt1
- version 0.5.53
- many impovements
- Fix in the open URL dialog: the text should be selected now.
- Fixed warnings about using deprecated setBackgroundColor.

* Tue Aug 28 2007 Alexey Morsov <swi@altlinux.ru> 0.5.45-alt1
- version 0.5.45
- minor changes

* Fri Aug 24 2007 Alexey Morsov <swi@altlinux.ru> 0.5.42-alt1
- Serious bug: a lot of actions were missing in 
  the actions' editor. Fixed.

* Thu Aug 23 2007 Alexey Morsov <swi@altlinux.ru> 0.5.41-alt1
- version 0.5.41
- Fixed the problem with the Video->Size menu.
- Bug fix: now the info about the demuxer, audio and video
  codec are updated after a restart of the mplayer process.
- Fix: now reading the info about video, audio drivers, 
  codecs and demuxers is done in a language independent way.

* Fri Aug 17 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0817
- version 0.5.29-08017

* Fri Aug 10 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0809
- version 0.5.29-0809
- Fixed a bug in the playlist.
- Many interface and translation changes

* Tue Jul 31 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0730
- version 0.5.29-0730
- fix bug #12428
- Fix: if the mplayer path is a relative path, don't convert it 
	to an absolute one. Otherwise smplayer may not work in external 
	devices as it might not find mplayer.
- Some fixes with the style stuff in Preferences->Interface.

* Sun Jul 29 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0727
- version 0.5.29-0727
- Bug fix: exit from fullscreen when playing an audio file.
- Bug fix: the end of file is signaling once the process has finished.
- Bug fix: the size of the main window might be much bigger than it
	should when playing a file passed through command line. I think this is
	fixed now. 
- The problem was that the file begins to play when the main window is
	not shown yet. Anyway this part of the code is a mess and has to be fixed. 
- Some fixes in myclient. Now uses UTF-8 to encode the texts, the 
	timeout is set to 200 ms.
- Fix: if you don't pass any file to the 2nd instance, it won't show. 
- Fix: tray icon: it will remember again if the main window was hidden on startup.
- Fix: when a video finished and a 2nd one starts to play from the playlist, 
	the setting for not repainting the window background was ignored. 
- Properly fixed a problem with a signal. 

* Sat Jul 21 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0720
- version 0.5.29-0720
- Fix with the myprocess stuff. A connection was not made. 
	This could make that the screensaver weren't turned on.
- Now the video background stops repainting just *before* the mplayer 
	process starts, instead of doing it when it already has started. 
	This could fix that the video window could still get black sometimes
- Fix: now reading the info about video, audio drivers, codecs and 
	demuxers is done in a language independent way (it looks for tags 
	like "ID_VIDEO_OUTPUTS" instead of English text)


* Thu Jul 12 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0710
- version 0.5.29-0710
- The priority option in preferences was broken. Fixed. 

* Tue Jul 10 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0709
- version 0.5.29-0709
- Bug fix: now the info about the demuxer, audio and video codec are updated
after a restart of the mplayer process.

* Thu Jul 05 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0704
- version 0.5.29-0704 

* Mon Jul 02 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0701.2
- version 0.5.29-0701-2 

* Sat Jun 30 2007 Alexey Morsov <swi@altlinux.ru> 0.5.29-alt1.0628.2
- version 0.5.29
- spec reorganized due to swith to qt4-only
- add new updated translations for RU and UA (thanks to drool@)

* Mon Jun 25 2007 Alexey Morsov <swi@altlinux.ru> 0.5.21-alt1
- version 0.5.21
- fix alternatives

* Fri Jun 22 2007 Alexey Morsov <swi@altlinux.ru> 0.5.19-alt1
- version 0.5.19 

* Wed Jun 20 2007 Alexey Morsov <swi@altlinux.ru> 0.5.18-alt1
- version 0.5.18
- fix alternative (package separation)

* Wed Jun 20 2007 Alexey Morsov <swi@altlinux.ru> 0.5.17-alt1
- version 0.5.17
- add alternatives (thanks to evg@)
- adjust spec for alternatives

* Thu Jun 14 2007 Alexey Morsov <swi@altlinux.ru> 0.5.14-alt1
- version 0.5.14

* Wed Jun 13 2007 Alexey Morsov <swi@altlinux.ru> 0.5.12-alt1
- version 0.5.12
- fix building optflags'

* Tue Jun 12 2007 Alexey Morsov <swi@altlinux.ru> 0.5.11-alt1
- version 0.5.11

* Sun Jun 10 2007 Alexey Morsov <swi@altlinux.ru> 0.5.9-alt1
- version 0.5.9

* Thu Jun 07 2007 Alexey Morsov <swi@altlinux.ru> 0.5.7-alt1
- version 0.5.7

* Wed Jun 06 2007 Alexey Morsov <swi@altlinux.ru> 0.5.6-alt1
- version 0.5.6

* Wed Jun 06 2007 Alexey Morsov <swi@altlinux.ru> 0.5.5-alt2
- fix patch1

* Tue Jun 05 2007 Alexey Morsov <swi@altlinux.ru> 0.5.5-alt1
- Added in the audio menu an option to load an external audio file
- Added the option "dont_use_eq_options" in the config file, ([preferences]
- Updated the German translation.
- Added an empty icon for gamma


* Tue Jun 05 2007 Alexey Morsov <swi@altlinux.ru> 0.5.4-alt1
- The size of the floating control can be changed
- The size and position of the main window will be remembered.


* Mon Jun 04 2007 Alexey Morsov <swi@altlinux.ru> 0.5.3-alt1
- Updated the Polish and Russian translations.
- New fullscreen control widget, smaller than the previous one. 

* Wed May 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.0-alt1
- NMU
- new version
- disabled external ukrainian translation (upstream merged)
- fix doc path without mv ;-)

* Sun May 20 2007 Alexey Morsov <swi@altlinux.ru> 0.4.24-alt1
- new version (Added support for SSA/ASS override styles)

* Fri May 18 2007 Alexey Morsov <swi@altlinux.ru> 0.4.23-alt1
- new version (fix colorkeys)

* Fri May 18 2007 Alexey Morsov <swi@altlinux.ru> 0.4.22-alt1
- new version
- fix Summary charset (fix bug #11802)

* Tue May 15 2007 Alexey Morsov <swi@altlinux.ru> 0.4.20-alt1
- new version
- add tray icon in qt3/kde
- fix float control with full-screen mode and two monitors

* Fri May 11 2007 Alexey Morsov <swi@altlinux.ru> 0.4.18-alt1
- new version

* Wed May 09 2007 Alexey Morsov <swi@altlinux.ru> 0.4.16-alt1
- new version (add new features for subtitles)

* Tue May 08 2007 Alexey Morsov <swi@altlinux.ru> 0.4.15-alt2
- new version
- fix kde support (damn copy-n-paste)
- add .desktop files

* Mon May 07 2007 Alexey Morsov <swi@altlinux.ru> 0.4.13-alt1
- new version
- build for qt3/qt4/kde (thanks to drool@ for spec)
- add menu and ukrainian translations (from drool@ package)

* Fri Apr 20 2007 Alexey Morsov <swi@altlinux.ru> 0.3.38-alt1
- new version
- support for kde

* Thu Apr 19 2007 Alexey Morsov <swi@altlinux.ru> 0.3.29-alt1
- initial build for sisyphus

* Sat Apr 14 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.20-alt0.M24.1
- new version

* Sat Apr 14 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.19-alt0.M24.1
- new version
- disable external ukrainian translation (upstream merged)

* Fri Apr 13 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.18-alt0.M24.1
- new version
- updated and enabled external ukrainian translation

* Thu Apr 12 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.17-alt0.M24.1
- new version
- disable external ukrainian translation (upstream merged)

* Wed Apr 11 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.16-alt0.M24.1
- new version
- updated ukrainian translation

* Wed Apr 11 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.15-alt0.M24.1
- new version

* Mon Apr 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.14-alt0.M24.1
- new version
- update & fix ukrainian translation

* Mon Apr 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.13-alt0.M24.2
- update & fix ukrainian translation

* Mon Apr 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.13-alt0.M24.1
- new version
- update smplayer-0.3.7_alt_dirs_optflags.diff for 0.3.13

* Sat Apr 07 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.12-alt0.M24.1
- new version
- disable external ukrainian translation (upstream merged)
- update & fix ukrainian translation

* Sat Apr 07 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.11-alt0.M24.1
- new version
- remove patch for QThread support (upstream merged)
- add external ukrainian translation

* Fri Apr 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.10-alt0.M24.1
- new version

* Fri Apr 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.9-alt0.M24.2 
- change patch for QThread support (author's variant)

* Fri Apr 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.9-alt0.M24.1
- new version
- add patch for QThread support (thanks to wRAR for hint)
- split building with Qt3 and Qt4 compilation
- remove patch for desktop-file for more informative (upstream merged)

* Thu Apr 05 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.8-alt0.M24.1
- new version
- update patch for desktop file for 0.3.8 version (upstream updated)

* Wed Apr 04 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.7-alt0.M24.3
- add russian comments into desktop file and to description

* Wed Apr 04 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.7-alt0.M24.2
- cleanup spec (upstream merged method for converting to Qt4)
- change creating menu-file method
- add patch for desktop-file for more informative

* Wed Apr 04 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.7-alt0.M24.1
- new version
- update smplayer-0.3.1_alt_dirs_optflags.diff for 0.3.7

* Tue Apr 03 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.6-alt0.M24.1
- new version
- disable external russian translation (upstream updated)

* Tue Apr 03 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.5-alt0.M24.1
- new version :-D

* Mon Apr 02 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.4-alt0.M24.1
- new version :-(

* Mon Apr 02 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.3-alt0.M24.1
- new version
- enable external russian translation (little fixed)

* Sun Apr 01 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.2-alt0.M24.1
- new version

* Fri Mar 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.M24.1
- new version
- disable external russian translation (upstream merged)
- update Patch0 for 0.3.1 version

* Thu Mar 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.M24.1
- new version
- update and fix russian translation

* Wed Mar 28 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.43-alt0.M24.2
- enable external russian translation (little fixed)

* Wed Mar 28 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.43-alt0.M24.1
- new version
- disable external russian translation (upstream merged)

* Tue Mar 27 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.42-alt0.M24.1
- new version
- update and fix russian translation for 0.2.42 version

* Mon Mar 26 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.41-alt0.M24.1
- new version
- update russian translation for 0.2.41 version

* Sun Mar 25 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.40-alt0.M24.1
- new version

* Fri Mar 23 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.38-alt0.M24.1
- new version
- little fixing into russian language file

* Wed Mar 21 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.30-alt0.M24.2
- add russian language (alpha)

* Sun Mar 18 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.30-alt0.M24.1
- new version

* Sat Mar 17 2007 Motsyo Gennadi <drool@altlinux.ru> 0.2.27-alt0.M24.1
- initial build for ALT Linux 2.4 Master

* Mon Feb 12 2007 Ricardo Villalba <rvm@escomposlinux.org>
  - first spec file
