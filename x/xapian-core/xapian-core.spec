%def_disable static

Name: xapian-core
Version: 1.4.15
Release: alt1

Summary: The Xapian Probabilistic Information Retrieval Library

License: GPL
Group: Databases
Url: http://www.xapian.org

Source: http://www.oligarchy.co.uk/xapian/%version/%{name}-%{version}.tar
Source100: %name.watch

Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ zlib-devel libuuid-devel

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This is core package.

%package -n libxapian
Summary: Xapian search engine libraries
Group: System/Libraries

%description -n libxapian
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package provides the libraries for applications using Xapian
functionality.

%package -n libxapian-devel
Group: Development/C++
Summary: Files needed for building packages which use Xapian
Requires: libxapian = %version

%description -n libxapian-devel
This package provides the files needed for building packages which
use Xapian library.

%if_enabled static
%package -n libxapian-devel-static
Group: Development/C++
Summary: Files needed for building packages which use Xapian statically
Requires: libxapian-devel = %version

%description -n libxapian-devel-static
This package provides the files needed for building packages which
link against Xapian library statically or use XO_LIB_XAPIAN macroo
and build with libtool.
%endif

%package -n %name-doc
Group: Development/Documentation
Summary: Developer's documentation for Xapian
Obsoletes: xapian-doc < 0.9.9
Provides: xapian-doc = %version-%release
BuildArch: noarch

%description -n %name-doc
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package contains API reference in HTML and PostScript.

%prep
%setup
%ifarch %e2k
# current lcc doesn't know these
sed -i  -e 's,-fno-gnu-keywords,,;s,-Wstrict-null-sentinel,,' \
	-e 's,-Wstrict-overflow=1,,;s,-Wlogical-op,,;s,-Wdouble-promotion,,' \
	configure.ac
# http://stackoverflow.com/questions/14892101/
%add_optflags -ftls-model=global-dynamic
%endif

%build
%autoreconf
%configure %{subst_enable static}
%make_build
gzip -9nf ChangeLog

%install
%makeinstall_std
rm -rf %buildroot%_datadir/doc/xapian-core/

%if_enabled static
# should we still support this?
%else
rm -f %buildroot%_libdir/libxapian.a
%endif

