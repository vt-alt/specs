%define php7_sapi cli
%add_findreq_skiplist %_usrsrc/php7-devel/*

%ifarch %mips
%add_optflags -DSLJIT_IS_FPU_AVAILABLE=0
%endif

Summary: The PHP7 scripting language
Name:	 php7
Version: 7.3.15
Release: alt1

%define php7_name      %name
%define _php7_version  %version
%define _php7_major  7.3
%define php7_release   %release
%define rpm_build_version %_php7_version

License: PHP-3.01
Group:	 Development/Other
Url: http://www.php.net/
#Git: http://git.php.net/repository/php-src.git

Source0: php7-source.tar
Source1: phpver.rpm.macros.standalone
Source2: php-packaging.readme
Source3: php.ini
Source4: phpinfo.tar

Patch1: php-version.patch
Patch2: php-shared-1.patch
Patch3: php-cli-build.patch
Patch4: php-test-pcntl.patch
Patch5: php-5.3.3-sapi-scandir.patch
Patch6: php-devel-scripts-alternatives.patch
Patch7: php-7.1.0-dlopen.patch
Patch8: php-4.3.11-libtool.patch
Patch9: php-5.2.5-norpath.patch
Patch10: php-5.1.0b1-cxx.patch
Patch11: php-no-static-program.patch
Patch12: php-set-session-save-path.patch
Patch13: php7-7.1.10-alt-lsattr.patch
Patch14: php-7.2.12-acinclude.patch
Patch15: php7-7.2.21-alt-e2k-lcc123.patch
Patch16: php5-5.5.9-phar-phppath.patch
Patch17: php-mysqlnd-socket.patch
Patch18: php-7.2.14-alt-zend-signal-visibility.patch
Patch19: php-7.2-alt-phar-manfile-suffix.patch
Patch20: php7-7.1.0-phpize.patch
Patch21: php7-7.3-alt-tests-fix.patch
Patch22: php7-7.3.10-alt-e2k-lcc123.patch

Patch70: php7-debian-Add-support-for-use-of-the-system-timezone-database.patch
Patch71: php7-debian-Use-system-timezone.patch

PreReq:  php7-libs = %version-%release
Provides: php-engine = %version-%release
Provides: %name = %rpm_build_version-%release

BuildRequires: chrpath libmm-devel libxml2-devel ssmtp termutils zlib-devel re2c bison alternatives

# for tests
BuildRequires: /proc

BuildRequires(pre): rpm-build-php7 rpm-macros-alternatives
BuildRequires(pre): rpm-build-ubt

BuildRequires: libtool_1.5 chrpath
%set_libtool_version 1.5

%description
PHP7 is a widely-used general-purpose scripting language that is
especially suited for Web development and can be embedded into HTML.
The most common use of PHP coding is probably as a replacement
for CGI scripts.

%package -n rpm-build-php7-version
Summary:	RPM helper macros to rebuild PHP7 packages

Group:		Development/Other
License:	GPLv3
BuildArch:	noarch

%description -n rpm-build-php7-version
These helper macros provide possibility to rebuild
PHP7 packages by some Alt Linux Team Policy compatible way.

%package mysqlnd
Group: System/Servers
Summary: Native PHP driver for MySQL
Requires: php7 = %rpm_build_version-%php7_release
Provides: %name-mysqlnd = %rpm_build_version-%php7_release

%description mysqlnd
Native PHP driver for MySQL

%package devel
Group: Development/C
Summary: Development package for PHP7

Requires: php7-libs = %version-%release
Requires: rpm-build-php7
Requires: rpm-build-php7-version = %version-%release
# for phpize
Requires: libtool, autoconf, automake

Provides: php-devel
Provides: %name-devel = %rpm_build_version-%release
Provides: php-engine-devel = %version-%release

%description devel
The php7-devel package lets you compile dynamic extensions to PHP7.
Instead of recompiling the whole php binary, install this package
and use the new self-contained extensions support. For more information,
read the file SELF-CONTAINED-EXTENSIONS.

%package libs
Group: Development/C
Summary: Package with common data for various PHP7 packages
Requires: php-base >= 2.5

Provides: php7-bcmath = %php7_version-%php7_release
Provides: php7-ctype = %php7_version-%php7_release
Provides: php7-date = %php7_version-%php7_release
Provides: php7-filter = %php7_version-%php7_release
Provides: php7-ftp = %php7_version-%php7_release
Provides: php7-gettext = %php7_version-%php7_release
Provides: php7-hash = %php7_version-%php7_release
Provides: php7-iconv = %php7_version-%php7_release
Provides: php7-json = %php7_version-%php7_release
Provides: php7-libxml = %php7_version-%php7_release
Provides: php7-mhash = %php7_version-%php7_release
Provides: php7-pcre = %php7_version-%php7_release
Provides: php7-posix = %php7_version-%php7_release
Provides: php7-reflection = %php7_version-%php7_release
Provides: php7-session = %php7_version-%php7_release
Provides: php7-shmop = %php7_version-%php7_release
Provides: php7-simplexml = %php7_version-%php7_release
Provides: php7-spl = %php7_version-%php7_release
Provides: php7-standard = %php7_version-%php7_release
Provides: php7-sysvmsg = %php7_version-%php7_release
Provides: php7-sysvsem = %php7_version-%php7_release
Provides: php7-sysvshm = %php7_version-%php7_release
Provides: php7-tokenizer = %php7_version-%php7_release
Provides: php7-wddx = %php7_version-%php7_release
Provides: php7-xml = %php7_version-%php7_release
Provides: php7-dom = %php7_version-%php7_release
Provides: php7-xmlwriter = %php7_version-%php7_release
Provides: php7-zlib = %php7_version-%php7_release
Provides: php7-libs = %php7_version-%release


Obsoletes: php7-simplexml php7-mhash
Obsoletes: php7-dom < %EVR

%description libs
The php7-libs package contains parts of PHP7 distribution which are
in use by other PHP7-related packages.

%prep
%setup -q -n php7-source
%setup -q -n php7-source -T -D -a4
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p1
%patch5 -p1 -b .scandir
%patch6 -p2 -b .alternatives
%patch7 -p0
%patch8 -p0
%patch9 -p2
%patch10 -p2
%patch11 -p2
%patch12 -p2
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%ifarch %e2k
%patch22 -p1
%endif
%patch70 -p1
%patch71 -p1


mv README.SELF-CONTAINED-EXTENSIONS SELF-CONTAINED-EXTENSIONS

cp -dpR %SOURCE2 .

LIBS="$LIBS -lpthread"
CFLAGS="%optflags -fPIC"
export LIBS CFLAGS

subst "s,./vcsclean,," build/buildcheck.sh
subst "s,./stamp=$,," build/buildcheck.sh
# symbols visibility fix
sed -is 's,\(zend_module_entry \)\(.*= {\),zend_module_entry __attribute__ ((visibility("default"))) \2,;' ext/*/*.c

