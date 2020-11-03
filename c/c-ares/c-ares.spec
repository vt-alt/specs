Name: c-ares
Version: 1.16.1
Release: alt1

Summary: A library that performs asynchronous DNS operations
License: MIT
Group: System/Libraries

Url: http://c-ares.haxx.se/
Source: %url/download/c-ares-%version.tar

# need for test/configure
BuildRequires: gcc-c++

%description -n c-ares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. This package contains little utilities built with
this library.

%package -n libcares
Summary: A library that performs asynchronous DNS operations
Group: System/Libraries

%description -n libcares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n libcares-devel
Summary: Libraries, includes, etc. to develop applications used c-ares
Group: System/Libraries
Requires: libcares = %version-%release

%description -n libcares-devel
This package contains the header files and libraries links needed to
compile applications or shared objects that use c-ares.

%prep
%setup -n c-ares-%version

%build
%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	--enable-debug
# strip rpath
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std
install -d %buildroot%_bindir
install -pm755 .libs/{acountry,adig,ahost} %buildroot%_bindir/

%files -n c-ares
%_bindir/*

%files -n libcares
%_libdir/*.so.*

%files -n libcares-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Fri May 15 2020 Anton Farygin <rider@altlinux.ru> 1.16.1-alt1
- 1.16.1

* Tue Mar 31 2020 Anton Farygin <rider@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Thu Nov 15 2018 Anton Farygin <rider@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.14.0-alt1
- 1.14.0 

* Tue Aug 08 2017 Anton Farygin <rider@altlinux.ru> 1.13.0-alt1
- 1.13.0 with these security fixes:
        * CVE-2016-5180 - Heap-based buffer overflow in the ares_create_query function.
        * CVE-2017-1000381 - NAPTR parser out of bounds access.

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1
- Version 1.10.0

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.7.5-alt2
- Fix RPATH issue.

* Sat Aug 20 2011 Victor Forsiuk <force@altlinux.org> 1.7.5-alt1
- 1.7.5

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 1.7.4-alt1
- 1.7.4

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.3-alt2
- Rebuilt for soname set-versions.

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 1.7.3-alt1
- 1.7.3

* Fri Mar 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Dec 22 2009 Victor Forsyuk <force@altlinux.org> 1.7.0-alt1
- 1.7.0

* Thu Dec 11 2008 Victor Forsyuk <force@altlinux.org> 1.6.0-alt1
- 1.6.0

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 1.5.3-alt2
- Removed obsolete %%post* scripts.

* Fri Sep 12 2008 Victor Forsyuk <force@altlinux.org> 1.5.3-alt1
- 1.5.3

* Thu Jun 12 2008 Victor Forsyuk <force@altlinux.org> 1.5.2-alt1
- Initial build.
