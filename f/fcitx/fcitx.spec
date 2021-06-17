# due to kcmshell4
%filter_from_requires /^kde4base-runtime-core/d
Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install pkgconfig(cairo-xlib) pkgconfig(fontconfig) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(xkbcommon)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx.conf
%{!?gtk2_binary_version: %global gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
%{!?gtk3_binary_version: %global gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}

Name:			fcitx
Summary:		An input method framework
Version:		4.2.9.8
Release:		alt2_1.p9.1
License:		GPLv2+
URL:			https://fcitx-im.org/wiki/Fcitx
Source0:		http://download.fcitx-im.org/fcitx/%{name}-%{version}_dict.tar.xz
Source1:		xinput-%{name}
BuildRequires:		gcc-c++
BuildRequires:		libpango-devel libpango-gir-devel, libdbus-devel, opencc-devel
BuildRequires:		wget, intltool, chrpath, sysconftool, opencc
BuildRequires:		ctest cmake, libtool, doxygen icu-utils libicu-devel
BuildRequires:		libqt4-declarative libqt4-devel libqt4-help qt4-designer qt4-doc-html qt5-declarative-devel qt5-designer qt5-tools gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel, libicu-devel
BuildRequires:		libX11-devel libXvMC-devel xorg-proto-devel, xorg-xtrans-devel
BuildRequires:		gobject-introspection-devel, libxkbfile-devel
BuildRequires:		libenchant-devel, iso-codes-devel icu-utils libicu-devel
BuildRequires:		libX11-devel, libdbus-glib-devel, dbus-tools-gui
BuildRequires:		desktop-file-utils, libxml2-devel
BuildRequires:		lua-devel, extra-cmake-modules
BuildRequires:		xkeyboard-config-devel
BuildRequires:		libuuid-devel
BuildRequires:		libjson-c-devel
Requires:		%{name}-data = %{version}-%{release}
Requires:		imsettings
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-gtk3 = %{version}-%{release}
Requires:		%{name}-gtk2 = %{version}-%{release}
Source44: import.info

%description
Fcitx is an input method framework with extension support. Currently it
supports Linux and Unix systems like FreeBSD.

Fcitx tries to provide a native feeling under all desktop as well as a light
weight core. You can easily customize it to fit your requirements.

%package data
Group: System/Libraries
Summary:		Data files of Fcitx
BuildArch:		noarch
Requires:		icon-theme-hicolor
Requires:		dbus

%description data
The %{name}-data package provides shared data for Fcitx.

%package libs
Group: System/Libraries
Summary:		Shared libraries for Fcitx
Provides:		%{name}-keyboard = %{version}-%{release}
Obsoletes:		%{name}-keyboard =< 4.2.3

%description libs
The %{name}-libs package provides shared libraries for Fcitx

%package devel
Group: Development/Other
Summary:		Development files for Fcitx
Requires:		%{name}-libs = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx libraries.

%package table-chinese
Group: System/Libraries
Summary:		Chinese table of Fcitx
BuildArch:		noarch
Requires:		%{name}-table = %{version}-%{release}

%description table-chinese
The %{name}-table-chinese package provides other Chinese table for Fcitx.

%package gtk2
Group: System/Libraries
Summary:		Fcitx IM module for gtk2
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}

%description gtk2
This package contains Fcitx IM module for gtk2.

%package gtk3
Group: System/Libraries
Summary:		Fcitx IM module for gtk3
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		imsettings-gnome

%description gtk3
This package contains Fcitx IM module for gtk3.

%package qt4
Group: System/Libraries
Summary:		Fcitx IM module for qt4
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}

%description qt4
This package contains Fcitx IM module for qt4.

%package pinyin
Group: System/Libraries
Summary:		Pinyin Engine for Fcitx
URL:			https://fcitx-im.org/wiki/Built-in_Pinyin
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}

%description pinyin
This package contains pinyin engine for Fcitx.

%package qw
Group: System/Libraries
Summary:		Quwei Engine for Fcitx
URL:			https://fcitx-im.org/wiki/QuWei
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}

%description qw
This package contains Quwei engine for Fcitx.

%package table
Group: System/Libraries
Summary:		Table Engine for Fcitx
URL:			https://fcitx-im.org/wiki/Table
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}
Requires:		%{name}-pinyin = %{version}-%{release}

%description table
This package contains table engine for Fcitx.


%prep
%setup -q
# bash4
sed -i '1s,env bash,env bash4,' data/script/fcitx-diagnose.sh

%build
%{fedora_v2_cmake} -DENABLE_GTK3_IM_MODULE=On -DENABLE_QT_IM_MODULE=On -DENABLE_OPENCC=On -DENABLE_LUA=On -DENABLE_GIR=On -DENABLE_XDGAUTOSTART=Off
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install 

find %{buildroot}%{_libdir} -name '*.la' -delete -print

install -pm 644 -D %{SOURCE1} %{buildroot}%{_xinputconf}

# patch fcitx4-config to use pkg-config to solve libdir to avoid multiarch
# confilict
sed -i -e 's:%{_libdir}:`pkg-config --variable=libdir fcitx`:g' \
  %{buildroot}%{_bindir}/fcitx4-config

chmod +x %{buildroot}%{_datadir}/%{name}/data/env_setup.sh

%find_lang %{name}

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-skin-installer.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_fcitx<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_xinputconf}	55
EOF

