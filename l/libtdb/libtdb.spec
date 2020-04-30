%define _unpackaged_files_terminate_build 1

%def_with check

Name: libtdb
Version: 1.4.3
Release: alt1

Summary: A trivial database system
License: LGPLv3+
Group: System/Libraries
Url: http://tdb.samba.org/

Source: http://samba.org/ftp/tdb/tdb-%{version}.tar.gz
Patch: tdb-alt-fix-python-ldflags.patch

BuildRequires: docbook-dtds docbook-style-xsl xsltproc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

This is the primary library.

%package -n tdb-utils
Summary: a trivial database system utils
Group: Databases
Requires: %name = %version-%release

%description -n tdb-utils
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

This package contains some utils for managing tdb databases

%package devel
Summary: a trivial database system development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

These are the development files.

%package -n python3-module-tdb
Group: Development/Python3
Summary: Python3 bindings for the Tdb library
Requires: %name = %EVR

%description -n python3-module-tdb
Python3 bindings for libtdb

%prep
%setup -n tdb-%version
%patch -p1

%build
%undefine _configure_gettext
%configure \
           --disable-rpath \
           --bundled-libraries=NONE \
	   --builtin-libraries=replace

%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/libtdb.a

%check
make test

%files
%_libdir/libtdb.so.*
%doc docs/README

%files -n tdb-utils
%_bindir/*
%_man8dir/*

%files devel
%_libdir/libtdb.so
%_includedir/tdb.h
%_pkgconfigdir/tdb.pc

%files -n python3-module-tdb
%python3_sitelibdir/tdb.cpython-*.so
%python3_sitelibdir/_tdb_text.py*
%python3_sitelibdir/__pycache__/_tdb_text.cpython*.py*

%changelog
* Wed Feb 05 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.4.3-alt1
- Update to latest release without crypt replace
- Set license to LGPLv3+

* Thu Oct 31 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.2-alt1
- Update to new release without python2 support

* Wed Feb 27 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.3.18-alt1
- Update to latest release with python3 by default

* Tue Nov 27 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.3.16-alt2
- Disable ubt macros due binary package identity changes

* Sat Jul 21 2018 Stanislav Levin <slev@altlinux.org> 1.3.16-alt1
- 1.3.15 -> 1.3.16
- Build package for Python3

* Tue Sep 19 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.15-alt1
- Update to latest release for samba-4.7 and samba-4.8

* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.14-alt1
- Update to release for samba-4.7.0

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.12-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.12-alt1%ubt
- Update to release for samba-4.6.0

* Fri Sep 09 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.10-alt1
- Update to release for samba-4.5.0

* Tue Apr 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- 1.3.9

* Sun Mar 13 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.8-alt2
- Rebuild with new libtalloc

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.8-alt1
- 1.3.8
- Enable tests
- Rename from tdb to libtdb
- Optional build python3 module (disaled by default)

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.7-alt1
- 1.3.7

* Wed Jul 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Mon Jan 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Mon Dec 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Mon Sep 22 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Tue Jun 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt2
- fixed https://bugzilla.samba.org/show_bug.cgi?id=10625

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Mar 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.13-alt1
- 1.2.13

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.11-alt1
- 1.2.11

* Thu Jul 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9-alt1.1
- Rebuild with Python-2.7

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1.2.9-alt1
- 1.2.9
- Add python bindings in new python-module-tdb subpackage

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Sat Nov 05 2005 Nick S. Grechukh <gns@altlinux.org> 1.0.6-alt3
- initial build for Sisyphus

* Mon Dec 10 2001 Ben Woodard <ben@zork.net>
- Bumped up the version number
- changed email addrs.

* Thu May 23 2001 Jonathon D Nelson <jnelson@securepipe.com>
- Created redhat packages.

