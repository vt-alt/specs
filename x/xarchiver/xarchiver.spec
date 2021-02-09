Name: xarchiver
Version: 0.5.4.17
Release: alt1

Summary: A GTK+2 only archive manager
License: %gpl2plus
Group: File tools

Url: http://xarchiver.sourceforge.net/
Source: %name-%version.tar.gz
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses rpm-build-xfce4 xfce4-dev-tools
# Automatically added by buildreq on Thu Dec 19 2019
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config intltool libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libharfbuzz-devel libpango-devel perl perl-Encode perl-parent pkg-config python-modules python2-base sh4 xml-common xml-utils
BuildRequires: glibc-devel-static libgtk+2-devel xsltproc libzstd-devel

%description
Xarchiver is a lightweight GTK2 only frontend for manipulating 7z, arj,
bzip2, gzip, iso, rar, lha, tar, zip, RPM and deb files. It allows you
to create archives and add, extract, and delete files from them.
Password protected archives in the arj, 7z, rar, and zip formats are
supported.

%prep
%setup

%build
touch AUTHORS NEWS # XXX

%xfce4reconf
%configure \
    -enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*.desktop
%dir %_datadir/pixmaps/%name
%_datadir/pixmaps/%name/*.png
%_libexecdir/thunar-archive-plugin/xarchiver.tap
%_iconsdir/*/*/*/*
%_man1dir/*
%doc %_docdir/%name

%changelog
* Thu Jan 28 2021 Fr. Br. George <george@altlinux.ru> 0.5.4.17-alt1
- Autobuild version bump to 0.5.4.17

* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 0.5.4.14.0.35.g47ca4c0-alt1
- Update to git g47ca4c0 (zstd support)

* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 0.5.4.14-alt1
- Autobuild version bump to 0.5.4.14

* Tue Jul 26 2016 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt2
- Fix detection of a tar program (closes: #32303).
- Fix crash when cancelling progress bar.

* Thu Oct 02 2014 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- Patches from Debian:
  + Detect encrypted 7z archives.
  + Fix desktop file.
- Drop obsoleted patch.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.5.4.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt2
- Added patch from Fedora.
- Spec updated, sources: bz2.tar -> tar.
- Fix License.
- Description updated (from Fedora spec).
- Spec cleanup.
- Remove outdated russian documentation.

* Mon Dec 01 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.2-alt1
- new version
- drop outdated russian documentation

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.6-alt3.1
- update buildrequires (tnx viy@ and repocop)

* Wed Apr 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.6-alt3
- Register desktop mime entry (tnx viy@ and repocop)

* Tue Apr 08 2008 Andrey Cherepanov <cas@altlinux.org> 0.4.6-alt2
- fix Russian translation
- fix desktop file
- add Russian documentation
- open localized documentation (if exist)

* Mon Nov 27 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.6-alt1
- new version 0.4.6

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- Xfce 4.4rc2

* Thu Sep 07 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sun Jan 15 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Dec 21 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3-alt1
- 0.3

* Fri Nov 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.2.1-alt2
- add russian translation

* Tue Jul 05 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.2.1-alt1
- build for ALT Linux
