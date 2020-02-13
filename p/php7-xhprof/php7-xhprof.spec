%define		php7_extension	xhprof
%define 	real_name	xhprof
%define		real_version	2.1.4

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 hierarchical profiler

License:	%asl
Group:		System/Servers
URL:		https://pecl.php.net/package/xhprof

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh
Source3:	%real_name.conf

BuildRequires(pre): rpm-build-php7 rpm-build-licenses rpm-macros-webserver-common

# Automatically added by buildreq on Tue Jan 28 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config perl php7-libs python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: glibc-devel-static php7-devel

BuildRequires: php7-devel = %php7_version

%description
XHProf is a function-level hierarchical profiler for PHP and
has a simple HTML based navigational interface.
The raw data collection component is implemented in C (as a
PHP extension). The reporting/UI layer is all in PHP.
It is capable of reporting function-level inclusive and
exclusive wall times, memory usage, CPU times and number
of calls for each function. Additionally, it supports ability
to compare two runs (hierarchical DIFF reports), or aggregate
results from
multiple runs.


%prep
%setup -c
%patch0 -p1
cp %SOURCE3 %real_name.conf

%build
pushd extension/
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
pushd extension/
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params
popd

mkdir -p %buildroot%webserver_webappsdir
cp -a xhprof_html %buildroot%webserver_webappsdir
cp -a xhprof_lib  %buildroot%webserver_webappsdir
sed -e 's|DIRECTORY|%webserver_webappsdir/xhprof_html|g' -i %real_name.conf

%files
%doc CHANGELOG README.md LICENSE
%doc examples/sample.php scripts/xhprofile.php
%doc xhprof.conf

%php7_extconf/%php7_extension
%php7_extdir/*

%webserver_webappsdir/xhprof_html
%webserver_webappsdir/xhprof_lib

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Tue Jan 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.13-alt1
- Initial build for ALT Linux Sisyphus
