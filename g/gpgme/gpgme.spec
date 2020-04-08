
%define gpgme_sover 11
%define libgpgme libgpgme%gpgme_sover
%define gpgmepp_sover 6
%define libgpgmepp libgpgmepp%gpgmepp_sover
%define qgpgme_sover 7
%define libqgpgme libqgpgme%qgpgme_sover

%define min_gnupg_version 1.9.6
%define gpg_bin_path %_bindir/gpg2
%define gpgsm_bin_path %_bindir/gpgsm

%def_disable beta

%add_python3_req_skip _gpgme
%add_python_req_skip _gpgme

Name: gpgme
Version: 1.13.1
Release: alt1

Summary: GnuPG Made Easy is a library designed to make access to GnuPG easier for applications
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.gnupg.org/related_software/gpgme/index.html

Conflicts: libgpgme-devel < 1.7
Requires: %gpg_bin_path

# ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%version.tar.bz2
Source: gpgme-%version.tar
# FC
Patch1: 0001-fix-stupid-ax_python_devel.patch
# ALT
Patch11: gpgme-1.4.3-alt-version-script.patch
Patch12: gpgme-1.3.0-alt-gpgme-config-assuan.patch
Patch13: gpgme-1.3.0-alt-tests.patch
Patch14: gpgme-1.3.2-rh-alt-linkage.patch
Patch15: alt-revision.patch

#GOST
%define gostversion 1.0.0
Patch16: %name-%version-gost-constants.patch

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): python-devel python3-devel
BuildRequires: /proc gcc-c++ gnupg2 libgpg-error-devel libpth-devel libstdc++-devel libassuan-devel >= 2.0
BuildRequires: texinfo
BuildRequires: qt5-base-devel swig
BuildRequires: glib2-devel

%package common
Summary: %name common package
Group: System/Configuration/Other
Conflicts: libgpgme < 1.7
%description common
%name common package

%package -n %libgpgme
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Requires: %gpg_bin_path
%description -n %libgpgme
%name library

%package -n %libgpgmepp
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libgpgmepp
%name library

%package -n %libqgpgme
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libqgpgme
%name library

%package -n lib%name
Summary: GnuPG Made Easy!
Group: System/Libraries
Requires: %libgpgme
Provides: libgpgme1 = %version-%release
Obsoletes: libgpgme1 < %version-%release

%package -n lib%name-devel
Summary: Include files for development with GPGME
Group: Development/C
Requires: libgpg-error-devel
Provides: libgpgme1-devel = %version-%release
Obsoletes: libgpgme1-devel < %version-%release

%package -n lib%name-devel-static
Summary: Static libraries for development with GPGME
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: libgpgme1-devel-static = %version-%release
Obsoletes: libgpgme1-devel-static < %version-%release

%package -n python3-module-gpg
Summary: Python GpgME pindings
Group: Development/Python
%description -n python3-module-gpg
Python GpgME pindings

%package -n python-module-gpg
Summary: Python GpgME pindings
Group: Development/Python
%description -n python-module-gpg
Python GpgME pindings

%description
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

%description -n lib%name
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

%description -n lib%name-devel
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

This package contains include files required for development of
GPGME-based applications.

%description -n lib%name-devel-static
GnuPG Made Easy (GPGME) is a C language library that allows to add
support for cryptography to a program.  It is designed to make access
to public key crypto engines like GnuPG or GpgSM easier for
applications.  GPGME provides a high-level crypto API for encryption,
decryption, signing, signature verification and key management.

This package contains static libraries required for development of
GPGME-based statically linked applications.

%prep
%setup
%patch1 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
#%patch14 -p1
%patch15 -p2
%patch16 -p1

%if_disabled beta
sed -i -e 's/@BETA@/no/' configure.ac
%else
sed -i -e 's/@BETA@/yes/' configure.ac
%endif
sed -i -e 's/@REVISION@/gost-%gostversion/' -e 's/@REVISION_DESC@/ALT/' configure.ac

