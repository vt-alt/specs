Name: xorg-proto-devel
Version: 2021.4
Release: alt1
Summary: X.Org combined protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-dri2proto-devel
Provides: xorg-dri3proto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel
Provides: xorg-inputproto-devel xorg-kbproto-devel xorg-presentproto-devel xorg-randrproto-devel
Provides: xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel
Provides: xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel
Provides: xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel

Obsoletes: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-dri2proto-devel
Obsoletes: xorg-dri3proto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel
Obsoletes: xorg-inputproto-devel xorg-kbproto-devel xorg-presentproto-devel xorg-randrproto-devel
Obsoletes: xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel
Obsoletes: xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel
Obsoletes: xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: fop xmlto xsltproc xorg-sgml-doctools xorg-util-macros

%description
X.Org combined protocol headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--host= \
	--build= \
	--disable-specs

%install
%make DESTDIR=%buildroot install

%files
%_docdir/xorgproto
%_includedir/*
%_datadir/pkgconfig/*.pc

%changelog
* Wed May 19 2021 Valery Inozemtsev <shrek@altlinux.ru> 2021.4-alt1
- 2021.4

* Wed Apr 22 2020 Valery Inozemtsev <shrek@altlinux.ru> 2020.1-alt1
- 2020.1

* Fri Jun 21 2019 Valery Inozemtsev <shrek@altlinux.ru> 2019.1-alt1
- 2019.1

* Wed May 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 2018.4-alt3
- fixed provides/obsoletes

* Tue May 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 2018.4-alt2
- fixed provides/obsoletes

* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 2018.4-alt1
- initial build

