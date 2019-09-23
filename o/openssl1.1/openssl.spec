%def_enable tsget

Name: openssl1.1
Version: 1.1.1d
Release: alt1.1

Summary: OpenSSL - Secure Sockets Layer and cryptography shared libraries and tools
License: OpenSSL
Group: System/Base
Url: http://www.openssl.org

# git://git.altlinux.org/gears/o/openssl10.git
Source: openssl-%version.tar
Source1: openssl-config
Source2: Makefile.certificate
Source3: make-dummy-cert
Source4: cc.sh

Patch03: openssl-alt-config.patch
Patch04: openssl-alt-engines-path.patch
Patch05: openssl-alt-e2k-makecontext.patch
Patch06: openssl-upstream-properly-handle-BIO_CTRL_PENDING-and-BIO_CTRL_WPENDING.patch

# Patches from Fedora
# Build changes
Patch101: openssl-rh-build.patch
# Patch102: openssl-rh-defaults.patch (different config)
Patch103: openssl-rh-no-html.patch
# Patch104: openssl-rh-man-rename.patch (not needed)
# Bug fixes
Patch121: openssl-rh-issuer-hash.patch
# Functionality changes
# Patch131: openssl-rh-conf-paths.patch (changes config)
Patch132: openssl-rh-version-add-engines.patch
Patch133: openssl-rh-apps-dgst.patch
# Patch136: openssl-rh-no-brainpool.patch (why disable it?)
# Patch137: openssl-rh-ec-curves.patch (breaks tests; we have no reason to disable this curves, right?)
Patch138: openssl-rh-no-weak-verify.patch
Patch140: openssl-rh-disable-ssl3.patch
Patch141: openssl-rh-system-cipherlist.patch
# Patch142: openssl-rh-fips.patch (not needed)
# Patch143: openssl-rh-ignore-bound.patch (not sure)
# Patch144: openssl-rh-version-override.patch (not needed; FIPS)
Patch145: openssl-rh-weak-ciphers.patch
# Patch146: openssl-rh-seclevel.patch (not needed; FIPS)
# Patch148: openssl-rh-fips-post-rand.patch (not needed)
# Patch149: openssl-rh-evp-kdf.patch (new functionality; not sure)
# Patch150: openssl-rh-ssh-kdf.patch (new functionality; not sure)
# Backported fixes including security fixes

%define shlib_soversion 1.1
%define openssldir /var/lib/ssl
%define old_openssldir %_libdir/ssl

BuildRequires: /usr/bin/pod2man bc zlib-devel perl-PathTools
%if_enabled tsget
BuildRequires: perl-WWW-Curl
%endif

%{?!_without_check:%{?!_disable_check:BuildRequires: perl-Module-Load-Conditional perl-devel perl-Math-BigInt}}

%package -n libcrypto%shlib_soversion
Summary: OpenSSL libcrypto shared library
Group: System/Libraries
Provides: libcrypto = %version-%release
# due to openssl.cnf
Conflicts: libcrypto7, libssl7, libssl6 < 0.9.8d-alt6, libcrypto10 <= 1.0.2q-alt1
# due to openssldir migration
Conflicts: openssl < 0:0.9.8d-alt1
# due to runtime openssl version check
Conflicts: openssh-common < 5.9p1-alt5
Requires: ca-certificates

%package -n libssl%shlib_soversion
Summary: OpenSSL libssl shared library
Group: System/Libraries
Provides: libssl = %version
Requires: libcrypto%shlib_soversion = %version-%release

%package -n libssl-devel
Summary: OpenSSL include files and development libraries
Group: Development/C
Provides: openssl-devel = %version
Obsoletes: openssl-devel < %version
Requires: libssl%shlib_soversion = %version-%release
# due to /usr/bin/openssl-config
Conflicts: openssl < %version-%release, openssl > %version-%release
# manpage clash: crypto(3).
Conflicts: erlang <= 0:R9C.0-alt2

%package -n libssl-devel-static
Summary: OpenSSL static libraries
Group: Development/C
Provides: openssl-devel-static = %version
Obsoletes: openssl-devel-static < %version
Requires: libssl-devel = %version-%release

%package -n openssl
Summary: OpenSSL tools
Group: System/Base
Provides: %openssldir
# due to /usr/bin/openssl-config
Conflicts: libssl-devel < %version-%release, libssl-devel > %version-%release
Requires: libssl%shlib_soversion = %version-%release

%package -n openssl-doc
Summary: OpenSSL documentation and demos
Group: Development/C
Requires: openssl = %version-%release
BuildArch: noarch

