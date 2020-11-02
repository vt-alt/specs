%define _unpackaged_files_terminate_build 1

Name: libtar
Version: 1.2.20
Release: alt2.git.6d0ab4c
Summary: C library for manipulating POSIX tar files
License: BSD
Group: System/Libraries
Url: https://repo.or.cz/w/libtar.git

# git://repo.or.cz/libtar.git
Source: %name-%version.tar

# Patches from Debian
Patch1: CVE-2013-4420.patch
Patch2: oldgnu_prefix.patch
Patch3: no_strip.patch

# Automatically added by buildreq on Tue Mar 09 2010
BuildRequires: zlib-devel

%description
libtar is a C library for manipulating tar archives. It supports both the strict
POSIX tar format and many of the commonly-used GNU extensions.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %name library.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

# set correct version for .so build
%define ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %ltversion/' \
lib/Makefile.in

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_libdir/%name.so.*

%files devel
%_includedir/*.h
%_libdir/%name.so
%_man3dir/*

%changelog
* Thu Oct 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.20-alt2.git.6d0ab4c
- Applied patches from Debian (Fixes: CVE-2013-4420).

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.20-alt1
- 1.2.20
- removed obsolete patches

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.11-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.2.11-alt1.1
- rebuild (with the help of girar-nmu utility)

* Wed Mar 10 2010 Victor Forsiuk <force@altlinux.org> 1.2.11-alt1
- Initial build.
