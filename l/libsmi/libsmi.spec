%define mibsdir %_datadir/mibs
%define pibsdir %_datadir/pibs
%define yangdir %_datadir/yang

%def_disable static
%def_disable mibs_internal

Name: libsmi
Version: 0.5.0
Release: alt1.svn1841

Summary: A library to access SMI MIB information
License: BSD
Group: System/Libraries
URL: http://www.ibr.cs.tu-bs.de/projects/libsmi/index.html

Packager: Alexey Shabalin <shaba@altlinux.ru>

# SVN http://svn.ibr.cs.tu-bs.de/software-ibr-1999-libsmi
Source0: %name-%version.tar
Source1: smi.conf

Patch2: libsmi-0.4.8-alt-man.patch
Patch3: libsmi-deb-smistrip.patch
Patch4: libsmi-alt-fix-build.patch
Patch5: libsmi-0.5.0-alt-yyleng.patch
Patch7: libsmi-0.4.8-alt-bison.patch


Requires: snmp-mibs
BuildRequires: flex gcc-c++ wget
%if_enabled static
BuildRequires: glibc-devel-static
%endif

%package devel
Summary: Development environment for libsmi library
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static libsmi library
Group: Development/C
Requires: %name-devel = %version-%release

%package mibs
Summary: MIB files for LibSMI
Group: Networking/Other
BuildArch: noarch
Provides: snmp-mibs

%package -n smi-tools
Summary: LibSMI tools
Group: Networking/Other
Requires: %name = %version-%release
Requires: wget

%description
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules. 

This package contains tools to check, dump, and convert MIB 
definitions and a steadily maintained and revised archive 
of all IETF and IANA maintained standard MIB modules. 

%description devel
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules. 

This package contains development files needed to develop %name-based
applications.

%description devel-static
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules. 

This package contains the static %name library needed to develop 
statically linked %name-based applications.

%description mibs
MIBs for %name. May be used with other packages (net-snmp, for example)

%description -n smi-tools
This package contains the LibSMI tools.


%prep
%setup -q

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-shared \
	--sysconfdir=%_sysconfdir \
	--enable-smi \
	--enable-sming
LIBTOOL=/usr/bin/libtool %make_build

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_sysconfdir
install -p -m 644 %SOURCE1 %buildroot%_sysconfdir/smi.conf

%check
%make_build check ||:

%files
%doc ChangeLog ANNOUNCE README COPYING THANKS smi.conf-example
%config(noreplace) %_sysconfdir/smi.conf
%_libdir/*.so.*

%files devel
%doc TODO doc/draft-irtf-nmrg-sming-02.txt
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4
%_includedir/*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%if_enabled mibs_internal
%files mibs
%mibsdir
%pibsdir
%yangdir
%else
%exclude %mibsdir
%exclude %pibsdir
%exclude %yangdir
%endif

%files -n smi-tools
%_bindir/*
%_man1dir/*

%changelog
* Wed Aug 28 2019 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1.svn1841
- 0.5.0 svn rev 1841

* Mon Jul 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.8-alt2.2
- Fixed build.

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt2.1
- Fixed build

* Mon Oct 25 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.8-alt2
- some backports
- security fix: CVE-2010-2891 (ALT #24394)

* Thu Feb 25 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.8-alt1
- 0.4.8
- move tools to smi-tools subpackage
- move mibs to libsmi-mibs subpackage, but not build by default; use external snmp-mibs package
- disable build static by default
- add debian smistrip.patch
- change Packager

* Fri Nov 29 2002 Oleg Prokopyev <riiki@altlinux.ru> 0.4.1-alt1
- new version

* Fri Nov 22 2002 Oleg Prokopyev <riiki@altlinux.ru> 0.4.0-alt1
- Initial build for Sisyphus.
