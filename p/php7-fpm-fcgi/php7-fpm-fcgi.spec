%define php7_sapi fpm-fcgi

Name: php7-fpm-fcgi
Version: %php7_version
Release: %php7_release.1
Summary: The PHP7 HTML-embedded scripting language as a php-fpm (FastCGI) binary.
Group: System/Servers
Url: http://www.php.net/
License: PHP-3.01

Requires: php7 = %php7_version
Requires: php7 >= %php7_version-%php7_release
Provides: php-engine = %php7_version-%php7_release
Requires: service >= 0.5.26-alt1

Source1: php.ini
Source2: %name-browscap.ini
Source3: php7-fpm.init
Source4: php7-fpm.logrotate
Source5: php7-fpm.service
Source6: php7-fpm.rotate

Patch0: php5-fpm-fcgi-5.3.3.20100722-config.m4.patch
Patch1: php7-fpm-fcgi-7.1.0-build.patch
Patch2: php7-fpm-fcgi-7.1.0-config.patch
Patch3: php7-fpm-fcgi-7.1.0-setproctitle.patch

BuildRequires(pre): rpm-build-php7 rpm-macros-apache
BuildRequires:	php7-devel = %php7_version

BuildRequires: libevent-devel

%description
PHP is an HTML-embedded scripting language.  PHP attempts to make it
easy for developers to write dynamically generated web pages.  PHP
also offers built-in database integration for several commercial
and non-commercial database management systems, so writing a
database-enabled web page with PHP is fairly simple.  The most
common use of PHP coding is probably as a replacement for CGI
scripts.  
Using PHP as a CGI binary is an option for setups that for some reason 
do not wish to integrate PHP as a module into server software (like Apache), 
or will use PHP with different kinds of CGI wrappers to create safe 
chroot and setuid environments for scripts. 
This setup usually involves installing executable PHP binary to the 
web server cgi-bin directory. CERT advisory CA-96.11 recommends 
against placing any interpreters into cgi-bin.

%prep
%setup -T -c
%php7_sapi_prepare fpm
ln -s %php7_extsrcdir ext


%patch0 -p1
%patch1 -p1 -b .a
%patch2 -p1
%patch3 -p1

%build
%add_optflags -DHAVE_CLEARENV

# some hackaround
mkdir -p sapi modules
ln -s ../ sapi/fpm
touch modules/z

FPM_BUILD_VARS=" \
    PHP_SAPI=default \
    PHP_MODULES=sapi/fpm/php-fpm \
    SAPI_FPM_PATH=sapi/fpm/php7-fpm \
    BUILD_DIR=. \
"
# add fastcgi.c to source files for php-fpm
sed -si '/fpm\/fpm\.c/a\\tfastcgi.c \\ ' config.m4

phpize7
%configure \
	--disable-static \
	--enable-fpm  \
	--with-fpm-user=_php_fpm \
	--with-fpm-group=_webserver \
	--with-php-config=%_bindir/php-config7 \
	--localstatedir=/var \
	--program-suffix=7 \
	EXTRA_LIBS="-lphp-%_php7_version -lrt" \
	$FPM_BUILD_VARS 

%php7_make sapi/fpm/php-fpm

%install
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%php7_servicedir/%php7_sapi \
	%buildroot/%php7_sysconfdir/%php7_sapi/php.d
	
%php7_make_install install-fpm program_suffix=7-%_php7_version

ln -s php-fpm7-%_php7_version %buildroot%_sbindir/php7-fpm

install -m 644 %SOURCE1 %buildroot/%php7_sysconfdir/%php7_sapi/php.ini
install -m 644 %SOURCE2 %buildroot/%php7_sysconfdir/%php7_sapi/browscap.ini

for f in \
	%buildroot/%php7_sysconfdir/%php7_sapi/php.ini
do
  subst 's,@SAPI@,%php7_sapi,g' "$f"
  subst 's,@PHP_VERSION@,%_php7_version,g' "$f"
  subst 's,@PHP_MAJOR@,%_php7_major,g' "$f"
  subst 's,@PHP_LIBDIR@,%_libdir/php,g' "$f"
  subst 's,@CGIBINDIR@,%webserver_cgibindir,g' "$f"
  subst 's,@PHP_BROWSCAP@,%php7_sysconfdir/%php7_sapi/browscap.ini,g' "$f"
done

install -pD -m755 %SOURCE3 %buildroot%_initdir/php7-fpm
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/91-php-%name.filetrigger << EOF
#!/bin/sh
LC_ALL=C sed 's|^%php7_sysconfdir/%php7_sapi/control.d||' |
        egrep -qs '^%php7_sysconfdir/%php7_sapi|^%php7_extdir' || exit 0
/sbin/service php7-fpm condrestart||:
EOF
chmod 0755 %buildroot%_rpmlibdir/91-php-%name.filetrigger


# Make alternatives support.
install -d %buildroot/%_altdir
php_weight="$(echo "%_php7_version" | sed 's,[^[:digit:]],,g')"

cat << EOF > %buildroot/%_altdir/php7-fpm
%_sbindir/php-fpm	%_sbindir/php-fpm7-%_php7_version	$php_weight
EOF

mkdir -p %buildroot%_logdir/php7-fpm
mkdir -p %buildroot%_runtimedir/php7-fpm

# config for logrotate
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/php7-fpm

mkdir -p  %buildroot%_sysconfdir/tmpfiles.d
echo 'd /run/php7-fpm 0750 root _webserver' >> %buildroot%_sysconfdir/tmpfiles.d/php7-fpm.conf

mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE5 %buildroot%_unitdir/php7-fpm.service
install -pD -m755 %SOURCE6 %buildroot/usr/libexec/service/legacy-actions/php7-fpm/rotate

%pre
/usr/sbin/groupadd -r -f _php_fpm 2>/dev/null ||:
/usr/sbin/groupadd -r -f _webserver 2>/dev/null ||:
/usr/sbin/useradd -r -g _php_fpm -d / -s /dev/null -n -c "PHP FastCGI Process Manager" _php_fpm >/dev/null 2>&1 ||:

%preun
%php7_sapi_preun
%preun_service php7-fpm

%files
%doc CREDITS
%config %_initdir/php7-fpm
%_sbindir/php-fpm7-%_php7_version
%_sbindir/php7-fpm
%_altdir/php7-fpm 
%dir %php7_sysconfdir/%php7_sapi
%dir %php7_sysconfdir/%php7_sapi/php.d
%dir %_sysconfdir/fpm7/
%dir %_sysconfdir/fpm7/php-fpm.d
%dir %_logdir/php7-fpm
%dir  %attr(775,root,_php_fpm) %verify(not mode) %_runtimedir/php7-fpm
%config(noreplace) %_sysconfdir/fpm7/php-fpm.conf
%config(noreplace) %_sysconfdir/fpm7/php-fpm.d/www.conf
%config(noreplace) %php7_sysconfdir/%php7_sapi/php.ini
%config(noreplace) %php7_sysconfdir/%php7_sapi/browscap.ini
%config(noreplace) %_sysconfdir/logrotate.d/php7-fpm
%config(noreplace) %_sysconfdir/tmpfiles.d/php7-fpm.conf
%php7_servicedir/%php7_sapi
%config %_unitdir/php7-fpm.service
%_rpmlibdir/91-php-%name.filetrigger
%_man8dir/*
/usr/libexec/service/legacy-actions/php7-fpm

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

