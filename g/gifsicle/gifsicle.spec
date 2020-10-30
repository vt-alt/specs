%define _unpackaged_files_terminate_build 1

Name: gifsicle
Version: 1.92
Release: alt1
Summary: command-line program for manipulating GIF images
Group: Graphics
License: GPL-2.0
Url: http://www.lcdf.org/gifsicle

# https://github.com/kohler/gifsicle.git
Source: %name-%version.tar

# Automatically added by buildreq on Tue Mar 27 2007
BuildRequires: libSM-devel libX11-devel

%description
Gifsicle is a powerful command-line program for manipulating GIF image
files.  It has good support for transparency and colormap manipulation,
simple image transformations (cropping, flipping), and creating,
deconstructing, and editing GIF animations. It can also optimize GIF
animations for space. Also included is a GIF animation viewer and a
program that checks whether two GIFs look the same.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/gifdiff
%_man1dir/gifdiff.1.*
%_bindir/gifsicle
%_man1dir/gifsicle.1.*
%_bindir/gifview
%_man1dir/gifview.1.*
%doc README.md NEWS.md

%changelog
* Wed Oct 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.92-alt1
- Updated to upstream version 1.92 (Fixes: CVE-2017-1000421).

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1.88-alt1
- Autobuild version bump to 1.88

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 1.87-alt1
- Autobuild version bump to 1.87

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 1.86-alt1
- Autobuild version bump to 1.86

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 1.84-alt1
- Autobuild version bump to 1.84

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.83-alt1
- Autobuild version bump to 1.83

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 1.82-alt1
- Autobuild version bump to 1.82

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 1.78-alt1
- Autobuild version bump to 1.78

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.71-alt1
- Autobuild version bump to 1.71
- Fix docs

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1.70-alt1
- Autobuild version bump to 1.70

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1.68-alt1
- Autobuild version bump to 1.68

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.67-alt1
- Autobuild version bump to 1.67

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.66-alt1
- Autobuild version bump to 1.66

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 1.64-alt1
- Autobuild version bump to 1.64

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 1.63-alt1
- Autobuild version bump to 1.63

* Tue Mar 27 2007 Alex V. Myltsev <avm@altlinux.ru> 1.48-alt1
- 1.48: bug fix for --crop-transparency.

* Sun Mar 04 2007 Alex V. Myltsev <avm@altlinux.ru> 1.46-alt1
- 1.46: minor scripting features.

* Sun Sep 18 2005 Alex V. Myltsev <avm@altlinux.ru> 1.43-alt1
- Version 1.43: minor bugfixes.

* Tue Jun 14 2005 Alex V. Myltsev <avm@altlinux.ru> 1.42-alt1
- Version 1.42.

* Fri Apr 08 2005 Alex V. Myltsev <avm@altlinux.ru> 1.37-alt1
- Initial build for ALT Linux.

