%def_with inotify
%def_without fam
%def_enable qtgui
%def_enable webkit

%define pre %nil

Name: recoll
Version: 1.25.22
Release: alt1

Summary: A personal full text search package
License: %gpl2plus
Group: File tools

Url: http://www.recoll.org
Source0: %url/%name-%version%pre.tar.gz
Source1: recoll_ru.ts
Source2: recoll_ru.qm
Source3: recoll_uk.ts
Source4: recoll_uk.qm
# 1.24.1+ru
Source5: recoll-searchgui.desktop
Source100: recoll.watch

Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ libaspell-devel ImageMagick
%{?_with_fam:BuildRequires: libfam-devel}
BuildRequires: libxapian-devel >= 0.9
BuildRequires: rpm-build-licenses
BuildRequires: perl-Image-ExifTool
BuildRequires: zlib-devel
BuildRequires: libaspell-devel
BuildRequires: libchm-devel
BuildRequires: libxslt-devel
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%if_enabled qtgui
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools-devel libXt-devel xorg-cf-files
%if_enabled webkit
BuildRequires: qt5-webkit-devel
%endif
%endif

%add_findreq_skiplist %_datadir/%name/filters/*
%add_findreq_skiplist %_datadir/%name/examples/*

%description
Recoll is a personal full text search package based on a very strong
backend (Xapian), for which it provides an easy to use, feature-rich,
easy administration interface.

See also recoll-extras package for somewhat more exotic stuff.
%if_disabled qtgui

Note that this package has been built without its usual GUI.
%endif

%package extras
Summary: More helper scripts for Recoll
Group: File tools
Requires: %name = %version
BuildArch: noarch

%description extras
This package contains additional helper scripts for recoll which might
need bulky additional required packages, manual setup, or both.

%package full
Summary: All the recommended stuff for Recoll
Group: File tools
BuildArch: noarch
Requires: %name-extras = %version
Requires: perl-Image-ExifTool
Requires: antiword unrtf wv
Requires: python-module-pychm python3-module-lxml
Requires: aspell aspell-ru-rk
Requires: xpdf-utils ghostscript-utils

%description full
This package contains just the requirements for additional packages
that might be of use with Recoll.

%package -n python3-module-%name
Summary: Python bindings for Recoll
Group: Development/Python
Obsoletes: python-module-%name

%description -n python3-module-%name
This package contains Python bindings for Recoll.

%prep
%setup -n %name-%version%pre

sed -i 's/openoffice/loffice/' sampleconf/mimeview
sed -i '/^Categories=/s/=/=Qt;/' desktop/*.desktop
# updated translations: ru
cp -a %SOURCE1 %SOURCE2 qtgui/i18n/
cp -a %SOURCE5 desktop/

%build
export CXXFLAGS="%optflags" PATH="$PATH:%_libdir/qt5/bin"
export QMAKE=qmake-qt5
%configure \
	%{subst_with inotify} \
	%{subst_with fam} \
	%{subst_enable qtgui} \
	%{subst_enable webkit} \
	#
%make_build
gzip --best --keep --force ChangeLog
for s in 128 96 72 64 36 32 24 22 16; do
    convert -depth 8 -resize ${s}x$s desktop/%name{.xcf,-$s.png}
done

%install
%makeinstall_std INSTALL_ROOT=%buildroot
for s in 128 96 72 64 36 32 24 22 16; do
    install -pDm644 desktop/%name-$s.png %buildroot%_iconsdir/hicolor/${s}x$s/apps/%name.png
done
sed -i 's/xterm/xvt/g' %buildroot%_datadir/%name/filters/*

# use /usr/bin/xdg-open
rm -f %buildroot%_datadir/%name/filters/xdg-open

%files
%_bindir/*
%_libdir/%name
%_datadir/%name
%exclude %_datadir/%name/filters/rcllyx
%exclude %_datadir/%name/filters/*.py
%exclude %_datadir/%name/filters/*.zip
%if_enabled qtgui
%_datadir/appdata/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*
%_desktopdir/*
%endif
%_man1dir/*
%_man5dir/*
%doc ChangeLog.* README

%files extras
%_datadir/%name/filters/rcllyx
%_datadir/%name/filters/*.py
%_datadir/%name/filters/*.zip

%files full

%files -n python3-module-%name
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%name/
%python3_sitelibdir/recollchm/

%changelog
* Thu Aug 29 2019 Michael Shigorin <mike@altlinux.org> 1.25.22-alt1
- new version (watch file uupdate)

* Thu Aug 29 2019 Michael Shigorin <mike@altlinux.org> 1.25.21-alt2
- updated -full subpackage dependencies (closes: #37146)

* Mon Aug 26 2019 Michael Shigorin <mike@altlinux.org> 1.25.21-alt1
- new version (watch file uupdate)

* Mon Aug 05 2019 Michael Shigorin <mike@altlinux.org> 1.25.20-alt1
- new version (watch file uupdate)

* Thu Jun 13 2019 Michael Shigorin <mike@altlinux.org> 1.25.19-alt1
- new version (watch file uupdate)

* Tue May 28 2019 Michael Shigorin <mike@altlinux.org> 1.25.18-alt1
- new version (watch file uupdate)

* Wed May 22 2019 Michael Shigorin <mike@altlinux.org> 1.25.16-alt1
- new version (watch file uupdate)

* Sun Apr 28 2019 Michael Shigorin <mike@altlinux.org> 1.25.15-alt1
- new version (watch file uupdate)

* Sun Apr 14 2019 Michael Shigorin <mike@altlinux.org> 1.25.13-alt1
- new version (watch file uupdate)

* Fri Apr 12 2019 Michael Shigorin <mike@altlinux.org> 1.25.12-alt1
- new version (watch file uupdate)

* Fri Mar 29 2019 Michael Shigorin <mike@altlinux.org> 1.25.11-alt1
- new version (watch file uupdate)

* Tue Mar 26 2019 Michael Shigorin <mike@altlinux.org> 1.25.10-alt1
- new version (watch file uupdate)

* Sat Mar 23 2019 Michael Shigorin <mike@altlinux.org> 1.25.9-alt1
- new version (watch file uupdate)

* Fri Mar 22 2019 Michael Shigorin <mike@altlinux.org> 1.25.8-alt1
- new version (watch file uupdate)

* Thu Mar 07 2019 Michael Shigorin <mike@altlinux.org> 1.25.5-alt1
- new version (watch file uupdate)

* Sun Feb 24 2019 Michael Shigorin <mike@altlinux.org> 1.25.4-alt1
- new version (watch file uupdate)
- built with libchm

* Fri Feb 01 2019 Michael Shigorin <mike@altlinux.org> 1.24.5-alt1
- new version (watch file uupdate)

* Fri Nov 16 2018 Michael Shigorin <mike@altlinux.org> 1.24.3-alt1
- new version (watch file uupdate)
- dropped upstream patch

* Fri Sep 21 2018 Michael Shigorin <mike@altlinux.org> 1.24.1-alt2
- merged underwit@'s work:
  + updated Russian translations
  + qt5.11 patch suggested by upstream
- merged shaba@'s suggestions:
  + added python-module-recoll subpackage
  + disabled fam (inotify is enabled already)
  + build with system aspell
- s/ooffice/loffice/

* Mon May 14 2018 Michael Shigorin <mike@altlinux.org> 1.24.1-alt1
- new version (watch file uupdate)

* Tue Apr 10 2018 Michael Shigorin <mike@altlinux.org> 1.24.0-alt1
- new version (watch file uupdate)

* Wed Jan 10 2018 Michael Shigorin <mike@altlinux.org> 1.23.7-alt2
- fix build with webkit disabled: both patches already in release

* Tue Jan 09 2018 Michael Shigorin <mike@altlinux.org> 1.23.7-alt1
- new version (watch file uupdate)

* Sat Dec 09 2017 Michael Shigorin <mike@altlinux.org> 1.23.6-alt1
- new version (watch file uupdate)

* Fri Dec 01 2017 Michael Shigorin <mike@altlinux.org> 1.23.5-alt1
- new version (watch file uupdate)

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.23.3-alt3
- Rebuilt with new xapian.

* Fri Sep 08 2017 Michael Shigorin <mike@altlinux.org> 1.23.3-alt2
- build against qt5

* Wed Sep 06 2017 Michael Shigorin <mike@altlinux.org> 1.23.3-alt1
- new version (watch file uupdate)

* Tue May 16 2017 Michael Shigorin <mike@altlinux.org> 1.23.2-alt1
- new version (watch file uupdate)

* Tue Mar 14 2017 Michael Shigorin <mike@altlinux.org> 1.23.1-alt1
- new version (watch file uupdate)

* Thu Mar 09 2017 Michael Shigorin <mike@altlinux.org> 1.23.0-alt1
- new version (watch file uupdate)

* Sun Dec 04 2016 Michael Shigorin <mike@altlinux.org> 1.22.4-alt1
- new version (watch file uupdate)

* Wed Jun 22 2016 Michael Shigorin <mike@altlinux.org> 1.22.3-alt1
- new version (watch file uupdate)

* Thu Jun 16 2016 Michael Shigorin <mike@altlinux.org> 1.22.2-alt1
- new version (watch file uupdate)

* Wed Jun 15 2016 Michael Shigorin <mike@altlinux.org> 1.22.1-alt1
- new version (watch file uupdate)

* Fri Apr 15 2016 Michael Shigorin <mike@altlinux.org> 1.22.0-alt1
- new version (watch file uupdate)
- fixed installation

* Fri Apr 08 2016 Michael Shigorin <mike@altlinux.org> 1.21.6-alt1
- new version (watch file uupdate)

* Sun Jan 31 2016 Michael Shigorin <mike@altlinux.org> 1.21.5-alt1
- new version (watch file uupdate)

* Wed Jan 13 2016 Michael Shigorin <mike@altlinux.org> 1.21.4-alt1
- new version (watch file uupdate)

* Sat Oct 31 2015 Michael Shigorin <mike@altlinux.org> 1.21.3-alt1
- new version (watch file uupdate)

* Thu Oct 01 2015 Michael Shigorin <mike@altlinux.org> 1.21.2-alt1
- new version (watch file uupdate)

* Thu Aug 06 2015 Michael Shigorin <mike@altlinux.org> 1.21.1-alt1
- new version (watch file uupdate)
- made qtgui build conditional

* Fri Jun 19 2015 Michael Shigorin <mike@altlinux.org> 1.21.0-alt1
- new version (watch file uupdate)

* Fri May 22 2015 Michael Shigorin <mike@altlinux.org> 1.20.6-alt2
- rebuilt against libxapian 1.2.21

* Mon Apr 27 2015 Michael Shigorin <mike@altlinux.org> 1.20.6-alt1
- new version (watch file uupdate)

* Mon Apr 06 2015 Michael Shigorin <mike@altlinux.org> 1.20.5-alt1
- new version (watch file uupdate)
- qt5 compat tweaks

* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 1.20.4-alt1
- new version (watch file uupdate)

* Sun Mar 29 2015 Michael Shigorin <mike@altlinux.org> 1.20.3-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 1.20.2-alt1
- new version (watch file uupdate)

* Fri Dec 26 2014 Michael Shigorin <mike@altlinux.org> 1.20.1-alt1
- new version (watch file uupdate)
- added appdata file

* Tue Jul 29 2014 Michael Shigorin <mike@altlinux.org> 1.20.0p2-alt1
- new version (watch file uupdate)

* Tue Jul 29 2014 Michael Shigorin <mike@altlinux.org> 1.20.0p1-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 1.20.0-alt1
- new version (watch file uupdate)

* Sun Jun 08 2014 Michael Shigorin <mike@altlinux.org> 1.19.14-alt1
- new version (watch file uupdate)

* Wed May 07 2014 Michael Shigorin <mike@altlinux.org> 1.19.13-alt2
- full subpackage now pulls extras in finally

* Tue May 06 2014 Michael Shigorin <mike@altlinux.org> 1.19.13-alt1
- new version (watch file uupdate)

* Sun Apr 13 2014 Michael Shigorin <mike@altlinux.org> 1.19.12p1-alt1
- 1.19.12p1
- suppress findreq for filters (bundled msodumper workaround)
- added watch file

* Tue Nov 12 2013 Michael Shigorin <mike@altlinux.org> 1.19.9-alt1
- 1.19.9

* Tue May 14 2013 Michael Shigorin <mike@altlinux.org> 1.19.2-alt1
- 1.19.2

* Tue Nov 06 2012 Michael Shigorin <mike@altlinux.org> 1.18.1-alt1
- 1.18.1

* Fri May 25 2012 Michael Shigorin <mike@altlinux.org> 1.17.3-alt1
- 1.17.3
  + email indexing crash fix

* Thu May 17 2012 Michael Shigorin <mike@altlinux.org> 1.17.2-alt1
- 1.17.2 (minor bugfixes)

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 1.17.0-alt1
- 1.17.0
  + usability enhancements
  + indexing from GUI
  + filtering improvements

* Mon Nov 28 2011 Michael Shigorin <mike@altlinux.org> 1.16.2-alt2
- replaced xterm references with xvt in filters (closes: #26629)

* Wed Nov 09 2011 Michael Shigorin <mike@altlinux.org> 1.16.2-alt1
- 1.16.2 (bugfixes)
  + indexer now puts itself in the ionice "idle" class by default
  + verbosity level of some messages were adjusted
  + new command line options for the recollq program

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.16.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 11 2011 Michael Shigorin <mike@altlinux.org> 1.16.1-alt2
- extras and full subpackages made noarch

* Thu Sep 29 2011 Michael Shigorin <mike@altlinux.org> 1.16.1-alt1
- 1.16.1
  + fixes a frequent, annoying crash when running
    a query in the GUI with the indexing thread running

* Thu Sep 22 2011 Michael Shigorin <mike@altlinux.org> 1.16.0-alt1
- 1.16.0

* Sun May 29 2011 Michael Shigorin <mike@altlinux.org> 1.15.9-alt1
- 1.15.9
  + fixes an architecture-dependant startup crash in 1.15.8;
    there is no need to upgrade if you are not experiencing it

* Wed May 04 2011 Michael Shigorin <mike@altlinux.org> 1.15.8-alt1
- 1.15.8

* Sat Mar 12 2011 Michael Shigorin <mike@altlinux.org> 1.15.7-alt1
- 1.15.7 (minor fixups)

* Sun Mar 06 2011 Michael Shigorin <mike@altlinux.org> 1.15.5-alt1
- 1.15.5 (fixes more crashes still in 1.15.2)

* Tue Feb 15 2011 Michael Shigorin <mike@altlinux.org> 1.15.2-alt1
- 1.15.2 ("Remember sort state" bugfix)

* Sat Feb 05 2011 Michael Shigorin <mike@altlinux.org> 1.15.1-alt1
- 1.15.1

* Sat Nov 27 2010 Michael Shigorin <mike@altlinux.org> 1.14.3-alt3
- introduced -full subpackage based on mithraen@'s metapackages
  and (fake) wrar@-pleasing Recommends: in description
  (doesn't pull in -extras, at least not yet)

* Fri Nov 26 2010 Michael Shigorin <mike@altlinux.org> 1.14.3-alt2
- moved hotrecoll.py into a subpackage of its own due to
  hefty additional dependencies on its account (thanks evg@)
- included rcllyx into the very same subpackage

* Thu Nov 25 2010 Michael Shigorin <mike@altlinux.org> 1.14.3-alt1
- 1.14.3

* Mon Oct 04 2010 Michael Shigorin <mike@altlinux.org> 1.14.2-alt1
- 1.14.2

* Sun Sep 19 2010 Michael Shigorin <mike@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 1.13.04-alt2
- rebuilt against libxapian-1.2.0

* Sat Apr 24 2010 Michael Shigorin <mike@altlinux.org> 1.13.04-alt1
- 1.13.04

* Sun Feb 21 2010 Michael Shigorin <mike@altlinux.org> 1.13.02-alt1
- 1.13.02

* Thu Jan 07 2010 Michael Shigorin <mike@altlinux.org> 1.13.01-alt1
- 1.13.01

* Wed Jan 06 2010 Michael Shigorin <mike@altlinux.org> 1.13.00-alt1
- 1.13.00

* Thu Oct 29 2009 Michael Shigorin <mike@altlinux.org> 1.12.3-alt1
- 1.12.3
- dropped patch

* Thu May 28 2009 Michael Shigorin <mike@altlinux.org> 1.12.0-alt4
- fixed build with gcc-4.4 against glibc-2.10
  (thanks ldv@ for explanation)

* Mon Feb 16 2009 Michael Shigorin <mike@altlinux.org> 1.12.0-alt3
- built against Qt4

* Mon Feb 16 2009 Michael Shigorin <mike@altlinux.org> 1.12.0-alt2
- updated ru/uk translations

* Wed Feb 11 2009 Michael Shigorin <mike@altlinux.org> 1.12.0-alt1
- 1.12.0:
  + kioslave
  + collapse identical results
  + context help
  + attachments can be saved from email

* Thu Jan 08 2009 Michael Shigorin <mike@altlinux.org> 1.11.4-alt1
- 1.11.4

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.11.0-alt2
- applied repocop patch

* Mon Nov 03 2008 Michael Shigorin <mike@altlinux.org> 1.11.0-alt1
- 1.11.0 (major feature enhancements)
  + NB: this release needs a full reindex
- removed patch (was fixed upstream)

* Wed Sep 24 2008 Michael Shigorin <mike@altlinux.org> 1.10.6-alt3
- updated Russian and Ukrainian translations

* Wed Sep 24 2008 Michael Shigorin <mike@altlinux.org> 1.10.6-alt2
- added patch by the author to fix command-line argument charset
  handling for non-utf8/ascii locales

* Sun Sep 21 2008 Michael Shigorin <mike@altlinux.org> 1.10.6-alt1
- 1.10.6: fix a simple and mildly nasty bug for mbox indexing

* Tue Sep 02 2008 Michael Shigorin <mike@altlinux.org> 1.10.5-alt1
- 1.10.5 (minor bugfixes)

* Mon Aug 25 2008 Michael Shigorin <mike@altlinux.org> 1.10.2-alt2
- accepted changes by led@, built for Sisyphus
- minor spec cleanup
- fixed BuildRequires

* Fri Aug 22 2008 Led <led@altlinux.ru> 1.10.2-alt1.1
- with libfam
- updated BuildRequires
- cleaned up spec
- add icons
- fixed License

* Mon Jun 02 2008 Michael Shigorin <mike@altlinux.org> 1.10.2-alt1
- 1.10.2: minor bugfixes

* Wed Jan 30 2008 Michael Shigorin <mike@altlinux.org> 1.10.1-alt1
- 1.10.1:
  + filename indexing fixes in different corner cases
  + allow stopping indexing through menu action
  + "indexedmimetypes" configuration variable to explicitly
    set the file types to index

* Sun Nov 25 2007 Michael Shigorin <mike@altlinux.org> 1.10.0-alt1
- 1.10.0:
  + configuration GUI for the indexing parameters
  + support for CJK texts
  + new filters for image and TeX formats
  + kicker applet

* Wed Sep 12 2007 Michael Shigorin <mike@altlinux.org> 1.9.0-alt1
- 1.9.0

* Thu Jul 05 2007 Michael Shigorin <mike@altlinux.org> 1.8.2-alt4
- force rebuild against xapian 1.0.2 (network protocol version
  bumped up doesn't affect recoll directly but in mixed setups
  one doesn't want to use older core due to that, and there
  were smaller relevant fixes either)

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.8.2-alt3
- *force* rebuild against xapian 1.0.1, there was incompatible
  ABI change there

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.8.2-alt2
- rebuilt against xapian-core 1.0.1

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 1.8.2-alt1
- 1.8.2
- built against xapian 1.0.0
- removed patches
- s/openoffice/ooffice/ mimeconf mimeview

* Mon Mar 12 2007 Michael Shigorin <mike@altlinux.org> 1.8.1-alt1
- 1.8.1
- built against xapian 0.9.10
- removed debian menu (fd.o entry in place)
- disabled Lyx filter by default (would require lyx-qt which
  brings in tetex -- that's overkill for many "desktop" users)

* Tue Jan 16 2007 Michael Shigorin <mike@altlinux.org> 1.7.5-alt1
- 1.7.5
- should also index email attachments (but correctly; 1.7.4
  has some lapses there)

* Tue Nov 28 2006 Michael Shigorin <mike@altlinux.org> 1.6.2-alt1
- 1.6.2
- updated icon location

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 1.5.10-alt1
- 1.5.10 (ah... why not bother? :)

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 1.5.6-alt1
- 1.5.6 (I know about 1.5.10, just want to go home today)
- rebuilt against xapian 0.9.9

* Thu Oct 19 2006 Michael Shigorin <mike@altlinux.org> 1.5.5-alt1
- 1.5.5

* Thu Oct 19 2006 Michael Shigorin <mike@altlinux.org> 1.5.4-alt3
- updated Russian and Ukrainian translations

* Wed Oct 11 2006 Michael Shigorin <mike@altlinux.org> 1.5.4-alt2
- rebuilt against xapian 0.9.7
- added an icon

* Tue Oct 03 2006 Michael Shigorin <mike@altlinux.org> 1.5.4-alt1
- 1.5.4 (major feature enhancements)

* Mon May 15 2006 Michael Shigorin <mike@altlinux.org> 1.4.3-alt1
- 1.4.3
  + translations merged upstream
- rebuilt against libxapian-0.9.6

* Fri May 05 2006 Michael Shigorin <mike@altlinux.org> 1.4.2-alt1
- 1.4.2 (thanks gns@ for pinging me)
  + similar documents search
  + query history
  + term completion
  + improved usability, e.g. cancel during indexation
- built against xapian-core 0.9.5
- additional filter pack seems unneeded
- updated translations
- added an attempt at icon
- pretty Url
- minor spec cleanup

* Sun Apr 09 2006 Michael Shigorin <mike@altlinux.org> 1.3.3-alt3
- found a spec typo during backporting that made 1.3.3-alt2
  no different from 1.3.3-alt1

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.3.3-alt2
- added fixed filter pack provided by the author
  (reportedly fixes some problems with filenames containing spaces)

* Tue Apr 04 2006 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- 1.3.3
- got the most important part of patch4 (OOo wrapper name) back
- merged 3.0 spec changes (menu file)

* Sat Apr 01 2006 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- 1.3.1
- translations accepted upstream (thanks Jean for gently
  pinging me to update Russian)

* Thu Mar 30 2006 Michael Shigorin <mike@altlinux.org> 1.3.1-alt0.2
- 1.3.1pre2

* Tue Mar 28 2006 Michael Shigorin <mike@altlinux.org> 1.3.1-alt0.1
- 1.3.1pre1
- removed patch4

* Fri Mar 10 2006 Michael Shigorin <mike@altlinux.org> 1.2.3-alt0.M30.1
- built for M30
- added Debian menu file
- added %%optflags

* Fri Mar 10 2006 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3
- upstream fixed installation, no more ugly spec hacks; good
- updated translation; thanks Yury Kashirin for lupdate hint
- added desktop file (maybe lame one)
- added defaults fixes (first try); if you already have ~/.recoll,
  might need to have a glance yourself

* Mon Feb 06 2006 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2
- patch2 temporarily disabled, need to update translation

* Thu Jan 26 2006 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0
  + maybe case (in)sensitivity issue is fixed
- removed patch3

* Thu Jan 26 2006 Michael Shigorin <mike@altlinux.org> 1.0.16-alt1
- 1.0.16

* Mon Dec 19 2005 Michael Shigorin <mike@altlinux.org> 1.0.15-alt1
- 1.0.15
- fixed ru translation install/use, thanks eostapets@
- spec cleanup

* Sat Dec 10 2005 Michael Shigorin <mike@altlinux.org> 1.0.14-alt2
- add Russian translation

* Fri Dec 09 2005 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14
- don't apply hackaround (doesn't help that particular case)

* Tue Dec 06 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt2
- added recommended companion packages to description
- added hackaround by eostapets@ to quickly do something
  with non-7bit icase search

* Mon Dec 05 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- built for ALT Linux

