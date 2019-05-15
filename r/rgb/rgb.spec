Name: rgb
Version: 1.0.6
Release: alt3
Summary: Uncompile an rgb color
Group: System/X11
Source: %name-%version.tar.gz
License: MIT

BuildRequires: libX11-devel
BuildRequires: xorg-util-macros
Provides: xorg-rgb = %version
Obsoletes: xorg-rgb < %version
Provides: xorg-x11-rgb = %version
Obsoletes: xorg-x11-rgb < %version

%description
The showrgb program reads an rgb color-name database compiled for use with
the dbm database routines and converts it back to source form.

%prep
%setup -n %name-%version

%build
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%_bindir/showrgb
%_datadir/X11/rgb.txt
%_mandir/man1/*

%changelog
* Wed May 15 2019 Fr. Br. George <george@altlinux.ru> 1.0.6-alt3
- Replace xorg-x11-rgb

* Wed May 15 2019 Fr. Br. George <george@altlinux.ru> 1.0.6-alt2
- Replace xorg-rgb

* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.0.6-alt1
- Autobuild version bump to 1.0.6

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:16:07 (27485)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
