%define nspr_version 4.21-alt1

Summary:	Netscape Network Security Services(NSS)
Name:		nss
Version:	3.45.0
Release:	alt1
License:	MPL/GPL/LGPL
Group:		System/Libraries
Url:		http://www.mozilla.org/projects/security/pki/nss
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	nss-%version.tar
Source1:	nss.pc.in
Source2:	nss-config.in
Source4:	nss-db-%version.tar
Source5:	setup-nsssysinit.sh
Source6:	system-pkcs11.txt
Source7:	nss-pem-%version.tar

Patch0:		nss_with_system_nspr.patch
Patch2:		nss-no-rpath.patch
Patch3:		nss-use-sqlite.patch
Patch4:		nss-use-mozsqlite.patch
Patch5:		nss-fix-objdir.patch
Patch6:		nss-no-tests.patch

# Fedora patches
Patch10:	nss-enable-pem.patch

BuildRequires:  gcc-c++
BuildRequires:  chrpath zlib-devel libsqlite3-devel
BuildRequires:  rpm-macros-alternatives
BuildRequires:  libnspr-devel >= %nspr_version
Requires:       libnspr       >= %nspr_version

%description
Network Security Services (NSS) is a set of libraries designed
to support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME,
X.509 v3 certificates, and other security standards.  See:
http://www.mozilla.org/projects/security/pki/nss/overview.html

%package -n lib%name
Summary:	Netscape Network Security Services(NSS)
Group:		System/Libraries

Provides:	%name = %version-%release

%description -n lib%name
Network Security Services (NSS) is a set of libraries designed
to support cross-platform development of security-enabled server
applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME,
X.509 v3 certificates, and other security standards.  See:
http://www.mozilla.org/projects/security/pki/nss/overview.html

%package -n lib%name-sysinit
Summary:	System NSS Initilization
Group:		System/Libraries
Requires:	lib%name = %version-%release

Provides:	%name-sysinit
Provides:	%name-system-init

%description -n lib%name-sysinit
Default Operating System module that manages applications loading
NSS globally on the system. This module loads the system defined
PKCS #11 modules for NSS and chains with other NSS modules to load
any system or user configured modules.


%package -n lib%name-devel
Summary:	NSS development kit
Group:		Development/C
Requires:	lib%name = %version-%release

Provides:	%name-devel        = %version-%release
Provides:	%name-pkcs11-devel = %version-%release

%description -n lib%name-devel
NSS development kit

%package -n lib%name-devel-static
Summary:	NSS static libraries
Group:		Development/C
Requires:	lib%name-devel = %version-%release

Provides:	%name-devel-static = %version-%release

%description -n lib%name-devel-static
NSS development kit (static libs)

%package -n lib%name-nssckbi-checkinstall
Summary: Check p11-kit-trust.so and libnssckbi.so compatibility
Group: Security/Networking
Requires: p11-kit-checkinstall

%description -n lib%name-nssckbi-checkinstall
During installation check that p11-kit-trust.so and libnssckbi.so are
compatible with each other.
This package intedent to be used in the install check step in the build
system only and should not be installed in the real systems.

%package -n %name-utils
Summary:	Netscape Network Security Services Utilities
Group:		Development/Other
Requires:	lib%name = %version-%release

Provides:	%name-tools

%description -n %name-utils
Netscape Network Security Services Utilities


%prep
%setup -q
%setup -q -T -D -a7
%patch2 -p0
%patch5 -p2
%patch6 -p2

%patch10 -p0

:>nss/coreconf/Werror.mk

pushd nss/tests/ssl
# Create versions of sslcov.txt and sslstress.txt that disable tests
# for SSL2 and EXPORT ciphers.
cat sslcov.txt| sed -r "s/^([^#].*EXPORT|^[^#].*SSL2)/#disabled \1/" > sslcov.noSSL2orExport.txt
cat sslstress.txt| sed -r "s/^([^#].*EXPORT|^[^#].*SSL2)/#disabled \1/" > sslstress.noSSL2orExport.txt
popd

