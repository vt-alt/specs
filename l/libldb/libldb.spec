%define _unpackaged_files_terminate_build 1
%def_with check

%ifarch %arm %ix86 mips mipsel
%def_without mdb
%else
%def_with mdb
%endif

Name: libldb
Version: 2.0.12
Release: alt2
Summary: A schema-less, ldap like, API and database
License: LGPLv3+
Group: System/Libraries
Url: http://ldb.samba.org/

Source: http://samba.org/ftp/ldb/ldb-%{version}.tar.gz
Patch: ldb-samba-modules.patch
Patch1: ldb-alt-fix-python-ldflags.patch
Patch2: ldb-skip-test_guid_indexed_v1_db-on-mips64el-ppc64le-mipsel.patch
Patch3: ldb-skip-ldb_lmdb_free_list_test-on-ppc64le.patch

BuildRequires: libpopt-devel libldap-devel xsltproc docbook-style-xsl docbook-dtds
BuildRequires: libcmocka-devel >= 1.1.3
BuildRequires: libtdb-devel >= 1.4.2
BuildRequires: libtalloc-devel >= 2.2.0
BuildRequires: libtevent-devel >= 0.10.0
%if_with mdb
BuildRequires: liblmdb-devel >= 0.9.16
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-tdb
BuildRequires: python3-module-talloc-devel
BuildRequires: python3-module-tevent

Requires: libtdb >= 1.4.2
Requires: libtalloc >= 2.2.0
Requires: libtevent >= 0.10.0
%if_with mdb
Requires: liblmdb >= 0.9.16
%endif

%description
An extensible library that implements and LDAP like API to access remote LDAP
servers, or use local tdb databases.

%package devel
Group: Development/C
Summary: Developer tools for the LDB library
Requires: %name = %version-%release

%description devel
Header files needed to develop programs that link against the LDB library.

%package -n ldb-tools
Group: Development/Tools
Summary: Tools to manage LDB files
Requires: %name = %version-%release

%description -n ldb-tools
Tools to manage LDB files

%package -n python3-module-pyldb
Group: Development/Python3
Summary: Python3 bindings for the LDB library
Requires: %name = %EVR

%description -n python3-module-pyldb
Python3 bindings for the LDB library

%package -n python3-module-pyldb-devel
Group: Development/Python3
Summary: Development files for the Python3 bindings for the LDB library
Requires: python3-module-pyldb = %EVR
Requires: %name-devel = %EVR

%description -n python3-module-pyldb-devel
Development files for the Python3 bindings for the LDB library

%prep
%setup -n ldb-%version
%patch -p2
%patch1 -p1
%patch2 -p1
%ifarch ppc64le
%patch3 -p2
%endif

%build
%undefine _configure_gettext
%configure	\
		--disable-rpath \
		--disable-rpath-install \
		--bundled-libraries=NONE \
		--builtin-libraries=replace \
		--with-modulesdir=%_libdir/ldb/modules \
		--with-samba-modulesdir=%_libdir/samba \
%if_without mdb
                --without-ldb-lmdb \
%endif
		--with-privatelibdir=%_libdir/ldb
%make

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a
rm -f %buildroot/%_man3dir/_*

%check
make test

%files
%_libdir/libldb.so.*
%dir %_libdir/ldb
%dir %_libdir/ldb/modules
%dir %_libdir/ldb/modules/ldb

%_libdir/ldb/libldb-key-value.so
%if_with mdb
%_libdir/ldb/libldb-mdb-int.so
%endif
%_libdir/ldb/libldb-tdb-int.so
%_libdir/ldb/libldb-tdb-err-map.so

%_libdir/ldb/modules/ldb/asq.so
%_libdir/ldb/modules/ldb/ldap.so
%_libdir/ldb/modules/ldb/paged_searches.so
%_libdir/ldb/modules/ldb/rdn_name.so
%_libdir/ldb/modules/ldb/sample.so
%_libdir/ldb/modules/ldb/server_sort.so
%_libdir/ldb/modules/ldb/skel.so
%_libdir/ldb/modules/ldb/tdb.so
%_libdir/ldb/modules/ldb/ldb.so
%if_with mdb
%_libdir/ldb/modules/ldb/mdb.so
%endif

%files devel
%_includedir/ldb.h
%_includedir/ldb_errors.h
%_includedir/ldb_handlers.h
%_includedir/ldb_module.h
%_includedir/ldb_version.h
%_libdir/libldb.so
%_pkgconfigdir/ldb.pc
%_man3dir/ldb.3.*

%files -n ldb-tools
%_bindir/ldbadd
%_bindir/ldbdel
%_bindir/ldbedit
%_bindir/ldbmodify
%_bindir/ldbrename
%_bindir/ldbsearch
%_man1dir/ldbadd.1.*
%_man1dir/ldbdel.1.*
%_man1dir/ldbedit.1.*
%_man1dir/ldbmodify.1.*
%_man1dir/ldbrename.1.*
%_man1dir/ldbsearch.1.*
%_libdir/ldb/libldb-cmdline.so

%files -n python3-module-pyldb
%python3_sitelibdir/ldb.cpython-*.so
%python3_sitelibdir/_ldb_text.py
%python3_sitelibdir/__pycache__/_ldb_text.cpython-*.py*
%_libdir/libpyldb-util.cpython-*.so.*

%files -n python3-module-pyldb-devel
%_includedir/pyldb.h
%_libdir/libpyldb-util.cpython-*.so
%_pkgconfigdir/pyldb-util.cpython-*.pc

