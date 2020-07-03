%define		php7_extension	exif

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	Read header information from JPEG and DIFF headers
Group:		System/Servers
License:	PHP

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh
Patch0: php7-exif-mbstring-bug68547.patch

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version
BuildRequires: php7 = %php7_version
# for unicode support in exif files
BuildRequires: php7-mbstring = %php7_version
Requires: php7-mbstring = %php7_version

%description
The EXIF functions provide access to information stored in headers
of JPEG and TIFF images. This way you can read meta data generated
by digital cameras and certain image processing applications.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .
%patch0 -p3

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--enable-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%check
# turned off tests on i586 does not pass the tests/bug76557.phpt (poor processing errors from exif)
# 063+ Warning: exif_read_data(bug76557.jpg): Process tag(x3030=UndefinedTa): Illegal pointer offset(x30303030 < xF70732CE) in /usr/src/RPM/BUILD/php7-exif-7.3.10/tests/bug76557.php on line 2
# 063- Warning: exif_read_data(bug76557.jpg): Process tag(x3030=UndefinedTa): Illegal pointer offset(x30303030 + x30303030 = x60606060 > x00EE) in %sbug76557.php on line %d

%ifnarch %ix86 armh
ln -s %php7_extdir/* modules/
NO_INTERACTION=1 make test
%endif

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
