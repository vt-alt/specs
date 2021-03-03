# This spec is backported to ALTLinux p9 automatically by rpmbph script from etersoft-build-utils.
#
%def_enable docs
%def_enable mysql
%def_enable sqlite
%def_enable pgsql
%def_enable python
%def_enable rrd
%def_enable io
%def_enable logicproc
#%def_enable modbus
%def_disable tests
%def_disable mqtt
%def_disable netdata
%def_enable api
%def_enable logdb
%def_enable opentsdb
%def_enable uresolver

%ifarch %ix86
%def_enable com485f
%else
%def_disable com485f
%endif

%define oname uniset2

Name: libuniset2
Version: 2.9.3
Release: alt1.M90P.2
Summary: UniSet - library for building distributed industrial control systems

License: LGPL-2.1
Group: Development/C++
Url: http://wiki.etersoft.ru/UniSet

Packager: Pavel Vainerman <pv@altlinux.ru>

# Git: http://git.etersoft.ru/projects/asu/uniset.git
Source: %name-%version.tar

# Automatically added by buildreq on Fri Aug 26 2016
# optimized out: fontconfig libgpg-error libsasl2-3 libsqlite3-devel libstdc++-devel libwayland-client libwayland-server perl pkg-config python-base python-devel python-module-omniidl python-modules python3
BuildRequires: gcc-c++ libev-devel libomniORB-devel libpoco-devel libsigc++2-devel libxml2-devel xsltproc

# for uniset2-codegen
BuildPreReq: xsltproc

# due -std=c++11 using
# BuildPreReq: gcc5 >= 4.8
# Must be gcc >= 4.7

%if_enabled io
BuildRequires: libcomedi-devel
%endif

%if_enabled mysql
# build with mariadb 
BuildRequires: libmariadb-devel
%endif

%if_enabled sqlite
BuildRequires: libsqlite3-devel
%endif

%if_enabled pgsql
BuildRequires: libpqxx-devel
%endif

%if_enabled rrd
BuildRequires: librrd-devel
%endif

%if_enabled mqtt
BuildRequires: libmosquitto-devel
%endif

%if_enabled netdata
BuildRequires: netdata
%endif

%if_enabled python
BuildRequires: python-devel python-module-distribute
BuildRequires(pre): rpm-build-python

# swig
# add_findprov_lib_path %python_sitelibdir/%oname
%endif

%if_enabled docs
BuildRequires: doxygen graphviz ImageMagick-tools
%endif

%if_enabled tests
BuildRequires: catch
%endif

#set_verify_elf_method textrel=strict,rpath=strict,unresolved=strict

%description
UniSet is a library for distributed control systems.
There are set of base components to construct this kind of systems:
* base interfaces for your implementation of control algorithms.
* algorithms for the discrete and analog input/output based on COMEDI interface.
* IPC mechanism based on CORBA (omniORB).
* logging system based on MySQL,SQLite,PostgreSQL databases.
* Web interface to display logging and statistic information.
* utilities for system's configuration based on XML.

UniSet have been written in C++ and IDL languages but you can use another languages in your
add-on components. The main principle of the UniSet library's design is a maximum integration
with open source third-party libraries. UniSet provide the consistent interface for all
add-on components and third-party libraries.

More information in Russian:

%package devel
Group: Development/C
Summary: Libraries needed to develop for UniSet
Requires: %name = %version-%release

%description devel
Libraries needed to develop for UniSet.


%if_enabled python
%package -n python-module-%oname
Group: Development/Python
Summary: python interface for libuniset
Requires: %name = %version-%release

# py_provides UGlobal UInterface UniXML uniset

%description -n python-module-%oname
Python interface for %name
%endif

%if_enabled netdata
%package netdata-plugin
Group: Development/Tools
Summary: python plugin for netdata
Requires: python-module-%oname

%description netdata-plugin
python plugin for netdata
%endif

%package utils
Summary: UniSet utilities
Group: Development/Tools
Requires: %name = %version-%release
Provides: %oname-utils
Obsoletes: %oname-utils

%description utils
UniSet utilities

%if_enabled docs

%package docs
Group: Development/C++
Summary: Documentations for developing with UniSet
# Requires: %name = %version-%release
BuildArch: noarch

%description docs
Documentations for developing with UniSet
%endif

%package extension-common
Group: Development/C++
Summary: libUniSet2 extensions common
Requires: %name = %version-%release

%description extension-common
Extensions for libuniset

%package extension-common-devel
Group: Development/C++
Summary: Libraries needed to develop for uniset extensions
Requires: %name-devel = %version-%release
Provides: %name-extentions-devel
Obsoletes: %name-extentions-devel

%description extension-common-devel
Libraries needed to develop for uniset extensions

%if_enabled uresolver
%package extension-uresolver
Group: Development/Tools
Summary: CORBA object reference resolver based on http

%description extension-uresolver
CORBA object reference resolver based on http
%endif

%if_enabled mysql
%package extension-mysql
Group: Development/Databases
Summary: MySQL-dbserver implementatioin for UniSet
Requires: %name-extension-common = %version-%release

%description extension-mysql
MySQL dbserver for %name

%package extension-mysql-devel
Group: Development/Databases
Summary: Libraries needed to develop for uniset MySQL
Requires: %name-extension-common-devel = %version-%release

%description extension-mysql-devel
Libraries needed to develop for uniset MySQL
%endif

%if_enabled sqlite
%package extension-sqlite
Group: Development/Databases
Summary: SQLite-dbserver implementatioin for UniSet
Requires: %name-extension-common = %version-%release

%description extension-sqlite
SQLite dbserver for %name

%package extension-sqlite-devel
Group: Development/Databases
Summary: Libraries needed to develop for uniset SQLite
Requires: %name-extension-common = %version-%release

%description extension-sqlite-devel
Libraries needed to develop for uniset SQLite

%if_enabled logdb
%package extension-logdb
Group: Development/C++
Summary: database for %name logs (sqlite)
Requires: %name-extension-sqlite = %version-%release

%description extension-logdb
Database (sqlite) for logs for %name
%endif
%endif

%if_enabled opentsdb
%package extension-opentsdb
Group: Development/C++
Summary: backend for OpenTSDB
Requires: %name-extension-common = %version-%release

%description extension-opentsdb
Backend for OpenTSDB

%package extension-opentsdb-devel
Group: Development/Databases
Summary: Libraries needed to develop for uniset OpenTSDB backend
Requires: %name-extension-common-devel = %version-%release

%description extension-opentsdb-devel
Libraries needed to develop for backend for OpenTSDB

%endif

%if_enabled pgsql
%package extension-pgsql
Group: Development/Databases
Summary: PostgreSQL-dbserver implementatioin for UniSet
Requires: %name-extension-common = %version-%release

%description extension-pgsql
PostgreSQL dbserver for %name

%package extension-pgsql-devel
Group: Development/Databases
Summary: Libraries needed to develop for uniset PostgreSQL
Requires: %name-extension-common-devel = %version-%release

%description extension-pgsql-devel
Libraries needed to develop for uniset PostgreSQL
%endif

%if_enabled rrd
%package extension-rrd
Group: Development/C++
Summary: libUniSet2 RRD extension
Requires: %name-extension-common = %version-%release
%description extension-rrd
RRD extensions for libuniset

%package extension-rrd-devel
Group: Development/C++
Summary: Libraries needed to develop for uniset RRD extension
Requires: %name-extension-common-devel = %version-%release

%description extension-rrd-devel
Libraries needed to develop for uniset RRD extension
%endif

%if_enabled logicproc
%package extension-logicproc
Group: Development/C++
Summary: LogicProcessor extension for libUniSet
Requires: %name-extension-common = %version-%release

%description extension-logicproc
LogicProcessor for %name

%package extension-logicproc-devel
Group: Development/C++
Summary: Libraries needed to develop for uniset LogicProcesor extension
Requires: %name-extension-common-devel = %version-%release

%description extension-logicproc-devel
Libraries needed to develop for uniset LogicProcessor extension
%endif

%if_enabled io
%package extension-io
Group: Development/C++
Summary: IOControl with io for UniSet
Requires: %name-extension-common = %version-%release

%description extension-io
IOControl for %name

%package extension-io-devel
Group: Development/C++
Summary: Libraries needed to develop for uniset IOControl (io)
Requires: %name-extension-common-devel = %version-%release

%description extension-io-devel
Libraries needed to develop for uniset IOControl (io)
%endif

%if_enabled mqtt
%package extension-mqtt
Group: Development/C++
Summary: MQTTpublisher from UniSet
Requires: %name-extension-common = %version-%release

%description extension-mqtt
MQTT for %name

%package extension-mqtt-devel
Group: Development/C++
Summary: Libraries needed to develop for uniset MQTT extension
Requires: %name-extension-common-devel = %version-%release

