Name: libuv
Version: 1.28.0
Release: alt1

Summary: Evented I/O for NodeJS

Group: Development/Tools
License: MIT License
Url: https://github.com/libuv/libuv

# Source-url: https://github.com/libuv/libuv/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-devel gcc-c++ openssl-devel zlib-devel gyp

%add_python_req_skip TestCommon

%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on Windows 
and libev on Unix systems. We intend to eventually contain all platform differences in this library.

%package devel
Summary: Devel package for libuv
Group: Development/Other
License: GPL
Requires: %name = %version-%release

%description devel
libuv header and build tools.

%prep
%setup

%build
# due option hack in autogen.sh
#autoreconf
./autogen.sh
%configure --disable-static
%make_build

# not for hasher
#check
#make check

%install
%makeinstall_std
# FIXME: --disable-static does no disable static
rm -f %buildroot%_libdir/%name.a

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc


%changelog
* Thu Jun 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1.28.0-alt1
- new version 1.28.0 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1.23.2-alt1
- new version 1.23.2 (with rpmrb script)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.20.3-alt1
- new version 1.20.3 (with rpmrb script)

* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.18.0-alt1
- new version 1.18.0 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.16.1-alt1
- new version 1.16.1 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt1
- new version 1.15.0 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 1.13.1-alt1
- new version 1.13.1 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Thu Jul 14 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Tue Feb 09 2016 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)
- move sources to libuv subdir
- change soname to 1.0.0

* Sat Jun 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.11.5-alt1
- 0.11.5

* Wed May 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.8-alt1
- 0.10.8

* Tue May 07 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.5-alt1
- 0.10.5

* Thu Apr 18 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.4-alt1.1
- Build without soname

* Thu Apr 18 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.4-alt1
- 0.10.4

* Sat Apr 06 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.3-alt1
- 0.10.3

* Thu Nov 15 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9-alt1
- Initial build

