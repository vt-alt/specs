Summary: Generator Tools for Coding SOAP/XML Web Services in C and C++
Name: gsoap
Version: 2.8.94
Release: alt2
License: GPLv2+
Group: Development/Tools
URL: http://gsoap2.sourceforge.net
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source0: http://downloads.sourceforge.net/gsoap2/gsoap_%version.tar.gz
Patch: %name-%version-alt.patch

#packagereq: optimized out: glibc-devel-static glibc-pthread libcom_err-devel libkrb5-devel libstdc++-devel perl-threads
BuildRequires: dos2unix flex gcc-c++ libssl-devel libstdc++-devel-static tzdata zlib-devel


%description
The gSOAP Web services development toolkit offers an XML to C/C++
language binding to ease the development of SOAP/XML Web services in C
and C/C++.


%package -n lib%name-devel
Summary: Devel libraries and headers for linking with gSOAP generated stubs
Group: Development/C

%description -n lib%name-devel
gSOAP libraries, headers and generators for linking with and creating
gSOAP generated stubs


%package -n lib%name-devel-static
Summary: Static devel libraries and headers for linking with gSOAP generated stubs
Group: Development/C
Requires: zlib-devel-static

%description -n lib%name-devel-static
gSOAP static libraries


%prep
%setup -q -n gsoap-2.8
%patch -p1

# a number of ~ files are distribute, but we do not want them
find . -name "*~" -exec rm {} \;

# we want all txt files to have unix end-of-line encoding
dos2unix README.txt LICENSE.txt NOTES.txt


%build
# patches change autoconf and automake files, so we must reconfigure
autoreconf --install --force

%configure --prefix=/usr

# dependencies are not declared properly
#make %{?_smp_mflags}
make

# during the build a number of files that we should not distribute are
# created in soapcpp2/samples/ (a doc directory), we must remove them
#find soapcpp2/samples/ -name ".deps" -prune -exec rm -rf {} \;

# we do not want to bother distributing samples for Windows or OS X
#rm -rf soapcpp2/samples/magic_VC
#rm -rf soapcpp2/samples/quote_VC
#rm -rf soapcpp2/samples/quote_MAC_ProjBuild

# samples do not need to be executable by default
#chmod a-x soapcpp2/samples/ssl/root.sh
#chmod a-x soapcpp2/samples/ssl/cacerts.pem


%install
make install DESTDIR=%buildroot


%check
make check


%files -n lib%name-devel-static
%_libdir/libgsoapck.a
%_libdir/libgsoapck++.a
%_libdir/libgsoap.a
%_libdir/libgsoapssl.a
%_libdir/libgsoapssl++.a
%_libdir/libgsoap++.a


