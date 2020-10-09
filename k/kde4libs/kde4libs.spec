%define _kde_alternate_placement 1

%if_enabled kde_mobile
%def_disable desktop
%else
%def_enable desktop
%endif

%def_enable openexr
%def_disable hupnp

%add_findpackage_path %_kde4_bindir
%add_findreq_skiplist %_K4apps/cmake/modules*.py

%define major 4
%define minor 14
%define bugfix 38
%define rname kdelibs
Name: kde4libs
Version: %major.%minor.%bugfix
Release: alt7

%define conflictver %major.%minor-alt0.0.1
%define conflictver_kdevelop 3.4.1-alt0.0.1

Group: System/Libraries
Summary: K Desktop Environment 4 - Libraries
Url: http://www.kde.org/
License: LGPLv2/BSD/GFDL

Requires: kde-common >= %major.%minor
PreReq: altlinux-freedesktop-menu-kde4
Requires: ca-certificates shared-mime-info

Conflicts: koffice-core = 1.9.98.3
# Conflicts for old KDE
#Conflicts: kde4-i18n-de < %conflictver kde4-i18n-fr < %conflictver kde4-i18n-he < %conflictver
#Conflicts: kde4-i18n-et < %conflictver kde4-i18n-ru < %conflictver kde4-i18n-uk < %conflictver
#Conflicts: kde4-i18n-tt < %conflictver kde4-i18n-kk < %conflictver kde4-i18n-pt_BR < %conflictver
#Conflicts: kdevelop-common < %conflictver_kdevelop
#Conflicts: kde4accessibility-common < %conflictver
#Conflicts: kde4addons-common < %conflictver
#Conflicts: kde4admin-common < %conflictver
#Conflicts: kde4artwork-common < %conflictver
#Conflicts: kde4artwork-wallpapers < %conflictver
#Conflicts: kde4base-common < %conflictver
#Conflicts: kde4base-runtime < %conflictver
#Conflicts: kde4base-runtime-common < %conflictver kde4base-common < %version
#Conflicts: kde4base-workspace-common < %conflictver kde4base-common < %version
#Conflicts: kde4devplatform-common < %conflictver
#Conflicts: kde4edu-common < %conflictver
#Conflicts: kde4games-common < %conflictver
#Conflicts: kde4multimedia-common < %conflictver
#Conflicts: kde4network-common < %conflictver
#Conflicts: kde4pimlibs-common < %conflictver
#Conflicts: kde4pimlibs < %conflictver kde4base-common < %version
#Conflicts: kde4pim-common < %conflictver
#Conflicts: kde4plasma-addons-common < %conflictver
#Conflicts: kde4toys-common < %conflictver
#Conflicts: kde4utils-common < %conflictver
#Conflicts: kde4sdk-common < %conflictver
#Conflicts: kde4webdev-common < %conflictver
#Conflicts: kde4-konqueror-plugins-common < %conflictver


Source: %rname-%version.tar

