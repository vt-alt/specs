
%define rname avidemux
%def_disable ownffmpeg
%def_disable xvba
%add_python_req_skip ADM_resize ADM_image

Name: avidemux-qt
Version: 2.7.6
Release: alt1

Group: Video
Summary: Avidemux is a graphical AVI files editor
Summary(ru_RU.UTF-8): Avidemux -- это редактор AVI-файлов с графическим интерфейсом
Url: http://avidemux.org/
License: GPL-2.0-only

ExcludeArch: armh

Provides: avidemux3 = %version-%release
Provides: avidemux2 = %version-%release
Obsoletes: avidemux2 < %version-%release
Provides: avidemux = %version-%release
Conflicts: avidemux

Source: avidemux-%version.tar
%if_enabled ownffmpeg
Source1: ffmpeg.tar.bz2
%endif
Source2: avidemux.desktop
Source3: http://gitorious.org/avidemux2-6/avidemux2-6/blobs/raw/7cf44bbc1f33894594b2bc84089d1779edc5c2b9/avidemux_plugins/ADM_autoScrips/lib/ADM_resize.py
Source4: avidemux_ru.ts

%if_enabled ownffmpeg
Patch1: avidemux-2.5.6-alt-ffmpeg-0.9.2.patch
%endif
Patch2: alt-i18n-qm-path.patch
Patch3: alt-crash-retranslate.patch
Patch4: alt-flags.patch
Patch5: alt-buildfix.patch
Patch6: alt-fix-find-x264.patch
Patch7: alt-other-arch.patch
#
Patch100: avidemux-2.5.1-opencore-check.patch

# Automatically added by buildreq on Mon Aug 24 2015 (-bi)
# optimized out: cmake-modules elfutils glibc-devel-static libEGL-devel libGL-devel libX11-devel libXext-devel libXv-devel libalsa-devel libgpg-error libjack-devel libjson-c libogg-devel libopencore-amrnb0 libopencore-amrwb0 libqt5-core libqt5-gui libqt5-script libqt5-widgets libqt5-xml libstdc++-devel libvorbis-devel libxcb-devel makeinfo perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage pkg-config python-base python3 python3-base qt5-base-devel rpm-build-gir rsync ruby ruby-stdlibs xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: bzlib-devel cmake gcc-c++ git-core libSDL-devel libXvMC-devel libaften-devel libarts-devel libdca-devel libfaad-devel liblame-devel liblzma-devel liblzo2-devel libopencore-amrnb-devel libopencore-amrwb-devel libpulseaudio-devel libsamplerate-devel libsqlite3-devel libva-devel libvdpau-devel libvpx-devel libx264-devel libx265-devel libxvid-devel nss-ldapd perl-podlators python-module-google qt5-script-devel qt5-tools rpm-build-python3 rpm-build-ruby texi2html xsltproc yasm zlib-devel-static
BuildRequires: bzlib-devel cmake gcc-c++ yasm glibc-devel libGL-devel libGLU-devel libSDL2-devel python-devel
BuildRequires: libdca-devel libfaad-devel libjack-devel liblame-devel libtwolame-devel libopus-devel
#BuildRequires: libaften-devel
BuildRequires: liblzma-devel liblzo2-devel libsqlite3-devel libfreetype-devel fontconfig-devel libfribidi-devel
BuildRequires: libopencore-amrnb-devel libopencore-amrwb-devel libpulseaudio-devel libsamplerate-devel
BuildRequires: libvdpau-devel libva-devel libXv-devel libXvMC-devel
%if_enabled xvba
BuildRequires: libxvba-devel
%endif
BuildRequires: libvorbis-devel libvpx-devel libx264-devel libx265-devel
BuildRequires: libass-devel liba52-devel libmad-devel libmp4v2-devel
BuildRequires: libxml2-devel libxvid-devel
BuildRequires: perl-podlators perl-IO-Compress texi2html
BuildRequires: qt5-base-devel qt5-script-devel qt5-tools
BuildRequires: xml-utils xsltproc yasm kde-common-devel libalsa-devel zlib-devel

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX
compatible encoder and the Gimp Toolkit (GTK) libraries.

%description -l ru_RU.UTF-8
Avidemux -- это редактор AVI-файлов с графическим интерфейсом.
Он позволяет монтировать видеосцены из видеофайлов и изображений
и добавлять к ним звуковую дорожку, а затем кодировать в файлы сжатых
форматов.

%package gui-qt
Group: Video
Summary: Qt GUI for %name
Requires(post,preun): alternatives >= 0.2
Requires: %name-common = %version-%release
Provides: %name-qui = %version-%release
Conflicts: %name <= 2.4.4-alt1
%description gui-qt
Qt GUI for %name