%files -n lib%name-devel
%doc README.txt NOTES.txt LICENSE.txt
%_bindir/soapcpp2
%_bindir/wsdl2h
%_libdir/pkgconfig/gsoapck.pc
%_libdir/pkgconfig/gsoapck++.pc
%_libdir/pkgconfig/gsoap.pc
%_libdir/pkgconfig/gsoap++.pc
%_libdir/pkgconfig/gsoapssl.pc
%_libdir/pkgconfig/gsoapssl++.pc
%_includedir/stdsoap2.h
%dir %_datadir/gsoap
%dir %_datadir/gsoap/import
%_datadir/gsoap/import/c14n.h
%_datadir/gsoap/import/dom.h
%_datadir/gsoap/import/ds2.h
%_datadir/gsoap/import/ds.h
%_datadir/gsoap/import/README.txt
%_datadir/gsoap/import/soap12.h
%_datadir/gsoap/import/stldeque.h
%_datadir/gsoap/import/stl.h
%_datadir/gsoap/import/stllist.h
%_datadir/gsoap/import/stlset.h
%_datadir/gsoap/import/stlvector.h
%_datadir/gsoap/import/wsa3.h
%_datadir/gsoap/import/wsa4.h
%_datadir/gsoap/import/wsa5.h
%_datadir/gsoap/import/wsa.h
%_datadir/gsoap/import/WS-example.c
%_datadir/gsoap/import/WS-example.h
%_datadir/gsoap/import/WS-Header.h
%_datadir/gsoap/import/wsp.h
%_datadir/gsoap/import/wsrp.h
%_datadir/gsoap/import/wsse2.h
%_datadir/gsoap/import/wsse.h
%_datadir/gsoap/import/wsu.h
%_datadir/gsoap/import/xlink.h
%_datadir/gsoap/import/xmime4.h
%_datadir/gsoap/import/xmime5.h
%_datadir/gsoap/import/xmime.h
%_datadir/gsoap/import/xml.h
%_datadir/gsoap/import/xmlmime5.h
%_datadir/gsoap/import/xmlmime.h
%_datadir/gsoap/import/xop.h
%dir %_datadir/gsoap/WS
%_datadir/gsoap/WS/README.txt
%_datadir/gsoap/WS/WS-Addressing.xsd
%_datadir/gsoap/WS/WS-Addressing03.xsd
%_datadir/gsoap/WS/WS-Addressing04.xsd
%_datadir/gsoap/WS/WS-Addressing05.xsd
%_datadir/gsoap/WS/WS-Discovery.wsdl
%_datadir/gsoap/WS/WS-Enumeration.wsdl
%_datadir/gsoap/WS/WS-Policy.xsd
%_datadir/gsoap/WS/WS-Routing.xsd
%_datadir/gsoap/WS/WS-typemap.dat
%_datadir/gsoap/WS/discovery.xsd
%_datadir/gsoap/WS/ds.xsd
%_datadir/gsoap/WS/enumeration.xsd
%_datadir/gsoap/WS/typemap.dat
%_datadir/gsoap/WS/wsse.xsd
%_datadir/gsoap/WS/wsu.xsd
%dir %_datadir/gsoap/custom
%_datadir/gsoap/custom/README.txt
%_datadir/gsoap/custom/chrono_duration.cpp
%_datadir/gsoap/custom/chrono_duration.h
%_datadir/gsoap/custom/chrono_time_point.cpp
%_datadir/gsoap/custom/chrono_time_point.h
%_datadir/gsoap/custom/float128.c
%_datadir/gsoap/custom/float128.h
%_datadir/gsoap/custom/int128.c
%_datadir/gsoap/custom/int128.h
%_datadir/gsoap/custom/long_double.c
%_datadir/gsoap/custom/long_double.h
%_datadir/gsoap/custom/long_time.c
%_datadir/gsoap/custom/long_time.h
%_datadir/gsoap/custom/struct_timeval.c
%_datadir/gsoap/custom/struct_timeval.h
%_datadir/gsoap/custom/struct_tm.c
%_datadir/gsoap/custom/struct_tm.h
%_datadir/gsoap/custom/struct_tm_date.c
%_datadir/gsoap/custom/struct_tm_date.h
%dir %_datadir/gsoap/extras
%_datadir/gsoap/extras/README.txt
%_datadir/gsoap/extras/ckdb.c
%_datadir/gsoap/extras/ckdb.h
%_datadir/gsoap/extras/ckdbtest.c
%_datadir/gsoap/extras/ckdbtest.h
%_datadir/gsoap/extras/fault.cpp
%_datadir/gsoap/extras/logging.cpp
%_datadir/gsoap/extras/soapdefs.h
%dir %_datadir/gsoap/plugin
%_datadir/gsoap/plugin/README.txt
%_datadir/gsoap/plugin/cacerts.c
%_datadir/gsoap/plugin/cacerts.h
%_datadir/gsoap/plugin/httpda.c
%_datadir/gsoap/plugin/httpda.h
%_datadir/gsoap/plugin/httpdatest.c
%_datadir/gsoap/plugin/httpdatest.h
%_datadir/gsoap/plugin/httpform.c
%_datadir/gsoap/plugin/httpform.h
%_datadir/gsoap/plugin/httpget.c
%_datadir/gsoap/plugin/httpget.h
%_datadir/gsoap/plugin/httpgettest.c
%_datadir/gsoap/plugin/httpgettest.h
%_datadir/gsoap/plugin/httpmd5.c
%_datadir/gsoap/plugin/httpmd5.h
%_datadir/gsoap/plugin/httpmd5test.c
%_datadir/gsoap/plugin/httpmd5test.h
%_datadir/gsoap/plugin/httppost.c
%_datadir/gsoap/plugin/httppost.h
%_datadir/gsoap/plugin/logging.c
%_datadir/gsoap/plugin/logging.h
%_datadir/gsoap/plugin/md5evp.c
%_datadir/gsoap/plugin/md5evp.h
%_datadir/gsoap/plugin/plugin.c
%_datadir/gsoap/plugin/plugin.h
%_datadir/gsoap/plugin/smdevp.c
%_datadir/gsoap/plugin/smdevp.h
%_datadir/gsoap/plugin/threads.c
%_datadir/gsoap/plugin/threads.h
%_datadir/gsoap/plugin/wsaapi.c
%_datadir/gsoap/plugin/wsaapi.h
%_datadir/gsoap/plugin/wsse2api.c
%_datadir/gsoap/plugin/wsse2api.h
%_datadir/gsoap/plugin/wsseapi.c
%_datadir/gsoap/plugin/wsseapi.h
# Additions in 2.7.12-1
%_datadir/gsoap/WS/WS-ReliableMessaging.wsdl
%_datadir/gsoap/WS/WS-ReliableMessaging.xsd
%_datadir/gsoap/WS/reference-1.1.xsd
%_datadir/gsoap/WS/ws-reliability-1.1.xsd
%_datadir/gsoap/import/ref.h
%_datadir/gsoap/import/wsrm.h
%_datadir/gsoap/import/wsrm4.h
%_datadir/gsoap/import/wsrx.h
# Additions in 2.7.13-1
%_datadir/gsoap/import/stdstring.h
%_datadir/gsoap/import/xsd.h
%_datadir/gsoap/plugin/wsseapi.cpp
# Additions in 2.7.15
%_datadir/gsoap/plugin/httpposttest.h
%_datadir/gsoap/plugin/httpposttest.c
# Additions in 2.7.16-1
%_datadir/gsoap/custom/duration.c
%_datadir/gsoap/custom/duration.h
%_datadir/gsoap/plugin/wsrmapi.c
%_datadir/gsoap/plugin/wsrmapi.h
# Additions in 2.7.17-1
%_datadir/gsoap/WS/WS-Policy12.xsd
%_datadir/gsoap/WS/WS-SecurityPolicy.xsd
%_datadir/gsoap/import/wsse11.h
# Additions in 2.8.3-1
%_datadir/gsoap/WS/xenc.xsd
%_datadir/gsoap/import/xenc.h
%_datadir/gsoap/plugin/mecevp.c
%_datadir/gsoap/plugin/mecevp.h
# Additions in 2.8.4-1
%_datadir/gsoap/import/wsdd.h
%_datadir/gsoap/import/wsdx.h
%_datadir/gsoap/plugin/wsddapi.c
%_datadir/gsoap/plugin/wsddapi.h
# Additions in 2.8.7-1
%_datadir/gsoap/import/wsdd10.h
# Additions in 2.8.12-1
%_datadir/gsoap/WS/WS-SecureConversation.xsd
%_datadir/gsoap/WS/WS-Trust.wsdl
%_datadir/gsoap/WS/WS-Trust.xsd
%_datadir/gsoap/import/ser.h
%_datadir/gsoap/import/wsc.h
%_datadir/gsoap/import/wsrm5.h
%_datadir/gsoap/import/wsrx5.h
%_datadir/gsoap/import/wst.h
%_datadir/gsoap/import/wstx.h
# Additions in 2.8.16-1
%_datadir/gsoap/import/wsc2.h
%_datadir/gsoap/plugin/calcrest.h
# Additions in 2.8.17-1
%_datadir/gsoap/plugin/mq.c
%_datadir/gsoap/plugin/mq.h
# Additions in 2.8.21-1
%_datadir/gsoap/WS/LEGAL.txt
%_datadir/gsoap/WS/ws-bpel_abstract_common_base.xsd
%_datadir/gsoap/WS/ws-bpel_executable.xsd
%_datadir/gsoap/WS/ws-bpel_plnktype.xsd
%_datadir/gsoap/WS/ws-bpel_serviceref.xsd
%_datadir/gsoap/WS/ws-bpel_varprop.xsd
%_datadir/gsoap/import/plnk.h
%_datadir/gsoap/import/vprop.h
# Additions in 2.8.22-1
%_datadir/gsoap/import/wsdd5.h
%_datadir/gsoap/plugin/wsseapi-lite.c
%_datadir/gsoap/plugin/wsseapi-lite.h
# Additions in 2.8.23-1
%_datadir/gsoap/WS/oasis-sstc-saml-schema-assertion-1.1.xsd
%_datadir/gsoap/WS/saml-schema-assertion-2.0.xsd
%_datadir/gsoap/import/saml1.h
%_datadir/gsoap/import/saml2.h
# Additions in 2.8.31
%_datadir/gsoap/import/xenc2.h
# Additions in 2.8.34
%_datadir/gsoap/custom/qbytearray_base64.cpp
%_datadir/gsoap/custom/qbytearray_base64.h
%_datadir/gsoap/custom/qbytearray_hex.cpp
%_datadir/gsoap/custom/qbytearray_hex.h
%_datadir/gsoap/custom/qdate.cpp
%_datadir/gsoap/custom/qdate.h
%_datadir/gsoap/custom/qdatetime.cpp
%_datadir/gsoap/custom/qdatetime.h
%_datadir/gsoap/custom/qstring.cpp
%_datadir/gsoap/custom/qstring.h
%_datadir/gsoap/custom/qtime.cpp
%_datadir/gsoap/custom/qtime.h
%_datadir/gsoap/plugin/sessions.c
%_datadir/gsoap/plugin/sessions.h
# Additions in 2.8.35
%_datadir/gsoap/import/wsp_appliesto.h
%_datadir/gsoap/plugin/wstapi.c
%_datadir/gsoap/plugin/wstapi.h
# Additions in 2.8.67
%_datadir/gsoap/import/wst2.h
%_datadir/gsoap/import/wstx2.h
# Additions in 2.8.75
%_datadir/gsoap/plugin/httppipe.c
%_datadir/gsoap/plugin/httppipe.h
# Additions in 2.8.76
%_datadir/gsoap/plugin/curlapi.c
%_datadir/gsoap/plugin/curlapi.h

