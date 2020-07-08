%define soversion 4

Name: json-c
Version: 0.13.1
Release: alt2

Summary: JSON implementation in C
License: MIT
Group: System/Libraries
Url: https://github.com/json-c/json-c/wiki

Source: %name-%version-%release.tar
# git://github.com/json-c/json-c.git

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

%package -n lib%name%soversion
Summary: JSON shared library
Group: System/Libraries

%description -n lib%name%soversion
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains shared JSON-C library

%package -n lib%name-devel
Summary: header files for libjson
Group: Development/C
Requires: lib%name%soversion = %version-%release

%description -n lib%name-devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains development part of JSON-C

%prep
%setup

%build
%autoreconf
%configure --enable-rdrand --disable-static
%make

%install
%makeinstall_std

# Relocate shared libraries from %%_libdir/ to /%%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
        ln -fnrs %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%check
%make check

%files -n lib%name%soversion
/%_lib/*.so.%{soversion}*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Sat Jul 04 2020 Alexey Shabalin <shaba@altlinux.org> 0.13.1-alt2
- Update to json-c-0.13 branch (ee9f67c81a3c2a44557f0cc16dc136c140293252)
- Fixes: CVE-2020-12762

* Mon Dec 31 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13.1-alt1
- Updated to 0.13.1.

* Fri Jan 26 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt2
- move library /usr/lib -> /lib

* Fri May 05 2017 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Tue May 27 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12
- rename to libjson-c

* Fri Dec 07 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- 0.10

* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt2
- updated to svn rev.59

* Tue Aug  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released
