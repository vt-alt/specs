Name: libudfread
Version: 1.1.1
Release: alt1
Summary: library for reading UDF from raw devices and image file
License: LGPLv2.1
Group: Development/C
Url: https://code.videolan.org/videolan/libudfread
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%description
library for reading UDF from raw devices and image file

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
autoreconf -fisv
%configure
%make

%install
%makeinstall_std


%files
%_libdir/libudfread.so.*

%files devel
%_includedir/*
%_libdir/libudfread.so
%_pkgconfigdir/*.pc

%changelog
* Mon Nov 30 2020 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt3
- rebuilt for aarch64

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- fixed cflags in pkgconfig

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- first build for ALT

