%define glibc_sourcedir /usr/src/glibc-source

Name: glibc
Version: 2.27
Release: alt11
Epoch: 6

Summary: The GNU libc libraries
# GPLv2+ is used in a bunch of programs, LGPLv2+ is used for libraries.
# Things that are linked directly into dynamically linked programs
# and shared libraries (e.g. crt files, lib*_nonshared.a) have an additional
# exception which allows linking it into any kind of programs or shared
# libraries without restrictions.
License: LGPLv2+, LGPLv2+ with exceptions, GPLv2+
Group: System/Base
Url: http://www.gnu.org/software/glibc/

# Remove -s to get verbose output.
%define PARALLELMFLAGS PARALLELMFLAGS='-j%__nprocs'

%def_with optimization
%def_enable langify
%def_with locales
%def_enable memusagestat

%ifarch x86_64
%def_enable multiarch
%else
%def_disable multiarch
%endif

%define basever 2.27

%define enablekernel 3.2

%ifarch aarch64
%define enablekernel 3.7.0
%endif

%ifarch x32
%define enablekernel 3.4.0
%endif

%ifarch ppc64le
%define enablekernel 3.10.0
%endif

# http://git.altlinux.org/gears/g/glibc.git
Source: glibc-%version-%release.tar

Obsoletes: libc-static, libc-devel, libc-profile, libc-headers,
Obsoletes: linuxthreads, gencat, ldconfig

%define libc_locales_list aa af am an ar as ast ayc az be bem ber bg bho bn bo br brx bs byn ca crh cs csb cv cy da de doi dv dz el en es et eu fa ff fi fil fo fr fur fy ga gd gez gl gu gv ha he hi hne hr hsb ht hu hy ia id ig ik is it iu iw ja ka kk kl km kn ko kok ks ku kw ky lb lg li lij lo lt lv mag mai mg mhr mi mk ml mn mni mr ms mt my nan nb nds ne nhn niu nl nn nr nso oc om or os pa pap pl ps pt ro ru rw sa sat sc sd se shs si sid sk sl so sq sr ss st sv sw szl ta te tg th ti tig tk tl tn tr ts tt ug uk unm ur uz ve vi wa wae wal wo xh yi yo yue zh zu
%define libc_locales %(for i in %libc_locales_list;do echo -n "locale-$i locales-$i ";done)
%define renamed_locales ru_RU.iso88595 ru_UA.koi8u uk_UA.koi8u

PreReq: %name-core = %EVR
PreReq: %name-pthread = %EVR
PreReq: %name-nss = %EVR
PreReq: %name-locales = %EVR
PreReq: %name-gconv-modules = %EVR
PreReq: iconv = %EVR
PreReq: %name-timezones = %EVR
PreReq: %name-utils = %EVR

# Required to hardlink identical locale files.
BuildPreReq: hardlink

# Due to STB_GNU_UNIQUE
BuildPreReq: binutils >= 1:2.20

# Due to enablekernel.
BuildPreReq: glibc-kernheaders >= %enablekernel

BuildPreReq: rpm-build >= 4.0.4-alt61

# This is required for building auxiliary programs.
%{?!_disable_memusagestat:BuildPreReq: libgd2-devel}

BuildPreReq: makeinfo

# g++ and /proc are required for test suite.
%{?!_without_check:%{?!_disable_check:BuildPreReq: gcc-c++ libstdc++-devel-static /proc}}

%define _localstatedir /var
%define _gconvdir %_libdir/gconv
%filter_from_provides /GLIBC_PRIVATE/d
%filter_from_requires /GLIBC_PRIVATE/d

%package preinstall
Summary: The GNU libc preinstall utilities
Group: System/Base
AutoReq: no
PreReq: filesystem

%package core
Summary: The GNU libc core libraries and utilities
Group: System/Libraries
AutoReq: no
PreReq: setup
PreReq: %name-preinstall >= %EVR
Conflicts: %name < %EVR
Conflicts: glibc-core-archopt
Provides: linuxthreads, ldconfig
Obsoletes: linuxthreads, ldconfig
# The dynamic linker supports DT_GNU_HASH
Provides: rtld(GNU_HASH)
# The dynamic linker supports STB_GNU_UNIQUE
Provides: rtld(GNU_UNIQUE)
# The dynamic linker supports STT_GNU_IFUNC
Provides: rtld(GNU_IFUNC)

%package pthread
Summary: The GNU libc pthread libraries
Group: System/Libraries
PreReq: %name-core = %EVR
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}
# due to pthread_cancel_init() which calls __libc_dlopen ("libgcc_s.so.1")
Requires: libgcc_s.so.1%lib_suffix

%package nss
Summary: The GNU libc Name Service Switch subsystem
Group: System/Libraries
PreReq: %name-pthread = %EVR

%package -n libnsl1
Summary: Legacy NIS support library
Group: System/Legacy libraries
PreReq: %name-core = %EVR

%package locales
Summary: The GNU libc locales
Group: System/Internationalization
PreReq: %name-pthread = %EVR
Provides: %name-locales-virtual = %EVR
Provides: locale locales %libc_locales
Obsoletes: locale locales %libc_locales
Obsoletes: %name-locales-junior
Obsoletes: i586-glibc-locales

%package i18ndata
Summary: Files for building customized GNU libc locales
Group: System/Base
BuildArch: noarch
PreReq: %name-core = %EVR
Obsoletes: %name-localedata
Provides: %name-localedata
Conflicts: mutt < 1.3.22.1i

%package gconv-modules
Summary: The GNU libc charset conversion modules
Group: System/Base
PreReq: %name-pthread = %EVR
# hack
Provides: %(test %_lib = lib64 && s='()(64bit)' || s=; for n in CNS GB ISOIR165 JIS JISX0213 KSC; do echo -n "lib$n.so$s %_libdir/gconv/lib$n.so$s "; done)

%package -n iconv
Summary: The GNU libc charset conversion modules
Group: System/Base
PreReq: %name-gconv-modules = %EVR

%package timezones
Summary: The GNU libc timezones data
Group: System/Base
PreReq: %name-pthread = %EVR
Requires: tzdata

%package utils
Summary: The GNU libc misc utilities
Group: System/Base
PreReq: %name-pthread = %EVR
Requires: mktemp >= 1:1.3.1
Provides: gencat
Obsoletes: gencat
# due to rpcinfo
Conflicts: rpcbind < 0.2.1-alt0.4

%package devel
Summary: Include and object files required for C development
Group: Development/C
Requires: %name = %EVR
Requires: glibc-kernheaders >= %enablekernel
Requires: kernel-headers-common >= 1.1.4-alt1
Requires: libcrypt-devel
#Requires: %name-doc = %EVR
%ifarch %ix86 x86_64 %arm
Provides: %_includedir/gnu/stubs-32.h
%endif
%ifarch %ix86
# Earlier gcc's had atexit reference in crtendS.o, which does not
# work with this glibc where atexit is in libc_nonshared.a
Conflicts: gcc < 0:2.96-ipl9mdk
%endif
Obsoletes: libc-headers, libc-devel, linuxthreads-devel

%package devel-static
Summary: Static libraries for C development
Group: Development/C
Requires: %name-devel = %EVR
Obsoletes: libc-static

%package doc
Summary: Documentation for C development
Group: Development/Other
BuildArch: noarch
PreReq: %name-pthread = %EVR
Conflicts: texinfo < 3.11

%package debug
Summary: The GNU libc utilities for software debugging
Group: Development/C
Requires: %name-devel = %EVR
Obsoletes: libc-debug

%package -n nscd
Summary: A Name Service Caching Daemon (nscd)
Group: System/Servers
Conflicts: kernel < 2.2.0
PreReq: shadow-utils
PreReq: %name-pthread = %EVR

%package source
Summary: GNU libc sources
Group: Development/Other
BuildArch: noarch

%description
The GNU C library defines all of the library functions that are specified
by the ISO C standard, as well as additional features specific to POSIX
and other derivatives of the Unix operating system, and extensions
specific to the GNU system.

The GNU libc is a set of standard libraries which are used by multiple
programs on the system.  In order to save disk space and memory, as well
as to make upgrading easier, common system code is kept in one place
and shared between programs.

%description preinstall
This package contains glibc preinstall utility.

%description core
This package contains most essential GNU libc libraries and files,
including dynamic linker and its configurator, standard C library and
the standard math library.  Without these files a GNU/Linux system will
not function.

