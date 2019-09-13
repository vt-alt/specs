%define _name libmbim
%define _libexecdir %prefix/libexec

Name: %_name-glib
Version: 1.20.0
Release: alt1

Summary: MBIM modem protocol helper library
License: %lgpl2plus
Group: System/Libraries
URL: https://cgit.freedesktop.org/libmbim/libmbim/
# git://anongit.freedesktop.org/libmbim/libmbim
Source: %name-%version.tar

Patch: %_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: glib2-devel libgio-devel libgudev-devel
BuildRequires: python-modules-json
BuildRequires: gtk-doc help2man

%define _unpackaged_files_terminate_build 1

%description
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.
This package contains MBIM modem protocol helper library.

%package utils
Summary: MBIM command line utilities
License: %gpl2plus
Group: System/Base
Requires: %name = %version-%release

%description utils
The Mobile Broadband Interface Model (MBIM) is a new standard
to communicate with mobile broadband modem devices developed
by the USB Implementors Forum.
This package contains MBIM command line utilities.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: glib2-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: This package contains development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: %name-devel = %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup
%patch -p1
touch README ChangeLog

%build
%ifarch %e2k
%define more_warnings no
%else
%define more_warnings error
%endif

%autoreconf
%configure \
	--disable-static \
	--with-udev \
	--enable-gtk-doc \
	--enable-more-warnings=%more_warnings
%make_build

# Fix mbimcli name in the man page
sed -i 's;lt\\-mbimcli;mbimcli;' docs/man/mbimcli.1

%install
%makeinstall_std

%check
make check

%files
%_libdir/*.so.*
%_libexecdir/mbim-proxy

%files utils
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/completions/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*


%changelog
* Thu Sep 12 2019 Mikhail Efremov <sem@altlinux.org> 1.20.0-alt1
- Updated to 1.20.0.

* Thu May 16 2019 Mikhail Efremov <sem@altlinux.org> 1.18.2-alt1
- Updated to 1.18.2.

* Thu Jan 10 2019 Mikhail Efremov <sem@altlinux.org> 1.18.0-alt1
- Updated to 1.18.0.

* Wed Aug 29 2018 Mikhail Efremov <sem@altlinux.org> 1.16.2-alt1
- Use %%e2k macro.
- Updated to 1.16.2.

* Fri Jan 26 2018 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt1
- Move mbim-proxy to %prefix/libexec.
- Updated to 1.16.0.

* Thu Jan 25 2018 Mikhail Efremov <sem@altlinux.org> 1.14.4-alt1
- Fix build on e2k.
- Updated to 1.14.4.

* Mon Aug 14 2017 Mikhail Efremov <sem@altlinux.org> 1.14.2-alt1
- Updated to 1.14.2.

* Tue Jul 19 2016 Mikhail Efremov <sem@altlinux.org> 1.14.0-alt1
- Explicitly use --with-udev configure option.
- Updated to 1.14.0.

* Wed Mar 23 2016 Mikhail Efremov <sem@altlinux.org> 1.12.4-alt1
- Updated to 1.12.4.

* Fri Feb 13 2015 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1
- Updated to 1.10.2.

* Tue Aug 05 2014 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Updated to 1.10.0.

* Tue Mar 11 2014 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Wed Dec 18 2013 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Wed Jul 03 2013 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Fri Jun 14 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Improve descriptions.
- Updated to 1.2.0.

* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Use G_GUINT64_FORMAT for printing speed values.
- Initial build.