%build
export BUILD_OPT=1 
export NS_USE_GCC=1
export CC_IS_GCC=1
export NSS_NO_SSL2_NO_EXPORT=1
export NSS_ENABLE_ECC=1
export NSS_ENABLE_WERROR=0
export NSS_USE_SYSTEM_SQLITE=1
export USE_SYSTEM_ZLIB=1
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
export NSPR_INCLUDE_DIR=/usr/include/nspr
export NSPR_LIB_DIR=%_libdir

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

%{?_is_lp64:export USE_64=1}

make -C nss/coreconf
make -C nss/coreconf platform 2>/dev/null |grep '^Linux' >destdir
make -C nss/lib/dbm
make -C nss

%install
mkdir -p %buildroot{%_bindir,%_libdir/pkgconfig,%_includedir}

# Get some variables
DESTDIR="$(head -1 destdir)"
NSPR_VERSION="$(nspr-config --version)"
nss_h="nss/lib/nss/nss.h"
NSS_VMAJOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMAJOR[[:space:]]\+,,p' "$nss_h")"
NSS_VMINOR="$(sed -ne 's,^#define[[:space:]]\+NSS_VMINOR[[:space:]]\+,,p' "$nss_h")"
NSS_VPATCH="$(sed -ne 's,^#define[[:space:]]\+NSS_VPATCH[[:space:]]\+,,p' "$nss_h")"