%changelog
* Mon Oct 21 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.8.94-alt2
- Remove dynamic libraries defected by design

* Sun Oct 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.8.94-alt1
- Update to latest release

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.8.75-alt1
- Update to latest winter release
- Disable ubt macros due binary package identity change

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 2.8.42-alt2.S1.1
- NMU: rebuild with new openssl.

* Tue Dec 26 2017 Denis Medvedev <nbr@altlinux.org> 2.8.42-alt2
- NMU: rebuild for new glibc: fixes bug with xlocale.h

* Wed Feb 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.42-alt1
- Update to new release
- Increment soversion for gsoap libraries

* Sun Jan 10 2016 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.27-alt1
- Update to last stable release with 2.8.x branch

* Thu Apr 18 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.17-alt1
- Update to last stable release with 2.7.x branch
- Fix SOAP_NEW with parenthesis for gcc compatibility
- Fix GSOAPSSL linking flags

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.7.15-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.7.15-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Mar 09 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.7.15-alt1
- Initial build for Sisyphus

* Fri Sep 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.7.13-2
- Fix build

* Mon May 11 2009  <matt@redhat> - 2.7.13-1
- Updated to gsoap 2.7.13

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.7.12-2
- rebuild with new openssl

* Wed Dec 24 2008  <matt@redhat> - 2.7.12-1
- Updated to gsoap 2.7.12:
-  Numerous bug fixes - xml:lang, maxOccurs="unbounded", SSL, xmlns="", ...
-  New features, maintaining backward compatibility - MinGW, wsseapi, multi-endpoint connect, ...
- Patches removed (incorporated upstream):
-  datadir_importpath-2.7.10.patch
-  install_soapcpp2_wsdl2h_aux-2.7.10.patch
-  no_locale.patch as default off, enable by defining WITH_C_LOCALE
- Patches added (sent upstream):
-  unused_args.patch - eliminate many unused param warnings