%description pthread
This package contains glibc libpthread and related shared libraries.

%description locales
This package contains GNU libc locales, files that tell your system
about your language, names of days and months, charset, and other
language/territory/charset specific things.

%description i18ndata
This package contains source files required for building locales.  Locales
are files, that tell your system about your language, names of days and
months, alphabet and other language/territory/charset specific things.

%description gconv-modules
This package contains helper modules necessary to convert data between
various charsets.

%description -n iconv
This package contains program that can convert text files between
various charsets.

%description timezones
This package contains files, utilities and databases for operating
timezones data in the system.

%description utils
This package contains miscellaneous non-essential %name utilities that
didn't fit in specific packages.

%description nss
NSS is a Name Service Switch subsystem.  The basic idea is to put the
implementation of the different services offered to access the databases
in separate modules.

%description -n libnsl1
This package provides the legacy version of libnsl library, for
accessing NIS services.

This library is provided for backwards compatibility only;
applications should use libnsl2 instead to gain IPv6 support.

%description devel
This package contains the header and object files necessary for developing
programs which use the standard C libraries (which are used by nearly all
programs).  If you are developing programs which will use the standard
C libraries, your system needs to have these standard header and object
files available in order to create the executables.

%description devel-static
This package contains the GNU libc static libraries necessary for
developing statically linked programs which use the standard C libraries.

%description doc
This package contains documentation distributed with GNU libc.

%description debug
This package contains utilities for software debugging,
including:
+ memusage
+ memusagestat
+ pcprofiledump
+ xtrace

%description -n nscd
The nscd daemon caches name service lookups and can improve
performance with LDAP, and may help with DNS as well.

%description source
This package contains source code of GNU libc.

%prep
%setup -n %name-%version-%release

find -type f -name configure -print0 |
	xargs -r0 touch --

################################################################################
%build
%define buildtarget build-%_target

%if_without optimization
%define _optlevel %nil
%define optflags_optimization -O%_optlevel %optflags_debug
%else #with optimization

%endif #without optimization

%define _configure_script ../configure

# workaround
unset LD_PRELOAD LD_ASSUME_KERNEL ||:

export CC=%__cc CXX=%__cxx \
	ac_cv_lib_audit_audit_log_avc=no \
	ac_cv_path_BASH_SHELL=/bin/sh \
	ac_cv_path_KSH=/bin/sh \
	#

rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

%configure \
	--disable-crypt \
	--disable-profile \
	--enable-bind-now \
	%{?_enable_multiarch:--enable-multi-arch} \
	--enable-obsolete-rpc \
	--enable-kernel=%enablekernel \
	--enable-tunables \
	--enable-stack-protector=strong \
	#

make %PARALLELMFLAGS

popd #%buildtarget

make -C alt enablekernel=%enablekernel CC=%__cc path_link=../%buildtarget

################################################################################
%install
%makeinstall_std %PARALLELMFLAGS -C %buildtarget

pushd %buildroot%_libdir
%__cc -r -nostdlib -o libpthread.o -Wl,--whole-archive ./libpthread.a
rm libpthread.a
ar rcs libpthread.a libpthread.o
rm libpthread.o
popd

mkdir -p %buildroot%_cachedir/ldconfig
> %buildroot%_cachedir/ldconfig/aux-cache

# Relocate shared libraries used by catchsegv, memusage and xtrace.
mv %buildroot/%_lib/lib{memusage,pcprofile,SegFault}.so \
	%buildroot%_libdir/ ||:

# Relocate libnsl.
mv %buildroot/%_lib/libnsl{-*.so,.so.1} %buildroot%_libdir/

# Install upgrade programs.
make -C alt install

%if_with locales
make -r %PARALLELMFLAGS -j%__nprocs install-locales -C localedata \
	DESTDIR=%buildroot objdir=$PWD/%buildtarget

# Hardlink identical locale files together.
hardlink -vc %buildroot%_prefix/lib/locale

# Convert these locale directories into symlinks.
for n in %renamed_locales; do
	t=%buildroot%_prefix/lib/locale/"${n%%.*}"
	rm -rf "$t"
	ln -s "$n" "$t"
done
%endif #with locales

mkdir -p %buildroot{%_initdir,%_unitdir,/etc/sysconfig,/lib/tmpfiles.d}
install -pm644 alt/nsswitch.conf %buildroot/etc/
install -pm644 nscd/nscd.conf %buildroot/etc/
install -pm755 alt/nscd.init %buildroot%_initdir/nscd
install -pm644 alt/nscd.{service,socket} %buildroot%_unitdir/
install -pm644 alt/nscd.conf %buildroot/lib/tmpfiles.d/
touch %buildroot/etc/sysconfig/nscd
mkdir -pm711 %buildroot/var/{lib,run}/nscd
mksock %buildroot/var/run/nscd/socket
touch %buildroot/var/run/nscd/nscd.pid
touch %buildroot/var/{lib,run}/nscd/{passwd,group,hosts,services}

%ifarch x86_64
install -pm644 alt/stubs-32.h %buildroot%_includedir/gnu/
%endif
%ifarch %ix86
cmp alt/stubs-32.h %buildroot%_includedir/gnu/stubs-32.h || {
	echo 'Bundled stubs-32.h is out of date'
	exit 1
}
%endif

# Install nss.conf
install -pm644 nis/nss %buildroot%_sysconfdir/nss.conf

# Install gai.conf
install -pm644 posix/gai.conf %buildroot%_sysconfdir/

# Install bindresvport.blacklist
install -pm644 alt/bindresvport.blacklist %buildroot%_sysconfdir/

# Include ld.so.conf and ld.so.conf.d
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d
echo 'include /etc/ld.so.conf.d/*.conf' >%buildroot%_sysconfdir/ld.so.conf

# Include %%ghost ld.so.cache
install -pD -m644 /dev/null %buildroot%_sysconfdir/ld.so.cache

# Include gconv-modules.cache
install -pD -m644 /dev/null %buildroot%_gconvdir/gconv-modules.cache

# Create /etc/localtime
touch %buildroot%_sysconfdir/localtime

# zoneinfo now lives in tzdata package.
rm -rf %buildroot%_datadir/zoneinfo

# Remove unpackaged files
rm %buildroot{%_infodir/dir,%_datadir/locale/locale.alias}

# The last bit: more documentation.
%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
cp -pL LICENSES README* alt/README* NEWS \
	%buildroot%docdir/
find %buildroot%docdir/ -type f -size +8k -print0 |
	xargs -r0 xz -9

>devel.files
>devel-static.files
for f in `ls %buildroot%_libdir/lib*.a |
	  grep -v '_p.a$' |
	  sed -e "s|%buildroot||g"`; do
	if [ -e "%buildroot${f%%.a}.so" ] || [ -e "%buildroot${f%%-%basever.a}.so" ]; then
		echo "$f" >>devel-static.files
	else
		echo "$f" >>devel.files
	fi
done

%find_lang libc

%if_with locales
%if_enabled langify
(
	cd %buildroot%_prefix/lib/locale
	for f in *; do
		n=${f%%%%@*}
		n=${n%%%%.*}
		n=${n%%%%_*}
		echo "%%lang($n) %%attr(-,root,root) %_prefix/lib/locale/$f"
	done
) >>libc.lang
%endif #enabled langify

echo '%%dir %_datadir/locale' >>libc.lang
for lang in $((cat alt/locales-add && cd %buildroot%_prefix/lib/locale && ls |sed 's/[.@].*//') |sort -u); do
	for n in $lang ${lang%%%%_*}; do
		mkdir -p "%buildroot%_datadir/locale/$n"/LC_{MESSAGES,TIME}
		echo "%%lang($n) %%dir %_datadir/locale/$n"
		echo "%%lang($n) %%dir %_datadir/locale/$n/LC_MESSAGES"
		echo "%%lang($n) %%dir %_datadir/locale/$n/LC_TIME"
	done
done |sort -u >>libc.lang
%endif #with locales

mkdir -p %buildroot%glibc_sourcedir
cp %SOURCE0 %buildroot%glibc_sourcedir/

%ifarch aarch64
ln -s /lib64/ld-linux-aarch64.so.1 %buildroot/lib/
%endif
%ifarch riscv64
ln -s /lib64/ld-linux-riscv64-lp64d.so.1 %buildroot/lib/
%endif

