%define		php7_extension	ssh2
%define 	real_name	php-ssh2
%define		real_version	1.2

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release.1

Summary:	PHP7 bindings for the libssh2 library

License:	PHP License
Group:		System/Servers
URL:		https://pecl.php.net/package/ssh2

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh


BuildRequires(pre): rpm-build-php7

# Automatically added by buildreq on Mon Jun 15 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config perl php7-libs python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: glibc-devel-static libssh2-devel php7-devel

BuildRequires: php7-devel = %php7_version

%description
php7-zmq extension provides bindings to the functions of libssh2
which implements the SSH2 protocol.

%prep
%setup -c

sed -e 's/@PACKAGE_VERSION@/%real_version/g' -i php_ssh2.h
sed -e 's/@PACKAGE_VERSION@/%real_version/g' -i package.xml

rm -f LICENSE
ln -s -- $(relative %_licensedir/PHP-3.01 %_docdir/%name/LICENSE) LICENSE

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version

%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--enable-zmq \
	%nil

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%doc README.md
%doc --no-dereference LICENSE

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Tue Jun 16 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.18-alt1.1
- Fix module configuration

* Mon Jun 15 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.18-alt1
- Initial build for ALT Linux Sisyphus

