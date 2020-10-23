%define _unpackaged_files_terminate_build 1

Name: xli
Version: 1.17.0
Release: alt9
Summary: X11 Image Loading Utility
License: MIT
Group: Graphics

Url: http://pantransit.reptiles.org/prog
# had to repackage
# %url/%name-%version.tar.bz2
Source: %name-%version.tar

Patch1: xli-1.17.0-mdk-path.patch
Patch2: xli-1.17.0-alt-includes.patch

# Patches from Debian
Patch10: 040-8-bit_palette_support.patch
Patch11: 050-read_past_bufferend_343718.patch
Patch12: 060-security_fixes.patch
Patch13: 080-fillscreen_forall.patch
Patch14: 090-multiple_images_merge.patch
Patch15: 100-xpm_background.patch
Patch16: 110-arrow_keys.patch
Patch17: 130-zoom_auto_440768.patch
Patch18: 150-fix-x-resource-leak.patch
Patch19: 160-disable-libjpeg-scaling.patch
Patch20: 170-fix-spelling.patch
Patch21: 180-add_GCC_hardening.patch

Provides: xloadimage
Obsoletes: xloadimage

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: gccmakedep imake libX11-devel libXext-devel libjpeg-devel libpng-devel xorg-cf-files

%description
This utility will view several types of images under X11, or load images
onto the X11 root window.
Can view the following image types under X11:
FBM Image, Sun Rasterfile, CMU WM Raster, Portable Bit Map (PBM, PGM,
PPM), Portable Network Graphics (PNG), Faces Project, GIF Image, JFIF
style jpeg Image, Utah RLE Image, Windows, OS/2 RLE Image, Photograph
on CD Image, X Window Dump, Targa Image, McIDAS areafile, G3 FAX Image,
PC Paintbrush Image, GEM Bit Image, MacPaint Image, X Pixmap, X Bitmap.

%prep
%setup
%patch1 -p1
%patch2 -p2
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p2
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
%add_optflags -Werror=implicit-function-declaration
xmkmf -a
%make_build CFLAGS="%optflags"
for i in xli xlito; do
	install -pm644 $i.man $i.1
done
install -pm644 xliguide.man xliguide.5
install -pm644 mit.cpyrght COPYRIGHT

%install
mkdir -p %buildroot{%_x11bindir,%_x11mandir/man{1,5},%_sysconfdir/X11/app-defaults}
%make_install install \
	SYSPATHFILE="%buildroot%_sysconfdir/X11/app-defaults/Xli" \
	BINDIR="%buildroot%_x11bindir"

for n in 1 5; do
	for i in *.$n; do
		install -pm644 "$i" "%buildroot%_x11mandir/man$n/$i"
	done
done

ln -snf xli %buildroot%_x11bindir/xsetbg
ln -snf xli %buildroot%_x11bindir/xview

chmod 644 README*

%files
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%_x11bindir/*
%_x11mandir/man?/*
%doc chkgamma.jpg README* ABOUTGAMMA COPYRIGHT

# TODO:
# - look at 2006-11-10 snapshot?

%changelog
* Thu Oct 22 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.17.0-alt9
- Applied patches from Debian (Fixes: CVE-2005-3178).

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.17.0-alt8.1
- Rebuilt with libpng15

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 1.17.0-alt8
- fixed build (buildreq)

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 1.17.0-alt7
- fixed build (buildreq)
- spec cleanup
- me as a Packager:

* Mon Mar 28 2005 Dmitry V. Levin <ldv@altlinux.org> 1.17.0-alt6
- Applied debian patch (fixes CAN-2005-0638 and CAN-2005-0639).

* Thu Jan 08 2004 Stanislav Ievlev <inger@altlinux.org> 1.17.0-alt5
- rebuild with gcc3.3

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.17.0-alt4
- rebuild with gcc3

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.17.0-alt3
- fixed build

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.17.0-alt2
- Rebuilt with libpng.so.3

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.17.0-alt1
- ALT adaptions.

* Tue Aug 28 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.17.0-3mdk
- patch to fix buffer overflow

* Thu Jul 12 2001 Stefan van der Eijk <stefan@eijk.nu> 1.17.0-2mdk
- BuildRequires:	libjpeg-devel
- Removed BuildRequires:	zlib-devel

* Mon Feb  5 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.17.0-1mdk
- Get compile with last glibc.
- 1.17.0.

* Thu Aug 31 2000 Florin Grad <florin@mandrakesoft.com> 1.16-7mdk
- removed the png from the description according to the README file

* Wed Aug 30 2000 Florin Grad <florin@mandrakesoft.com> 1.16-6mdk- removed the png from the description according to the README file
- fixed the strange permissions of the source files

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.16-5mdk
- automatically added BuildRequires

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16-4mdk
- Add Obsoletes: Provides: xloadimage.

* Mon Mar 20 2000 Camille Begnis <camille@mandrakesoft.com> 1.16-3mdk
- Fixed group
- fixed bad symlinks

* Sat Mar 18 2000 Camille Begnis <camille@mandrakesoft.com> 1.16-2mdk
- let spec-helper do its job

* Sat Feb  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16-1mdk
- Apply debian patchs.
- First packaging.

# end of file