%brp_strip_debug */%_lib/ld-*.so* */%_lib/libpthread-*.so

# due to libpthread.
%set_verify_elf_method unresolved=relaxed

################################################################################
%check
cat /proc/self/maps >/dev/null
export TIMEOUTFACTOR=10

cat > %buildtarget/xfail.mk <<@@@
export test-xfail-XPG4/unistd.h/linknamespace = yes
export test-xfail-tst-resolv-search=yes
export test-xfail-tst-default-attr=yes
%ifarch x86_64
export test-xfail-test-ildouble=yes
%endif
%ifarch %ix86
export test-xfail-test-double-finite=yes
export test-xfail-test-double=yes
export test-xfail-test-float-finite-y0=yes
export test-xfail-test-float-y0=yes
export test-xfail-test-float32-finite-y0=yes
export test-xfail-test-float32-y0=yes
export test-xfail-test-float64x-clog10=yes
export test-xfail-test-float64x-finite-clog10=yes
export test-xfail-test-float64x-finite-lgamma=yes
export test-xfail-test-float64x-lgamma=yes
export test-xfail-test-idouble=yes
export test-xfail-test-ifloat-y0=yes
export test-xfail-test-ifloat32-y0=yes
export test-xfail-test-ifloat64x-clog10=yes
export test-xfail-test-ifloat64x-lgamma=yes
export test-xfail-test-ildouble-acosh=yes
export test-xfail-test-ildouble-clog10=yes
export test-xfail-test-ildouble-lgamma=yes
export test-xfail-test-ildouble=yes
export test-xfail-test-ldouble-clog10=yes
export test-xfail-test-ldouble-finite-clog10=yes
export test-xfail-test-ldouble-finite-lgamma=yes
export test-xfail-test-ldouble-finite=yes
export test-xfail-test-ldouble-lgamma=yes
export test-xfail-test-ldouble=yes
export test-xfail-tst-malloc-usable-tunables=yes
%endif
%ifarch aarch64
export test-xfail-test-errno-linux=yes
export test-xfail-tst-mlock2=yes
export test-xfail-tst-pkey=yes
export test-xfail-tst-clock2=yes
%endif
%ifarch ppc64le
export test-xfail-tst-pkey=yes
%endif

include Makefile
@@@

ulimit -u $(ulimit -Hu)
make %PARALLELMFLAGS -C %buildtarget -f xfail.mk -k check fast-check=yes LDFLAGS=-Wl,--no-as-needed || {
  rc=$?
  grep '^FAIL:' %buildtarget/tests.sum | cut -d" " -f2- |
    xargs -i tail -v -n 100 %buildtarget/{}.test-result %buildtarget/{}.out ||:
# architectures we care for enough to fail here
%ifarch %ix86 x86_64 aarch64 ppc64le
  exit $rc
%endif
}
cat %buildtarget/tests.sum

%pre core -p /sbin/glibc_preinstall
%post core -p /sbin/glibc_post_upgrade

%post -n iconv
%_sbindir/iconvconfig

%pre locales
for n in %renamed_locales; do
	f="%_prefix/lib/locale/${n%%.*}"
	if [ -d "$f" -a ! -L "$f" ]; then
		rm -rf "$f"
		touch "$f.RPMLOCK"
	fi
done
%if "%_libdir" != "%_prefix/lib"
if [ -L %_prefix/lib/locale ]; then
	rm -f %_prefix/lib/locale
fi
%endif

%post locales
for n in %renamed_locales; do
	d="%_prefix/lib/locale/$n"
	f="%_prefix/lib/locale/${n%%.*}"
	if [ -f "$f.RPMLOCK" -a -d "$f" -a ! -d "$d.RPMSAVE" ]; then
		mv "$d" "$d.RPMSAVE"
		rm -f "$f.RPMLOCK"
	fi
done

%triggerpostun locales -- %name-locales, %name < 6:2.2.4-alt3
for n in %renamed_locales; do
	d="%_prefix/lib/locale/$n"
	if [ -d "$d.RPMSAVE" -a ! -d "$d" ]; then
		mv "$d.RPMSAVE" "$d"
	fi
done

%pre devel
# This used to be a link and it is causing nightmares now.
if [ -L %_includedir/scsi ]; then
	rm -f %_includedir/scsi
fi

%pre -n nscd
/usr/sbin/useradd -M -o -r -u 28 -d / -s /dev/null -c "NSCD Daemon" nscd ||:

%post -n nscd
%post_service nscd

%preun -n nscd
%preun_service nscd

%triggerpostun core -p /sbin/glibc_fix_nsswitch -- %name < 6:2.2.4-alt3, %name-nss < 6:2.2.4-alt4

%files

