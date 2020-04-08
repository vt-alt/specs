
%def_enable static
%def_disable pth
%def_enable info_nogen
%define req_gpgerror_ver 1.11
%define soversion 20

Name: libgcrypt
Version: 1.8.5
Release: alt3

%define soname %{name}%{soversion}

Group: System/Libraries
Summary: The GNU crypto library
License: LGPL
URL: http://www.gnupg.org/

Source: %name-%version.tar

Patch0: libgcrypt-1.8.4-fix-overflow-streebog.patch

# GOST patch
%define vko_ver 2.0.0
%define imit_ver 1.0.0
%define keymeshing_ver 1.0.0
Patch1: libgcrypt-1.8.5-curves-2012.patch
Patch2: libgcrypt-1.8.5-vko-salt.patch
Patch3: libgcrypt-1.8.5-gost89-optimize.patch
Patch4: libgcrypt-1.8.5-gost89-imit.patch
Patch5: libgcrypt-1.8.5-gost89-keymeshing.patch

BuildRequires: libgpg-error-devel >= %req_gpgerror_ver
%if_enabled static
BuildRequires: glibc-devel-static
%endif
%if_enabled pth
BuildRequires: libpth-devel
%endif
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.

%package -n %soname
Summary: The GNU crypto library
Group: System/Libraries
Requires: libgpg-error >= %req_gpgerror_ver
Provides: %name = %version-%release
# GOST provides
Provides: %name(vko) = %vko_ver
Provides: %name(imit) = %imit_ver
Provides: %name(keymeshing) = %keymeshing_ver
%description -n %soname
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.

%package -n %soname-pth
Summary: GNU Crypto library with GNU Pth user-space thread support
Group: System/Libraries
Requires: libgpg-error >= %req_gpgerror_ver
%description -n %soname-pth
This is a portion of Libgcrypt supporting user-space
threads provided by the GNU Pth library.

%package -n gcrypt-utils
Group: Networking/Other
Summary: Utilities for the %name package
Conflicts: %name-devel <= 1.4.2
Provides: %name-utils = %version-%release
Obsoletes: %name-utils < %version-%release
%description -n gcrypt-utils
This package contains %name utilities.

%package devel
Group: Development/Other
Summary: Development files for the %name package
Requires: %soname = %version-%release
Requires: libgpg-error-devel  >= %req_gpgerror_ver
%if_enabled pth
Requires: %soname-pth = %version-%release
%endif
Conflicts: %{name}0-devel
%description devel
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.
This package contains files needed to develop
applications using libgcrypt (e.g. Aegypten project).

%package devel-static
Summary: Static libraries for the %name-devel package
Group: Development/Other
Requires: %name-devel = %version-%release
Requires: libgpg-error-devel-static  >= %req_gpgerror_ver
Conflicts: %{name}0-devel-static
%description devel-static
Static libraries for the %name-devel package


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%if_enabled info_nogen
sed -i "s|^info_TEXINFOS|#info_TEXINFOS|" doc/Makefile.am
sed -i "s|^gcrypt_TEXINFOS|#gcrypt_TEXINFOS|" doc/Makefile.am
%endif

%build
%add_optflags %optflags_shared
%autoreconf

rm -f COPYING.LIB
ln -s %_licensedir/LGPL-2.1 COPYING.LIB

%configure %{subst_enable static} \
    --enable-shared \
    --enable-noexecstack \
    --enable-ld-version-script \
    --enable-random=linux \
    --disable-dev-random

%make_build -C doc ||:
%make_build

%install
%makeinstall

# relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
mv -f %buildroot%_libdir/libgcrypt.so.* %buildroot/%_lib
ln -sf ../../%_lib/libgcrypt.so.%soversion %buildroot%_libdir/libgcrypt.so

