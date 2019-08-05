%global _unpackaged_files_terminate_build 1
%def_disable static
%define Name OpenSM
%define _libexecdir /usr/libexec

Name: opensm
%define lname lib%name
Summary: InfiniBand subnet manager and administration
Version: 3.3.22
Release: alt1
License: %gpl2only
Group: Networking/Other
URL: http://openib.org
# https://github.com/linux-rdma/opensm.git
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.service
Source3: %name.launch
Patch: %name-%version.patch

Requires: lib%name = %version-%release
Provides: %{name}2 = %version-%release
Obsoletes: %{name}2 < %version-%release

BuildRequires(pre): rpm-build-licenses
BuildRequires: flex rdma-core-devel 

%description
%Name provides an implementation of an InfiniBand Subnet Manager and
Administration. Such a software entity is required to run for in order
to initialize the InfiniBand hardware (at least one per each InfiniBand
subnet).

%package -n lib%name
Summary: Libraries from the %name package
Group: System/Libraries
Provides: lib%{name}2 = %version-%release
Obsoletes: lib%{name}2 < %version-%release

%description -n lib%name
Shared libraries that are part of the %name package but are also used
by other applications. If you don't need %name itself installed, these
libraries can be installed to satisfy dependencies of other
applications.


%package -n lib%name-devel
Summary: Development files for %Name
Group: Development/C
Requires: lib%name = %version-%release
Requires: libibumad-devel
Provides: lib%{name}2-devel = %version-%release
Obsoletes: lib%{name}2-devel < %version-%release

%description -n lib%name-devel
Development files for %Name.

%package -n lib%name-devel-static
Summary: Static %Name libraries
Group: Development/C
Requires: lib%name-devel = %version-%release libibumad-devel-static

%description -n lib%name-devel-static
Static %Name libraries.

%prep
%setup
%patch -p1

%build
./autogen.sh
%add_optflags %optflags_shared
%configure \
    %{subst_enable static} \
    --with-opensm-conf-sub-dir=rdma

%make_build

cd opensm
./opensm -c ../opensm-%version.conf

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot{%_cachedir/%name,%_initdir,%_sysconfdir/{rdma,sysconfig},%_logrotatedir}
install -D -m644 opensm-%version.conf %buildroot%_sysconfdir/rdma/opensm.conf
install -D -m 0755 %SOURCE1 %buildroot%_initdir/%name
install -D -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -D -m 0755 %SOURCE3 %buildroot%_libexecdir/%name-launch
install -D -m 0644 scripts/opensm.logrotate %buildroot%_logrotatedir/opensm
cat > %buildroot/%_sysconfdir/sysconfig/%name <<__CONF__
OSM_ARGS=
OSM_HOSTS=
__CONF__

rm -f %buildroot/etc/init.d/opensmd

%post 
%post_service %name

%preun
%preun_service %name


%files
%doc AUTHORS COPYING README
%doc doc/*.txt
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/rdma/opensm.conf
%config(noreplace) %_logrotatedir/opensm
%_initdir/%name
%_unitdir/%name.service
%_libexecdir/%name-launch
%_sbindir/*
%_man5dir/*
%_man8dir/*
%dir %_cachedir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/infiniband/*
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Sat Jul 20 2019 Alexey Shabalin <shaba@altlinux.org> 3.3.22-alt1
- 3.3.22

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 3.3.21-alt1
- 3.3.21

* Thu Apr 12 2018 Alexey Shabalin <shaba@altlinux.ru> 3.3.20-alt1
- 3.3.20
- disable static build

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.7-alt2
- Rebuilt for debuginfo

* Tue Dec 07 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.7-alt1
- New version

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.6-alt2
- Rebuilt for soname set-versions
- Fixed underlinking of libraries

* Thu Sep 02 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.6-alt1
- New version

* Wed Sep 01 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.5-alt2
- Rebuild with new libibumad

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 3.3.5-alt1
- 3.3.5 (OFED 1.5.1)

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt3
- Rebuild from upstream git repository
- Fixed libraries linking

* Mon Jun 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt2
- Rename opensm -> opensm2

* Tue May 26 2009 Led <led@altlinux.ru> 3.3.2-alt1
- 3.3.2

* Tue May 26 2009 Led <led@altlinux.ru> 3.2.6-alt1
- 3.2.6

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5_20081207-alt3
- Rebuild with automake 1.11

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5_20081207-alt2
- Rebuild with gcc4.4

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5_20081207-alt1
- Version 3.2.5_20081207

* Wed Oct 29 2008 Led <led@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 3.1.11-alt1
- OFED-1.3.1

* Fri Feb 22 2008 Stanislav Ievlev <inger@altlinux.org> 3.0.3-alt3
- add init.d script

* Mon Aug 27 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.3-alt2
- turn on devel part

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.3-alt1
- Initial build