%package -n openssl-engines
Summary: OpenSSL ENGINE interface modules
Group: System/Libraries
Requires: libssl%shlib_soversion = %version-%release

%package -n tsget
Summary: Time Stamping HTTP/HTTPS client
Group: Security/Networking 
BuildArch: noarch
Requires: libssl%shlib_soversion = %version-%release

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

%description -n libcrypto%shlib_soversion
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL libcrypto shared library.

%description -n libssl%shlib_soversion
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL libssl shared library.

%description -n libssl-devel
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL include files and development libraries
required when building OpenSSL-based applications.

%description -n libssl-devel-static
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains static libraries required when developing
OpenSSL-based statically linked applications.

%description -n openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the base OpenSSL cryptography and SSL/TLS tools.

%description -n openssl-doc
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains the OpenSSL cryptography and SSL/TLS extra
documentation and demos required when developing applications.

%description -n openssl-engines
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

With OpenSSL 0.9.6, a new component was added to support alternative
cryptography implementations, most commonly for interfacing with external
crypto devices (eg. accelerator cards).  This component is called ENGINE,
and its presence in OpenSSL 0.9.6 (and subsequent bug-fix releases) caused
a little confusion as 0.9.6** releases were rolled in two versions,
a "standard" and an "engine" version.  In development for 0.9.7, the
ENGINE code has been merged into the main branch and is present in
the standard releases from 0.9.7 forwards.

There are currently following built-in ENGINE implementations:
- 4758cca: IBM 4758 CCA hardware support;
- aep: Aep hardware support;
- atalla: Atalla hardware support;
- chil: CHIL hardware support;
- cswift: CryptoSwift hardware support;
- gost: GOST (Russian cryptography standard) implementation;
- nuron: Nuron hardware support;
- padlock: VIA PadLock ACE support;
- sureware: SureWare hardware support;
- ubsec: UBSEC hardware support.

In addition, dynamic binding to external ENGINE implementations is
provided by a special ENGINE called "dynamic".

%description -n tsget
The tsget command can be used for sending a time stamp request, as
specified in RFC 3161, to a time stamp server over HTTP or HTTPS and
storing the time stamp response in a file.  This tool cannot be used for
creating the requests and verifying responses, you can use the OpenSSL
ts(1) command to do that.  tsget can send several requests to the server
without closing the TCP connection if more than one requests are specified
on the command line.

%prep
%setup -n openssl-%version
%patch03 -p1
%patch04 -p1
%patch05 -p2
%patch06 -p1

%patch101 -p1
#%%patch102 -p1 (different config)
%patch103 -p1
#%%patch104 -p1 (not needed)
%patch121 -p1
#%%patch131 -p1 (changes config)
%patch132 -p1
%patch133 -p1
#%%patch136 -p1 (why disable it?)
#%%patch137 -p1 (breaks tests; we have no reason to disable this curves, right?)
%patch138 -p1
%patch140 -p1
%patch141 -p1
#%%patch142 -p1 (not needed)
#%%patch143 -p1 (not sure)
#%%patch144 -p1 (not needed; FIPS)
%patch145 -p1
#%%patch146 -p1 (not needed; FIPS)
#%%patch148 -p1 (not needed)
#%%patch149 -p1 (new functionality; not sure)
#%%patch150 -p1 (new functionality; not sure)

find -type f -name \*.orig -delete

# Correct shared library name.
sed -i 's/\\\$(SHLIB_MAJOR)\.\\\$(SHLIB_MINOR)/\\$(VERSION)/g' Configure

%build
ADD_ARGS=%_os-%_arch
%ifarch %ix86
	ADD_ARGS=linux-elf
%ifarch i386
	ADD_ARGS="$ADD_ARGS 386"
%endif
%endif
%ifarch %arm
ADD_ARGS=linux-generic32
%endif
%ifarch x32
ADD_ARGS=linux-x32
%endif
%ifarch s390x
ADD_ARGS=linux64-s390x
%endif
%ifarch mips mipsel
ADD_ARGS=linux-mips32
%endif
%ifarch mips64 mips64el
ADD_ARGS=linux64-mips64
%endif
%ifarch riscv64 %e2k
ADD_ARGS=linux-generic64
%endif

if echo 'extern __uint128_t i;' |
   gcc %optflags -Werror -c -o/dev/null -xc -; then
	ADD_ARGS="enable-ec_nistp_64_gcc_128 $ADD_ARGS"
fi

# Correct compilation options.
%add_optflags -fno-strict-aliasing -Wa,--noexecstack

