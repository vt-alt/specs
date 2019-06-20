%def_without pgsql
Name: gnunet
Version: 0.11.5
Release: alt1

Summary: Peer-to-peer framework

License: GPLv3+
Group: Communications
Url: http://gnunet.org/
Packager: ALT QA Team <qa@packages.altlinux.org>

Source: http://ftpmirror.gnu.org/gnunet/%name-%version.tar
# (TODO: add pseudouser)
Source1: gnunetd.init.altlinux
Source2: gnunetd.service

Patch2: gnunet-0.11.0-alt-mysql8-transition.patch

BuildRequires: gcc-c++ libmysqlclient21-devel libgnurl-devel libextractor-devel libgcrypt-devel libglade-devel libncursesw-devel libsqlite3-devel zlib-devel
#BuildRequires: %_bindir/git %_bindir/svnversion libICE-devel libSM-devel 
BuildRequires: glib2-devel libglpk36-devel libgnutls-devel libltdl7-devel libmicrohttpd-devel libunistring-devel pkgconfig(libgtop-2.0) python-devel
BuildRequires: libpulseaudio-devel libopus-devel libogg-devel
BuildRequires: libidn2-devel libjansson-devel libzbar-devel
%if_with pgsql
BuildRequires: libpq-devel
%endif

%description
GNUnet is a peer-to-peer framework with focus on providing security. All
peer-to-peer messages in the network are confidential and authenticated.
The framework provides a transport abstraction layer and can currently
encapsulate the network traffic in UDP (IPv4 and IPv6), TCP (IPv4 and IPv6),
HTTP, or SMTP messages. GNUnet supports accounting to provide contributing
nodes with better service. The primary service build on top of the framework
is anonymous file sharing.

%package -n lib%name
Summary: Libraries needed for %name
Group: System/Libraries

%description -n lib%name
GNUnet is a peer-to-peer framework with focus on providing security. All
peer-to-peer messages in the network are confidential and authenticated.
The framework provides a transport abstraction layer and can currently
encapsulate the network traffic in UDP (IPv4 and IPv6), TCP (IPv4 and IPv6),
HTTP, or SMTP messages. GNUnet supports accounting to provide contributing
nodes with better service. The primary service build on top of the framework
is anonymous file sharing.

%package -n lib%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup
%patch2 -p0

# broken --disable-testing
%__subst "s|ats-tests||" src/Makefile.*

%build
%autoreconf
CFLAGS="%optflags -I%_includedir/mysql"
CXXFLAGS="%optflags -I%_includedir/mysql"
export CFLAGS CXXFLAGS

# disable testing due recursive linking bug
%configure --disable-rpath --disable-testing --disable-documentation
%make_build V=1 || %make V=1

%install
# usr/bin/ld.default: warning: libgnunetblock.so.0, needed by /tmp/.private/lav/gnunet-buildroot/usr/lib64/libgnunetblockgroup.so, not found (try using -rpath or -rpath-link)
# libtool:   error: error: relink 'libgnunet_plugin_block_test.la' with the above command before installing it
export LD_LIBRARY_PATH=$(pwd)/src/block/.libs:$(pwd)/src/ats/.libs:$(pwd)/src/statistics/.libs:$(pwd)/src/json/.libs:$(pwd)/src/gnsrecord/.libs
%makeinstall_std
%find_lang %name
mkdir -p %buildroot{%_initdir,%_unitdir}
install -m0755 %SOURCE1 %buildroot%_initdir/gnunetd
install -m0644 %SOURCE2 %buildroot%_unitdir/gnunetd.service

