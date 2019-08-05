%add_findreq_skiplist %perl_vendor_archlib/*

%def_disable perl
%def_disable tcl
%def_disable tk
%def_enable nss
%def_enable cyrus_sasl
%def_disable gnutls
%def_disable gevolution
%def_enable meanwhile
%def_disable cap
%def_enable nm
%def_disable mono
%def_enable consoleui
%def_enable dbus
%def_enable avahi
%def_enable dot
%def_enable doxygen
%def_enable relnot
%def_enable idn
%def_enable farstream
%def_enable gstreamer
%def_enable screensaver
%def_enable gestures
%def_enable gtkspell
%def_enable devhelp

# X session management
%def_enable sm

# voice and video
%def_enable vv

Name: pidgin
Version: 2.13.0
Release: alt6

Summary: A GTK+ based multiprotocol instant messaging client
License: GPL
Group: Networking/Instant messaging
Url: http://pidgin.im
Packager: Alexey Shabalin <shaba@altlinux.ru>

Provides: gaim = %version
Obsoletes: gaim
%{?_disable_gevolution:Obsoletes: pidgin-gevolution <= %version-%release}

Conflicts: pidgin-mini

Requires: libpurple = %version-%release
Requires(pre): GConf

Source0: %name-%version.tar
Source2: purple-altlinux-prefs.xml
Patch0: %name-%version-%release.patch

# From configure.ac
BuildRequires: glib2-devel libgtk+2-devel
BuildRequires: libpango-devel >= 1.4.0
BuildRequires: libXext-devel libX11-devel
%{?_enable_gtkspell:BuildRequires: libgtkspell-devel >= 2.0.2}
%{?_enable_nss:BuildRequires: libnss-devel libnspr-devel}
%{?_enable_cyrus_sasl:BuildRequires: libsasl2-devel}
%{?_enable_gnutls:BuildRequires: libgnutls-devel}
%{?_enable_consoleui:BuildRequires: libncurses-devel libncursesw-devel}
%{?_enable_nm:BuildRequires: libnm-devel}
%{?_enable_meanwhile:BuildRequires: libmeanwhile-devel}
%{?_enable_perl:BuildRequires: perl-devel}
%{?_enable_tcl:BuildRequires: tcl-devel}
%{?_enable_tk:BuildRequires: tk-devel}
%{?_enable_mono:BuildRequires: mono-devel mono-mcs rpm-build-mono mono-nunit-devel /proc}
%{?_enable_gevolution:BuildRequires: evolution-data-server-devel}
%{?_enable_dbus:BuildRequires: libdbus-devel >= 0.35 libdbus-glib-devel >= 0.35}
%{?_enable_avahi:BuildRequires: libavahi-devel libavahi-glib-devel}
%{?_enable_dot:BuildRequires: graphviz}
%{?_enable_doxygen:BuildRequires: doxygen}
%{?_enable_idn:BuildRequires: libidn-devel}
%{?_enable_farstream:BuildRequires: libfarstream0.2-devel >= 0.2.7}
%{?_enable_vv:BuildRequires: gst-plugins1.0-devel}
%{?_enable_gstreamer:BuildRequires: gstreamer1.0-devel}
%{?_enable_sm:BuildRequires: libSM-devel}
%{?_enable_screensaver:BuildRequires: libXScrnSaver-devel xorg-scrnsaverproto-devel}
BuildRequires: libsqlite3-devel >= 3.3
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires(pre): GConf libGConf-devel

BuildRequires: gcc-c++ libgpg-error
BuildRequires: python3-devel
# for shared gadu plugin
BuildRequires: libgadu-devel >= 1.11.0
BuildRequires: intltool
# now intltool wants that
BuildRequires: perl-XML-Parser

BuildRequires: desktop-file-utils
BuildRequires: ca-certificates

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, SILC, Simple and
Zephyr.  These protocols are implemented using a modular, easy to
use design.  To use a protocol, just add an account using the
account editor.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, or ICQ Inc.

%package devel
Summary: Development headers, documentation, and libraries for Pidgin
Group: Development/Other
Requires: %name = %version-%release
Requires: libpurple-devel = %version-%release
Provides: gaim-devel = %version
Obsoletes: gaim-devel
Conflicts: pidgin-mini-devel

%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%package -n libpurple
Summary: libpurple library for IM clients like Pidgin and Finch
Group: System/Libraries
Requires: ca-certificates
Conflicts: libpurple-mini

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM,
Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n libpurple-devel
Summary: Development headers, documentation, and libraries for libpurple
Group: Development/Other
Requires: libpurple = %version-%release
Conflicts: libpurple-mini-devel

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%if_enabled relnot
%package -n %name-relnot
Summary: Release notification plugin for Pidgin
Group: Networking/Instant messaging
Requires: %name = %version-%release

%description -n %name-relnot
Release notification plugin for Pidgin.
%endif

%if_enabled gevolution
%package -n %name-gevolution
Summary: Gevolution plugin for Pidgin
Group: Networking/Instant messaging
Requires: %name = %version-%release
Obsoletes: gaim-gevolution
Provides: gaim-gevolution = %version

%description -n %name-gevolution
Gevolution plugin for Pidgin.
%endif

%if_enabled mono
%package -n libpurple-mono
Summary: Mono .NET plugin support for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
Obsoletes: gaim-mono
Provides: gaim-mono = %version

%description -n libpurple-mono
Mono support for Pidgin.
%endif

%if_enabled perl
%package -n libpurple-perl
Summary: Perl support for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
Requires: perl-base
Obsoletes: gaim-perl
Provides: gaim-perl = %version

%description -n libpurple-perl
Perl support for Pidgin.
%endif

%if_enabled tcl
%package -n libpurple-tcl
Summary: Tcl/Tk support for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
Obsoletes: gaim-tcl
Provides: gaim-tcl = %version

%description -n libpurple-tcl
Tcl/Tk support for Pidgin.
%endif

%if_enabled consoleui
%package -n finch
Summary: A text-based user interface for Pidgin
Group: Networking/Instant messaging
Requires: libpurple = %version-%release
Provides: gaim-text = %version
Obsoletes: gaim-text

%description -n finch
A text-based user interface for using libpurple.  This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.

%package -n finch-devel
Summary: Headers etc. for finch stuffs
Group: Development/Other
Requires: finch = %version-%release
Requires: libpurple-devel = %version-%release
Provides: gaim-text-devel = %version
Obsoletes: gaim-text-devel

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.
%endif

%if_enabled dbus
%package -n libpurple-dbus
Summary: D-Bus client utilities for Pidgin
Group: Networking/Instant messaging
Requires: %name = %version-%release
Requires: libpurple-client = %version-%release
Obsoletes: gaim-dbus
Provides: gaim-dbus = %version

%description -n libpurple-dbus
D-Bus client utilities for Pidgin.

%package -n libpurple-client
Summary: Client library for IM clients like Pidgin and Finch
Group: System/Libraries

%description -n libpurple-client
This package provides client library for purple-based IM like Pidgin and Finch
%endif

%prep
%setup
%patch0 -p1

cp %SOURCE2 prefs.xml

# Bug #528796: Get rid of #!/usr/bin/env python
# Upstream refuses to use ./configure --python-path= in these scripts.
for file in finch/plugins/pietray.py libpurple/purple-remote libpurple/plugins/dbus-buddyicons-example.py \
            libpurple/plugins/startup.py libpurple/purple-url-handler libpurple/purple-notifications-example; do
    sed -i 's/env python/python3/' $file
done

%build
%autoreconf
%configure \
	--disable-schemas-install \
	%{subst_enable avahi} \
	%{subst_enable dot} \
	%{subst_enable doxygen} \
	%{subst_enable mono} \
	%{subst_enable cap} \
	%{subst_enable nm} \
	%{subst_enable perl} \
	%{subst_enable gevolution} \
	%{subst_enable dbus} \
	%{subst_enable tk} \
	%{subst_enable tcl} \
	%{subst_enable consoleui} \
	%{subst_enable meanwhile} \
	%{subst_enable idn} \
	%{subst_enable farstream} \
	%{subst_enable vv} \
	%{subst_enable gstreamer} \
	%{subst_enable sm} \
	%{subst_enable screensaver} \
	%{subst_enable gestures} \
	%{subst_enable gtkspell} \
	%{subst_enable devhelp} \
%if_disabled gstreamer
	--disable-gstreamer-interfaces \
%endif
%if_enabled gnutls
	--enable-gnutls=yes \
%else
	--enable-gnutls=no \
%endif
%if_enabled cyrus_sasl
	--enable-cyrus-sasl \
%else
	--disable-cyrus-sasl \
%endif
%if_enabled nss
	--with-nss-includes=%_includedir/nss \
	--with-nspr-includes=%_includedir/nspr \
	--with-nspr-libs=%_libdir \
	--with-nss-libs=%_libdir \
	--enable-nss=yes \
%else
	--enable-nss=no \
%endif
%if_enabled perl
	--with-perl-lib=vendor \
%endif
	--with-python=%__python3 \
	--with-system-ssl-certs=%_datadir/ca-certificates \
	--with-extraversion=%release


%make_build

%install
%make DESTDIR=%buildroot install

# install ALTLinux pidgin default prefs.xml
mkdir -p %buildroot%_sysconfdir/purple
install -m 644 prefs.xml %buildroot%_sysconfdir/purple/prefs.xml
sed -i 's|/usr/lib|%_libdir|' %buildroot%_sysconfdir/purple/prefs.xml

find %buildroot%_libdir -name \*.la -delete
# remove non-plugin unrequired library symlinks
rm -f %buildroot%_libdir/purple-2/liboscar.so
rm -f %buildroot%_libdir/purple-2/libymsg.so

%find_lang --with-gnome %name

%post
%gconf2_install purple

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall purple
fi

%files -f %name.lang
%doc AUTHORS COPYRIGHT INSTALL NEWS README doc/*.txt
%config %_sysconfdir/gconf/schemas/*
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_datadir/appdata/*.appdata.xml
%_pixmapsdir/%name
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.*
%if_enabled perl
%perl_vendor_archlib/Pidgin.pm
%dir %perl_vendor_autolib/Pidgin
%perl_vendor_autolib/Pidgin/*
%perl_vendor_man3dir/Pidgin*
%endif
%if_enabled gevolution
%exclude %_libdir/%name/gevolution.so
%endif
%if_enabled relnot
%exclude %_libdir/%name/relnot.so
%endif

%if_enabled relnot
%files -n %name-relnot
%_libdir/%name/relnot.so
%endif

%files -n libpurple
%dir %_sysconfdir/purple
%config(noreplace) %_sysconfdir/purple/*
%_libdir/libpurple.so.*
%_libdir/purple-2
%_datadir/sounds/purple
%if_enabled tcl
%exclude %_libdir/purple-2/tcl.so
%endif
%if_enabled mono
%exclude %_libdir/purple-2/mono.so
%exclude %_libdir/purple-2/*.dll
%endif
%if_enabled perl
%exclude %_libdir/purple-2/perl.so
%endif

%if_enabled dbus
%files -n libpurple-dbus
%_bindir/purple-client-example
%_bindir/purple-remote
%_bindir/purple-send
%_bindir/purple-send-async
%_bindir/purple-url-handler

%files -n libpurple-client
%_libdir/libpurple-client.so.*
%endif

%if_enabled gevolution
%files -n %name-gevolution
%_libdir/%name/gevolution.so
%endif

%if_enabled mono
%files -n libpurple-mono
%_libdir/purple-2/mono.so
%_libdir/purple-2/*.dll
%endif

%if_enabled perl
%files -n libpurple-perl
%_libdir/purple-2/perl.so
%perl_vendor_archlib/Purple.pm
%dir %perl_vendor_autolib/Purple
%perl_vendor_autolib/Purple/*
%perl_vendor_man3dir/Purple*
%endif

%if_enabled tcl
%files -n libpurple-tcl
%_libdir/purple-2/tcl.so
%endif

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%files -n libpurple-devel
%doc ChangeLog.API HACKING PLUGIN_HOWTO libpurple/purple-notifications-example
%_includedir/libpurple
%_libdir/libpurple.so
%if_enabled dbus
%_libdir/libpurple-client.so
%endif
%_pkgconfigdir/purple.pc
%_datadir/aclocal/purple.m4

%if_enabled consoleui
%files -n finch
%_man1dir/finch.*
%_bindir/finch
%_libdir/libgnt.so.*
%_libdir/gnt
%_libdir/finch

%files -n finch-devel
%_includedir/finch
%_includedir/gnt
%_pkgconfigdir/gnt.pc
%_pkgconfigdir/finch.pc
%_libdir/libgnt.so
%endif

%changelog
* Tue Jul 16 2019 Alexey Shabalin <shaba@altlinux.org> 2.13.0-alt6
- Build against with NM
- Drop aim support
- Build with python3
- fix generate russian comment in desktop file (ALT bug 36824)

* Wed Dec 19 2018 Grigory Ustinov <grenka@altlinux.org> 2.13.0-alt5
- Rebuild without NM support.

* Thu Dec 13 2018 Grigory Ustinov <grenka@altlinux.org> 2.13.0-alt4
- Rebuild with libidn support.

* Wed Dec 12 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.13.0-alt3
- fixed libpurple's error: '/usr/bin/ld: cannot find -ljabber'

* Thu Nov 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.13.0-alt2
- Rebuild without libidn support, because it's deprecated.

* Thu Mar 29 2018 Alexey Shabalin <shaba@altlinux.ru> 2.13.0-alt1
- 2.13.0

* Mon Mar 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.11.0-alt1
- 2.11.0

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.12-alt2
- new libpurple-client subpackage

* Wed Feb 10 2016 Alexey Shabalin <shaba@altlinux.ru> 2.10.12-alt1
- 2.10.12

* Fri Jan 30 2015 Alexey Shabalin <shaba@altlinux.ru> 2.10.11-alt2
- rebuilt against libfarstream-0.2.so.5

* Wed Nov 26 2014 Alexey Shabalin <shaba@altlinux.ru> 2.10.11-alt1
- 2.10.11

* Mon Oct 27 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.10.10-alt1
- New version (CVE-2014-3694, CVE-2014-3695, CVE-2014-3696, CVE-2014-3697
  CVE-2014-3698).

* Tue Apr 08 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.10.9-alt1
- New version (#29937).

* Mon Oct 07 2013 Alexey Shabalin <shaba@altlinux.ru> 2.10.7-alt3
- rebuild with new libsasl2-3

* Wed Mar 06 2013 Alexey Shabalin <shaba@altlinux.ru> 2.10.7-alt2
- disable build cap plugin

* Mon Mar 04 2013 Alexey Shabalin <shaba@altlinux.ru> 2.10.7-alt1
- 2.10.7
- build with sasl support

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 2.10.6-alt3
- port to GStreamer 1.0 and Farstream 0.2

* Tue Oct 02 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.6-alt2
- disable gevolution plugin

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.6-alt1
- 2.10.6
- fixed CVE-2012-3374

* Fri May 18 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.4-alt1
- 2.10.4
- fixed CVE-2012-2214, CVE-2012-2318, CVE-2012-1178, CVE-2011-4939
- drop upstreamed farstream patch

* Thu Mar 29 2012 Michael Shigorin <mike@altlinux.org> 2.10.1-alt3
- rebuilt against current gnome

* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt2
- port to farstream (fc patch)

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt1
- 2.10.1 (fixed CVE-2011-3594,CVE-2011-4601,CVE-2011-4602,CVE-2011-4603)

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.10.0-alt2.1
- Rebuild with Python-2.7

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt2
- rebuild
- build --with-system-ssl-certs

* Tue Aug 23 2011 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Jun 29 2011 Alexey Shabalin <shaba@altlinux.ru> 2.9.0-alt2
- add conflicts with pidgin-mini

* Tue Jun 28 2011 Alexey Shabalin <shaba@altlinux.ru> 2.9.0-alt1
- 2.9.0 (fixed CVE-2011-2485: remote denial of service from corrupt buddy icons)
- enable evolution plugin

* Wed Jun 08 2011 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue May 31 2011 Alexey Shabalin <shaba@altlinux.ru> 2.7.11-alt2
- rebuild for NetworkManager 0.9

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 2.7.11-alt1
- 2.7.11
- CVE-2011-1091: remote denial of service in Yahoo protocol plugin

* Mon Feb 14 2011 Alexey Shabalin <shaba@altlinux.ru> 2.7.10-alt1
- 2.7.10

* Wed Dec 29 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.9-alt1
- 2.7.9

* Tue Dec 21 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.8-alt1
- 2.7.8

* Thu Nov 25 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.7-alt1
- 2.7.7

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.5-alt1
- 2.7.5

* Sun Oct 24 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.4-alt1
- 2.7.4

* Wed Aug 11 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.3-alt1
- 2.7.3
- fixed in 2.7.2:
 + CVE-2010-2528: crash bug that can be triggered by remove users

* Mon May 31 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.1-alt1
- 2.7.1
- Add Obsoletes pidgin-gevolution

* Wed May 26 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt2
- Upstream backports:
 3c30f64efedafc379b6536852bbb3b6ef5f1f6c9 - fix for receiving HTML on ICQ
 13fbe0815f84d5b3c001947559f5818c10275f4c - prevent null deref on disconnecting account
 c4a874926d07b8597db4b78a181a89cf720a8418 - fix blinking tray icon on new message
 cfe0e649dda34d9252d40d8f67e445336a247998 - prevent race condition on Yahoo! login
 e3dd36706068f3b8eabd630ff71d270c145cce42 - fix crash in Oscar
 13fbe0815f84d5b3c001947559f5818c10275f4c - fix crash during network disconnect
- patches for support pidgin-sipe (upstream #11598, #11830)

* Sat May 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- 2.7.0
- fix NTLM proxy authorization (ALT #23474)
- Upstream backport:
  87ada76abf90c44e615679efc5f8128bb941bba1 Reduce MSN traffic

* Mon Apr 19 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.6-alt4
- disable build gevolution plugin; it hasn't been ported to the de-bonobo-ized eds-2.30

* Sat Mar 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.6-alt3
- update Russian translation by Alexandre Prokoudine

* Sat Mar 06 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.6-alt2
- Upstream backports:
  + Fix AIM SSL clientLogin
  + Fix AIM clientLogin with proxy

* Mon Feb 22 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.6-alt1
- 2.6.6:
    + Fixes a remote MSN SLP crash (CVE-2010-0277) (Closes: #566775)
    + Fixes a remote Finch XMPP crash (CVE-2010-0420)
    + Fixes a remote smiley freeze/CPU pegging DoS (CVE-2010-0423)
- drop %%add_findprov_lib_path for %%_libdir/pidgin %%_libdir/purple-2 %%_libdir/finch

* Mon Jan 25 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.5-alt2
- build without system-ssl-certs

* Tue Jan 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Fri Dec 11 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.4-alt1
- 2.6.4
- drop patch for old be translation
- update russian translation, thx to dkoryavov at yandex.ru

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.3-alt2.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt2
- sync spec with pidgin-mini, thx to php-coder@
- update russian translation from attachments #21176
- Fixed uncompressed manual page (noted by repocop), thx to php-coder@

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Sep 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2
- update russian translation

* Mon Sep 07 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.1-alt3
- define OSCAR_DEFAULT_CUSTOM_ENCODING as "CP1251" (patch4) (ALT #16815)

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt2
- fixed using GNOME proxy settings properly

* Wed Aug 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fixed CVE-2009-2694

* Fri Jul 17 2009 Michael Shigorin <mike@altlinux.org> 2.5.8-alt2
- built with NM support enabled by default (shrek@'s request)

* Fri Jul 10 2009 Alexey Shabalin <shaba@altlinux.ru> 2.5.8-alt1
- 2.5.8
- fixed CVE-2009-1889

* Thu Jun 25 2009 Michael Shigorin <mike@altlinux.org> 2.5.7-alt1
- 2.5.7 rebuilt for Sisyphus
  + solves Yahoo Messenger problems (protocol 16 support)
- restored Packager: to shaba@
- minor spec cleanup

* Wed Jun 24 2009 Alex Negulescu <a@wdu.ro> 2.5.7-alt0
- initial build of 2.5.7, which permits connecting to all messenger servers

* Fri May 22 2009 Michael Shigorin <mike@altlinux.org> 2.5.6-alt1
- 2.5.6:
  + CVE-2009-1373: XMPP SOCKS5 stream server buffer overflow
  + CVE-2009-1374: remote DoS with a special QQ packet
  + CVE-2009-1375: PurpleCircBuffer (XMPP/Sametime) BoF
  + CVE-2009-1376: buffer overflow via specially crafted SLP
    message due to incomplete fix for CVE-2008-2927
- thanks crux@ for notification (fixes: #20141)

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 2.5.5-alt2
- fixed FTBFS

* Wed Mar 11 2009 Michael Shigorin <mike@altlinux.org> 2.5.5-alt1
- forward-ported M41 spec to Sisyphus: it was cleaned up
  but Sisyphus spec got better in the meanwhile too

* Wed Mar 04 2009 Michael Shigorin <mike@altlinux.org> 2.5.5-alt0.M41.1
- 2.5.5

* Thu Jan 22 2009 Michael Shigorin <mike@altlinux.org> 2.5.4-alt0.M41.2
- added ICQ-related patch referenced at http://developer.pidgin.im/ticket/8198
- spec cleanup

* Thu Jan 15 2009 Michael Shigorin <mike@altlinux.org> 2.5.4-alt0.M41.1
- 2.5.4 built for M41
- patch0 updated from Sisyphus' 2.5.3-alt1

* Mon Dec 01 2008 Vladimir Scherbaev <vladimir@altlinux.org> 2.5.1-alt2.M41.1
- Backport to Desktop 4.1
- 2.5.1

* Tue Nov 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt2
- rebuild with new evolution-data-server

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Fri Aug 22 2008 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt2
- change requires %_datadir/ca-certificates to package ca-certificates(16816)

* Tue Aug 19 2008 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- build --with-system-ssl-certs=%_datadir/ca-certificates

* Wed Jul 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3
- disable gnutls, enable nss(#15810)
- add default system prefs.xml
- Add debian patch to re-read resolv.conf when connecting to a server

* Thu May 22 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- fix charset in status userinfo (#15384)
- add more options for configure

* Wed Apr 23 2008 Igor Zubkov <icesik@altlinux.org> 2.4.1-alt3
- build with external libgadu

* Sun Apr 20 2008 Igor Zubkov <icesik@altlinux.org> 2.4.1-alt2
- move release notification plugin to separate package (closes #15379)

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1.1
- fix autotools (thanks to Igor Zubkov <icesik at altlinux.org> - patch1)
- update BuildPreReq

* Wed Mar 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0
- update patch for linking

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.3.1-alt1.1
- Rebuilt with python-2.5.

* Mon Dec 10 2007 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Thu Dec 06 2007 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sat Oct 27 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- 2.2.2
- move dbus client utiles(exec scripts and lib) from libpurple to libpurple-dbus
- must fix #13026 with new rpm-build-python find requires

* Wed Oct 10 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Sep 17 2007 Igor Zubkov <icesik@altlinux.org> 2.2.0-alt1
- 2.1.1 -> 2.2.0

* Mon Aug 27 2007 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1.1
- rebuild with new evolution-data-server-1.10.3.1

* Sat Aug 25 2007 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1
- move sounds from pidgin to purple package
- more fine use icons in %%files

* Sat Aug 18 2007 Igor Zubkov <icesik@altlinux.org> 2.1.0-alt2
- NMU:
  + add packager tag
  + remove packages-info-i18n-common from buildrequires
  + fix plugins linking

* Mon Aug 13 2007 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0
- mini fix spec in %%files

* Thu Jun 21 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Thu May 10 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt9
- fix spec

* Mon May 07 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt8
- 2.0.0 release
- rename gaim -> pidgin
- rename libgaim -> libpurple
- rename gaim-test -> finch
- drop all patches

* Sat Mar 31 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt7.beta6
- add PreReq: GConf (#11166)

* Tue Feb 27 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt6.beta6
- fix library path provides
- drop gaim-text (move files to gaim)
- drop gaim-text-devel (move header files to gaim-devel)
- add patches from debian (6,102.103,111)

* Mon Feb 05 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt5.beta6
- 2.0.0beta6
- remove patch for perl

* Mon Dec 25 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt4.beta5
- rebuild with new dbus

* Thu Nov 30 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt3.beta5
- no build plugins: perl, tk/tcl, mono
- disable support libnss/libnspr, cyrus-sasl
- fix spec

* Wed Nov 15 2006 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt2.beta5
-  2.0.0beta5

* Mon Dec 19 2005 Vital Khilko <vk@altlinux.ru> 2.0.0beta1-alt1
- new version

* Thu Dec 08 2005 Vital Khilko <vk@altlinux.ru> 1.5.0-alt2
- #8215

* Fri Aug 12 2005 Vital Khilko <vk@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Jul 11 2005 Vital Khilko <vk@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Jun 21 2005 Vital Khilko <vk@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon May 16 2005 Vital Khilko <vk@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Apr 04 2005 Vital Khilko <vk@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Mar 22 2005 Vital Khilko <vk@altlinux.ru> 1.2.0-alt1
- 1.2.0
- gevolution plugin moved to separate package
- added Perl support

* Wed Mar 02 2005 Vital Khilko <vk@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Feb 22 2005 Vital Khilko <vk@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Feb 01 2005 Vital Khilko <vk@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Jan 20 2005 Vital Khilko <vk@altlinux.ru> 1.1.1-alt1
- 1.1.1
- xosd plugin moved to separate package
- added package independent smileys themes support

* Mon Nov 15 2004 Vital Khilko <vk@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri Nov 05 2004 Vital Khilko <vk@altlinux.ru> 1.0.2-alt2
- Rebuilded with libgnutls

* Mon Oct 25 2004 Vital Khilko <vk@altlinux.ru> 1.0.2-alt1
- new version released
- added belarusian translation

* Mon Sep 20 2004 Vital Khilko <vk@altlinux.ru> 1.0.0-alt1
- new version released

* Mon Aug 30 2004 Vital Khilko <vk@altlinux.ru> 0.82.1-alt1
- new version released

* Wed Aug 11 2004 Vital Khilko <vk@altlinux.ru> 0.81-alt1
- new version released
- include osd plugin

* Wed Jul 21 2004 Vital Khilko <vk@altlinux.ru> 0.80-alt2
- enabled evolution plugin

* Mon Jul 19 2004 Vital Khilko <vk@altlinux.ru> 0.80-alt1
- new version released

* Wed Jun 09 2004 Vital Khilko <vk@altlinux.ru> 0.78-alt2
- oscar protocol patch by Slava Astashonak

* Mon May 31 2004 Vital Khilko <vk@altlinux.ru> 0.78-alt1
- new version released

* Sun Apr 25 2004 Vital Khilko <vk@altlinux.ru> 0.77-alt1
- new version released

* Sun Apr 04 2004 Vital Khilko <vk@altlinux.ru> 0.76-alt1
- new version released

* Tue Mar 16 2004 Vital Khilko <vk@altlinux.ru> 0.75-alt2
- added security patch

* Thu Dec 11 2003 Vital Khilko <vk@altlinux.ru> 0.74-alt1
- new version released
- enabled all features

* Fri Jul 18 2003 Grigory Milev <week@altlinux.ru> 0.65-alt1
- new version released

* Wed Apr 16 2003 Grigory Milev <week@altlinux.ru> 0.61-alt1
- new version released

* Wed Jan 29 2003 Grigory Milev <week@altlinux.ru> 0.59.8-alt2
- added recode plugin

* Wed Jan  8 2003 Grigory Milev <week@altlinux.ru> 0.59.8-alt1
- new version released

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 0.59.1-alt1
- new version (non maintainer build)

* Mon Apr 29 2002 Grigory Milev <week@altlinux.ru> 0.57-alt1
- new version released

* Mon Apr  1 2002 Grigory Milev <week@altlinux.ru> 0.55-alt1
- new version released

* Mon Mar  4 2002 Grigory Milev <week@altlinux.ru> 0.53-alt1
- new version released

* Tue Feb 19 2002 Grigory Milev <week@altlinux.ru> 0.52-alt1
- new version released

* Mon Jan 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.51-alt2
- Updated buildrequires.

* Fri Jan 25 2002 Grigory Milev <week@altlinux.ru> 0.51-alt1
- new version released

* Mon Dec 17 2001 Grigory Milev <week@altlinux.ru> 0.50-alt1
- New version released

* Thu Nov 15 2001 Alexander Bokovoy <ab@altlinux.ru> 0.48-alt2
- 0.48
- wmgaim + recode from Grigory Bakunov (black@asplinux.ru)

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 0.44-alt1
- 0.44

* Wed Jul 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.11.0-alt2
- Rebuilt with new perl.

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 0.11.0-alt1
- 0.11.0 . Rebuilt with perl-5.6.1

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Tue Oct 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10.3-1mdk
- up to 0.10.3

* Tue Sep 26 2000 Daouda Lo <daouda@mandrakesoft.com> 0.9.20-5mdk
- menu title should begin with capital letter.
- ICQ section was replaced by Instant messaging.

* Thu Sep  7 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.20-4mdk
- Adding small and large icons

* Tue Aug 29 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.20-3mdk
- Change icon for menu

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.20-2mdk
- automatically added BuildRequires

* Mon Jul 17 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.20-1mdk
- up to 0.9.20

* Fri Jun 23 2000 Vincent Saugey <vince@mandrakesoft.com> 0.9.19-1mdk
- 0.9.19

* Thu Jun  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.18-1mdk
- 0.9.18
- minor fixes in specfile

* Fri Apr 28 2000 Daouda Lo <daouda@mandrakesoft.com> 0.9.11-3mdk
- add 32*32 icon

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.11-2mdk
- Don't +x the menu entries.

* Fri Mar 31 2000 John Buswell <johnb@mandrakesoft.com> 0.9.11-1mdk
- v0.9.11
- Added menu
- fixed group
- spec-helper

* Wed Nov 03 1999 John Buswell <johnb@mandrakesoft.com>
Build Release

* Tue Nov 02 1999 Lenny Cartier <lenny@mandrakesoft.com>
v0.9.9

* Wed Oct 13 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Specfile adaptations.
