%def_with vv
%def_with krb5
%def_enable purple
%def_enable telepathy

Name: pidgin-sipe
Version: 1.25.0
Release: alt1
Summary: Pidgin plugin for connecting to MS Communications Server

Group: Networking/Instant messaging
License: GPLv2+
Url: http://sipe.sourceforge.net/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: %name-%version.tar
# Patch1: %name-%version-git_snapshot.patch

Requires: pidgin
Requires: gst-plugins-nice1.0 farstream0.2 gst-plugins-good1.0
Requires: gssntlmssp

BuildRequires: intltool
BuildRequires: pkgconfig(glib-2.0) >= 2.18.0 pkgconfig(gmodule-2.0) pkgconfig(gio-2.0) >= 2.32.0
BuildRequires: pkgconfig(gmime-3.0) >= 3.0.0
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(purple) >= 2.8.0
BuildRequires: flex
%{?_with_vv:BuildRequires: pkgconfig(nice) >= 0.1.0 pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-rtp-1.0) pkgconfig(farstream-0.2)}
%{?_with_krb5:BuildRequires: libkrb5-devel gssntlmssp-devel}
%{?_enable_telepathy:BuildRequires: pkgconfig(dbus-glib-1) pkgconfig(telepathy-glib) >= 0.18.0 pkgconfig(gobject-2.0)}
BuildRequires: pkgconfig(dbus-1)

%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

%package -n telepathy-sipe
Summary: Telepathy connection manager to connect to MS Office Communicator
Group: Networking/Instant messaging
Requires: gssntlmssp
Requires: gst-plugins-nice1.0

%description -n telepathy-sipe
A Telepathy connection manager that implements the extended version of
SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)

This package provides the protocol support for Telepathy clients.

%prep
%setup -q
# %patch1 -p1

%build
%autoreconf
%configure \
	--disable-quality-check \
	--disable-static \
	%{subst_enable purple} \
	%{subst_enable telepathy} \
	%{subst_with vv} \
	%{subst_with krb5}

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/purple-2/*.la
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/purple-2/libsipe.so
%_pixmapsdir/pidgin/protocols/*/sipe.*
%_datadir/metainfo/%name.metainfo.xml

%files -n telepathy-sipe
%_libexecdir/telepathy-sipe
%_datadir/dbus-1/services/*.service
%_datadir/empathy/icons/hicolor/*/apps/im-sipe.*
%_datadir/telepathy/profiles/sipe.profile

%changelog
* Mon Feb 24 2020 Nikita Nikiforov <rav263@altlinux.org> 1.25.0-alt1
- 1.25.0

* Tue Apr 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.24.0-alt1
- 1.24.0

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 1.23.3-alt1
- 1.23.3

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.23.0-alt1
- 1.23.0

* Mon Mar 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.22.0-alt1
- 1.22.0

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.21.1-alt1
- 1.21.1

* Wed Feb 10 2016 Alexey Shabalin <shaba@altlinux.ru> 1.20.1-alt1
- 1.20.1

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.19.1-alt1
- 1.19.1

* Mon Jan 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.18.5-alt1
- 1.18.5

* Thu Nov 13 2014 Alexey Shabalin <shaba@altlinux.ru> 1.18.4-alt1
- 1.18.4

* Thu Aug 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.18.3-alt1
- 1.18.3

* Mon Jun 16 2014 Alexey Shabalin <shaba@altlinux.ru> 1.18.2-alt1
- 1.18.2

* Thu May 23 2013 Alexey Shabalin <shaba@altlinux.ru> 1.15.1-alt1
- 1.15.1

* Fri Apr 05 2013 Alexey Shabalin <shaba@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Tue Mar 05 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.1-alt1
- 1.14.1
- build with telepathy support

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 1.13.2-alt1
- 1.13.2

* Fri May 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1.13.1-alt1
- 1.13.1

* Wed Mar 21 2012 Alexey Shabalin <shaba@altlinux.ru> 1.13.0-alt1
- 1.13.0

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt2.bc511e4
- git snapshot bc511e4d34c71a5025f3b884ae803bb5356deff9

* Mon Aug 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Wed Jun 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.11.2-alt2
- upstream snapshot ac3d61915fe3976502718baf40ca3ef72b7f7642
- build without voice and video support

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.11.2-alt1
- 1.11.2

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- stable 1.10.1
- build without voice and video support

* Wed May 26 2010 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt2.git_dcc66501
- git snapshot dcc665015b63e9c77de6573c63fa747d59ef968a (pre 1.11.0)
- build with voice and video support

* Mon Apr 19 2010 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1.git15372
- 1.9.0
- git snapshot 1537295681eaf3457716ab2ae9cae04a44b25a9e

* Thu Feb 11 2010 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1.git5a9509
- 1.8.0 + git snaphot 20100211

* Thu Dec 24 2009 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- Initial packaging
