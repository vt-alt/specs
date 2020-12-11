Name: eiskaltdcpp
Version: 2.4.0
Release: alt1

Summary: EiskaltDC++ - Direct Connect client

License: GPLv3
Group: Networking/File transfer
Url: http://code.google.com/p/eiskaltdc/

Source: %name-%version.tar
Patch: eiskaltdcpp-use_libidn2.patch

BuildRequires: boost-interprocess-devel bzlib-devel cmake gcc-c++
BuildRequires: libaspell-devel libgtk+2-devel libidn2-devel liblua-devel
BuildRequires: libnotify-devel libpcrecpp-devel qt5-phonon-devel
BuildRequires: qt5-tools-devel qt5-multimedia-devel qt5-script-devel
BuildRequires: libssl-devel perl-JSON-RPC perl-Term-ShellUI libminiupnpc-devel

%add_findreq_skiplist *xmms2_audacious2.ru_RU.UTF-8.php
%add_findreq_skiplist *commands.ru_RU.UTF-8.php

%description
EiskaltDC++ is a cross-platform program that uses the Direct Connect and
ADC protocol. It is compatible with other DC clients, such as the original DC
from Neomodus, DC++ and derivatives. EiskaltDC++ also interoperates
with all common DC hub software.

%package common
Group: Networking/File transfer
Summary: Common files for %name
Requires: lib%name = %EVR
BuildArch: noarch
%description common
Common files for %name

%package gtk
Group: Networking/File transfer
Summary: GTK-based graphical interface
Requires: %name-gtk-data = %EVR
%description gtk
Gtk interface based on code of FreeDC++ and LinuxDC++

%package gtk-data
Group: Networking/File transfer
Summary: noarch files for GTK-based graphical interface
Requires: %name-common = %EVR
BuildArch: noarch
%description gtk-data
noarch files for Gtk interface based on code of FreeDC++ and LinuxDC++

%package qt
Group: Networking/File transfer
Summary: Qt-based graphical interface
Provides: %name = %EVR
Obsoletes: %name <= 2.0.3-alt1
Requires: %name-qt-data = %EVR
%description qt
Qt-based graphical interface

%package qt-data
Group: Networking/File transfer
Summary: Qt-based graphical interface
Requires: %name-common = %EVR
BuildArch: noarch
%description qt-data
noarch files for Qt-based graphical interface

%package -n lib%name
Group: System/Libraries
Summary: eiskaltdcpp libraries
Obsoletes: libdcpp
%description -n lib%name
eiskaltdcpp libraries

%package daemon
Group: Networking/File transfer
Summary: Daemon interface
Requires: %name-common = %EVR
%description daemon
Daemon interface

%package cli
Group: Networking/File transfer
Summary: cli for Daemon
Requires: %name-daemon = %EVR
%description cli
command line interface for XML-RPC Daemon

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing $(pkg-config libpcre --cflags) $(pkg-config harfbuzz --cflags)
%cmake_insource \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_SKIP_RPATH:BOOL=yes \
-DCMAKE_C_FLAGS:STRING="%optflags" \
-DCMAKE_CXX_FLAGS:STRING="%optflags" \
-DCMAKE_INSTALL_PREFIX=%prefix \
-DLIB_DESTINATION=%_lib \
%if %_lib == lib64
-DLIBDIR=lib64 \
%endif
-DUSE_ASPELL=ON \
-DFREE_SPACE_BAR_C=ON \
-DUSE_MINIUPNP=ON \
-DLOCAL_MINIUPNP=ON \
-DUSE_GTK=ON \
-DDBUS_NOTIFY=ON \
-DUSE_JS=ON \
-DLUA_SCRIPT=ON \
-DWITH_LUASCRIPTS=ON \
-DWITH_SOUNDS=ON \
-DUSE_QT_SQLITE=ON \
-DNO_UI_DAEMON=ON \
-DJSONRPC_DAEMON=ON \
-DUSE_CLI_JSONRPC=ON \
-DPCRE_INCLUDE_DIR=$(pkg-config libpcre --variable=includedir) \
-DPERL_REGEX=ON \
-DUSE_QT=OFF \
-DUSE_QT5=ON \
-DUSE_IDN2=ON
%make_build

%install
%makeinstall_std
%find_lang %name-gtk
%find_lang lib%name

%files qt
%_bindir/%name-qt

%files qt-data
%_desktopdir/%name-qt.desktop
%_datadir/%name/qt
%_man1dir/%name-qt*

%files gtk
%_bindir/%name-gtk

%files gtk-data -f %name-gtk.lang
%_desktopdir/%name-gtk.desktop
%_datadir/%name/gtk
%_man1dir/%name-gtk*

