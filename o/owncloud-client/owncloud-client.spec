AutoReq: yes, nopython
AutoProv: yes, nopython nopython3
%add_python3_path %_datadir/nautilus-python/extensions/

%define rname owncloudclient
Name: owncloud-client
Version: 2.6.3
Release: alt1

Group: Networking/File transfer
Summary: ownCloud Desktop Client
License: GPLv2
Url: http://owncloud.org/sync-clients/

Provides: mirall = %version-%release
Obsoletes: mirall <= %version-%release

# https://download.owncloud.com/desktop/stable/
Source: %rname-%version.tar
Source1: owncloud-client.desktop
Patch1: alt-dont-check-updates.patch
Patch2: alt-confdir.patch
Patch3: alt-static-libs.patch
Patch4: alt-move-deleted-to-trash.patch
Patch5: alt-qt5.15.patch

# Automatically added by buildreq on Mon Oct 24 2016 (-bi)
# optimized out: cmake cmake-modules desktop-file-utils elfutils gcc-c++ kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libqtkeychain-qt5 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-module-google python-module-sphinx python-modules python3 python3-base qt5-base-devel qt5-tools rpm-build-gir rpm-build-python3 texlive-latex-base zlib-devel
#BuildRequires: doxygen extra-cmake-modules graphviz kf5-kio-devel libqtkeychain-qt5-devel libsqlite3-devel libssl-devel python3-dev qt5-tools-devel qt5-webkit-devel ruby ruby-stdlibs zlib-devel-static
BuildRequires(pre): rpm-build-python3
BuildRequires: kde-common-devel rpm-build-kf5
BuildRequires: doxygen extra-cmake-modules graphviz kf5-kio-devel libqtkeychain-qt5-devel libsqlite3-devel libssl-devel qt5-tools-devel zlib-devel

%description
The ownCloud Desktop Client is a tool to synchronize files from ownCloud Server with your computer.

%package kde5
Summary: KDE5 %name integration
Group: Graphical desktop/KDE
Requires: %name
%description kde5
KDE5 %name integration

%package nautilus
Summary: Nautilus %name integration
Group: Graphical desktop/GNOME
Requires: %name
%description nautilus
Nautilus %name integration

%prep
%setup -qn %rname-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i 's|-Wno-gnu-zero-variadic-macro-arguments||' cmake/modules/Warnings.cmake

%build
%add_optflags %optflags_shared
%Kbuild \
    -DBUILD_WITH_QT4=OFF \
    -DDATA_INSTALL_DIR=%_datadir \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc/owncloud-client \
    -DKDE_INSTALL_PLUGINDIR=%_K5plug \
    -DKDE_INSTALL_KSERVICES5DIR=%_K5srv \
    -DNO_SHIBBOLETH=ON \
    #

%install
%Kinstall
mkdir -p %buildroot/%_desktopdir
desktop-file-install \
    --dir=%buildroot/%_desktopdir \
    %{SOURCE1}

%find_lang --with-qt --output=%name.lang client

%files -f %name.lang
%doc changelog/CHANGELOG.tmpl README.md
%config(noreplace) %_sysconfdir/ownCloud/sync-exclude.lst
%_bindir/owncloud
%_bindir/owncloudcmd
%_libdir/ownCloud/plugins/owncloudsync_vfs_suffix.so
%_desktopdir/%name.desktop
#%_datadir/owncloud-client
%_iconsdir/hicolor/*/apps/owncloud.*
%_iconsdir/hicolor/*/apps/ownCloud_*.*
%_xdgmimedir/packages/owncloud.xml

%files kde5
%_K5lib/libownclouddolphinpluginhelper.so
%_K5plug/kf5/overlayicon/
%_K5plug/*owncloud*.so
%_K5srv/*owncloud*.desktop

%files nautilus
%_datadir/nautilus-python/extensions/

%changelog
* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 2.6.3-alt1
- new version

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 2.5.1-alt4
- build with python3

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt3
- NMU: remove rpm-build-ubt from BR:

* Fri Dec 14 2018 Sergey V Turchin <zerg@altlinux.org> 2.5.1-alt2
- move deleted files to trash by default

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 2.5.1-alt1
- new version

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt4
- NMU: added URL

* Tue Jan 23 2018 Oleg Solovyov <mcpain@altlinux.org> 2.4.0-alt3
- fix for moving more than two files with identical names

* Tue Jan 16 2018 Oleg Solovyov <mcpain@altlinux.org> 2.4.0-alt2
- fix moving single files to trash

* Wed Dec 27 2017 Oleg Solovyov <mcpain@altlinux.org> 2.4.0-alt1
- new version

* Mon Dec 18 2017 Oleg Solovyov <mcpain@altlinux.org> 2.3.4-alt2
- move remote-deleted files to trash

* Wed Dec 13 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt1
- new version

* Mon Oct 09 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.3-alt1
- new version

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt1.M80P.1
- build for M80P

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt2
- rebuild with new libqt5keychain

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt0.M80P.1
- build for M80P

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt1
- new version (ALT#32649)

* Mon Feb 08 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Wed Oct 21 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Wed Oct 21 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt0.M70P.1
- build for M70P

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt1
- new version

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.3-alt1
- new version

* Mon Feb 02 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt0.M70P.1
- build for M70P

* Mon Feb 02 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- new version

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1.M70P.1
- built for M70P

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt2
- obsolete mirall

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt0.M70P.1
- built for M70P

* Fri Sep 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1
- new version

* Fri Aug 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3.M60P.2
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt4
- don't conflict with mirall
- bump release

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1.M60P.1
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- fix menu item

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt0.M60P.1
- built for M60P

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build
