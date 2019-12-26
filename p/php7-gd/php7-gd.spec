%define	php7_extension	gd
Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release.1

Summary:	GD library support for PHP
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: glibc-devel-static libfreetype-devel libjpeg-devel libpng-devel php7-devel t1lib-devel libwebp-devel
BuildRequires:	php7-devel = %php7_version
Provides: php7-gd2 = %EVR
Obsoletes: php7-gd2 < %EVR

%description
The %name includes a dynamic shared object (DSO) that adds
GD support to PHP. GD is a library that enables you to create PNG,
JPEG, XPM, and WBMP graphics. It is linked with freetype and t1lib so
you can use TrueType fonts. PHP is an HTML-embedded scripting language.
If you need GD support for PHP applications, you will need to install
this package in addition to the php package.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-jpeg-dir=%_prefix \
	--with-t1lib \
	--with-webp-dir=%_prefix \
	--with-png-dir=%_prefix \
	--with-zlib-dir=%_prefix \
	--with-freetype-dir=%_prefix \
	--with-libdir=%_lib \
	--with-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Mon Dec 16 2019 Anton Farygin <rider@altlinux.org>
- renamed from php7-gd2 to php7-gd
- built with libwebp (closes: #37626)
- cleanup buildrequires
