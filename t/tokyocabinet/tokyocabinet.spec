%def_enable fastest
%def_disable debug
%def_disable devel
%def_disable profile
%def_enable shared
%def_enable static
%def_disable uyield
%def_enable zlib
%def_enable bzip
%def_disable lzo
%def_disable lzma
%def_enable pthread
%def_enable off64
%def_disable check
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%{!?x86_64:%global x86_64 x86_64}

%define Name Tokyo Cabinet
Name: tokyocabinet
%define lname lib%name
Summary: A modern implementation of a DBM
Version: 1.4.47
Release: alt2
License: %lgpl2plus
Group: Databases
Packager: Vladimir Lettiev <crux@altlinux.org>
URL: http://fallabs.com/%name
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
%{?_enable_zlib:BuildRequires: zlib-devel}
%{?_enable_bzip:BuildRequires: bzlib-devel}
%{?_enable_lzo:BuildRequires: liblzo2-devel}
%{?_enable_lzma:BuildRequires: lzmalib-devel}

%description
%Name is a library of routines for managing a database. It is
the successor of QDBM. %Name runs very fast. For example, the
time required to store 1 million records is 1.5 seconds for a hash
database and 2.2 seconds for a B+ tree database. Moreover, the database
size is very small and can be up to 8EB. Furthermore, the scalability
of %Name is great.


%package utils
Summary: Command line tools for managing %Name databases
Group: Databases
Requires: %lname = %version-%release

%description utils
%Name is a library of routines for managing a database. It is
the successor of QDBM. %Name runs very fast. For example, the
time required to store 1 million records is 1.5 seconds for a hash
database and 2.2 seconds for a B+ tree database. Moreover, the database
size is very small and can be up to 8EB. Furthermore, the scalability
of %Name is great.
This package contains command line tools for managing %Name
databases.


%if_enabled shared
%package -n %lname
Summary: %Name library
Group: System/Libraries

%description -n %lname
%Name is a library of routines for managing a database. It is
the successor of QDBM. %Name runs very fast. For example, the
time required to store 1 million records is 1.5 seconds for a hash
database and 2.2 seconds for a B+ tree database. Moreover, the database
size is very small and can be up to 8EB. Furthermore, the scalability
of %Name is great.
%endif


%package -n %lname-devel
Summary: Headers for developing programs that will use %lname
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name is a library of routines for managing a database. It is
the successor of QDBM. %Name runs very fast. For example, the
time required to store 1 million records is 1.5 seconds for a hash
database and 2.2 seconds for a B+ tree database. Moreover, the database
size is very small and can be up to 8EB. Furthermore, the scalability
of %Name is great.
This package contains the libraries and header files needed for
developing with %lname.


%if_enabled static
%package -n %lname-devel-static
Summary: Static version of %Name database library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is a library of routines for managing a database. It is
the successor of QDBM. %Name runs very fast. For example, the
time required to store 1 million records is 1.5 seconds for a hash
database and 2.2 seconds for a B+ tree database. Moreover, the database
size is very small and can be up to 8EB. Furthermore, the scalability
of %Name is great.
This package contains static libraries for building statically linked
programs which use %Name.
%endif


%package doc
Summary: Documentation for %Name
Group: Documentation
BuildArch: noarch

%description doc
%Name is a library of routines for managing a database. It is
the successor of QDBM. %Name runs very fast. For example, the
time required to store 1 million records is 1.5 seconds for a hash
database and 2.2 seconds for a B+ tree database. Moreover, the database
size is very small and can be up to 8EB. Furthermore, the scalability
of %Name is great.
This package contains documentation for developers.


%prep
%setup
%patch -p1


%build
%define _optlevel 3
%ifarch %ix86 %x86_64
%add_optflags -minline-all-stringops
%endif
%autoreconf
%configure \
    %{subst_enable fastest} \
    %{subst_enable debug} \
    %{subst_enable devel} \
    %{subst_enable profile} \
    %{subst_enable shared} \
    %{subst_enable uyield} \
    %{subst_enable zlib} \
    %{subst_enable bzip} \
    %{subst_enable_to lzo exlzo} \
    %{subst_enable_to lzma exlzma} \
    %{subst_enable pthread} \
    %{subst_enable off64}