%files doc
%_infodir/*.info*
%docdir/

%files preinstall
/sbin/glibc_preinstall

%files core
/%_lib/lib*.so*
%exclude /%_lib/lib*thread*.so*
%exclude /%_lib/libanl*.so*
%exclude /%_lib/librt*.so*
/%_lib/ld*.so.*
%ifarch aarch64
/lib/ld-linux-aarch64.so.1
%endif
%ifarch riscv64
/lib/ld-linux-riscv64-lp64d.so.1
%endif
%attr(755,root,root)/%_lib/ld*.so
%exclude /%_lib/libnss_[a-eg-z]*
/sbin/glibc_post_upgrade
/sbin/glibc_fix_*
/sbin/*ldconfig
%ghost %_sysconfdir/ld.so.cache
%dir %_sysconfdir/ld.so.conf.d
%dir %attr(700,root,root) %_cachedir/ldconfig
%ghost %verify(not md5 size mtime) %attr(600,root,root) %config(noreplace,missingok) %_cachedir/ldconfig/aux-cache
%ghost %verify(not md5 size mtime) %attr(644,root,root) %config(noreplace,missingok) %_sysconfdir/localtime
%config(noreplace) %_sysconfdir/bindresvport.blacklist
%config(noreplace) %_sysconfdir/gai.conf
%config(noreplace) %_sysconfdir/ld.so.conf
%config(noreplace) %_sysconfdir/nss.conf
%config(noreplace) %_sysconfdir/nsswitch.conf
%config(noreplace) %_sysconfdir/rpc

%files pthread
/%_lib/lib*thread*.so*
/%_lib/libanl*.so*
/%_lib/librt*.so*

%files nss
/%_lib/libnss_*.so*
%exclude /%_lib/libnss_f*

%files -n libnsl1
%_libdir/libnsl-*.so
%_libdir/libnsl.so.1

%if_with locales
%files locales -f libc.lang
%_bindir/locale*
%dir %_prefix/lib/locale
%if_disabled langify
%_prefix/lib/locale/*
%endif #disabled langify
%endif #with locales

%files gconv-modules
%dir %_gconvdir
%_gconvdir/*.so
%_gconvdir/gconv-modules
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) %_gconvdir/gconv-modules.cache

%files -n iconv
%_bindir/iconv*
%_sbindir/iconv*

%files timezones
%_bindir/tzselect
%_sbindir/zdump
%_sbindir/zic

%files utils
/sbin/sln
%_bindir/*
%exclude %_bindir/iconv*
%exclude %_bindir/locale*
%if_enabled memusagestat
%exclude %_bindir/memusage*
%endif
%exclude %_bindir/pcprofiledump
%exclude %_bindir/tzselect
%exclude %_bindir/xtrace
%_libexecdir/getconf
%_libdir/audit/sotruss-lib.so
%exclude /var/db/Makefile

%files devel -f devel.files
%_libdir/lib*.so
%exclude %_libdir/libnsl-*.so
%exclude %_libdir/libmemusage.so
%exclude %_libdir/libpcprofile.so
%_libdir/*.o
%_includedir/*

%files devel-static -f devel-static.files

%files debug
%if_enabled memusagestat
%_bindir/memusage*
%endif
%_bindir/pcprofiledump
%_bindir/xtrace
%_libdir/libmemusage.so
%_libdir/libpcprofile.so

%files -n nscd
%ghost %config(noreplace,missingok) /etc/sysconfig/nscd
%config(noreplace) %_sysconfdir/nscd.conf
%_initdir/nscd
%_unitdir/nscd.service
%_unitdir/nscd.socket
/lib/tmpfiles.d/nscd.conf
%_sbindir/nscd*
%attr(711,root,root) %dir /var/run/nscd
%attr(666,root,root) %ghost /var/run/nscd/socket
%attr(644,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/run/nscd/nscd.pid
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/run/nscd/passwd
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/run/nscd/group
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/run/nscd/hosts
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/run/nscd/services
%attr(1770,root,nscd) %dir /var/lib/nscd
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/lib/nscd/passwd
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/lib/nscd/group
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/lib/nscd/hosts
%attr(600,root,root) %ghost %config(noreplace,missingok) %verify(not md5 size mtime) /var/lib/nscd/services

%files i18ndata
%_datadir/i18n

%files source
%glibc_sourcedir

%changelog
* Thu Oct 10 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.27-alt11
- Updated to glibc-2.27-141-g5b4f7382af from 2.27 branch.
- Added ld-linux compat symlinks for aarch64 and riscv64.

* Wed Jul 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.27-alt10
- ppc64le:
  + glibc-preinstall: set minimal kernel version to 3.10.0 (current
  arch minimum in libc);
  + Fixed check-abi lists;
  + check: xfailed tst-pkey test.
- check: terminate build only on %%ix86, x86_64, aarch64, and ppc64le.

* Thu Jun 20 2019 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt9
- Updated to glibc-2.27-119-gf056ac8363 from 2.27 branch
  (closes: #36065).

* Sun Jan 06 2019 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt8
- Updated to glibc-2.27-102-g68c2930a56 from 2.27 branch.
- riscv: changed slibdir, rtlddir, libdir, and LD_SO_PREFIX
  (by Nikita Ermakov).

* Tue Nov 27 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt7
- Updated to glibc-2.27-89-g9f433fc791 from 2.27 branch
  (fixes CVE-2018-19591).

* Mon Jun 25 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt6
- The password hashing library, libcrypt, is now provided
  by a separate package.

* Thu Jun 21 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt5
- Updated to glibc-2.27-64-gffc5623 from 2.27 branch.
- Moved libcrypt from glibc-core to a separate subpackage.

* Thu May 10 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt4
- Updated to glibc-2.27-51-gb2dd29a from 2.27 branch.
- glibc_preinstall: rewritten as a regular statically linked executable.

* Mon Mar 12 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt3
- Updated to glibc-2.27-27-gb63daad from 2.27 branch.

* Mon Feb 19 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt2
- Updated to glibc-2.27-14-gb4108a3 from 2.27 branch.
- Fixed build of test suite with gcc7.

* Thu Feb 01 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.27-alt1
- Updated to glibc-2.27.
- Moved legacy libnsl to a separate subpackage.

* Tue Jan 30 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.26.9000.0.1248.407552c-alt1
- Updated to glibc-2.26.9000-1248-g407552c (closes: #26977).
- Switched IDNA implementation to libidn2 (by Florian Weimer;
  fixes: CVE-2016-6261, CVE-2016-6263, CVE-2017-14062).

* Tue Jan 23 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.26.0.131.fabef2e-alt2
- Added workaround needed to execute statically linked binaries on ovz-el
  kernel flavour (ALT#34433).

* Fri Jan 12 2018 Dmitry V. Levin <ldv@altlinux.org> 6:2.26.0.131.fabef2e-alt1
- Updated to glibc-2.26-131-gfabef2e from 2.26 branch
  with assorted backports from master (fixes CVE-2018-1000001).

* Fri Dec 22 2017 Dmitry V. Levin <ldv@altlinux.org> 6:2.26.0.124.98f244e-alt1
- Updated to glibc-2.26-124-g98f244e from 2.26 branch
  with assorted backports from master.
- The minimum Linux kernel version that this version of glibc
  can be used with on x86_64 is 3.2.
- The deprecated NIS(+) name service modules, libnss_nis and libnss_nisplus,
  are not built and packaged by this version of glibc.
- Added a C.UTF-8 locale from Fedora.

* Mon Dec 18 2017 Dmitry V. Levin <ldv@altlinux.org> 6:2.25-alt4
- Updated to glibc-2.25-80-ga8920e6 from 2.25 branch.
- Backported upstream fixes for sw bugs:
  20831 21928 22505 22577 22606 22607 22625 22627.
- Explicitly defined glibc_preinstall entry point (by Gleb F-Malinovskiy).

* Thu Oct 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.25-alt3
- Backported upstream fixes for sw bugs: 21209 21242 21265 21298 21386 21624
  21654 21778 21972 (fixes for CVE-2017-15670 CVE-2017-15804).
- Packaged glibc sources as a separate package.

* Thu Apr 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.25-alt2
- x86_64: moved libm-2.25.a to glibc-devel-static subpackage.
- check: xfailed tst-getrandom test.

* Wed Apr 05 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.25-alt1
- Updated to 2.25 branch.

* Tue Dec 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.24-alt1
- Updated to 2.24 branch with backports from master and fedora.

* Thu Jun 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.23-alt3
- Backported upstream fixes for sw bugs: 19648 19703 19861 20005 20010
  20012 20111 20112 (including fix for CVE-2016-4429).
- Backported upstream implementation of group merging (NSS).

* Tue May 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.23-alt2
- Backported upstream fixes for sw bugs:
  19679, 19758, 19759, 19762, 19791, 19792, 19822, 19879
  (including fixes for CVE-2016-1234, CVE-2016-3075, CVE-2016-3706).

* Fri Feb 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.23-alt1
- Updated to 2.23 branch with backports from master and fedora.

* Tue Dec 08 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 6:2.22-alt1
- Updated to 2.22 branch with backports from master and fedora.

* Wed Jan 15 2014 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt8
- libc.so: link libc.so.6 both before and after libc_nonshared.a,
  to fix spurious undefined reference with --as-needed reported
  in sw#16403.

* Mon Jan 13 2014 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt7
- Backported more upstream fixes, including fixes for sw bugs:
  387, 10278, 12492, 13028, 14286, 14752, 15277, 15308, 15309, 15362,
  15380, 15381, 15618, 15672, 15763, 15859, 15892, 16055, 16274.
- glibc-devel: added /usr/include/gnu/stubs-32.h to provides.

* Sat Jan 11 2014 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt6
- Backported upstream fixes for sw bugs:
  14547, 14699, 15003, 15014, 15073, 15122, 15160, 15234, 15330, 15465,
  15736, 15754, 15759, 15855, 15856, 15857, 15917, 16038, 16072
  (including fixes for CVE-2012-4412, CVE-2012-4424, CVE-2013-4237,
   CVE-2013-4332, CVE-2013-4458, CVE-2013-4788).
- x86_64: packaged /usr/include/gnu/stubs-32.h from x86.

* Tue Apr 09 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt5
- getaddrinfo: updated fix for sw#15339.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt4
- getaddrinfo: backported fixes for sw#15330 and sw#15339.

* Mon Mar 25 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt3
- getaddrinfo: reverted the change that made ECONNREFUSED
  return EAI_SYSTEM instead of EAI_AGAIN.

* Mon Mar 25 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt2
- stdlib.h: Made __secure_getenv prototype available without
  -D_GNU_SOURCE as in older glibc releases.

* Sun Mar 24 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.17-alt1
- Updated to 2.17 branch with backports from master, fedora and
  libc-alpha@.
- glob: changed to use getuid+getpwuid_r instead of
  getlogin_r+getpwnam_r.
- Reexported __secure_getenv while apps are being ported
  to secure_getenv.

* Fri Mar 22 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.16-alt6
- ls.so:
  + enhanced locale-related environment sanitation;
  + fixed locale-related environment sanitation on x86-64.

* Wed Jan 30 2013 Dmitry V. Levin <ldv@altlinux.org> 6:2.16-alt5
- Updated to 2.16 branch with backports from master.

* Sun Sep 30 2012 Dmitry V. Levin <ldv@altlinux.org> 6:2.16-alt4
- Updated to 2.16 branch with backports from master and fedora.

* Mon Sep 03 2012 Dmitry V. Levin <ldv@altlinux.org> 6:2.16-alt3
- nscd: fixed /etc/nscd.conf (closes: #27694).

* Wed Aug 29 2012 Dmitry V. Levin <ldv@altlinux.org> 6:2.16-alt2
- locales/ru_RU: fixed abday (sw#10873) and abmon.
- ru.po: reintroduced fixes from 2.11.3-alt8.
- sys/cdefs.h: fixed support of old compilers (sw#13741, sw#14530).
- glibc_post_upgrade: moved telinit support to 0ldconfig.filetrigger
  (closes: #27666).

* Tue Aug 21 2012 Dmitry V. Levin <ldv@altlinux.org> 6:2.16-alt1
- Updated to 2.16.

* Wed May 16 2012 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt8
- Backported upstream fixes to build with binutils >= 2.21.51.0.3.

* Mon Feb 06 2012 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt7
- Backported upstream fixes for Sourceware#12453 (closes: #26848),
  Sourceware#12350 and Sourceware#12811.

* Fri Aug 12 2011 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt6
- Updated crypt_blowfish to 1.2.
- glibc_preinstall: Fixed handling of kernel versions with zeroes
  (closes: #26029).

* Tue Jun 21 2011 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt5
- Updated to glibc-2.11.3-61-g78856c5 with some broken commits reverted.
- Updated crypt_blowfish to 1.1 (fixes CVE-2011-2483).

* Thu Apr 28 2011 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt4
- Backported upstream fixes for Sourceware#12393,
  Sourceware#12583 (CVE-2011-1659) and Sourceware#12685.
- Fixed nscd reload (closes: #25379).
- glibc-utils: dropped rpcinfo which is now provided by
  rpcbind >= 0.2.1-alt0.4.

* Fri Feb 04 2011 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt3
- Updated to glibc-2.11.3-26-gb72646a.
- Enabled MULTIARCH support on %%ix86 and x86-64.
- Disabled core-debug, nss-debug and devel-debug subpackages.
- Built without -DNDEBUG=1.

* Tue Jan 11 2011 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt2
- Backported updated $ORIGIN hardening from Fedora.
- Backported upstream regex* fixes.

* Tue Nov 30 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.3-alt1
- Updated to glibc-2.11.3.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.2-alt4
- Updated to glibc-2.11.2-15-g0cd8f10.
- Backported $ORIGIN hardening from Fedora.
- Backported fixes for warnings reported by gcc 4.5.

* Mon Oct 11 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.2-alt3
- locales:
  + added ru_RU.IBM866 (closes #23745);
  + changed localedir from %%_libdir to %%_prefix/lib.

* Mon May 31 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.2-alt2
- Updated to glibc-2.11.2-5-g2158096.

* Thu May 20 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.2-alt1
- Updated to glibc-2.11.2.

* Wed Mar 17 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.1-alt4
- nss_nis: Reverted part of commit glibc-2.11-64-ga682a1b
  to fix regression (closes: #23173).
- nsswitch.conf: Disabled nis/nis+ by default.

* Thu Mar 11 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.1-alt3
- Updated to glibc-2.11.1-4-g11c19d3.
- Updated crypt_blowfish to 1.0.4.
- Updated binutils versioned build requirement.

* Wed Jan 13 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.1-alt2
- glibc-core: Added rtld(GNU_UNIQUE) to provides list.

* Fri Jan 08 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.11.1-alt1
- Updated to glibc-2.11.1 + fedora/glibc-2.11.1-1.

* Fri Jan 08 2010 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.2-alt1
- Updated to glibc-2.10.2-1-g313f9d1.

* Tue Oct 27 2009 Kirill A. Shutemov <kas@altlinux.org> 6:2.10.1-alt8
- Fix build with binutils >= 2.20

* Thu Oct 01 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt7
- Added ports support for ARM (by Kirill A. Shutemov).

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt6
- Updated to glibc-2.10.1-69-gaa152ec from
  http://sourceware.org/git/?p=glibc.git;a=shortlog;h=refs/heads/release/2.10/master
- Moved "make check" to %%check section.

* Mon Aug 17 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt5
- Updated to glibc-2.10.1-68-gc87c885 from
  http://sourceware.org/git/?p=glibc.git;a=shortlog;h=refs/heads/release/2.10/master

* Thu Jun 25 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt4
- Updated to glibc-2.10.1-41-gd0f6ed7 from
  http://repo.or.cz/w/glibc/pb-stable.git?a=shortlog;h=glibc-2.10-branch
- locales/ru_UA: Added proper first_weekday and first_workday (closes: #20575).

* Mon Jun 15 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt3
- Updated to glibc-2.10.1-30-g9cf5572 from
  http://repo.or.cz/w/glibc/pb-stable.git?a=shortlog;h=glibc-2.10-branch
- Cherry picked fixes for bits/select.h macros from
  http://sourceware.org/git/?p=glibc.git;a=shortlog;h=master

* Wed Jun 10 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt2
- Updated to glibc-2.10.1-27-ge40d82c from
  http://repo.or.cz/w/glibc/pb-stable.git?a=shortlog;h=glibc-2.10-branch
- Cherry picked several fixes from
  http://sourceware.org/git/?p=glibc.git;a=shortlog;h=master
- Fixed extra PLT calls.
- Removed obsolete %%install_info/%%uninstall_info calls.
- Fixed stripping ld and libpthread on architectures where lib != %%_lib.

* Wed May 13 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.10.1-alt1
- Updated to 2.10.1 release.

* Tue May 05 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.9.90-alt1
- Updated to snapshot 20090427.
- Bumped assumed kernel version to 2.6.18.
- README.ALT: Removed obsolete clause (closes: #19713).

* Mon Apr 20 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.9-alt5
- glibc-doc is no longer required by glibc-devel (closes: #17963).
- Backported fix for__res_maybe_init() from trunk (closes: #19657).

* Mon Mar 02 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.9-alt4
- Imported a few fixes from trunk.
- glibc_fix_post: Moved /etc/localtime update to tzdata %%post (closes: #18786).
- glibc-locales: Packaged more /usr/share/locale/ directories (closes: #19023).
- Built with glibc-kernheaders-2.6.29-alt2.

* Tue Jan 27 2009 Dmitry V. Levin <ldv@altlinux.org> 6:2.9-alt3
- Imported a few fixes from trunk.
- io/ftw.h: Fixed "comma at end of enumerator list" -pedantic-errors
  compilation warnings.
- misc/bits/syslog.h (syslog, vsyslog): Removed "return"
  in functions returning void (fixes -pedantic-errors
  compilation warnings, reported by Slava Semushin).

* Tue Dec 23 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.9-alt2
- Imported a few fixes from trunk (sync with FC glibc-2.9-3).
- iconv: Fixed -r implementation (closes: #18264).

* Tue Nov 18 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.9-alt1
- Updated to 2.9 release.
- Removed obsolete post_ldconfig/postun_ldconfig calls.
- post_ldconfig/postun_ldconfig: Converted to symlinks to ldconfig.
- ldconfig: Changed to exit when executed during rpm package install.

* Fri Nov 07 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.8.90-alt3
- Updated to snapshot 20081103.
- Reintroduced changes to ldconfig search algorithm.
- Changed dynamic linker to call posix_fadvise(2) for shared
  objects (patch from SuSE, updated by ulfr@; closes: #14264).
- Moved libpthread and related shared libraries from glibc-core
  to new glibc-pthread subpackage.
- Packaged glibc-i18ndata subpackage as noarch.
- Moved documentation from glibc and glibc-devel to
  new glibc-doc noarch subpackage.
- Implemented PIE support on ARM (by kas@; closes: sourceware ports/6999).

* Wed Oct 22 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.8.90-alt2
- misc/syslog.c (openlog_internal): Fixed __have_sock_cloexec initialization.

* Mon Oct 20 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.8.90-alt1
- Updated to 2.8.90 (snapshot 20081018).

* Thu Oct 16 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt8
- Moved zoneinfo to tzdata package.

* Thu Sep 18 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt7
- Added postinstall workaround for the /etc/localtime change.
- Removed explicit binary pathname provides.

* Mon Sep 15 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt6
- glibc-core: Changed /etc/localtime to UTC.
- Imported the dynamic-resolvconf patch from Debian (avm@).
- Built with fresh glibc-kernheaders.

* Tue May 13 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt5
- glibc-locales: Packaged more /usr/share/locale/ subdirectories.

* Mon Mar 24 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt4
- glibc_preinstall: Build statically with glibc.
- Applied two ARM fixes (kas@).

* Sun Jan 27 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt3
- Marked %%_gconvdir/gconv-modules as a regular file.
- Marked %%_gconvdir/gconv-modules.cache as a %%ghost file (#14136).
- nscd.conf: Disabled hosts caching by default (#8867).
- Added glibc_fix_ldconfig workaround (#6570).
- Removed redundant glibc_fix_nsswitch proxy to glibc_fix_nsswitch.sh.

* Sun Jan 13 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt2
- elf/dl-version.c (_dl_check_map_versions): Fixed trace mode (#11271).
- Added /proc to build deps, required for test suit.
- Pass --enable-bind-now to debug build as well.

* Fri Jan 11 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5.1-alt1
- Updated to 2.5.1 release.
- Merged fixes from fedora-glibc-2_5-18_1.
- Backported upstream fixes for sourceware bugs:
  3842, 3905, 3996, 4125, 4745, 4773, 4776, 4792,
  4813, 5028, 5043, 5058, 5071, 5103, 5208, 5222.

* Fri Jan 11 2008 Dmitry V. Levin <ldv@altlinux.org> 6:2.5-alt6
- Added arm support (kas@).
- Replaced homebrew linkify with packaged hardlink during build.
- Always include native stubs as before the 2.5-alt5 change (avm@).

* Wed Oct 31 2007 Dmitry V. Levin <ldv@altlinux.org> 6:2.5-alt5
- Nullified stubs.h (avm@).

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 6:2.5-alt4
- Updated to glibc-2_5-branch snapshot 20070112.
- Merged fixes from FC glibc-2.5-10.
- bindresvport.blacklist: Added missing well-known ports (#10706).

* Sat Oct 14 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.5-alt3
- Fixed bashism in ldd as suggested by Han Boetes.
- Fixed russian translation for "Operation not permitted" message.
- Backported few fixes from cvs HEAD.
- Implemented glibc preinstall check.

* Sun Oct 08 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.5-alt2
- Updated to glibc-2_5-branch snapshot 20061006.
- Build with -U_FORTIFY_SOURCE and -fno-stack-protector.
- init.d/nscd: Removed obsolete nscd_nischeck.

* Fri Sep 29 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.5-alt1
- Updated to 2.5 release.
- Reviewed and rediffed patches.
- Bumped assumed kernel version to 2.6.9.
  WARNING: attempts to run dynamically linked software
  with earlier kernels will fail.

* Fri May 26 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt7
- Backported configure.in fix (fixes #9599):
  Compile source test file with -fPIC for -shared.
- Backported x86-64 TLS asm syntax corrections.
- Updated crypt_blowfish to 1.0.2:
  Enable BF_SCALE on x86-64 for better performance.

* Fri May 19 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt6
- Remove __nonnull attribute from ctermid (fixes #9587).

* Tue May 16 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt5
- Fixed "ldd -u" (fixes #9352).
- Applied upstream linuxthreads TLS fix (fixes #8402).
- Fixed invalid weak_alias directive in the crypt patch.

* Sat Mar 11 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt4
- Updated crypt_blowfish to 1.0.1.
- Corrected ldd script (fixes #9065).

* Sun Jan 08 2006 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt3
- Backported upstream patch to fix build with fresh as.
- nscd: Packaged /var/lib/nscd (fixes #7973).
- Enabled TLS support by default.

* Tue Nov 29 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt2
- Reverted glob(3) changes introduced in 2.3.5-alt6.

* Tue Nov 08 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.6-alt1
- Updated to 2.3.6.
- Corrected typos in documentation (fixes #8389).
- Build with --enable-bind-now.

* Mon Sep 05 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt7
- confstr, getconf: Introduced _CS_LIBDIR and _CS_SLIB.
- tt_RU: Fixed territory and description (#7755).

* Wed Aug 10 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt6
- Updated to glibc-2_3-branch snapshot 20050802.
- Applied glob(3) update from gnulib.

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt5
- Synced with Owl: even more changes to the sanitize-env patch:
  corrected the way __libc_enable_secure is set in __libc_init_secure():
  if still undecided at that point, provide safe defaults for
  __libc_enable_secure and __libc_security_mask.
- io/sys/sendfile.h: Removed __nonnull from sendfile and
  sendfile64 declarations.

* Tue May 17 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt4
- Reworked sanitize-env patch again:
  Left __libc_enable_secure a boolean variable.
  Instead, introduced an internal bitmask, __libc_security_mask.

* Sun May 15 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt3
- Reworked sanitize-env patch to take into account AT_SECURE value
  of the auxiliary vector in addition to AT_*ID values.

* Thu May 12 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt2
- Changed _dl_osversion_init(), _dl_non_dynamic_init() and
  dl_main() functions to not assume too old kernel version.

* Mon May 09 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.5-alt1
- Updated to glibc-2_3-branch snapshot 20050427 (2.3.5+).
- Updated patches.
- Raised minimal required kernel version to 2.4.1.
- Reverted incompatible change to glob(3) for a while.
- Applied SuSE changes:
  + fnmatch: If conversion to wide character fails, fall back
    to single byte matching.
  + localedef: Added new option --archive.
  + localedef: Changed default to --no-archive.
- Applied Debian change:
  + ls.so: Aligned rtld_global and rtld_global_ro sizes
    for using i686 optimized library.
- Built with glibc-kernheaders-2.4.25-alt2.

* Tue May 03 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200406160000-alt3
- Additional x86_64 support tweaks (#6531).

* Tue Feb 08 2005 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200406160000-alt2
- Backported upstream fixes:
  + i386/fpu/libm-test-ulps: Update for GCC 3.4.
  + scripts/output-format.sed: Updated.
  * misc/syslog.c: Fix copying of PID in case of out-of-memory situation.
    Always try both UDP and TCP.
  + sys/mount.h: Synced MS_RMT_MASK flag and BLK* ioctls with linux kernel headers.
  + sysdeps/unix/alarm.c: Round return value to nearest.
  + linux/futimes.c: Catch errno values indicating file-name lookup errors.
- Applied SuSE changes:
  + getconf: Added -a option.
  + x86_64/fpu, x86_64/string*, arm/ioperm.c: updated.
- Applied Owl changes:
  + Added rpcgen-cpp patch to avoid hardcoding of path to cpp binary.

* Thu Jun 17 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200406160000-alt1
- Updated to glibc snapshot 200406160000.
- Added README.ALT file.

* Thu Jun 10 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200406101000-alt1
- Updated to glibc snapshot 200406101000.
- sanitize_env patch: Corrected kernel-2.6.x support.
- iconv -r: Fixed.
- memusagestat: fix linkage.
- memusage, xtrace: fix tmp file handling.

* Wed Jun 02 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200406020600-alt1
- Updated to glibc snapshot 200406020600.
- Fixed realpath(3) behaviour.
- Corrected glibc-core package dependencies (#4266).

* Sat May 15 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200405070341-alt1
- Updated sanitize_env patch.
- Rebuilt with binutils-2.15.90.0.3-alt2 and gcc-3.3.3-alt5.

* Fri May 07 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200405070000-alt1
- Updated to glibc snapshot 200405070000.

* Sun May 02 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200404240000-alt4
- ld.so: relax strip method to keep some symbols required for gdb
  to debug shared library initializers (#4069).

* Fri Apr 30 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200404240000-alt3
- nscd:
  + packaged /var/run/nscd;
  + updated rc script (#4049).

* Thu Apr 29 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200404240000-alt2
- _dl_make_stack_executable(): fixed mprotect return code handling.

* Wed Apr 28 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200404240000-alt1
- Updated to glibc snapshot 200404240000.
- ldconfig: reverted symlink handling changes in search_dir().

* Wed Apr 21 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.3.3.200404190147-alt1
- Updated to glibc snapshot 200404190147.
- Reviewed patches.  Updated patches:
  + texinfo docs;
  + linuxthreads docs;
  + gcc -Wpointer-arith support in string2.h;
  + gcc -pedantic support in sys/mount.h;
  + backport of sys/queue.h from OpenBSD;
  + set proper optind when argc < 1;
  + allow tmpfile(3) to use $TMPDIR;
  + fix asprintf/vasprintf error handling;
  + check for asprintf return code;
  + check for potential integer overflow in fread*/fwrite*;
  + vsyslog(3)/syslog(3): don't blindly trust __progname;
  + vsyslog(3)/syslog(3): use ctime_r(3) instead of strftime_r(3).
  + strlcpy(3),strlcat(3): import from OpenBSD;
  + resolv: use improved res_randomid;
  + malloc: sanity check in dlmalloc's unlink() macro;
  + libcrypt: blowfish-crypt support, gensalt interface;
  + iconv: add "--replace" option;
  + adjust kernel version constants to fit ALT kernels;
  + sanitize the environment in a paranoid way;
  + ldconfig: exit during distribution install;
  + support more ru_* locales;
  + relocate helper libraries from /lib to %_libdir;
  + xtrace.sh: change default terminal to xvt;
  + ldd: always execute traced object directly with dynamic linker;