%files -n lib%name -f lib%name.lang
%_libdir/lib%name.so.*

%files common
%_datadir/%name/emoticons
%_datadir/%name/examples
%_datadir/%name/sounds
%_datadir/%name/luascripts
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_pixmapsdir/*

%files daemon
%_bindir/%name-daemon
%_man1dir/%name-daemon*

%files cli
%_bindir/%name-cli-jsonrpc
%_man1dir/%name-cli*
%_datadir/%name/cli

%changelog
* Fri Dec 04 2020 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Build new version.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.10.0.691.git57ccdeb-alt1
- Build from last commit (Closes: #36782).

* Thu Jul 02 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.10.0.689.git0a574792-alt1
- Build from last commit.

* Sat Feb 22 2020 Nikita Ermakov <arei@altlinux.org> 2.2.10.0.646.git93944747-alt2
- Change BR from liblua5.1-devel to more general liblua-devel.

* Tue Dec 31 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.10.0.646.git93944747-alt1
- Build from last commit (Closes: #37709).

* Wed Nov 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.10.0.614.gitc9c510b8-alt2
- Fixed build.

* Mon May 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.10.0.614.gitc9c510b8-alt1
- Build from last commit (Closes: #36783).
- Change build scheme.
- Drop openssl patch (applied in 3b9c502).
- Adapt libIDN2 patch.
- Add BR on libminiupnpc-devel.
- Spec refactoring.

* Tue Oct 30 2018 Grigory Ustinov <grenka@altlinux.org> 2.2.10-alt3
- Build with libidn2.

* Wed Sep 26 2018 Grigory Ustinov <grenka@altlinux.org> 2.2.10-alt2
- Fix build with openssl1.1.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.10-alt1.1
- NMU: rebuilt with boost-1.67.0

* Mon Apr 23 2018 Grigory Ustinov <grenka@altlinux.org> 2.2.10-alt1
- Build new version.
- Transfer to qt5 (Closes: #34636).

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.8-alt1.qa3
- NMU: rebuild with new lua 5.1

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.8-alt1.qa2
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2.2.8-alt1.1
- rebuild with boost 1.57.0

* Tue Jun 25 2013 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.8-alt1
- 2.2.8 release (ALT#29105)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.7-alt1.1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt1.1
- Fixed build with Boost 1.52.0
- Built with Qt Declarative Ui and PCRE support

* Wed Aug 22 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.7-alt1
- 2.2.7 release (ALT#27653)
- daemon and cli use json

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1.1
- Fixed build

* Tue Jan 03 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.5-alt1
- 2.2.5 release

* Wed Oct 12 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.4-alt1
- 2.2.4 release
- Build with command line interface for XML-RPC Daemon

* Wed Oct 12 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt4
- Fix build

* Wed Sep 28 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt3
- Build with xmlrpc server daemon

* Wed Jul 13 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt2
- Build with Daemon (ALT#26360)

* Sat Jun 25 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.3-alt1
- 2.2.3 release

* Sat Jun 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.2-alt1
- 2.2.2 release

* Tue Apr 05 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt2
- Install luascripts

* Wed Mar 09 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.1-alt1
- 2.2.1 release

* Tue Feb 15 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt2
- Fix build

* Mon Jan 17 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt1
- 2.2.0 release

* Fri Jan 07 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt0.2.beta2
- Really 2.2.0 beta2 (ALT#24869)

* Tue Jan 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt0.1.beta2
- 2.2.0 beta2
- fix posible crashes (remove cmake macros. thanx Ivan A. Melnikov)

* Tue Nov 23 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.1-alt1
- 2.1.1 release

* Mon Nov 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt1
- 2.1.0 release

* Sun Oct 31 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.5.beta3
- 2.1.0-beta3

* Fri Oct 22 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.4.beta2
- 2.1.0-beta2

* Tue Oct 19 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.3.svn1989
- svn r1989 (ALT#24361)
- rename libdcpp to libeiskaltdcpp

* Thu Sep 02 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.2.svn1666
- svn r1666

* Thu Aug 12 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt0.1.svn1521
- svn r1521
- split to subpackages(qt,gtk,common,libdcpp)

* Wed Jun 09 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.3-alt1
- 2.0.3 release 

* Thu May 06 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.2-alt1
- 2.0.2 release

* Mon Apr 19 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.1-alt1
- 2.0.1 release

* Mon Mar 22 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0-alt1
- 2.0 release

* Fri Mar 19 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.99-alt0.2
- Updated to revision 366
  +  Fixed crushing on Oxygen theme
  +  Fixed desktop file (repocop)
  +  Added aspell support

* Sat Mar 06 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.99-alt0.1
- 1.99 (beta!)
- Initial build for sisyphus