* Thu Feb 21 2008  <mfarrellee@redhat> - 2.7.10-4
- Applied upd patch from upstream. It fixes glibc C locale issues,
  hp-ux h_errno definition, and xsd:dateTime timezone processing for
  WS-I
- Removed tru64_hp_ux patches, they are present in upstream's upd
  patch
- Added no_locale.patch to stop configure from checking for locale
  version of functions

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.7.10-3
- Autorebuild for GCC 4.3

* Mon Feb 18 2008  <mfarrellee@redhat> - 2.7.10-2
- Removed --disable-namespaces from configure, result is code compiled
  against gsoap does not need to call set_soap_namespaces

* Sun Jan 27 2008  <mfarrellee@redhat> - 2.7.10-1
- Upgraded to 2.7.10 release
- Stopped hosting patches on grid.et.redhat.com
- Removed import_dom_h patch, it was integrated
- Removed large autotools patch, replaced with patch
  (use_libtool-2.7.10.patch) changing configure.in, gsoap/Makefile.am
  and gsoap/wsdl/Makefile.am, which enable libtool use, and a
  call to autoreconf
- Changed soapcpp2 references to gsoap as per new layout of source
  distribution
- Updated tru64_hp_up_c/pp patches to handle new source layout
- Install of soapcpp2/import with cp removed in favor of a patch to
  gsoap/Makefile.am (install_soapcpp2_wsdl2h_aux-2.7.10.patch)