- Package libc 2.0 compatibility add-on in separate subpackage.
- ld.so.conf: include %_sysconfdir/ld.so.conf.d/* by default.
- Package %%ghost %_sysconfdir/ld.so.cache.
- Updated contact address for bug reports.

* Thu Mar 25 2004 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.12
- glibc.spec: explicitly build with gcc3.2.
- glibc.spec: fixed "syntax error in expression" error.
- ldd: removed useless warning message (#3401).
- glibc-devel: updated info-install dependencies (#3544).
- glibc-locales: packaged %_datadir/locale and subdirs (#3498).

* Wed Dec 17 2003 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.11
- Allow tmpfile(3) to use $TMPDIR, as suggested by (GalaxyMaster).
- Sanity check the forward and backward chunk pointers in dlmalloc's
  unlink() macro, thanks to Stefan Esser for the idea (Owl).
- Backported CP1125 support.
- glibc-devel: added dependence on kernel-headers-common (#3199).

* Mon Sep 01 2003 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.10
- Backported from libc-current:
  + getgrouplist fix (CAN-2003-0689);
  + sendfile64 support for linux kernel >= 2.4.
- Fixed CP932 MS Windows Japanese charset support
  (MORIYAMA Masayuki, Alexander Bokovoy).

* Mon Jun 09 2003 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.9
- vsyslog(3): don't pass ident to openlog_internal() at reconnect.
- nscd: rewritten start/stop script to new rc scheme.
- Rebuilt with
  glibc-kernheaders-2.4.21-alt1
  binutils-2.14.90.0.4-alt2
  gcc3.2-3.2.3-alt1

* Thu Apr 24 2003 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.8
- glibc-core: Provides: /sbin/glibc_fix_nsswitch, /sbin/glibc_post_upgrade.

* Sun Mar 23 2003 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.7
- Backported from libc-current:
  + Fix overflows in xdrmem.
  + canonicalize: Check for malloc return value.
  + nice: Use getpriority() for the return value.
  + __pthread_reset_main_thread: Don't muck with RLIMIT_STACK
    in FLOATING_STACKS linuxthreads.

* Fri Nov 08 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.6
- Updated crypt_blowfish to version 0.4.5:
  * Fri Nov 08 2002 Solar Designer <solar@owl.openwall.com>
  - Made the x86 assembly code in crypt_blowfish reentrant
    (this time for real), made crypt_blowfish more careful
    about overwriting sensitive data.
- Cleaned up the default /etc/nsswitch.conf file (Owl).
- Backported from glibc-2.3.2:
  * posix/unistd.h [__USE_GNU] (getresuid, getresgid,
    setresuid, setresgid): Declare them.
- Explicitly use autoconf-2.13 for build.
- libpthread: keep some symbols required for debugging
  threaded applications.
- Removed soname provides from -debug subpackages.

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.5
- Avoid some potential reads beyond end of undersized DNS responses
  by making sure they're at least HFIXEDSZ+QFIXEDSZ in size.
- Fixed -debug subpackages.

* Mon Sep 30 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.4
- Take care of problems caused by res_send and friends returning
  the size of the DNS response (even if that's more than
  the size of the buffer to which it copied the response).

* Tue Sep 24 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.3
- Updated code to snapshot 2002-09-23 of glibc-2-2-branch.
- Reverted previous resolv patch for a while.

* Fri Sep 06 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.2
- resolv (both main and compat): backported from HEAD:
  MAXPACKET: Increase minimum value from 1024 to 65536,
  to avoid buffer overrun.
- Added checks for potential integer overflow in fread*/fwrite*.
- Switched back to default stripping policy:
  make use of new (rpm-build >= 4.0.4-alt3) strip feature.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.6-alt0.1
