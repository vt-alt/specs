Name:		apache2-mod_http2
Version:	1.15.4
Release:	alt1
Summary:	module implementing HTTP/2 for Apache 2
Group:		System/Servers
License:	ASL 2.0
URL:		https://icing.github.io/mod_h2/
Source0:	%name-%version.tar
Source1:	%name.watch
Patch0:		%name-%version-alt.patch
BuildRequires(pre): apache2-devel > 2.4.27-alt1
BuildRequires:	pkgconfig, libnghttp2-devel >= 1.7.0, libssl-devel >= 1.0.2, libaprutil1-devel, libcurl-devel
Provides: mod_h2 = %EVR
Provides: mod_http2 = %EVR
Provides: apache2-mod_h2 = %EVR

%description
The mod_h2 Apache httpd module implements the HTTP2 protocol (h2+h2c) on
top of libnghttp2 for httpd 2.4 servers.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf -fisv
%configure
%make

%install
make DESTDIR=%{buildroot} install
rm -rf %buildroot/etc/httpd/share/doc/

# create configuration
mkdir -p %buildroot%apache2_mods_available
echo "LoadModule http2_module modules/mod_http2.so" > %buildroot%apache2_mods_available/%name.load
echo "LoadModule proxy_http2_module modules/mod_proxy_http2.so" > %buildroot%apache2_mods_available/mod_proxy_http2.load

%files
%doc README README.md ChangeLog AUTHORS LICENSE
%apache2_mods_available/*.load 
%apache2_moduledir/mod_http2.so
%apache2_moduledir/mod_proxy_http2.so

%changelog
* Wed Nov 27 2019 Anton Farygin <rider@altlinux.ru> 1.15.4-alt1
- 1.15.4

* Tue Jul 23 2019 Anton Farygin <rider@altlinux.ru> 1.15.3-alt1
- 1.15.3

* Thu Jun 20 2019 Anton Farygin <rider@altlinux.ru> 1.15.2-alt1
- 1.15.2

* Sat Jun 01 2019 Anton Farygin <rider@altlinux.ru> 1.15.1-alt1
- 1.15.1

* Fri Mar 15 2019 Anton Farygin <rider@altlinux.ru> 1.14.1-alt1
- 1.14.1

* Thu Feb 21 2019 Anton Farygin <rider@altlinux.ru> 1.12.5-alt1
- 1.12.5

* Wed Feb 06 2019 Anton Farygin <rider@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 1.11.4-alt1
- 1.11.4

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 1.11.3-alt1
- 1.11.3

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.20-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue May 08 2018 Anton Farygin <rider@altlinux.ru> 1.10.20-alt1
- 1.10.20

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 1.10.16-alt1
- new version

* Wed Jan 10 2018 Anton Farygin <rider@altlinux.ru> 1.10.14-alt1
- new version

* Wed Nov 01 2017 Anton Farygin <rider@altlinux.ru> 1.10.13-alt1
- new version

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 1.10.12-alt1
- new version

* Wed Jul 19 2017 Anton Farygin <rider@altlinux.ru> 1.10.7-alt1
- first build for ALT