./Configure shared \
	--prefix=%prefix \
	--libdir=%_lib \
	--openssldir=%openssldir \
	--system-ciphers-file=%_sysconfdir/openssl/cipher-list.conf \
	enable-egd \
	enable-md2 \
	enable-rfc3779 \
	enable-ssl3 \
	zlib \
	$ADD_ARGS \
	%optflags \
#

make generate_crypto_objects
%make_build

# Make soname symlinks.
/sbin/ldconfig -nv .

# Save library timestamps for later check.
touch -r libcrypto.so.%shlib_soversion libcrypto-stamp
touch -r libssl.so.%shlib_soversion libssl-stamp

#LD_LIBRARY_PATH=`pwd` make rehash

%install
# The make_install macro doesn't work here.
make install \
	CC=%_sourcedir/cc.sh \
	DESTDIR=%buildroot \
	MANDIR=%_mandir

# Fail if one of shared libraries was rebuit.
if [ libcrypto.so.%shlib_soversion -nt libcrypto-stamp -o \
     libssl.so.%shlib_soversion -nt libssl-stamp ]; then
	echo 'Shared library was rebuilt by "make install".'
	exit 1
fi

# Fail if the openssl binary is statically linked against OpenSSL at this
# stage (which could happen if "make install" caused anything to rebuild).
LD_LIBRARY_PATH=`pwd` ldd %buildroot%_bindir/openssl |tee openssl.libs
grep -qw libssl openssl.libs
grep -qw libcrypto openssl.libs

# Install openssl-config script.
install -pDm755 %_sourcedir/openssl-config %buildroot%_bindir/openssl-config
subst -p 's,%%version,%version,g;s,%%openssldir,%openssldir,g' \
	%buildroot%_bindir/openssl-config

# Relocate shared libraries from %_libdir/ to /lib/.
mkdir -p %buildroot{/%_lib,%_libdir/openssl,%_sbindir}
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f") || continue
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# Relocate openssl.cnf from %%openssldir/ to %_sysconfdir/openssl/.
mkdir -p %buildroot%_sysconfdir/openssl
mv %buildroot%openssldir/openssl.cnf %buildroot%_sysconfdir/openssl/
ln -s -r %buildroot%_sysconfdir/openssl/openssl.cnf %buildroot%openssldir/

# Rename some man pages, fix references.
for f in passwd.1 config.5; do
	name="${f%%.*}"
	sect="${f##*.}"
	NAME=`printf %%s "$name" |tr '[:lower:]' '[:upper:]'`
	sed -i "s/\\<$NAME $sect\\>/SSL&/" %buildroot%_mandir/man"$sect/$f"
	mv -v %buildroot%_mandir/man"$sect"/{,ssl}"$f"
	find %buildroot%_mandir -type f -print0 |
		xargs -r0 grep -FZl "\\fI$name\\fR\\|($sect)" -- |
		xargs -r0 subst -p "s/\\\\fI$name\\\\fR\\\\|($sect)/\\\\fIssl$name\\\\fR\\\\|($sect)/" --
	find %buildroot%_mandir -type l |while read link; do
		[ "$(readlink -n "$link")" = "$f" ] || continue
		ln -sfv "ssl$f" "$link"
	done
done
# ln -s sslconfig.5 %buildroot%_mandir/man5/openssl.cnf.5

# Make backwards-compatibility symlink to ssleay.
ln -snf openssl %buildroot%_bindir/ssleay

# Install a makefile for generating keys and self-signed certs,
# and a script for generating them on the fly.
install -pDm644 %_sourcedir/Makefile.certificate \
	%buildroot%openssldir/certs/Makefile
install -pDm644 %_sourcedir/make-dummy-cert \
	%buildroot%openssldir/certs/make-dummy-cert

ln -s -r %buildroot%_datadir/ca-certificates/ca-bundle.crt \
	%buildroot%openssldir/cert.pem

%if_enabled tsget
mv %buildroot%openssldir/misc/tsget.pl %buildroot%_sbindir/
rm %buildroot%openssldir/misc/tsget
ln -s tsget.pl %buildroot%_sbindir/tsget
%else
rm %buildroot%openssldir/misc/tsget.pl
rm %buildroot%openssldir/misc/tsget
%endif

rm %buildroot%openssldir/openssl.cnf.dist
rm %buildroot%openssldir/ct_log_list.cnf.dist

%define docdir %_docdir/openssl-%version
mkdir -p %buildroot%docdir
install -pm644 CHANGES* LICENSE NEWS README* \
	%buildroot%docdir/