- Updated code and patches to snapshot 2002-08-27 of glibc-2-2-branch;
  following patches were merged into this branch:
  cvs-20020304-ftime.patch
  cvs-20020320-nis.patch
  cvs-20020404-dirname.patch
  cvs-20020128-20020424-dl_load.patch
  cvs-20020514-semctl.patch
  cvs-20020227-20020506-catgets.patch
  cvs-20020702-libnss_dns.patch
  cvs-20020802-xdr_array.patch
  cvs-20020807-calloc.patch
  2.2.5-alt-linuxthreads-signals.patch
- %_bindir/xtrace: If `TERMINAL_PROG' is not set, set it to `xvt'.
- locale/programs/charmap.c (charmap_read): Don't attempt to access NULL result.
- Don't obsolete old currencies from Euro countries (mdk).
- Fixed i386 ULPs for cacosh() tests.
- Moved (some) static libraries to devel-static subpackage.
- Built with gcc 3.2.1-alt0.2.

* Wed Aug 07 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt12
- malloc/malloc.c (calloc): Also check elem_size != 0 before division.
- Parallelized %%make_install.

* Tue Aug 06 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt11
- Fixed the DNS resolver buffer overflows in glibc-compat code (Tomohiro Kato).
- Check for overflows on multiplication (based on patches from Solar):
  sunrpc/xdr_array.c (xdr_array), malloc/malloc.c (calloc).