rm doc/*.info* m4/{libtool,lt}*.m4

%autoreconf

%build
mkdir -p tmp_bin
ln -sf %_bindir/gpg2 tmp_bin/gpg
export PATH=$PWD/tmp_bin:$PATH

%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
# --enable-maintainer-mode is required to generate the info file
# when building from CVS snapshot
%configure \
	--disable-silent-rules \
	%{?cvsdate: --enable-maintainer-mode } \
	%{subst_enable static} \
	--disable-fd-passing \
	--with-gpg=%gpg_bin_path \
	--with-gpgsm=%gpgsm_bin_path \
	#

%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std

#check
#export PATH=$PWD/tmp_bin:$PATH
#%make_build -k check

%files
%_bindir/gpgme-tool
%_bindir/gpgme-json

%files common
%doc AUTHORS NEWS README THANKS

%files -n python3-module-gpg
%python3_sitelibdir/gpg*

%files -n python-module-gpg
%python_sitelibdir/gpg*

%files -n lib%name-devel
%_bindir/gpgme-config
%_includedir/*.h
%_includedir/gpgme++/
%_includedir/QGpgME/
%_includedir/qgpgme/
%_libdir/*.so
%_libdir/cmake/Gpgmepp/
%_libdir/cmake/QGpgme/
%_datadir/aclocal/*.m4
%_infodir/*.info*
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-*.pc
%_datadir/common-lisp/source/%name

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name
%files -n %libgpgme
%_libdir/libgpgme.so.%gpgme_sover
%_libdir/libgpgme.so.%gpgme_sover.*
%files -n %libgpgmepp
%_libdir/libgpgmepp.so.%gpgmepp_sover
%_libdir/libgpgmepp.so.%gpgmepp_sover.*
%files -n %libqgpgme
%_libdir/libqgpgme.so.%qgpgme_sover
%_libdir/libqgpgme.so.%qgpgme_sover.*

%changelog
* Mon Dec 09 2019 Paul Wolneykien <manowar@altlinux.org> 1.13.1-alt1
- Fresh up to v 1.13.1.

* Wed Jan 30 2019 Paul Wolneykien <manowar@altlinux.org> 1.11.1-alt2
- Remove the redundant %%ubt macro.
- Added GOST hash constants from libgcrypt (308--311).

* Mon Apr 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Apr 20 2018 Sergey V Turchin <zerg@altlinux.org> 1.11.1-alt1
- new version

* Fri Apr 20 2018 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt2
- fix requires

* Sat Oct 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt0.M80P.1
- Backport new version to p8 branch

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- new version

* Mon Mar 06 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt2
- clean requires

* Tue Feb 28 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- new version

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 1.5.5-alt2
- fix build requires

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 1.5.5-alt1
- new version

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- new version

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt0.M70P.1
- built for M70P

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt1
- new version
- security fixes: CVE-2014-3564

* Thu Jun 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt0.M70P.1
- built for M70P

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt1
- new version

* Tue Dec 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt1
- new version

* Wed May 23 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt2
- Fixed build with ld --no-copy-dt-needed-entries.

* Mon Aug 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt5
- Fixed tests to work with gnupg-2.0.17.

* Thu Nov 18 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt4
- Rebuilt for soname set-versions.

* Mon Feb 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt3
- Fixed gpgme-config so it won't force redundant linkage with -lassuan
  any longer; libgpgme is already linked with -lassuan, that's enough.
  This unwanted gpgme-config behaviour was introduced in 1.3.0 version.
- Dropped -texinfo.patch, install-info(1) starting with texinfo-4.12
  formats direntries automatically.
- Forced info docs regeneration with makeinfo --no-split.

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt2
- Rebuilt with libassuan2.so.0.
- Updated version script.
- Cleaned up specfile.

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version (ALT#20640)

* Tue May 12 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.8-alt0.M50.1
- built for M50

* Thu May 07 2009 Sergey V Turchin <zerg@altlinux.org> 1.1.8-alt1
- new version
- remove deprecated macroses from specfile
- fix requires to gnupg2-gpg

* Tue Oct 21 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1.7-alt2
- fix requires

* Mon Oct 20 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1.7-alt1
- new version

* Wed Jan 09 2008 Sergey V Turchin <zerg at altlinux dot org> 1.1.6-alt1
- new version

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.5-alt1
- new version

* Fri Mar 09 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.3-alt2
- add multiple-message.patch from upstream

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.3-alt1
- new version

* Fri Mar 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.1.2-alt1
- new version

* Wed Nov 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1.0-alt1
- new version

* Tue Nov 29 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt2
- obsolete libgpgme1

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt1
- new version

* Wed Jun 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Mon Oct 25 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Thu Aug 26 2004 Sergey Vlasov <vsu@altlinux.ru> 0.3.16-alt2
- Added gpgme-0.3.16-fix-select-status.patch: fix hang in tests/gpg/t-edit (the
  event loop was remembering that the fd was ready even after
  rungpg.c:read_status() had flushed it).
- Updated BuildRequires.

* Fri Dec 12 2003 Sergey Vlasov <vsu@altlinux.ru> 0.3.16-alt1
- 0.3.16 release:
  * Compatibility fixes for GnuPG 1.9.x
- Do not package static libraries by default.
- Removed *.la files.
- Updated BuildRequires.

* Thu May 29 2003 Sergey Vlasov <vsu@altlinux.ru> 0.3.15-alt1
- 0.3.15 release.
- Build with libpth support (does not introduce new dependencies for the
  binary package - thread library is detected using weak symbols).
- Build with gpgsm support (but the dependency to newpg is not added -
  the application/library package which links to libgpgme and uses the
  gpgsm features must have this dependency).

* Fri Feb 07 2003 Sergey Vlasov <vsu@altlinux.ru> 0.3.14-alt2
- Updated URL (#1656) and source location.
- Removed patch to set minimum required GnuPG version to 1.0.7.
  Now GnuPG >= 1.2.0 is required.

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.3.14-alt1
- new version

* Sun Oct 27 2002 Sergey Vlasov <vsu@altlinux.ru> 0.3.12-alt1
- 0.3.12 release.
- Patch to set minimum required GnuPG version to 1.0.7
  (I don't see any changes which would require GnuPG 1.2.0).
- Added "make check" to make sure the library really works.

* Thu Aug 29 2002 Sergey Vlasov <vsu@altlinux.ru> 0.3.10-alt0.1
- Version from CVS 20020829 (bug with child process handling was fixed).
- Removed gnupg requires from *-devel.
- More specfile cleanup.
- Patch to backport gpgme.m4 to old autoconf (removed AC_HELP_STRING).

* Mon Sep 17 2001 Sergey Vlasov <vsu@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Tue Apr 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.2.1-alt1
- 0.2.1
- Moved static libraries to devel-static subpackage.
- Specfile cleanup.

* Mon Feb 19 2001 AEN <aen@logic.ru>
- first build for Sisyphus
