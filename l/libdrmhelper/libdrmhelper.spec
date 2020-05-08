Name: libdrmhelper
Version: 1.3.0
Release: alt1

Summary: A privileged helper for drm initialization
License: LGPL-3.0-or-later
Group: System/Libraries

Source: %name-%version.tar

%description
%summary.

%package devel
Summary: Development environment for drmhelper
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required to build
drmhelper-based software.

%package devel-static
Summary: Static drmhelper library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static library required to build
statically linked drmhelper-based software.

%prep
%setup

%build
%make_build \
	CFLAGS="%optflags" \
	libdir="%_libdir" \
	libexecdir="%_libexecdir"

%install
%makeinstall_std \
	libdir="%_libdir" \
	libexecdir="%_libexecdir"

%pre
/usr/sbin/groupadd -r -f drmpriv

%files
%_libdir/*.so.*
%attr(710,root,drmpriv) %dir %_libexecdir/drmhelper
%attr(4710,root,drmpriv) %_libexecdir/drmhelper/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files devel-static
%_libdir/*.a

%changelog
* Mon Apr 27 2020 Alexey Gladkov <legion@altlinux.ru> 1.3.0-alt1
- Wait for helper to avoid zombies.

* Sun Mar 29 2020 Alexey Gladkov <legion@altlinux.ru> 1.2.0-alt1
- Drop seccomp.

* Sat Mar 28 2020 Alexey Gladkov <legion@altlinux.ru> 1.1.0-alt1
- Improve error handling.
- Open character devices in the /dev directory.
- Use seccomp by default.

* Wed Jan 29 2020 Alexey Gladkov <legion@altlinux.ru> 1.0.0-alt1
- First build for ALT Linux.
