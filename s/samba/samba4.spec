%set_verify_elf_method unresolved=relaxed
%add_findprov_skiplist /%_lib/*
%add_debuginfo_skiplist /%_lib

%define rname samba
%define dcname samba-DC
%define _localstatedir /var
%define libwbc_alternatives_version 0.15

# internal libs
%def_without talloc
%def_without tevent
%def_without tdb
%def_without ldb
%def_with    winbind

%def_with profiling_data

# build as separate package
%def_with libsmbclient
%def_with libwbclient
%def_with libnetapi
%def_with doc

%def_with dc
%def_without ntvfs
%def_with clustering_support
%def_without testsuite

%if_with testsuite
# The testsuite only works with a full build right now.
%force_with dc
%endif

%if_with dc
%def_with ldb_modules
%endif

%def_with mitkrb5
%def_with separate_heimdal_server
%def_with systemd
%def_enable avahi

# https://bugzilla.altlinux.org/show_bug.cgi?id=36315
# Not all macroses exists on stable branches:
# ifarch %ix86 %arm %mips32 ppc %e2k
%ifarch %ix86 %arm mipsel ppc e2k e2kv4
%def_without libcephfs
%def_disable cephfs
%else
%def_with libcephfs
%def_enable cephfs
%endif

%ifarch e2k e2kv4
%def_disable glusterfs
%else
%def_enable glusterfs
%endif

Name:    samba
Version: 4.10.6
Release: alt2

Group:   System/Servers
Summary: The Samba4 CIFS and AD client and server suite
License: GPLv3+ and LGPLv3+
Url:     http://www.samba.org/

Source:  %rname-%version.tar

# Red Hat specific replacement-files
Source1: samba.log
Source5: smb.init
Source6: samba.pamd
Source8: winbind.init
Source9: smb.conf.default
Source10: nmb.init
Source11: pam_winbind.conf
Source12: ctdb.init
Source13: samba.limits
Source20: samba.init
Source21: smbusers

Source200: README.dc
Source201: README.downgrade

Patch: %rname-%version-alt.patch
Patch10: samba-grouppwd.patch

Provides: samba4 = %version-%release
Obsoletes: samba4 < %version-%release
Provides: samba-swat = %version-%release
Obsoletes: samba-swat < %version-%release

# Need for samba_upgradedns
Requires: tdb-utils

Requires(pre): %name-common = %version-%release
Requires: %name-libs = %version-%release
%if_with winbind
Requires: %name-winbind-clients = %version-%release
%endif
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif

BuildRequires: /proc
BuildRequires: libe2fs-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libgnutls-devel
BuildRequires: libncurses-devel
BuildRequires: libpam-devel
BuildRequires: perl-devel
BuildRequires: perl-Parse-Yapp
BuildRequires: libpopt-devel
BuildRequires: python-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libreadline-devel
BuildRequires: libldap-devel
BuildRequires: zlib-devel
BuildRequires: libarchive-devel >= 3.1.2
BuildRequires: libjansson-devel
BuildRequires: libgpgme-devel

%if_with mitkrb5
BuildRequires: libssl-devel
BuildRequires: libkrb5-devel
%if_with dc
BuildRequires: krb5-kdc
%endif
%endif
BuildRequires: glibc-devel glibc-kernheaders
# https://bugzilla.samba.org/show_bug.cgi?id=9863
BuildConflicts: setproctitle-devel
BuildRequires: libiniparser-devel
BuildRequires: libcups-devel
BuildRequires: gawk libgtk+2-devel libcap-devel libuuid-devel
%{?_with_doc:BuildRequires: inkscape libxslt xsltproc netpbm dblatex html2text docbook-style-xsl}
%if_without talloc
BuildRequires: libtalloc-devel >= 2.1.16
BuildRequires: python-module-talloc-devel
BuildRequires: python3-module-talloc-devel
%endif

%if_without tevent
BuildRequires: libtevent-devel >= 0.9.39
BuildRequires: python-module-tevent
BuildRequires: python3-module-tevent
%endif

%if_without tdb
BuildRequires: libtdb-devel >= 1.3.18
BuildRequires: python-module-tdb
BuildRequires: python3-module-tdb
%endif

%if_without ldb
%define ldb_version 1.5.5
BuildRequires: libldb-devel = %ldb_version
BuildRequires: python-module-pyldb-devel
BuildRequires: python3-module-pyldb-devel
%endif
%{?_with_testsuite:BuildRequires: ldb-tools}
%{?_with_systemd:BuildRequires: libsystemd-devel}
%{?_enable_avahi:BuildRequires: libavahi-devel}
%{?_enable_glusterfs:BuildRequires: glusterfs3-devel >= 3.4.0.16}
%{?_with_libcephfs:BuildRequires: ceph-devel}

%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

%package dc-common
Summary: Files used by MIT and Heimdal Active Directory Domain Services servers
Group: System/Servers

%description dc-common
%rname-dc-common provides files necessary for both MIT and Heimdal
Active Directory Domain Services servers separately builded and packaged.

%package dc
Summary: Samba Active Directory Domain Controller with Heimdal Kerberos
Group: Networking/Other
Obsoletes: %dcname < %version-%release
Provides: %dcname = %version-%release
Requires: %name-dc-client = %version-%release
Requires: %name-dc-common = %version-%release
%if_without separate_heimdal_server
Requires: %name = %version-%release
Requires: %name-dc-libs = %version-%release
%if_with mitkrb5
Requires: krb5-kdc
%endif
%else
Requires: tdb-utils
Requires: %name-winbind-common = %version-%release
Requires(pre): %name-common = %version-%release
%endif
Conflicts: %name-dc-mitkrb5

%description dc
Samba as Active Directory Domain Services (AD DS) also called a domain controller,
build with Heimdal Kerberos server and libraries.

%package dc-mitkrb5
Summary: Samba Active Directory Domain Controller with MIT Kerberos
Group: Networking/Other
Requires: %name-dc-libs = %version-%release
Requires: %name-dc-client = %version-%release
Requires: %name-dc-common = %version-%release
Requires: %name-winbind = %version-%release
Requires: krb5-kdc
Conflicts: %name-dc

%description dc-mitkrb5
Samba as Active Directory Domain Services (AD DS) also called a domain controller,
build with MIT Kerberos server and libraries.

%package client
Summary: Samba client programs
Group: Networking/Other
Requires: %name-common = %version-%release
Requires: %name-common-tools = %version-%release
Requires: %name-libs = %version-%release
%if_with libsmbclient
Requires: libsmbclient = %version-%release
%endif
Provides: samba-utils = %version-%release
Provides: samba-client-cups = %version-%release
Obsoletes: samba-client-cups < %version-%release

%description client
The %rname-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package dc-client
Summary: Samba Active Directory client programs
Group: Networking/Other
Requires: %name-client = %version-%release
Provides: %dcname-client = %version-%release
Obsoletes: %dcname-client < 4.10

%description dc-client
The %rname-client package provides Active Directory Domain Services clients.

%package common
Summary: Files used by both Samba servers and clients
Group: System/Servers
Requires: %name-libs = %version-%release
%if_with libnetapi
Requires: libnetapi = %version-%release
%endif
Provides: %dcname-common = %version-%release
Obsoletes: %dcname-common < 4.10

%description common
%rname-common provides files necessary for both the server and client
packages of Samba.

%package libs
Summary: Samba libraries
Group: System/Libraries
Requires: %name-common-libs = %version-%release

%if_with libnetapi
Requires: libnetapi = %version-%release
%endif
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif
%if_with libsmbclient
Requires: libsmbclient = %version-%release
%endif

%description libs
The %rname-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package vfs-cephfs
Summary: Samba VFS module for Ceph distributed storage system
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-libs = %version-%release

%description vfs-cephfs
Samba VFS module for Ceph distributed storage system integration.

%package vfs-glusterfs
Summary: Samba VFS module for GlusterFS
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-common-libs = %version-%release

%description vfs-glusterfs
Samba VFS module for GlusterFS integration.

%package dc-libs
Summary: Samba libraries
Group: System/Libraries
Requires: %name-libs = %version-%release
Provides: %dcname-libs = %version-%release
Obsoletes: %dcname-libs < 4.10

%if_with ldb_modules
Requires: libldb-modules-dc = %version-%release
%endif

%description dc-libs
The %rname-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package common-libs
Summary: Samba common libraries
Group: System/Libraries
Provides: %dcname-common-libs = %version-%release
Obsoletes: %dcname-common-libs < 4.10
Provides: %rname-client-libs = %version-%release
Obsoletes: %rname-client-libs < 4.10
%if_without ldb
Requires: libldb = %ldb_version
%endif

%description common-libs
The %rname-common-libs package contains the common libraries needed by modules that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package common-tools
Summary: Tools for Samba servers and clients
Group: System/Servers
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
Provides: %dcname-common-tools = %version-%release
Obsoletes: %dcname-common-tools < 4.10

%description common-tools
The %rname-common-tools package contains tools for Samba servers and
SMB/CIFS clients.

%package -n libsmbclient
Summary: The SMB client library
Group: System/Libraries
Provides: libsmbclient-DC = %version-%release
Obsoletes: libsmbclient-DC < 4.10

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libldb-modules-dc
Summary: The LDB domain controller modules
Group: System/Libraries
Provides: libldb-modules-DC = %version-%release
Obsoletes: libldb-modules-DC < 4.10

%description -n libldb-modules-dc
The libldb-modules-DC contains the ldb library modules from the Samba domain controller.

%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development/C
Requires: libsmbclient = %version-%release
Provides: libsmbclient-DC-devel = %version-%release
Obsoletes: libsmbclient-DC-devel < 4.10

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%package -n libwbclient
Summary: The winbind client library
Group: System/Libraries
Provides: libwbclient-DC = %version-%release
Obsoletes: libwbclient-DC < 4.10

%description -n libwbclient
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient-devel
Summary: Developer tools for the winbind library
Group: Development/C
Requires: libwbclient = %version-%release
Provides: libwbclient-DC-devel = %version-%release
Obsoletes: libwbclient-DC-devel < 4.10

%description -n libwbclient-devel
The libwbclient-devel package provides developer tools for the wbclient library.

%package -n libnetapi
Summary: Samba netapi library
Group: System/Libraries
Provides: libnetapi-DC = %version-%release
Obsoletes: libnetapi-DC < 4.10

%description -n libnetapi
Samba netapi library

%package -n libnetapi-devel
Summary: Samba netapi development files
Group: Development/Other
Requires: libnetapi = %version-%release
Conflicts: libnetapi-devel
Provides: libnetapi-DC-devel = %version-%release
Obsoletes: libnetapi-DC-devel < 4.10

%description -n libnetapi-devel
Samba netapi development files

%package -n python-module-%name
Summary: Samba Python libraries
Group: Networking/Other
Requires: %name-libs = %version-%release
Provides: python-module-%dcname = %version-%release
Obsoletes: python-module-%dcname < 4.10

%add_python_req_skip Tdb

%description -n python-module-%name
The %rname-python package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python programs.

%package -n python3-module-%name
Summary: Samba Python3 libraries
Group: Networking/Other
Requires: %name-libs = %version-%release
Provides: python3-module-%dcname = %version-%release
Obsoletes: python3-module-%dcname < 4.10

# these modules currently don't support Python3 and aren't packaged
%add_python3_req_skip dsdb
%add_python3_req_skip param
%add_python3_req_skip passdb
%add_python3_req_skip samba.dsdb

%add_python3_req_skip samba._ldb
%add_python3_req_skip samba.auth
%add_python3_req_skip samba.credentials
%add_python3_req_skip samba.dcerpc.base
%add_python3_req_skip samba.dcerpc.dnsp
%add_python3_req_skip samba.dcerpc.drsuapi
%add_python3_req_skip samba.dcerpc.misc
%add_python3_req_skip samba.dcerpc.netlogon
%add_python3_req_skip samba.dcerpc.samr
%add_python3_req_skip samba.dcerpc.security
%add_python3_req_skip samba.gpo
%add_python3_req_skip samba.messaging
%add_python3_req_skip samba.net
%add_python3_req_skip samba.netbios
%add_python3_req_skip samba.ntstatus
%add_python3_req_skip samba.param
%add_python3_req_skip samba.posix_eadb
%add_python3_req_skip samba.registry
%add_python3_req_skip samba.security
%add_python3_req_skip samba.xattr_native
%add_python3_req_skip samba.xattr_tdb

# Python3 not fully migrated yet
%add_python3_req_skip ConfigParser
%add_python3_req_skip StringIO

%description -n python3-module-%name
The %rname-python3 package contains the Python3 libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python3 programs.

%package -n python3-module-%name-devel
Summary: Samba Python3 development libraries
Group: Development/Other
Requires: python3-module-%name = %version-%release

%description -n python3-module-%name-devel
The python3-module-%name package contains the Python3 libraries development files.

%package devel
Summary: Developer tools for Samba libraries
Group: Development/C
Requires: %name-libs = %version-%release
Provides: %dcname-devel = %version-%release
Obsoletes: %dcname-devel < 4.10

%description devel
The %rname-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
BuildArch: noarch
# Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Provides: %dcname-pidl = %version-%release
Obsoletes: %dcname-pidl < 4.10

%description pidl
The %rname-pidl package contains the Perl IDL compiler used by Samba
and Wireshark to parse IDL and similar protocols

%package test
Summary: Testing tools for Samba servers and clients
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
%if_with winbind
Requires: %name-winbind = %version-%release
%endif
%if_with libsmbclient
Requires: libsmbclient = %version-%release
%endif
Provides: %dcname-test = %version-%release
Obsoletes: %dcname-test < 4.10

%description test
%rname-test provides testing tools for both the server and client
packages of Samba.

%if_with winbind
%package winbind-common
Summary: Files used by MIT and Heimdal Winbind servers
Group: System/Servers

%description winbind-common
%rname-winbind-common provides files necessary for both MIT and Heimdal
Winbind servers separately builded and packaged.

%package winbind
Summary: Samba winbind
Group: System/Servers
Requires: %name-winbind-common = %version-%release
Requires: %name-common = %version-%release
Requires: %name-libs = %version-%release
Provides: %dcname-winbind = %version-%release
Obsoletes: %dcname-winbind < 4.10
%if_with libwbclient
# There are working configurations exists where samba-winbind could be
# using with sssd. Also it could be already installed from installation DVD.
## Conflicts: libwbclient-sssd
Requires: libwbclient
%endif

%description winbind
The %rname-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%package winbind-clients
Summary: Samba winbind clients
Group: System/Servers
Requires: %name-winbind = %version-%release
Provides: %dcname-winbind-clients = %version-%release
Obsoletes: %dcname-winbind-clients < 4.10
%if_with libwbclient
Requires: libwbclient = %version-%release
%endif

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Group: System/Servers
%if_with libwbclient
Requires: libwbclient = %version-%release
%else
Requires: %name-libs = %version-%release
%endif
Provides: %dcname-winbind-krb5-locator = %version-%release
Obsoletes: %dcname-winbind-krb5-locator < 4.10

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

%package winbind-krb5-localauth
Summary: Samba winbind krb5 plugin for mapping user accounts
Group: System/Servers
%if_with libwbclient
Requires: libwbclient = %version-%release
%else
Requires: %name-libs = %version-%release
%endif
Provides: %dcname-winbind-krb5-localauth = %version-%release
Obsoletes: %dcname-winbind-krb5-localauth < 4.10

%description winbind-krb5-localauth
The winbind krb5 localauth is a plugin that permits the MIT Kerberos libraries
that Kerberos principals can be validated against local user accounts.

%if_with clustering_support
%package ctdb
Summary: A Clustered Database based on Samba's Trivial Database (TDB)
Group: System/Servers

Requires: %name-libs = %version-%release

# for ps and killall
Requires: psmisc
Requires: tdb-utils
# for pkill and pidof:
Requires: procps
# for netstat:
Requires: net-tools
Requires: ethtool
# for ip:
Requires: iproute
Requires: iptables
# for flock, getopt, kill:
Requires: util-linux
Conflicts: ctdb

%description ctdb
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

%package ctdb-tests
Summary: CTDB clustered database test suite
Group: Development/Other
Requires: %name-libs = %version-%release
Requires: %name-ctdb = %version-%release
Requires: nc
Conflicts: ctdb-tests
Conflicts: ctdb-devel
Provides:  %name-ctdb-devel = %version-%release
Obsoletes: %name-ctdb-devel < %version-%release
Provides: %dcname-ctdb-tests = %version-%release
Obsoletes: %dcname-ctdb-tests < 4.10

%description ctdb-tests
Test suite for CTDB.
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.
%endif

%if_with doc
%package doc
Summary: Documentation for the Samba suite
Group: Documentation
Requires: %name-common = %version-%release
BuildArch: noarch
Provides: %dcname-doc = %version-%release
Obsoletes: %dcname-doc < 4.10

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.
%endif

%package -n task-samba-dc
Summary: Complete Samba Active Directory Domain Controller with Heimdal Kerberos
Group: System/Servers
BuildArch: noarch
Provides: task-samba-ad-dc = %version-%release
Provides: task-ad-dc = %version-%release
Requires: samba-dc samba-winbind-clients %{?_with_doc:samba-doc} krb5-kinit ldb-tools

%description -n task-samba-dc
Samba server acts as a Domain Controller that is compatible with
Microsoft Active Directory.

%package -n task-samba-dc-mitkrb5
Summary: Complete Samba Active Directory Domain Controller with MIT Kerberos
Group: System/Servers
BuildArch: noarch
Requires: samba-dc-mitkrb5 %{?_with_doc:samba-doc} krb5-kinit ldb-tools

%description -n task-samba-dc-mitkrb5
Samba server acts as a Domain Controller that is compatible with
Microsoft Active Directory with MIT Kerberos server and libraries.

%package util-private-headers
Summary: libsamba_util private headers
Group: Development/C
Provides: %dcname-util-private-headers = %version-%release
Obsoletes: %dcname-util-private-headers < 4.10

%description util-private-headers
libsamba_util private headers.

%prep
%setup -q -n %rname-%version
%patch -p1
%patch10 -p1

%if_with separate_heimdal_server
rm -rf ../%rname-%version-separate-heimdal-server
cp -a ../%rname-%version ../%rname-%version-separate-heimdal-server
%endif

%build

%define _talloc_lib ,talloc,pytalloc,pytalloc-util
%if_without talloc
%define _talloc_lib ,!talloc,!pytalloc,!pytalloc-util
%endif

%define _tevent_lib ,tevent,pytevent
%if_without tevent
%define _tevent_lib ,!tevent,!pytevent
%endif

%define _tdb_lib ,tdb,pytdb
%if_without tdb
%define _tdb_lib ,!tdb,!pytdb
%endif

%define _ldb_lib ,ldb,pyldb,pyldb-util
%if_without ldb
%define _ldb_lib ,!ldb,!pyldb,!pyldb-util
%endif

%define _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ldb_lib}

%define _samba4_idmap_modules idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2
%define _samba4_pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%define _samba4_auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
# auth_domain needs to be static
%define _samba4_modules %_samba4_idmap_modules,%_samba4_pdb_modules,%_samba4_auth_modules

%define _libsmbclient %nil
%if_without libsmbclient
%define _libsmbclient smbclient,smbsharemodes,
%endif

%define _libwbclient %nil
%if_without libwbclient
%define _libwbclient wbclient,
%endif

%define _libnetapi %nil
%if_without libnetapi
%define _libnetapi netapi,
%endif

%define _samba4_private_libraries %{_libsmbclient}%{_libwbclient}%{_libnetapi}

%undefine _configure_gettext
%define _samba_libdir  %_libdir
%define _samba_mod_libdir  %_libdir/samba
%define _samba_dc_libdir  %_libdir/samba-dc
%define _samba_dc_mod_libdir  %_libdir/samba-dc
%define _wbclient_libdir %_samba_mod_libdir/wbclient
%define _samba_piddir /var/run
%define _samba_sockets_dir /var/run/samba

%define configure_common() \
	%configure \\\
	--enable-fhs \\\
	--with-piddir=%_samba_piddir \\\
	--with-sockets-dir=%_samba_sockets_dir \\\
	--with-lockdir=%_localstatedir/lib/samba \\\
	--with-cachedir=%_localstatedir/cache/samba \\\
	--with-privatedir=/var/lib/samba/private \\\
	--with-shared-modules=%_samba4_modules \\\
	--bundled-libraries=%_samba4_libraries \\\
	--with-ads \\\
	--with-pie \\\
	--with-relro \\\
	--without-fam \\\
	--private-libraries=%_samba4_private_libraries \\\
%if_with systemd \
	--with-systemd \\\
%else \
	--without-systemd \\\
%endif \
%if_with winbind \
	--with-winbind \\\
%else \
	--without-winbind \\\
%endif \
%if_with testsuite \
	--enable-selftest \\\
%endif \
%if_with profiling_data \
	--with-profiling-data \\\
%endif \
	%{subst_enable avahi} \\\
	--with-libcephfs-common=%_libdir/ceph \\\
	%{subst_enable cephfs} \\\
	%{subst_enable glusterfs} \\\
	%*

%configure_common \
%if_with mitkrb5 \
	--with-system-mitkrb5 \
%endif \
%if_without dc \
	--without-ad-dc \
%else \
%if_with mitkrb5 \
	--with-experimental-mit-ad-dc \
%endif \
%if_with ntvfs \
	--with-ntvfs-fileserver \
%endif \
%endif \
%if_with clustering_support \
	--with-cluster-support \
%endif \
	--extra-python=python2.7 \
	--libdir=%_samba_libdir \
	--with-modulesdir=%_samba_mod_libdir \
	--with-privatelibdir=%_samba_mod_libdir \
	--with-pammodulesdir=%_lib/security \
	--with-pam \
%endif

%if_with separate_heimdal_server
pushd ../%rname-%version-separate-heimdal-server

%configure_common \
	--libdir=%_samba_dc_libdir \
	--with-modulesdir=%_samba_dc_mod_libdir \
	--with-privatelibdir=%_samba_dc_mod_libdir \
	--without-pam

[ -n "$NPROCS" ] || NPROCS=%__nprocs; export JOBS=$NPROCS
%make_build NPROCS=%__nprocs

popd
%endif

[ -n "$NPROCS" ] || NPROCS=%__nprocs; export JOBS=$NPROCS
%make_build NPROCS=%__nprocs

%if_with doc
pushd docs-xml
export XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml"
%autoreconf
%configure
%make_build smbdotconf/parameters.all.xml
%make_build release
popd
%endif

%install
%if_without separate_heimdal_server
%makeinstall_std
%else
pushd ../%rname-%version-separate-heimdal-server

%makeinstall_std

popd

mkdir -p %buildroot%_altdir

mv %buildroot%python3_sitelibdir %buildroot%_samba_dc_mod_libdir/python%_python3_version
mv %buildroot%_bindir %buildroot%_samba_dc_mod_libdir/bin
mv %buildroot%_sbindir %buildroot%_samba_dc_mod_libdir/sbin
for f in samba samba_kcc samba_dnsupdate samba_spnupdate samba_upgradedns eventlogadm nmbd smbd winbindd; do
    printf "%_sbindir/$f\t%_samba_dc_mod_libdir/sbin/$f\t50\n" >> %buildroot%_altdir/samba-heimdal
done
printf "%_bindir/wbinfo\t%_samba_dc_mod_libdir/bin/wbinfo\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_bindir/ntlm_auth\t%_samba_dc_mod_libdir/bin/ntlm_auth\t50\n" >> %buildroot%_altdir/samba-heimdal
printf "%_samba_mod_libdir/ldb\t%_samba_dc_mod_libdir/ldb\t50\n" >> %buildroot%_altdir/samba-heimdal

printf '#!/bin/bash\nexport PYTHONPATH="%_samba_dc_mod_libdir/python%_python3_version"\nexec %_bindir/samba-tool.py3 "$@"\n' >%buildroot%_samba_dc_mod_libdir/bin/samba-tool
printf "%_bindir/samba-tool\t%_samba_dc_mod_libdir/bin/samba-tool\t50\n" >> %buildroot%_altdir/samba-heimdal
chmod 0755 %buildroot%_samba_dc_mod_libdir/bin/samba-tool

%makeinstall_std

rm -f %buildroot%_altdir/samba-mit
touch %buildroot%_altdir/samba-mit
mkdir %buildroot%_samba_mod_libdir/sbin
for f in eventlogadm nmbd smbd; do
    mv %buildroot%_sbindir/$f %buildroot%_samba_mod_libdir/sbin/
    printf "%_sbindir/$f\t%_samba_mod_libdir/sbin/$f\t20\n" >> %buildroot%_altdir/samba-mit
done
for f in samba samba_kcc samba_dnsupdate samba_spnupdate samba_upgradedns; do
    mv %buildroot%_sbindir/$f %buildroot%_samba_mod_libdir/sbin/
    printf "%_sbindir/$f\t%_samba_mod_libdir/sbin/$f\t20\n" >> %buildroot%_altdir/samba-mit-dc
done

mkdir %buildroot%_samba_mod_libdir/bin
mv %buildroot%_bindir/wbinfo %buildroot%_samba_mod_libdir/bin/
mv %buildroot%_bindir/ntlm_auth %buildroot%_samba_mod_libdir/bin/
mv %buildroot%_sbindir/winbindd %buildroot%_samba_mod_libdir/sbin/
printf "%_sbindir/winbindd\t%_samba_mod_libdir/sbin/winbindd\t20\n" > %buildroot%_altdir/samba-mit-winbind
printf "%_bindir/wbinfo\t%_samba_mod_libdir/bin/wbinfo\t20\n" >> %buildroot%_altdir/samba-mit-winbind
printf "%_bindir/ntlm_auth\t%_samba_mod_libdir/bin/ntlm_auth\t20\n" >> %buildroot%_altdir/samba-mit-winbind

mv %buildroot%_samba_mod_libdir/ldb %buildroot%_samba_mod_libdir/ldb.mit
printf "%_samba_mod_libdir/ldb\t%_samba_mod_libdir/ldb.mit\t50\n" > %buildroot%_altdir/samba-mit-dc-modules

mv %buildroot%_bindir/samba-tool %buildroot%_bindir/samba-tool.py3
printf '#!/bin/bash\nexec %_bindir/samba-tool.py3 "$@"\n' >%buildroot%_samba_mod_libdir/bin/samba-tool
printf "%_bindir/samba-tool\t%_samba_mod_libdir/bin/samba-tool\t20\n" > %buildroot%_altdir/samba-mit-dc-client
chmod 0755 %buildroot%_samba_mod_libdir/bin/samba-tool

%endif

mkdir -p %buildroot/sbin
mkdir -p %buildroot/usr/{sbin,bin}
mkdir -p %buildroot/%_lib/security
mkdir -p %buildroot/var/lib/samba
mkdir -p %buildroot/var/lib/ctdb
mkdir -p %buildroot%_localstatedir/cache/samba
mkdir -p %buildroot/var/lib/samba/{private,winbindd_privileged,scripts,sysvol}
mkdir -p %buildroot/var/log/samba/old
mkdir -p %buildroot/var/spool/samba
mkdir -p %buildroot%_samba_piddir/winbindd
mkdir -p %buildroot%_samba_sockets_dir
mkdir -p %buildroot%_samba_mod_libdir
mkdir -p %buildroot%_pkgconfigdir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/{pam.d,logrotate.d,security,sysconfig}


# Move libwbclient.so* into private directory, it cannot be just libdir/samba
# because samba uses rpath with this directory.
install -d -m 0755 %buildroot%_wbclient_libdir
mv %buildroot%_libdir/libwbclient.so* %buildroot%_wbclient_libdir
if [ ! -f %buildroot%_wbclient_libdir/libwbclient.so.%libwbc_alternatives_version ]
then
    echo "Expected libwbclient version not found, please check if version has changed."
    exit -1
fi
ln -s ../..%_wbclient_libdir/libwbclient.so.%libwbc_alternatives_version %buildroot%_libdir/
ln -s ../..%_wbclient_libdir/libwbclient.so.0 %buildroot%_libdir/
ln -s ../..%_wbclient_libdir/libwbclient.so %buildroot%_libdir/

# Add alternatives for libwbclient
mkdir -p %buildroot%_altdir
printf '%_libdir/libwbclient.so.%libwbc_alternatives_version\t%_wbclient_libdir/libwbclient.so.%libwbc_alternatives_version\t10\n' > %buildroot%_altdir/libwbclient-samba
printf '%_libdir/libwbclient.so.0\t%_wbclient_libdir/libwbclient.so.0\t10\n' >> %buildroot%_altdir/libwbclient-samba

printf '%_libdir/libwbclient.so\t%_wbclient_libdir/libwbclient.so\t10\n' > %buildroot%_altdir/libwbclient-devel-samba
mkdir -p %buildroot/lib/tmpfiles.d

# Install other stuff
install -m644 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/samba
install -m644 %SOURCE9 %buildroot%_sysconfdir/samba/smb.conf
install -m644 %SOURCE11 %buildroot%_sysconfdir/security
install -m644 %SOURCE6 %buildroot%_sysconfdir/pam.d/samba
echo 127.0.0.1 localhost > %buildroot%_sysconfdir/samba/lmhosts
mkdir -p %buildroot%_sysconfdir/openldap/schema
install -m644 examples/LDAP/samba.schema %buildroot%_sysconfdir/openldap/schema/samba.schema
install -m755 packaging/printing/smbprint %buildroot%_bindir/smbprint

cp packaging/systemd/samba.sysconfig packaging/systemd/samba.sysconfig.alt
echo "KRB5CCNAME=FILE:/run/samba/krb5cc_samba" >>packaging/systemd/samba.sysconfig.alt
install -m644 packaging/systemd/samba.sysconfig.alt %buildroot%_sysconfdir/sysconfig/samba
install -m644 %SOURCE21 %buildroot%_sysconfdir/samba/smbusers

install -m755 %SOURCE10 %buildroot%_initrddir/nmb
install -m755 %SOURCE5 %buildroot%_initrddir/smb
install -m755 %SOURCE8 %buildroot%_initrddir/winbind
%if_with dc
install -m755 %SOURCE20 %buildroot%_initrddir/samba
%endif

# Put README in builddir
cp %SOURCE200 %SOURCE201 .

for i in nmb smb winbind samba; do
    cat packaging/systemd/$i.service.in | sed -e 's|@PIDDIR@|%_samba_piddir|g' -e 's|@SYSCONFDIR@|%_sysconfdir|g' -e 's|@SBINDIR@|%_sbindir|g' \
        -e '/@systemd_smb_extra@/d' -e '/@systemd_nmb_extra@/d' -e '/@systemd_winbind_extra@/d' -e '/@systemd_samba_extra@/d'  >packaging/systemd/$i.service
    install -m 0644 packaging/systemd/$i.service %buildroot%_unitdir/$i.service
done
subst 's,Type=notify,Type=forking,' %buildroot%_unitdir/*.service
%if_with clustering_support
install -m755 %SOURCE12 %buildroot%_initrddir/ctdb
install -m 0644 ctdb/config/ctdb.service %buildroot%_unitdir
echo "d %_samba_piddir/ctdb 755 root root" >> %buildroot%_tmpfilesdir/ctdb.conf
touch %buildroot%_sysconfdir/ctdb/nodes
%endif

install -m644 packaging/systemd/samba.conf.tmp %buildroot%_tmpfilesdir/%rname.conf

# NetworkManager online/offline script
install -d -m 0755 %buildroot%_sysconfdir/NetworkManager/dispatcher.d/
install -m 0755 packaging/NetworkManager/30-winbind-systemd \
            %buildroot%_sysconfdir/NetworkManager/dispatcher.d/30-winbind


# Clean out crap left behind by the PIDL install.
find %buildroot -type f -name .packlist -exec rm -f {} \;
rm -f %buildroot%perl_vendorlib/wscript_build
rm -rf %buildroot%perl_vendorlib/Parse/Yapp

# winbind
%if_with winbind
mkdir -p %buildroot/%_lib
ln -sf ..%_samba_libdir/libnss_winbind.so %buildroot/%_lib/libnss_winbind.so.2
ln -sf ..%_samba_libdir/libnss_wins.so    %buildroot/%_lib/libnss_wins.so.2

mkdir -p  %buildroot%_libdir/krb5/plugins/libkrb5
mv %buildroot%_samba_mod_libdir/krb5/winbind_krb5_locator.so %buildroot%_libdir/krb5/plugins/libkrb5/
%if_with mitkrb5
mv %buildroot%_samba_mod_libdir/krb5/winbind_krb5_localauth.so %buildroot%_libdir/krb5/plugins/libkrb5/
%endif
%endif

#cups backend
%define cups_serverbin %(cups-config --serverbin 2>/dev/null)
mkdir -p %buildroot%{cups_serverbin}/backend
ln -s %_bindir/smbspool %buildroot%{cups_serverbin}/backend/smb

# Fix up permission on perl install.
%_fixperms %buildroot%perl_vendor_privlib

# remove tests form python modules
rm -rf %buildroot%python_sitelibdir/samba/{tests,subunit,external/subunit,external/testtool}
rm -f %buildroot%python_sitelibdir/samba/third_party/iso8601/test_*.py
rm -rf %buildroot%python3_sitelibdir/samba/{tests,subunit,external/subunit,external/testtool}
rm -f %buildroot%python3_sitelibdir/samba/third_party/iso8601/test_*.py
%if_with separate_heimdal_server
rm -rf %buildroot%_samba_dc_mod_libdir/python%_python3_version/samba/{tests,subunit,external/subunit,external/testtool}
rm -f %buildroot%_samba_dc_mod_libdir/python%_python3_version/samba/third_party/iso8601/test_*.py
%endif

# remove cmocka library
rm -f %buildroot%_samba_mod_libdir/libcmocka-samba4.so
%if_with separate_heimdal_server
rm -f %buildroot%_samba_dc_mod_libdir/libcmocka-samba4.so
%endif

# move pkgconfig to standart path:
[ "%_libdir" != "%_samba_libdir" ] && mv %buildroot{%_samba_libdir/pkgconfig,%_libdir}

# Install documentation
%if_with doc
mkdir -p %buildroot%_defaultdocdir/%rname/
cp -a docs-xml/output/htmldocs %buildroot%_defaultdocdir/%rname/
%endif

# Cleanup man pages
%if_without libsmbclient
/bin/rm -f %buildroot%_man7dir/libsmbclient.7*
%endif

# Install pidl/lib/Parse/Pidl/Samba3/Template.pm
cp -a pidl/lib/Parse/Pidl/Samba3/Template.pm %buildroot%_datadir/perl5/Parse/Pidl/Samba3/

# Copy libsamba_util private headers
mkdir -p %buildroot%_includedir/samba-4.0/private/lib/util/charset
cp lib/util/*.h %buildroot%_includedir/samba-4.0/private/lib/util
cp lib/util/charset/*.h %buildroot%_includedir/samba-4.0/private/lib/util/charset
mkdir -p %buildroot%_includedir/samba-4.0/private/libcli/util
cp libcli/util/*.h %buildroot%_includedir/samba-4.0/private/libcli/util
subst 's,\.\./,,' %buildroot%_includedir/samba-4.0/private/lib/util/*.h

# Install limits
mkdir -p %buildroot%_sysconfdir/security/limits.d/
install -m644 %SOURCE13 %buildroot%_sysconfdir/security/limits.d/90-samba.conf

# Install traffic tools
install -m755 script/traffic_learner %buildroot%_bindir/traffic_learner
install -m755 script/traffic_replay %buildroot%_bindir/traffic_replay
#install -m755 script/traffic_summary.pl %buildroot%_bindir/traffic_summary (perl-XML-Twig requires)

%find_lang pam_winbind
%find_lang net

%if_with testsuite
%check
TDB_NO_FSYNC=1 %make_build test
%endif

%post
%post_service smb
%post_service nmb

%preun
%preun_service smb
%preun_service nmb

%if_with dc
%post dc
%post_service samba

%preun dc
%preun_service samba
%endif

%if_with winbind
%pre winbind-common
%_sbindir/groupadd -f -r wbpriv >/dev/null 2>&1 || :

%post winbind
%post_service winbind

%preun winbind
%preun_service winbind
%endif

%files
%doc COPYING README.md WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%doc README.downgrade
%if_with separate_heimdal_server
%_altdir/samba-mit
%_samba_mod_libdir/sbin/eventlogadm
%_samba_mod_libdir/sbin/nmbd
%_samba_mod_libdir/sbin/smbd
%else
%_sbindir/eventlogadm
%_sbindir/nmbd
%_sbindir/smbd
%endif
%config(noreplace) %_sysconfdir/samba/smbusers
%attr(755,root,root) %_initdir/smb
%attr(755,root,root) %_initdir/nmb
%_unitdir/nmb.service
%_unitdir/smb.service

%if_with dc
%files dc-common
%attr(755,root,root) %_initdir/samba
%_unitdir/samba.service
%dir /var/lib/samba/sysvol
%_datadir/samba/setup
%if_with doc
%_man8dir/samba.8*
%endif #doc

%files dc
%if_without separate_heimdal_server
%_sbindir/samba
%_sbindir/samba_kcc
%_sbindir/samba_dnsupdate
%_sbindir/samba_spnupdate
%_sbindir/samba_upgradedns
%else #!separate_heimdal_server
%doc COPYING README.md WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%_altdir/samba-heimdal
#_samba_dc_mod_libdir/sbin/eventlogadm
#_samba_dc_mod_libdir/sbin/nmbd
#_samba_dc_mod_libdir/sbin/smbd
#_samba_dc_mod_libdir/sbin/samba
#_samba_dc_mod_libdir/sbin/samba_kcc
#_samba_dc_mod_libdir/sbin/samba_dnsupdate
#_samba_dc_mod_libdir/sbin/samba_spnupdate
#_samba_dc_mod_libdir/sbin/samba_upgradedns
#_samba_dc_mod_libdir/sbin/winbindd
#_samba_dc_mod_libdir/bin/
%dir %_samba_dc_mod_libdir
%_samba_dc_libdir/

%files dc-mitkrb5
%_altdir/samba-mit-dc
%_samba_mod_libdir/sbin/samba
%_samba_mod_libdir/sbin/samba_kcc
%_samba_mod_libdir/sbin/samba_dnsupdate
%_samba_mod_libdir/sbin/samba_spnupdate
%_samba_mod_libdir/sbin/samba_upgradedns

%files -n task-samba-dc-mitkrb5
%endif

%files dc-client
%if_with separate_heimdal_server
%_altdir/samba-mit-dc-client
%_samba_mod_libdir/bin/samba-tool
%_bindir/samba-tool.py3
%else
%_bindir/samba-tool
%endif
%_sbindir/samba-gpupdate
%if_with doc
%_man8dir/samba-tool.8*
%_man8dir/samba-gpupdate.8*
%endif #doc
%endif #dc

%files client
%_bindir/cifsdd
%_bindir/dbwrap_tool
%_bindir/findsmb
%_bindir/nmblookup
%_bindir/oLschema2ldif
%_bindir/regdiff
%_bindir/regpatch
%_bindir/regshell
%_bindir/regtree
%_bindir/rpcclient
%_bindir/samba-regedit
%_bindir/sharesec
%_bindir/smbcacls
%_bindir/smbclient
%_bindir/smbcquotas
%_bindir/smbget
%_bindir/smbpasswd
%_bindir/smbprint
%_bindir/smbspool
#_bindir/smbta-util
%_bindir/smbtar
%_bindir/smbtree
%_libexecdir/samba/smbspool_krb5_wrapper
%{cups_serverbin}/backend/smb
%if_with doc
%_man1dir/dbwrap_tool.1*
%_man1dir/nmblookup.1*
%_man1dir/oLschema2ldif.1*
%_man1dir/regdiff.1*
%_man8dir/samba-regedit.8*
%_man1dir/regpatch.1*
%_man1dir/regshell.1*
%_man1dir/regtree.1*
%exclude %_man1dir/findsmb.1*
%_man1dir/log2pcap.1*
%_man1dir/rpcclient.1*
%_man1dir/sharesec.1*
%_man1dir/smbcacls.1*
%_man1dir/smbclient.1*
%_man1dir/smbcquotas.1*
%_man1dir/smbget.1*
%_man5dir/smbgetrc.5*
%exclude %_man1dir/smbtar.1*
%_man1dir/smbtree.1*
%_man5dir/smbpasswd.5*
%_man8dir/smbpasswd.8*
%_man8dir/smbspool.8*
%_man8dir/smbspool_krb5_wrapper.8*
#_man8dir/smbta-util.8*
%_man8dir/cifsdd.8*
%endif

%if_with tdb
%_bindir/tdbbackup
%_bindir/tdbdump
%_bindir/tdbrestore
%_bindir/tdbtool
%if_with doc
%_man8dir/tdbbackup.8*
%_man8dir/tdbdump.8*
%_man8dir/tdbrestore.8*
%_man8dir/tdbtool.8*
%endif #doc
%endif #tdb

%if_with ldb
%_bindir/ldbadd
%_bindir/ldbdel
%_bindir/ldbedit
%_bindir/ldbmodify
%_bindir/ldbrename
%_bindir/ldbsearch
%if_with doc
%_man1dir/ldbadd.1*
%_man1dir/ldbdel.1*
%_man1dir/ldbedit.1*
%_man1dir/ldbmodify.1*
%_man1dir/ldbrename.1*
%_man1dir/ldbsearch.1*
%endif
%_samba_mod_libdir/libldb-cmdline.so
%endif

%files common
%_tmpfilesdir/%rname.conf
%config(noreplace) %_sysconfdir/logrotate.d/samba
%config(noreplace) %_sysconfdir/security/limits.d/90-samba.conf
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%dir %_samba_piddir/winbindd
%dir %_samba_sockets_dir
%attr(755,root,root) %dir %_localstatedir/cache/samba
%attr(710,root,root) %dir /var/lib/samba/private
%attr(755,root,root) %dir %_sysconfdir/samba
%config(noreplace) %_sysconfdir/samba/smb.conf
%config(noreplace) %_sysconfdir/samba/lmhosts
%config(noreplace) %_sysconfdir/sysconfig/samba
%attr(1777,root,root) %dir /var/spool/samba
%_sysconfdir/openldap/schema/samba.schema
%_sysconfdir/pam.d/samba
%if_with doc
%_man5dir/lmhosts.5*
%_man5dir/smb.conf.5*
%_man7dir/samba.7*

%_man8dir/eventlogadm.8*
%_man8dir/smbd.8*
%_man8dir/nmbd.8*
%_man8dir/vfs_*.8*

%if_with libcephfs
%exclude %_man8dir/vfs_ceph.8*
%endif
%if_enabled glusterfs
%exclude %_man8dir/vfs_glusterfs.8*
%endif
%endif #doc

%files common-tools -f net.lang
%_bindir/mvxattr
%_bindir/net
%_bindir/pdbedit
%_bindir/profiles
%_bindir/smbcontrol
%_bindir/smbstatus
%_bindir/testparm
%if_with doc
%_man1dir/mvxattr.1*
%_man1dir/profiles.1*
%_man1dir/smbcontrol.1*
%_man1dir/smbstatus.1*
%_man1dir/testparm.1*
%_man8dir/net.8*
%_man8dir/pdbedit.8*
%endif #doc

# common libraries
%_samba_mod_libdir/libpopt-samba3-samba4.so
%_samba_mod_libdir/libcmdline-contexts-samba4.so
%_samba_mod_libdir/libpopt-samba3-cmdline-samba4.so
%_samba_mod_libdir/pdb

%files devel
%_includedir/samba-4.0

%exclude %_includedir/samba-4.0/netapi.h
%exclude %_includedir/samba-4.0/private
#%exclude %_includedir/samba-4.0/torture.h

%if_with libsmbclient
%exclude %_includedir/samba-4.0/libsmbclient.h
%endif
%if_with libwbclient
%exclude %_includedir/samba-4.0/wbclient.h
%endif

%_samba_libdir/libdcerpc-binding.so
%_samba_libdir/libdcerpc-samr.so
%_samba_libdir/libdcerpc.so
%_samba_libdir/libndr-krb5pac.so
%_samba_libdir/libndr-nbt.so
%_samba_libdir/libndr-standard.so
%_samba_libdir/libndr.so
%_samba_libdir/libsamba-credentials.so
%_samba_libdir/libsamba-errors.so
%_samba_libdir/libsamba-hostconfig.so
%_samba_libdir/libsamba-policy.so
%_samba_libdir/libsamba-util.so
%_samba_libdir/libsamdb.so
%_samba_libdir/libsmbconf.so
%_samba_libdir/libtevent-util.so
%_samba_libdir/libsamba-passdb.so
%_samba_libdir/libsmbldap.so

%_pkgconfigdir/dcerpc.pc
%_pkgconfigdir/dcerpc_samr.pc
%_pkgconfigdir/ndr.pc
%_pkgconfigdir/ndr_krb5pac.pc
%_pkgconfigdir/ndr_nbt.pc
%_pkgconfigdir/ndr_standard.pc
%_pkgconfigdir/samba-credentials.pc
%_pkgconfigdir/samba-hostconfig.pc
%_pkgconfigdir/samba-policy.pc
%_pkgconfigdir/samba-util.pc
%_pkgconfigdir/samdb.pc

%if_with dc
%_samba_libdir/libdcerpc-server.so
%_pkgconfigdir/dcerpc_server.pc
%endif

%files common-libs
%_samba_libdir/libdcerpc-binding.so.*
%_samba_libdir/libdcerpc-samr.so.*
%_samba_libdir/libdcerpc.so.*
%_samba_libdir/libndr-krb5pac.so.*
%_samba_libdir/libndr-nbt.so.*
%_samba_libdir/libndr-standard.so.*
%_samba_libdir/libndr.so.*
%_samba_libdir/libsamba-credentials.so.*
%_samba_libdir/libsamba-errors.so.*
%_samba_libdir/libsamba-hostconfig.so.*
%_samba_libdir/libsamba-policy.so.*
%_samba_libdir/libsamba-util.so.*
%_samba_libdir/libsamdb.so.*
%_samba_libdir/libsmbconf.so.*
%_samba_libdir/libtevent-util.so.*
%_samba_libdir/libsamba-passdb.so.*
%_samba_libdir/libsmbldap.so.*

%files libs
%_samba_mod_libdir/auth
%_samba_mod_libdir/vfs

%if_with libcephfs
%exclude %_samba_mod_libdir/vfs/ceph.so
%endif

%if_enabled glusterfs
%exclude %_samba_mod_libdir/vfs/glusterfs.so
%endif

# libraries needed by the public libraries
%_samba_mod_libdir/libCHARSET3-samba4.so
%_samba_mod_libdir/libMESSAGING-samba4.so
%_samba_mod_libdir/libMESSAGING-SEND-samba4.so
%_samba_mod_libdir/libLIBWBCLIENT-OLD-samba4.so
%_samba_mod_libdir/libaddns-samba4.so
%_samba_mod_libdir/libads-samba4.so
%_samba_mod_libdir/libasn1util-samba4.so
%_samba_mod_libdir/libauth-samba4.so
%_samba_mod_libdir/libauth4-samba4.so
%_samba_mod_libdir/libauth-unix-token-samba4.so
%_samba_mod_libdir/libauthkrb5-samba4.so
%_samba_mod_libdir/libcli-ldap-common-samba4.so
%_samba_mod_libdir/libcli-ldap-samba4.so
%_samba_mod_libdir/libcli-nbt-samba4.so
%_samba_mod_libdir/libcli-cldap-samba4.so
%_samba_mod_libdir/libcli-smb-common-samba4.so
%_samba_mod_libdir/libcli-spoolss-samba4.so
%_samba_mod_libdir/libcliauth-samba4.so
%_samba_mod_libdir/libclidns-samba4.so
%_samba_mod_libdir/libcluster-samba4.so
%_samba_mod_libdir/libcmdline-credentials-samba4.so
%_samba_mod_libdir/libcommon-auth-samba4.so
%_samba_mod_libdir/libdbwrap-samba4.so
%_samba_mod_libdir/libdcerpc-samba-samba4.so
%_samba_mod_libdir/libdcerpc-samba4.so
%_samba_mod_libdir/libevents-samba4.so
%_samba_mod_libdir/libflag-mapping-samba4.so
%_samba_mod_libdir/libgenrand-samba4.so
%_samba_mod_libdir/libgensec-samba4.so
%_samba_mod_libdir/libgse-samba4.so
%_samba_mod_libdir/libgpext-samba4.so
%if_with dc
%_samba_mod_libdir/libdfs-server-ad-samba4.so
%endif
%_samba_mod_libdir/libhttp-samba4.so
%_samba_mod_libdir/libinterfaces-samba4.so
%_samba_mod_libdir/libiov-buf-samba4.so
%_samba_mod_libdir/libkrb5samba-samba4.so
%_samba_mod_libdir/libldbsamba-samba4.so
%_samba_mod_libdir/liblibcli-lsa3-samba4.so
%_samba_mod_libdir/liblibcli-netlogon3-samba4.so
%_samba_mod_libdir/liblibsmb-samba4.so
%_samba_mod_libdir/libmessages-dgm-samba4.so
%_samba_mod_libdir/libmessages-util-samba4.so
%_samba_mod_libdir/libmsghdr-samba4.so
%_samba_mod_libdir/libsmb-transport-samba4.so
%_samba_mod_libdir/libmsrpc3-samba4.so
%_samba_mod_libdir/libndr-samba-samba4.so
%_samba_mod_libdir/libndr-samba4.so
%_samba_mod_libdir/libnet-keytab-samba4.so
%_samba_mod_libdir/libnetif-samba4.so
%_samba_mod_libdir/libnon-posix-acls-samba4.so
%_samba_mod_libdir/libnpa-tstream-samba4.so
%_samba_mod_libdir/libposix-eadb-samba4.so
%_samba_mod_libdir/libprinting-migrate-samba4.so
%_samba_mod_libdir/libregistry-samba4.so
%_samba_mod_libdir/libsamba-cluster-support-samba4.so
%_samba_mod_libdir/libsamba-debug-samba4.so
%_samba_mod_libdir/libsamba-modules-samba4.so
%_samba_mod_libdir/libsamba-net-samba4.so
%_samba_mod_libdir/libsamba-security-samba4.so
%_samba_mod_libdir/libsamba-sockets-samba4.so
%_samba_mod_libdir/libsamba-python-samba4.so
%_samba_mod_libdir/libsamdb-common-samba4.so
%_samba_mod_libdir/libsecrets3-samba4.so
%_samba_mod_libdir/libserver-id-db-samba4.so
%_samba_mod_libdir/libserver-role-samba4.so
%_samba_mod_libdir/libshares-samba4.so
%_samba_mod_libdir/libsamba3-util-samba4.so
%_samba_mod_libdir/libsmbclient-raw-samba4.so
%_samba_mod_libdir/libsmbd-base-samba4.so
%_samba_mod_libdir/libsmbd-conn-samba4.so
%_samba_mod_libdir/libsmbd-shim-samba4.so
%_samba_mod_libdir/libsmbldaphelper-samba4.so
%_samba_mod_libdir/libsmbpasswdparser-samba4.so
%_samba_mod_libdir/libsys-rw-samba4.so
%_samba_mod_libdir/libsocket-blocking-samba4.so
%_samba_mod_libdir/libtalloc-report-samba4.so
%_samba_mod_libdir/libtdb-wrap-samba4.so
%_samba_mod_libdir/libtime-basic-samba4.so
%_samba_mod_libdir/libtorture-samba4.so
%_samba_mod_libdir/libtrusts-util-samba4.so
%_samba_mod_libdir/libutil-cmdline-samba4.so
%_samba_mod_libdir/libutil-reg-samba4.so
%_samba_mod_libdir/libutil-setid-samba4.so
%_samba_mod_libdir/libutil-tdb-samba4.so
%_samba_mod_libdir/libxattr-tdb-samba4.so

%if_with libcephfs
%files vfs-cephfs
%_samba_mod_libdir/vfs/ceph.so
%_man8dir/vfs_ceph.8*
%endif

%if_enabled glusterfs
%files vfs-glusterfs
%_samba_mod_libdir/vfs/glusterfs.so
%_man8dir/vfs_glusterfs.8*
%endif

%if_with clustering_support
%_samba_mod_libdir/libctdb-event-client-samba4.so
%endif

%if_with ldb
%_samba_mod_libdir/libldb.so.*
%_samba_mod_libdir/libpyldb-util.so.*
%endif
%if_with talloc
%_samba_mod_libdir/libtalloc.so.*
%_samba_mod_libdir/libpytalloc-util.so.*
%endif
%if_with tevent
%_samba_mod_libdir/libtevent.so.*
%endif
%if_with tdb
%_samba_mod_libdir/libtdb.so.*
%endif
%if_without libsmbclient
%_samba_mod_libdir/libsmbclient.so.*
%endif
%if_without libwbclient
%_samba_mod_libdir/libreplace-samba4.so
%_samba_mod_libdir/libwbclient.so.*
%_samba_mod_libdir/libwinbind-client-samba4.so
%endif
%if_without libnetapi
%_samba_mod_libdir/libnetapi.so.*
%endif


%if_with dc
%files dc-libs
%_samba_mod_libdir/bind9/dlz_bind9.so
%_samba_mod_libdir/bind9/dlz_bind9_9.so
%_samba_mod_libdir/bind9/dlz_bind9_10.so
%_samba_mod_libdir/bind9/dlz_bind9_11.so
%_samba_mod_libdir/bind9/dlz_bind9_12.so
%if_without mitkrb5
%_samba_mod_libdir/libheimntlm-samba4.so.1
%_samba_mod_libdir/libheimntlm-samba4.so.1.0.1
%_samba_mod_libdir/libkdc-samba4.so.2
%_samba_mod_libdir/libkdc-samba4.so.2.0.0
%_samba_mod_libdir/libpac-samba4.so
%endif #!mitkrb5
%_samba_mod_libdir/libdnsserver-common-samba4.so
%_samba_mod_libdir/libdsdb-module-samba4.so
%_samba_mod_libdir/libdsdb-garbage-collect-tombstones-samba4.so
%_samba_mod_libdir/libscavenge-dns-records-samba4.so
%if_without ldb_modules
%if_with separate_heimdal_server
%_altdir/samba-mit-dc-modules
%_samba_mod_libdir/ldb.mit
%else
%_samba_mod_libdir/ldb
%endif
%endif
%_samba_mod_libdir/gensec
%_samba_mod_libdir/libdb-glue-samba4.so
%if_without mitkrb5
%_samba_mod_libdir/libHDB-SAMBA4-samba4.so
%_samba_mod_libdir/libasn1-samba4.so.*
%_samba_mod_libdir/libcom_err-samba4.so.*
%_samba_mod_libdir/libgssapi-samba4.so.*
%_samba_mod_libdir/libhcrypto-samba4.so.*
%_samba_mod_libdir/libhdb-samba4.so.*
%_samba_mod_libdir/libheimbase-samba4.so.*
%_samba_mod_libdir/libhx509-samba4.so.*
%_samba_mod_libdir/libkrb5-samba4.so.*
%_samba_mod_libdir/libroken-samba4.so.*
%_samba_mod_libdir/libwind-samba4.so.*
%else
%_samba_mod_libdir/libpac-samba4.so
%_samba_libdir/krb5/plugins/kdb/samba.so
%endif #!mitkrb5
%_samba_mod_libdir/libprocess-model-samba4.so
%_samba_mod_libdir/libservice-samba4.so
%_samba_mod_libdir/process_model
%_samba_mod_libdir/service
%_samba_libdir/libdcerpc-server.so.*
%if_with ntvfs
%_samba_mod_libdir/libntvfs-samba4.so
%endif
%else
%doc README.dc-libs
%_samba_mod_libdir/libdnsserver-common-samba4.so
%endif

%if_with ldb_modules
%files -n libldb-modules-dc
%if_with separate_heimdal_server
%_altdir/samba-mit-dc-modules
%_samba_mod_libdir/ldb.mit
%else
%_samba_mod_libdir/ldb
%endif
%endif

%if_with libsmbclient
%files -n libsmbclient
%_samba_libdir/libsmbclient.so.*

%files -n libsmbclient-devel
%_includedir/samba-4.0/libsmbclient.h
%_samba_libdir/libsmbclient.so
%_pkgconfigdir/smbclient.pc
%if_with doc
%_man7dir/libsmbclient.7*
%endif #doc
%endif

%if_with libwbclient
%files -n libwbclient
%ghost %_libdir/libwbclient.so.*
%_wbclient_libdir/libwbclient.so.*
%_samba_mod_libdir/libwinbind-client-samba4.so
%_samba_mod_libdir/libreplace-samba4.so
%_altdir/libwbclient-samba

%files -n libwbclient-devel
%_includedir/samba-4.0/wbclient.h
%ghost %_libdir/libwbclient.so
%_wbclient_libdir/libwbclient.so
%_pkgconfigdir/wbclient.pc
%_altdir/libwbclient-devel-samba
%endif

%if_with libnetapi
%files -n libnetapi
%_samba_libdir/libnetapi.so.*

%files -n libnetapi-devel
%_samba_libdir/libnetapi.so
%_includedir/samba-4.0/netapi.h
%_pkgconfigdir/netapi.pc
%endif

%files pidl
%attr(755,root,root) %_bindir/pidl
%if_with doc
%_man1dir/pidl.1.*
%_man3dir/Parse::Pidl::*
%endif
%perl_vendor_privlib/*

%files -n python-module-%name
%python_sitelibdir/samba/

%files -n python3-module-%name
%python3_sitelibdir/samba/
%_libdir/libsamba*.cpython-*.so.*
%_samba_mod_libdir/libsamba*.cpython-*.so

%files -n python3-module-%name-devel
%_pkgconfigdir/samba*.cpython-*.pc
%_libdir/libsamba*.cpython-*.so

%if_with doc
%files doc
%doc %_defaultdocdir/%rname/htmldocs
%endif

%files test
%_bindir/gentest
%_bindir/locktest
%_bindir/masktest
%_bindir/ndrdump
%_bindir/smbtorture
%_bindir/traffic_learner
%_bindir/traffic_replay
#%_samba_libdir/libtorture.so.*
%if_with dc
%_samba_mod_libdir/libdlz-bind9-for-torture-samba4.so
%else
%_samba_mod_libdir/libdsdb-module-samba4.so
%endif
%if_with doc
%_man1dir/gentest.1*
%_man1dir/locktest.1*
%_man1dir/masktest.1*
%_man1dir/ndrdump.1*
%_man1dir/smbtorture.1*
%_man1dir/vfstest.1*
%_man7dir/traffic_learner.7*
%_man7dir/traffic_replay.7*
%endif

%if_with testsuite
# files to ignore in testsuite mode
%_samba_mod_libdir/libnss-wrapper-samba4.so
%_samba_mod_libdir/libsocket-wrapper-samba4.so
%_samba_mod_libdir/libuid-wrapper-samba4.so
%endif

%if_with winbind
%files winbind-common
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%_unitdir/winbind.service
%attr(755,root,root) %_initrddir/winbind
%_sysconfdir/NetworkManager/dispatcher.d/30-winbind
%if_with doc
%_man8dir/winbindd.8*
%_man8dir/idmap_*.8*
%endif

%files winbind -f pam_winbind.lang
%_samba_mod_libdir/idmap
%_samba_mod_libdir/nss_info
%_samba_mod_libdir/libnss-info-samba4.so
%_samba_mod_libdir/libidmap-samba4.so
%if_with separate_heimdal_server
%_altdir/samba-mit-winbind
%_samba_mod_libdir/sbin/winbindd
%_samba_mod_libdir/bin/wbinfo
%_samba_mod_libdir/bin/ntlm_auth
%else
%_bindir/ntlm_auth
%_bindir/wbinfo
%_sbindir/winbindd
%endif

%files winbind-clients
%_samba_libdir/libnss_winbind.so*
/%_lib/libnss_winbind.so.*
%_samba_libdir/libnss_wins.so*
/%_lib/libnss_wins.so.*
/%_lib/security/pam_winbind.so
%config(noreplace) %_sysconfdir/security/pam_winbind.conf
%if_with doc
%_man1dir/ntlm_auth.1.*
%_man1dir/wbinfo.1*
%_man5dir/pam_winbind.conf.5*
%_man8dir/pam_winbind.8*
%endif

%files winbind-krb5-locator
%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so
%if_with doc
%_man8dir/winbind_krb5_locator.8*
%endif #doc
%endif

%if_with mitkrb5
%files winbind-krb5-localauth
%_libdir/krb5/plugins/libkrb5/winbind_krb5_localauth.so
%if_with doc
%_man8dir/winbind_krb5_localauth.8*
%endif #doc
%endif

%if_with clustering_support
%files ctdb
#doc ctdb/README
%dir %_sysconfdir/ctdb
%config(noreplace) %_sysconfdir/ctdb/nodes
%config(noreplace) %_sysconfdir/ctdb/notify.sh
%config(noreplace) %_sysconfdir/ctdb/debug-hung-script.sh
%config(noreplace) %_sysconfdir/ctdb/ctdb-crash-cleanup.sh
%config(noreplace) %_sysconfdir/ctdb/functions
%config(noreplace) %_sysconfdir/ctdb/debug_locks.sh
%_sysconfdir/ctdb/statd-callout
%dir /var/lib/ctdb
%_unitdir/ctdb.service
%_initdir/ctdb
%_tmpfilesdir/ctdb.conf

%_sysconfdir/ctdb/nfs-checks.d
%_sysconfdir/ctdb/nfs-linux-kernel-callout
%_sysconfdir/sudoers.d/ctdb
%dir %_sysconfdir/ctdb/events
%dir %_sysconfdir/ctdb/events/notification
%dir %_sysconfdir/ctdb/events/legacy
%_sysconfdir/ctdb/events/notification/README
%dir %_datadir/ctdb/events/legacy
%_datadir/ctdb/events/legacy/*.script
%_sbindir/ctdbd
%_sbindir/ctdbd_wrapper
%_bindir/ctdb
%_bindir/ctdb_diagnostics
%_bindir/ctdb_local_daemons
%_bindir/ltdbtool
%_bindir/onnode
%_bindir/ping_pong
%_libexecdir/ctdb/ctdb-config
%_libexecdir/ctdb/ctdb-event
%_libexecdir/ctdb/ctdb-eventd
%_libexecdir/ctdb/ctdb-path
%_libexecdir/ctdb/ctdb_killtcp
%_libexecdir/ctdb/ctdb_lock_helper
%_libexecdir/ctdb/ctdb_lvs
%_libexecdir/ctdb/ctdb_mutex_fcntl_helper
%_libexecdir/ctdb/ctdb_natgw
%_libexecdir/ctdb/ctdb_recovery_helper
%_libexecdir/ctdb/ctdb_takeover_helper
%_libexecdir/ctdb/smnotify

%if_with doc
%_man1dir/ctdb.1*
%_man1dir/ctdbd.1*
%_man1dir/onnode.1*
%_man1dir/ltdbtool.1*
%_man1dir/ping_pong.1*
%_man1dir/ctdb_diagnostics.1*
%_man1dir/ctdbd_wrapper.1*
%_man5dir/ctdb.conf.5*
%_man5dir/ctdb-script.options.5*
%_man5dir/ctdb.sysconfig.5*
%_man7dir/ctdb.7*
%_man7dir/ctdb-tunables.7*
%_man7dir/ctdb-statistics.7*
%endif

%files ctdb-tests
%_libexecdir/ctdb/tests
%_bindir/ctdb_run_tests
%_bindir/ctdb_run_cluster_tests
%_datadir/ctdb/tests
%endif

%files -n task-samba-dc

%files util-private-headers
%_includedir/samba-4.0/private

%changelog
* Wed Aug 14 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.6-alt2
- Change lstat to stat check in directory_create_or_exist for compatibility
  with oldstyle /var/run due it symlink in modern linux installations

* Mon Aug 12 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.6-alt1
- Update to latest summer release

* Wed Jul 31 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.5-alt1
- Update to latest security release
- Security fixes:
  + CVE-2019-12435 Samba AD DC Denial of Service in DNS management server (dnsserver)
  + CVE-2019-12436 Samba AD DC LDAP server crash (paged searches)

* Fri Jul 19 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt5
- Partial fixes for SMBLoris vulnerability on smbd
  + Add smbd read timeout parameter
  + Set max smbd processes to 768

* Thu Jul 04 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt4
- Remove conflict to libwbclient-sssd due problem that apt install
  it for with gssntlmssp-debuginfo (Closes: 36750)
- New metapackage task-samba-dc-mitkrb5 to install complete Domain Controller
  with MIT Kerberos server and libraries

* Mon Jun 14 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt3
- Add requires samba-common-tools for samba-common

* Mon May 27 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt2
- Build with MIT and Heimdal separately
- Fix upgrade of latest samba-4.9 builds from branches

* Mon May 27 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.3-alt1
- Update to latest security release
- Security fixes:
  + CVE-2018-16860 Samba AD DC S4U2Self/S4U2Proxy unkeyed checksum

* Mon May 27 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.2-alt2
- Initial support build with MIT and Heimdal separately:
  + Replace common DC and Winbind common files to separate subpackages
  + Add samba-vfs-cephfs and samba-vfs-glusterfs subpackages

* Thu Apr 11 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.2-alt1
- Update to spring security release
- Security fixes:
  + CVE-2019-3870 World writable files in Samba AD DC private/ dir
  + CVE-2019-3880 Save registry file outside share as unprivileged user

* Tue Apr 09 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.1-alt1
- Update to second release of Samba 4.10

* Wed Mar 20 2019 Evgeny Sinelikov <sin@altlinux.org> 4.10.0-alt1
- Update to first release of Samba 4.10

* Tue Mar 19 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.5-alt2
- Fix build compatibility for newest architectures with not exists
  macroses on stable branches

* Fri Mar 15 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.5-alt1
- Update to latest release with security ldb fixes (CVE-2019-3824)
- Prepare to replace runtime files from /var/run to /run directory

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 4.9.4-alt4
- disable support ceph on 32-bit arch

* Mon Jan 28 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.4-alt3
- Merge samba and samba-DC packages into single package
- Rename samba-DC to samba-dc for compatibilty

* Tue Jan 02 2019 Evgeny Sinelikov <sin@altlinux.org> 4.9.4-alt2
- Merge and rebuild for e2k
- Change group access for private directory due effective mask with acl

* Thu Dec 20 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.4-alt1
- Update to first winter security release
- Security fixes regressions:
  + CVE-2018-16853 Do not segfault if client is not set
  + CVE-2018-14629 Fix CNAME loop prevention using counter regression

* Wed Nov 28 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.3-alt1
- Update to autumn security release
- Revert Samba DC to build with internal Heimdal Kerberos implementation
- Clean test module of third_party/iso8601 and subunit modules
- Security fixes:
  + CVE-2018-14629 Unprivileged adding of CNAME record causing loop in AD Internal DNS server
  + CVE-2018-16841 Double-free in Samba AD DC KDC with PKINIT
  + CVE-2018-16851 NULL pointer de-reference in Samba AD DC LDAP server
  + CVE-2018-16852 NULL pointer de-reference in Samba AD DC DNS servers
  + CVE-2018-16853 Samba AD DC S4U2Self crash in experimental MIT Kerberos configuration (unsupported)
  + CVE-2018-16857 Bad password count in AD DC not always effective

* Sat Oct 13 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.1-alt1
- Rebuild latest release of Samba 4.9 without ubt macros

* Thu Oct 11 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.6-alt1
- Update to latest autumn release
- Disable ubt macros due binary package identity change

* Tue Sep 25 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.1-alt1%ubt
- Update to second release of Samba 4.9

* Tue Sep 18 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.9.0-alt1%ubt
- Update to first release of Samba 4.9

* Fri Sep 14 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.8.5-alt2%ubt
- Fixed the patch which allows joining to Windows based domain controllers

* Fri Aug 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.5-alt1%ubt
- Update to latest summer release

* Tue Aug 14 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.4-alt1%ubt
- Update to summer security release
- Security fixes:
  + CVE-2018-1139 Weak authentication protocol allowed
  + CVE-2018-1140 Denial of Service Attack on DNS and LDAP server
  + CVE-2018-10858 Insufficient input validation on client directory
    listing in libsmbclient
  + CVE-2018-10918 Denial of Service Attack on AD DC DRSUAPI server
  + CVE-2018-10919 Confidential attribute disclosure from the AD LDAP server
+ Build with subpackage for Python3

* Wed Jul 07 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.3-alt2%ubt
- Rebuild Samba DC with MIT Kerberos
- Fix join.py with automatically connect to domain naming master

* Wed Jul 04 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.3-alt1%ubt
- Update to new summer release of Samba 4.8

* Thu Jun 21 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.8-alt1%ubt
- Update to first summer release of Samba 4.7
- Fix doc knob: task-samba-dc should conditionally R: samba-DC-doc
- Rebuild for e2k with missing SYS_setgroups32
- Disable glusterfs and cephfs for e2k
- Disable cephfs support for mipsel

* Fri Jun 08 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.7-alt2%ubt
- Split samba-DC-common to separate samba-DC-common-tools
- Fix build against new python Sisyphus release with libnsl2

* Fri Apr 27 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.8.1-alt1%ubt
- Update to latest release of Samba 4.8

* Thu Apr 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.7-alt1%ubt
- Update to first spring release of Samba 4.7

* Fri Mar 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.6-alt1%ubt
- Update to latest winter release of Samba 4.7

* Thu Mar 15 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.14-alt1%ubt.1
- Rebuild security release (Fixes: CVE-2018-1050, CVE-2018-1057) with old
  ceph version without libceph-common for c7/c8

* Mon Mar 12 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.14-alt1%ubt
- Update to spring security release
- Security fixes:
  + CVE-2018-1050 Codenomicon crashes in spoolss server code
  + CVE-2018-1057 Unprivileged user can change any user (and admin) password

* Tue Feb 20 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.13-alt1%ubt
- Update to second winter release with common bugfixes

* Tue Jan 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.12-alt2%ubt
- Fix trouble with joined machine account moving when it already exists.
  Move it only if the admin specified an explicit OU (Samba bug #12696)

* Fri Jan 05 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.7.4-alt1%ubt
- Update to first winter release of Samba 4.7

* Thu Dec 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.12-alt1%ubt
- Update to first winter release with common bugfixes (closes: 33210)

* Thu Nov 23 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt2%ubt
- Backport from Heimdal upstream include/includedir directives for krb5.conf

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.3-alt1%ubt
- Update for second autumn security release of Samba 4.7

* Tue Nov 21 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.11-alt1%ubt
- Second autumn security release (Fixes: CVE-2017-14746, CVE-2017-15275)

* Fri Nov 17 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.2-alt1%ubt
- Update to third autumn release of Samba 4.7

* Thu Nov 16 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.10-alt1%ubt
- Update for third autumn release with common bugfixes

* Tue Nov 14 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.1-alt1%ubt
- Update for second autumn release with common bugfixes of Samba 4.7

* Wed Oct 25 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.7.0-alt2%ubt
- Fix KDC not works in configuration with trusted domain (samba bug #13078)

* Wed Oct 25 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.9-alt1%ubt
- Update for second autumn release with common bugfixes

* Thu Oct 12 2017 Evgeny Sinelnikov <sin@altlinux.org> 4.6.8-alt3%ubt
- Fix KDC not works in configuration with trusted domain (samba bug #13078)

* Wed Sep 27 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.8-alt2%ubt
- rebuild with new  libcephfs

* Fri Sep 22 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.0-alt1%ubt
- Update to new autumn release of Samba 4.7
- Revert removed lpcfg_register_defaults_hook() for openchange

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.8-alt1%ubt
- Update for autumn security release:
  + CVE-2017-12150 (SMB1/2/3 connections may not require signing where they
   should)
  + CVE-2017-12151 (SMB3 connections don't keep encryption across DFS redirects)
  + CVE-2017-12163 (Server memory information leak over SMB1)

* Wed Sep 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt3%ubt
- Avoid build trouble with ubt macros id on branch c8

* Fri Aug 18 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt2%ubt
- Clean code from old merged chunks

* Wed Aug 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.7-alt1%ubt
- Update to second summer release

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Wed Jul 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.6-alt1%ubt
- Update to summer security release
- Security fixes:
  + CVE-2017-11103 Orpheus' Lyre KDC-REP service name validation

* Tue Jun 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt2%ubt
- Remove conflict samba-DC-libs with samba-libs
- Adjust python module requirement to samba-DC-common-libs
- Add conflict python-module-samba-DC with python-module-samba

* Tue Jun 06 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.5-alt1%ubt
- Udpate to first summer release

* Mon Jun 05 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt2%ubt
- Add libldb-modules-DC package with domain controller ldb modules for ldb-tools
- Add samba-DC-common-libs with libraries for common modules
- Append list of libraries consists in libwbclient-DC to not require
  samba-DC-common-libs

* Wed May 24 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.4-alt1%ubt
- Update to second spring security release
- Fix longtime initialization bug in ldb proxy
- Security fixes:
  + CVE-2017-7494 Remote code execution from a writable share

* Tue Apr 25 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.3-alt1%ubt
- Udpate to second spring release
- Remove conflict winbind with libwbclient-sssd due upgrade problems

* Wed Apr 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt2%ubt
- Fix problem with failed to create kerberos keytab during join to domain

* Fri Mar 31 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.2-alt1%ubt
- Update with regression fix of spring security release
- Revert winbind problem fixes with access user to keytab due troubles in 4.6.x

* Thu Mar 23 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.1-alt1%ubt
- Update to spring security release
- Fixed build --without docs (closes: 33118)
- Security fixes:
  + CVE-2017-2619 Symlink race allows access outside share definition

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.6.0-alt1%ubt
- Udpate to first spring release
- Revert removed unused DCERPC_FAULT_UNK_IF for openchange

* Wed Feb 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.5-alt1%ubt
- Update to winter release
- Fix PAM winbind problem with access user to keytab

* Wed Dec 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt2%ubt
- Do not delete an existing valid credential cache for KEYRING type
- Set FQDN to lower at fill_mem_keytab_from_system_keytab()

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.3-alt1%ubt
- Update for release with security fixes:
  - CVE-2016-2123 (ndr_pull_dnsp_name contains an integer wrap problem)
  - CVE-2016-2125 (client code always requests a forwardable ticket)
  - CVE-2016-2126 (crash winbindd using a legitimate Kerberos ticket)

* Mon Dec 19 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.2-alt1%ubt
- Udpate to first winter release

* Sat Dec 03 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt2
- Add conflict winbind with libwbclient-sssd due compatibility
- Update build dependencies versions for external samba libraries
- Build with separate libwbclient-DC

* Fri Oct 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt1
- Update with variety of fixes for autumn release

* Thu Sep 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.0-alt1
- Update to new autumn release

* Fri Jul 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.5-alt1
- Update for security release with CVE-2016-2119

* Thu Jun 30 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.4-alt3
- Apply fixes for DRSUAPI limits of too strict for some workloads,
  e.g. DRSUAPI replication with large objects.
   https://bugzilla.samba.org/show_bug.cgi?id=11948
 + Set DCERPC_NCACN_{REQUEST,RESPONSE}_DEFAULT_MAX_SIZE
 + Allow a total reassembled response payload of 240 MBytes

* Wed Jun 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.4-alt2
- Package libsamba_util private headers to package
  samba-DC-util-private-headers

* Fri Jun 10 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.4-alt1
- Update to new version

* Tue May 24 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt3
- build with libsystemd without compat libs
- add patches from fedora
- add again samba-grouppwd.patch

* Mon May 23 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.3-alt2
- Fix rpc_server/drsuapi: Set msDS_IntId as attid for linked attributes if exists

* Wed May 04 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.3-alt1
- New version

* Thu Apr 28 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.2-alt2
- Fix CVE-2016-2110/NTLMSSP regression (https://bugzilla.samba.org/show_bug.cgi?id=11849)

* Tue Apr 12 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.2-alt1
- New version
- Security fixes:
  - CVE-2015-5370 (Multiple errors in DCE-RPC code)
  - CVE-2016-2110 (Man in the middle attacks possible with NTLMSSP)
  - CVE-2016-2111 (NETLOGON Spoofing Vulnerability)
  - CVE-2016-2112 (LDAP client and server don't enforce integrity)
  - CVE-2016-2113 (Missing TLS certificate validation)
  - CVE-2016-2114 ("server signing = mandatory" not enforced)
  - CVE-2016-2115 (SMB IPC traffic is not integrity protected)
  - CVE-2016-2118 (SAMR and LSA man in the middle attacks possible)

* Tue Mar 22 2016 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version (https://www.samba.org/samba/history/samba-4.4.0.html)
- Remove samba-DC-test-build and samba-DC-ctdb-devel

* Sun Mar 13 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.6-alt2
- Rebuild with new libtalloc

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.6-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.6.html)
- Security fixes:
  - CVE-2015-7560 (Incorrect ACL get/set allowed on symlink path)
  - CVE-2016-0771 (Out-of-bounds read in internal DNS server)
- Do not use specified GID for wbpriv group

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.5-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.5.html)

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.4-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.4.html)

* Thu Dec 24 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt2
- Change services type from notify to forking

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.3.html)
- Security fixes:
  - CVE-2015-3223 (Denial of service in Samba Active Directory
  server)
  - CVE-2015-5252 (Insufficient symlink verification in smbd)
  - CVE-2015-5299 (Missing access control check in shadow copy
  code)
  - CVE-2015-5296 (Samba client requesting encryption vulnerable
  to downgrade attack)
  - CVE-2015-8467 (Denial of service attack against Windows
  Active Directory server)
  - CVE-2015-5330 (Remote memory read in Samba LDAP server)

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1.1
- NMU: dropped unused prehistoric BR: perl-Perl4-CoreLibs

* Tue Dec 01 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.2.html)
- Enable RPATH in installed files to correct link using .pc files

* Thu Nov 26 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt3
- Remove libxfs-qa-devel from build requirements
- Package samba-DC-ctdb, samba-DC-ctdb-devel and samba-DC-ctdb-tests

* Mon Nov 16 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt2
- Enable clustering support

* Tue Oct 20 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.1.html)
- New metapackage task-samba-dc to install complete Domain Controller

* Tue Sep 22 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt2
- Exclude libnss_win* from debuginfo
- Make libnss_win* symlinks to /lib*
- Package unit samba.service for systemd
- Add conditional build of winbind part
- Move all libraries to samba-DC-libs
- Remove duplicated requirements

* Thu Sep 10 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version (https://www.samba.org/samba/history/samba-4.3.0.html)
- Requires /proc for doc generation

* Mon Aug 24 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt2
- Build in dc mode in %_libdir/samba-dc to prevent link conflict
  with ordinary samba in repository
- Build without libsmbclient, libwbclient and libnetapi
- Move documentation to /usr/share/doc/samba

* Tue Jul 14 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version of Samba AD DC

* Mon Jun 01 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version of Samba AD DC

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version of Samba AD DC
- Fix post/postun hooks for samba init script

* Fri Apr 10 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version of Samba AD DC
- Enable documentation build

* Mon Feb 23 2015 Andrey Cherepanov <cas@altlinux.org> 4.1.17-alt1
- New version
- Security fixes:
  + fixes CVE-2015-0240 (security flaw in the smbd file server daemon)

* Thu Jan 15 2015 Andrey Cherepanov <cas@altlinux.org> 4.1.16-alt1
- New version
- Security fixes:
  + CVE-2014-8143: Samba's AD DC allows the administrator to delegate
    creation of user or computer accounts to specific users or groups.
    However, all released versions of Samba's AD DC did not implement the
    additional required check on the UF_SERVER_TRUST_ACCOUNT bit in the
    userAccountControl attributes.

* Wed Jan 14 2015 Andrey Cherepanov <cas@altlinux.org> 4.1.15-alt1
- New version

* Thu Dec 25 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.14-alt0.M70P.1
- New version
- Disable build documentation because it cannot built

* Mon Oct 20 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.13-alt0.M70P.1
- New version
- Do not use pidfile to stop service samba

* Tue Oct 14 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.12-alt0.M70P.1
- New version

* Mon Oct 13 2014 Andrey Cherepanov <cas@altlinux.org> 4.1.11-alt1.M70P.1
- Build in DC mode
- Fix mitkrb5 support with and without DC mode
- Build on all available cores. Increase build and install verbosity
- Add setproctitle support
- Set verbosity level of make by VERBOSE option (-v, -vv or -vvv)
- Remove missing upgradeprovision programm
- Add initscript for samba
- Add dlz_bind9_9.so
- Rename to samba-DC conflicted by ordinary samba
- Add tdb-utils for samba_upgradedns program
- Use %%force_with to really set flag for tests

* Wed Aug 27 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.11-alt2
- update init scripts for ALTLinux

* Tue Aug 05 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.11-alt1
- 4.1.11
- fixed unstrcpy macro length is invalid(CVE-2014-3560)

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.10-alt1
- 4.1.10

* Tue Jun 24 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.9-alt1
- 4.1.9
- fixed nmbd denial of service(CVE-2014-0244)
- fixed Segmentation fault in smbd_marshall_dir_entry(CVE-2014-3493)

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.8-alt1
- 4.1.8
- fixed CVE-2014-0239, CVE-2014-0178

* Wed May 07 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.7-alt2
- add winbind-krb5-locator package

* Mon May 05 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.7-alt1
- 4.1.7

* Mon Mar 17 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.6-alt1
- 4.1.6
- fixed CVE-2013-4496, CVE-2013-6442

* Wed Jan 15 2014 Alexey Shabalin <shaba@altlinux.ru> 4.1.4-alt1
- 4.1.4

* Mon Dec 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt1
- 4.1.3
- fixed CVE-2013-4408, CVE-2012-6150

* Wed Dec 04 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1.2-alt1
- 4.1.2
- drop swat package
- change build options:
  + --with-profiling-data
  + drop --disable-ntdb
  + --without-fam
  + drop --builtin-libraries=ccan
- build with avahi support
- build with external libntdb

* Wed Nov 27 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Tue Nov 12 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.11-alt1
- 4.0.11
- fixed CVE-2013-4475, CVE-2013-4476

* Tue Oct 08 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.10-alt1
- 4.0.10

* Mon Aug 26 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.9-alt1
- 4.0.9
- add -D options for default forking type start of services to sysV init and systemd

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.8-alt1
- 4.0.8
- fixed CVE-2013-4124

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.7-alt1
- 4.0.7

* Thu May 23 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Tue Apr 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 19 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.4-alt1
- 4.0.4 (fixed CVE-2013-186)
- add /var/cache/samba to samba-common package (ALT#28601)

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.3-alt2
- make systemctl reference indirect in packaging/NetworkManager/30-winbind-systemd (ALT#28585)

* Fri Feb 15 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.3-alt1
- 4.0.3
- build as default samba, replaced samba4 packages
- rename pdb_ldap to pdb_ldapsam

* Mon Feb 04 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.2-alt2
- obsoletes libnetapi4,libwbclient4,libsmbclient4 by samba4-libs if build without them

* Mon Feb 04 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.2-alt1
- 4.0.2
- fixed gensec: Allow login without a PAC by default (samba bug #9581)

* Fri Feb 01 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt3
- build without libnetapi
- add symlink ldapsam.so to ldap.so

* Thu Jan 31 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt2
- build without libsmbclient and libwbclient

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Dec 21 2012 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt2
- 4.0.0 release

* Wed Mar 28 2012 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha18
- alpha18

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.0-alt1.alpha16.1
- Rebuild with Python-2.7

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha16
- alpha16

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha15
- alpha15

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt0.alpha15
- pre alpha15 snapshot

* Thu Sep 23 2010 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha13
- Upgrade to alpha13

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1.alpha11
- initial build for ALT Linux Sisyphus

* Mon Jun 28 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.0-24.alpha11
- Revert changes to %%Release, use %%main_release instead.
- Rebuild for perl-5.12.x.

* Mon Jun 28 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.0-23.alpha11.2
- Once again rebuild for perl-5.12.x.

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.0.0-23.alpha11.1
- Mass rebuild with perl-5.12.0

* Wed Feb 24 2010 Stephen Gallagher <sgallagh@redhat.com> - 4.0.0-23.alpha11
- Rebuild against newer libtevent

* Sun Jan 24 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-22.alpha11
- Upgrade to alpha11

* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-21.alpha10
- Bump ldb_version to 0.9.10.

* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-20.alpha10
- Only install new command-line utilities if enable_samba4 is non-zero.

* Wed Jan 06 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-19.alpha10
- Upgrade to alpha10

* Thu Sep 17 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-18.1.alpha8_git20090916
- Need docbook stuff to build man pages

* Thu Sep 17 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-18.alpha8_git20090916
- Fix broken dependencies

* Wed Sep 16 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-17.alpha8_git20090916
- Upgrade to alpha8-git20090916

* Wed Sep 16 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-16.alpha7
- Stop building libtevent, it is now an external package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-15.2alpha7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-15.2alpha7
- Fix dependency

* Sat May 09 2009  Simo Sorce <ssorce@redhat.com> - 4.0.0-15.1alpha7
- Don't build talloc and tdb, they are now separate packages

* Mon Apr 06 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-14alpha7
- Fix a build issue in samba4-common (RH bug #494243).

* Wed Mar 25 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-13alpha7
- rebuild with correct CFLAGS (also fixes debuginfo)

* Tue Mar 10 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-12alpha7
- Second part of fix for the ldb segfault problem from upstream

* Mon Mar 09 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-11alpha7
- Add upstream patch to fix a problem within ldb

* Sun Mar 08 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-10alpha7
- Remove ldb.pc from samba4-devel (RH bug #489186).

* Wed Mar  4 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-9alpha7
- Make talloc,tdb,tevent,ldb easy to exclude using defines
- Fix package for non-mock "dirty" systems by deleting additional
  files we are not interested in atm

* Wed Mar  4 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-8alpha7
- Fix typo in Requires

* Mon Mar  2 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-7alpha7
- Compile and have separate packages for additional samba libraries
  Package in their own packages: talloc, tdb, tevent, ldb

* Fri Feb 27 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-4.alpha7
- Update to 4.0.0alpha7

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-3.alpha6
- Formal package review cleanups.

* Mon Feb 23 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-2.alpha6
- Disable subpackages not needed by OpenChange.
- Incorporate package review feedback.

* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-1.alpha6
- Update to 4.0.0alpha6

* Wed Dec 17 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.8.alpha6.GIT.3508a66
- Fix another file conflict: smbstatus

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.7.alpha6.GIT.3508a66
- Disable the winbind subpackage because it conflicts with samba-winbind
  and isn't needed to support OpenChange.

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.6.alpha6.GIT.3508a66
- Update to the GIT revision OpenChange is now requiring.

* Fri Aug 29 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.5.alpha5.fc10
- Fix licence tag (the binaries are built into a GPLv3 whole, so the BSD licence need not be mentioned)

* Fri Jul 25 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.4.alpha5.fc10
- Remove talloc and tdb dependency (per https://bugzilla.redhat.com/show_bug.cgi?id=453083)
- Fix deps on chkconfig and service to main pkg (not -common)
  (per https://bugzilla.redhat.com/show_bug.cgi?id=453083)

* Mon Jul 21 2008 Brad Hards <bradh@frogmouth.ent> - 0:4.0.0-0.3.alpha5.fc10
- Use --sysconfdir instead of --with-configdir
- Add patch for C++ header compatibility

* Mon Jun 30 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.2.alpha5.fc9
- Update per review feedback
- Update for alpha5

* Thu Jun 26 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.1.alpha4.fc9
- Rework Fedora's Samba 3.2.0-1.rc2.16 spec file for Samba4
