%define _unpackaged_files_terminate_build 1

Name: feh
Version: 3.5
Release: alt1
Summary: Image viewer using Imlib 2
Group: Graphics
License: BSD

Url: https://feh.finalrewind.org/

# git://github.com/derf/feh.git refs/tags/v%%version
Source: %name-%version.tar

# Automatically added by buildreq on Thu Sep 08 2011
# optimized out: imlib2 imlib2-devel libX11-devel xorg-xproto-devel zlib-devel
BuildRequires: libXinerama-devel libXt-devel libcurl-devel libgiblib-devel libpng-devel libexif-devel libjpeg-utils

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slideshow or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%setup

%build
export VERSION="%version"
export CFLAGS="%optflags"
export PREFIX="%_prefix"

%make_build exif=1

%install
export VERSION="%version"
export CFLAGS="%optflags"
export PREFIX="%_prefix"

%makeinstall_std exif=1

%files
%_bindir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%exclude %_datadir/doc/%name

%doc AUTHORS ChangeLog README.md TODO
%doc COPYING

%changelog
* Mon Oct 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5-alt1
- Updated to upstream version 3.5 (Fixes: CVE-2017-7875).

* Thu Jun 16 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.16-alt1
- Updated to 2.16.

* Wed Dec 24 2014 Andrew Clark <andyc@altlinux.org> 2.12-alt4.89256a02
- version update to 2.12-alt4.89256a02

* Sun Oct 19 2014 Andrew Clark <andyc@altlinux.org> 2.12-alt3.a664ddeb
- version update to 2.12-alt3.a664ddeb

* Thu Jun 12 2014 Andrew Clark <andyc@altlinux.org> 2.12-alt2.2b04e7f4
- version update to 2.12-alt2.2b04e7f4

* Sat May 24 2014 Andrew Clark <andyc@altlinux.org> 2.12-alt1.717f2a00
- version update to 2.12-alt1.717f2a00

* Sat Mar 29 2014 Andrew Clark <andyc@altlinux.org> 2.10-alt1
- version update 2.10

* Wed Jan 8 2014 Andrew Clark <andyc@altlinux.org> 2.9.3-alt3.6a5b24b0
- version update 2.9.3-alt3.6a5b24b0

* Mon Nov 4 2013 Andrew Clark <andyc@altlinux.org> 2.9.3-alt2.fa727bc8
- version update 2.9.3-alt2.fa727bc8

* Wed Jul 24 2013 Andrew Clark <andyc@altlinux.org> 2.9.3-alt1
- version update 2.9.3-alt1

* Sun May 26 2013 Andrew Clark <andyc@altlinux.org> 2.9.2-alt1
- version update 2.9.2-alt1

* Sat Apr 13 2013 Andrew Clark <andyc@altlinux.org> 2.9.1-alt1.7fbd8d9f
- version update to 2.9.1-alt1.7fbd8d9f

* Sun Feb 17 2013 Andrew Clark <andyc@altlinux.org> 2.9.1-alt1
- version update to 2.9.1-alt1

* Sun Jan 6 2013 Andrew Clark <andyc@altlinux.org> 2.8-alt1
- version update to 2.8-alt1

* Fri Dec 14 2012 Andrew Clark <andyc@altlinux.org> 2.7-alt1.3f30958d
- version update to 2.7-alt1.3f30958d

* Tue Oct 30 2012 Andrew Clark <andyc@altlinux.org> 2.7-alt1.96d57781
- version update to 2.7-alt1.96d57781

* Thu Oct 4 2012 Andrew Clark <andyc@altlinux.org> 2.6.3-alt1
- version update to 2.6.3-alt1

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.1
- Rebuilt with libpng15

* Sat Sep 1 2012 Andrew Clark <andyc@altlinux.org> 2.6-alt1
- version update to 2.6-alt1

* Mon May 7 2012 Andrew Clark <andyc@altlinux.org> 2.5-alt1.9ed58f2c
- version update to 2.5-alt1.9ed58f2c

* Sun Nov 13 2011 Andrew Clark <andyc@altlinux.org> 2.1-alt1
- version update to 2.1-alt1

* Thu Sep 8 2011 Andrew Clark <andyc@altlinux.org> 1.16-alt1
- version update to 1.16-alt1

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 1.14.1-alt1
- version update to 1.14.1-alt1

* Sun Feb 13 2011 Andrew Clark <andyc@altlinux.org> 1.11.2-alt1
- version update to 1.11.2-alt1

* Fri Jan 7 2011 Andrew Clark <andyc@altlinux.org> 1.10.1-alt1
- version update to 1.10.1-alt1

* Sun Oct 10 2010 Andrew Clark <andyc@altlinux.org> 1.10-alt1
- version update to 1.10-alt1

* Sun Sep 5 2010 Andrew Clark <andyc@altlinux.org> 1.9-alt1
- version update to 1.9-alt1

* Sat Jul 31 2010 Andrew Clark <andyc@altlinux.org> 1.8-alt1
- version update to 1.8-alt1

* Fri Jan 27 2006 Alex Murygin <murygin@altlinux.ru> 1.3.4-alt1
- new version

* Mon Jul 18 2005 Alex Murygin <murygin@altlinux.ru> 1.3.3-alt1
- new version
- changed url

* Wed Feb 09 2005 Alex Murygin <murygin@altlinux.ru> 1.3.0-alt1
- new version

* Thu Dec 16 2004 Alex Murygin <murygin@altlinux.ru> 1.2.9-alt1
- new version

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 1.2.6-alt1
- First build for AltLinux