%build
%autoreconf -I build
./buildconf --force

%php7_env

%configure \
	--prefix=%_prefix \
	--program-suffix=7 \
	--localstatedir=%_var \
	--enable-inline-optimization \
	--with-config-file-path=%php7_sysconfdir/ \
	--with-config-file-scan-dir=%php7_sysconfdir/%php7_sapi/php.d/ \
	--with-pic \
	\
	--enable-cli \
	--disable-cgi \
	\
	--disable-debug \
	--enable-safe-mode \
	--disable-magic-quotes \
	--disable-rpath \
	\
	--enable-bcmath \
	--enable-ctype \
	--enable-ftp \
	--enable-session \
	--enable-shmop \
	--enable-sysvsem \
	--enable-sysvshm \
	--enable-sysvmsg \
	--enable-libxml \
	--enable-dom \
	--disable-opcache \
	--enable-simplexml \
	--disable-pdo \
	--enable-hash \
	--enable-xml \
	--enable-wddx \
	--disable-fileinfo \
	--disable-xmlreader \
	--enable-shared=yes \
	--enable-static=no \
	\
	--with-layout=GNU \
	--with-exec-dir=%_bindir \
	--with-zlib=%_usr \
	--with-gettext=%_usr \
	--with-iconv \
	--enable-mysqlnd=shared \
	--without-mysql \
	--without-openssl \
	--with-mm=%_usr \
	--without-sqlite \
	--with-regex=php \
	--without-pear \
	%ifarch %e2k
	--without-pcre-jit \
	%endif
#
%php7_make

%install
%php7_make_install

# All things already installed, install differences only
mkdir -p \
	%buildroot/%php7_libdir/extensions \
	%buildroot/%_bindir \
	%buildroot/%php7_sysconfdir/%php7_sapi/php.d \
	%buildroot/%php7_extconf \
	%buildroot/%php7_servicedir/%php7_sapi \
	%buildroot/%_datadir/php/%_php7_version/modules