%package gui-gtk
Group: Video
Summary: GTK GUI for %name
Requires(post,preun): alternatives >= 0.2
Requires: %name-common = %version-%release
Provides: %name-qui = %version-%release
Conflicts: %name <= 2.4.4-alt1
%description gui-gtk
GTK GUI for %name

%package common
Group: Video
Summary: Common files for %name
Requires(post,preun): alternatives >= 0.2
Provides: %name-qui = %version-%release
Conflicts: %name <= 2.4.4-alt1
%description common
Common files for %name

%prep
%setup -qn %rname-%version
%if_enabled ownffmpeg
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%patch7 -p1
%patch100 -p1

#cp -f %SOURCE4 po/

%if_enabled ownffmpeg
install -m 0644 %SOURCE1 avidemux_core/ffmpeg_package
%endif

grep -rlw 'amd/amdxvba\.h' | xargs sed -i 's|amd/\(amdxvba\.h\)|\1|g'


%build
%add_optflags -Wno-error=return-type
export QTDIR=%_qt5_prefix
BUILDDIR=$PWD
sh bootStrap.bash \
    --with-core \
    --with-cli \
    --with-qt \
    --with-plugins \
    --with-system-libass \
    --with-system-liba52 \
    --with-system-libmad \
    --with-system-libmp4v2 \
    #
#lrelease-qt5 avidemux/qt4/i18n/*.ts
#for p in po/*.po ; do
#    FLNG=`echo "$p" | sed -e 's|\..*||' -e 's|.*\/||'`
#    msgfmt -o po/"$FLNG".mo $p
#done

%install
%set_verify_elf_method unresolved=relaxed,textrel=relaxed
cp -ar install/* %buildroot/
mkdir -p %buildroot/usr/
for d in bin include %_lib share
do
    [ -d "%buildroot/$d" ] || continue
    mv "%buildroot/$d" %buildroot/usr/
done

install -pD -m644 avidemux_icon.png %buildroot/%_pixmapsdir/%rname.png
install -pD -m644 %SOURCE2 %buildroot/%_desktopdir/org.avidemux.Avidemux.desktop
install -pD -m644 %SOURCE3 %buildroot/%_libdir/ADM_plugins6/autoScripts/lib/
ln -s avidemux3_qt5 %buildroot/%_bindir/%rname

#for p in po/*.mo ; do
#    LNG=`echo "$p" | sed -e 's|\..*||' -e 's|.*\/||' -e 's|@.*||'`
#    FLNG=`echo "$p" | sed -e 's|\..*||' -e 's|.*\/||'`
#    mkdir -p %buildroot/%_datadir/locale/"$LNG"/LC_MESSAGES
#    install -m 0644 po/"$FLNG".mo %buildroot/%_datadir/locale/"$LNG"/LC_MESSAGES/avidemux.mo
#done
#mkdir -p %buildroot/%_datadir/avidemux6/i18n/
#install -m 0644 lrelease-qt5 avidemux/qt4/i18n/avidemux*.qm %buildroot/%_datadir/avidemux6/i18n/

%find_lang --with-qt avidemux
#echo "%%defattr(644,root,root,755)" > avidemux.lang
#for f in %buildroot/%_datadir/avidemux6/i18n/avidemux*.qm
#do
#    LNG=`echo "$f"| sed -e 's|^.*/\(.*\)_\([a-z][a-z]\)[^[:alpha:]].*|\2|'`
#    FILE=%%_datadir/avidemux6/i18n/`basename "$f"`
#    echo "%%lang($LNG) $FILE" >>avidemux.lang
#done