- No pre-generated Makefiles are distributed, no longer removing them
- stdsoap2_cpp.cpp not in distribution, no longer removing it
- Added datadir_importpath-2.7.10.patch to set SOAPCPP2_IMPORT_PATH
  and WSDL2H_IMPORT_PATH, useful defaults, using ${datadir} instead of
  `pwd`
- Added autoconf, automake and libtool to BuildRequires, because
  configure.in and gsoap/Makefile.am are patched
- Added ?dist to Release

* Fri Nov 30 2007  <mfarrellee@redhat> - 2.7.9-0.4.l
- Added OpenSSL requirement

* Tue Nov 27 2007  <mfarrellee@redhat> - 2.7.9-0.3.l
- Decided soapcpp2/import/ files should be in /usr/share instead of
  /usr/include because they are not really headers gcc can
  process. Also, this is likely the location new versions of gsoap
  will install the import headers. People should use -I
  /usr/share/gsoap/import

* Mon Nov 26 2007  <mfarrellee@redhat> - 2.7.9-0.2.l
- Changed license tag to GPLv2+, which is more accurate
- Resolved bz399761 by adding soapcpp2/import/*.h to the -devel
  package as /usr/include/gsoap, users will need to add -I
  /usr/include/gsoap to their soapcpp2 line

* Sun Sep 30 2007  <mfarrellee@redhat> - 2.7.9-0.1.l
- Updated to 2.7.9l (2.7.9k patches still apply)
- Added patch for import/dom.h missing xsd__anyAttribute definitions
- Removed removal of .deps directories and autom4te.cache

* Mon Sep 24 2007  <mfarrellee@redhat> - 2.7.9-0.2.k
- Moved pkgconfig requirement to -devel package

* Tue Sep 11 2007  <mfarrellee@redhat> - 2.7.9-0.1.k
- Initial release

