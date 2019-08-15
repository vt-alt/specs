Summary:	Netscape Portable Runtime (NSPR)
Name:		nspr
Version:	4.21
Release:	alt2
Epoch:		1
License:	MPL/GPL/LGPL
Group:		System/Libraries
Url:		http://www.mozilla.org/projects/nspr/
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar
Source1:	%name.pc.in

# Automatically added by buildreq on Wed Feb 13 2008 (-bi)
BuildRequires: gcc-c++

%description
Netscape Portable Runtime (NSPR) provides a platform-neutral API for system level and libc like functions. 
The API is used in the Mozilla client, many of Netscape/AOL/iPlanet's and other software offerings.

%package -n lib%name
Summary:        Netscape Portable Runtime (NSPR)
Group:          System/Libraries
Provides:	%name = %version-%release

%description -n lib%name
Netscape Portable Runtime (NSPR) provides a platform-neutral API for system level and libc like functions. 
The API is used in the Mozilla client, many of Netscape/AOL/iPlanet's and other software offerings.

%package -n lib%name-devel
Summary: NSPR development kit
Group: Development/C
Requires: lib%name = %epoch:%version-%release
Provides: %name-devel = %version-%release

%description -n lib%name-devel
NSPR development kit

%package -n lib%name-devel-static
Summary: NSPR static libraries
Group: Development/C
Requires: lib%name-devel = %epoch:%version-%release
Provides: %name-devel-static = %version-%release

%description -n lib%name-devel-static
NSPR development kit (static libs)

%prep
%setup -q

sed -i \
	-e 's@AC_CONFIG_AUX_DIR(\${srcdir}/build/autoconf)@AC_CONFIG_AUX_DIR(build/autoconf)@' \
	nspr/configure.in

%build
cd nspr
%add_optflags %optflags_shared
%configure \
	--includedir=%_includedir/%name \
	--with-mozilla \
	%{?_is_lp64:--enable-64bit} \
	--enable-optimize="%optflags" \
	--enable-mdupdate \
	--with-pthreads \
	--disable-cplus \
	#

%make_build

%install
cd nspr
%makeinstall install export \
	  includedir=%buildroot/%_includedir/%name

find %buildroot/%_includedir/nspr -type f -name '*.h' -print0 |
    xargs -r0 sed -i -e 's@^\([[:space:]]*#include[[:space:]]\+\)"\([^"]\+\)"@\1<nspr/\2>@g'

%__mkdir_p %buildroot/%_datadir/%name-%version
mv -f %buildroot/%_bindir/prerr.properties %buildroot/%_datadir/%name-%version/

NSPR_LIBS=`%buildroot/%_bindir/nspr-config --libs`
NSPR_CFLAGS=`%buildroot/%_bindir/nspr-config --cflags`
NSPR_VERSION=`%buildroot/%_bindir/nspr-config --version`
%__mkdir_p %buildroot/%_libdir/pkgconfig
sed -e "s,@libdir@,%_libdir,g" \
    -e "s,@prefix@,%_prefix,g" \
    -e "s,@exec_prefix@,%_prefix,g" \
    -e "s,@includedir@,%_includedir/nspr,g" \
    -e "s,@NSPR_VERSION@,$NSPR_VERSION,g" \
    -e "s,@FULL_NSPR_LIBS@,$NSPR_LIBS,g" \
    -e "s,@FULL_NSPR_CFLAGS@,$NSPR_CFLAGS,g" \
	%SOURCE1 > %buildroot/%_libdir/pkgconfig/nspr.pc

