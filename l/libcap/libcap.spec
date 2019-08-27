Name: libcap
Version: 2.27.0.2.ac1e
Release: alt1
Epoch: 1

Summary: Library for getting and setting POSIX.1e capabilities
License: GPL-2.0-only or BSD-3-Clause
Group: System/Libraries
Url: https://sites.google.com/site/fullycapable/
# git://git.altlinux.org/gears/l/libcap.git
Source: %name-%version-%release.tar

# For backwards compatibility.
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}
Provides: %name.so.1%lib_suffix

BuildRequires: gperf
BuildRequires(pre): libpam-devel

%set_pam_name pam_cap

%package utils
Summary: Utilities for getting and setting POSIX.1e capabilities
Group: System/Base
Requires: %name = %epoch:%version-%release

%package devel
Summary: Development environment for libcap
Group: Development/C
Requires: %name = %epoch:%version-%release

%package -n %pam_name
Summary: PAM module for enforcing inheritable capability sets
Group: System/Base
Provides: pam_cap = %epoch:%version-%release
Obsoletes: pam_cap < %epoch:%version
Requires: %name = %epoch:%version-%release

%description
This is a library for getting and setting POSIX.1e
(formerly POSIX 6) draft 15 capabilities.

%description utils
This packages contains utilities for getting and setting
POSIX.1e (formerly POSIX 6) draft 15 capabilities.

%description devel
The development library, header files, and documentation
for building applications dealing with POSIX.1e
(formerly POSIX 6) draft 15 capabilities.

%description -n %pam_name
The purpose of this PAM module is to enforce inheritable capability sets
for users specified in configuration file.

%prep
%setup -n %name-%version-%release

%build
%make_build CC=%__cc CFLAGS="%optflags" \
	lib=%_lib DEBUG= INDENT= STALIBNAME=

%install
%makeinstall_std lib=%_lib STALIBNAME= RAISE_SETFCAP=no
install -pDm600 pam_cap/capability.conf %buildroot/etc/security/capability.conf

# Relocate development library from /%_lib/ to %_libdir/.
symlink="%buildroot/%_lib/libcap.so"
soname=$(readlink "$symlink")
rm "$symlink"
ln -rsnf %buildroot/%_lib/"$soname" "%buildroot%_libdir/libcap.so"

# For backwards compatibility.
ln -rsnf %buildroot/%_lib/"$soname" "%buildroot%_libdir/libcap.so.1"

%files
/%_lib/*.so.*
%_libdir/*.so.*

%files utils
/sbin/*
%_man1dir/*
%_man8dir/*

%files devel
%_libdir/*.so
%_includedir/sys/*.h
%_pkgconfigdir/*.pc
%_man3dir/*
%doc CHANGELOG License README *.txt pgp.keys.asc doc/capability.notes progs/*.c

%files -n %pam_name
%config(noreplace) /etc/security/capability.conf
%_pam_modules_dir/*

%changelog
* Sun Apr 21 2019 Dmitry V. Levin <ldv@altlinux.org> 1:2.27.0.2.ac1e-alt1
- libcap-2.26 -> libcap-2.27-2-gac1ef31.

* Wed Jan 02 2019 Dmitry V. Levin <ldv@altlinux.org> 1:2.26-alt1
- libcap-2.25-8-gbe92eaa -> libcap-2.26.

* Sun Dec 30 2018 Dmitry V. Levin <ldv@altlinux.org> 1:2.25.0.8.be92-alt1
- libcap-2.25-1-g1f52c8a -> libcap-2.25-8-gbe92eaa.

* Sun Mar 26 2017 Dmitry V. Levin <ldv@altlinux.org> 1:2.25-alt1
- Updated to libcap-2.25-1-g1f52c8a.

* Wed Apr 30 2014 Dmitry V. Levin <ldv@altlinux.org> 1:2.24-alt1
- Updated to libcap-2.24-2-g3c22870 (closes: #29286).

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.16-alt4
- Rebuilt for more debuginfo.

* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.16-alt3
- Rebuilt for debuginfo.

* Fri Nov 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.16-alt2
- Rebuilt for soname set-versions.

* Sun Mar 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.16-alt1
- Updated to 2.16 release.
- sys/capability.h: Fixed linux headers include prevention.

* Sun Nov 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.15-alt2
- Updated to 2.15 release.

* Thu Nov 13 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.15-alt1
- Updated to 2.15.

* Wed Nov 05 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.14-alt1
- Updated to 2.14.

* Tue Sep 16 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt17
- Fixed build with fresh kernel headers.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt16
- Uncompressed tarball, reduced macro abuse in specfile.

* Fri Oct 14 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt15
- Enabled additional gcc diagnostics and fixed all uncovered warnings.

* Thu Oct 06 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt14
- Removed prototypes of cap_get_fd, cap_get_file, cap_set_fd and
  cap_set_file functions from sys/capability.h file (closes #8142).

* Mon Aug 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt13
- Restricted list of global symbols exported by the library.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt12
- Relocated development library to %%_libdir.
- Added multilib support.

* Tue Apr 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt11
- Link the libcap shared library with glibc.

* Thu Nov 06 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt10
- Do not override capget and capset symbols defined in glibc.
- Build the shared library with -fPIC.

* Mon Oct 13 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt9
- Enhanced bounds checking patch.

* Wed Aug 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt8
- Refined userland patch.

* Thu May 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt7
- Pass -Werror to compiler.
- Do not set executable bit for library.

* Mon Sep 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt6
- Fixed few compilation warnings.
- Rediffed some of patches with "-p" option.

* Mon Sep 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt5
- Updated %post/%postun scripts.
- Updated devel-static requirements.
- Use subst instead of perl for build.

* Tue Feb 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.10-alt4
- Reworked userland patch.

* Wed Feb 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.10-ipl3
- Merged two RH patches:
  + fixed libcap/_makenames.c to use own header;
  + fixed sys/capability.h to avoid kernel headers devour in user mode.

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.10-ipl2
- Added snprintf sanity fix.
- Fixed cap_free usage within library.

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 1.10-ipl1
- Split to %name, %name-utils and %name-devel subpackages.

* Fri Dec  3 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