# unpackaged files found
rm -f %buildroot%_docdir/gnunet/COPYING %buildroot%_docdir/gnunet/README

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%doc %_man1dir/gnunet*.1*
%doc %_man5dir/gnunet*.5*
%_bindir/gnunet-arm
%_bindir/gnunet-ats
%_bindir/gnunet-auto-share
%_bindir/gnunet-bugreport
%_bindir/gnunet-cadet
%_bindir/gnunet-config
%_bindir/gnunet-core
%_bindir/gnunet-directory
%_bindir/gnunet-dht-get
%_bindir/gnunet-dht-monitor
%_bindir/gnunet-dht-put
%_bindir/gnunet-download
#_bindir/gnunet-download-manager.scm
#%_bindir/gnunet-ecc
%_bindir/gnunet-fs
%_bindir/gnunet-gns
#_bindir/gnunet-gns-import.sh
%_bindir/gnunet-gns-proxy-setup-ca
#_bindir/gnunet-mesh
%_bindir/gnunet-namestore
%_bindir/gnunet-nat
%_bindir/gnunet-nat-auto
%_bindir/gnunet-nat-server
%_bindir/gnunet-peerinfo
%_bindir/gnunet-peerstore
#%_bindir/gnunet-pseudonym
%_bindir/gnunet-publish
%_bindir/gnunet-resolver
%_bindir/gnunet-reclaim
#%_bindir/gnunet-rsa
%_bindir/gnunet-search
%_bindir/gnunet-scalarproduct
%_bindir/gnunet-statistics
#_bindir/gnunet-template
#%_bindir/gnunet-testing
#%_bindir/gnunet-testing-run-service
%_bindir/gnunet-transport
%_bindir/gnunet-transport-certificate-creation
%_bindir/gnunet-unindex
%_bindir/gnunet-uri
%_bindir/gnunet-vpn
%_bindir/gnunet-bcd
%_bindir/gnunet-conversation
%_bindir/gnunet-conversation-test
%_bindir/gnunet-datastore
%_bindir/gnunet-identity
%_bindir/gnunet-namecache
%_bindir/gnunet-nse
%_bindir/gnunet-qr
%_bindir/gnunet-revocation
%_bindir/gnunet-zoneimport
#_bindir/gnunet-set-ibf-profiler
#_bindir/gnunet-set-profiler

#_libexecdir/gnunet/libexec/gnunet-helper-audio-playback
#_libexecdir/gnunet/libexec/gnunet-helper-audio-record
#_libexecdir/gnunet/libexec/gnunet-service-conversation



%_datadir/gnunet/
%_initdir/gnunetd
%_unitdir/gnunetd.service

%files -n lib%name
%_libdir/gnunet/
%_libdir/libgnunetarm.so.*
%_libdir/libgnunetats.so.*
%_libdir/libgnunetblock.so.*
%_libdir/libgnunetblockgroup.so.*
%_libdir/libgnunetcadet.so.*
%_libdir/libgnunetconsensus.so.*
%_libdir/libgnunetcore.so.*
%_libdir/libgnunetdatacache.so.*
%_libdir/libgnunetdatastore.so.*
%_libdir/libgnunetdht.so.*
%_libdir/libgnunetdns.so.*
#%_libdir/libgnunetdnsparser.so.*
#%_libdir/libgnunetdnsstub.so.*
%_libdir/libgnunetfragmentation.so.*
%_libdir/libgnunetfs.so.*
%_libdir/libgnunetgns.so.*
#%_libdir/libgnunetgns_common.so.*
%_libdir/libgnunethello.so.*
#%_libdir/libgnunetlockmanager.so.*
#_libdir/libgnunetmesh.so.*
#%_libdir/libgnunetmy.so.*
#%_libdir/libgnunetmysql.so.*
%_libdir/libgnunetnamestore.so.*
%_libdir/libgnunetnatauto.so.*
%_libdir/libgnunetnatnew.so.*
%_libdir/libgnunetnse.so.*
%_libdir/libgnunetnt.so.*
%_libdir/libgnunetpeerinfo.so.*
%_libdir/libgnunetpeerstore.so.*
%if_with pgsql
%_libdir/libgnunetpq.so.*
%endif
%_libdir/libgnunetreclaim.so.*
%_libdir/libgnunetreclaimattribute.so.*
%_libdir/libgnunetrest.so.*
%_libdir/libgnunetregex.so.*
%_libdir/libgnunetregexblock.so.*
%_libdir/libgnunetstatistics.so.*
%_libdir/libgnunetatsapplication.so.*
%_libdir/libgnunetatstransport.so.*
%_libdir/libgnunetscalarproduct.so.*
%_libdir/libgnunetsecretsharing.so.*
%_libdir/libgnunetsq.so.*
%_libdir/libgnunetcurl.so.*
%_libdir/libgnunetjson.so.*
#%_libdir/libgnunetjsonapi.so.*
#%_libdir/libgnunetjsonapiutils.so.*
#%_libdir/libgnunetstream.so.*
#%_libdir/libgnunettestbed.so.*
#%_libdir/libgnunettesting.so.*
%_libdir/libgnunettransport.so.*
%_libdir/libgnunettransportcore.so.*
%_libdir/libgnunettransportmonitor.so.*
%_libdir/libgnunettransportapplication.so.*
%_libdir/libgnunettransportcommunicator.so.*
#%_libdir/libgnunettun.so.*
%_libdir/libgnunetutil.so.*
%_libdir/libgnunetvpn.so.*
%_libdir/libgnunetconversation.so.*
%_libdir/libgnunetfriends.so.*
%_libdir/libgnunetgnsrecord.so.*
%_libdir/libgnunetidentity.so.*
%_libdir/libgnunetmicrophone.so.*
%_libdir/libgnunetnamecache.so.*
%_libdir/libgnunetrevocation.so.*
%_libdir/libgnunetset.so.*
%_libdir/libgnunetspeaker.so.*