%files -f %{name}.lang
%_altdir/xinputrc_fcitx
%doc AUTHORS ChangeLog THANKS TODO
%doc --no-dereference COPYING
%config %{_xinputconf}
%{_bindir}/fcitx-*
%{_bindir}/fcitx
%{_bindir}/createPYMB
%{_bindir}/mb2org
%{_bindir}/mb2txt
%{_bindir}/readPYBase
%{_bindir}/readPYMB
%{_bindir}/scel2org
%{_bindir}/txt2mb
%{_datadir}/applications/%{name}-skin-installer.desktop
%dir %{_datadir}/%{name}/dbus/
%{_datadir}/%{name}/dbus/daemon.conf
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/x-fskin.xml
%{_mandir}/man1/createPYMB.1*
%{_mandir}/man1/fcitx-remote.1*
%{_mandir}/man1/fcitx.1*
%{_mandir}/man1/mb2org.1*
%{_mandir}/man1/mb2txt.1*
%{_mandir}/man1/readPYBase.1*
%{_mandir}/man1/readPYMB.1*
%{_mandir}/man1/scel2org.1*
%{_mandir}/man1/txt2mb.1*

%files libs
%doc --no-dereference COPYING
%{_libdir}/libfcitx*.so.*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/%{name}-[!pqt]*.so
%{_libdir}/%{name}/%{name}-punc.so
%{_libdir}/%{name}/%{name}-quickphrase.so
%{_libdir}/%{name}/libexec/
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Fcitx-1.0.typelib

%files data
%doc --no-dereference COPYING
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/24x24/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/skin/
%dir %{_datadir}/%{name}/addon
%{_datadir}/%{name}/addon/%{name}-[!pqt]*.conf
%{_datadir}/%{name}/addon/%{name}-punc.conf
%{_datadir}/%{name}/addon/%{name}-quickphrase.conf
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/spell/
%dir %{_datadir}/%{name}/imicon/
%dir %{_datadir}/%{name}/inputmethod/
%dir %{_datadir}/%{name}/configdesc/
%dir %{_datadir}/%{name}/table/
%{_datadir}/%{name}/configdesc/[!ft]*.desc
%{_datadir}/%{name}/configdesc/fcitx-[!p]*.desc
%{_datadir}/dbus-1/services/org.fcitx.Fcitx.service

%files devel
%doc --no-dereference COPYING
%{_bindir}/fcitx4-config
%{_libdir}/libfcitx*.so
%{_libdir}/pkgconfig/fcitx*.pc
%{_includedir}/fcitx*
%{_datadir}/cmake/%{name}/
%{_docdir}/%{name}/*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Fcitx-1.0.gir

%files table-chinese
%doc %_docdir/%name
%{_datadir}/%{name}/table/*
%{_datadir}/%{name}/imicon/[!ps]*.png

%files pinyin
%doc %_docdir/%name
%{_datadir}/%{name}/inputmethod/pinyin.conf
%{_datadir}/%{name}/inputmethod/shuangpin.conf
%{_datadir}/%{name}/pinyin/
%{_datadir}/%{name}/configdesc/fcitx-pinyin.desc
%{_datadir}/%{name}/configdesc/fcitx-pinyin-enhance.desc
%{_datadir}/%{name}/addon/fcitx-pinyin.conf
%{_datadir}/%{name}/addon/fcitx-pinyin-enhance.conf
%{_datadir}/%{name}/imicon/pinyin.png
%{_datadir}/%{name}/imicon/shuangpin.png
%{_libdir}/%{name}/%{name}-pinyin.so
%{_libdir}/%{name}/%{name}-pinyin-enhance.so
%{_datadir}/%{name}/py-enhance/

%files qw
%doc %_docdir/%name
%{_datadir}/%{name}/inputmethod/qw.conf
%{_libdir}/%{name}/%{name}-qw.so
%{_datadir}/%{name}/addon/fcitx-qw.conf

%files table
%doc %_docdir/%name
%{_datadir}/%{name}/configdesc/table.desc
%{_libdir}/%{name}/%{name}-table.so
%{_datadir}/%{name}/addon/fcitx-table.conf

%files gtk2
%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/im-fcitx.so

%files gtk3
%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/im-fcitx.so

%ifnarch riscv64
%files qt4
%{_libdir}/qt4/plugins/inputmethods/qtim-fcitx.so
%endif

%changelog
* Mon Jun 07 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.9.8-alt2_1.p9.1
- Backport new version to p9 branch (ALT #40162).

* Mon May 17 2021 Igor Vlasenko <viy@altlinux.org> 4.2.9.8-alt2_2
- build w/o kde4

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 4.2.9.8-alt2_1
- updated buildrequires

* Fri Sep 11 2020 Igor Vlasenko <viy@altlinux.ru> 4.2.9.8-alt1_1
- new version

* Thu Jun 18 2020 Nikita Ermakov <arei@altlinux.org> 4.2.9.7-alt1_3
- Exclude qt4 support for riscv64

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 4.2.9.7-alt1_2
- update to new release by fcimport

* Tue Oct 08 2019 Sergey V Turchin <zerg@altlinux.org> 4.2.9.6-alt2_4.1
- drop requires to kde4

* Mon Apr 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.9.6-alt2_4
- rebuild (closes: #36598)

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.9.6-alt1_4
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.9.4-alt1_1
- update by fc import

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt2.1.1
- rebuild with new lua 5.3

* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.2.7-alt2.1
- rebuild with new icu

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 4.2.7-alt2
- build for Sisyphus

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1_4
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1_1
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6.1-alt1_3
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6.1-alt1_2
- initial fc import

