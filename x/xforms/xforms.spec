BuildRequires: chrpath
%def_disable static
%define suff sp1
Name: xforms
Version: 1.0.93
Release: alt5

Summary: A GUI toolkit based on Xlib for the X Window System

Group: Development/Other
License: LGPL-2.1+
#Url: http://world.std.com/~xforms
URL:     http://www.nongnu.org/xforms/

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildConflicts: lib%name

Source: http://download.savannah.nongnu.org/releases/xforms/%name-%version%suff.tar.gz

# manually removed: libxforms-devel 
# Automatically added by buildreq on Sun Feb 05 2006
BuildRequires: gccmakedep imake libX11-devel libXext-devel libXpm-devel libGL-devel libjpeg-devel xorg-cf-files xorg-xproto-devel libICE-devel libXpm-devel libSM-devel
BuildRequires: chrpath

%description
XForms GUI library

%package -n lib%name
Summary: A GUI toolkit based on Xlib for the X Window System
Group: Development/Other
Provides: %name = %version
Obsoletes: %name

%description -n lib%name
XForms features a rich set of objects (like buttons, sliders,
and menus) integrated into an easy and efficient object/event callback
execution model, allowing for fast and easy construction of X applications.
The library is extensible--new objects can easily be created and added.

If you're installing xforms, you may want to also install xforms-devel,
which is a near-WYSIWYG GUI builder which works with XForms.

%package -n lib%name-demos
Group: Development/Other
Summary: XForms demonstration programs
Provides: %name-demos = %version
Obsoletes: %name-demos
Requires: lib%name = %version-%release

%description -n lib%name-demos
Xforms-demos includes the full source code to 50+ demonstration
programs.  If you plan on using XForms and you aren't an expert, you should
download xforms-demos and take a look at them.

%package -n lib%name-devel
Group: Development/Other
Summary: An XForms GUI builder and other development stuff
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: lib%name = %version-%release

%description -n lib%name-devel
Xforms-devel is a near-WYSIWYG GUI builder that can be used to
design your UI and write the corresponding C code for you.  If you are
installing xforms, you may want to also install xforms-devel.  If you want
to install xforms-devel, you must also install xforms.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/Other
Summary: Static Libraries for lib%name
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static Libraries for lib%name
%endif

%prep
%setup -q -n %name-%version%suff

%build
./autogen.sh
%configure \
%if_disabled static
  --disable-static \
%endif
  --enable-optimization="$RPM_OPT_FLAGS"

%make_build X_PRE_LIBS="" XPM_LIB=-lXpm
make -C demos

%install
#make install DESTDIR=$RPM_BUILD_ROOT
# hack around 
make install DESTDIR=$RPM_BUILD_ROOT includedir=%_includedir/xforms

#install additional demo progs
pushd demos
    for i in *
    do
	[ -d $i ] && continue
	[ -x $i ] && install -pm755 $i %buildroot%_bindir
    done
popd

for i in /usr/bin/fd2ps /usr/bin/fdesign %_libdir/libformsGL.so.2.0.0 %_libdir/libflimage.so.2.0.0; do
	chrpath -d $RPM_BUILD_ROOT$i
done

%files -n lib%name
%doc  ChangeLog *README* NEWS COPYING.LIB
%_bindir/fd2ps
%_libdir/*.so.*
%_man1dir/fd2ps.*
%_man5dir/*

%files -n lib%name-demos
%_bindir/*
%exclude %_bindir/iconvert
%exclude %_bindir/fd2ps
%exclude %_bindir/fdesign

%files -n lib%name-devel
%_bindir/fdesign
%_includedir/xforms/*.h
%_libdir/*.so
%_man1dir/fdesign.*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Feb 10 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.93-alt5
- fixed conflict with openimageio-utils (ALT #39670)

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt4
- fixed build

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt3
- chrpath -d'ed

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt2
- autoreconf'ed

* Thu Apr 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt1
- new version

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.90-alt1.1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.90-alt1.1
- NMU (by repocop): the following fixes applied:
 * postun_ldconfig for libxforms
 * post_ldconfig for libxforms

* Wed Aug 30 2006 Igor Vlasenko <viy@altlinux.ru> 1.0.90-alt1
- picked up from orphaned;
- new version

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- NMU: rebuild with new X pathes
- cleanup spec, update build requires, update Source URL
- fix linking flimage with forms
- add packager

* Fri Oct 17 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt1
- final

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt0.2RC5.2
- RC5

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt0.2RC4
- fix paths

* Mon Sep 23 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt0.1RC4
- 1.0 RC4
- spec cleanup
- libification

* Mon Jun 18 2001 AEN <aen@logic.ru> 0.88.1-ipl5mdk
- Requires fixed
* Fri Jun 16 2001 AEN <aen@logic.ru> 0.88.1-ipl4mdk
- Group fixed (bug #24)

* Mon Dec 04 2000 AEN <aen@logic.ru>
- rebuild for 7.2RE

* Tue Nov 9 1999 AEN <aen@logic.ru>
- bzipped man-pages
- built for RE

* Tue Nov 10 1998 Jeff Johnson <jbj@redhat.com>
- Build from (non-distributable) source.

* Thu Oct 06 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file
- built for 5.2

* Thu May 14 1998 Michael Maher <mike@redhat.com>
- inspected package and buildroots.

* Tue Jan 27 1998 Otto Hammersmith <otto@redhat.com>
- fixed fdesign being a directory
- moved fdesign to devel package,
- fixed broken symlink from libforms.so to libforms.so.0.88

* Mon Dec  8 1997 Otto Hammersmith <otto@redhat.com>
- fixed alpha library dependency problems.

* Sun Dec  7 1997 Otto Hammersmith <otto@redhat.com>
- add provides for the .81 libs

* Tue Dec  2 1997 Otto Hammersmith <otto@redhat.com>
- buildrooted

* Wed Nov 19 1997 Otto Hammersmith <otto@redhat.com>
- updated to 0.88

* Tue Apr 8 1997 Michael Fulbright <msf@redhat.com>
Updated package to version 0.86.
