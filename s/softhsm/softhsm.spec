%define _unpackaged_files_terminate_build 1
%define softhsm_module "SoftHSM PKCS #11 Module"

Name: softhsm
Version: 2.5.0

Release: alt2
Summary: Software version of a PKCS#11 Hardware Security Module
License: BSD
Group: System/Configuration/Other
# Source-git: https://github.com/opendnssec/SoftHSMv2.git
Url: http://www.opendnssec.org/

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libnss-devel
BuildRequires: libsqlite3-devel
BuildRequires: zlib-devel
BuildRequires: sqlite3

%{?!_without_check:%{?!_disable_check:BuildRequires: cppunit-devel}}

Requires: lib%name = %EVR

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM. SoftHSM is
designed to meet the requirements of OpenDNSSEC, but can also work
together with other cryptographic products because of the PKCS#11
interface.

%package -n lib%name
Summary: Library for Software Hardware Security Module
Group: System/Libraries

%description -n lib%name
This package contains development files for SoftHSM library.

%package devel
Summary: Development package of softhsm that includes the header files
Group: Development/C
BuildArch: noarch
Requires: lib%name = %EVR

%description devel
The devel package contains the libsofthsm include files.

%prep
%setup
%patch -p1

%build
%autoreconf

# remove softhsm/ subdir auto-added to --libdir
sed -i "s:full_libdir/softhsm:full_libdir:g" configure
sed -i 's:^full_libdir=":#full_libdir=":g' configure.ac
sed -i "s:libdir)/@PACKAGE@:libdir):" Makefile.in

%configure \
	--localstatedir=/var \
	--libdir=%_libdir/pkcs11 \
	--with-openssl=%prefix \
	--enable-ecc \
	--disable-gost \
	--with-migrate \
	--enable-visibility \
        --with-p11-kit=%_datadir/p11-kit/modules/ \
	#

%make_build

%check
%make check

%install
%makeinstall_std

rm %buildroot/%_sysconfdir/softhsm2.conf.sample
rm -f %buildroot/%_libdir/pkcs11/*a
mkdir -p %buildroot%_includedir/softhsm
cp src/lib/*.h %buildroot%_includedir/softhsm
mkdir -p %buildroot/%_sharedstatedir/softhsm/tokens

# leave a softlink where softhsm-1 installed its library. Programs like
# opendnssec have that filename in their configuration file.
mkdir -p %buildroot/%_libdir/softhsm/
ln -s ../pkcs11/libsofthsm2.so %buildroot/%_libdir/softhsm/libsofthsm.so
# rhbz#1272423 NSS needs it to be in the search path too
ln -s pkcs11/libsofthsm2.so %buildroot/%_libdir

%pre
getent group ods >/dev/null || groupadd -r ods
getent passwd ods >/dev/null || \
    useradd -r -g ods -d %_sharedstatedir/softhsm -s /sbin/nologin \
    -c "softhsm private keys owner" ods
exit 0

%post

%files
%doc LICENSE README.md NEWS
%_bindir/softhsm2-dump-file
%_bindir/softhsm2-keyconv
%_bindir/softhsm2-migrate
%_bindir/softhsm2-util
%_datadir/p11-kit/modules/softhsm2.module
%attr(0770,ods,ods) %dir %_sharedstatedir/softhsm
%attr(0770,ods,ods) %dir %_sharedstatedir/softhsm/tokens
%_man1dir/*

%files -n lib%name
%dir %_libdir/softhsm
%_libdir/softhsm/libsofthsm.so
%_libdir/libsofthsm2.so
%_libdir/pkcs11/libsofthsm2.so
%config(noreplace) %_sysconfdir/softhsm2.conf
%_man5dir/softhsm2.conf.5*

%files devel
%_includedir/softhsm/

%changelog
* Wed Sep 11 2019 Stanislav Levin <slev@altlinux.org> 2.5.0-alt2
- Applied upstream fixes for FreeIPA DNSSEC.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.4.0 -> 2.5.0.

* Tue Sep 04 2018 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.1.0 -> 2.4.0.

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt3
- Fix build with new cppunit

* Thu Nov 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.0-alt2
- Fixed tokendir in softhsm2.conf.
- Moved softhsm2.conf.5 manpage to lib%name subpackage.

* Wed Nov 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 2.0.0-alt0.rc1.1
- built for ALT Linux (based on rosa/fedora package)
- fixed broken as-needed linking of softhsm2-pk11install.c,
  see also https://bugzilla.mozilla.org/124318