%description extension-mqtt-devel
Libraries needed to develop for uniset MQTT extension
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable docs} %{subst_enable mysql} %{subst_enable sqlite} %{subst_enable pgsql} %{subst_enable python} %{subst_enable rrd} %{subst_enable io} %{subst_enable logicproc} %{subst_enable tests} %{subst_enable mqtt} %{subst_enable api} %{subst_enable netdata} %{subst_enable logdb} %{subst_enable com485f} %{subst_enable opentsdb}
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%if_enabled docs
rm -f %buildroot%_docdir/%oname/html/*.map
rm -f %buildroot%_docdir/%oname/html/*.md5
%endif

%files utils
%_bindir/%oname-admin
%_bindir/%oname-mb*
%_bindir/%oname-nullController
%_bindir/%oname-sviewer-text
%_bindir/%oname-smonit
%_bindir/%oname-vmonit
%_bindir/%oname-simitator
%_bindir/%oname-log
%_bindir/%oname-logserver-wrap
%_bindir/%oname-start*
%_bindir/%oname-stop*
%_bindir/%oname-func*
%_bindir/%oname-codegen
%_bindir/%oname-log2val
%dir %_datadir/%oname/
%dir %_datadir/%oname/xslt/
%_datadir/%oname/xslt/*.xsl
%_datadir/%oname/xslt/skel*


%files
%_libdir/libUniSet2.so.*

%files devel
%dir %_includedir/%oname/
%_includedir/%oname/*.h
%_includedir/%oname/*.hh
%_includedir/%oname/*.tcc
%_includedir/%oname/modbus/

%_libdir/libUniSet2.so
%_datadir/idl/%oname/
%_pkgconfigdir/libUniSet2.pc

%if_enabled mysql
%files extension-mysql
%_bindir/%oname-mysql-*dbserver
%_libdir/*-mysql.so*

%files extension-mysql-devel
%_pkgconfigdir/libUniSet2MySQL.pc
%_includedir/%oname/extensions/mysql/
%endif

%if_enabled sqlite
%files extension-sqlite
%_bindir/%oname-sqlite-*dbserver
%_libdir/*-sqlite.so.*

%files extension-sqlite-devel
%_pkgconfigdir/libUniSet2SQLite.pc
%_includedir/%oname/extensions/sqlite/
%_libdir/*-sqlite.so

%if_enabled logdb
%files extension-logdb
%_bindir/%oname-logdb*
%endif
%endif

%if_enabled opentsdb
%files extension-opentsdb
%_bindir/%oname-backend-opentsdb*
%_libdir/libUniSet2BackendOpenTSDB.so.*

%files extension-opentsdb-devel
%_pkgconfigdir/libUniSet2BackendOpenTSDB.pc
%_includedir/%oname/extensions/BackendOpenTSDB.h
%_libdir/libUniSet2BackendOpenTSDB.so
%endif

%if_enabled pgsql
%files extension-pgsql
%_bindir/%oname-pgsql-*dbserver
%_libdir/*-pgsql.so.*

%files extension-pgsql-devel
%_pkgconfigdir/libUniSet2PostgreSQL.pc
%_includedir/%oname/extensions/pgsql/
%_libdir/*-pgsql.so
%endif

%if_enabled python
%files -n python-module-%oname
%python_sitelibdir/*
%python_sitelibdir_noarch/%oname/*
%dir %python_sitelibdir_noarch/%oname
%endif

%if_enabled netdata
%files netdata-plugin
%_libdir/netdata/python.d/*.*
%config(noreplace) %_sysconfdir/netdata/python.d/*.conf
%endif

%if_enabled docs
%files docs
%_docdir/%oname/
%endif

%files extension-common
%_bindir/%oname-mtr-conv
%_bindir/%oname-mtr-setup
%_bindir/%oname-mtr-read
%_bindir/%oname-vtconv
%_bindir/%oname-rtu188-state
%_bindir/%oname-rtuexchange
%_bindir/%oname-smemory
%_bindir/%oname-smviewer
%_bindir/%oname-network
%_bindir/%oname-unet*

%_libdir/libUniSet2Extensions.so.*
%_libdir/libUniSet2MB*.so.*
%_libdir/libUniSet2RT*.so.*
%_libdir/libUniSet2Shared*.so.*
%_libdir/libUniSet2Network*.so.*
%_libdir/libUniSet2UNetUDP*.so.*

%if_enabled logicproc
%files extension-logicproc
%_libdir/libUniSet2LP*.so.*
%_bindir/%oname-logicproc
%_bindir/%oname-plogicproc

%files extension-logicproc-devel
%_pkgconfigdir/libUniSet2Log*.pc
%_libdir/libUniSet2LP*.so
%_includedir/%oname/extensions/logicproc/
%endif

%if_enabled rrd
%files extension-rrd
%_bindir/%oname-rrd*
%_libdir/libUniSet2RRD*.so.*

%files extension-rrd-devel
%_pkgconfigdir/libUniSet2RRD*.pc
%_libdir/libUniSet2RRD*.so
%_includedir/%oname/extensions/rrd/
%endif

%if_enabled io
%files extension-io
%_bindir/%oname-iocontrol
%_bindir/%oname-iotest
%_bindir/%oname-iocalibr
%_libdir/libUniSet2IO*.so.*

%files extension-io-devel
%_libdir/libUniSet2IO*.so
%_pkgconfigdir/libUniSet2IO*.pc
%_includedir/%oname/extensions/io/
%endif

%if_enabled mqtt
%files extension-mqtt
%_bindir/%oname-mqtt*
%_libdir/libUniSet2MQTTPublisher*.so.*

%files extension-mqtt-devel
%_pkgconfigdir/libUniSet2MQTTPublisher*.pc
%_libdir/libUniSet2MQTTPublisher*.so
%_includedir/%oname/extensions/mqtt/
%endif

%if_enabled uresolver
%files extension-uresolver
%_bindir/%oname-httpresolver*
%endif

%files extension-common-devel
%dir %_includedir/%oname/extensions
%_includedir/%oname/extensions/*.*
%exclude %_includedir/%oname/extensions/BackendOpenTSDB.h
%_libdir/libUniSet2Extensions.so
%_libdir/libUniSet2MB*.so
%_libdir/libUniSet2RT*.so
%_libdir/libUniSet2Shared*.so
%_libdir/libUniSet2Network.so
%_libdir/libUniSet2UNetUDP.so
%_pkgconfigdir/libUniSet2Extensions.pc
%_pkgconfigdir/libUniSet2MB*.pc
%_pkgconfigdir/libUniSet2RT*.pc
%_pkgconfigdir/libUniSet2Shared*.pc
%_pkgconfigdir/libUniSet2Network*.pc
%_pkgconfigdir/libUniSet2UNet*.pc

#%_pkgconfigdir/libUniSet2*.pc
%exclude %_pkgconfigdir/libUniSet2.pc

# history of current unpublished changes

%changelog
* Fri Feb 12 2021 Pavel Vainerman <pv@altlinux.ru> 2.9.3-alt1.M90P.2
- backport to ALTLinux p9 (by rpmbph script)

* Sun Jan 31 2021 Pavel Vainerman <pv@altlinux.ru> 2.9.3-alt2
- fixed lib version

* Thu Jan 14 2021 Pavel Vainerman <pv@altlinux.ru> 2.9.3-alt1
- minor fixes (supported old omniORB)

* Sat Jan 09 2021 Pavel Vainerman <pv@altlinux.ru> 2.9.2-alt1
- admin: added 'sinfo' function
- admin: freezeValue -> freeze/unfreeze
- globally updated help

* Fri Jan 08 2021 Pavel Vainerman <pv@altlinux.ru> 2.9.1-alt1
- supported http-resolver (when localIOR=1)

* Thu Jan 07 2021 Pavel Vainerman <pv@altlinux.ru> 2.8.2-alt1
- supported "freeze vaule"
- modbus master: runtime reload config
- update docs

* Sat Jan 02 2021 Pavel Vainerman <pv@altlinux.ru> 2.8.1-alt3
- make style
- fixed docs

* Sun Dec 27 2020 Pavel Vainerman <pv@altlinux.ru> 2.8.1-alt2
- ALT spec: some fixes

* Fri Dec 25 2020 Pavel Vainerman <pv@altlinux.ru> 2.8.1-alt1
- logserver/logreader refactoring
- update docs
- some python-module refactoring

* Sun Oct 25 2020 Pavel Vainerman <pv@altlinux.ru> 2.8-alt15
- minor fixes

* Fri Feb 14 2020 Pavel Vainerman <pv@altlinux.ru> 2.8-alt14
- removed old define -D_GLIBCXX_USE_NANOSLEEP

* Fri Feb 14 2020 Pavel Vainerman <pv@altlinux.ru> 2.8-alt13
- (UNetUDP): added --unet-packsendpause and --unet-packsendpause-factor

* Tue Jan 28 2020 Pavel Vainerman <pv@altlinux.ru> 2.8-alt12
- minor fixes

* Sun Jan 26 2020 Pavel Vainerman <pv@altlinux.ru> 2.8-alt11
- remove std=c++11 cflags

* Thu Dec 19 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt10
- (DBServer_PostrgeSQL): fix for check connection

* Mon Jul 15 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt9
- (UNetUDP): fix bug in init digital sensors

* Mon Mar 18 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt8
- minor fixes

* Sun Feb 24 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt7
- (LogDB): added support write logfiles

* Mon Feb 11 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt6
- (TSDB): reopen connection for error "broken pipe"

* Sat Feb 09 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt5
- (uniset-codegen): setup logrotate command

* Tue Feb 05 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt4
- (PGSQL): fix SIGSEGV in flushInsertBuffer()

* Tue Feb 05 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt3
- (admin): fix error in "sendText" funciton

* Mon Feb 04 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt2
- added 'mtype' for TextMessage

* Sun Feb 03 2019 Pavel Vainerman <pv@altlinux.ru> 2.8-alt1
- added new public function 'pushMessage(string)'

* Thu Jan 31 2019 Pavel Vainerman <pv@altlinux.ru> 2.7-alt17
- new release

* Thu Oct 11 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt16
- (codegen): reformat
- (Modbus): modify genRegID(), update test, used 'using' instead 'typedef'
- (UNet): set default prefix for log setup (default: "--unet-log")
- (UNet): increased the maximum allowed number of analog values for node (2000)

* Tue Sep 04 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt15
- (mtr): fix bug for read from 'serial device'
- (UNet): added "undefined_value" property
- (SM): added undefined value for IOController
- (RTU): minor fixes (catch exceptions)
- (UNetUDP): check byte order
- (UNetUDP): encoding is not used if the byte order is the same as the system
- (ComPort485F): added error handling for read
- (mbrtutest): added 'polltime' option eterbug #13154

* Thu Aug 02 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt14
- remove deprecated classes
- (SM): fixed bug 'uninitialized time value'

* Wed Jul 11 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt13
- (UActivator): refactoring the program termination process
- minor fixes 

* Sun Jun 10 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt12
- spec cleanup

* Mon Jun 04 2018 Alexey Shabalin <shaba@altlinux.ru> 2.7-alt11
- rebuild with libmariadb

* Thu May 24 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt10
- fix pack opentsdb backend

* Thu May 24 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt9
- added opentsdb backend

* Fri May 18 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt8
- (codegen): added msgstr() function
- make style

* Tue May 08 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt7
- (http): added support "CORS" (Access-Control-Allow-Origin)
- (logdb): added --logdb-httpserver-reply-addr host:port
- minor fixes in LogSession

* Tue Apr 03 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt6
- new minor release

# * Wed Mar 28 2018 Vinogradov Aleksei <uzum@server> 2.7-alt5
# - test build after rebase pv/master

* Fri Mar 09 2018 Alexei Takaseev <taf@altlinux.org> 2.7-alt4.1
- Rebuild with poco 1.9.0

* Wed Feb 21 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt4
- (omniThread): fix compile error for 'const' function and other minor fixes

* Thu Feb 01 2018 Pavel Vainerman <pv@altlinux.ru> 2.7-alt3
- minor fixes

* Wed Jan 10 2018 Alexei Takaseev <taf@altlinux.org> 2.7-alt2.1
- Rebuild with poco 1.8.1

* Thu Dec 14 2017 Pavel Vainerman <pv@altlinux.ru> 2.7-alt2
- minor fixes

* Wed Dec 13 2017 Pavel Vainerman <pv@altlinux.ru> 2.7-alt1
- new component 'logdb'
- added 'const' for more functions
- minor fixes
- remove deprecated components

* Sun Nov 12 2017 Alexei Takaseev <taf@altlinux.org> 2.6-alt41.1
- Rebuild with poco 1.8.0.1

# * Thu Nov 02 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt41
#- build new version

#* Mon Sep 25 2017 Pavel Vainerman <pv@altlinux.ru> 2.7-alt1
#- change directory structure
#- shared_ptr --> unique_ptr
#- minor refactoring
#- remote deprecated components
#- added LogDB

# * Thu Nov 02 2017 Vinogradov Aleksei <uzum@server> 2.6-alt40
# - DBInterface: minor fix in method name

# * Wed Nov 01 2017 Vinogradov Aleksei <uzum@server> 2.6-alt39
# - PostgreSQLInterface: cancel query method added

* Tue Sep 12 2017 Alexei Takaseev <taf@altlinux.org> 2.6-alt19.1
- Rebuild with poco 1.7.9

# * Mon Jul 31 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt38
# - iocontrol: fix segfault

# * Tue Jul 11 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt37
# - (LogReader): add '--grep' mode
# - minor fixes
# - MBExchange: safemode

# * Wed Jun 28 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt36
# - new release (fixes after coverity scan)

# * Tue Jun 27 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt35
# - (Modbus): add new log

# * Sun Jun 25 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt34
# - (DelayTimer): add new functions (isWaiting[On|Off])

# * Sun Jun 25 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt33
# - (ModbusSlave): Added processing of a couple of new errors
# - (UNet): added initial pause mechanism

# * Sat Jun 03 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt32
# - refactoring function names

# * Sat Jun 03 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt31
# - (EventLoopServer): refactoring start process

# * Sat Jun 03 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt30
# - test build (devel)

# * Fri Jun 02 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt29
# - test build (devel)

# * Thu Jun 01 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt27
# - test build (devel)

# * Thu Jun 01 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt26
# - test build (devel)

# * Wed May 31 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt25
# - test build (devel)

# * Wed May 31 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt25
# - test build (devel)

# * Wed May 31 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt24
# - minor release

# * Tue May 30 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt23.1
# - CommonEventLoop refactring start process

# * Mon May 29 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt23
# - (Configuration): add getStartapIgnoreTimeout()
# - minor fixes

# * Mon May 29 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt22
# - set default sm-ready-timeout to 120000 msec (2 min)
# - changed raise(SIGTERM) --> std::terminate()

# * Mon May 29 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt21
# - (UNetExchange): add function for setup eventloop timeout 

# * Sun May 28 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt20
# - (Configuration): fixed bug in check endPoint function

* Thu May 25 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt19
- MBSlave: Now does not terminate when socket is not open
- Configuration: Now does not terminate when endPoint is not available
- minor fixes

* Tue May 09 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt18
- DBInterface refactoring (setbug #12672)

* Sun May 07 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt17
- IOC:askSensor() refactoring N2

* Wed May 03 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt16
- IOC:askSensor() refactoring

* Mon May 01 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt15
- (codegen): add msg statistic for getInfo()
- (http): minor fixes format for help

* Thu Apr 20 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt14
- IOBase: added support 'precision < 0'
- LogicProcessor: add "A2D" element (analog to discrete)

* Thu Apr 20 2017 Alexei Takaseev <taf@altlinux.org> 2.6-alt12.1
- Rebuild with poco 1.7.8p2

* Mon Feb 27 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt12
- up version

* Tue Feb 21 2017 Alexei Takaseev <taf@altlinux.org> 2.6-alt10.1
- Rebuild with poco 1.7.7

* Mon Jan 09 2017 Pavel Vainerman <pv@altlinux.ru> 2.6-alt10
- add tests for REST API (with RPC)
- python: refactoring UInterface (add UInterfaceModbus and UInterfaceUniSet)
- refactoring TCPCheck (use future)
- minor refactoring and fixes

* Fri Dec 16 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt9
- UObject: added attempts to activate the object

* Wed Dec 14 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt8
- SM: terminate if read dump (configuration) failed

* Tue Dec 13 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt7
- Modbus: refactoring code and test (for 64bit)
- iobase: refactoring tests for 64bit
- TCPCheck: fixed bug (for exit thread)
- UNetUDP: minor fixes in tests

* Mon Dec 12 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt6
- codegen: up timeout or activate
- codegen: add logs for startup

* Thu Dec 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt5
- fixed bug in uniset2-admin --oinfo

* Wed Dec 07 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt4
- new version
- getChangedTime --> getTimeChange
- getInfo( long param ) --> getInfo( string param )
- IDL Interface: added new function: string apiRequest( string query )
- getInfo() deprecated..

* Sun Dec 04 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt3.3
- IOC rest api: reformat json reply

* Sat Dec 03 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt3.2
- getChangedTime --> getTimeChange
- getInfo( long param ) --> getInfo( string param )
- IDL Interface: added new function: string apiRequest( string query )
  / ..getInfo() deprecated now.. /

* Tue Nov 22 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt3.1
- CommonEventLoop: refactoring prepare process (part. 2)

* Tue Nov 22 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt3
- CommonEventLoop: refactoring prepare process

* Mon Nov 21 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt2
- UNet: fixed bug in change receive channel

* Sat Nov 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt1.5
- LogServer: attempt to fixed bug in run fuction (infinity lock)

* Sat Nov 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt1.4
- LogServer: attempt to fixed bug in run fuction (infinity lock)

* Sat Nov 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt1.3
- (codegen): add process state info for getInfo()

* Fri Nov 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt1.2
- set default activate-timeout 30 sec
- show pid() in getInfo()
- minor fixes

* Fri Nov 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt1.1
- add try/catch for run log server

* Fri Nov 11 2016 Pavel Vainerman <pv@altlinux.ru> 2.6-alt1
- build new version
- remove 'fastSaveValue'
- add suppor HTTP REST API
- (SM): add new statistics for consumers

* Mon Oct 24 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt20
- correction after verification static analyzer (part 2)
- LogServer: fixed bug "connection refuse" (again)
- DebugStream: refactoring, add showMicroseconds(),showMilliseconds

* Sat Oct 22 2016 Alexei Takaseev <taf@altlinux.org> 2.5-alt19.1
- Rebuild with poco 1.7.6

* Tue Oct 11 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt19
- Calibration: fixed bug in getValue(), refactoring
- correction after verification static analyzer
- LogServer: fixed bug "connection refuse"

* Sat Oct 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt18
- LogServer: fixed bug "do not close connection"

* Fri Sep 30 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt17
- ModbusMultiMaster: add new check connection strategy
- LogServer: minor fixes

* Tue Sep 27 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt16
- LogSession: add more logs
- codegen: add logserver information in getInfo()

* Tue Sep 20 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt15
- up build

* Tue Sep 20 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt14.4
- UTCPStream: check POCO_INVALID_SOCKET

* Mon Sep 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt14.3
- UTCPStream: shudown and close (for disconnect)

* Mon Sep 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt14.2
- (ModbusTCPMaster): added disconnect() function

* Mon Sep 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt14.1
- (ModbusTCPMaster): added catch exceptions

* Mon Sep 12 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt14
- up build

* Sun Sep 11 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt13.1
- (ModbusTCPMster): refactoring
- (optimization): added the use of the qualifier 'noexcept'

* Fri Sep 09 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt13
- minor fixes in millisecToPoco() and microsecToPoco() functions

* Thu Sep 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt12
- up build

* Thu Sep 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt11
- DebugStream: added support format: level1,level2,-level3
  for set or delete debug levels.
- add support old version of libpoco (version < 1.7.4)

* Wed Sep 07 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt10
- fixed bug in millisecToPoco() function

* Tue Sep 06 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt9
- (UNetUDP): optimization use mutex
- (unet-udp-tester): add new command line agruments
- (IONotifyController): optimization use setLocalValue(), minor fixes
- (MBTCPMaster): fixed bugs in error logs and minor fixes
- (SMViewer): added display supplier
- other minor fixes and optimizations

* Fri Sep 02 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt8
- add -D_GLIBCXX_USE_NANOSLEEP for old gcc version (<5.0)

* Fri Sep 02 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt7
- usleep --> std::this_thread::sleep_for(..);
- clean up #include ...

* Thu Sep 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt6
- (python): add getObjectID() for python UInterface

* Thu Sep 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt5
- up build

* Mon Aug 29 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt4
- (python): add supplier ID for setValue function

* Fri Aug 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt3
- update requires

* Fri Aug 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt2
- Fixed converting timeout_t to Poco::TimeSpan

* Thu Aug 25 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt1.2
- (UNetUDP): add debug information (getInfo)
- minor fixes

* Wed Aug 24 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt1.1
- codegen: make readonly in-variables

* Wed Aug 24 2016 Pavel Vainerman <pv@altlinux.ru> 2.5-alt1
- test build with libpoco

* Sun Aug 21 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt9
- build new version

* Sun Aug 21 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt8.2
- IONotifyController: add debug information (getInfo)

* Sat Aug 20 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt8.1
- miscoseconds --> nanoseconds
- optimization
- fixed bug in ModbusTCPMaster

* Fri Aug 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt8
- ModbusTCPCore: minor optimization

* Fri Aug 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt7
- minor fixes

* Fri Aug 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt6.1
- test build

* Tue Aug 09 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt6
- build new version (optimization, refactoring)

* Mon Aug 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt5.1
- test build

* Wed Aug 03 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt5
- build new version

* Mon Aug 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt4
- build new version

* Thu Jul 28 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt3.1
- test build

* Tue Jul 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt3
- merge devel/master

* Tue Jul 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt2
- minor fixes

* Mon Jul 25 2016 Pavel Vainerman <pv@altlinux.ru> 2.4-alt1
- build new version

* Sun Jul 24 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt10
- up build

* Fri Jul 22 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt9.1
- test build

* Wed Jun 29 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt9
- build new version

* Wed Jun 29 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt8
- DBServer_PGSQL: added support for the insert buffer

* Fri Jun 03 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt7
- codegen: fixed bug in updateOutput
- revert commit: "added several attempts to save the value"

* Fri May 27 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt6
- codegen: added several attempts to save the value

* Wed May 11 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt5
- fixes after coverity_scan

* Thu Apr 28 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt4
- build new version

* Thu Apr 28 2016 Pavel Vainerman <pv@etersoft.ru> 2.3-alt3.1
- (ModbusTCPCore): test build

* Wed Apr 27 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt3
- fixed build for 64-bit

* Wed Apr 20 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt2
- (LogSession): disable "keep alive message"

* Tue Apr 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt1
- build new version

* Sun Apr 17 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt31.7
- LogSession: auto restore log levels after all sesssions closed

* Mon Apr 11 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt31.6
- LogSession: added the connection test

* Sun Apr 10 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt31.5
- LogSession: add buffer limit.. (200 messages, ~30kB)

* Sun Apr 03 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt31.3
- ModbusSlave: iowait optimization

* Thu Mar 31 2016 Pavel Vainerman <pv@etersoft.ru> 2.2-alt31.2
- test build

* Tue Mar 29 2016 Pavel Vainerman <pv@etersoft.ru> 2.2-alt31.1
- test build

* Wed Mar 23 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt31
- IONotifyContoller: fixed bug in depend (notify)(setbug #9302)
- ModbusMultiMaster: fixed bug for change channel (timeout)

* Tue Mar 22 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt30
- minor fixes in DealyTimer and MBExchange (not respond logic)

* Sun Mar 20 2016 Pavel Vainerman <pv@etersoft.ru> 2.2-alt29.2
- rebuild

* Sun Mar 20 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt29.1
- test build

* Sat Mar 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt28.4
- test build

* Sat Mar 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt28.3
- test build

* Sat Mar 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt28.2
- test build

* Fri Mar 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt28.1
- test build

* Mon Mar 07 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt29
- minor fixes

* Sun Feb 21 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt28
- build with MQTTPublisher
- default mqtt extention disabled

* Sat Feb 20 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt27
- (ModbusTCP): add forceDisconnect() func for tcp connection

* Fri Feb 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt26
- (codegen): revert waitSM logic..

* Fri Feb 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt25
- (codegen): fixed bug (waitReady --> waitWorking)

* Thu Feb 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt24
- modbustcpserver-echo: fixed bug for options
- ModbusTCPMultiMaster: add new logs,
   add ignore option for GateList, modify change channel logic

* Wed Feb 17 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt23
- IONotifyController: fixed buf for init thresholdslist

* Tue Feb 09 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt22
- ModbusSlave(TCP): add show ip:port to vmonit setbug #9012

* Sat Feb 06 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt21
- RRDServer: fixed bug in write sequence to rrd base

* Sat Feb 06 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt20
- RRDServer: fixed bug for long name processing..

* Mon Jan 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt19
- rebuild new version

* Mon Jan 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt17.2.3.alt1
- add supported libev:
  - refactoring ModbusSlave (use libev)
  - refactoring LogServer (use libev)
  - refactoring UNetReceiver (use libev)
- minor fixes

* Fri Jan 15 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt17
- rebuild new version

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt13.1
- NMU: rebuild with libpqxx 4

* Wed Dec 23 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt16
- fixed bug in DBNetInterface (uzum)

* Sat Dec 19 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt15
- (codegen): added to display information about the timers

* Sat Dec 19 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt14
- (uzum): refactoring DBInterface..

* Wed Dec 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt13
- set public for UniSetObject::askTimer 

* Mon Dec 14 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt12
- refactoring: remove xxx_LT classes
- add new function for LT_Object
- add userparam for UniSetObject::getInfo( int userparam)
- codegen: add function: long* valptr(ObjectId) and --gen-vmap parameter

* Tue Nov 03 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt11
- RRDServer: add support 'dsname', check RRD_MAX_DSNAME_LEN

* Fri Oct 30 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt10
- fixes after coverity scan..
- minor fixes
- use char* --> std::string

* Wed Oct 14 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt9
- new release

* Wed Oct 14 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt8.1
- (VMonit): sort output 

* Thu Oct 08 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt8
- (uniset-codegen): minor fixes in resetMsg()  mechanism

* Mon Oct 05 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt7
- (ModbusServer): rename receive(ModbusAddress addr..) --> receive_one(ModbusAddress addr..)

* Mon Oct 05 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt6
- (ModbusServer): add helper function addr2vaddr()

* Fri Oct 02 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt5
- (ModbusSlave): added support for multiple addresses for MBSlave

* Fri Oct 02 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt4
- (ModbusSlave): added support setBroadcastMode() // addr = 255
- (codegen): change log for 'unknown message id' crit --> level8

* Mon Sep 21 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt3
- (ModbusMaster): modify check "not respond" mechanism

* Sun Sep 20 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt2
- minor fixes after 'cppcheck'

* Thu Sep 17 2015 Pavel Vainerman <pv@altlinux.ru> 2.2-alt1
- new UNetUDP: support 'sendfactor'

* Mon Sep 14 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt25
- (PassiveTimer): fixed bug in default init
- (Pulse): refactoring

* Thu Sep 10 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt24
- (LogServer): refactoring (more use shared_ptr)

* Mon Sep 07 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt23
- (ModbusPersistentSlave): fixed bug in end connection processing
- (uniset-log): fixed bug in end connection processing

* Sun Sep 06 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt22
- refactoring (use shared_ptr), change pollfactor realisation..

* Sat Sep 05 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt21
- (modbus slave): add more logs.. 

* Sat Aug 29 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt20
- (ModbusSession): add setKeepAliveParams()

* Sat Aug 29 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt19
- (ModbusSlave): rename ModbusMultiSlave --> ModbusPersistentSlave, minor fixes

* Thu Aug 27 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt18
- (ModbusExchange):  add reinit_timeout timer..

* Fri Aug 21 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt17
- up build

* Fri Aug 21 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt16.2
- (ModbusTCP): fixed bug in update respond sensor in SharedMemory

* Thu Aug 20 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt16.1
- (ModbusTCP): add more vmonit parameters

* Thu Aug 20 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt16
- (modbustcptest): add 'check' for connection

* Tue Aug 18 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt15.3
- minor build

* Fri Aug 14 2015 Pavel Vainerman <pv@etersoft.ru> 2.1-alt15.2
- up build

* Thu Aug 13 2015 Pavel Vainerman <pv@etersoft.ru> 2.1-alt15.1
- test build for new UNetUDP

* Wed Aug 12 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt15
- (Modbus): add new property "pollfactor" (see docs)

* Sun Aug 09 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt14
- (UTCPStream): add new function "setKeepAliveParams"

* Sat Aug 08 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt13
- (ModbusMultiMaster): minor fixes (add "force" for <GateList>)

* Sat Aug 08 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt12
- (Modbus): minor fixes in ModbusMultiMaster

* Tue Jul 21 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt11
- minor fixes in uniset2-codegen
- ModbusMaster: add --prefix-query-max-count val - the maximum 
  number of requested registers in one query

* Fri Jul 03 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt10
- fixed bug in ModbusMultiMaster (setbug #7596)
- enable pgsql interface

* Tue Jun 30 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt9
- temporary disable pgsql interface

* Sun Jun 28 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt8.1
- VMonitor: added output information in the form of two columns

* Sat Jun 20 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt8
- release

* Fri Jun 19 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.8
- SQLxxxInterface: minor fixes (refactoring)
- ModbusMaster: force set value for DI,DO --> [1,0]

* Tue Jun 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.7
- fixed minor bug in uniset2-admin --oinfo (uniset2-vmonitor)
- vmonitor: add helper functions

* Wed Jun 10 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.6
- fixed libUniSet2Extensions.pc

* Tue Jun 09 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.5
- minor fixes
- VMonitor: add new helper functions pretty_str(..)
- uniset-vmonit: add -d - dump state

* Mon Jun 08 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.4
- (codegen): add no_vmonit="1" flag for <variables>

* Sun Jun 07 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.3
- (vmonitor): added support vmonitor for standart components
(SharedMemory,ModbusSlave,ModbusMaster,UNetUDP)

* Sun Jun 07 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.2
- (codegen): add user info function (getMonitInfo())

* Sat Jun 06 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7.1
- (vmonit): new utilities (variables monitor)

* Fri Jun 05 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt7
- (ModbusSlave): fixed bug in read0x function (for float and precision)

* Thu Jun 04 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt6
- (smonit): print supplier, change print format 
- (admin): add getChangedTime function
- (codegen): reuse getInfo() function (internal variables monitor)

* Tue Jun 02 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt5
- (LogServer): refactoring

* Mon Jun 01 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt4
- (LogServer): added suppport "filter mode"
- (LogAgregator): refactoring, change show loglist format

* Sun May 31 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt3
- (LogAgregator):
  - added support agregator hierarchy
  - add docs
  - add new tests

* Sat May 30 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt2
- (optimization): TransportMessage change format
- (uniset-codegen): minor fixes
- (SharedMemory): add new tests
- (LogServer): add regexp support for logname

* Thu May 28 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-alt1
- repack header files..

* Tue May 26 2015 Pavel Vainerman <pv@etersoft.ru> 2.0-alt35.1
- PassiveTimer: uset chrono
- LogServer: add --list function
- minor fixes

* Sun May 24 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt35
- added support LogServer for: 
   SharedMemory,RRDServer,MBTCPMaster,MBSlave,UNetExchange,IOControl,
   codegen,DBServer_xxx

* Wed May 20 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt34.4
- (ModbusSlave): fixed bug in much_real_write (again) (thank`s hd@nio14)
- (DelayTimer): fixed critical bug in logic (thank`s ilyap@etersoft.ru)

* Tue May 19 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt34.3
- (ModbusSlave): add 'optimize write function mechanism' (and --prefix-no-mbfunc-optimization 0,1)

* Mon May 18 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt34.2
- (ModbusSlave): fixed bug in much_real_write (mbfunc=0x10 processing)

* Mon May 18 2015 Pavel Vainerman <pv@etersoft.ru> 2.0-alt34.1
- (ModbusSlave): fixed bug in readOutputRegisters

* Mon May 18 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt34
- (ModbusMaster): fixed bug in 'set respond senror mechanism'
- (ModbusMaster): refactoring
- make style
- minor fixes

* Fri May 15 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt33
- (ModbusSlave): added support mbfunc.. (use RegID)

* Wed May 13 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt32
- sync from 1.x/master: ModbusMaster: fixed bug: unstable timeout...(thank`s ilyap@etersoft.ru)
- make style

* Mon May 11 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt31
- Calibrations: fixed bug
- LogSession: fixed bug
- PQSQL: minor fixes, update requires
- make style

* Fri May 08 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt30
- ModbusSlave: added support nbit='' for 0x06 and 0x10 function (setbug #7337)

* Tue May 05 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt29
- SM: add reserv mechanism for initializing (setbug #7289)
- SM: fixed bug in 'heartbeat'
- SM: add tests
- minor fixes
- refactoring
- add new tests

* Thu Apr 23 2015 Pavel Vainerman <pv@etersoft.ru> 2.0-alt28.2
- unet-udp: special build... change maximum for digital and analog data. Set A=1500, D=5000.

* Thu Apr 23 2015 Pavel Vainerman <pv@etersoft.ru> 2.0-alt28.1
- unet-udp: special build... change maximum for digital and analog data. Set A=800, D=5000.

* Mon Apr 20 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt28
- optimization: use std::unordered_map instead of std::map

* Thu Apr 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt27
- (UniXML): refactoring UniXML::iterator::find..

* Thu Apr 09 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt26
- (ModbusSlave): added support nbit
- (ModbusSlave): added support 0x01 (readCoilStatus) function
- (ModbusSlave): minor fixes

* Tue Apr 07 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt25
- fixed bug in 'MBSlave' (thank`s Alexandr Hanadeev)
- add --xxx-set-prop-prefix for MBSlave 

* Sat Apr 04 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt24.1
- test pgsql extension build

* Thu Apr 02 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt24
- codegen: modify interface for messages (setMsg())
- remove alarm() function (deprecated)

* Thu Mar 19 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt23
- unetudp: fxied critial bug in "switching channels" (thank`s Alexey Surov)

* Mon Mar 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt22
- codegen: add dumpIO(), str(), strval() functions (debug helpers)

* Thu Mar 12 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt21
- codegen: adjustment documentation
- unetudp: add tests, minor optimization (thank`s Alexey Vinogradov)

* Fri Mar 06 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt20
- (modbustcpmaster): minor fixes in error messages

* Fri Mar 06 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt19
- codegen: fixed bug (in previous commit)
- codegen: fixed warning (redefined mylog macroses)

* Sat Feb 28 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt18
- codegen: set default argprefix=myname (object name)
- codegen: fixed minor bug in mylog..
- refactoring IORFile interface
- (modbusmaster): fixed bug (setbug #5583) in initialization..

* Sat Feb 21 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt17
- use omni_options[] argument for ORB_init().
- minor fixes

* Fri Feb 06 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt16
- add <omniORB> section to configure.xml (for use in the ORB_init())

* Sun Feb 01 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt15
- fixed minor bug in uniset2-smonit utility
- minor fixes
- (minor) refactoring try/catch exceptions

* Mon Jan 26 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt14
- change LogServer,LogSession,LogReader interfaces

* Fri Jan 23 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt13
- refactoring ulog and dlog: Objects converted to shared_ptr<DebugStream>
  for subsequent use LogAgregator.
- modify interface for LogReader,LogSession,LogServer

* Fri Jan 23 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt12
- refactoring LogAgregator,LogServer,LogSesson --> use shared_ptr
- fixed bug in MBExchange (read prop_prefix)
- mbtcpserver-echo:  rename command line parameter: --ignore-addr ==> --reply-all 

* Sat Jan 17 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-alt11
- refactoring "exit process"
- fixed bug in specfile: --enable-doc --> --enable-docs
- transition to use shared_ptr wherever possible

* Sat Dec 20 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt10.1
- added PostgreSQL support

* Mon Nov 24 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt10
- use shared_ptr 

* Mon Oct 20 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt9
- fixed bug in UniXML::iterator getPIntProp() for prop<=0

* Wed Oct 08 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt8
- added unit-tests (use "catch" test unit framework)
- added use autoconf testsuite 

* Wed Oct 01 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt7
- make "extension-smplus" package
- make "extension-logicproc" package

* Thu Aug 21 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt6
- make "extension-common" package
- make "extension-rrd" package
- make "extension-mysql" package
- make "extension-sqlite" package
- make "extension-io" package

* Wed Aug 20 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt5
- (iobase): rename 'jar' ==> 'debounce'
- fixed bug (setbug# 6219) in DBServer_MySQL (SIGSEGV)

* Tue Jun 10 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt4
- minor fixes..

* Sat Feb 22 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt3
- use std::move

* Thu Feb 20 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt2
- rename 'disactivate' --> 'deactivate'

* Wed Feb 19 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt1
- add ModbusMultiSlave (multithreaded modbus slave server)

* Tue Feb 04 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.9
- use -std=c++0x (auto, for( auto..), etc)

* Mon Feb 03 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.8
- fixed bug in LT_Object

* Sun Feb 02 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.7
- refactoring DBInterface (rename to MySQLInterface, add MySQLResult class,..)

* Sun Feb 02 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.6
- add thresholds processing for ModbusMaster (TCP and RTU)
- minor fixes

* Fri Jan 31 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.5
- minor fixes
- test build

* Fri Jan 31 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.4
- rename uniset --> uniset2

* Thu Jan 30 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.3
- optimization: avoiding the use of 'alias mechanism'
  ('objectid@virtualnode:realnode' ==> 'objectid')
- add ObjectActivator::Instance function (singlton pattern)
- minor fixes

* Fri Jan 24 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.2
- oprimization processing message (warning: use reinterpret_cast<> )

* Tue Dec 24 2013 Pavel Vainerman <pv@altlinux.ru> 2.0-alt0.1
- rename "IOTypes" --> "IOType"
- rename DigitalInput --> DI
- rename DigitalOutput --> DO
- rename AnalogInput --> AI
- rename AnalogOutput --> AO
- remove deprecated services: InfoServer,TimeService,SystemGuard
- remove deprecated intefaces: MessageInterface
- remove deprecated messages: AlarmMessage, InfoMessage, DBMessage
- remove 'state' from SensorMessage
- remove deprecated function setState,getState,askState
  use simple function: setValue,getValue,askSensor
- possible use of the property 'iotype' in uniset-codegen
- refactoring <depends> mechanism
- add iofront=[01,10] to IOBase
- remove deprecated interfaces (Storages,CycleStorage,TableStorage,TextIndex,..)
- rename unideb --> ulog
- DebugStream refactoring (add new function, add syntax sugar for ulog, dlog /dcrit,dwarn,dlog1,ulog1,ucrit,.../)
- UniversalInterface --> UInterface
- ObjectsManager --> UniSetManager
- ObjectsActitvator --> UniSetActivator
- remove deprecated property: "sensebility"
- rename property "inverse" --> "threshold_invert"

* Tue Dec 10 2013 Pavel Vainerman <pv@altlinux.ru> 1.7-alt3
- add RRDServer

* Fri Dec 06 2013 Pavel Vainerman <pv@altlinux.ru> 1.7-alt2
- (unetexchange): add 'prefix'

* Wed Dec 04 2013 Pavel Vainerman <pv@altlinux.ru> 1.7-alt1
- (modbus): add ModbusMultiChannel

* Fri Nov 29 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt17
- (uniset-codegen): move 'arg-prefix' from <variables> to <settings>

* Tue Nov 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt16
- (uniset-codegen): add 'loglevel' parameters for src.xml

* Mon Oct 28 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt15
- (python): fixed bug in UInterface

* Sat Oct 26 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt14
- (python): fixed bug in UInterface

* Thu Oct 24 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt13
- (python): add getArgParam, getArgInt and checkArg functions for UGlobal.py

* Thu Sep 19 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt12
- (Modbus): Added ability to set the sensor mode (modeSensor) for each device
- fixed bug in MTR types: T_Str16 and T_Str8 (tnx ilyap)
- fixed bug in MTR::send_param

* Thu Jun 13 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt11
- fixed after cppcheck checking

* Wed Jun 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt10
- add for ModbusMaster (RTU|TCP) --xxx--aftersend-pause

* Tue May 14 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt9
- add for Modbus (RTU|TCP) exchange  --xxx-reopen-timeout msec. (eterbug #9296)

* Wed May 08 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt8
- fixed minor bug in uniset-codegen (getValue)

* Wed Mar 20 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt7
- modbus: add new function 0x2B/0x0E(43/14)"Read device identification"

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt6
- python: add __init__.py

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt5
- force add python provides

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt4
- restote UInterface for python

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt3
- add doc for python bindings
- rebuild wrapper files with new swig

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt2
- fixed build for x86_64

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt1
- python: final build

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt0.5
- python: test build

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt0.4
- python: test build

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt0.3
- python: test build

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt0.2
- python: test build

* Mon Mar 04 2013 Pavel Vainerman <pv@altlinux.ru> 1.6-alt0.1
- add python interface

* Mon Jan 14 2013 Pavel Vainerman <pv@altlinux.ru> 1.5-alt10
- add error code for MTR (eterbug #8659)
- (uniset-codegen): add generate class Skeleton (--make-skel)

* Sat Jan 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.5-alt9
- add SQLite support

* Mon Dec 03 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt8
- add uniset-smemory-plus

* Fri Nov 30 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt7
- returned file 'SandClock.h' back and declared it obsolete

* Thu Nov 29 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt6
- add DelayTimer class
- rename SandClock --> HourGlass

* Fri Nov 23 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt5
- (Calibration): add getLeftRaw(),getRightRaw(),getLeftVal(),getRightVal()
- (Calibration): fixed bugs

* Fri Nov 23 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt4
- (uniset-codegen): fixed minor bug

* Thu Nov 22 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt3
- (Calibration): add getMinRaw(),getMaxRaw(),getMinVal(),getMaxVal()

* Wed Nov 21 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt2
- new ConfirmMessage format (eterbug #8842)

* Tue Nov 06 2012 Pavel Vainerman <pv@altlinux.ru> 1.5-alt1
- add depends for IOBase

* Tue Sep 04 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt11
- minor fixes (IOControl::getState, isExist)

* Wed Aug 29 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt10
- (UDPNet): increase the resolution of the sensors over the network (600 analog, 600 digital)

* Mon Aug 20 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt9
- fixed bug in previous commit (bug in UniXML::iterator::find)

* Tue Aug 07 2012 Pavel Vaynerman <pv@server> 1.4-alt8
- fixed bug in UniXML::iterator::find

* Wed Jul 25 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt7
- (codegen): added support type 'long'
- add setThreadPriority(..) for UniSetObject

* Tue Jul 10 2012 Pavel Vaynerman <pv@server> 1.4-alt6
- (unetudp): fixed bug in the logic of switching channels

* Thu Jun 14 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt5
- (codegen): fixed bug in validation 'iotype'

* Sun Jun 10 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt4
- (codegen): added validation 'iotype'

* Sun Jun 10 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt3
- (DBServer_MySQL): buffer is added to query

* Fri Jun 08 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt2
- added support type 'double' for uniset-codegen (<variables>)

* Thu May 31 2012 Pavel Vainerman <pv@altlinux.ru> 1.4-alt1
- rename unet2 -->unetudp
- release version 1.4

* Thu May 31 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt19
- DBServer: set log info level - LEVEL9
- minor fixies for linker errors (new gcc)

* Tue Apr 10 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt18
- fixed bug in ComPort485F (reinit function)

* Fri Mar 16 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt17
- rebuild

* Fri Mar 16 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt16
- (unet2): fixed bug in respond sensors (again)

* Thu Mar 15 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt15
- (unet2): fixed bug in respond sensors

* Thu Mar 15 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt14
- (unet2): add 'unet_respond_invert' parameter

* Sun Mar 11 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt13
- minor fixes in uniset-codegen (add "preAskSensors")

* Fri Mar 02 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt12
- fixed bug in DigitalFilter
- fixed bug in RTU188 exchange

* Tue Feb 28 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt11
- (iocontrol): fixed bug in configuring UNIO96

* Fri Feb 24 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt10
- (modbus): realized exchange with RTU188

* Wed Feb 22 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt9
- (modbus): fixed bug in modbus exchange for RTU188 (initialization)

* Tue Feb 21 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt8
- (modbus): fixed bug in modbus exchange for RTU188

* Sat Feb 18 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt7
- changed implementation SharedMemory::History (optimization)

* Fri Feb 17 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt6
- (io): corrected a mistake in configuring analog I/O

* Fri Feb 10 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt5
- (IOControl): Added support for setting boards such as 'Grayhill'
- (Modbus): Fixed minor bug in configuration with RTU188

* Fri Feb 03 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt4
- add commmon (respond and lostpackets) sensors for UNet2

* Tue Jan 31 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt3
- minor fixes in simitator

* Tue Jan 24 2012 Pavel Vainerman <pv@altlinux.ru> 1.3-alt2.1
- rebuild

* Mon Dec 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.3-alt2
- fixed buf in Configuration

* Mon Dec 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.3-alt1
- Added support for multiple profiles(Configuration) simultaneously

* Fri Dec 23 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt62
- fixed bug in UniversalInterface

* Fri Dec 23 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt61
- minor fixes in LogicProcessor

* Wed Dec 21 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt60
- fixed bug in LogicProcessor

* Mon Dec 19 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt59
- add precision for output variables

* Wed Nov 30 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt58
- fixed bug in ModbusSlave::readInputStatus(0x02)

* Sun Nov 27 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt57
- add uniset-mtr-read utility

* Sat Nov 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt56
- (modbus): fixed bug (again) in ModbusSlave::readInputStatus(0x02)

* Sat Nov 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt55
- (modbus): fixed bug in ModbusSlave::readInputStatus(0x02)

* Fri Nov 25 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt54
- (modbus): added 'const-reply' for modbustcptester

* Thu Nov 24 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt53
- (modbus): added information log

* Wed Nov 16 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt52
- (modbus): An opportunity to change the prefix is added to the properties

* Wed Nov 02 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt51
- (unet2): added reserv channel exchange

* Mon Oct 31 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt50
- ModbusMaster extensions code refactoring

* Tue Oct 25 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt49
- added support 'const' and [private|protecte|public]
for <variables> in uniset-codegen

* Sat Oct 22 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt48
- added support for list of variables (<variables>) in uniset-codegen

* Tue Oct 11 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt47
- new build

* Sat Oct 08 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt46
- add reopen() for ComPort

* Tue Oct 04 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt45
- dependence on mandatory disabled launching a local omninames service

* Mon Oct 03 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt44
- add nodes filter for UNet2
- minor optimization

* Thu Jul 14 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt42
- fixed bug in uniset-codegen

* Sun Jun 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt41
- fixed bug in ComediControl::cinfugureSubdev
- and other minor fixes

* Thu Jun 09 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt38
- fied bug in ComPort::cleanupChannel()

* Sun Jun 05 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt37
- add cleanup before send for ComPort

* Tue May 24 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt36
- add 'node' param processing for uniset-codegen

* Fri May 20 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt35
- minor fixed in UniXML::getProp()

* Thu May 19 2011 Pavel Vainerman <pv@etersoft.ru> 1.0-alt34
- fixed bug in IOControl

* Thu May 19 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt33
- fixed bug in DBInterface::ping (again). Many thanks uzum

* Thu May 19 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt32
- fixed bug in DBInterface::nextRow function
- fixed bug in DBInterface::ping

* Fri May 13 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt31
- move DBServer-MySQL to extensions directory
- add pc-file for libUniSet-mysql
- create new devel package - "libuniset-mysql-devel"
- minor fixes

* Wed May 11 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt30
- add new function to UniversalInterface

* Sat May 07 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt29
- (unet2): new protocol implementation

* Thu May 05 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt28
- add setup function for ModbusTCPMaster and ModbusTCPServer

* Wed May 04 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt27
- fixed bug in ModbusTCPMaster and ModbusTCPServer

* Wed May 04 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt26
- minor fixes

* Wed May 04 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt25
- (unet2): minor fixes

* Sun May 01 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt24
- build for new uniset-unet2 version

* Sun May 01 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt23
- (uniset-unet2): fixed bug (SEGFAULT with a large number of items)

* Wed Apr 20 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt22
- (uniset-unet2-tester): fixed minor bugs

* Wed Apr 20 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt21
- (uniset-unet2-tester): add new parameter
   -l | --check-lost   - Check the lost packets.

* Wed Apr 20 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt20
- (uniset-unet2-tester): rename command line parameters

* Tue Apr 19 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt19
- a little cleaning

* Tue Apr 19 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt18
- add unet2-tester

* Tue Mar 29 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt17
- set encoding="utf-8" for codegen templates

* Tue Mar 29 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt16
- fixed minor bug in codegen

* Sat Mar 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt15
- fixed return value in some utilities

* Thu Mar 24 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt14
- fixed bug in MBSlave

* Thu Mar 24 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt13
- rename some utilities (mtr-xxx --> uniset-mtr-xxx, vtconv --> uniset-vtconv)

* Wed Mar 23 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt12
- fixed bug in TableBlockStorage interface

* Thu Mar 17 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt11
- fixed bug in MBTCPMaster (query optimization)

* Sun Mar 13 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt10
- fixed bug in uniset-codegen (again)

* Sun Mar 13 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt9
- fixed bug in uniset-codegen

* Fri Mar 11 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt8
- fixed bug in conf->getArgPInt function (new libUniSet revision)

* Wed Mar 02 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt7
- add UNet2 to extensions

* Tue Mar 01 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt6
- MBTCPMaster new version (fixed any bugs)

* Thu Feb 24 2011 Pavel Vainerman <pv@server> 1.0-alt5
- new build (optimization local timers)

* Thu Feb 24 2011 Pavel Vainerman <pv@server> 1.0-alt4
- new build

* Mon Feb 14 2011 Pavel Vainerman <pv@server> 1.0-alt3
- fixed bug in ModbusTCPMaster

* Mon Feb 14 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt2
- minor fixes
- new version ModbusTCPMaster

* Wed Feb 09 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1
- fixed bug in VERSION (bad pc-files)

* Wed Jan 26 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.1
- pre-release build

* Sat Jan 22 2011 Pavel Vainerman <pv@altlinux.ru> 0.99-alt30
- add "prefix" for IOControl

* Fri Jan 14 2011 Ilya Shpigor <elly@altlinux.org> 0.99-alt27
- initial build for ALT Linux Sisyphus

* Fri Jan 14 2011 Pavel Vainerman <pv@etersoft.ru> 0.99-eter26
- fixed bug in ModbusTCP Master. Set default signed type for data

* Sat Dec 04 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter25
- fixed bug in uniset-mbtcptest (writexx)
- minor fixes ( add 'm'-parametes for set value < 0 )

* Tue Nov 30 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter24
- ModbusRTU::mbException: public Exception

* Mon Nov 29 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter23
- fixed bug in Modbus<-->SM (signed and unsigned value)

* Mon Nov 29 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter22
- smonitor new format (id@node)

* Tue Nov 23 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter20
- new build

* Tue Nov 16 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter17
- fixed bug in MBSlave

* Mon Nov 15 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter16
- Modbus: add test for query count

* Mon Nov 15 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter15
- new build

* Fri Nov 12 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter14
- new build

* Thu Nov 11 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter13
- uniset-admin refactor. ( [get|set]Value, call remote sensors)

* Mon Nov 08 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter12
- fixed minor bug in uniset-codegen

* Mon Oct 18 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter9
- new build

* Wed Oct 13 2010 Ilya Shpigor <elly@altlinux.org> 0.99-eter8
- fix bug in ModbusTCPServer
- add gateway imitation to uniset-mbtcpserver-echo

* Sat Oct 09 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter7
- fixed bug in MBTCPMaster

* Sun Oct 03 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter6
- test codegen build

* Tue Sep 28 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter5
- MBSlave (RTU|TCP) optimization

* Mon Sep 20 2010 Ilya Shpigor <elly@altlinux.org> 0.99-eter4
- new build 0.99-eter4

* Fri Sep 17 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter3
- add new value types (I2,U2) in to MBTCPMaster

* Fri Sep 17 2010 Pavel Vainerman <pv@etersoft.ru> 0.99-eter2
- build for new MBSlave

* Tue Sep 14 2010 Pavel Vainerman <pv@altlinux.ru> 0.99-eter1
- test UDP build

* Tue Sep 07 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.98-eter9
- Build for Sisyphus Etersoft addon:
  commit fc7fb2eefaf900088d7e6583df440c914aeb9560

* Wed Aug 25 2010 Pavel Vainerman <pv@server> 0.98-eter8
- fixed bug for install IDL-files

* Wed Aug 11 2010 Pavel Vainerman <pv@altlinux.ru> 0.98-eter7
- add new types for MTR
- minor fixes in SharedMemory::HistoryInfo (add timestamp)

* Fri Jul 30 2010 Ilya Shpigor <elly@altlinux.org> 0.98-eter6
- add MTR support
- add db_ignore parameter for DBServer

* Tue Jul 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.98-eter4
- iterator for CycleStorage
- some fixes for CycleStorage iterator

* Wed Jun 16 2010 Ivan Donchevskiy <yv@etersoft.ru> 0.98-eter3
- new build

* Tue Jun 01 2010 Vitaly Lipatov <lav@altlinux.ru> 0.98-eter2
- fixed bug in uniset-codegen
- minor fixes in SM (add virtual function)
- fixed bug in SandClock interface
- fixed bug in ModbuRTU::autedetect slave adress function
- minor fixes in MTR setup API
- add MTR setup (API and utility)

* Wed Mar 03 2010 Ilya Shpigor <elly@altlinux.org> 0.98-eter1
- new build for Sisyphus with utf8 support

* Sat Feb 13 2010 Pavel Vainerman <pv@altlinux.ru> 0.97-eter54
- fixed bug in codegen

* Thu Feb 04 2010 Pavel Vainerman <pv@altlinux.ru> 0.97-eter53
- new build

* Tue Feb 02 2010 Larik Ishkulov <gentro@etersoft.ru> 0.97-eter52
- new build

* Fri Jan 29 2010 Pavel Vainerman <pv@altlinux.ru> 0.97-eter50
- add simitator

* Tue Jan 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.97-eter49
- fixed bug in ModbusTCPMaster

* Mon Dec 28 2009 Alexander Morozov <amorozov@etersoft.ru> 0.97-eter48
- added new filters
- fixed some bugs

* Thu Dec 03 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter46
- fixed bug in MBTCPMaster

* Wed Dec 02 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter45
- new build (for builder50)
* Mon Nov 23 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter44
- exclude SMDBServer

* Thu Nov 19 2009 Larik Ishkulov <gentro@etersoft.ru> 0.97-eter37
- new build

* Wed Nov 18 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter36
- new build

* Mon Nov 16 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter35
- fixed bug in uniset-mysql-dbserver

* Thu Nov 12 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter34
- new build

* Tue Oct 27 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter33
- fixed bug (int previous build) in SM
- fixed bug in uniset-stop.sh

* Tue Oct 27 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter32
- new build

* Sat Oct 24 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter31
- new build

* Wed Oct 21 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter30
- new build

* Sun Oct 18 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter29
- new build

* Fri Oct 09 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter28
- minor optimization

* Mon Oct 05 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter27
- new build

* Sun Oct 04 2009 Vitaly Lipatov <lav@altlinux.ru> 0.97-eter26
- new build

* Thu Oct 01 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter25
- return old mutex

* Thu Oct 01 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter24
- new mutex

* Wed Sep 30 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter23
- control (on/off) new ComPort

* Wed Sep 30 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter22
- new build

* Tue Sep 29 2009 Vitaly Lipatov <lav@altlinux.ru> 0.97-eter21
- new build

* Tue Sep 29 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter20
- new vtypes for Modbus

* Mon Sep 28 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter19
- new comport

* Mon Sep 28 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter18
- restore mutex

* Mon Sep 28 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter17
- new mbtcpmaster

* Mon Sep 28 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter16
- new mutex

* Sat Sep 26 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter15
- new build

* Sat Sep 26 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter14
- add default heartbeat time to Configuration

* Sat Sep 26 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter13
- add heartbeat logic to uniset-codegen

* Sat Sep 26 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter12
- minor fixes in IONotifyController

* Fri Sep 25 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter11
- return old mutex

* Wed Sep 23 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter10
- new build

* Wed Sep 23 2009 Pavel Vainerman <pv@altlinux.ru> 0.97-eter9
- new mutex

* Tue Sep 22 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter8
- new build

* Tue Sep 22 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter7
- new build

* Tue Sep 22 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter6
- new build

* Tue Sep 22 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter5
- minor fixes in SM

* Tue Sep 22 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter4
- minor fixes in IOBase

* Tue Sep 22 2009 Pavel Vainerman <pv@etersoft.ru> 0.97-eter3
- fixed bugs in IOControl

* Sat Sep 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.97-eter2
- fix build

* Wed Sep 16 2009 Vitaly Lipatov <lav@altlinux.ru> 0.97-eter1
- add getProp and getInt into generated _SK class for use default cnode
- UniXML: make xml2local, local2xml protected
- UniXML: add getContent for iterator (via xmlNodeGetContent)
- use logFile with string, without c_str
- UniXML: add getPropUtf8, findNodeUtf8, extFindNodeUtf8
- UniSetTypes: add getArgInt, getArgPInt
- forbid direct use atoi function in uniset and uniset related projects
- add string support for getIdByName
- use appropriate getArg(P)Int, get(P)IntProp instead direct atoi using
- Configuration: add getPIntField, getIntProp, getPIntProp, getArgPint
- Added byte size check in CycleStorage and TableBlockStorage
- add uniset-network (new component - UniNetwork)
- add new interface: getSensors()
- add new realization MBTCPMaster
- introduce getPintProp for get positive only values (returns def if the value zero or negative). Note: def may be negative if needed.

* Tue Sep 15 2009 Pavel Vainerman <pv@etersoft.ru> 0.96-eter63
- new build

* Mon Sep 07 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter54
- rebuild for new ModbusType parameters

* Mon Sep 07 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter53
- rebuild for new MBTCPMaster

* Sun Sep 06 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter52
- minor fixes in MBTCPMAster

* Fri Aug 21 2009 Pavel Vainerman <pv@etersoft.ru> 0.96-eter51
- minor fixes in RTUExchange

* Wed Aug 19 2009 Pavel Vainerman <pv@etersoft.ru> 0.96-eter50
- fixed bug in IOControl (blink mechanic)

* Wed Aug 19 2009 Pavel Vainerman <pv@etersoft.ru> 0.96-eter49
- add BLINK2, BLINK3 to IOControl

* Tue Aug 18 2009 Pavel Vainerman <pv@etersoft.ru> 0.96-eter48
- fixed bug in PassiveTimer

* Wed Aug 05 2009 Vitaly Lipatov <lav@altlinux.ru> 0.96-eter37
- fixed smp build

* Mon Aug 03 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter36
- new build

* Mon Aug 03 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter35
- new  RS  properties

* Sat Aug 01 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter30
- new build

* Tue Jul 14 2009 Vitaly Lipatov <lav@altlinux.ru> 0.96-eter29
- build from gear repo, rewrote spec
- rename extentions to extensions (see eterbug #4008)
- update buildreq

* Mon Apr 06 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter4
- new ComediInterface

* Mon Apr 06 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter3
- merge with mutabor/master

* Mon Apr 06 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-eter2
- fixed bugs in uniset-codegen

* Sat Jan 17 2009 Pavel Vainerman <pv@altlinux.ru> 0.96-alt7
- new version

* Tue Dec 16 2008 Pavel Vainerman <pv@altlinux.ru> 0.96-alt1
- new version (+extensions)

* Tue Nov 27 2007 Pavel Vainerman <pv@altlinux.ru> 0.93-alt13
- new version

* Tue Nov 27 2007 Pavel Vainerman <pv@altlinux.ru> 0.93-alt11
- new version

* Sun Nov 04 2007 Pavel Vainerman <pv@altlinux.ru> 0.92-alt5
- new version

* Tue Oct 23 2007 Pavel Vainerman <pv@altlinux.ru> 0.92-alt4
- build for C30

* Wed Oct 17 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt8
- new version

* Wed Oct 17 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt7
- new version

* Fri Sep 14 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt6
- new version

* Fri Aug 03 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt5
- new build for C30

* Thu Aug 02 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt4
- new version for C30

* Thu Aug 02 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt3
- new version for C30

* Mon Jul 30 2007 Pavel Vainerman <pv@altlinux.ru> 0.91-alt1
- build for C30

* Fri Jul 13 2007 Pavel Vainerman <pv@altlinux.ru> 0.9-alt14.C30
- buid for C30

* Sun Jul 08 2007 Pavel Vainerman <pv@altlinux.ru> 0.9-alt13
- new build

* Sat Jul 07 2007 Pavel Vainerman <pv@altlinux.ru> 0.9-alt0.C30.1
- build for C30

* Tue Jun 19 2007 Pavel Vainerman <pv@altlinux.ru> 0.8-alt10.M30
- new version

* Mon Jun 18 2007 Pavel Vainerman <pv@altlinux.ru> 0.8-alt9.M30
- new version (for M30)

* Mon Jun 18 2007 Pavel Vainerman <pv@altlinux.ru> 0.8-alt8.M30
- new version (for M30)

* Mon Jun 18 2007 Pavel Vainerman <pv@altlinux.ru> 0.8-alt7
- new version (for M30)

* Mon Jun 18 2007 Pavel Vainerman <pv@altlinux.ru> 0.8-alt1
- new build

* Mon Jun 18 2007 Pavel Vainerman <pv@altlinux.ru> 0.7-alt5
- new build

* Sat Feb 17 2007 Pavel Vainerman <pv@altlinux.ru> 0.7-alt2
- new build

* Mon Feb 05 2007 Pavel Vainerman <pv@altlinux.ru> 0.7-alt1
- new build

* Mon Dec 25 2006 Pavel Vainerman <pv@altlinux.ru> 0.7-alt0.1
- new build

* Tue Jun 13 2006 Pavel Vainerman <pv@altlinux.ru> 0.6-alt2
- fix bug for gcc 4.1.0

* Tue Jun 13 2006 Pavel Vainerman <pv@altlinux.ru> 0.6-alt1
- new version

* Fri Sep 09 2005 Pavel Vainerman <pv@altlinux.ru> 0.5.RC5-alt2
- fixed bug ind AskDUmper::SInfo::operator=

* Mon Aug 29 2005 Pavel Vainerman <pv@altlinux.ru> 0.5.RC5-alt1
- detach mysql-dbserver
- add --disable-mysql for configure script

* Fri Jun 24 2005 Pavel Vainerman <pv@altlinux.ru> 0.5.RC1-alt1
- build new version
- fixed bugs

* Sat Mar 26 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.9-alt4
- fixed bug in IOController: not registration child Objects
- add docs section for IOConfigure

* Sun Feb 27 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.9-alt3
- change createNext in UniXML
- add copyNode (new function to UniXML)

* Tue Feb 22 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.9-alt2
- bug fix for AskDumperXML1

* Mon Feb 21 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.9-alt1
- add ClassGen utility

* Fri Feb 04 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.8-alt1
- correct uniset-admin --logrotate function

* Sat Jan 29 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.7-alt1
- compiled for gcc3.4

* Thu Jan 06 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.6-alt1
- move idl files to /%_datadir/idl/%name
- remove old files

* Mon Jan 03 2005 Pavel Vainerman <pv@altlinux.ru> 0.4.4-alt1
- new version
- rename TimeService --> TimerService
- new start/stop scripts for local run

* Fri Dec 24 2004 Pavel Vainerman <pv@altlinux.ru> 0.4.1-alt1
- new version
- add analog and digital filters
- add sensibility for analog sensor

* Wed Dec 22 2004 Pavel Vainerman <pv@altlinux.ru> 0.0.4-alt1
- build new version

* Tue Nov 09 2004 Pavel Vainerman <pv@altlinux.ru> 0.0.2-alt1
- new version
- disable uniset.xxx-xxx.xxx.rpm

* Mon Nov 08 2004 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt1
- first build
