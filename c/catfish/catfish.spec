Name: catfish
Version: 1.4.7
Release: alt1
Summary: A handy file search tool

Group: File tools
License: GPLv2+
Url: http://www.twotoasts.de/index.php/catfish/
Source: %name-%version.tar.gz
BuildArch: noarch

##BuildRequires: intltool python-module-PyXML python-module-distutils-extra python-module-pexpect python-module-zeitgeist2.0 python3-dev
# Automatically added by buildreq on Mon Jun 10 2019
# optimized out: at-spi2-atk fontconfig gobject-introspection gobject-introspection-x11 libat-spi2-core libatk-gir libcairo-gobject libgdk-pixbuf libgdk-pixbuf-gir libgpg-error libgtk+3-gir libpango-gir libwayland-client libwayland-cursor libwayland-egl perl perl-Encode perl-XML-Parser perl-parent python-base python-modules python3 python3-base python3-module-dbus python3-module-ptyprocess python3-module-pygobject3 sh4
BuildRequires: intltool python3-dev python3-module-distutils-extra python3-module-pexpect python3-module-zeitgeist2.0

# search engine
Requires: %_bindir/locate
Requires: %_bindir/find
Requires: python3-module-catfish

%description
A handy file search tool using different backends which is
configurable via the command line.

This program acts as a frontend for different file search engines.
The interface is intentionally lightweight and simple. But it takes
configuration options from the command line.

%package -n python3-module-catfish
Group: Development/Python3
License: GPLv2+
Summary: Supplemental module for catfish

%description -n python3-module-catfish
Supplemental Python3 module for catfish, a handy file search tool

%prep
%setup -n %name-%version

%build
%python3_build

%install

# XXX upstream cant' handle this :)
install -D build/share/applications/*.desktop %buildroot/%_desktopdir/org.xfce.Catfish.desktop

%python3_install

cp -a build/mo %buildroot%_datadir/locale
rm -rf %buildroot%_defaultdocdir/%name

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING README

%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name
%_datadir/metainfo/*
%_datadir/icons/hicolor/scalable/apps/*.svg
%_man1dir/*

%files -n python3-module-catfish
%python3_sitelibdir_noarch/*

%changelog
* Mon Jun 10 2019 Fr. Br. George <george@altlinux.ru> 1.4.7-alt1
- Autobuild version bump to 1.4.7 (Closes: #36594)
- Switch to Python3

* Thu Feb 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.4-alt1
- Updated to upstream version 1.4.4.

* Thu Nov 17 2016 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Autobuild version bump to 1.4.2
- Separate supplemental module

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Autobuild version bump to 1.2.2

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Wed Apr 16 2014 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Thu Oct 10 2013 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Autobuild version bump to 0.8.2
- Mass upstream version update
- Catch icon_not_found exception again

* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 0.3.2-alt3
- Catch icon_not_found exception (Closes: 26027)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 0.3.2-alt2
- Add requirement python-module-pygtk-libglade (closes: 25231)

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.1
- Rebuilt with python 2.6

* Mon Jun 01 2009 Fr. Br. George <george@altlinux.ru> 0.3.2-alt1
- Initial build from FC

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.2-2
- GTK icon cache updating script update

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com>
- Rebuild for Python 2.6

* Tue Oct 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3.2-1
- 0.3.2

* Thu Oct 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-1
- 0.3

* Fri Oct  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.3.c
- Remove beagle dependency for now because beagle is not
  available on ppc64 (although catfish itself is noarch :( )

* Wed Oct  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.2.c
- License update
- Create sub-metapackage to install all supported search engines
- Remove redhat-artwork dependency

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.c
- 0.3c

* Tue May 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.b
- 0.3b

* Wed Apr  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.3-0.1.a
- 0.3a

* Wed Feb 28 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2.2-1
- 0.2.2

* Sun Feb 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2.1-1
- 0.2.1

* Wed Feb 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2stable-1
- 0.2

* Tue Jan 30 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2d-1
- 0.2d

* Mon Jan 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2c-1
- 0.2c

* Sun Jan 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2b-1
- Upstream rename: search4files -> catfish
- Remove the dependencies for beagle, nautilus,
  replace with redhat-artwork

* Mon Jan  1 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.2a-1
- 0.2a

* Sat Dec 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Require pyxdg again (fc7)

* Wed Dec 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1e-1
- 0.1e

* Thu Dec 14 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1d-1
- 0.1d
- Disable pyxdg support on devel for now.

* Sat Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1c-2
- Fix type typo

* Fri Dec  8 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.1c-1
- Initial packaging to import to Fedora Extras.