install -m 644 %SOURCE3                      %buildroot/%php7_sysconfdir/%php7_sapi/php.ini

for f in \
  %buildroot/%php7_sysconfdir/%php7_sapi/php.ini
do
  subst 's,@PHP_MAJOR@,%_php7_major,g' "$f"
  subst 's,@PHP_VERSION@,%_php7_version,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@SAPI@,%php7_sapi,g' "$f"
done

[ -f "%buildroot/%_bindir/phpextdist" ] || 
    cp -dpR scripts/dev/phpextdist %buildroot/%_bindir/

chmod 755 %buildroot/%_bindir/*

# This file is not needed by any program.
rm -f %buildroot/%_libdir/libphp-%_php7_version.la

# Remove RPATH
/usr/bin/chrpath --delete %buildroot/%_bindir/php7-%_php7_version
/usr/bin/chrpath --delete %buildroot/%_bindir/phpinfo7-%_php7_version

# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(printf %%s "%_php7_version" | sed 's,[^[:digit:]],,g')0"

cat << EOF > %buildroot/%_altdir/php7
%_bindir/phar		%_bindir/phar7.phar	$php_weight
%_bindir/phpdbg		%_bindir/phpdbg7	$php_weight
%_bindir/php	%_bindir/php7-%_php7_version	$php_weight
%_bindir/php7	%_bindir/php7-%_php7_version	$php_weight
%_man1dir/php7.2	%_man1dir/php-%_php7_version.1	$php_weight
EOF

cat << EOF > %buildroot/%_altdir/php7-devel
%_bindir/phpize		%_bindir/phpize7	$php_weight
%_bindir/php-config	%_bindir/php-config7	$php_weight
EOF

# Make backup some files to make devel package.
%make clean

mkdir -p %buildroot%_usrsrc/php7-devel/{ext,sapi,main,conf}
cp -dpR php.ini* %buildroot%_usrsrc/php7-devel/conf
cp -dpR ext/*    %buildroot%_usrsrc/php7-devel/ext
cp -dpR sapi/*   %buildroot%_usrsrc/php7-devel/sapi

# Add necessary files to build any sapi packages.
mkdir -p %buildroot%_usrsrc/php7-devel/sapi/BUILD
cp -dpR main/{internal_functions.c,fastcgi.c} %buildroot%_usrsrc/php7-devel/sapi/BUILD
cp -dpR include                   %buildroot%_usrsrc/php7-devel/sapi/BUILD

# install headers for PDO subpackages
install -m644 -D ext/pdo/php_pdo.h %buildroot%_includedir/php/%_php7_version/ext/pdo/php_pdo.h
install -m644 -D ext/pdo/php_pdo_driver.h %buildroot%_includedir/php/%_php7_version/ext/pdo/php_pdo_driver.h
install -m644 -D ext/pdo/php_pdo_error.h %buildroot%_includedir/php/%_php7_version/ext/pdo/php_pdo_error.h

# install headers for mysqlnd subpackages
install -m644 -D ext/mysqlnd/mysqlnd.h %buildroot%_includedir/php/%_php7_version/ext/mysqlnd/mysqlnd.h
install -m644 -D ext/mysqlnd/mysqlnd_portability.h %buildroot%_includedir/php/%_php7_version/ext/mysqlnd/mysqlnd_portability.h
install -m644 -D ext/mysqlnd/mysqlnd_enum_n_def.h %buildroot%_includedir/php/%_php7_version/ext/mysqlnd/mysqlnd_enum_n_def.h
install -m644 -D ext/mysqlnd/mysqlnd_structs.h %buildroot%_includedir/php/%_php7_version/ext/mysqlnd/mysqlnd_structs.h

mkdir -p %buildroot/%php7_extconf/mysqlnd
echo "file_ini=01_mysqlnd.ini" >%buildroot/%php7_extconf/mysqlnd/params
echo "extension=mysqlnd.so" >%buildroot/%php7_extconf/mysqlnd/config

# install correct phar
mv %buildroot%_bindir/phar.phar %buildroot%_bindir/phar7.phar
ln -sf phar7.phar %buildroot%_bindir/phar7
sed -i -s 's,%buildroot,,' %buildroot%_bindir/phar7.phar

# rpm macros 
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
cp %SOURCE1 %buildroot/%_sysconfdir/rpm/macros.d/%php7_name-ver



subst 's,@php7_name@,%php7_name,'           %buildroot/%_sysconfdir/rpm/macros.d/%php7_name-ver
subst 's,@_php7_version@,%_php7_version,'   %buildroot/%_sysconfdir/rpm/macros.d/%php7_name-ver
subst 's,@php7_major@,%_php7_major,'   %buildroot/%_sysconfdir/rpm/macros.d/%php7_name-ver
subst 's,@php7_release@,%php7_release,'     %buildroot/%_sysconfdir/rpm/macros.d/%php7_name-ver
subst 's,sbin/lsattr,bin/lsattr,' %buildroot/%php7_libdir/build/config.guess
mkdir -p  %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/%name.filetrigger << EOF
#!/bin/sh
LC_ALL=C egrep -qs '^%php7_extdir' || exit 0
if [ -x %php7_postin ]; then
    export php_servicedir=%php7_servicedir
    export php_sysconfdir=%php7_sysconfdir
    export php_extconf=%php7_extconf
    export sapiList=cli
    %php7_postin ||:
fi
EOF
chmod 755 %buildroot/%_rpmlibdir/%name.filetrigger

%check
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1
export SKIP_ONLINE_TESTS=1
export SKIP_IO_CAPTURE_TESTS=1
# the test always fails when run in the building tree
rm -f tests/basic/bug54514.phpt
# the test fails due to an error in glibc-2.27 packaged for ALT: https://bugzilla.altlinux.org/show_bug.cgi?id=37368
rm -f ext/standard/tests/strings/setlocale_variation2.phpt

if ! make test; then
  set +x
  for f in $(find .. -name \*.diff -type f -print); do
    if ! grep -q XFAIL "${f/.diff/.phpt}"
    then
      echo "TEST FAILURE: $f --"
      cat "$f"
      echo -e "\n-- $f result ends."
    fi
  done
  set -x
# tests contain errors that fail on other architectures 
%ifarch x86_64
  exit 1
%endif
fi
unset NO_INTERACTION REPORT_EXIT_STATUS 

%post
%php7_sapi_postin

%preun
%php7_sapi_preun

%define		php7_extension	mysqlnd

%post mysqlnd
%php7_extension_postin

%preun mysqlnd
%php7_extension_preun

%files
%_altdir/php7
%_bindir/phpdbg7
%_bindir/php7-%_php7_version
%_bindir/phar7*
%_bindir/phpinfo7-%_php7_version
%dir %php7_sysconfdir/%php7_sapi
%dir %php7_sysconfdir/%php7_sapi/php.d
%config(noreplace) %php7_sysconfdir/%php7_sapi/php.ini
%_man1dir/php7-%_php7_version.1*
%_man1dir/php7.*
%_man1dir/phpdbg7.*
%_man1dir/phar7*.1*
%_rpmlibdir/%name.filetrigger
%doc CODING_STANDARDS CREDITS INSTALL LICENSE
%doc NEWS README.* php.ini-* EXTENSIONS
%doc UPGRADING*

%files -n rpm-build-php7-version
%_sysconfdir/rpm/macros.d/%php7_name-ver

%files libs
%dir %php7_sysconfdir
%php7_libdir
%php7_datadir
%exclude %php7_extdir/mysqlnd*
%exclude %php7_extconf/mysqlnd
%_libdir/libphp-%_php7_version.so*
%exclude %php7_libdir/build
%exclude %php7_servicedir/cli

%files mysqlnd
%php7_extdir/mysqlnd*.so
%php7_extconf/mysqlnd/*

%files devel
%_bindir/php-config7
%_bindir/phpize7
%_bindir/phpextdist
%_includedir/php
%php7_libdir/build
%_altdir/php7-devel
%_libdir/libphp-%_php7_version.a
%_usrsrc/php7-devel
%_man1dir/php-config7.*
%_man1dir/phpize7.*
%doc SELF-CONTAINED-EXTENSIONS php-packaging.readme
%doc tests run-tests.php 

%changelog
* Thu Feb 20 2020 Anton Farygin <rider@altlinux.ru> 7.3.15-alt1
- 7.3.15 (Fixes: CVE-2020-7063, CVE-2020-7062, CVE-2020-7061)

* Tue Feb 04 2020 Anton Farygin <rider@altlinux.ru> 7.3.14-alt1
- 7.3.14 (Fixes: CVE-2020-7060, CVE-2020-7059)

* Fri Dec 20 2019 Anton Farygin <rider@altlinux.ru> 7.3.13-alt1
- 7.3.13. (Fixes: CVE-2019-11046, CVE-2019-11045, CVE-2019-11049,
	          CVE-2019-11050, CVE-2019-11047)

* Mon Nov 25 2019 Anton Farygin <rider@altlinux.ru> 7.3.12-alt1
- 7.3.12

* Tue Nov 19 2019 Anton Farygin <rider@altlinux.ru> 7.3.11-alt1
- 7.3.11 (fixes: CVE-2019-11043)

* Tue Nov 19 2019 Michael Shigorin <mike@altlinux.org> 7.3.10-alt2
- E2K: lcc support updates: drop 1.21, fix 1.23 (mcst#4061)

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 7.3.10-alt1
- 7.3.10
- enabled upstream tests
- enabled dom module

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 7.3.9-alt1
- 7.3.9

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 7.2.23-alt1
- 7.2.23

* Wed Sep 04 2019 Anton Farygin <rider@altlinux.ru> 7.2.22-alt1
- 7.2.22

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 7.2.21-alt1
- 7.2.21 (Fixes: CVE-2019-11042, CVE-2019-11041)

* Thu Jul 11 2019 Michael Shigorin <mike@altlinux.org> 7.2.19-alt1.1
- move autoreconf from %%prep to %%build

* Sat Jun 01 2019 Anton Farygin <rider@altlinux.ru> 7.2.19-alt1
- 7.2.19 (fixes: CVE-2019-11040)
- fixed build on mipsel by iv@

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 7.2.18-alt1
- 7.2.18

* Tue Apr 09 2019 Anton Farygin <rider@altlinux.ru> 7.2.17-alt1
- 7.2.17

* Mon Mar 11 2019 Anton Farygin <rider@altlinux.ru> 7.2.16-alt1
- 7.2.16

* Thu Feb 14 2019 Anton Farygin <rider@altlinux.ru> 7.2.15-alt1
- 7.2.15

* Tue Jan 15 2019 Anton Farygin <rider@altlinux.ru> 7.2.14-alt1
- 7.2.14 (fixes: CVE-2018-19935)
- removed the .a archive from php7-mysqlnd package (closes: #34521)
- E2K: worked around the lack of gcc5's builtins in lcc-1.23 (closes: #35856)

* Fri Dec 14 2018 Anton Farygin <rider@altlinux.ru> 7.2.13-alt1
- 7.2.13
- added filetrigger for cli sapi and it's modules

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 7.2.12-alt1
- 7.2.12
- added patches from debian for using the default system timezone (closes: #34771)

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 7.2.11-alt1
- 7.2.11

* Wed Sep 26 2018 Michael Shigorin <mike@altlinux.org> 7.2.10-alt2
- E2K: explicitly link with -lcxa

* Fri Sep 21 2018 Anton Farygin <rider@altlinux.ru> 7.2.10-alt1
- 7.2.10

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 7.2.9-alt1
- 7.2.9

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 7.2.8-alt1
- 7.2.8 with fixes for multiple security issues

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 7.2.6-alt1
- 7.2.6

* Fri May 11 2018 Anton Farygin <rider@altlinux.ru> 7.2.5-alt1
- 7.2.5

* Wed Feb 07 2018 Anton Farygin <rider@altlinux.ru> 7.1.14-alt1
- 7.1.14

* Sun Dec 10 2017 Anton Farygin <rider@altlinux.ru> 7.1.12-alt1
- 7.1.12

* Fri Nov 03 2017 Anton Farygin <rider@altlinux.ru> 7.1.11-alt1
- 7.1.11 (Fixes: CVE-2016-1283)

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 7.1.10-alt1
- 7.1.10

* Tue Sep 19 2017 Anton Farygin <rider@altlinux.ru> 7.1.9-alt1
- 7.1.9

* Fri Aug 04 2017 Anton Farygin <rider@altlinux.ru> 7.1.8-alt1
- new version

* Fri Jul 07 2017 Anton Farygin <rider@altlinux.ru> 7.1.7-alt1
- new version

* Sun Jun 11 2017 Anton Farygin <rider@altlinux.ru> 7.1.6-alt1
- new version

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 7.1.5-alt1
- new version

* Thu Apr 27 2017 Anton Farygin <rider@altlinux.ru> 7.1.4-alt1
- new version

* Sat Mar 18 2017 Anton Farygin <rider@altlinux.ru> 7.1.3-alt1
- new version

* Wed Feb 01 2017 Anton Farygin <rider@altlinux.ru> 7.1.1-alt1
- new version

* Wed Dec 7 2016 Anton Farygin <rider@altlinux.ru> 7.1.0-alt1
- build PHP-7.1 for ALT
