Name:           x2goclient
Version:        4.1.2.2
Release:        alt1
Summary:        X2Go Client application (Qt)

Group:          Communications
License:        GPLv2+
URL:            http://www.x2go.org
Source0:        %name-%version.tar
Source1:        x2goclient_ru.ts
# Drop clumsy attempt at Kerberos delegation
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=731
Patch0:         x2goclient-krb5.patch
# ensure RPM_LD_FLAGS/RPM_OPT_FLAGS are used
# https://bugzilla.redhat.com/show_bug.cgi?id=1306463
Patch2:         x2goclient-optflags.patch
Patch3:  	x2goclient-alt-startkde.patch
Patch4:		x2goclient-encoding.patch
Patch5:		x2goclient-alt-no-pam.patch
Patch7:		x2goclient-alt-select-broker-sessions.patch
Patch9:		x2goclient-use-utf8.patch

BuildRequires(pre): libssh-devel
BuildRequires(pre): rpm-build-apache2
BuildRequires:  gcc-c++
BuildRequires:  libcups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXpm-devel
BuildRequires:  man
BuildRequires:  libldap-devel
BuildRequires:  qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-tools
BuildRequires:  libX11-devel
BuildRequires:  libssl-devel
BuildRequires:  perl-base
BuildRequires:  perl-Proc-Simple
BuildRequires:  perl-Term-ReadPassword
BuildRequires:  zlib-devel
Requires:       icon-theme-hicolor
Requires:       nx-libs >= 3.5.0.31
Requires:       nxproxy >= 3.5.0.31
# For GSSAPI authenticated connections
Requires:       openssh-clients
# For local folder sharing and printing
Requires:       openssh-server

%description
X2Go is a server-based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client-side mass storage mounting support
- client-side printing support
- audio support
- authentication by smartcard and USB stick

X2Go Client is a graphical client (Qt) for the X2Go system.
You can use it to connect to running sessions and start new sessions.


%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch9 -p1
# update russian translations
cat %SOURCE1 >res/i18n/x2goclient_ru.ts
# Fix up install issues
sed -i -e 's/-o root -g root//' Makefile
sed -i -e '/^MOZPLUGDIR=/s/lib/%{_lib}/' Makefile
# Use system qtbrowserplugin
sed -i -e '/CFGPLUGIN/aTEMPLATE=lib' x2goclient.pro
sed -i -e '/^LIBS /s/$/ -ldl/' x2goclient.pro
for f in Makefile config_linux.sh ; do
    sed -i 's|-qt4|-qt5|g' $f
    sed -i 's|X2GO_CLIENT_TARGET=plugin|X2GO_CLIENT_TARGET=""|g' $f
done

%define libsshver %(rpm -q --qf '%%{VERSION}' libssh 0.8)
%if "%(rpmvercmp %libsshver 0.8 )" >= "0"
# libssh-0.8
sed -i -e '/^LIBS /s/-lssh_threads//' x2goclient.pro
%endif

%build
export PATH=%{_qt5_bindir}:$PATH
%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=%_prefix install_client install_man
desktop-file-validate %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_sysconfdir/httpd/conf.d
ln -s ../../x2go/x2goplugin-apache.conf %buildroot%_sysconfdir/httpd/conf.d/x2goplugin-provider.conf

%files
%doc AUTHORS COPYING LICENSE 
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/
%_man1dir/%name.1*

%changelog
* Wed Jun 03 2020 Oleg Solovyov <mcpain@altlinux.org> 4.1.2.2-alt1
- New version (Closes: #38558)

* Wed Jan 29 2020 Oleg Solovyov <mcpain@altlinux.org> 4.1.2.1-alt3
- Strip home from paths (Closes: #37931, #37934)
- Send commands via SSH using UTF-8 (Closes: #37933)

* Thu Aug 01 2019 Oleg Solovyov <mcpain@altlinux.org> 4.1.2.1-alt2
- Allow session selection in broker mode

* Tue Oct 16 2018 Oleg Solovyov <mcpain@altlinux.org> 4.1.2.1-alt1.1
- Check for libssh >= 0.8

* Mon Oct 15 2018 Oleg Solovyov <mcpain@altlinux.org> 4.1.2.1-alt1
- New version

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 4.1.1.1-alt9
- fix to build with Qt-5.11
- fix to build with libssh-0.8

* Thu Jun 21 2018 Oleg Solovyov <mcpain@altlinux.org> 4.1.1.1-alt8
- fix remote printing

* Fri Jun 15 2018 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1.1-alt7
- fix window title encoding (patch updated)
  (thx Oleg Solovyov <mcpain@altlinux.org>
  and Sergey V Turchin <zerg@altlinux.org>).

* Wed Jun 06 2018 Oleg Solovyov <mcpain@altlinux.org> 4.1.1.1-alt6
- fix window title encoding

* Wed Apr 25 2018 Sergey V Turchin <zerg@altlinux.org> 4.1.1.1-alt5
- Update russian translation.

* Mon Apr 16 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.1-alt3
- Build with Qt5 (thanks zerg@ for the patch).
- Use startkde5 instead of startkde.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.1-alt2
- Use nx-libs.

* Thu Feb 22 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.1-alt1
- New version.
- Return to old nx.

* Wed Feb 07 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.1.0-alt2
- Use nxproxy-x2go

* Mon Nov 06 2017 Andrey Cherepanov <cas@altlinux.org> 4.1.1.0-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 4.1.0.1-alt1
- New version

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 4.1.0.0-alt2
- New version

* Fri Aug 04 2017 Andrey Cherepanov <cas@altlinux.org> 4.0.5.0-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.5.0-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.5.0-alt1_3
- update to new release by fcimport

* Mon Nov 10 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.3.0-alt1_1
- new version

