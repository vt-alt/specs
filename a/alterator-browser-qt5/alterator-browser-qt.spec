%define qbIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define qbIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define qbIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define qbIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define alternatives_ver %{get_version alternatives}
%define alterator_cfg %_sysconfdir/alterator

%define bin_name alterator-browser-qt5
%define raw_name alterator-browser-qt

Name: %bin_name
Version: 3.1.4
Release: alt1

Source:%name-%version.tar

Summary: X11 Qt interface driver for alterator
License: GPL
Group: System/Configuration/Other
Packager: Sergey V Turchin <zerg at altlinux dot org>

PreReq(post,preun): alternatives >= 0.2
Requires: qt5-translations
Requires: qt5-virtualkeyboard
Requires: /usr/bin/xdg-open
Requires: alterator-browser-gui-common
Requires: alterator-common >= 2.9-alt0.14
Requires: alterator-icons
Provides: alterator-browser
Provides: alterator-browser-x11
Provides: alterator-browser-qt-light = 2.8-alt1
Obsoletes: alterator-browser-qt-light < 2.8-alt1
Provides: alterator-browser-qt = %version-%release
Obsoletes: alterator-browser-qt < %version-%release
Provides: alterator-browser-qt4 = %version-%release
Obsoletes: alterator-browser-qt4 < %version-%release
Obsoletes: alterator-look-qt

BuildRequires: libalternatives-devel
BuildRequires: libudev-devel
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools

%description
X11 Qt interface driver for alterator

%prep
%setup -q
%qmake_qt5

%build
%make_build
lrelease-qt5 %raw_name.pro

%install
%installqt5
mv  %buildroot/%_bindir/%raw_name %buildroot/%_bindir/%bin_name