- resolv: improved the code used to produce unpredictable DNS query IDs
  to make it generate different sequences of IDs in forked processes
  (problem noted by Jarno Huuskonen), conserve the kernel's randomness
  pool (based on feedback from Michael Tokarev), and properly reseed
  when chrooted (Owl).

* Wed Jul 03 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt10
- resolv/nss_dns/dns-network.c: Reduce linebuflen in parallel
  to bumping up the buffer pointer (Andreas Schwab).
- Adjusted kernel version constants to fit ALT kernels.
  *** BEWARE ***
  supported kernels: 2.2.18-ipl1mdk and higher (LFS is assumed):
  following features assumed to be present:
  + syscalls: {,f}truncate64,mmap2,{,l,f}stat64,fcntl64,getdents64;
  + options: O_DIRECTORY.
  This behaviour is controlled by "altkernel" build option.

* Tue Jun 18 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt9
- glibc-locales:
  + Changed name for interpackage dependencies to %name-locales-virtual.
  + Renamed junior-specific locales to %name-locales-junior.

* Sat Jun 15 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt8
- Refined ldd and glibcbug patches.
- %name-core-%%_target_cpu subpackage:
  + added more libraries;
  + built without i686-specific HP_TIMING support.
- Given libcrypt.so an entry point and made it directly runnable itself.

* Wed Jun 12 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt7
- Fixed malfunction of ldconfig update helpers.
- Changed behaviour: use ctime_r(3) instead of strftime_r(3) in syslog(3)
  so that month names will not depend on current locale settings
  (Michael Tokarev).
- Added %name-core-%%_target_cpu build support: for this package,
  optlevel=3 and assume kernel >= 2.4.1
- Relocated /%_lib/libSegFault.so to %_libdir/libSegFault.so;
  moved it from glibc-core to glibc-utils (only needed by catchsegv).
- Removed from glibc-core-debug: lib{memusage,pcprofile,SegFault}.so

* Sun Jun 09 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt6
- Backported from libc-current:
  + catgets: fix typo in code which uses read to load the catalog;
  + ftime: don't return 1000 in millitm;
  + nis: correctly close the UDP connection;
  + dirname: ignore trailing slashes at end of non-null result;
  + check_fds: make sure newly opened file descriptor has correct number;
  + dl_load: correct __lseek parameters;
  + semctl: only use va_arg if the argument will be used.
- sanitize_env:
  + turned __libc_enable_secure variable into bitmap;
  + changed behaviour: save important variables (only TMPDIR atm.)
    when executing non-suid sgid binaries.
