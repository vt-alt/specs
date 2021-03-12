
%add_findpackage_path %_kde4_bindir
#add_findreq_skiplist %_K4apps/kate/plugins/pate/kate/__init__.py
#add_findreq_skiplist %_K4apps/kate/plugins/pate/kate/__init__.py
#add_findreq_skiplist %_K4apps/kate/pate/*_utils/*/*.py
#add_findreq_skiplist %_K4apps/kate/pate/*_utils/*.py
#add_findreq_skiplist %_K4apps/kate/pate/python_autocomplete/*.py
%add_python_req_skip pate jedi pyflakes pyplete 

%if_enabled kde_mobile
%def_disable desktop
%else
%def_enable desktop
%endif

%define rname kate
%define major 4
%define minor 14
%define bugfix 7
Name: kde4-kate
Version: %major.%minor.%bugfix
Release: alt5

Group: Editors
Summary: Advanced text editor
Url: http://www.kde.org/
License: GPLv2

Requires: kde4-icon-theme
Requires: %name-core = %version-%release
Provides: kde4sdk-kate = %version-%release
Obsoletes: kde4sdk-kate < %version-%release

Source: %rname-%version.tar
Patch1: alt-disable-tests.patch
Patch2: alt-gcc6.patch

# Automatically added by buildreq on Fri Sep 16 2011 (-bi)
# optimized out: automoc cmake cmake-modules desktop-file-utils docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-mime-info xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): kde4libs-devel rpm-build-ubt
BuildRequires: gcc-c++ glib2-devel zlib-devel kde-common-devel desktop-file-utils
BuildRequires: qjson-devel kde4-kactivities-devel
BuildRequires: python-devel 

%description
A fast and advanced text editor with nice plugins

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdesdk-common <= 3.5.12-alt1
Conflicts: kdebase-common <= 3.5.12-alt2
%description common
Common empty package for %rname

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: kde4libs >= %{get_version kde4libs}
%description core
Core files needed for %rname

%package -n kde4-kwrite
Group: Editors
Summary: Text editor for KDE
Requires: kde4-icon-theme
Requires: %name-core = %version-%release
Provides: kde4base-kwrite = %version-%release
Obsoletes: kde4base-kwrite < %version-%release
%description -n kde4-kwrite
Text editor for KDE

%package -n libkateinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkateinterfaces4
%name library.

%package -n libkatepartinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkatepartinterfaces4
%name library.

%package -n libktexteditor4_codesnippets_core
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libktexteditor4_codesnippets_core
%name library.

%package devel
Summary: Header files for %rname
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
This package includes the header files you will need to compile
applications for %rname.


%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K4build \
    -DKDE4_BUILD_TESTS:BOOL=OFF \
    #

%install
%K4install

kde4_add_text_mimes() {
desktop-file-install --mode=0755 --dir %buildroot%_K4xdg_apps \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	$1
}

kde4_add_text_mimes %buildroot%_K4xdg_apps/kate.desktop
kde4_add_text_mimes %buildroot%_K4xdg_apps/kwrite.desktop


%files common

%files core
%_K4lib/katepart.so
%_K4lib/ktexteditor_*.so
%_K4apps/ktexteditor_*/
%_K4apps/katepart
%_K4conf/katemoderc
%_K4srv/katepart.desktop
%_K4srv/ktexteditor_*.desktop
%_K4iconsdir/hicolor/*/apps/ktexteditorautobrace.*
%_K4iconsdir/hicolor/*/actions/debug-*.png

%files
%if_enabled desktop
%_K4lib/katefiletemplates.so
%_K4srv/katefiletemplates.desktop
%endif
%_K4bindir/kate
%_K4xdg_apps/kate.desktop
%_K4apps/kate/
%_K4apps/katexmltools
%_K4conf_update/kate-2.4.upd
%_K4conf/katerc
%_K4conf/kateschemarc
%_K4conf/katesyntaxhighlightingrc
%_K4conf/ktexteditor_codesnippets_core.knsrc
%_K4libdir/libkdeinit4_kate.so
%_K4lib/kate*plugin.so
%_K4lib/plasma_applet_katesession.so
%_K4lib/kate_kttsd.so
%_K4srv/kate*plugin.desktop
%_K4srv/kateopenheader.desktop
%_K4srv/katesymbolviewer.desktop
%_K4srv/katetabbarextension.desktop
%_K4srv/katetextfilter.desktop
%_K4srv/plasma-applet-katesession.desktop
%_K4srv/kate_kttsd.desktop
%_K4srv/katexmlcheck.desktop
%_K4srv/katexmltools.desktop
%_K4srv/katesql.desktop
%_K4srv/katesearch.desktop
#_K4srv/katepate_*.desktop
%_K4srvtyp/kateplugin.desktop
#_K4srvtyp/katepythonplugin.desktop
#%_K4doc/*/kate-plugins
%_K4doc/*/kate
%_K4iconsdir/hicolor/*/apps/kate.*
# pate plugin
#python_sitelibdir/PyKate4/
#_K4srv/pate.desktop

%files -n kde4-kwrite
%_K4bindir/kwrite
%_K4libdir/libkdeinit4_kwrite.so
%_K4xdg_apps/kwrite.desktop
%_K4apps/kwrite/
%_K4doc/en/kwrite/

%files -n libkateinterfaces4
%_K4libdir/libkateinterfaces.so.*
%files -n libkatepartinterfaces4
%_K4libdir/libkatepartinterfaces.so.*

%files devel
%_K4includedir/kate/
%_K4includedir/kate_*.h
%_K4link/lib*.so

%changelog
* Fri Feb 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.14.7-alt5
- Disabled building python modules and plugins.

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.14.7-alt4
- NMU: remove %ubt from release

* Fri Apr 20 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt3%ubt
- fix to build with new gcc

* Thu Oct 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt2
- update from KDE/4.14 branch

* Thu Apr 23 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt1
- new version

* Thu Jan 29 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.4-alt1
- new version

* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Tue Oct 07 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt2
- fix package files on arm

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Jul 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Wed May 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Tue Apr 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Sat Jan 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt0.M70P.1
- built for M70P

* Fri Jan 10 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Wed Jun 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue May 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Wed Mar 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Tue Feb 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- build python plugin

* Tue Jan 29 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Tue Dec 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Dec 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Fri Nov 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Mon Oct 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1.M60P.1
- built for M60P

* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.2
- rebuilt

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- fix kwrite startup without kate

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1.M60T.1
- built for M60T

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- fix requires (ALT#26424)

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