# translations
mkdir -p %buildroot/%_qt5_translationdir
install -m 0644 translations/*.qm %buildroot/%_qt5_translationdir/

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name <<__EOF__
%_bindir/alterator-browser-x11	%_bindir/%bin_name 10
%_bindir/%raw_name	%_bindir/%bin_name 10
%_bindir/qtbrowser	%_bindir/%bin_name 10
__EOF__

#mkdir -p %buildroot/%alterator_cfg
#ln -s /dev/null %buildroot/%alterator_cfg/design-browser-qt
#mkdir -p %buildroot/%_datadir/%name/design
#ln -s %alterator_cfg/design-browser-qt %buildroot/%_datadir/%name/design/current

%find_lang --with-qt --all-name %name

%files -n %bin_name -f %name.lang
%config %_altdir/%bin_name
#%ghost %config %alterator_cfg/design-browser-qt
%_bindir/%bin_name
#%_datadir/%name/


%changelog
* Fri Feb 28 2020 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- don't crash on Wayland

* Wed Dec 04 2019 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- activate window without window manager
- show version in about dialog

* Tue Dec 03 2019 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt1
- update tooltips on language change

* Tue Dec 03 2019 Sergey V Turchin <zerg at altlinux dot org> 3.1.1-alt1
- update tooltips on language change

* Wed Sep 25 2019 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt1
- allow to disable virtual keyboard via env or kernel cmdline

* Fri Jun 14 2019 Sergey V Turchin <zerg at altlinux dot org> 3.0.5-alt2
- don't use ubt macro

* Thu Sep 20 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.5-alt1
- hide cursor on startup animation

* Mon Jun 18 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.4-alt1
- fix busy cursor on long alterator request

* Thu Jun 14 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.3-alt1
- set window icon

* Fri Apr 20 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.2-alt2
- require virtualkeyboard module

* Thu Mar 29 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.2-alt1
- startup animation small improvement

* Mon Mar 26 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.1-alt1
- set startup animation color according current color scheme

* Tue Mar 06 2018 Sergey V Turchin <zerg at altlinux dot org> 3.0.0-alt2
- obsolete alterator-browser-qt4

* Thu Dec 14 2017 Sergey V Turchin <zerg at altlinux dot org> 3.0.0-alt1
- enable High-DPI pixmaps by default

* Fri Jun 16 2017 Sergey V Turchin <zerg at altlinux dot org> 2.92.1-alt1
- fix to quit without confirmation

* Tue Jun 13 2017 Sergey V Turchin <zerg at altlinux dot org> 2.92.0-alt1
- handle closing main window

* Tue May 30 2017 Sergey V Turchin <zerg at altlinux dot org> 2.91.1-alt1
- enable high-DPI scaling by default

* Thu Apr 20 2017 Sergey V Turchin <zerg at altlinux dot org> 2.91.0-alt1
- add virtual keyboard support

* Mon Apr 17 2017 Sergey V Turchin <zerg at altlinux dot org> 2.90.4-alt1
- simplify timer usage

* Mon Apr 17 2017 Sergey V Turchin <zerg at altlinux dot org> 2.90.3-alt1
- fix i18n

* Fri Apr 14 2017 Sergey V Turchin <zerg at altlinux dot org> 2.90.2-alt1
- fix color scheme

* Fri Apr 14 2017 Sergey V Turchin <zerg at altlinux dot org> 2.90.1-alt1
- fix detect window manager

* Fri Apr 14 2017 Sergey V Turchin <zerg at altlinux dot org> 2.90.0-alt1
- port to Qt5

* Thu Apr 13 2017 Sergey V Turchin <zerg at altlinux dot org> 2.19.4-alt2
- rename package

* Tue Feb 18 2014 Sergey V Turchin <zerg at altlinux dot org> 2.19.4-alt1
- using QT_USE_FAST_CONCATENATION and QT_USE_FAST_OPERATOR_PLUS compile flags

* Tue Dec 03 2013 Sergey V Turchin <zerg at altlinux dot org> 2.19.3-alt1
- don't eat parentless items in checktree

* Fri Oct 11 2013 Sergey V Turchin <zerg at altlinux dot org> 2.19.2-alt1.M70P.1
- built for M70P

* Fri Oct 11 2013 Sergey V Turchin <zerg at altlinux dot org> 2.19.2-alt2
- update russian translation

* Wed Sep 25 2013 Sergey V Turchin <zerg at altlinux dot org> 2.19.2-alt1
- set tooltip for wizardface action "Next" (ALT#26187)

* Fri Jun 14 2013 Sergey V Turchin <zerg at altlinux dot org> 2.19.1-alt1
- fix displaysize delimiter

* Thu Jun 06 2013 Sergey V Turchin <zerg at altlinux dot org> 2.19.0-alt1
- add displaysize info widget

* Fri Apr 26 2013 Sergey V Turchin <zerg at altlinux dot org> 2.18.10-alt1
- fix signal/slot when selection changed in checktree

* Wed Apr 03 2013 Sergey V Turchin <zerg at altlinux dot org> 2.18.9-alt1
- fix event loop in checktree

* Tue Apr 02 2013 Sergey V Turchin <zerg at altlinux dot org> 2.18.8-alt1
- fix checktree event selected

* Thu Mar 28 2013 Sergey V Turchin <zerg at altlinux dot org> 2.18.7-alt1
- fix reading desktop-files

* Wed Mar 27 2013 Sergey V Turchin <zerg at altlinux dot org> 2.18.6-alt1
- return current item if no selected items in checktree

* Mon Mar 25 2013 Sergey V Turchin <zerg at altlinux dot org> 2.18.5-alt1
- update Kazakh translation (ALT#28747)

* Mon Oct 08 2012 Sergey V Turchin <zerg at altlinux dot org> 2.18.4-alt1
- fix to build with gcc 4.7

* Wed Jul 18 2012 Sergey V Turchin <zerg at altlinux dot org> 2.18.3-alt0.M60P.1
- built for M60P

* Wed Jul 18 2012 Sergey V Turchin <zerg at altlinux dot org> 2.18.3-alt1
- open urls from textbox and help browser by external browser
- set initial black background if no window manager

* Thu Jun 14 2012 Sergey V Turchin <zerg at altlinux dot org> 2.18.2-alt2
- fix to build with gcc-4.6

* Fri Jul 15 2011 Sergey V Turchin <zerg at altlinux dot org> 2.18.2-alt1
- fix iterator when changing dirs in slideshow

* Fri Jul 15 2011 Sergey V Turchin <zerg at altlinux dot org> 2.18.1-alt1
- fix crash on switch to next image in slideshow when stc dir empty

* Fri Jul 15 2011 Sergey V Turchin <zerg at altlinux dot org> 2.18.0-alt1
- add "prev" attribute for slideshow

* Thu Jul 14 2011 Sergey V Turchin <zerg at altlinux dot org> 2.17.2-alt1
- fix slideshow "step" attribute

* Wed Jul 13 2011 Sergey V Turchin <zerg at altlinux dot org> 2.17.1-alt1
- clean splashscreen borders

* Wed Jul 13 2011 Sergey V Turchin <zerg at altlinux dot org> 2.17.0-alt2
- remove debug messages

* Wed Jul 13 2011 Sergey V Turchin <zerg at altlinux dot org> 2.17.0-alt1
- add "once" and "next" attributes for slideshow (ALT#25896)

* Wed Apr 13 2011 Sergey V Turchin <zerg at altlinux dot org> 2.16.2-alt1
- show name of running external module

* Tue Apr 12 2011 Sergey V Turchin <zerg at altlinux dot org> 2.16.1-alt1
- don't freeze main window when external application running(ALT#25422)

* Mon Apr 11 2011 Sergey V Turchin <zerg at altlinux dot org> 2.16.0-alt1
- add external applications support for ACC

* Mon Mar 21 2011 Sergey V Turchin <zerg at altlinux dot org> 2.15.7-alt1
- fix path to mailbox socket for installer (ALT#25261)

* Fri Mar 18 2011 Sergey V Turchin <zerg at altlinux dot org> 2.15.6-alt1
- fix path to mailbox socket for installer

* Thu Mar 17 2011 Sergey V Turchin <zerg at altlinux dot org> 2.15.5-alt1
- move pidfile to alterator subdirectory

* Wed Mar 09 2011 Sergey V Turchin <zerg at altlinux dot org> 2.15.4-alt1
- add toolbar Quit button

* Mon Feb 28 2011 Sergey V Turchin <zerg at altlinux dot org> 2.15.3-alt1
- reduce spacing to remove installer vertical scrollbar when install packages

* Fri Jan 14 2011 Sergey V Turchin <zerg at altlinux dot org> 2.15.2-alt1
- update Ukrainian translation; thanks rom_as@alt

* Fri Oct 22 2010 Sergey V Turchin <zerg at altlinux dot org> 2.15.1-alt1
- fix theme:ok pixmap

* Fri Sep 17 2010 Sergey V Turchin <zerg at altlinux dot org> 2.15.0-alt1
- support animated gifs and mngs in slideshow

* Tue Sep 14 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.7-alt1
- some code cleanup

* Thu Sep 02 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.6-alt1
- remove workaround against bug in QThread::exec() from Connection

* Wed Aug 25 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.5-alt1
- fix uncheck corresponding items when set current-rows to checktree
- optimize checktree

* Tue Aug 24 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.4-alt1
- fix checktree event when changed

* Mon Aug 16 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.3-alt1
- add temporary workaround for broken QThread::exec() in Connection

* Fri Aug 06 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.2-alt1
- add workaround against brokern QThread::exec() in slideshow

* Fri Aug 06 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.1-alt1
- fix loop in checktree

* Thu Aug 05 2010 Sergey V Turchin <zerg at altlinux dot org> 2.14.0-alt1
- allow set tabbox tab label text to last tab with index "-1"
- checktree fixes

* Tue Jun 15 2010 Sergey V Turchin <zerg at altlinux dot org> 2.13.0-alt1
- add new widget checktree

* Tue Nov 24 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.3-alt0.M51.1
- built for M51

* Thu Nov 19 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.3-alt1
- set object name for splashscreen

* Thu Nov 12 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.2-alt1.M51.1
- built for M51

* Thu Nov 12 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.2-alt2
- fix cleanup attributes during new widget request

* Thu Nov 12 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.2-alt1
- don't force default style to Plastique
- don't spawn events when set additional attributes during new widget request
- more cleanup attributes during new widget request

* Wed Oct 14 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.1-alt1
- fix lost messagebox buttons (ALT#21934)

* Tue Oct 13 2009 Sergey V Turchin <zerg at altlinux dot org> 2.12.0-alt1
- allow to set misc widget attributes in new request
- remove tabpage widget; tabbox autopageable now

* Tue Sep 29 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.25-alt1
- fix switch help in centerface (ALT#21466)

* Thu Sep 24 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.24-alt1
- sort Tab order in centerface

* Thu Sep 10 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.23-alt1
- fix switching focus between radios by arrows (ALT#21390)

* Thu Sep 03 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.22-alt1
- fix possible broken initial focus order (ALT#21198)

* Wed Sep 02 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.21-alt1
- fix tab-index and tab-index on complex widgets

* Thu Aug 27 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.20-alt2
- fix retrieve unknown pixmap

* Wed Aug 26 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.20-alt1
- use altlinux icon for unknown pixmaps

* Tue Aug 25 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.19-alt3
- hide cursor over startup animation

* Mon Aug 17 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.19-alt2
- fix raise window when minimized and second browser instance started

* Tue Jun 23 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.19-alt1
- fix activating window when second browser instance started with Qt-4.5

* Tue Jun 09 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.18-alt1
- fix mailbox data encoding

* Fri Jun 05 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.17-alt1
- fix to terminate slideshow thread

* Thu May 07 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.16-alt1
- fix to change selection in listbox when space pressed
- don't set window position when have window manager
- allow to stop slideshow thread via (slideshow url "")

* Tue May 05 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.15-alt1
- add changed and return-pressed events for fileselect and colorselect

* Tue May 05 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.14-alt1
- apply color to colorselect button on editing text line

* Mon May 04 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.13-alt1
- use value attribute for fileselect and colorselect
- colorize button in colorselect

* Mon May 04 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.12-alt1
- add fileselect and colorselect widgets

* Thu Apr 30 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.11-alt1
- add options for file select request

* Wed Apr 29 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.10-alt1
- reduce widget spacing in controlface

* Wed Apr 29 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.9-alt1
- fix to slideshow startup

* Tue Apr 28 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.8-alt1
- load slideshow images from separate thread

* Tue Apr 21 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.7-alt1
- disable QSocketNotifier before Qt warning
- add attribte 'expanded' to gridbox

* Fri Apr 10 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.6-alt1.M50.1
- built for M50

* Fri Apr 10 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.6-alt2
- fix default currant_action_key in centerface
- update Russian translation

* Mon Apr 06 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.6-alt1
- fix gridbox widgets placement
- add 'changed' event to radio
- add 'expert' button to centerface

* Thu Mar 19 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.5-alt1
- improve spinbox extended slider-spinbox dependency
- don't use deprecated macroses

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.4-alt1
- don't use buttons for logo icons in wizardface

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.3-alt1
- fix crash via check group contains widget before remove it from group
- allow to switch wizardface steps list via clicking a logo

* Thu Feb 26 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.2-alt1
- hide wizardface steps list by default
- small wizardface lookout improvements

* Thu Feb 19 2009 Sergey V Turchin <zerg at altlinux dot org> 2.11.1-alt1
- new wizardface layout
- add widget grouping support
- add automatic grouping radios via widget grouping support
- fix to find unexistent pixmaps

* Sat Feb 14 2009 Sergey V Turchin <zerg at altlinux dot org> 2.10.5-alt1
- fix radio event toggled

* Mon Feb 09 2009 Sergey V Turchin <zerg at altlinux dot org> 2.10.4-alt2
- fix pidfile path

* Mon Feb 09 2009 Sergey V Turchin <zerg at altlinux dot org> 2.10.4-alt1
- fix to don't start timeedit on focus out when stopped

* Mon Dec 29 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.3-alt3
- handle focused "Prev" button when Enter pressed in wizardface

* Wed Dec 24 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.3-alt2
- fix question messagebox icon

* Fri Dec 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.3-alt1
- allow keyboard navigation in centerface
- handle alterator attribute "type" as Q_PROPERTY(alttype)
- fox focus proxy for spinbox

* Wed Dec 17 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.2-alt2.M41.2
- turn on own alternatives handling macroses

* Wed Dec 10 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.2-alt2.M41.1
- built for M41

* Wed Dec 10 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.2-alt3
- fix to hide dialogs before closing

* Tue Dec 09 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.2-alt2
- fix closing dialogs

* Mon Dec 01 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.2-alt1
- fix loop QEvents

* Thu Nov 27 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.1-alt1
- add attribute 'expanded' to spinbox (shows slider)

* Wed Nov 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.0-alt2
- fix to set sefault focus to new popup

* Wed Nov 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2.10.0-alt1
- fix crash at quit (#14490)
- remove constraints support (#16120)

* Wed Nov 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.101-alt1
- activate window of already running browser when start new
- save current help for centerface modules list
- disable centerface Main button during modules list view

* Fri Nov 14 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.100-alt1
- add value attribute to textbox

* Fri Nov 14 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.99-alt2
- fix to set altgroup to proper widget

* Thu Nov 13 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.99-alt1
- handle alterator attribute "name" as Q_PROPERTY(altgroup)

* Wed Nov 05 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.98-alt2
- fix to word wrap messageboxes text by default

* Wed Nov 05 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.98-alt1
- allow to push any focused/default button by Enter in any dialog
- fix to restore help browser vertical scroll position

* Sat Nov 01 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.97-alt1
- make all popups windowless

* Fri Oct 10 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.96-alt1
- add URL handler to help browser
- add dummy URL handler to textbox

* Fri Sep 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.95-alt1
- allow to set background image to AMainWidget AWizardFace ACenterface via QSS

* Fri Sep 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.94-alt1
- fix to use parent background of wizardface and centerface views

* Thu Sep 25 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.93-alt2
- fix build on x86_64

* Wed Sep 24 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.93-alt1
- fix crash when set busy cursor with no active window

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.92-alt1
- fix timeedit dateedit return values

* Mon Aug 18 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.91-alt1
- add autocompletion support for edit widget

* Tue Aug 05 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.90-alt1
- add event changed to listbox, combobox, checkbox
- add value attribute to timeedit, dateedit

* Sat Jun 07 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.89-alt1
- improve wizardface and dialog scroll area focus handling

* Sat Jun 07 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.88-alt1
- fix typo when wizardface create requested
- don't use sub-type to determine dialog or main window
- make help and owerview buttons visible on top in centerface

* Fri Jun 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.87-alt1
- fix set *listbox current-rows attribute
- no signal selected from *listbox when
  alterator set current, current-rows, state-rows attributes

* Fri Jun 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.86-alt1
- fix to make splash a non-window to avoid crash
- hide old module while new is not shown in centerface

* Wed Jun 04 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.85-alt1
- add linkbutton widget
- fix mailbox
- fix dialog actions support
- fix centerface look

* Tue Jun 03 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.84-alt1
- new centerface widget API

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.83-alt2
- turn on Enter key support in wizardface

* Fri May 30 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.83-alt1
- fix #15792

* Fri May 30 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.82-alt1
- fix *listbox state-rows attribute
- force return *multi*listbox current-rows and state-rows if empty list

* Thu May 29 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.81-alt1
- fix clear-layout attribute
- fix centerface modules attribute

* Wed May 28 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.80-alt1
- send "selected" signal when selection changed to none in listbox
- don't quote *listbox return
- set busy cursor on dialogs too

* Tue May 27 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.79-alt1
- fix checklistbox feel

* Mon May 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.78-alt1
- release centerface widget
- clean wizarface signal mapper when action removed

* Fri May 23 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.77-alt4
- don't quote current-action and current-module in centerface result
- remove centerface debug widgets

* Thu May 22 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.77-alt3
- don't quote current-action and current-step in wizardface result

* Thu May 22 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.77-alt2
- fix to return value by checkbox

* Wed May 21 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.77-alt1
- add value attribute to checkbox
- initial centerface widget

* Mon May 12 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.76-alt1
- add value attribute for edit widget
- add window-title value attribute for all widgets
- hbox == box

* Wed Apr 16 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.75-alt1
- add wizardface step-text step-pixmap action-text action-pixmap attributes

* Fri Apr 11 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.74-alt1
- fix setting window title
- fix checklistbox

* Thu Apr 03 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.73-alt1
- add file selection alterator request support

* Thu Apr 03 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.72-alt1
- add message translations
- rename title_text to wizardface_title_text

* Thu Mar 20 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.71-alt6
- minimize buttons in gridbox

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.71-alt5
- allow multivalue for align attribute

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.71-alt4
- fix focus attribute for timeedit dateedit edit and textbox

* Mon Mar 17 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.71-alt3
- remove window title from wizardface step name area
- remove unused widget attributes

* Wed Mar 12 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.71-alt2
- fix typo in /usr/share/alterator/design/images path

* Fri Mar 07 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.71-alt1
- add /usr/share/alterator/design/images to pixmaps search paths list

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.70-alt1
- add url attribute to textbox
- add step (milliseconds) attribute to slideshow (0 == stop)
- add window-title attribute for all widgets
- add radiolistbox, mutlilistbox, checklistbox widgets
- add current-rows and state-rows attributes for
  listbox radiolistbox mutlilistbox checklistbox

* Tue Feb 12 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.69-alt4
- fix title in wizardface

* Wed Feb 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.69-alt3
- add window title to wizardface step name area

* Thu Jan 10 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.69-alt2
- box, hbox, box widgets are deprecated. Use gridbox instead.

* Wed Jan 09 2008 Sergey V Turchin <zerg at altlinux dot org> 2.9.69-alt1
- remove help-place widget

* Thu Dec 20 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.68-alt1
- move additional actions to menu if all actions more then 4 in wizardface
- no text on menu button
- add has-help attribute to main_widget for global help switch off

* Fri Dec 07 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.67-alt1
- don't cut "\n" from alterator input

* Mon Nov 12 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.66-alt1
- fix "align" attribute

* Mon Nov 12 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.65-alt1
- fix to skip empty input from alterator
- don't return text if textbox read-only
- add min-width min-height attributes

* Tue Oct 30 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.64-alt1
- fix clear steps in wizardface "steps" attribute
- fix to use QTextStream instead iostream in alterator IO
- make elements a separate object

* Fri Oct 05 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.63-alt5
- fix press Esc in help dialog

* Fri Oct 05 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.63-alt4
- add egg by F1,F1

* Thu Oct 04 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.63-alt3
- fix check action exist when add to wizardface

* Wed Oct 03 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.63-alt2
- fix scrooll help to old position

* Wed Oct 03 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.63-alt1
- create help widget in runtime to retranslate UI and reduce memory usage 

* Wed Sep 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.62-alt2
- fix timedit time format

* Mon Aug 27 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.62-alt1
- show seconds in timeedit in non-latin locales
- fix cursor position for window-magagerless popup dialogs

* Fri Aug 24 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.61-alt1
- make "Next/Finish" in wizardface by F12
- get all pixmaps via design

* Wed Aug 08 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.60-alt1
- reset all timeedit widgets when forward clicked in wizardface

* Fri Aug 03 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.59-alt2
- add reset parameter to timeedit

* Fri Aug 03 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.59-alt1
- stop timeedit clock when editing time

* Fri Jul 13 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.58-alt1
- don't use background pixmap for timeedit clock

* Wed Jul 11 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.57-alt2
- fix analog clock hour arrow position
- set "main_widget" object name for main widget

* Wed Jul 11 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.57-alt1
- fix keyboard focus on windowmanager-less popups 
- show splashscreen on top only without window manager
- don't draw the inner frame on windowmanager-less popups
- fix set title for main window

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.56-alt1
- don't hide splashscreen when clicked by mouse
- override theme:* pixmaps by browser-design
- override whirl.mng by browser-design

* Thu Jul 05 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.55-alt2
- align progressbar text Qt-style independent

* Fri Jun 29 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.55-alt1
- fix find icon pixmaps
- fix tab-index attribute
- add rowspan,colspan attributes for all widgets (grigbox childs only)
- internal improvements

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.54-alt2
- identify wizardface title text widget for QSS
- load only PNG and JPG for icon pixmaps

* Thu Jun 14 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.54-alt1
- identify wizardface view widget for QSS
- add design directory

* Fri Jun 01 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.53-alt1
- add startup animation

* Fri Jun 01 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.52-alt1
- fix setup columns size for splitbox
- separate initial alterator request to thread
  to possible view busy mouse cursor

* Thu May 31 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.51-alt1
- add splitbox widget

* Fri May 11 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.50-alt1
- add updated() signal to combobox 

* Mon May 07 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.49-alt1
- add multiple excluding values to constraints

* Tue Apr 24 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.48-alt4
- don't disable UI during special request to alterator

* Mon Apr 23 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.48-alt3
- disable UI during special request to alterator

* Mon Apr 16 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.48-alt2
- remove Help button by default from wizardface

* Tue Apr 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.48-alt1
- fix set language from alterator
- remove tab-order attribute, add tab-index

* Thu Apr 05 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.47-alt1
- fix early igniring outgouing events during special request to alterator

* Tue Apr 03 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.46-alt1
- add possibility to ignore outgoing events during special request to alterator
- support one-file design themes
- add tab-order, focus attributes to all widgets
- add possibility remove focus from fidget

* Wed Mar 28 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.45-alt2
- small UI fix

* Fri Mar 23 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.45-alt1
- add slideshow widget
- add custom GUI design support

* Mon Mar 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.44-alt1
- add locale guessing fix from ldv@alt
- use internal QObject timers instead QTimer
- use pixmap for timeedit clock background
- use only alMultiListBox for lisbbox
- rearrange wizardface widgets with bottomleft logo
				    
* Tue Mar 13 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.43-alt1
- add start/stop attributes to timeedit
- rearrange wizardface widgets

* Mon Mar 12 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.42-alt1
- make analog clock in timeedit
- use steps icons in wizardface

* Fri Mar 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.41-alt2
- fix expanded attribute

* Mon Mar 05 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.41-alt1
- add dateedit and timeedit widgets
- make tabbox::current a numeric
	    
* Mon Mar 05 2007 Stanislav Ievlev <inger@altlinux.org> 2.9.40-alt1.1
- add tabbox selected event callback

* Tue Feb 27 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.40-alt1
- turn constraints on
- wait request thread before quit
- don't using splash when long request to alterator

* Thu Feb 22 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.39-alt1
- rename "text" attribute to "current-text" for combobox
- show splash when long request to alterator

* Fri Feb 16 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.38-alt1
- resize columns when insert rows to multicolumn listbox
- change language on language change request
- add text to menu button in wizardface
- don't use alternate color in 1-column listbox
- add width/height attribute for all widgets
- use alternate color in multicolumn listbox and tree
- fix scrollbars on initial showing of textbox with text

* Wed Feb 14 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.37-alt1
- add "text" attrubute to combobox
- add "expanded" attrubute to tree

* Tue Feb 13 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.36-alt1
- prefer user defined orientation in separator
- allow to inherit orientation from tabbox to tabpage
- remove selection on set current < 0 in tree and listbox

* Mon Feb 12 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.35-alt2
- fix spinbox event "changed"

* Fri Feb 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.35-alt1
- obsolete old alterator-browser-qt-light
- add margin/spacing attribute for container widgets

* Tue Feb 06 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.34-alt1
- auto-adjust first column width in tree
- allow insert html into textbox
- add text-wrap attribute to label
- add text attribute to progressbar

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.33-alt1
- fix edit return-pressed event

* Thu Jan 25 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.32-alt3
- change edit return-pressed event
  from QLineEdit::returnPressed() to QLineEdit::editingFinished() 

* Thu Jan 25 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.32-alt2
- fix dialog popup

* Wed Jan 24 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.32-alt1
- add gridbox widget

* Mon Jan 15 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.31-alt1
- fix splitter, rename to separator
- fix help button position
- add orientation to dialog mainwidget and wizardface

* Fri Jan 12 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.30-alt1
- temporary add width/height for dialogs

* Wed Jan 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.29-alt1
- move browser socket into alterator sub-directory

* Wed Jan 10 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.28-alt1
- add orientation(default vertical) attribute to container widgets

* Tue Jan 09 2007 Sergey V Turchin <zerg at altlinux dot org> 2.9.27-alt2
- fix cursor names

* Fri Dec 29 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.27-alt1
- add cursor attribute
- add actions to dialog
- add spinbox widget

* Tue Dec 26 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.26-alt1
- add wizardface default tranlations
- add help item to wizardface by default

* Fri Dec 22 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.25-alt1
- add internal messaging system support

* Tue Dec 19 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.24-alt1
- add widgets: vtabbox, htabbox, vtab-page, htab-page
- show help browser when wizardface menu item activated

* Thu Dec 14 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.23-alt4
- anonymize widget and all it's children before delete

* Wed Dec 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.23-alt3
- fix updated signal from checkbox

* Wed Dec 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.23-alt2
- set default help text

* Wed Dec 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.23-alt1
- add constraints to edit, textedit
- add messagebox buttons translation
- display step numers from 1 in wizardface

* Tue Dec 12 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.22-alt1
- change steps visibility

* Tue Dec 12 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.21-alt3
- turn off children-align attribute

* Mon Dec 11 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.21-alt2
- don't show empty steps list

* Mon Dec 11 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.21-alt1
- return children-align attribute
- add align attribute

* Fri Dec 08 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.20-alt1
- implement help browser
- reduce events flood from slider

* Thu Dec 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.19-alt2
- fix messagebox buttons size

* Thu Dec 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.19-alt1
- add max-width, max-height attributes

* Mon Dec 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.18-alt1
- fix full-screen mode

* Mon Dec 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.17-alt3
- fix LANGUAGE detection

* Fri Dec 01 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.17-alt2
- fix messagebox borders and placement
- add workaround against showing dialogs when loaded

* Thu Nov 30 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.17-alt1
- fix button and label size

* Thu Nov 30 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.16-alt1
- fix cleaning widgets

* Wed Nov 29 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.15-alt1
- add base constraints support

* Wed Nov 29 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.14-alt1
- add spacer widget

* Tue Nov 21 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.13-alt3
- fix tree/columns

* Tue Nov 21 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.13-alt2
- fix listbox/double-click, wizardface/title

* Mon Nov 20 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.13-alt1
- add rows-clear attribute to listbox/combobox

* Fri Nov 17 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.12-alt4
- fix wizardface menu actions attributes

* Fri Nov 17 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.12-alt3
- stable wizardface API

* Fri Nov 17 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.12-alt2
- fix current attribute for wizardface

* Thu Nov 16 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.12-alt1
- new wizardface API

* Mon Nov 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.11-alt1
- fix document:popup-*
- new wizardface interface

* Fri Nov 10 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.10-alt1
- update to new alterator

* Thu Nov 02 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.9-alt2
- small widgets layout fix

* Tue Oct 31 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.9-alt1
- ignore attributes: layout-policy, width, height, align, children-align,
  background-color

* Mon Oct 23 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.8-alt1
- fix window manager detection

* Fri Oct 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.7-alt1
- fix dialog borders

* Thu Oct 12 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.6-alt1
- detect Window Manager

* Tue Oct 10 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.5-alt1
- update to new alterator

* Mon Oct 09 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.4-alt4
- update to new alterator

* Mon Oct 09 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.4-alt3
- add some fixes for new alterator

* Fri Oct 06 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.4-alt2
- fix draw primitives with Qt-4.2

* Tue Sep 26 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.4-alt1
- apply default icons to wizardface buttons
- arrange buttons in wizardface

* Mon Sep 25 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.3-alt1
- autowrap text on labels
- add current and title attributes to wizardface
- require alterator-icons

* Wed Jul 12 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.2-alt1
- update to new alterator

* Tue Jun 20 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.1-alt5
- add changed event to silder

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.1-alt4
- add value attribute to slider

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.1-alt3
- fix slider attributes

* Thu Jun 15 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.1-alt2
- add slider,splitter widgets

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2.9.1-alt1
- update to new alterator

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt24
- turn off modeless dialogs

* Tue May 30 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt23
- add fix for tree

* Tue May 30 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt22
- make listbox clicked by space 

* Wed May 24 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt21
- fix compile with new gcc

* Thu May 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt20
- update to new alterator

* Fri Apr 28 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt19
- update to vector based model
- fix problems with multiline textboxes

* Fri Apr 21 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt18
- add scrolling to wizardface inner widget

* Thu Apr 20 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt17
- improve pixmap theme handling

* Fri Apr 14 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt16
- change language selection order

* Thu Apr 13 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt15
- rename some standard pixmaps to better understanding by ID

* Wed Apr 12 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt14
- update standatd pixmaps list

* Tue Apr 11 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt13
- rename items to rows
- add pixmaps caching
- add support for internal Qt pixmaps

* Thu Apr 06 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt12
- add alTree fixes

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt11
- add patch fix for item-text and item-pixmap in multicolon listbox

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt10
- don't use alMultiListBox for 1 column

* Tue Apr 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt9
- add alMultiListBox
- add alHelpPlace

* Fri Mar 31 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt8
- add alTree

* Fri Mar 31 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt7
- fix combobox post items

* Thu Mar 30 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt6
- add (combobox alterability)

* Tue Mar 28 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt5
- save window geometry on exit

* Thu Mar 23 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt4
- add (listbox on-double-click)

* Tue Mar 21 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt3
- add progressbar
- add alProxy

* Fri Mar 17 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt2
- add on-click, on-return to listbox
- add on-return to edit
- add on-click to listbox

* Wed Mar 15 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6.1-alt1
- add align for label
- add widget named root and symlink to vbox
- add sax optimization

* Tue Mar 14 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6-alt14
- clear listbox and combobox when add list of items

* Thu Mar 09 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6-alt13
- add items property to listbox and combobox

* Mon Mar 06 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6-alt12
- fix current item when listbox on-select

* Wed Feb 22 2006 Sergey V Turchin <zerg at altlinux dot org> 2.6-alt11
- separate main window
- start full-screen without window manager

* Tue Feb 21 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt10
- improve language selection

* Wed Feb 08 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt9
- listbox fixes (indentation + auto-scrolling)

* Tue Feb 07 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt8.1
- little layout fixes

* Mon Feb 06 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt8
- resurrect old hacks for QDialog
- added support for full-screen

* Fri Jan 27 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt7.2
- added support for splashes

* Fri Jan 27 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt7.1
- added support for tooltips

* Mon Jan 23 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt7
- change DOM parser to SAX

* Fri Jan 20 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt6.4
- tabbox current property fix

* Thu Jan 19 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt6.3
- performance fix

* Wed Jan 18 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt6.2
- layout bugfix

* Mon Jan 16 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt6.1
- replace QListWidget with QTreeWidget

* Wed Jan 11 2006 Stanislav Ievlev <inger@altlinux.org> 2.6-alt6
- added support for radio-buttons and spacers

* Thu Dec 22 2005 Stanislav Ievlev <inger@altlinux.org> 2.6-alt5
- added support for timers

* Tue Dec 20 2005 Stanislav Ievlev <inger@altlinux.org> 2.6-alt4
- improve initial connection
- ressurect locale support

* Mon Dec 19 2005 Stanislav Ievlev <inger@altlinux.org> 2.6-alt3
- fixed layout

* Fri Dec 16 2005 Stanislav Ievlev <inger@altlinux.org> 2.6-alt2
- fixed xml support

* Thu Dec 15 2005 Stanislav Ievlev <inger@altlinux.org> 2.6-alt1.1
- fixed provides

* Thu Dec 08 2005 Stanislav Ievlev <inger@altlinux.org> 2.6-alt1
- now as qtbrowser

* Fri Dec 02 2005 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.4.2
- little code cleanup

* Thu Dec 01 2005 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.4.1
- fixed support for pixmap attribute of button

* Wed Nov 30 2005 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.4
- added children-align property support

* Tue Nov 29 2005 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.3
- fixed bugs

* Thu Nov 03 2005 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.2
- improvements

* Wed Nov 02 2005 Stanislav Ievlev <inger@altlinux.org> 2.5-alt0.1
- build current unstable version

* Wed Aug 31 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1-alt0.3
- add border to splash

* Tue Aug 30 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1-alt0.2
- new widgets layout
- scrollview widget for module window
- fix splash background color

* Tue Aug 30 2005 Stanislav Ievlev <inger@altlinux.org> 2.1-alt0.1
- initial build (specially for zerg)

