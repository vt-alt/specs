
Name: virt-viewer
Version: 9.0
Release: alt1

Summary: Virtual Machine Viewer
Group: System/Configuration/Other
License: GPL-2.0+
Url: https://gitlab.com/virt-viewer/virt-viewer
# Vcs https://gitlab.com/virt-viewer/virt-viewer
Source: %name-%version.tar

Obsoletes: spice-client < 0.12.5-alt3

BuildRequires: glib2-devel >= 2.40 libgio-devel
BuildRequires: libxml2-devel
BuildRequires: libvirt-devel >= 0.9.7 libvirt-glib-devel >= 0.1.8
BuildRequires: libgtk+3-devel >= 3.12
BuildRequires: perl-podlators gettext
BuildRequires: libspice-gtk3-devel >= 0.35 libspice-glib-devel spice-protocol >= 0.12.7
BuildRequires: libgtk3vnc-devel >= 0.4.0
BuildRequires: libvte3-devel
BuildRequires: libgovirt-devel >= 0.3.3 librest-devel >= 0.8
BuildRequires: bash-completion

%description
Virt Viewer provides a graphical viewer for the guest OS
display. At this time is supports guest OS using the VNC
or SPICE protocols. Further protocols may be supported in
the future as user demand dicatates. The viewer can connect
directly to both local and remotely hosted guest OS, optionally
using SSL/TLS encryption.

%prep
%setup

%build
mkdir -p m4
touch ChangeLog AUTHORS
%autoreconf
%configure \
	--disable-static \
	--disable-update-mimedb \
    --with-spice-gtk \
    --with-vte \
	--with-buildid=-%release

%make_build

%install
%make_install install  DESTDIR=%buildroot
%find_lang %name

%files -f %name.lang
%doc README.md COPYING NEWS
%_bindir/*
%_man1dir/*
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_datadir/appdata/remote-viewer.appdata.xml
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/devices/*
%_datadir/bash-completion/completions/virt-viewer

%changelog
* Sat May 09 2020 Alexey Shabalin <shaba@altlinux.org> 9.0-alt1
- new version 9.0

* Tue Apr 23 2019 Pavel Moseev <mars@altlinux.org> 8.0-alt3
- update translation

* Mon Mar 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 8.0-alt2
- Allow toggling clipboard sharing between host and guest.

* Sun Mar 10 2019 Alexey Shabalin <shaba@altlinux.org> 8.0-alt1
- 8.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 7.0-alt2
- app: Remove VirtViewerApp::has-focus
- app: Always add guest name comment

* Fri Jul 27 2018 Alexey Shabalin <shaba@altlinux.org> 7.0-alt1
- 7.0 release

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0-alt0.1
- upstream/master snapshot
- build without spice-controller

* Tue Mar 06 2018 Alexey Shabalin <shaba@altlinux.ru> 6.0-alt1
- 6.0

* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 5.0-alt1
- 5.0

* Mon Jul 04 2016 Alexey Shabalin <shaba@altlinux.ru> 4.0-alt1
- 4.0

* Mon Jun 27 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt2
- rebuild with spice-gtk-0.32-alt1

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt1
- 3.1

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1
- 3.0

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1.1
- rebuild with new libgovirt

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.6-alt1
- 0.5.6
- build with oVirt support

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Nov 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1
- build with gtk+3

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt2
- rebuild with new libspice-gtk-devel

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20110211
- snapshot 20110211

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20110112
- snapshot 20110112

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20101221
- snapshot 20101221
- build with spice support

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.3-alt1
- Initial build for ALTLinux