%files -f avidemux.lang
%_desktopdir/org.avidemux.Avidemux.desktop
%_bindir/avidemux
%_bindir/avidemux3_cli
%_bindir/avidemux3_jobs*
%_bindir/avidemux3_qt5
%_libdir/libADM6*.so.*
%_libdir/libADM_*.so
%_libdir/ADM_plugins?/
#%_datadir/ADM_scripts
%dir %_datadir/avidemux6
%dir %_datadir/avidemux6/*/
%dir %_datadir/avidemux6/*/*
#%_datadir/avidemux6/help
%_iconsdir/hicolor/*/apps/org.avidemux.Avidemux.*

# devel
%exclude %_includedir/avidemux

%changelog
* Tue Aug 25 2020 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt1
- new version

* Mon Jun 29 2020 Sergey V Turchin <zerg@altlinux.org> 2.7.4-alt1
- new version
- don't build on armh

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 2.7.3-alt1
- new version (ALT#36355)

* Fri Feb 22 2019 Sergey V Turchin <zerg@altlinux.org> 2.7.1-alt2
- fix compile with gcc-8

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 2.7.1-alt1
- new version
- build on all arches

* Thu Jun 14 2018 Anton Farygin <rider@altlinux.ru> 2.7.0-alt2
- rebuilt with libva-2.1 
- build only on x86

* Tue Feb 27 2018 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt1
- new version

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 2.6.20-alt4
- rebuilt for new x264

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 2.6.20-alt3
- fix find x264

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 2.6.20-alt2
- fix compile flags
- fix find x264

* Wed Aug 09 2017 Sergey V Turchin <zerg@altlinux.org> 2.6.20-alt1
- new version

* Tue May 30 2017 Anton Farygin <rider@altlinux.ru> 2.6.15-alt1
- rebuild with new x265

* Wed Nov 30 2016 Sergey V Turchin <zerg@altlinux.org> 2.6.15-alt0.M80P.1
- build for M80P

* Wed Nov 30 2016 Sergey V Turchin <zerg@altlinux.org> 2.6.15-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 2.6.13-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 2.6.12-alt2
- fix build requires

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 2.6.12-alt1
- new version

* Wed Mar 09 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.10-alt2
- rebuilt with recent x264

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 2.6.10-alt1
- new version

* Wed Jul 23 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.8-alt2
- Convert Russian localization from gettext to qt linguist format

* Thu May 15 2014 Sergey V Turchin <zerg@altlinux.org> 2.6.8-alt1
- new version

* Tue May 13 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.7-alt3
- rebuilt with recent x264

* Sat Dec 28 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.7-alt2
- built with xvba support

* Fri Dec 27 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.7-alt1
- new version

* Fri Sep 13 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.5-alt1
- new version

* Wed Jun 26 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.4-alt1
- new version

* Thu Mar 07 2013 Sergey V Turchin <zerg@altlinux.org> 2.6.1-alt1
- new version

* Mon Nov 12 2012 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt1
- new version

* Mon Aug 06 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.6-alt0.M60P.1
- built for M60P

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.6-alt1
- new version
- built with internal ffmpeg-0.9.2

* Mon Apr 30 2012 Andrey Cherepanov <cas@altlinux.org> 2.5.5-alt0.M60P.2
- rebuilt with recent libx264

* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt2
- rebuilt with recent libvpx and libx264

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.5-alt0.M60P.1
- built for M60P

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.5-alt1
- new version

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.4-alt4.1
- rebuilt with recent x264

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt4
- fix build requires

* Wed Nov 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt3
- add Russian translation to desktop-file
- rebuilt with new x264

* Thu Oct 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt2
- fix build requires and desktop-file categories

* Thu Oct 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt1
- new version

* Sat Mar 21 2009 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt2
- fix build with gcc 4.3 (thanks, PLD)

* Thu Jul 31 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)
- rebuild without esound, without arts

* Tue Jul 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)
- cleanup spec, update buildreqs, build with xulrunner

* Thu Apr 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version (2.4)

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt0.1pre3
- 2.4pre3

* Fri Jul 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt0.1pre2
- new version (2.4) - fix bug #12441
- build with libaften
- set avidemux link to gtk binary

* Tue Feb 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- fixes from Michael Shigorin <mike@altlinux.org>:
 - built against firefox-devel, fixed multilib issue
 - replaced debian menu file with freedesktop one (from livna.org)
 - replaced build procedure (from rpmforge.net spec)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1
- new version 2.3.0 (with rpmrb script)

* Sun Aug 06 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt0.1pre2b
- 2.2.0pre, rebuild without libx264
- note: still wait for 2.3.0, 2.2.0 will never released
- add avidemux binary name

* Mon Jun 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.3
- rebuild with new libx264

* Thu May 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.2
- rebuild with dynamic libx264 (fix bug #9539)

* Wed Mar 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1
- new version 2.1.2 (with rpmrb script)
- rename package to avidemux
- disable build with arts
- cleanup spec with rpmcs

* Thu Dec 22 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt0.1
- new version

* Tue Nov 29 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt0.1step3
- new version

* Sun Oct 09 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt0.1step2
- new version

* Thu Dec 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.34-alt0.5test2
- 2.0.34-test2

* Sun Jun 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.24-alt1
- 2.0.24
- avidemux2.png as icon (thanks lav@) and fixed menu file (close #4448).

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.20-alt0.6
- rebuild with xvid-1.0.0rc1.

* Sun Dec 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.20-alt0.5
- 2.0.20

* Mon Nov 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.18-alt0.5
- 2.0.18

* Sat Sep 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.16-alt0.5
- 2.0.16

* Tue Aug 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.14-alt0.5
- 2.0.14

* Mon Jul 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.10-alt0.5
- 2.0.10

* Thu Jun 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt0.5
- First build for Sisyphus.

