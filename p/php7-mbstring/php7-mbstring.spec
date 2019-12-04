%define		php7_extension	mbstring

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	PHP module for support multi-byte strings.
Group:		System/Servers
License:	PHP License

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version
BuildRequires:	php7 = %php7_version

%description
This package allows you to handle multiple Japanese encodings (SJIS, EUC,
UTF-8, JIS) in PHP.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
        --enable-mbregex \
	--enable-%php7_extension
%php7_make

%install
%php7_make_install phpincludedir=%includedir
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%check
NO_INTERACTION=1 make test

%files
%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

