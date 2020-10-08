Name: nip2
Version: 8.7.1
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: An image processing system

License: GPLv2+
Group: Graphics
Url: https://github.com/libvips/nip2

# Source-url: https://github.com/libvips/nip2/archive/v%version.tar.gz
Source: %name-%version.tar

Requires: vips >= 8
Provides: nip = %version
Obsoletes: nip <= 7.8.11

# Automatically added by buildreq on Fri Aug 13 2010
BuildRequires: desktop-file-utils flex libgsl-devel libgtk+2-devel libvips-devel libxml2-devel xdg-utils
BuildRequires: gcc-c++

%description
nip2 is an image processing system. It is good for very large
images (ie. larger than the amount of RAM in your machine), and
for working with colour. In use it's rather like a spreadsheet.
There's complete documentaion.

%package doc
Summary: Documentation for %name
Group: Graphics
BuildArch: noarch

%description doc
Documentation for %name.

%prep
%setup

%build
glib-gettextize --force --copy > /dev/null
%autoreconf

%configure
%make_build

%install
%makeinstall_std

# copy the formatted PS and HTML docs into the install area
#cp -a doc/html doc/pdf %buildroot%_docdir/%name/

%files
%_bindir/nip2
%_man1dir/*
%_datadir/nip2/
%_desktopdir/*.desktop
#_niconsdir/*
%_datadir/mime/packages/nip2.xml
%_datadir/mime/image/x-vips.xml
%_datadir/appdata/*.appdata.xml

#files doc
#_docdir/%name

# TODO:
# - look into uninstalled /usr/share/mime/*

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 8.7.1-alt1
- NMU: new version 8.7.1 (with rpmrb script)
- rebuild with new libvips 8

* Sat Sep 24 2016 Michael Shigorin <mike@altlinux.org> 8.4.0-alt1
- new version (watch file uupdate)

* Fri May 20 2016 Michael Shigorin <mike@altlinux.org> 8.3.0-alt1
- new version (watch file uupdate)

* Mon Jan 11 2016 Michael Shigorin <mike@altlinux.org> 8.2-alt1
- new version (watch file uupdate)
  + NB: no more run-nip2.sh

* Wed May 06 2015 Michael Shigorin <mike@altlinux.org> 8.0-alt2
- rebuilt against libvips-8.0.2

* Mon May 04 2015 Michael Shigorin <mike@altlinux.org> 8.0-alt1
- new version (watch file uupdate)

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 7.42.1-alt1
- new version (watch file uupdate)

* Thu Aug 28 2014 Michael Shigorin <mike@altlinux.org> 7.40.4-alt1
- new version (watch file uupdate)

* Thu Jul 17 2014 Michael Shigorin <mike@altlinux.org> 7.40.3-alt1
- new version (watch file uupdate)

* Fri Jul 04 2014 Michael Shigorin <mike@altlinux.org> 7.40.2-alt1
- new version (watch file uupdate)

* Wed Jun 25 2014 Michael Shigorin <mike@altlinux.org> 7.40.1-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 7.38.4-alt1
- new version (watch file uupdate)

* Thu Jun 19 2014 Michael Shigorin <mike@altlinux.org> 7.38.3-alt1
- new version (watch file uupdate)

* Mon Jan 20 2014 Michael Shigorin <mike@altlinux.org> 7.38.1-alt1
- new version (watch file uupdate)

* Sun Dec 22 2013 Michael Shigorin <mike@altlinux.org> 7.36.5-alt1
- new version (watch file uupdate)

* Tue Nov 12 2013 Michael Shigorin <mike@altlinux.org> 7.36.4-alt1
- new version (watch file uupdate)
- disabled autoreconf (breaks with new and shiny autocrap)

* Thu Oct 24 2013 Michael Shigorin <mike@altlinux.org> 7.36.2-alt1
- new version (watch file uupdate)

* Sun Oct 13 2013 Michael Shigorin <mike@altlinux.org> 7.36.1-alt1
- new version (watch file uupdate)

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 7.34.1-alt1
- new version (watch file uupdate)

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 7.32.1-alt1
- new version (watch file uupdate)

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 7.30.2-alt1
- new version (watch file uupdate)
- dropped gentoo patch

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 7.30.1-alt1.1
- adapted gentoo patch to fix FTBFS (https://bugs.gentoo.org/437446)

* Mon Sep 17 2012 Michael Shigorin <mike@altlinux.org> 7.30.1-alt1
- new version (watch file uupdate)

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 7.30.0-alt1
- new version (watch file uupdate)

* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.5-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 7.28.4-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 7.28.3-alt1
- 7.28.3

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 7.26.4-alt1
- 7.26.4
- drop RPATH

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 7.26.3-alt1
- 7.26.3 (thx fedorawatch)

* Mon Apr 04 2011 Michael Shigorin <mike@altlinux.org> 7.24.1-alt2
- don't include mimeinfo.cache
- amended BR:

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 7.24.1-alt1
- 7.24.1 (thanks force@)

* Sat Oct 16 2010 Michael Shigorin <mike@altlinux.org> 7.22.3-alt1
- 7.22.3
- minor spec cleanup

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 7.22.2-alt1
- 7.22.2

* Thu Dec 03 2009 Victor Forsyuk <force@altlinux.org> 7.20.6-alt1
- 7.20.6

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 7.18.2-alt1
- 7.18.2

* Mon Mar 23 2009 Michael Shigorin <mike@altlinux.org> 7.16.4-alt2
- applied repocop patch

* Sat Mar 21 2009 Michael Shigorin <mike@altlinux.org> 7.16.4-alt1
- 7.16.4
- autoreconf

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt3
- added Packager:
- require libified vips
- minor spec cleanup

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt2
- applied repocop patch

* Mon Nov 17 2008 Michael Shigorin <mike@altlinux.org> 7.16.3-alt1
- 7.16.3

* Tue Oct 07 2008 Michael Shigorin <mike@altlinux.org> 7.16.2-alt1
- 7.16.2
- fixed build (buildreq)
- renamed package to nip2
- spec cleanup
- replaced debian menufile with desktop file
- NB: the package seeks proper maintainer

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 7.8.11-alt2.1
- Rebuilt with libtiff.so.4.

* Tue Nov 04 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.11-alt2
- cleanup spec

* Mon Sep 15 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.11-alt1
- new version

* Fri May 09 2003 Anatoly Yakushin <jaa@altlinux.ru> 7.8.7-alt1
- adapted for Sisyphus, create menu and icon.

* Mon Feb 3 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-2
- hack to change default install prefix to /usr/local

* Thu Jan 30 2003 John Cupitt <john.cupitt@ng-london.org.uk> 7.8.6-1
- first stab at an rpm package for nip