%make_build


%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot%_datadir/%name/{COPYING,README,doc/*.ppt}
bzip2 --best %buildroot%_datadir/%name/ChangeLog
install -d -m 0755 %buildroot%_docdir
mv %buildroot{%_datadir/%name,%_docdir/%name-%version}


%check
%make_build check


%files utils
%_bindir/*
%_libexecdir/*.cgi
%_man1dir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}
%_pkgconfigdir/*
%_man3dir/*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files doc
%_docdir/%name-%version


%changelog
* Mon Mar 02 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.47-alt2
- Rebuilt.

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 1.4.47-alt1
- 1.4.47

* Sun Nov 21 2010 Vladimir Lettiev <crux@altlinux.ru> 1.4.46-alt1
- 1.4.46
- update URL
- dropped packager tag

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.42-alt2
- Rebuilt for soname set-versions

* Thu Jan 21 2010 Led <led@altlinux.ru> 1.4.42-alt1
- 1.4.42

* Wed Dec 09 2009 Led <led@altlinux.ru> 1.4.41-alt1
- 1.4.41

* Mon Nov 16 2009 Led <led@altlinux.ru> 1.4.39-alt1
- 1.4.39:
  + new macros: _alignof, _issigned, _maxof, TCALIGNOF, tcgeneric_t

* Tue Nov 10 2009 Led <led@altlinux.ru> 1.4.38-alt1
- 1.4.38:
  + new function: tcmpoolclear

* Mon Oct 19 2009 Led <led@altlinux.ru> 1.4.35-alt1
- 1.4.35:
  + new functions: tcadbsetskelmulti, tcadbmulnew, tcadbmuldel,
    setskeltran
  + "range" sub function for B+ tree was added to tcadbmisc

* Tue Oct 06 2009 Led <led@altlinux.ru> 1.4.34-alt1
- 1.4.34

* Sun Sep 27 2009 Led <led@altlinux.ru> 1.4.33-alt1
- 1.4.33
- changed URL

* Fri Aug 28 2009 Led <led@altlinux.ru> 1.4.32-alt1
- 1.4.32:
  + added "INC", "PRT" operators and "SET" directive
- 1.4.31:
  + new functions: tcwwwformdecode2, tcarccipher,
    tcmpoolpop, tcstatfile

* Wed Jul 22 2009 Led <led@altlinux.ru> 1.4.30-alt1
- 1.4.30:
  + new function: tctdbstrtometasearcytype
  + added command "metasearch" into tcadbmisc

* Sat Jul 11 2009 Led <led@altlinux.ru> 1.4.29-alt1
- 1.4.29:
  + efficiency couting sort was improved

* Fri Jul 03 2009 Led <led@altlinux.ru> 1.4.28-alt1
- 1.4.28:
  + new functions: tctdbmetasearch, tctdbget4, tctdbqrykwic,
    tctdbsetinvcache, tctdbidxsyncicc, tctdbidxcmpkey, tcstrutfnorm,
    tcstrkwic, tcstrtokenize

* Sat Jun 27 2009 Led <led@altlinux.ru> 1.4.27-alt1
- 1.4.27:
  + new functions: tcstrskipspc, tcstrucsnorm,
    tctdbidxputqgram, tctdbidxoutqgram, tctdbidxgetbyfts
  + added full-text search operators
  + added q-gram inverted index

* Tue Jun 16 2009 Led <led@altlinux.ru> 1.4.26-alt1
- 1.4.26:
  + new functions: tctdbidxputone, tctdbidxoutone, tctdbidxputtoken,
    tctdbidxouttoken, tctdbidxgetbytokens
  + tctdbsetindex, tctdbsearchimpl: token inverted index was added

* Sun Jun 14 2009 Led <led@altlinux.ru> 1.4.25-alt1
- 1.4.25:
  + new functions: tctdbiternext3, tcpathlock, tcpathunlock,
    tccstrescape, tccstrunescape, tcjsonescape, tcjsonunescape

* Wed Jun 10 2009 Led <led@altlinux.ru> 1.4.24-alt1
- 1.4.24:
  + new functions: runtmpl, proctmpl, tclistprintf, tcmapprintf,
    tctreeprintf, tcmapget4, tctreeget4, tctmplnew, tctmpldel,
    tctmplload, tctmpldump, tcwwwformencode, tcwwwformdecode

* Wed May 27 2009 Led <led@altlinux.ru> 1.4.23-alt1
- 1.4.23:
  + new functions: tctdbiterinit2, tcfdbiterinit2, tcfdbiterjumpimpl,
    tchdbiterinit2, tchdbiterjumpimpl, tcmapiterinit2, tcmdbiterinit2

* Sun May 24 2009 Led <led@altlinux.ru> 1.4.22-alt1
- 1.4.22
- 1.4.21:
  + new functions: tctdbsetdfunit, tctdbdfunit, tctdbdefrag,
    tcbdbsetdfunit, tcbdbdfunit, tcbdbdefrag, tchdbdefragimpl,
    tchdbfbptrim, tchdbshiftrec, tchdbsetdfunit, tchdbdfunit,
    tchdbdefrag

* Sat May 09 2009 Led <led@altlinux.ru> 1.4.20-alt1
- 1.4.20

* Thu May 07 2009 Led <led@altlinux.ru> 1.4.19-alt1
- 1.4.19:
  + new functions: tctdbidxhash, tctdbqryproc2, tctdbqrysearchout2
- 1.4.18:
  + new functions: tcadbsetskel, tcatoih

* Sun Apr 26 2009 Led <led@altlinux.ru> 1.4.17-alt1
- 1.4.17:
  + new functions: tctdbqryidxfetch, tcsysinfo
- 1.4.16:
  + new function: tcbdbleafcheck
  + shift mechanism of cursors on deleted leaves was added
- 1.4.15:
  + new functions: tcadboptimize, tcadbpath, tcsleep
  + abolished: tcfdblocktran, tcfdbunlocktran, tchdblocktran,
    tchdbunlocktran

* Tue Apr 07 2009 Led <led@altlinux.ru> 1.4.14-alt1
- 1.4.14:
  + tcbdbputimpl, tcbdbcurputimpl: page size limitation was added
  + removed tcbdbleafdatasize
  + tctdbsetindeximpl: inner indexes were tuned

* Mon Apr 06 2009 Led <led@altlinux.ru> 1.4.13-alt1
- 1.4.13:
  + new functions: tcfdbtranbegin, tcfdbtrancommit, tcfdbtranabort,
    tcadbtranbegin, tcadbtrancommit, tcadbtranabort

* Thu Apr 02 2009 Led <led@altlinux.ru> 1.4.12-alt1
- 1.4.12:
  + new function: tctdbqrycount
  + tcadbmisc: "count" option was added

* Fri Mar 20 2009 Led <led@altlinux.ru> 1.4.11-alt1
- 1.4.11:
  + new function: tctopsort
  + performance and concurrency was improved
  + bugfixes

* Wed Mar 11 2009 Led <led@altlinux.ru> 1.4.10-alt1
- 1.4.10:
  + new function: tchdbremoverec
  + new function: tctdbsetlimit instead of tctdbqrysetmax

* Sat Feb 28 2009 Led <led@altlinux.ru> 1.4.9-alt1
- 1.4.9

* Thu Feb 19 2009 Led <led@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Mon Feb 16 2009 Led <led@altlinux.ru> 1.4.6-alt1
- 1.4.6:
  + new function: tctdbsetuidseed

* Sun Feb 15 2009 Led <led@altlinux.ru> 1.4.5-alt2
- cleaned up CFLAGS

* Sun Feb 15 2009 Led <led@altlinux.ru> 1.4.5-alt1
- 1.4.5:
  + new functions: runrace, procrace
- 1.4.4:
  + new functions: tcstrisnum, tcadbputproc, tcfdbputproc,
    tcbdbputproc, tchdbputproc, tcmapputproc, tctreeputproc,
    tcmdbputproc, tcndbputproc
  + tcadbmisc: added sub funcitons "put", "out", and "get"

* Sat Jan 31 2009 Led <led@altlinux.ru> 1.4.3-alt1
- 1.4.3
- 1.4.2:
  + new function: tcatof
  + tcadb: all methods now support the table database API

* Thu Jan 22 2009 Led <led@altlinux.ru> 1.4.1-alt1
- 1.4.1:
  + new functions: tctdbqryonecondmatch, tctdbsetcache, tctdbforeach,
    tctdbqryproc
- 1.4.0:
  + new functions: tchdbgetnext3, tcstrjoin2, tcstrjoin3, tcstrjoin4,
    tcstrsplit2, tcstrsplit3, tcstrsplit4, tcatoix, tclistinvert,
    tclog2l, tclog2d, tclistnew3, tcmapnew3

* Wed Jan 07 2009 Led <led@altlinux.ru> 1.3.27-alt1
- 1.3.27

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.3.26-alt1
- 1.3.26:
  + new function: tcadbmisc

* Mon Dec 22 2008 Led <led@altlinux.ru> 1.3.25-alt1
- 1.3.25

* Mon Dec 15 2008 Led <led@altlinux.ru> 1.3.24-alt1
- 1.3.24:
  + new functions: tcmdbforeach, tcmdbforeachimpl, tcndbforeach,
    tcndbforeachimpl, tchdbforeach, tchdbforeachimpl, tcbdbforeach,
    tcbdbforeachimpl, tcfdbforeach, tcfdbforeachimpl, tcadbomode,
    tcadbreveal

* Sun Dec 14 2008 Led <led@altlinux.ru> 1.3.23-alt1
- 1.3.23
- 1.3.22:
  + new functions: tcmapput3, tcmdbput3, tcmapputcat3, tcmdbputcat3
    tctreeput3, tcndbput3

* Sun Dec 07 2008 Led <led@altlinux.ru> 1.3.21-alt1
- 1.3.21
- 1.3.20:
  + new functions: tchdbtranbegin, tchdbtrancommit, tchdbtranabort
- cleaned up spec

* Thu Nov 20 2008 Led <led@altlinux.ru> 1.3.19-alt1
- 1.3.19:
  + new functions: tcmdbnew, tcmdbdel, tcmdbopen, tcmdbclose,
    tcptrlistnew, tcptrlistdel, tcbdbputimpl, tcbdboutimpl,
    tcbdbgetimpl
  + tcadbnew, tcadbdel: on-memory tree database is now supported

* Sun Nov 09 2008 Led <led@altlinux.ru> 1.3.16-alt1
- 1.3.16:
  + tcmapdup: performance was improved
  + new functions: tcsystem, tctreenew, tctreedel, tctreeput,
    tctreeout, tctreeget
  + memory usage of reader declined
  + on-memory database is now supported

* Wed Oct 29 2008 Led <led@altlinux.ru> 1.3.15-alt1
- 1.3.15

* Wed Sep 24 2008 Led <led@altlinux.ru> 1.3.10-alt1
- 1.3.10
- updated %name-1.3.10-alt.patch

* Tue Sep 09 2008 Led <led@altlinux.ru> 1.3.8-alt1
- 1.3.8

* Fri Aug 29 2008 Led <led@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Mon Aug 25 2008 Led <led@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Wed Aug 13 2008 Led <led@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Wed Jul 30 2008 Led <led@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Jul 28 2008 Led <led@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Jul 25 2008 Led <led@altlinux.ru> 1.2.12-alt1
- 1.2.12
- initial Build for Sisyphus
- remade spec from Fedora

* Sun May 25 2008 Masahiro Hasegawa <masahase@gmail.com> - 1.2.6-1
- Update to 1.2.6

* Mon Apr 28 2008 Deji Akingunola <dakingun@gmail.com> - 1.2.5-1
- Update to 1.2.5

* Fri Feb 08 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.14-1
- Update to 1.1.14

* Fri Jan 11 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Tue Dec 18 2007 Deji Akingunola <dakingun@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Sat Nov 24 2007 Deji Akingunola <dakingun@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Sat Nov 24 2007 Deji Akingunola <dakingun@gmail.com> - 1.0.6-1
- Initial package