# RH
Patch101: kdelibs-4.3.90-install_all_css.patch
Patch102: kdelibs-4.5.80-parallel_devel.patch
Patch103: kdelibs-4.7.0-knewstuff_gpg2.patch
Patch104: kdelibs-4.5.80-no_rpath.patch
Patch105: kdelibs-4.7.4-SOLID_UPNP.patch
Patch106: kdelibs-4.14.38-openssl-1.1.patch
# Debian
Patch201: 14_hardcode_ptm_device.diff
Patch202: 30_kfileshare_kdesu_fileshareset.diff
Patch203: 31_relax_plugin_kde_version_check.diff
# SuSE
Patch301: desktop-translations.diff
Patch302: 0001-Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch
# upstream
# ALT
Patch1000: kdelibs-4.8.4-alt-xdg-dirs.patch
Patch1001: kdelibs-4.0.72-alt-custom-kdedir.patch
Patch1002: kdelibs-4.6.0-alt-exists_ext.patch
Patch1003: kdelibs-4.4.0-alt-applications.menu.patch
Patch1004: kdelibs-4.6.0-alt-libexec-install-dir.patch
Patch1005: kdelibs-4.7.0-alt-def-http-slave.patch
Patch1006: kdelibs-4.1.0-alt-libssl-name.patch
Patch1007: kdelibs-4.0.0-alt-su-close-pty.patch
Patch1008: kdelibs-4.3.90-alt-show-distribution.patch
Patch1009: kdelibs-4.0.71-alt-find-ruby.patch
Patch1010: kdelibs-4.6.5-alt-findqt4-version.patch
Patch1011: kdelibs-4.1.1-alt-find-automoc.patch
Patch1012: kdelibs-4.1.2-alt-mark-user-edited.patch
Patch1013: kdelibs-4.6.3-alt-places-add-docs.patch
Patch1014: kdelibs-4.2.2-alt-find-usb.patch
Patch1015: kdelibs-4.3.0-alt-resources-order.patch
Patch1016: kdelibs-4.14.9-alt-initial-preference.patch
Patch1017: kdelibs-4.6.0-alt-def-plasma.patch
Patch1018: kdelibs-4.5.0-alt-def-fonts.patch
Patch1019: kdelibs-4.6.0-alt-kfileplaces.patch
Patch1020: kdelibs-4.4.2-alt-disable-debug.patch
Patch1021: kdelibs-4.4.92-alt-find-docbook.patch
Patch1022: kdelibs-4.5.0-alt-submenu-delay.patch
Patch1023: kdelibs-4.7.4-plasma-tooltip-delay.patch
Patch1024: kdelibs-4.6.3-alt-samba-sharing.patch
Patch1025: kdelibs-4.7.1-alt-find-hupnp.patch
Patch1026: kdelibs-4.7.1-alt-find-pulseaudio.patch
Patch1027: kdelibs-4.10.0-alt-no-hal.patch
Patch1028: kdelibs-4.8.1-alt-kdesu-export-user-var.patch
Patch1029: kdelibs-4.14.6-alt-skip-antikde-mimeapps-list.patch
Patch1030: kdelibs-4.9.1-alt-platform-profile.patch
Patch1031: kdelibs-4.8.5-alt-add-desktop-translations.patch
Patch1032: kdelibs-4.9.1-alt-policy-dir.patch
Patch1033: kdelibs-4.9.1-alt-cmake-spaces.patch
Patch1034: alt-def-icon-theme.patch
Patch1035: kdelibs-4.10.2-alt-flags.patch
Patch1036: kdelibs-4.10.2-alt-add-protocol-all.patch
Patch1037: kdelibs-4.10.4-alt-def-plasma-theme-bg.patch
Patch1038: kdelibs-4.10.5-alt-run-with-context.patch
Patch1039: alt-def-widget-style.patch
Patch1040: alt-def-color-scheme.patch

Patch3000: kdelibs-4.4.92-alt-alternate-kconf_update_bin-path.patch

# security

BuildRequires(pre): kde-common-devel libqt4-devel libstrigi-devel attica-devel
#BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano libsoprano-devel >= 2.1
BuildRequires: bzlib-devel cmake libalsa-devel libselinux-devel
%if_enabled hupnp
BuildRequires: herqq-devel
%endif
BuildRequires: libXrender-devel libXext-devel libXScrnSaver-devel grantlee-devel
#BuildRequires: libaspell-devel aspell
BuildRequires: libenchant-devel
BuildRequires: libavahi-devel libjpeg-devel
BuildRequires: libgif-devel libxslt-devel liblzma-devel docbook-style-xsl docbook-dtds
%if_enabled openexr
BuildRequires: openexr-devel
%endif
BuildRequires: libkrb5-devel shared-desktop-ontologies-devel
BuildRequires: polkit-qt-1-devel libpolkit1-devel libudev-devel
BuildRequires: graphviz gcc-c++ libpcre-devel shared-mime-info
BuildRequires: xml-utils libutempter-devel phonon-devel automoc
BuildRequires: libacl-devel libattr-devel flex libqca2-devel
BuildRequires: libdbusmenu-qt-devel
BuildRequires: kde-common-devel >= %major.%minor
BuildRequires: libqt4-devel >= 4.4

%description
Libraries for the K Desktop Environment 4.

