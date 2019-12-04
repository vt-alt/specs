%define php7_extension smbclient
%define pecl7_name smbclient

Name: pecl-%pecl7_name
Version: 1.0.0
Release: alt1.%php7_version.%php7_release

Summary: A PHP wrapper for libsmbclient

License: New BSD License
Group: Development/Other
Url: http://pecl.php.net/package/%pecl7_name

Source: http://pecl.php.net/get/%pecl7_name-%version.tar

BuildRequires:php7-devel libsmbclient-devel

BuildRequires(Pre): rpm-build-pecl-php7

%description
smbclient is a PHP extension that uses Samba's libsmbclient library to provide
Samba related functions and 'smb' streams to PHP programs.

%prep
%setup -n %pecl7_name-%version

%build
phpize
%pecl7_configure '--with-smbclient'
%make_build

%install
%pecl7_install
mkdir -p %buildroot%_docdir/%name-%version/

%post
%php7_extension_postin

%preun
%php7_extension_preun

%files
%pecl7_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release