%files
%_bindir/copydatabase
%_bindir/quest
%_bindir/simpleexpand
%_bindir/simpleindex
%_bindir/simplesearch
%_bindir/xapian-check
%_bindir/xapian-compact
%_bindir/xapian-delve
%_bindir/xapian-metadata
%_bindir/xapian-progsrv
%_bindir/xapian-replicate
%_bindir/xapian-replicate-server
%_bindir/xapian-tcpsrv
%_datadir/xapian-core/
%_man1dir/*.1*
%doc AUTHORS ChangeLog* NEWS PLATFORMS README

%files -n libxapian
%_libdir/*.so.*

%files -n libxapian-devel
%_bindir/xapian-config
%_includedir/xapian.h
%_includedir/xapian/
%_libdir/libxapian.so
%_libdir/cmake/xapian/
%_datadir/aclocal/xapian.m4
%_pkgconfigdir/*.pc

%if_enabled static
%files -n libxapian-devel-static
%_libdir/libxapian.a
%endif

%files -n %name-doc
%doc docs/*.html
%doc docs/apidoc/html/
%doc HACKING

# NOTE:
# - do NOT build this package from git unless you want to maintain it,
#   I use watch file and it's more convenient to do that with srpms

%changelog
* Mon Mar 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.15-alt1
- new version 1.4.15 (with rpmrb script)
- update buildreqs

* Mon Oct 15 2018 Michael Shigorin <mike@altlinux.org> 1.4.5-alt3
- drop BR: libwrap (was weird anyways)

* Sun Jul 01 2018 Michael Shigorin <mike@altlinux.org> 1.4.5-alt2
- support e2kv4 through %%e2k macro (grenka@)
- merged my changes back

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1
- Updated to latest stable upstream version 1.4.5.

* Tue Oct 17 2017 Michael Shigorin <mike@altlinux.org> 1.4.5-alt0
- new version (watch file uupdate)

* Tue May 09 2017 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- new version (watch file uupdate)

* Fri Jan 27 2017 Michael Shigorin <mike@altlinux.org> 1.4.3-alt1
- new version (watch file uupdate)

* Tue Dec 27 2016 Michael Shigorin <mike@altlinux.org> 1.4.2-alt1
- new version (watch file uupdate)
- E2K: lcc adaptations

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- new version (watch file uupdate)

* Sun Jun 26 2016 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- new version (watch file uupdate)
  + dropped xapian-chert-update, xapian-inspect utilities
  + renamed delve to xapian-delve

* Wed Mar 30 2016 Michael Shigorin <mike@altlinux.org> 1.2.23-alt1
- new version (watch file uupdate)

* Fri Jan 01 2016 Michael Shigorin <mike@altlinux.org> 1.2.22-alt1
- new version (watch file uupdate)

* Fri May 22 2015 Michael Shigorin <mike@altlinux.org> 1.2.21-alt2
- added pkgconfig file (thx aris@)

* Thu May 21 2015 Michael Shigorin <mike@altlinux.org> 1.2.21-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 1.2.20-alt1
- new version (watch file uupdate)

* Tue Oct 21 2014 Michael Shigorin <mike@altlinux.org> 1.2.19-alt1
- new version (watch file uupdate)

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 1.2.18-alt1
- new version (watch file uupdate)

* Fri Mar 21 2014 Michael Shigorin <mike@altlinux.org> 1.2.17-alt1
- new version (watch file uupdate)

* Thu Dec 05 2013 Michael Shigorin <mike@altlinux.org> 1.2.16-alt1
- new version (watch file uupdate)
- dropped libtool patch, thanks upstream for the notice it's not needed

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 1.2.15-alt1
- new version (watch file uupdate)

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 1.2.14-alt1
- new version (watch file uupdate)

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 1.2.13-alt1
- new version (watch file uupdate)

* Thu Jun 28 2012 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- new version (watch file uupdate)
  + minor bugfixes/enhancements in 1.2.11 which had incorrect soname

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- new version (watch file uupdate)
  + assorted fixes

* Fri Mar 16 2012 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- 1.2.9

* Fri Aug 12 2011 Michael Shigorin <mike@altlinux.org> 1.2.7-alt1
- 1.2.7

* Thu Apr 14 2011 Michael Shigorin <mike@altlinux.org> 1.2.5-alt1
- 1.2.5: http://trac.xapian.org/wiki/ReleaseOverview/1.2.5

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.1
- Rebuilt for debuginfo

* Tue Dec 21 2010 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4: http://trac.xapian.org/wiki/ReleaseOverview/1.2.4
  + NB: remote database protocol change
  + Omega improvements
  + binding fixes
- [backdated] not published due to python module strict dep

* Mon Oct 04 2010 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3
- added cmake files to devel subpackage

* Tue Jun 22 2010 Michael Shigorin <mike@altlinux.org> 1.0.21-alt1
- 1.0.21 (postponed soname change till 1.2.x)

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0
  + dropped quartz* utils (obsolete)
  + added a few utilities in return
- buildreq

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 1.0.20-alt1
- 1.0.20

* Thu Apr 15 2010 Michael Shigorin <mike@altlinux.org> 1.0.19-alt1
- 1.0.19

* Mon Feb 15 2010 Michael Shigorin <mike@altlinux.org> 1.0.18-alt1
- 1.0.18: minor fixes/improvements

* Fri Jan 08 2010 Michael Shigorin <mike@altlinux.org> 1.0.17-alt3
- hacked xapian-config due to missing .la files (closes: #22629)

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.0.17-alt2
- buildreq (thx repocop)
- gzip ChangeLog

* Thu Nov 19 2009 Michael Shigorin <mike@altlinux.org> 1.0.17-alt1
- 1.0.17

* Thu Aug 27 2009 Michael Shigorin <mike@altlinux.org> 1.0.15-alt1
- 1.0.15

* Fri Jul 24 2009 Michael Shigorin <mike@altlinux.org> 1.0.14-alt2
- noarch doc subpackage (repocop)
- minor spec cleanup

* Wed Jul 22 2009 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14: more robust shared library

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13: minor fixes

* Tue Apr 21 2009 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12: minor fixes/improvements

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11: http://trac.xapian.org/wiki/ReleaseOverview/1.0.11

* Wed Dec 24 2008 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10: http://trac.xapian.org/wiki/ReleaseOverview/1.0.10
  + minor bugfixes

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.9-alt2
- applied repocop patch

* Mon Nov 03 2008 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9: http://trac.xapian.org/wiki/ReleaseOverview/1.0.9
  + spelling correction even faster
  + fixed issues due to excess precision

* Thu Sep 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.8-alt1
- 1.0.8: http://trac.xapian.org/wiki/ReleaseOverview/1.0.8
  + assorted fixes and performance improvements

* Wed Jul 16 2008 Michael Shigorin <mike@altlinux.org> 1.0.7-alt1
- 1.0.7: http://trac.xapian.org/wiki/ReleaseOverview/1.0.7
  + performance enhancements in some cases
  + minor bugfixes

* Tue Mar 18 2008 Michael Shigorin <mike@altlinux.org> 1.0.6-alt1
- 1.0.6 (minor feature enhancements)
  + single-ended range value checks
  + faster stemmers
  + improvements to xapian-check,
    xapian-compact metadata handling

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5 (minor feature enhancements)

* Tue Oct 30 2007 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- 1.0.4: http://wiki.xapian.org/ReleaseOverview/1.0.4
  + faster matcher
  + fixed flint bug introduced in 1.0.3
  + remote protocol minor version has been increased

* Mon Oct 01 2007 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- 1.0.3:
  + Flint DB format extended to support user metadata,
    1.0.2 and earlier won't be able to read 1.0.3 DBs
    (upgrade is automatic on opening with newer version)
- added xapian-inspect

* Thu Jul 05 2007 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- 1.0.2: http://wiki.xapian.org/ReleaseOverview/1.0.2
  + remote protocol version increased
  + optional Btree tables (1.0.2 is backwards compatible with
    1.0.0 and 1.0.1 databases but older versions won't be able
    to read DBs created or modified by 1.0.2)
  + QueryParser improvements, incl. precedence fixes for
    logical operators
  + misc. bugfixes in NumberValueRangeProcessor, matcher,
    delete_document(), exception handling during commit

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1: http://wiki.xapian.org/ReleaseOverview/1.0.1
  + warning: forced incompatible ABI change due to fixing
    possible double-free error introduced in 1.0.0
  + on a similar note, remote protocol version increased
  + upstream promises to try hard and avoid ABI breakage
    during 1.0.x (after 1.0.1 till 1.1.0)
  = basically we have to relink clients (of both library
    and server)

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0
- removed all patches
- added Packager:
- updated BuildRequires:
- added xapian-check

* Mon Mar 12 2007 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- 0.9.10
- removed patch1

* Tue Nov 28 2006 Michael Shigorin <mike@altlinux.org> 0.9.9-alt2
- apply upstream patch referenced from 0.9.9 release notes
- apply another patch for NEAR bug (from recoll author)

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- 0.9.9
- renamed from xapian to xapian-core accordingly to upstream
- apidoc is now PDF instead of PS
- spec cleanup
- SMP make

* Fri Nov 03 2006 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- 0.9.8

* Wed Oct 11 2006 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- 0.9.7
- added xapian-progsrv

* Mon May 15 2006 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- 0.9.6 (minor bugfixes)
  + added Ruby bindings
- added manpages

* Mon Apr 10 2006 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- 0.9.5

* Fri Mar 10 2006 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- 0.9.4
- removed patch1

* Mon Feb 06 2006 Michael Shigorin <mike@altlinux.org> 0.9.2-alt3
- thanks upstream developer Olly Betts <olly/survex.com> for
  checking our package and Dmitry Levin <ldv@> for libtool/xapian-config
  advice and patch
- finished implementing -devel-static subpackage, just in case;
  build disabled by default
- temporarily removed unicode query patch to check whether it was relevant
  to Cyrillic icase search with recoll

* Tue Dec 06 2005 Michael Shigorin <mike@altlinux.org> 0.9.2-alt2
- applied patch to enable unicode querying (disables stemming)
- see also recoll (qt frontend)

* Mon Dec 05 2005 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- built for ALT Linux (recoll dependency)
- removed static libraries (anyone needing 'em adds devel-static
  and mails me a spec patch)
- moved API docs to subpackage
- spec cleanup