%package devel
Group: Development/KDE and QT
Summary: Header files for compiling KDE 4 applications
Requires: %name = %version-%release
Requires: cmake libqt4-devel kde-common-devel >= %major.%minor
Requires: libXrender-devel libXext-devel libXdmcp-devel libXcomposite-devel libXdamage-devel libxkbfile-devel libXtst-devel libXScrnSaver-devel
Requires: libXpm-devel libXxf86vm-devel libXt-devel libXft-devel
Requires: libstrigi-devel libpcre-devel xml-utils
#Requires: libgif-devel
Requires: libutempter-devel bzlib-devel phonon-devel automoc shared-desktop-ontologies-devel
Requires: docbook-style-xsl docbook-dtds

%description devel
This package includes the header files you will need to compile
applications for KDE 4.

%prep
%setup -q -n %rname-%version

%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%if_enabled hupnp
%patch105 -p1
%endif
%patch106 -p1
#
%patch201 -p1
%patch202 -p1
%patch203 -p1
#
%patch301 -p0
%patch302 -p1
#
%patch1000 -p1 -b .xdg-dirs
%patch1001 -p1 -b .custom-kdedir
%patch1002 -p1 -b .exists_ext
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
#%patch1011 -p1
%patch1012 -p1
%patch1013 -p1
#%patch1014 -p1
#%patch1015 -p1 -b .resources-order
%patch1016 -p1
#%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1022 -p1
#%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
%patch1036 -p1
%patch1037 -p1
%patch1038 -p1
%patch1039 -p1
%patch1040 -p1

%patch3000 -p1

# CA certificates bundle
#pushd kio/kssl/kssl
#echo "%_datadir/ca-certificates/ca-bundle.crt" >localcerts
#./mergelocal
#popd


%build
export XDG_DATA_DIRS=%_K4datadir:%_datadir
#export CMAKE_LIBRARY_PATH=%_libdir
#define _K4buildtype Debug
#    -DKDE4_ENABLE_FINAL:BOOL=ON \
%K4cmake \
    -DKDE4_BUILD_TESTS=OFF \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
%if_enabled desktop
    -DKDE_PLATFORM_PROFILE="Desktop" \
%else
    -DKDE_PLATFORM_PROFILE="Mobile" \
%endif
    -DPCRE_INCLUDE_DIR=%_includedir/pcre \
    -DHUPNP_ENABLED:BOOL=%{?_enable_hupnp:ON}%{!?_enable_hupnp:OFF} \
    -DWITH_FAM:BOOL=OFF \
    -DWITH_SOLID_UDISKS2=ON \
    -DKIO_NO_SOPRANO=ON \
    -DKDE_DISTRIBUTION_TEXT="%distribution %_target_cpu" \
    -DKDE4_AUTH_BACKEND_NAME="POLKITQT-1" \
    -DKDE_DEFAULT_HOME:STRING=".kde4"

%K4make

# FIXME
#doc/api/doxygen.sh --doxdatadir=doc/common .


%install
%K4install

# move menu
mkdir -p %buildroot/%_sysconfdir/kde4/xdg/menus/applications-merged/
mv %buildroot/%_sysconfdir/kde4/xdg/menus/applications.menu %buildroot/%_sysconfdir/kde4/xdg/menus/applications-merged/

%ifdef _kde_alternate_placement
mkdir -p %buildroot/%_K4bindir/
pushd %buildroot/%_kde4_bindir
for f in *4
do
    ln -sf `relative %buildroot/%_kde4_bindir/$f %buildroot/%_K4bindir/$f` %buildroot/%_K4bindir/$f
done
popd
ln -sf `relative %buildroot/%_kde4_bindir/kde4-config %buildroot/%_K4bindir/kde4-config` %buildroot/%_K4bindir/kde4-config
%endif

# CA certificates bundle 2
#[ -f %buildroot/%_K4apps/kssl/ca-bundle.crt ] || exit 1
#ln -sf `relative %buildroot/%_datadir/ca-certificates/ca-bundle.crt %buildroot/%_K4apps/kssl/ca-bundle.crt` %buildroot/%_K4apps/kssl/ca-bundle.crt

# disable annoing autostart
mkdir -p %buildroot/%_K4start/
for n in tracker-extract tracker-miner-apps tracker-miner-fs tracker-miner-user-guides tracker-store ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_K4start/$n.desktop
done
# disable annoing menus
mkdir -p %buildroot/%_kde4_xdg_apps/
for n in gnome-mplayer mplayer gmplayer ; do
    echo -e "[Desktop Entry]\nHidden=true" > %buildroot/%_kde4_xdg_apps/$n.desktop
done


%files
%doc AUTHORS README TODO
#%_man1dir/*
%_man7dir/*
%_man8dir/*
#
#%config(noreplace) %_sysconfdir/profile.d/*
%exclude %_K4sysconfdir/kde4/xdg/menus/applications-merged/applications.menu
%config %_K4sysconfdir/dbus-1/system.d/*.conf
#
%_K4bindir/*
%exclude %_K4bindir/kconfig_compiler4
%exclude %_K4bindir/makekdewidgets4
%ifdef _kde_alternate_placement
%_kde4_bindir/*
%exclude %_kde4_bindir/kconfig_compiler4
%exclude %_kde4_bindir/makekdewidgets4
%endif
%_K4exec/*
%_K4apps/*
%exclude %_K4apps/LICENSES/
%exclude %_K4apps/cmake/
%exclude %_K4apps/kdewidgets/
%exclude %_K4datadir/apps/ksgmltools2/
%_K4start/*
%_K4conf/*
%_K4dbus_interfaces/*
%_K4xdg_mime/*
%_kde4_xdg_apps/*
%_K4srv/*
%_K4srvtyp/*
%_kde4_iconsdir/hicolor/*/actions/presence_*
#%_kde4_iconsdir/hicolor/*/apps/ktexteditorautobrace.*
%_K4i18n/all_languages
%_K4i18n/en_US/entry.desktop
%_K4doc/en/*
%_K4libdir/lib*.so.*
%_K4libdir/libkdeinit4_*.so
%_K4lib/*.so*
%_K4plug/script/*.so*
%_K4plug/imageformats/*.so*
%_K4plug/kauth
#%_datadir/polkit-1/actions/org.kde.kcontrol.kcmremotewidgets.policy

%files devel
%doc KDE4PORTING.html
%_K4bindir/kconfig_compiler4
%_K4bindir/makekdewidgets4
%ifdef _kde_alternate_placement
%_kde4_bindir/kconfig_compiler4
%_kde4_bindir/makekdewidgets4
%endif
%_K4libdir/cmake/KDeclarative
%_K4link/lib*.so
%dir %_K4plug/designer/
%_K4plug/designer/*.so*
%_K4apps/cmake/
%_K4apps/ksgmltools2/
%_K4apps/kdewidgets/
%_K4includedir/*

%changelog
* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 4.14.38-alt7
- build without libjasper

* Fri Dec 27 2019 Sergey V Turchin <zerg@altlinux.org> 4.14.38-alt6
- clean requires

* Thu Aug 08 2019 Sergey V Turchin <zerg@altlinux.org> 4.14.38-alt5
- security fixes: CVE-2019-14744

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 4.14.38-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Nov 20 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.38-alt3
- load dolphin translations to file dialogs

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.38-alt2
- build with openssl-1.1

* Wed Apr 25 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.38-alt1
- new version

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.14.34-alt2
- Fixed build with new cmake.

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 4.14.34-alt1
- new version

* Fri Feb 03 2017 Sergey V Turchin <zerg@altlinux.org> 4.14.28-alt1
- new version

* Wed Oct 26 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.25-alt0.M80P.1
- build for M80P

* Wed Oct 26 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.25-alt1
- new version

* Mon Aug 29 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.23-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.21-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.20-alt1
- new version
- det default colors from Breeze color scheme

* Wed Apr 20 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.18-alt3
- fix set default style

* Wed Apr 20 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.18-alt2
- set breeze widgets style and icons theme by default (kde4-styles-breeze package)

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.18-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.17-alt2
- completely disable nepomuk

* Wed Feb 17 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.17-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.16-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.15-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.14-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.13-alt1
- new version

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.12-alt1
- new version

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.11-alt1
- new version

* Wed Jul 15 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt1
- new version
- prefer KDE4 apps

* Thu Jun 18 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt3
- remove libsoprano-devel from devel package requires
- build without hupnp

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt2
- temporary build without openexr

* Mon Jun 08 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt1
- new version

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.8-alt1
- new version

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt1
- new version

* Fri Mar 20 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.6-alt2
- ignore /usr/share/applications/mimeapps.list

* Wed Mar 11 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.6-alt1
- new version

* Thu Feb 05 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.5-alt1
- new version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.4-alt1
- new version

* Thu Nov 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Mon Oct 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Mon Jul 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Tue Jun 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Wed May 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt2
- update code from 4.13 branch

* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Thu Apr 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt2.M70P.1
- built for M70P

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt3
- fix to build

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1.M70P.1
- built for M70P

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt2
- disable tracker autostart
- update from 4.12 branch

* Wed Mar 05 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Sat Jan 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt0.M70P.1
- built for M70P

* Thu Jan 09 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt1
- new version

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Tue Nov 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1.M70P.1
- built for M70P

* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt2
- don't revert code according kde-runtime changes

* Mon Sep 30 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Tue Sep 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt3
- update alt-run-with-context patch

* Thu Sep 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- fix kwallet freeze

* Tue Sep 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Mon Jul 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Tue Jun 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt2
- set default plasma theme background

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Mon May 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Tue Apr 30 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt4
- improve file properties dialog; thenks timonbl4@alt

* Tue Apr 16 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt3
- remove -std=iso9899:1990 from default CMAKE_C_FLAGS

* Fri Apr 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt2
- fix to build with libhupnp

* Wed Apr 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Mon Mar 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Sat Feb 23 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt5
- fix find libsmbclient includes

* Fri Feb 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt4
- update from 4.10 branch

* Thu Feb 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt3
- update from 4.10 branch

* Mon Feb 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update from 4.10 branch

* Thu Jan 31 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- update from 4.10 branch

* Wed Jan 23 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.6
- update from 4.10 branch
- built without aspell

* Wed Jan 16 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.5
- update from 4.10 branch
  (INSTALL_PYTHON_FILES_IN_PYTHON_PREFIX(FALSE) cmake define added)
- built enchant spell checking backend

* Wed Jan 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.4
- udpate from 4.10 branch

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- udpate from 4.10 branch

* Wed Dec 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- udpate from 4.10 branch
- fix to load udev and udisks solid backends

* Fri Dec 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Wed Dec 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version
- update udisks2 backend from KDE/4.10 branch

* Thu Nov 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt2
- update from KDE/4.9 branch
- update udisks2 backend from KDE/4.10 branch

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Mon Sep 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Tue Aug 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt2.M60P.1
- built for M60P

* Tue Aug 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt3
- update from 4.8 branch (kde bug 268020)

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1.M60P.1
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt2
- add for global desktop-files translation support

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Wed Aug 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Fri Jul 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt6
- rebuilt with new attica

* Wed Jun 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt4.M60P.1
- built for M60P

* Wed Jun 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt5
- use 4.8.x branch

* Tue Jun 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt3.M60P.1
- built for M60P

* Tue Jun 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt4
- fix find kde resources

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt3
- update from 4.8 branch

* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Mon Jun 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt6.M60P.1
- built for M60P

* Mon Jun 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt7
- fix duplicated menu enries

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt5.M60P.1
- build for M60P

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt6
- update from 4.8 branch
- revert nepomuk code to v4.8.3 tag (ALT#27337)

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt5
- update from 4.8 branch

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt4
- require altlinux-freedesktop-menu-kde4 directly
- update from 4.8 branch

* Fri May 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt3
- update from 4.8 branch

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- update from 4.8 branch

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt2
- workaround against building pykde4 on arm

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Mon Apr 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- built for M60P

* Thu Mar 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- set USER variable in kdesu_stub
- update from 4.8 branch

* Mon Mar 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Mar 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- don't lock desktop widgets by default

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Fri Dec 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt5.M60P.1
- built for M60P

* Fri Dec 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt6
- remove hal support
- build upnp solid backend and turn off by default

* Wed Dec 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt5
- update from 4.7 branch

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3.M60P.1
- built for M60P

* Wed Dec 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4
- update from 4.7 branch
- revert upstream commit 5960ae9846c333ef381a817af9d63776c4ddc201

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3
- update from 4.7 branch

* Fri Dec 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- update from KDE/4.7 branch (drop libkactivities)

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Wed Nov 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt3.M60P.1
- built for M60P

* Mon Nov 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt4
- don't build upnp solid backend

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2.M60P.1
- built for M60P

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt3
- fix build requires

* Thu Nov 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Wed Nov 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- update from 4.7 branch

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Fri Oct 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3.M60T.1
- built for M60T

* Mon Oct 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt4
- update from 4.7 branch

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3
- update from 4.7 branch

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- fix conflicts

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Wed Sep 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- fix build requires
- fix find pulseaudio

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Aug 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2.M60P.1
- built for M60P

* Wed Aug 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt3
- update from 4.6 branch

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1.M60P.1
- built for M60P

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- update form 4.6 branch
- add patch to fix FindQt4.cmake (ALT#25936)

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt0.M60P.1
- built for M60P

* Fri Jul 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt0.M60P.1
- built for M60P

* Fri Jun 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Mon May 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt3
- fix Documents bookmark translation

* Fri May 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- move Documents bookmark ontop

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt7
- add new system freedesktop menu support; thanks viy@alt

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt6
- fix Documents bookmark path 

* Wed Apr 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt5
- add xdg-user-dirs support for Documents in Places

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt4
- fix requires

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt3
- fix requires

* Tue Apr 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- fix requires

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version
- add fixes for samba file sharing

* Mon Feb 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Jan 26 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Tue Dec 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt2
- decrease default plasma tooltip popup delay

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Mon Nov 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Wed Oct 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt3
- add fix for opening https:/ links (ALT#24356)

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Wed Aug 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt2
- force default fonts to DejaVu

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.92-alt1
- 4.4.92

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt2
- rebuilt with new qt

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version
- disable debug output by default

* Fri Mar 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt2
- don't embed "Edit Item" dialog to KFilePlaceView
- fix KFilePlaceView popup menu position

* Sat Feb 27 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Tue Feb 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version
- fix build requires

* Fri Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt3
- rebuilt with fixed kde-common-devel (ALT#22783)

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2
- rebuilt with new Qt

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Fri Oct 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Fri Oct 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt3
- fix find new SSL libraries

* Thu Oct 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt2
- fix browser invocation with multiple arguments (ALT#21950)

* Wed Oct 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Thu Sep 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- build with LZMA/XZ compression support

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Mon Aug 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt4
- set default fonts

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt3
- set default desktop plugin

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- add X-KDE4-InitialPreference support

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2.M50.1
- built for M50

* Mon Jun 29 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt3
- CVE-2009-0945, CVE-2009-1690 (ALT#20633)

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- rebuilt

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Mon May 18 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt2
- rebuilt with new %%_K4link

* Mon May 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt3
- send language info in http header by default
- add some upstream fixes

* Tue Apr 07 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- add upstream fixes for kio and plasma

* Thu Apr 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Wed Mar 25 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt3
- built whith new Qt

* Mon Mar 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt2
- add ~/Documents folder to default places

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Fri Feb 06 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt3
- fix to build with libacl

* Thu Feb 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- built with libacl

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Mon Jan 12 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt2
- apply patch to remove -l option for su execution via kdesu (#18483)
- remove deprecated macroses from specfile

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt3
- fix to find emoticons

* Mon Sep 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt2
- rebuilt with new kde-common-devel

* Mon Sep 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt2
- fix xdg data dirs search order

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Tue May 27 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Sun May 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Sun May 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.71-alt1
- new version

* Tue Apr 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt3
- move adding search for kde link directory to system rpm macros

* Tue Mar 11 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt2
- rebuilt with Qt4 buildkey change

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- new version

* Thu Feb 28 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt9
- add libutempter-devel to requires for devel subpackage

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt8
- rebuilt with new openexr

* Tue Feb 19 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt7
- update requires for devel subpackage

* Tue Feb 19 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt6
- built with libutempter

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt5
- fix conflicts

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt4
- use %%K4cmake

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt3
- move kconfig_compiler4 makekdewidgets4 symlinks to -devel package

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt2
- fix FindRUBY.cmake

* Wed Feb 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- built for ALT