# Install NSS libraries 
cd dist
cp -aL "$DESTDIR"/bin/* %buildroot%_bindir
cp -aL "$DESTDIR"/lib/* %buildroot%_libdir

# Install NSS headers
cd public
cp -aL nss %buildroot%_includedir

# Install NSS utils
sed -e "s,@libdir@,%_libdir,g" \
    -e "s,@prefix@,%_prefix,g" \
    -e "s,@exec_prefix@,%_prefix,g" \
    -e "s,@includedir@,%_includedir/nss,g" \
    -e "s,@NSPR_VERSION@,$NSPR_VERSION,g" \
    -e "s,@NSS_VERSION@,%version,g" \
	%SOURCE1 > %buildroot/%_libdir/pkgconfig/nss.pc

sed -e "s,@libdir@,%_libdir,g" \
    -e "s,@prefix@,%_prefix,g" \
    -e "s,@exec_prefix@,%_prefix,g" \
    -e "s,@includedir@,%_includedir/nss,g" \
    -e "s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g" \
    -e "s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g" \
    -e "s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g" \
    %SOURCE2 > %buildroot/%_bindir/nss-config

chmod 755 %buildroot/%_bindir/nss-config

# Add real RPATH
find "%buildroot%_bindir" "%buildroot%_libdir" -type f | 
while read f; do
  file "$f" | grep -qs ELF || continue
  if chrpath -l "$f" | fgrep -qs "RPATH="; then
    chrpath -d "$f"
  fi
done

# https://wiki.mozilla.org/NSS_Shared_DB
# https://wiki.mozilla.org/NSS_Shared_DB_Samples
# https://wiki.mozilla.org/NSS_Shared_DB_Howto
# https://wiki.mozilla.org/NSS_Shared_DB_And_LINUX
mkdir -p -- %buildroot/%_sysconfdir/pki/nssdb
tar -x -C %buildroot/%_sysconfdir/pki/nssdb -f %SOURCE4
find %buildroot/%_sysconfdir/pki/nssdb -name 'blank-*.db' -printf '%%h %%f\n' |
while read p n; do
	mv -f -- "$p/$n" "$p/${n##blank-}"
done

install -p -m755 %SOURCE5 %buildroot/%_bindir/setup-nsssysinit.sh
install -p -m644 %SOURCE6 %buildroot/%_sysconfdir/pki/nssdb/pkcs11.txt

# alternatives
mkdir -p -- %buildroot/%_libdir/nss
mv -- %buildroot/%_libdir/libnssckbi.so %buildroot/%_libdir/nss/libnssckbi.so

mkdir -p -- %buildroot/%_altdir
cat >%buildroot/%_altdir/libnssckbi-%name <<EOF
%_libdir/libnssckbi.so	%_libdir/nss/libnssckbi.so	10
EOF

%files -n %name-utils
%_bindir/*
%exclude %_bindir/setup-nsssysinit.sh
# Remove tests and samples
%exclude %_bindir/%name-config
%exclude %_bindir/bltest
%exclude %_bindir/dbtest
%exclude %_bindir/mangle
%exclude %_bindir/ocspclnt
%exclude %_bindir/oidcalc
%exclude %_bindir/sdrtest
%exclude %_bindir/shlibsign

%files -n lib%name
%_altdir/libnssckbi-%name
%_libdir/*.so*
%_libdir/*.chk
%_libdir/nss
%dir %_sysconfdir/pki/nssdb
%config(noreplace) %_sysconfdir/pki/nssdb/cert8.db
%config(noreplace) %_sysconfdir/pki/nssdb/key3.db
%config(noreplace) %_sysconfdir/pki/nssdb/secmod.db
%exclude %_libdir/libnsssysinit.so

%files -n lib%name-sysinit
%_libdir/libnsssysinit.so
%config(noreplace) %_sysconfdir/pki/nssdb/cert9.db
%config(noreplace) %_sysconfdir/pki/nssdb/key4.db
%config(noreplace) %_sysconfdir/pki/nssdb/pkcs11.txt
%_bindir/setup-nsssysinit.sh

%files -n lib%name-devel
%_bindir/%name-config
%dir %_includedir/%name
%_includedir/%name
%_libdir/pkgconfig/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-nssckbi-checkinstall

# https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/NSS_{version}_release_notes
%changelog
* Thu Jul 11 2019 Alexey Gladkov <legion@altlinux.ru> 3.45.0-alt1
- New version (3.45).

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 3.44.0-alt1
- New version (3.44).

* Tue May 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.43.0-alt2
- Use %%_is_lp64 macro to determine if arch is 64-bit.

* Sun Mar 31 2019 Alexey Gladkov <legion@altlinux.ru> 3.43.0-alt1
- New version (3.43).

* Fri Feb 01 2019 Alexey Gladkov <legion@altlinux.ru> 3.42.1-alt1
- New version (3.42.1).

* Thu Dec 20 2018 Alexey Gladkov <legion@altlinux.ru> 3.40.1-alt1
- New version (3.40.1).

* Mon Nov 12 2018 Alexey Gladkov <legion@altlinux.ru> 3.40.0-alt1
- New version (3.40).

* Sun Sep 09 2018 Alexey Gladkov <legion@altlinux.ru> 3.39.0-alt1
- New version (3.39).

* Tue Jul 03 2018 Alexey Gladkov <legion@altlinux.ru> 3.38.0-alt1
- New version (3.38).

* Thu Jun 07 2018 Alexey Gladkov <legion@altlinux.ru> 3.36.4-alt1
- New version (3.36.4).

* Thu May 17 2018 Alexey Gladkov <legion@altlinux.ru> 3.36.1-alt1
- New version (3.36.1).

* Wed Mar 21 2018 Alexey Gladkov <legion@altlinux.ru> 3.36.0-alt1
- New version (3.36).

* Fri Jan 12 2018 Alexey Gladkov <legion@altlinux.ru> 3.34.1-alt3
- Fix the alteranatives file.

* Fri Dec 29 2017 Alexey Gladkov <legion@altlinux.ru> 3.34.1-alt2
- Add the alteranatives file for libnssckbi.so.
- Add libnss-nssckbi-checkinstall subpackage.

* Sat Dec 23 2017 Alexey Gladkov <legion@altlinux.ru> 3.34.1-alt1
- New version (3.34.1).
- Remove obsolete nss-alt-ssl-addon-certs.txt.

* Sun Oct 08 2017 Alexey Gladkov <legion@altlinux.ru> 3.33.0-alt1
- New version (3.33).

* Fri Aug 25 2017 Alexey Gladkov <legion@altlinux.ru> 3.32.0-alt1
- New version (3.32).

* Wed Jul 12 2017 Alexey Gladkov <legion@altlinux.ru> 3.31.0-alt1
- New version (3.31).

* Wed Mar 15 2017 Alexey Gladkov <legion@altlinux.ru> 3.30.0-alt1
- New version (3.30).

* Mon Jan 30 2017 Alexey Gladkov <legion@altlinux.ru> 3.28.1-alt1
- New version (3.28.1).

* Fri Oct 21 2016 Alexey Gladkov <legion@altlinux.ru> 3.27.1-alt1
- New version (3.27.1).

* Mon Aug 15 2016 Alexey Gladkov <legion@altlinux.ru> 3.26.0-alt1
- New version (3.26).

* Fri Jun 10 2016 Alexey Gladkov <legion@altlinux.ru> 3.24.0-alt1
- New version (3.24).

* Mon Mar 21 2016 Alexey Gladkov <legion@altlinux.ru> 3.23.0-alt1
- New version (3.23).
- Add tstclnt and vfyserv (ALT#31803)
- Disable SSL2.

* Wed Feb 10 2016 Alexey Gladkov <legion@altlinux.ru> 3.22.0-alt1
- New version (3.22.0).

* Fri Jan 08 2016 Alexey Gladkov <legion@altlinux.ru> 3.20.2-alt1
- New version (3.20.2).

* Thu Nov 05 2015 Alexey Gladkov <legion@altlinux.ru> 3.20.1-alt1
- New version (3.20.1).

* Sat Jul 25 2015 Alexey Gladkov <legion@altlinux.ru> 3.19.2-alt1
- New version (3.19.2).

* Mon May 18 2015 Alexey Gladkov <legion@altlinux.ru> 3.19.0-alt1
- New version (3.19.0).

* Mon Apr 06 2015 Alexey Gladkov <legion@altlinux.ru> 3.18.0-alt1
- New version (3.18.0).

* Sun Mar 08 2015 Alexey Gladkov <legion@altlinux.ru> 3.17.4-alt1
- New version (3.17.4).

* Mon Nov 17 2014 Alexey Gladkov <legion@altlinux.ru> 3.17.2-alt1
- New version (3.17.2).

* Wed Sep 24 2014 Alexey Gladkov <legion@altlinux.ru> 3.17.1-alt1
- New version (3.17.1).

* Mon Jun 30 2014 Alexey Gladkov <legion@altlinux.ru> 3.16.2-alt1
- New version (3.16.2).

* Sat May 10 2014 Alexey Gladkov <legion@altlinux.ru> 3.16.1-alt1
- New version (3.16.1).

* Thu Feb 06 2014 Alexey Gladkov <legion@altlinux.ru> 3.15.4-alt1
- New version (3.15.4).

* Wed Nov 20 2013 Alexey Gladkov <legion@altlinux.ru> 3.15.3-alt1
- New version (3.15.3).

* Thu Sep 26 2013 Alexey Gladkov <legion@altlinux.ru> 3.15.2-alt1
- New version (3.15.2).

* Fri Aug 09 2013 Alexey Gladkov <legion@altlinux.ru> 3.15.1-alt1
- New version (3.15.1).

* Wed Apr 10 2013 Alexey Gladkov <legion@altlinux.ru> 3.14.3-alt1
- New version (3.14.3).

* Thu Feb 14 2013 Alexey Gladkov <legion@altlinux.ru> 3.14.2-alt1
- New version (3.14.2).

* Fri Jan 11 2013 Alexey Gladkov <legion@altlinux.ru> 3.14.1-alt1
- New version (3.14.1).

* Tue Aug 28 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.6-alt1
- New version (3.13.6).

* Mon May 07 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.4-alt2
- Update external patches.
- Protect against calls before nss_init (ALT#27300).

* Wed Apr 18 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.4-alt1
- New version (3.13.4).

* Thu Jan 12 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.1-alt2
- Fix "__GNUC_MINOR" is not defined (ALT#26809).

* Mon Jan 02 2012 Alexey Gladkov <legion@altlinux.ru> 3.13.1-alt1
- New version (3.13.1).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.11-alt3
- Better coverage for DigiNotarGate in NSS.

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.11-alt2
- Dis-trust DigiNotar root certificate.

* Wed Aug 17 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.11-alt1
- New version (3.12.11).

* Thu Mar 10 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.9.0-alt2
- Apply fedora patches.
- Rebuilt to enable proper debuginfo.

* Fri Feb 25 2011 Alexey Gladkov <legion@altlinux.ru> 3.12.9.0-alt1
- New version (3.12.9).

* Mon Oct 25 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.8.0-alt1
- New version (3.12.8).
- Add libnss-sysinit subpackage.

* Tue Jun 01 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.7.0-alt1.20100601
- New cvs snapshot 3.12.7.0 20100601.

* Sun Mar 28 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.7.0-alt1.20100328
- New cvs snapshot 3.12.7.0 20100328.

* Thu Feb 18 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.6.0-alt1.20100218
- New cvs snapshot 3.12.6.0 20100218.

* Sat Jan 16 2010 Alexey Gladkov <legion@altlinux.ru> 3.12.6.0-alt1.20100116
- New cvs snapshot 3.12.6.0 20100116.

* Wed Nov 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt3.20091106
- Change requires.

* Mon Nov 09 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt2.20091106
- Use system sqlite3 (again).

* Fri Nov 06 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20091106
- New cvs snapshot 3.12.5.0 20091106.

* Sun Nov 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20091101
- New cvs snapshot 3.12.5.0 20091101.

* Fri Sep 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20090918
- New cvs snapshot 3.12.5.0 20090918.

* Mon Aug 31 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.5.0-alt1.20090831
- New cvs snapshot 3.12.5.0 20090831.

* Tue Jun 30 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.4.1-alt1.20090630
- New cvs snapshot 3.12.4.1 20090630.

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.4.1-alt1.20090601
- New cvs snapshot 3.12.4.1 20090601.

* Mon Apr 20 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.4-alt1.20090421
- New cvs snapshot 3.12.4 20090421.

* Thu Mar 05 2009 Alexey Gladkov <legion@altlinux.ru> 3.12.3-alt1.20090305
- New cvs snapshot 3.12.3 20090305.
- Use mozsqlite3.

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.12.3-alt1.20081117
- New cvs snapshot 3.12.3 20081117.

* Sat Jun 28 2008 Alexey Gladkov <legion@altlinux.ru> 3.12.1-alt1.20080628
- New cvs snapshot 3.12.1 20080628.

* Tue May 13 2008 Alexey Gladkov <legion@altlinux.ru> 3.12.1-alt1.20080513
- New version (3.12.1 beta).

* Fri Mar 28 2008 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20080328
- New cvs snapshot 3.12 20080328.

* Sun Mar 02 2008 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20080229
- New cvs snapshot (3.12).

* Sun Feb 03 2008 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20080202
- New cvs snapshot (3.12).

* Wed Nov 28 2007 Alexey Gladkov <legion@altlinux.ru> 3.12-alt1.20071128
- New version (3.12 beta).
- Build with system sqlite and zlib.

* Tue Oct 30 2007 Alexey Gladkov <legion@altlinux.ru> 3.11.7-alt1
- New version (3.11.7).

* Fri Feb 23 2007 Alexey Gladkov <legion@altlinux.ru> 3.11.4-alt1
- New version (3.11.4).
- Build without NSS_ECC_MORE_THAN_SUITE_B.
- Update ALT root CA.

* Thu Nov 16 2006 Alexey Gladkov <legion@altlinux.ru> 3.11.3-alt1
- new version (3.11.3).
- large spec cleanup.
- build with new nspr-4.6.3.

* Sun Jul 16 2006 Alexey Gladkov <legion@altlinux.ru> 3.11.2-alt1
- new version.

* Sun Dec 25 2005 Alexey Gladkov <legion@altlinux.ru> 3.11-alt1
- new version.
- nss.pc was added.
- nss-config fixed.
- x86_64 flags fix.

* Fri Dec 02 2005 Alexey Gladkov <legion@altlinux.ru> 3.10-alt1.1
- NMU.
- nss-config bugfix.
- crmf builtin inside libnss (patch #1).
- New package: nss-utils, libnss-devel-static .

* Wed Nov 23 2005 Eugene Ostapets <eostapets@altlinux.ru> 3.10-alt1
- initial build for ALT Linux.

