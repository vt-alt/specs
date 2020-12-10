Name: libtomcrypt
Version: 1.18.2
Release: alt3
Summary: A comprehensive, portable cryptographic toolkit
Group: System/Libraries
License: WTFPL
Url: http://www.libtom.net/

# https://github.com/libtom/libtomcrypt.git
Source: crypt-%version.tar.xz

Patch1: CVE-2019-17362.patch

BuildRequires: dblatex libtommath-devel

%description
A comprehensive, modular and portable cryptographic toolkit that
provides developers with a vast array of well known published block
ciphers, one-way hash functions, chaining modes, pseudo-random number
generators, public key cryptography and a plethora of other routines.

Designed from the ground up to be very simple to use. It has a modular
and standard API that allows new ciphers, hashes and PRNGs to be added
or removed without change to the overall end application. It features
easy to use functions and a complete user manual which has many source
snippet examples.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static development files for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
The %name-devel-static package contains static libraries files for
developing applications that use %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description doc
The %name-doc package contains documentation for use with %name.

%prep
%setup
%patch1 -p1

%build
# no configure script ships with libtomcrypt.  Its only requirement is
# ANSI C. And libtommath.  Explicitly force it to be built against libtommath
export CFLAGS="%optflags -DLTM_DESC -I%_includedir/tommath"
%make_build V=1 LIBPATH=%_libdir EXTRALIBS="-ltommath" -f makefile.shared library
%make_build V=1 LIBPATH=%_libdir -f makefile docs

%check
export CFLAGS="%optflags -DLTM_DESC -DUSE_LTM -I%_includedir/tommath -I testprof"
%make_build V=1 LIBPATH=%_libdir EXTRALIBS="-L.libs -ltommath" -f makefile.shared test
LD_LIBRARY_PATH=.libs ./test

%install
# There is no configure script that ships with libtomcrypt but it does
# have understand DESTDIR and its installs via that and the
# INSTALL_USER and INSTALL_GROUP environment variables.

export INSTALL_USER=$(id -un)
export INSTALL_GROUP=$(id -gn)
export CFLAGS="%optflags -DLTM_DESC -DUSE_LTM"

%makeinstall_std INCPATH=%_includedir/tomcrypt LIBPATH=%_libdir EXTRALIBS="-ltommath" -f makefile.shared
find %buildroot -name '*.h' -exec chmod 644 {} ';'

# remove unneeded files
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name 'libtomcrypt_prof*' -exec rm -f {} ';'

%files
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc LICENSE
%_includedir/tomcrypt
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-static
%_libdir/*.a

%files doc
%doc LICENSE doc/crypt.pdf

%changelog
* Tue Dec 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.18.2-alt3
- Applied security fix from upstream (Fixes: CVE-2019-17362).

* Tue Feb 12 2019 Fr. Br. George <george@altlinux.ru> 1.18.2-alt2
- Change packaging scheme
- Rebuild with libtommath-1.1.0

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.18.2-alt1.qa1
- NMU: applied repocop patch

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.18.2-alt1
- Build new version.

* Tue Apr 03 2018 Grigory Ustinov <grenka@altlinux.org> 1.18.1-alt1
- Build new version.
- Fix BuildRequires.

* Fri Jan 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.18.0-alt1
- Updated to upstream version 1.18.0.

* Wed Sep 14 2011 Fr. Br. George <george@altlinux.ru> 1.17-alt1
- Initial build from FC

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.17-9
- Autorebuild for GCC 4.3

* Sun Nov 25 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.17-8
- Resolve multilib conflicts from Bug #342431 by splitting out
  documentation to libtomcrypt-docs subpackage
- fix rpmlint Summary: warning

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.17-7
- Rebuild for selinux ppc32 issue.

* Tue Jul 10 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-6
- turn off optimization for ppc64 to work around Bug #239003

* Sat Jun 30 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-5
- removed package name from summary
- fixed URL and Source0 links
- really fixed linkage flag this time, added it to the build section not
  just the check.

* Fri Jun 29 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-4
- fixed linkage flag with correct tommath name
- added check section
- removed libtomcrypt_prof libraries from package
- remove package name from summary

* Wed Jun 27 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-3
- create makefile patch to ensure RPM_OPT_FLAGS is honored
- install headers into _includedir/tomcrypt
- add location of libtommath headers to CFLAGS

* Sat Jun 23 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-2
- update build process to pass LIBPATH to make

* Fri Jun 22 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.17-1
- Initial spec file creation