bzip2 -9 %buildroot%docdir/CHANGES*
cp -a demos doc %buildroot%docdir/
rm -rf %buildroot%docdir/doc/{apps,crypto,ssl}

# Create default cipher-list.conf from SSL_DEFAULT_CIPHER_LIST
sed -n -r 's,^#.*SSL_DEFAULT_CIPHER_LIST[[:space:]]+"([^"]+)",\1,p' \
	include/openssl/ssl.h > %buildroot%_sysconfdir/openssl/cipher-list.conf

%check
LD_LIBRARY_PATH=%buildroot/%_lib \
	OPENSSL_ENABLE_MD5_VERIFY= \
	OPENSSL_SYSTEM_CIPHERS_OVERRIDE=%buildroot%_sysconfdir/openssl/cipher-list.conf \
	make test V=1

%define _unpackaged_files_terminate_build 1

%files -n libcrypto%shlib_soversion
/%_lib/libcrypto*
%config(noreplace) %_sysconfdir/openssl/openssl.cnf
%dir %_sysconfdir/openssl/
%dir %openssldir
%openssldir/*.cnf
%openssldir/*.pem
%dir %docdir
%docdir/[A-Z]*

%files -n libssl%shlib_soversion
%config(noreplace) %_sysconfdir/openssl/cipher-list.conf
%dir %_sysconfdir/openssl/
/%_lib/libssl*

%files -n libssl-devel
%_bindir/openssl-config
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*

%files -n libssl-devel-static
%_libdir/*.a

%files -n openssl
%_bindir/*
%dir %openssldir
%openssldir/misc
%openssldir/certs
%dir %attr(700,root,root) %openssldir/private
%_mandir/man[157]/*
%if_enabled tsget
%exclude %_man1dir/tsget.*
%exclude %_man1dir/openssl-tsget.*
%endif

%files -n openssl-doc
%dir %docdir
%docdir/[a-z]*
%_man3dir/*

%files -n openssl-engines
%_libdir/openssl

%if_enabled tsget
%files -n tsget
%_sbindir/tsget
%_sbindir/tsget.pl
%_man1dir/tsget.*
%_man1dir/openssl-tsget.*
%endif

%changelog
* Sat Sep 21 2019 Michael Shigorin <mike@altlinux.org> 1.1.1d-alt1.1
- Fixed build --without check.

* Thu Sep 19 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1d-alt1
- Updated to 1.1.1d (fixes CVE-2019-1543, CVE-2019-1549, CVE-2019-1563,
  CVE-2019-1547, CVE-2019-1552).
- Changed License: tag to SPDX identifier of actual openssl license.

* Tue Apr 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1b-alt2
- Readded %%_bindir/openssl-config to openssl subpackage (removed in
  1.1.1b-alt1 release by mistake).
- Added %%e2k arch support (bircoph@).

* Wed Mar 20 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1b-alt1
- Updated to v1.1.1b.
- libcrypto1.1: add C: libcrypto10 <= 1.0.2q-alt1.

* Mon Mar 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0j-alt2
- Backport new gost algorithm identificators from upstream.

* Tue Nov 20 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0j-alt1
- Updated to v1.1.0j.

* Tue Aug 28 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0i-alt1
- Updated to v1.1.0i.

* Tue Mar 27 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2o-alt1
- Updated to v1.0.2o (fixes CVE-2018-0739).

* Thu Dec 07 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2n-alt1
- Updated to v1.0.2n (fixes CVE-2017-3737, CVE-2017-3738).
- Added --disable tsget knob.
- Added support of s390x and mips* architectures.

* Sat Nov 04 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2m-alt1
- Updated to v1.0.2m (fixes CVE-2017-3735, CVE-2017-3736).

* Thu Jan 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2k-alt1
- Updated to v1.0.2k (fixes CVE-2016-7055, CVE-2017-3731, CVE-2017-3732).

* Mon Sep 26 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2j-alt1
- Updated to v1.0.2j (fixes CVE-2016-6309).

* Thu Sep 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2i-alt1
- Updated to 1.0.2i (fixes CVE-2016-2177, CVE-2016-2179,
  CVE-2016-2180, CVE-2016-2181, CVE-2016-2182, CVE-2016-2183,
  CVE-2016-6302, CVE-2016-6303, CVE-2016-6304, CVE-2016-6306).

* Wed Jun 08 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2h-alt2
- Backported upstream fix for CVE-2016-2178.

* Tue May 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2h-alt1
- Updated to 1.0.2h (fixes CVE-2016-2105 CVE-2016-2106 CVE-2016-2107
  CVE-2016-2109 CVE-2016-2176).

* Tue Mar 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2g-alt1
- Updated to 1.0.2g (fixes CVE-2016-0701 CVE-2016-0702
  CVE-2016-0705 CVE-2016-0797 CVE-2016-0798
  CVE-2016-0799 CVE-2016-0800).
- Added default ciphers to system profile.

* Thu Jan 28 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2f-alt1
- Updated to 1.0.2f (fixes CVE-2015-3197 CVE-2016-0701).

* Tue Jan 12 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2e-alt2
- libcrypto10: added conflict: libcrypto7, libssl7
  (due to openssl.cnf; ALT#31671).

* Mon Dec 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2e-alt1
- Updated to 1.0.2e.
- Updated patches from Fedora openssl-1.0.2e-4.
- Added support of system profile for default cipher list.
- Disabled support of updating from openssl <= 0.9.6g-alt2.
- Updated openssl-alt-config.patch:
  + [ CA_default ] default_md = sha1 -> sha256.
  + [ req ] default_md = sha1 -> sha256.
  + [ tsa_config1 ] digests = md5, sha1 -> sha1, sha256, sha384, sha512.

* Thu Dec 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1q-alt1
- Updated to 1.0.1q (CVE-2015-1788 CVE-2015-3196 CVE-2015-3195
  CVE-2015-3194).

* Thu Jul 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1k-alt4
- Fixed CVE-2015-1793.

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1k-alt3
- Fixed CVE-2015-1789, CVE-2015-1790, CVE-2015-1791, CVE-2015-1792,
  CVE-2015-0209, CVE-2015-4000.

* Thu Mar 19 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1k-alt2
- Fixed CVE-2015-0209, CVE-2015-0286, CVE-2015-0287, CVE-2015-0288,
  CVE-2015-0289, CVE-2015-0293.

* Mon Jan 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1k-alt1
- Updated to 1.0.1k (fixes CVE-2014-3571, CVE-2015-0206, CVE-2014-3569,
  CVE-2014-3572, CVE-2015-0204, CVE-2015-0205, CVE-2014-8275,
  CVE-2014-3570) (closes: 30644).

* Mon Jan 05 2015 Dmitry V. Levin <ldv@altlinux.org> 1.0.1j-alt2
- Build with enable-ec_nistp_64_gcc_128 on architectures where
  gcc supports __uint128_t (closes: #30625).

* Thu Oct 30 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1j-alt1
- Updated to 1.0.1j (fixes CVE-2014-3512, CVE-2014-3511, CVE-2014-3510,
  CVE-2014-3507, CVE-2014-3506, CVE-2014-3505, CVE-2014-3509,
  CVE-2014-5139,  CVE-2014-3508, CVE-2014-3513, CVE-2014-3567,
  CVE-2014-3566, CVE-2014-3568).
- Updated patches from Fedora openssl-1.0.1j-2.
- kssl.h: include <krb5/krb5.h> instead of <krb5/krb5/krb5.h> (ldv@).

* Thu Jun 05 2014 Dmitry V. Levin <ldv@altlinux.org> 1.0.1h-alt1
- Updated to 1.0.1h (fixes CVE-2014-0224, CVE-2014-022, CVE-2014-019,
  CVE-2014-347, and CVE-2010-5298).

* Mon Apr 07 2014 Dmitry V. Levin <ldv@altlinux.org> 1.0.1g-alt1
- Updated to 1.0.1g (fixes CVE-2014-0076 and CVE-2014-0160).

* Tue Feb 04 2014 Dmitry V. Levin <ldv@altlinux.org> 1.0.1f-alt2
- Made 3DES strength to be 128 bits instead of 168 (RH#1056616).
- Dropped delusive compatibility with alien libssl packages.

* Mon Jan 06 2014 Dmitry V. Levin <ldv@altlinux.org> 1.0.1f-alt1
- Updated to 1.0.1f
  (fixes CVE-2013-4353, CVE-2013-6449, and CVE-2013-6450).

* Wed Apr 10 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.1e-alt1
- Updated to OpenSSL_1_0_1e-21-g0e9dd38.
- Updated patches from Fedora openssl-1.0.1e-4.
- Changed section where tests are run from %%build to %%check.

* Wed Feb 27 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.0k-alt1
- Updated to OpenSSL_1_0_0k-15-g0e05f88
  (fixes CVE-2013-0166 and CVE-2013-0169).

* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0j-alt1
- Updated to 1.0.0j (fixes CVE-2012-2333).

* Thu Apr 19 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0i-alt1
- Updated to 1.0.0i (fixes CVE-2012-2110).

* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0h-alt1
- Updated to 1.0.0h (fixes CVE-2012-0050, CVE-2012-0884 and other bugs).

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.0f-alt1
- Updated to 1.0.0f (fixes multiple CVEs).

* Mon Sep 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0e-alt1
- Updated to 1.0.0e (fixes CVE-2011-3207).

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0d-alt2
- In pkgconfig files, moved -ldl -lz to Libs.private.

* Wed Feb 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0d-alt1
- Updated to 1.0.0d (fixes CVE-2011-0014).

* Tue Feb 01 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0.0c-alt1
- Updated to 1.0.0c (fixes CVE-2010-4180).

* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0b-alt1
- Updated to 1.0.0b (fixes CVE-2010-2939 and CVE-2010-3864).

* Sat Oct 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0a-alt2
- Hardened conflict with incompatible libssl6 (closes: #24195).

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.0a-alt1
- Updated to 1.0.0a.
- Merged with FC openssl-1.0.0a-3.

* Thu Sep 30 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8o-alt2
- openssl.cnf: Updated from openssl-1.0.0a, merged with FC.

* Wed Sep 29 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8o-alt1
- Updated to 0.9.8o (fixes CVE-2010-0742).
- Fixed ssl/dtls1.h ABI breakage introduced in 0.9.8m.
- Fixed 0.9.8m build regression on architectures where %%_lib != lib.

* Thu Mar 25 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8n-alt1
- Updated to 0.9.8n (fixes CVE-2010-0740 and CVE-2010-0433).

* Fri Feb 26 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8m-alt1
- Updated to 0.9.8m with security fixes and improvements, including:
  + CVE-2009-3245, CVE-2008-1678
  + CVE-2009-1377, CVE-2009-1378, CVE-2009-1379
  + CVE-2009-1387 (closes: #20280)
  + CVE-2009-4355 (closes: #22817, #23037)
  + patch for Cisco VPN client DTLS

* Fri Jan 15 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8l-alt6
- Relocated backwards compatibility symlinks from /%_lib to %_libdir.
- Fixed backwards compatibility Provides on x86-64.

* Fri Jan 15 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8l-alt5
- Added extra symlinks and Provides for backwards compatibility
  with Mandriva's openssl.

* Fri Jan 08 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8l-alt4
- Built for target linux-generic32 on ARM.
- Applied upstream crypto/{md5,sha1} build fixes (by Evgeny Sinelnikov
  and Kirill A. Shutemov).
- Applied upstream compatibility patch for Cisco VPN client DTLS
  (closes: #22615).

* Sat Nov 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8l-alt1
- Updated to 0.9.8l with security fixes and improvements.
- Includes CVE-2009-3555

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8k-alt4
- Relocated %_sysconfdir/openssl and %openssldir from
  libssl7 subpackage to libcrypto7 subpackage.

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8k-alt3
- Packaged libcrypto shared library into separate subpackage
  to break dependency loop (closes: #20175).
- Packaged doc subpackage as noarch.
- Fixed backwards compatibility symlink added in previous build.

* Thu May 21 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8k-alt2
- Added extra symlinks for backwards compatibility with Fedora's libssl8.
- Backported security updates from 0.9.8l:
  CVE-2009-1377, CVE-2009-1378, CVE-2009-1379

* Wed Mar 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8k-alt1
- Updated to new 0.9.8k includes security fixes and improvements
- Includes CVE-2009-0789, CVE-2009-0591, CVE-2009-0590

* Thu Jan 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8j-alt1
- Updated to 0.9.8j includes properly check EVP_VerifyFinal() and
  similar return values (CVE-2008-5077)

* Tue Dec 09 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8i-alt3
- Added patch with pkcs12 fix for '-name' option

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8i-alt2
- Rebuilt without obsolete %post/%postun calls

* Wed Nov 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8i-alt1
- Updated to 0.9.8i

* Wed Nov 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8h-alt4
- Fixed KRB5 cipher crash for FQDN not equal SPN's FQDN at keytab.
  Resolved with fixing checks at kssl_keytab_is_available()

* Sun Aug 10 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.8h-alt3
- Updated dependencies (Alexey Tourbin).
- Added workaround for krb5.h inclusion.

* Sat Aug 09 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8h-alt2
- Fixed patches
+ At openssl-0.9.8g-rh-alt-soversion.patch SHLIB_SOVERSION set to 7
+ openssl-0.9.8g-rh-shlib-version.patch changed to openssl-0.9.8h-alt-shlib-version.patch

* Fri Aug 01 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8h-alt1
- Updated to new release
- Removed old fixes

* Fri Aug 01 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt1
- Prepared to Sisyphus release

* Tue Jun 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt0.eter3
- Added openssl-krb providing

* Fri Jun 13 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt0.eter2
- Changed soname
+ Renamed libssl6 to libssl7

* Thu Jun 12 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8g-alt0.eter1
- Updated to 0.9.8g
- Removed old patches and got new from Fedora

* Wed Mar 26 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.8d-alt4.test2
- Add rfc2712 support with MIT Kerberos.

* Wed Oct 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt4
- Backported upstream fix for off-by-one bug in the
  SSL_get_shared_ciphers() function (CVE-2007-5135).

* Tue Aug 07 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt3
- Fixed side-channel attack on private keys
  (CVE-2007-3108, RH#245732, http://cvs.openssl.org/chngview?cn=16275).
- Mitigated branch prediction attacks
  (RH#250573, http://cvs.openssl.org/chngview?cn=16077).
- Changed SSL/TLS server implementation to be stricter about session ID
  context matching (RH#233599, http://cvs.openssl.org/chngview?cn=16006).

* Tue Feb 06 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt2
- Moved a bundle of X.509 certificates of public Certificate
  Authorities (CA) from openssl package to separate ca-certificates
  package.
- Moved %openssldir/{openssl.cnf,cert.pem} from openssl subpackage
  to libssl6 subpackage.

* Sun Nov 05 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.8d-alt1
- openssl: Updated to 0.9.8d.
- TSA patch: Updated to 20060923 (still not applied by default).
- Asymm patch: Updated to 20061110 (still not applied by default).
- Packaged engine and tsget in separate subpackages.
- Makefile.certificate, ca-bundle.crt: Updated from FC.
- Updated FC specific patches from 0.9.8b-12.
- Renamed subpackage according to soname change: libssl4 -> libssl6.

* Thu Nov 02 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt6
- Updated upstream bss_conn.c fix.
- Renamed srpm: openssl -> openssl097.
- Renamed subpackage: libssl -> libssl4.

* Wed Sep 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt5
- Applied upstream fixes for DoS bugs in ASN1 parser
  (CVE-2006-2937, CVE-2006-2940).
- Applied fix for buffer overflow in SSL_get_shared_ciphers(),
  discovery and patch from Tavis Ormandy and Will Drewry of the
  Google Security Team (CVE-2006-3738).
- Applied fix for possible DoS in the sslv2 client code,
  discovery and patch from Tavis Ormandy and Will Drewry of the
  Google Security Team (CVE-2006-4343).
- Build this package without optimizations based on strict aliasing rules.

* Wed Sep 06 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt4
- Applied upstream patch to avoid RSA signature forgery (CVE-2006-4339).

* Tue Oct 11 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt3
- Applied upstream fix for potential SSL 2.0 rollback
  during SSL handshake (CAN-2005-2969).

* Fri Jun 24 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt2
- Minor package cleanup.

* Fri Jun 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.7g-alt1
- Removed those of RH patches which I do not like.
- Rediffed patches and renamed them accourding to the packaging policy.
- Relocated development manpages from libssl-devel subpackage to
  openssl-doc subpackage.

* Tue Jun 07 2005 Anton D. Kachalov <mouse@altlinux.org> 0.9.7g-alt0.4
- Added multilib support

* Fri Jun 03 2005 LAKostis <lakostis at altlinux.org> 0.9.7g-alt0.3
- Incorporated patches from Fedora.
- Changed certs dir to be more useful.
- Added provides/requires for tsa (for future use).

* Fri Jun 03 2005 LAKostis <lakostis at altlinux.org> 0.9.7g-alt0.2
- Updated to 0.9.7g.
- Made split build (with/without tsa patch).

* Wed Nov 16 2004 LAKostis <lakostis at altlinux.org> 0.9.7e-alt0.1.ts
- Test build with 0.9.7e.

* Thu Oct 26 2004 LAKostis <lakostis at altlinux.org> 0.9.7d-alt1.ts
- Added timestamping support patch.

* Sat May 08 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.7d-alt1
- Updated to 0.9.7d.
- Reviewed patches.
- Applied RH's soname convention.

* Wed Mar 17 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.6m-alt1
- Updated to 0.9.6m.

* Wed Mar 17 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.6l-alt2
- Fixed null-pointer assignment during SSL handshake
  (CAN-2004-0079).

* Fri Nov 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6l-alt1
- Updated to 0.9.6l.
- For non-i386 ix86 platforms, relaxed textrel check.

* Tue Sep 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6k-alt1
- Updated to 0.9.6k:
  + Fix various ASN1 parsing bugs.
  + SSL/TLS protocol fix for unrequested client certificates.

* Thu Aug 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6j-alt2
- Fixed linux-elf-arm architecture support (sbolshakov@, #2804).
- Shared %_bindir/openssl-config between openssl and
  libssl-devel subpackages (fixes #2806).

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6j-alt1
- Updated to 0.9.6j.

* Thu Mar 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6i-alt3
- Applied patch against Klima-Pokorny-Rosa attack.

* Tue Mar 18 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6i-alt2
- Applied blinding patch from OpenSSL team,
  to defend against timing attack on RSA keys.

* Wed Feb 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.6i-alt1
- Updated to 0.9.6i.

* Thu Dec 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6h-alt1
- Updated to 0.9.6h.
- Merged Owl changes:
  * Fri Nov 15 2002 Solar Designer <solar@owl.openwall.com>
  - Dropped the patch removing -Wl,-Bsymbolic which is no longer needed with
    0.9.6g and/or after dropping the explicit "make build-shared".
  - Dropped RSAref stuff.

* Sun Sep 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6g-alt3
- Fixed glibc/crypto compatibility patch.

* Sat Sep 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6g-alt2
- Fixed libssl linkage:
  Don't do an explicit "make build-shared", it's not needed and
  could only cause harm (link libssl against libcrypto statically).
- FHS fixes (#0000915):
  + changed %%openssldir from %_libdir/ssl to /var/lib/ssl;
  + moved openssl.cnf from %%openssldir/ to %_sysconfdir/openssl/;
  + on upgrade, copy old %%openssldir to new location;
  + added openssl-config script to provide current %%openssldir location.
- Renamed openssl-devel subpackage to libssl-devel.
- Renamed openssl-devel-static subpackage to libssl-devel-static.

* Mon Aug 19 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6g-alt1
- 0.9.6g; asn1_lib patch merged upstream.

* Mon Aug 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6e-alt1
- Updated to 0.9.6e, recent security patch merged upstream.
- Added two post-0.9.6e changes from the CVS which correct the recent ASN.1
  parsing vulnerability fixes (Owl).

* Wed Jul 31 2002 Solar Designer <solar@owl.openwall.com>
- Updated to 0.9.6e, dropping the shared-on-SPARC and the official
  security patches (both are now included).

* Mon Jul 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.9.6d-alt2
- Various security fixes (see CHANGES).

* Mon May 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6d-alt1
- Updated to 0.9.6d.
- Added a patch by Ben Laurie for "openssl dgst" to behave on read errors.
- Properly restrict the instruction set in assembly code when building for i386 (Owl).

* Wed Apr 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6c-alt3
- Fixed %_bindir/openssl linkage.
- Relocate shared libs to /lib/.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6c-alt2
- libssl: Conflicts: %%name < %%version-%%release.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9.6c-alt1
- 0.9.6c
- Relocated docs.

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6b-alt1
- 0.9.6b

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6a-alt2
- Changed two memcpy() calls to memmove() (nalin).
- Added a script for creating dummy certificates (nalin).

* Mon May 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6a-alt1
- 0.9.6a
- Keep standard soname scheme.
- Do not provide crypt symbol (solar).
- Use __libc_enable_secure variable (solar).
- Link %_bindir/openssl dinamically with shared libraries from libssl subpackage (solar).

* Wed Apr 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.6-ipl2mdk
- Moved shared libraries to libssl subpackage.
- Moved static libraries to devel-static subpackage.

* Thu Sep 28 2000 Dmitry V. Levin <ldv@fandra.org> 0.9.6-ipl1mdk
- 0.9.6

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org>
- 0.9.5a

* Fri Apr 28 2000 Dmitry V. Levin <ldv@fandra.org>
- separate openssl-doc package
- 0.9.5

* Sun Dec  5 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sun Nov 28 1999 Arne Coucheron <arneco@online.no>
  [0.9.4-3]
- config file moved to /var/ssl due to problems when it stays in /etc

* Tue Aug 17 1999 Arne Coucheron <arneco@online.no>
  [0.9.4-2]
- the source rpm was corrupt, so this is just a rerelase

* Wed Aug 11 1999 Arne Coucheron <arneco@online.no>
  [0.9.4-1]

* Sun Jun 20 1999 Arne Coucheron <arneco@online.no>
  [0.9.3a-1]
- several changes
