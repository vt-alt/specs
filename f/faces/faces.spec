Name: faces
Version: 1.7.7
Release: alt7

Summary: A list monitor with a visual output
License: LGPL
Group: Networking/Mail
Url: http://www.cs.indiana.edu/ftp/faces/

Source: ftp://ftp.cs.indiana.edu/pub/%name/%name/%name-%version.tar.bz2
Patch: faces-1.7.7-fix-build-with-gettext-0.20.patch

BuildRequires: libgtk+2-devel libICE-devel

%package xface
Summary: Utilities needed by mailers for handling Faces' X-face images
Group: Networking/Mail

%package -n libcompface
Summary: The Faces program's library
Group: System/Libraries

%package -n libcompface-devel
Summary: The Faces program's library and header files
Group: Development/C
Requires: libcompface = %version-%release

# {{{ descriptions
%description
Faces is a program for visually monitoring a list (typically a list of
incoming mail messages, a list of jobs in a print queue or a list of
system users).  Faces operates in five different modes: monitoring for
new mail, monitoring an entire mail file, monitoring a specified print
queue, monitoring users on a machine and custom monitoring.  Faces also
includes a utility for including a face image (a compressed, scanned
image) with mail messages.  The image has to be compressed in a certain
way, which can then be uncompressed and displayed on-the-fly in the mail
program.  This feature of %name is typically used with the exmh mail
handling system.

Install %name if you'd like to use its list monitoring capability or
its face image inclusion capability.  If you would like to include
face images in email, you'll also need to install the %name-xface
package.  If you would like to develop xface applications, you'll need
to also install %name-devel.

%description xface
Faces-xface includes the utilities that mail user agent programs need to
handle X-Face mail headers.  When an email program reads the X-face
header line in an email message, it calls these utilities to display
the face image included in the message.

You'll need to install %name-xface if you want your mail program to
display Faces' X-face images.

%description -n libcompface
%name shared library

%description -n libcompface-devel
libcompface-devel contains the %name program development environment,
(i.e., the static libraries and header files).

# }}}

%prep
%setup
%patch -p1
touch config.rpath
sed -i 's|@GT_NO@||g' */Makefile.in
sed -i 's|@GT_YES@|#NO#|g' */Makefile.in

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 faces.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m644 faces.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/compface
%_bindir/uncompface
%_man1dir/compface.1.*
%_man1dir/uncompface.1.*

%files xface
%_bindir/%name
%_man1dir/%name.1.*
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm

%files -n libcompface
%_libdir/*.so.*

%files -n libcompface-devel
%_libdir/*.so
%_includedir/*
%_man3dir/compface.3.*

%changelog
* Tue May 05 2020 Anton Midyukov <antohami@altlinux.org> 1.7.7-alt7
- Fix build with gettext >= 0.20.0

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.7-alt6.2
- NMU: added URL (closes: #34652)

* Wed Nov 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.7-alt6.1
- Fixed build

* Mon May 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.7-alt6
- explicitly link faces binary with libX11

* Sun Jan 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.7-alt5
- move pixmap from deprecated location

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.7-alt4
- obsolete by filetriggers macros removed

* Thu Dec 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.7-alt3
- fix build with automake >= 1.10

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.7-alt1
- 1.7.7, big sync with PLD

* Fri Sep 27 2002 Rider <rider@altlinux.ru> 1.6.1-ipl15mdk
- Rebuild

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 1.6.1-ipl14mdk
- Rebuilt in environment with sendmail-common installed.

* Wed Jan 03 2001 AEN <aen@logic.ru>
- adopted for RE

* Wed Aug 09 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.6.1-12mdk
- rebuild for the macors  Stefan: the patch failed to apply ...

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.6.1-11mdk
- automatically added BuildRequires

* Sun Apr 02 2000 Jerome Martin <jerome@mandrakesoft.com> 1.6.1-10mdk
- add mini icon for menus
- add menu entries
- fix rpm group
- specfile cleanup (permissions and spec-helper stuff)

* Tue Nov  9 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- fix ikon2xbm problem (r).

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Thu Apr 08 1999 Preston Brown <pbrown@redhat.com>
- fix xbm2ikon problem (bug # 1060).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 14)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- faces-devel moved to Development/Libraries

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- changed netpbm requirement to libgr-progs requirement

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

