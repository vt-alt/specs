%def_disable static

Summary: OpenFabrics InfiniBand Diagnostic Tools
Name: infiniband-diags
Version: 2.2.0
Release: alt1
License: GPLv2 or BSD
Group: System/Base
Url: https://github.com/linux-rdma/infiniband-diags

# https://github.com/linux-rdma/infiniband-diags.git
Source: %name-%version.tar
Packager: Timur Aitov <timonbl4@altlinux.org>

BuildRequires: rdma-core-devel
BuildRequires: libopensm-devel
BuildRequires: /usr/bin/rst2man
Requires: lib%name = %EVR
# old names
Provides: openib-diags = %version
Obsoletes: openib-diags


%description
This package provides IB diagnostic programs and scripts needed to
diagnose an IB subnet.

%package -n lib%name
Summary: Shared libraries for IB diagnostic programs
Group: System/Libraries
Provides: libibmad = %EVR
Obsoletes: libibmad < %EVR

%description -n lib%name
This package contains shared libraries for IB diagnostic programs.

%package -n lib%name-devel
Summary: Development files for IB diagnostic programs
Group: Development/C
Requires: lib%name = %EVR
Provides: libibmad-devel = %EVR
Obsoletes: libibmad-devel < %EVR

%description -n lib%name-devel
This package contains development files for IB diagnostic programs.

%package -n lib%name-devel-static
Summary: Static library for IB diagnostic programs
Group: Development/C
Requires: lib%name-devel = %EVR
Provides: libibmad-static = %EVR
Obsoletes: libibmad-static < %EVR

%description -n lib%name-devel-static
This package contains static library for IB diagnostic programs.

%package compat
Group: System/Base
Summary: OpenFabrics Alliance InfiniBand Diagnostic Tools

%description compat
Deprecated scripts and utilities which provide duplicated functionality, most
often at a reduced performance.  These are maintained for the time being for
compatibility reasons.

%prep
%setup

%build
./autogen.sh
%configure  \
    --enable-compat-utils \
    %{subst_enable static} \
    --with-perl-installdir=%perl_vendor_privlib

#sed -i -e '1a\echo=echo' libtool
%make_build
bzip2 --best --keep --force ChangeLog

%install
%makeinstall_std
chmod 644 %buildroot%_sysconfdir/infiniband-diags/ibdiag.conf

%files
%doc README ChangeLog.*
%perl_vendor_privlib/*.pm

# C programs here
%_sbindir/ibaddr
%_man8dir/ibaddr.*
%_sbindir/ibnetdiscover
%_man8dir/ibnetdiscover.*
%_sbindir/ibping
%_man8dir/ibping.*
%_sbindir/ibportstate
%_man8dir/ibportstate.*
%_sbindir/ibroute
%_man8dir/ibroute.*
%_sbindir/ibstat
%_man8dir/ibstat.*
%_sbindir/ibsysstat
%_man8dir/ibsysstat.*
%_sbindir/ibtracert
%_man8dir/ibtracert.*
%_sbindir/perfquery
%_man8dir/perfquery.*
%_sbindir/sminfo
%_man8dir/sminfo.*
%_sbindir/smpdump
%_man8dir/smpdump.*
%_sbindir/smpquery
%_man8dir/smpquery.*
%_sbindir/saquery
%_man8dir/saquery.*
%_sbindir/vendstat
%_man8dir/vendstat.*
%_sbindir/iblinkinfo
%_man8dir/iblinkinfo.*
%_sbindir/ibqueryerrors
%_man8dir/ibqueryerrors.*
%_sbindir/ibcacheedit
%_man8dir/ibcacheedit.*
%_sbindir/ibccquery
%_man8dir/ibccquery.*
%_sbindir/ibccconfig
%_man8dir/ibccconfig.*
%_sbindir/dump_fts
%_man8dir/dump_fts.*
# scripts here
%_sbindir/ibhosts
%_man8dir/ibhosts.*
%_sbindir/ibswitches
%_man8dir/ibswitches.*
%_sbindir/ibnodes
%_man8dir/ibnodes.*
%_sbindir/ibrouters
%_man8dir/ibrouters.*
%_sbindir/ibfindnodesusing.pl
%_man8dir/ibfindnodesusing.*
%_sbindir/ibidsverify.pl
%_man8dir/ibidsverify.*
%_sbindir/check_lft_balance.pl
%_man8dir/check_lft_balance.*
%_sbindir/dump_lfts.sh
%_man8dir/dump_lfts.*
%_sbindir/dump_mfts.sh
%_man8dir/dump_mfts.*
%_sbindir/ibstatus
%_man8dir/ibstatus.*
# and the rest
%_man8dir/infiniband-diags.*
%config(noreplace) %_sysconfdir/infiniband-diags/error_thresholds
%config(noreplace) %_sysconfdir/infiniband-diags/ibdiag.conf

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/infiniband/*
%_man3dir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files compat
%_sbindir/ibcheckerrs
%_man8dir/ibcheckerrs.*
%_sbindir/ibchecknet
%_man8dir/ibchecknet.*
%_sbindir/ibchecknode
%_man8dir/ibchecknode.*
%_sbindir/ibcheckport
%_man8dir/ibcheckport.*
%_sbindir/ibcheckportwidth
%_man8dir/ibcheckportwidth.*
%_sbindir/ibcheckportstate
%_man8dir/ibcheckportstate.*
%_sbindir/ibcheckwidth
%_man8dir/ibcheckwidth.*
%_sbindir/ibcheckstate
%_man8dir/ibcheckstate.*
%_sbindir/ibcheckerrors
%_man8dir/ibcheckerrors.*
%_sbindir/ibclearerrors
%_man8dir/ibclearerrors.*
%_sbindir/ibclearcounters
%_man8dir/ibclearcounters.*
%_sbindir/ibdatacounts
%_man8dir/ibdatacounts.*
%_sbindir/ibdatacounters
%_man8dir/ibdatacounters.*
%_sbindir/ibdiscover.pl
%_man8dir/ibdiscover.*
%_sbindir/ibswportwatch.pl
%_man8dir/ibswportwatch.*
%_sbindir/ibqueryerrors.pl
%_sbindir/iblinkinfo.pl
%_sbindir/ibprintca.pl
%_man8dir/ibprintca.*
%_sbindir/ibprintswitch.pl
%_man8dir/ibprintswitch.*
%_sbindir/ibprintrt.pl
%_man8dir/ibprintrt.*
%_sbindir/set_nodedesc.sh

%changelog
* Mon Jul 22 2019 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt2
- NMU: rebuilt with new python-module-docutils.

* Sat Aug 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- 2.1.0

* Thu Apr 12 2018 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0
- disable build static libs

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.7-alt2
- Rebuilt for debuginfo

* Mon Dec 20 2010 Timur Aitov <timonbl4@altlinux.org> 1.5.7-alt1
- New version

* Tue Aug 31 2010 Andriy Stepanov <stanv@altlinux.ru> 1.5.6-alt1
- New version

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2.1
- Added build requirement on libibcommon-devel

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt2
- Rebuild from upstream git repository

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1
- Version 1.5.2

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4_20081207-alt2
- Rebuild with gcc 4.4
- Disable -no-as-needed

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4_20081207-alt1
- Version 1.4.4_20081207

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.6-alt1
- OFED 1.3.1

* Fri Feb 22 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt2
- fix /usr/local in scripts

* Mon Aug 27 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt1
- Initial build