%changelog
* Thu Jul 23 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.12-alt2
- Disable ldb_lmdb_free_list_test on ppc64le (Samba#14404)

* Tue Jul 07 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.12-alt1
- Update to the 2.0.11 for latest samba-4.11.11 security release

* Tue Jun 30 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.11-alt1
- Update to the 2.0.11 for latest samba-4.11.10 release

* Tue Apr 28 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.10-alt1
- Update to the 2.0.10 for latest samba-4.11.8 release

* Tue Mar 10 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.9-alt1
- Update to the 2.0.9 for latest samba-4.11 releases

* Wed Feb 05 2020 Evgeny Sinelnikov <sin@altlinux.org> 2.0.8-alt1
- Update to the 2.0.8 for newest samba-4.11 releases

* Tue Nov 05 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.0.7-alt2
- Disable toggle_guidindex_check_pack test for mips64el, ppc64le and mipsel

* Thu Oct 31 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.0.7-alt1
- Update to the 2.0.7 for newest samba-4.11 releases without python2 support

* Fri Oct 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.5.6-alt1
- Update to the 1.5.6 for newest samba-4.10 releases

* Thu Aug 01 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.5.5-alt1
- Update to the 1.5.5 for newest samba-4.10 releases

* Sun Mar 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.5.4-alt1
- Update to the 1.5.4 release for samba-4.10
- Adjust lmdb disable tests patch for 32-bit platforms

* Sun Mar 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.6-alt3
- Fix samba-modulesdir from samba-dc to samba libdir

* Tue Mar 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.6-alt2
- Merge with stable branches for common build

* Wed Feb 27 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.6-alt1
- Update to the 1.4.6 security release for samba-4.9.5
- Security fixes:
  + CVE-2019-3824 ldb: Out of bound read in ldb_wildcard_compare

* Thu Jan 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.4.4-alt1
- Update to the 1.4.4 release for samba-4.9 (Samba#13616, Samba#13686)

* Wed Dec 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt4
- Disable lmdb support on armh

* Tue Dec 18 2018 Ivan A. Melnikov <iv@altlinux.org> 1.4.3-alt3
- Disable lmdb support on mips32

* Mon Dec 17 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.4.3-alt2
- Merge with branch p8_e2k for common build

* Thu Nov 08 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.4.3-alt1
- Update to the 1.4.3 release for samba-4.9.2

* Thu Oct 25 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.4.2-alt2
- Build for x86 without lmdb support
- Disable ubt macros due binary package identity changes

* Thu Sep 13 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.4.2-alt1%ubt
- Update to the 1.4.2 release for samba-4.9.0

* Fri Aug 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.3.6-alt1%ubt
- Update to the 1.3.6 release for samba-4.8.5

* Tue Aug 14 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.3.5-alt1%ubt
- Update to security release (Fixes: CVE-2018-1140)

* Sat Jul 21 2018 Stanislav Levin <slev@altlinux.org> 1.3.4-alt3%ubt
- Build package for Python3

* Tue Jul 17 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.3.4-alt2%ubt
- Fix missing NULL terminator in ldb_mod_op_test testsuite from master
  due build for aarch64

* Thu Jun 28 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.3.4-alt1%ubt
- Update to the 1.3.4 release for samba-4.8.3

* Fri Jun 08 2018 Ivan A. Melnikov <iv@altlinux.org> 1.3.3-alt1%ubt
- Update to the 1.3.3 release
- Add patch #1 to fix build with new python

* Fri Mar 23 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.3.2-alt1%ubt
- Update to new release for samba-4.8.0

* Fri Jan 05 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.2.3-alt1%ubt
- Update to new release for samba-4.7.4

* Tue Sep 19 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.2-alt1%ubt
- Update to new release for samba-4.7.0rc6

* Sat Aug 19 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.1-alt1%ubt
- Update to new 1.2.x release

* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.31-alt1%ubt
- Update to latest 1.1.x release

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.29-alt3%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Tue Jun 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.29-alt2%ubt
- Remove hacks with ldb samba modules path search via LDB_LIBRARY_PATH
  by additional --with-samba-modulesdir configure option (closes: #33427)

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.29-alt1%ubt
- Update to new release for samba-4.6.0

* Fri Sep 09 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.27-alt1
- Update to new release for samba-4.5.0

* Thu Jun 30 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.26-alt2
- Move ldb-modules.sh from profile.d to bashrc.d to run everywhere

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.26-alt1
- 1.1.26

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.25-alt1
- 1.1.25

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.24-alt1
- 1.1.24
- Security fixes:
  - CVE-2015-5330 (Remote memory read in Samba LDAP server)
  - CVE-2015-3223 (Denial of service in Samba Active Directory server)

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.23-alt1
- 1.1.23
- Enable tests

* Wed Nov 11 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.21-alt1.1
- Fix path to samba_dsdb.so module (exists only in samba-DC)

* Thu Sep 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.21-alt1
- 1.1.21

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.20-alt1
- 1.1.20

* Mon Jan 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.19-alt1
- 1.1.19

* Mon Dec 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.18-alt1
- 1.1.18

* Mon May 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.17-alt1
- 1.1.17

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.16-alt1
- 1.1.16

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.15-alt1
- 1.1.15

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Wed Oct 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.13-alt1
- 1.1.13

* Mon Sep 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Thu Jul 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- rebuild with new libtevent

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2
- package python bindings

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus
