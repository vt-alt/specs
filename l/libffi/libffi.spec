%define soname 6

Name: libffi
Version: 3.2.1
Release: alt3
Epoch: 1

Summary: Foreign Function Interface library
License: MIT
Group: System/Libraries
URL: http://sourceware.org/libffi

# http://sourceware.org/libffi/%name-%version.tar.gz
Source: %name-%version.tar
# git://git.altlinux.org/gears/l/libffi.git
Patch: %name-%version-%release.patch

%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu, gcc-c++, /proc, /dev/pts}}

# Automatically added by buildreq on Mon Jan 25 2016
# optimized out: perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-unicore
BuildRequires: makeinfo

%description
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.


%package -n libffi%soname
Summary: Header files and library for Foreign Function Interface development
Group: System/Libraries
Provides: libffi = %epoch:%version-%release

%description -n libffi%soname
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package contains Foreign Function Interface shared library
which is needed to run Foreign Function Interface dynamically
linked programs

%package devel
Summary: Header files and library for Foreign Function Interface development
Group: Development/Other
Requires: libffi%soname = %epoch:%version-%release

%description devel
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package includes the header files and library needed for
Foreign Function Interface development.

%package devel-static
Summary: Static library for Foreign Function Interface development
Group: Development/Other
Requires: libffi-devel = %epoch:%version-%release

%description devel-static
The libffi library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer
to call any function specified by a call interface description
at run time.

This package includes the static library needed for
Foreign Function Interface development.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
make -k check

%install
%makeinstall_std

%files -n %name%soname
%_libdir/*.so.*
%doc README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*
%_infodir/*

%files devel-static
%_libdir/*.a

%changelog
* Tue May 19 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.2.1-alt3
- Fixed testsuite regressions.
- Fixed License tag.

* Sat Jun 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.2.1-alt2
- Applied patch for aarch64 from Fedora.

* Mon Jan 25 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.2.1-alt1
- Updated to 3.2.1.

* Wed Aug 27 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.1-alt2
- Fix pkgconfig.
- Apply patch libffi-3.1-fix-exec-stack from fedora.

* Fri Aug 22 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.1-alt1
- New version.

* Mon Sep 19 2011 Alexey Tourbin <at@altlinux.ru> 1:3.0.10-alt1
- Updated to 3.0.10.

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt5
- Rebuilt for debuginfo.

* Thu Oct 28 2010 Kirill A. Shutemov <kas@altlinux.org> 1:3.0.9-alt4
- Rebuilt for soname set-versions.

* Fri Aug 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt3
- Fixed exported header files for -m32.

* Fri Aug 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt2
- Relocated header files to standard location.
- Dropped libffiX.Y provides/obsoletes.

* Sat Jul 31 2010 Kirill A. Shutemov <kas@altlinux.org> 1:3.0.9-alt1
- Initial build of standalone libffi for ALT Linux (closes: #20672)