- ldd: execute traced object with help of rtld (fixes #0000842).
- glibcbug script: fixed tmp usage, corrected email and editor settings.
- Build all libraries without debug info. Since now only new subpackages -
  glibc-core-debug, glibc-nss-debug, glibc-devel-debug - will contain
  same libraries built with symbols required for debugging into libc.
- BuildPreReq: rpm-build >= 4.0.4-alt0.3 (because of if/enable logic).

* Mon May 20 2002 Dmitry V. Levin <ldv@altlinux.org> 6:2.2.5-alt5
- Backported from libc-current:
  + catgets: free buffer if internal catalog open fails.
- Langified glibc-locales.

* Mon Apr 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 6:2.2.5-alt4
- linuxthreads/signals.c: added missing check for signal type check.
- Fixed locale renaming problem for upgrade from old glibc (< 6:2.2.4-alt3).

* Sun Mar 31 2002 Dmitry V. Levin <ldv@alt-linux.org> 6:2.2.5-alt3
- Added post_ldconfig/postun_ldconfig.
- Removed call for update chrooted libs from ldconfig
  (use post_ldconfig instead).

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 6:2.2.5-alt2
- Fixed locale renaming problem.
- Fixed glibc-core dependencies (#0000634).
- glibc-core, glibc-i18ndata, glibc-locales, glibc-nss, glibc-gconv-modules, glibc-utils, iconv:
  Conflicts: %name < %%epoch:%%version-%%release.

* Tue Feb 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 6:2.2.5-alt1
- 2.2.5, redone patches.
- Corrected package requires.
- Relocated %_bindir/{ldd,glibcbug} from %name-core to %name-utils.
- Updated sanitize-env patch.
- Changed ru_RU, ru_UA and uk_UA.KOI8-U locales to symlinks to real locales.
- Backported from current branch:
  + ALT Security Team's patches for asprintf and realloc issues;
  + elf/dl-load.c (_dl_map_object): Remove incorrect optimization for SHARED code.
- Merged in Owl patches for syslog and resolv.

* Wed Dec 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 6:2.2.4-alt5
- Updated code and patches to CVS 20010925.
- Updated c_stub, glibc-compat and diff-CYGNUS-to-REDHAT.patch to 2.2.4-19 (rhs).
- Fixed asprintf/vasprintf error handling.
- Added strclcpy and strlcat from OpenBSD.

* Tue Nov 27 2001 Dmitry V. Levin <ldv@alt-linux.org> 6:2.2.4-alt4
- nss: moved libnss_files-2.2.4.so, libnss_files.so.2 and nsswitch.conf to core subpackage.
- nsswitch.conf: added initial nss_tcb support.
- gconv-modules: Included gconv-modules.cache
- iconv: execute iconvconfig in %post.
- i18ndata: enabled compressed charmaps.
- locales: hardlink identical locale files together (jj).
- librt.so: turn into linker script (jj).

* Fri Aug 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.4-alt3
- Split glibc into several packages (nidd):
  + glibc-core
  + glibc-i18ndata
  + glibc-locales
  + glibc-nss
  + glibc-gconv-modules
  + iconv

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.4-alt2
- Updated RH patch (from 2.2.4-5).
- Added %_sbindir/iconvconfig.

* Thu Aug 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.4-alt1
- 2.2.4
- Sanitize the environment in a paranoid way (Solar idea).

* Wed Aug 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.4-alt0.1pre3
- 2.2.4pre3.
- Re-enabled MBS_SUPPORT.

* Sat Jun 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.2-ipl7mdk
- Patch from Solar Designer <solar@owl.openwall.com>:
    Sync the fts(3) routines with current OpenBSD and FreeBSD; this is
    triggered by Nick Cleaton's report of yet another FTS vulnerability
    to FreeBSD, and a discussion with Kris Kennaway and Todd Miller. It
    should no longer be possible to trick FTS into leaving the intended
    directory hierarchy, but DoS attacks on FTS itself remain possible.
- Added sgi_fam entry to /etc/rpc.

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.2-ipl6mdk
- Resurrected %%optflags_debug options for compiler.
- Fixed devel/debug requires and obsoletes tags.

* Mon May 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.2-ipl5mdk
- Split out utilities and libraries for debugging into %name-debug subpackage.
- Updated crypt_blowfish to version 0.4.

* Sun Mar 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.2.2-ipl4mdk
- Fixed typo in sys/mount.h
- Built for release.

* Sat Mar 10 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.2-ipl3mdk
- Updated 18n patch.
- Make ldconfig exit during distribution install.

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.2-ipl2mdk
- Fixed optind handling.

* Sun Feb 18 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.2-ipl1mdk
- 2.2.2 release.
- Disable MBS_SUPPORT.

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.1-ipl2mdk
- Updated RH patch.
- Resurrected glibc-2.0 compatibility support (jj).
- Upgraded sys/queue.h
- ldconfig: call for update chrooted libs.
- Fixed pthread_create manpage (mdk).
- Fixed string2.h (libs-alpha).
- Added more info entries.

* Sun Jan 14 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.1-ipl1mdk
- 2.2.1 release.

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.1-ipl0.3mdk
- 2.2.1pre2.
- Export gensalt, UFC-crypt and MD5-crypt interface (libcrypt).
- Added Requires tags for all subpackages.

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.1-ipl0.2mdk
- Export MD5 interface (libcrypt).
- Added blowfish-crypt support (libcrypt)
  (we use crypt_blowfish-0.3 from Solar Designer <solar@false.com>).

* Mon Jan 08 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.1-ipl0.1mdk
- 2.2.1pre1.
- Reconstructed RH specific patch.
- Dropped libNoVersion support.
- Dropped glibc-2.0 compatibility support for a while
  (wait for RH port to 2.2.1).

* Sat Dec 23 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl5mdk
- More fixes and updates from CVS (see ChangeLog for details).
- Forced strip_method to "executable" only.
- Updated localedef patch (change build behavior to break on signals).

* Sat Dec 16 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl4mdk
- Added uk_UA.CP1251 into the list of supported charsets.
- Added few patches from glibc-alpha.

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl3mdk
- More fixes from CVS (see ChangeLog for details).
- Relocated shared libraries used by memusage and xtrace,
  from /lib to %%_libdir.
- Moved to devel subpackage:
  %%_bindir/{memusage*,pcprofiledump,xtrace},
  %%_libdir/{libmemusage,libpcprofile}.so

* Wed Nov 15 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl2mdk
- Updated locale patch.
- Fixed texinfo documentation.
- FHSified paths.h
- Added "--replace" option to iconv utility.

* Fri Nov 10 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl1mdk
- 2.2
- Fixed ldconfig.

* Wed Nov 08 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.97-ipl1mdk
- 2.1.97
- Various patches from glibc-alpha.

* Sat Oct 28 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.96-ipl1mdk
- 2.1.96.

* Mon Oct 23 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.95-ipl2mdk
- Added forgotten /%_lib/lib{memusage,pcprofile,SegFault}.so files.
- Updated Obsoletes/Provides tags for locales.

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.95-ipl1mdk
- 2.1.95.
- Compatibility: revert back to uncompressed charmaps.

* Fri Oct 06 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.94-ipl3mdk
- Merge patches from 2.1.94 RH release #3.
- Updated %post section.

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.94-ipl2mdk
- Rebuilt with gcc-2.96.
- Added compat-glibc (for 2.0) lost in previous release.
- Updated nscd init script.
- Updated RE locale patch from AEN:
  Added kk_KZ and ky_KG locales (Kazakhstan and Kirghizia).

* Wed Sep 20 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.94-ipl1mdk
- 2.1.94 release.

* Mon Sep 04 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.92-ipl0.3mdk
- Revert back to old-style install-locales technique.
- Merge in patches from Jakub Jelinek <jakub@redhat.com>:
  + nss/nss_files/files-hosts.c (HOST_DB_LOOKUP): Increment counter in the loop.
  + g++ 2.95.2 chokes on wrong sys/time.h

* Wed Aug 30 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.92-ipl0.2mdk
- 2.1.92 snapshot 13.
- Merge in RH patches:
  + Sun Aug 27 2000 Matt Wilson <msw@redhat.com>
    Patch to determine invalide locale name from Ulrich.
  + Sun Aug 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
    Fix up sys/io.h

* Mon Aug 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.92-ipl0.1mdk
- RE adaptions.
- Added PT154 locale (from AEN <aen@logic.ru>).
- 2.1.92 snapshot 5.

* Wed Aug  9 2000 Jakub Jelinek <jakub@redhat.com>
- build from CVS archive