%if_enabled info_nogen
mkdir %buildroot/%_infodir/
install -m 0644 doc/*.info %buildroot/%_infodir/
%endif

%check
%ifnarch aarch64
%make check
%endif

%define _unpackaged_files_terminate_build 1

%files -n gcrypt-utils
%_bindir/dumpsexp
%_bindir/hmac256
%_bindir/mpicalc
%_man1dir/hmac256.*

%files -n %soname
/%_lib/%name.so.*
#%_libdir/%name-pthread.so.*
%doc AUTHORS ChangeLog NEWS README THANKS TODO

%if_enabled pth
%files %soname-pth
%_libdir/%name-pth.so.*
%endif

%files devel
%_bindir/*-config
%_includedir/*
%_libdir/*.so
%_datadir/aclocal/*
%_infodir/*
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue Oct 22 2019 Paul Wolneykien <manowar@altlinux.org> 1.8.5-alt3
- Maintenance release.

* Wed Oct 02 2019 Paul Wolneykien <manowar@altlinux.org> 1.8.5-alt2
- CryptoPro key meshing for GOST-28147.
- GOST-28147 IMIT mode (thx Dmitry Eremin-Solenikov).
- GOST-28147 optimizations (thx Dmitry Eremin-Solenikov).
- GOST VKO support in ECDH: multiply by an optional UKM value.
- Added GOST-R.3410-2012 curves.

* Thu Aug 29 2019 Paul Wolneykien <manowar@altlinux.org> 1.8.5-alt1
- Freshed up to version 1.8.5 (fixes CVE-2019-13627).
- Upstream: Improve ECDSA unblinding.
- Upstream: Provide a pkg-config file for libgcrypt.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt3
- NMU: remove rpm-build-ubt from BR:

* Mon May 13 2019 Paul Wolneykien <manowar@altlinux.org> 1.8.4-alt2
- Added patch fixing carry overflow in Stribog 512-bit addition.

* Mon Mar 25 2019 Paul Wolneykien <manowar@altlinux.org> 1.8.4-alt1
- Freshed up to version 1.8.4.

* Tue Dec 18 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.3-alt4
- Flip the UKM buffer relatively to its MPI value.
- Set "1.2.643.2.2.31.1" S-Box for KEK (CEK wrapping/unwrapping).
- More debug in ecc_encrypt_raw: Print out the public key.
- Identify GOST-28147 also by OID 1.2.643.2.2.21.

* Thu Oct 04 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.3-alt3
- Skip check on aarch64.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.3-alt2
- Include the GOST (VKO, MAC/IMIT) patch into the main package version.
- GOST VKO patch version 1.0.0 providing the virtual package.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.3-alt1
- Freshed up to v1.8.3.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2-alt2
- Include v1.7.10 security fix version patch.

* Tue Oct 02 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2-alt5.gost
- Git rid of the %%ubt suffix.
- Restored the original sources.

* Fri Sep 07 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2-alt4.gost
- Fixed changelog version.
- Fixed gear rules.
- GOST VKO patch version 1.0.0 providing the virtual package.

* Fri Sep 07 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2-alt3.gost
- Generate the patch with gear.
- Remove the build-generated files (source package).
- Fixed TAR format.

* Wed Jul 25 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2-alt2.gost
- Build with GOST (VKO, MAC/IMIT) patch.

* Thu Jun 14 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.10-alt1
- new version
- security fixes: CVE-2018-0495

* Thu Apr 19 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2-alt1
- Freshed up to the upstream version 1.8.2.

* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.9-alt2
- clean description (ALT#34383)

* Mon Sep 18 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.9-alt1
- new version
- security fixes: CVE-2017-0379

* Thu Jul 13 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.8-alt1
- new version

* Thu Jul 06 2017 Sergey V Turchin <zerg@altlinux.org> 1.6.6-alt2
- security fixes: CVE-2017-7526

* Thu Aug 18 2016 Sergey V Turchin <zerg@altlinux.org> 1.6.6-alt1
- new version

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 1.6.5-alt1
- new version
- security fixes: CVE-2015-7511

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1.1
- NMU: added BR: texinfo

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 1.6.4-alt1
- new version

* Wed Jun 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3
- rename libgrypt to libgcrypt20
- rename libgcrypt-utils to gcrypt-utils
- relocate shared libraries from %_libdir/ to /%_lib/

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.5.4-alt0.M70P.1
- built for M70P

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.5.4-alt1
- new version

* Thu Jul 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.5.3-alt1
- new version

* Fri Apr 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.5.2-alt1
- new version

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Wed Jun 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt3
- clean version script

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt2
- rebuilt

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt0.M51.1
- built for M51

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.6-alt1
- new version

* Mon Dec 14 2009 Sergey V Turchin <zerg@altlinux.org> 1.4.5-alt1
- new version

* Mon Apr 27 2009 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt2
- built static library

* Mon Jan 26 2009 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt1
- new version
- removed deprecated macroses from specfile

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt1
- new version
- update version script
- split utils to separate package

* Tue Sep 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.2-alt1
- new version

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.1-alt1
- new version

* Fri Dec 14 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.0-alt2
- built without libcap

* Tue Dec 11 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.0-alt1
- new version

* Mon Dec 03 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt1
- new version

* Fri Oct 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1.3.1-alt1
- new version

* Mon Feb 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.2.4-alt1
- new version

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1.2.3-alt1
- new version

* Wed Nov 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt1
- new version
- using /dev/urandom only (not /dev/random)

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.1-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.94-alt1
- new version
- sync patches with PLD

* Thu Mar 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.93-alt0.1
- Updated to the latest upstream release
- Spec cleanup

* Thu Feb 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.91-alt2
- rebuild

* Mon Feb 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.91-alt1
- new version

* Mon Jan 12 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.12-alt3
- remove *.la

* Tue Sep 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.12-alt2
- fix build

* Wed Sep 03 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.12-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.1.10-alt2
- fix requires

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.1.10-alt1
- build for ALT

* Sat Nov 23 2002 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1.10-6mdk
- Better fix for binary name(Patch #0)
- Follow mdk lib policy
- Removed non-existing libgcrypt.txt file from filelist
- bzip2'ed the source
- Remove tests from doc (rpmlint says so)
- Move *.so to -devel package, only *.so.* stays
- Cleanups

* Sat Nov 23 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.10-5mdk
- fix binary name for arch != i586

* Mon Nov 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-4mdk
- Rebuild

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-3mdk
- Fix bin name

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-2mdk
- Fix postun/post

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.10-1mdk
- Initial package
