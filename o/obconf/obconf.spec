Name: obconf
Version: 2.0.4
Release: alt3

Summary: Obconf is a configuration tool for the Openbox window manager
License: GPLv2+
Group: Graphical desktop/Other
Url: http://www.icculus.org/openbox/

Source0: %name-%version.tar
Source2: %name.pod

Patch0: %name-%version-alt.patch
Patch1: fix-tab-error.patch

Requires(post,postun): desktop-file-utils
BuildPreReq: desktop-file-utils
Requires(post,postun): shared-mime-info >= 0.15-alt2

BuildPreReq: libopenbox-devel >= 3.5.1
# Automatically added by buildreq on Sat Nov 15 2008 (-bi)
BuildRequires: libglade-devel libstartup-notification-devel
BuildRequires: perl-podlators

%description
%name is a configuration tool for Openbox window manager.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cp %SOURCE2 .

%build
autoreconf -fisv
%configure
%make_build

pod2man --section=1 --release=%version --center "Openbox documentation" obconf.pod > obconf.1

%install
%make_install DESTDIR=%buildroot install

install -pD -m 644 obconf.1 %buildroot%_man1dir/obconf.1

%find_lang %name

%files -f %name.lang
%doc AUTHORS README TODO
%_bindir/%name
%_man1dir/obconf.*
%_datadir/applications/*
%dir %_datadir/%name/
%_datadir/%name/
%_datadir/mime/packages/obconf.xml
%_datadir/mimelnk/application/x-openbox-theme.desktop
%_datadir/pixmaps/obconf.png

%changelog
* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 2.0.4-alt3
- Not require openbox more

* Mon Sep 18 2017 Anton Midyukov <antohami@altlinux.org> 2.0.4-alt2
- Fix --tab error 

* Mon Sep 14 2015 Aleksey Avdeev <solo@altlinux.org> 2.0.4-alt1
- release-2.0.4
- rebuild with new openbox

* Mon Aug 15 2011 Mykola Grechukh <gns@altlinux.ru> 2.0.4-alt0.25gcc7a188
- new version

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt5.2
- NMU: dropped debian menu

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt5.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt5
- apply patch from repocop

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt4
- fix desktop files (thanks to repocop)

* Thu Apr 17 2008 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt3
- rebuild with new openbox

* Thu Apr 10 2008 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt2
- run %%update_desktopdb && %%clean_desktopdb
  after install/uninstall (repocop fix)
- run %%update_mimedb && %%clean_mimedb
  after install/uninstall (repocop fix)

* Thu Feb 21 2008 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt1
- 2.0.2 -> 2.0.3

* Thu Jan 17 2008 Igor Zubkov <icesik@altlinux.org> 2.0.2-alt3
- add manual page from debian

* Wed Nov 14 2007 Igor Zubkov <icesik@altlinux.org> 2.0.2-alt2
- bump release

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 2.0.2-alt1
- 1.6 -> 2.0.2
- update Url
- buildreq

* Fri Mar 17 2006 Igor Zubkov <icesik@altlinux.ru> 1.6-alt1
- 1.6
- buildreq
- update url

* Mon Feb 09 2004 Anton V. Denisov <avd@altlinux.org> 1.5-alt2
- Explicitly use autoconf-2.5 and automake-1.7 for build.

* Wed Jan 21 2004 Anton V. Denisov <avd@altlinux.org> 1.5-alt1
- Initial release for ALT Linux Sisyphus.