%files -n lib%name
%_libdir/*.so*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/nspr
%_libdir/pkgconfig/*
%_datadir/%name-%version
%_datadir/aclocal/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Tue May 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:4.21-alt2
- Use %%_is_lp64 to determine if arch is 64-bit.

* Sun Mar 31 2019 Alexey Gladkov <legion@altlinux.ru> 1:4.21-alt1
- New stable release 4.21.

* Mon Nov 12 2018 Alexey Gladkov <legion@altlinux.ru> 1:4.20-alt1
- New stable release 4.20.

* Wed Mar 21 2018 Alexey Gladkov <legion@altlinux.ru> 1:4.19-alt1
- New stable release 4.19.

* Sun Oct 08 2017 Alexey Gladkov <legion@altlinux.ru> 1:4.17-alt1
- New stable release 4.17.

* Fri Aug 25 2017 Alexey Gladkov <legion@altlinux.ru> 1:4.16-alt1
- New stable release 4.16.

* Tue Jul 11 2017 Alexey Gladkov <legion@altlinux.ru> 1:4.15-alt1
- New stable release 4.15.

* Fri Oct 21 2016 Alexey Gladkov <legion@altlinux.ru> 1:4.13.1-alt1
- New stable release 4.13.1.

* Mon Mar 21 2016 Alexey Gladkov <legion@altlinux.ru> 1:4.12.0-alt1
- New stable release 4.12.

* Fri Feb 12 2016 Alexey Gladkov <legion@altlinux.ru> 1:4.11.0-alt1
- New stable release 4.11.

* Thu Nov 05 2015 Alexey Gladkov <legion@altlinux.ru> 1:4.10.10-alt1
- New stable release 4.10.10.

* Thu Nov 05 2015 Alexey Gladkov <legion@altlinux.ru> 1:4.10.9-alt1
- New stable release 4.10.9.

* Sun Mar 08 2015 Alexey Gladkov <legion@altlinux.ru> 1:4.10.8-alt1
- New stable release 4.10.8.

* Wed Sep 24 2014 Alexey Gladkov <legion@altlinux.ru> 1:4.10.7-alt1
- New stable release 4.10.7.

* Mon Jun 30 2014 Alexey Gladkov <legion@altlinux.ru> 1:4.10.6-alt1
- New stable release 4.10.6.

* Sat May 10 2014 Alexey Gladkov <legion@altlinux.ru> 1:4.10.5-alt1
- New stable release 4.10.5.

* Wed Feb 05 2014 Alexey Gladkov <legion@altlinux.ru> 1:4.10.3-alt1
- New stable release 4.10.3.

* Wed Nov 20 2013 Alexey Gladkov <legion@altlinux.ru> 1:4.10.2-alt1
- New stable release 4.10.2.

* Thu Sep 26 2013 Alexey Gladkov <legion@altlinux.ru> 1:4.10.1-alt1
- New stable release 4.10.1.

* Fri Aug 09 2013 Alexey Gladkov <legion@altlinux.ru> 1:4.10.0-alt1
- New stable release 4.10.

* Wed Apr 10 2013 Alexey Gladkov <legion@altlinux.ru> 1:4.9.6-alt1
- New stable release 4.9.6.

* Mon Feb 18 2013 Alexey Gladkov <legion@altlinux.ru> 1:4.9.5-alt1
- New stable release 4.9.5.

* Fri Jan 11 2013 Alexey Gladkov <legion@altlinux.ru> 1:4.9.4-alt1
- New stable release 4.9.4.

* Tue Aug 28 2012 Alexey Gladkov <legion@altlinux.ru> 1:4.9.2-alt1
- New stable release 4.9.2.

* Wed Apr 18 2012 Alexey Gladkov <legion@altlinux.ru> 1:4.9.0-alt1
- New stable release 4.9.

* Wed Aug 17 2011 Alexey Gladkov <legion@altlinux.ru> 1:4.8.9-alt1
- New stable release 4.8.9.

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 1:4.8.7-alt2
- Renamed Serial to Epoch, fixed interpackage dependencies.
- Built without --enable-strip to enable debuginfo.

* Fri Feb 25 2011 Alexey Gladkov <legion@altlinux.ru> 1:4.8.7-alt1
- New stable release 4.8.7.

* Sun Oct 24 2010 Alexey Gladkov <legion@altlinux.ru> 1:4.8.6-alt1
- New stable release 4.8.6.

* Mon May 31 2010 Alexey Gladkov <legion@altlinux.ru> 1:4.8.5-alt0.20100531
- New cvs snapshot 4.8.5 20100531.

* Sun Mar 28 2010 Alexey Gladkov <legion@altlinux.ru> 1:4.8.4-alt1
- New stable release 4.8.4.

* Mon Nov 09 2009 Alexey Gladkov <legion@altlinux.ru> 1:4.8.2-alt1
- New stable release 4.8.2.
- Fix CVE-2009-1563, CVE-2009-2463 (ALT#22207).

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 1:4.8.0-alt1
- new stable release 4.8.0.

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.3-alt1
- new stable release 4.7.3.

* Sat Jun 28 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080628
- new cvs snapshot 4.7.2 20080628.

* Wed Jun 25 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080625
- new cvs snapshot 4.7.2 20080625.

* Fri May 30 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080530
- new cvs snapshot 4.7.1 20080530.
- Add libnspr-devel-static package.

* Tue May 13 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.2-alt1.20080512
- new cvs snapshot 4.7.1 20080512.
* Fri Mar 21 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.1-alt1.20080321
- new cvs snapshot 4.7.1 20080321.

* Fri Feb 29 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7.1-alt1.20080229
- new cvs snapshot 4.7.1 20080229.

* Sat Feb 02 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7-alt1.20080202
- new cvs snapshot 20080202.

* Thu Jan 10 2008 Alexey Gladkov <legion@altlinux.ru> 1:4.7-alt1.20071127
- new cvs snapshot 20071127.

* Thu Sep 27 2007 Alexey Gladkov <legion@altlinux.ru> 1:4.6.7-alt1
- new stable release 4.6.7.

* Fri Feb 23 2007 Alexey Gladkov <legion@altlinux.ru> 1:4.6.5-alt1
- new stable release 4.6.5.

* Sun Oct 29 2006 Alexey Gladkov <legion@altlinux.ru> 1:4.6.3-alt1
- new stable release 4.6.3.

* Sun Feb 19 2006 Alexey Gladkov <legion@altlinux.ru> 4.7.0.cvs20060807-alt1
- new cvs snapshot 20060807.

* Wed Dec 21 2005 Alexey Gladkov <legion@altlinux.ru> 4.7.0.cvs20051124-alt2
- nspr.pc was added.

* Thu Nov 24 2005 Alexey Gladkov <legion@altlinux.ru> 4.7.0-alt1.cvs20051124
- new cvs snapshot.
- build with --disable-cplus.

* Mon Oct 17 2005 Alexey Gladkov <legion@altlinux.ru> 4.7.0-alt1.cvs
- initial build for ALT Linux.

