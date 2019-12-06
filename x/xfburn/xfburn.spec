Name: xfburn
Version: 0.6.1
Release: alt2.g89c4d68

Summary: CD-R/CD-RW disc writing application
Url: https://goodies.xfce.org/projects/applications/xfburn
License: GPL-2.0+
Packager: Xfce Team <xfce@packages.altlinux.org>
Group: Archiving/Cd burning

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: xfce4-dev-tools rpm-build-xfce4
BuildPreReq: libxfce4ui-gtk3-devel libexo-gtk3-devel
BuildRequires: xsltproc docbook-style-xsl
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel libburn-devel libisofs-devel libgio-devel libgudev-devel

%define _unpackaged_files_terminate_build 1

%description
Xfburn is a simple CD burning tool based on libburn/libisofs.


%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag xfburn_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-gudev \
	--enable-gstreamer \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/stock/media/*
%_desktopdir/*
%_datadir/appdata/*.xml
%_datadir/Thunar/sendto/*.desktop
%_man1dir/*

%changelog
* Fri Nov 29 2019 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt2.g89c4d68
- Updated url.
- Don't use rpm-build-licenses.
- Upstream git snapshot (for translations update).

* Tue Nov 05 2019 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Enabled debug (minimum level).
- Updated to 0.6.1.

* Thu Dec 14 2017 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt1
- Package appdata file.
- Minor spec fixes.
- Updated to 0.5.5.

* Mon May 18 2015 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- Updated to 0.5.4.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt2
- Rebuild with libxfce4util-4.12.

* Thu Apr 10 2014 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2 release.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2
- Updated to 0.5.0 release.

* Fri Dec 20 2013 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20131209
- Drop 'Utility' category from desktop-file.
- Fix Xfce name (XFCE -> Xfce).
- Upstream git snapshot.

* Thu Sep 05 2013 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20130825
- Add GenericName to the desktop file (closes: #29235).
- Updated translations (from upstream git).

* Wed May 08 2013 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20130508
- Drop obsoleted patches.
- Upstream git snapshot.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt3
- Fix build: Add missing header.
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt2
- Patches from upstream's bug tracker (Xfce bug #7355):
    + Port to libxfce4ui.
    + Port to gio/udev, remove HAL support.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Spec update & cleanup.
- Updated to 0.4.3.

* Tue Apr 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.1-alt1
- new version 

* Mon Apr 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt2
- build fixed 

* Mon Jan 12 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Mon Oct 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.3.svn5595-alt1
- new version
- git-svn imported repo

* Thu Mar 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0.svn20080320-alt1
- new version
- fixed build on Sisyphus 

* Wed Jan 16 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0.svn20080117-alt1
- new version
- patch for build with libburn-0.4.0

* Thu Sep 20 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0.svn20070826-alt2
- fixed requires 

* Thu Sep 20 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.0.svn20070826-alt1
- first build 