%files -n lib%name-devel
%_includedir/gnunet/
%_libdir/*.so
%_pkgconfigdir/gnunetarm.pc
%_pkgconfigdir/gnunetats.pc
%_pkgconfigdir/gnunetblock.pc
%_pkgconfigdir/gnunetcadet.pc
%_pkgconfigdir/gnunetcore.pc
%_pkgconfigdir/gnunetdatacache.pc
%_pkgconfigdir/gnunetdatastore.pc
%_pkgconfigdir/gnunetdht.pc
%_pkgconfigdir/gnunetdns.pc
#%_pkgconfigdir/gnunetdnsparser.pc
#%_pkgconfigdir/gnunetdv.pc
%_pkgconfigdir/gnunetfragmentation.pc
%_pkgconfigdir/gnunetfs.pc
%_pkgconfigdir/gnunetgns.pc
%_pkgconfigdir/gnunethello.pc
#%_pkgconfigdir/gnunetlockmanager.pc
#_pkgconfigdir/gnunetmesh.pc
%_pkgconfigdir/gnunetmysql.pc
%_pkgconfigdir/gnunetnamestore.pc
%_pkgconfigdir/gnunetnat.pc
%_pkgconfigdir/gnunetnse.pc
%_pkgconfigdir/gnunetpeerinfo.pc
#_pkgconfigdir/gnunetpostgres.pc
%_pkgconfigdir/gnunetregex.pc
%_pkgconfigdir/gnunetrps.pc
%_pkgconfigdir/gnunetstatistics.pc
#%_pkgconfigdir/gnunetstream.pc
%_pkgconfigdir/gnunettestbed.pc
%_pkgconfigdir/gnunettesting.pc
%_pkgconfigdir/gnunettransport.pc
#%_pkgconfigdir/gnunettun.pc
%_pkgconfigdir/gnunetutil.pc
%_pkgconfigdir/gnunetvpn.pc

%_libdir/pkgconfig/gnunetconsensus.pc
%_libdir/pkgconfig/gnunetconversation.pc
#%_libdir/pkgconfig/gnunetdnsstub.pc
%_libdir/pkgconfig/gnunetenv.pc
%_libdir/pkgconfig/gnunetidentity.pc
%_libdir/pkgconfig/gnunetmicrophone.pc
#%_libdir/pkgconfig/gnunetmulticast.pc
#%_libdir/pkgconfig/gnunetpsyc.pc
#%_libdir/pkgconfig/gnunetpsycstore.pc
%_libdir/pkgconfig/gnunetrevocation.pc
%_libdir/pkgconfig/gnunetscalarproduct.pc
%_libdir/pkgconfig/gnunetset.pc
%_libdir/pkgconfig/gnunetspeaker.pc

%changelog
* Tue Jun 18 2019 Vitaly Lipatov <lav@altlinux.ru> 0.11.5-alt1
- new version 0.11.5 (with rpmrb script)
- disable PostgreSQL support

* Fri Mar 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.11.0pre666-alt2
- fix FTBFS against libmysqlclient21
  + spec: add missing include subdir for configure to autodetect libmysqlclient

* Mon Nov 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.11.0pre666-alt1
- new version 0.11.0pre666 (with rpmrb script)
- build with libidn2

* Mon Sep 17 2018 Alexey Shabalin <shaba@altlinux.org> 0.10.1-alt4
- rebuild with libmicrohttpd-0.9.59

* Mon Aug 13 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt3
- drop excessive guile18-devel BR

* Thu May 31 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt2
- rebuilld with libmariadb
- fix sysvinit script
- add systemd unit

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- build new version

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.5a-alt1.qa3
- NMU: rebuilt with libunistring.so.2.

* Fri May 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5a-alt1.2
- Rebuilt with glpk36

* Wed Apr 02 2014 Alexei Takaseev <taf@altlinux.org> 0.9.5a-alt1.1.1
- fix buildreq libpq5.4-devel to libpq-devel

* Fri Jan 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5a-alt1.1
- Rebuilt with glpk35

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.5a-alt1
- Friendly NMU: update to 0.9.5a

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Rebuilt with glpk 4.48

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1
- Friendly NMU: update to 0.9.5

* Sun Jan 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1
- Friendly NMU: update to 0.9.1

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt3.1
- Fixed build

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt3
- fix build

* Thu Nov 25 2010 Paul Wolneykien <manowar@altlinux.ru> 0.8.1-alt2
- Add a GNUNet daemon service (init) script.

* Sun Jan 31 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version (0.8.1) import in git

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1 - 5740+/dries
- Updated to release 0.7.2.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.
