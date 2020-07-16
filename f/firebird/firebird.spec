%define _unpackaged_files_terminate_build 1

%define major 3.0.6.33328
%define minor 0
%define pkgname Firebird
%define pkgversion %major-%minor
%define fbroot %_libdir/%name

Name: firebird
Version: %major.%minor
Release: alt1
Summary: Firebird SQL Database, fork of InterBase
Group: Databases
License: IPL
Url: https://www.firebirdsql.org/

# https://github.com/FirebirdSQL/firebird.git
Source: %name-%version.tar
Source1: %name.init

Patch1: %name-3.0.5.33220.0-fedora-obsolete-syslogd.target.patch
Patch2: %name-3.0.5.33220.0-fedora-no-copy-from-icu.patch
Patch3: %name-3.0.5.33220.0-fedora-honour-buildflags.patch
Patch4: %name-3.0.5.33220.0-fedora-cloop-honour-build-flags.patch
Patch5: %name-3.0.5.33220.0-fedora-add-pkgconfig-files.patch
Patch6: %name-3.0.5.33220.0-fedora-Provide-sized-global-delete-operators-when-compiled.patch

Requires: libfbclient = %EVR

BuildPreReq: rpm-build-compat
BuildRequires: libtinfo-devel libicu-devel libedit-devel
BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: libtool
BuildRequires: libncurses-devel
BuildRequires: zlib-devel libtommath-devel
BuildRequires: libtomcrypt-devel

Obsoletes: %name-superserver
Conflicts: %name-superserver < %EVR
Provides: %name-superserver = %EVR
Obsoletes: %name-classic
Conflicts: %name-classic < %EVR
Provides: %name-classic = %EVR

%description
This is the Firebird SQL Database shared files.

%package devel
Summary: Development Libraries for Firebird SQL Database
Group: Development/Databases
Requires: %name = %EVR

%description devel
Development libraries for firebird.

%package utils
Summary: Client programs for Firebird SQL Database
Group: Databases
Requires: %name = %EVR
Obsoletes: %name-client-embedded <= 2.0
Obsoletes: %name-utils-superserver
Conflicts: %name-utils-superserver < %EVR
Provides: %name-utils-superserver = %EVR
Obsoletes: %name-utils-classic
Conflicts: %name-utils-classic < %EVR
Provides: %name-utils-classic = %EVR

%description utils
Client access tools for firebird.

%package -n libfbclient
Summary: Multi-threaded, non-local client libraries for Firebird SQL Database
Group: System/Libraries

%description -n libfbclient
Multi-threaded, non-local client libraries for Firebird SQL Database

%package server
Summary: Server for Firebird SQL Database
Group: Databases
Requires: %name = %EVR
Obsoletes: %name-server-superserver
Conflicts: %name-server-superserver < %EVR
Provides: %name-server-superserver = %EVR
Obsoletes: %name-server-classic
Conflicts: %name-server-classic < %EVR
Provides: %name-server-classic = %EVR
Obsoletes: %name-server-common
Conflicts: %name-server-common < %EVR
Provides: %name-server-common = %EVR
%add_findreq_skiplist %_sbindir/changeServerMode.sh

%description server
This is the server for the Firebird SQL Database.
It can also be used as an embedded server, when paired with the
client-embedded package.

It does not include any client access tools, nor does it include the
multi-threaded client library.

%package doc
Summary: Documentation for Firebird SQL server
Group: Databases
Requires: %name-server = %EVR
BuildArch: noarch

%description doc
Documentation for Firebird SQL server.

%package examples
Summary: Examples for Firebird SQL server
Group: Databases
Requires: %name-server = %EVR

%description examples
Examples for Firebird SQL server.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# sed vs patch for portability and addtional location changes
# based on FIREBIRD=%_libdir/firebird
check_sed() {
	MSG="sed of $3, required $2 line(s) modified $1"
	echo "${MSG}"
	[[ $1 -ge $2 ]] || { echo "${MSG}" ; exit -1 ; }
}

check_sed "$(sed -i -e 's:"isql :"isql-fb :w /dev/stdout' \
	src/isql/isql.epp | wc -l)" "1" "src/isql/isql.epp" # 1 line
check_sed "$(sed -i -e 's:isql :isql-fb :w /dev/stdout' \
	src/msgs/history2.sql | wc -l)" "4" "src/msgs/history2.sql" # 4 lines
check_sed "$(sed -i -e 's:--- ISQL:--- ISQL-FB:w /dev/stdout' \
	-e 's:isql :isql-fb :w /dev/stdout' \
	-e 's:ISQL :ISQL-FB :w /dev/stdout' \
	src/msgs/messages2.sql | wc -l)" "6" "src/msgs/messages2.sql" # 6 lines

find . -name \*.sh -exec chmod +x {} + || { echo "chmod failed" ; exit -1 ; }
rm -rf ./extern/{editline,icu,libtomcrypt,libtommath,zlib} || { echo "rm -rf failed" ; exit -1 ;}

%build
%add_optflags -fno-sized-deallocation -fno-delete-null-pointer-checks -I%_includedir/tommath
%add_optflags -fno-strict-aliasing
%add_optflags -Wno-deprecated -Wno-switch

%autoreconf
%configure \
	--prefix=%fbroot \
	--with-system-editline \
	--with-fbbin=%_bindir \
	--with-fbsbin=%_sbindir \
	--with-fbconf=%_sysconfdir/%name \
	--with-fblib=%_libdir \
	--with-fbinclude=%_includedir/%name \
	--with-fbdoc=%_defaultdocdir/%name \
	--with-fbudf=%_libdir/%name/udf \
	--with-fbsample=%_defaultdocdir/%name/sample \
	--with-fbsample-db=%_localstatedir/%name/data/ \
	--with-fbhelp=%_localstatedir/%name/system/ \
	--with-fbintl=%_libdir/%name/intl \
	--with-fbmisc=%_datadir/%name/misc \
	--with-fbsecure-db=%_localstatedir/%name/secdb/ \
	--with-fbmsg=%_localstatedir/%name/system/ \
	--with-fblog=%_logdir/%name \
	--with-fbglock=%_runtimedir/%name \
	--with-fbplugins=%_libdir/%name/plugins \
	--disable-rpath \
	%nil

%make

pushd gen
%make -f Makefile.install buildRoot
chmod -R u+w buildroot%{_docdir}/%{name}
chmod u+rw,a+rx buildroot/usr/include/firebird/firebird/impl
popd

%install
mkdir -p %buildroot
cp -r gen/buildroot/* %buildroot/

# prepare dir
mkdir -p %buildroot%_sysconfdir/xinetd.d
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%fbroot/intl
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_sysconfdir/profile.d
mkdir -p %buildroot%_runtimedir/%name
mkdir -p %buildroot%_localstatedir/%name/backup
mkdir -p %buildroot%_logdir/%name/
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_pkgconfigdir

cp -a src/misc/upgrade %buildroot%_datadir/%name

install -m 0644 gen/install/misc/firebird-superserver.service %buildroot%_unitdir/
install -m 0644 gen/install/misc/firebird-classic@.service %buildroot%_unitdir/
install -m 0644 gen/install/misc/firebird-classic.socket %buildroot%_unitdir/

cp -v gen/install/misc/*.pc %buildroot%_pkgconfigdir

pushd gen/Release/%name
# intl
cp intl/libfbintl.so %buildroot%fbroot/intl/fbintl.so
cp -a bin/posixLibrary.sh %buildroot%_datadir/%name
# examples
cp -a examples %buildroot%_datadir/%name
popd

mv %buildroot%fbroot/intl/fbintl.conf %buildroot%_sysconfdir/%name/fbintl.conf
ln -sf $(relative %_sysconfdir/%name/fbintl.conf %fbroot/intl/fbintl.conf) %buildroot%fbroot/intl/fbintl.conf
ln -sf fbintl.so %buildroot%fbroot/intl/libfbintl.so
ln -sf $(relative %fbroot/intl/fbintl.so %_sysconfdir/%name/libfbintl.so) %buildroot%_sysconfdir/%name/libfbintl.so

# services
install -m 755 %SOURCE1 %buildroot%_initdir/%name
mv %buildroot%_datadir/%name/misc/%name.xinetd %buildroot%_sysconfdir/xinetd.d/%name

# log
touch %buildroot%_logdir/%name/%name.log

mv %buildroot%_bindir/isql %buildroot%_bindir/isql-fb
mv %buildroot%_bindir/gstat %buildroot%_bindir/gstat-fb
mv %buildroot%_sbindir/fb_config %buildroot%_bindir/fb_config
mv %buildroot%_sysconfdir/%name/README %buildroot%_docdir/%name/
mv %buildroot%_sysconfdir/%name/{WhatsNew,*.txt} %buildroot%_docdir/%name/

rm -f %buildroot%_sbindir/FirebirdUninstall.sh
rm -rf %buildroot%_datadir/%name/misc/upgrade
rm -f %buildroot%_datadir/%name/misc/firebird-classic.socket
rm -f %buildroot%_datadir/%name/misc/firebird-classic@.service
rm -f %buildroot%_datadir/%name/misc/firebird-superserver.service
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.debian
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.generic
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.gentoo
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.mandrake
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.slackware
rm -f %buildroot%_datadir/%name/misc/firebird.init.d.suse
rm -f %buildroot%_datadir/%name/misc/rc.config.firebird

# -----------------------------------------------------------------------------
# server-common scripts
# -----------------------------------------------------------------------------
%post server
if [ ! -f %_sysconfdir/gds_hosts.equiv ]; then
	echo localhost > %_sysconfdir/gds_hosts.equiv
fi
%post_service %name

%preun server
%preun_service %name

%pre server
# Create the firebird group if it doesn't exist
%_sbindir/groupadd -f -r %name 2>/dev/null ||:
%_sbindir/useradd -d %_localstatedir/%name -g %name -s /dev/null -r %name 2>/dev/null ||:

%pre
# Add gds_db to %_sysconfdir/services if needed
FileName=%_sysconfdir/services
newLine="gds_db          3050/tcp  # Firebird SQL Database Remote Protocol"
oldLine=`grep "^gds_db" $FileName`
if [ -z "$oldLine" ]; then
	echo $newLine >> $FileName
fi

%files
%_docdir/%name/IDPLicense.txt
%_docdir/%name/IPLicense.txt
%doc doc/*
%dir %fbroot
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/databases.conf
%config(noreplace) %_sysconfdir/%name/fbtrace.conf
%config(noreplace) %_sysconfdir/%name/firebird.conf
%config(noreplace) %_sysconfdir/%name/plugins.conf
%dir %_datadir/%name
%dir %_datadir/%name/upgrade
%_datadir/%name/upgrade/*
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*
%dir %_datadir/%name/misc
%_datadir/%name/misc/*.sql

%files devel
%attr (0755,root,root) %_bindir/fb_config
%_bindir/gpre
%_includedir/*
%_libdir/libfbclient.so
%_pkgconfigdir/*.pc

%files utils
%_bindir/gbak
%_bindir/gfix
%_bindir/gstat-fb
%_bindir/isql-fb
%_bindir/qli
%_bindir/fbtracemgr

%files -n libfbclient
%_libdir/libfbclient.so.*

%files server
%dir %attr(2775,root,%name) %_runtimedir/%name
%dir %attr(2775,root,%name) %_localstatedir/%name
%dir %attr(2775,root,%name) %_localstatedir/%name/secdb
%dir %attr(2775,root,%name) %_localstatedir/%name/system
%dir %attr(2775,root,%name) %_localstatedir/%name/backup
#ghost %_sysconfdir/gds_hosts.equiv
%dir %fbroot/udf
%dir %fbroot/intl
%attr(0660,firebird,firebird) %config(noreplace) %_localstatedir/%name/secdb/security3.fdb
%attr(0664,firebird,firebird) %_localstatedir/%name/system/help.fdb
%attr(0664,firebird,firebird) %_localstatedir/%name/system/firebird.msg
%config(noreplace) %_sysconfdir/%name/fbintl.conf
%_sysconfdir/%name/libfbintl.so
%attr(0755,root,root) %_initdir/%name
%config(noreplace) %attr(640,root,root) %_sysconfdir/xinetd.d/%name
%_unitdir/*
%dir %attr (2770,root,%name) %_logdir/%name
%attr (0660,%name,%name) %_logdir/%name/%name.log
%fbroot/udf/*
%fbroot/intl/*
%_bindir/gsplit
%_bindir/nbackup
%_bindir/gsec
%_bindir/fbsvcmgr
%attr (0755,root,root) %_sbindir/*.sh
%_sbindir/fb_lock_print
%_sbindir/fbguard
%_sbindir/firebird
%_libdir/libib_util.so
%_datadir/%name/*.sh

%files doc
%_docdir/%name
%exclude %_docdir/%name/IDPLicense.txt
%exclude %_docdir/%name/IPLicense.txt
%exclude %_docdir/%name/sample

%files examples
%_docdir/%name/sample
%attr(0660,%name,%name) %_localstatedir/%name/data/employee.fdb
%dir %_datadir/%name/examples
%_datadir/%name/examples/*

%changelog
* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.6.33328.0-alt1
- Updated to upstream version 3.0.6.33328-0.

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.5.33220.0-alt1
- Updated to upstream version 3.0.5.33220-0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.4.33054.0-alt1.qa1
- NMU: applied repocop patch

* Wed Oct 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.4.33054.0-alt1
- Updated to upstream version 3.0.4.33054-0.

* Fri Jan 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt4
- Rebuilt with new libtommath.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt3
- Fixed init script once more (closes: #34060).
- Fixed issue with firebird not finding INTL module.
- Fixed config for xinetd.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt2
- Fixed init script (closes: #34060).
- Updated provides and obsoletes.

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2.32703.0-alt1
- Updated to upstream version 3.0.2.32703-0 (closes: #30271).

* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.5.18497.0-alt2.1
- Rebuild with new icu

* Thu Apr 04 2013 Dmitry V. Levin <ldv@altlinux.org> 2.1.5.18497.0-alt2
- Fixed build.

* Wed Apr 03 2013 Boris Savelev <boris@altlinux.org> 2.1.5.18497.0-alt1
- new version

* Fri Mar 16 2012 Boris Savelev <boris@altlinux.org> 2.1.4.18393.0-alt1
- new version

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 2.1.3.18185.0-alt4.3
- rebuilt for debuginfo
- enabled strict dependencies between subpackages

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.3.18185.0-alt4.2.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3.18185.0-alt4.2
- Rebuilt for soname set-versions

* Tue Mar 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt4.1
- rebuild with icu 4.4

* Sat Jan 23 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt4
- move %%_var/run/%%name to %%name-server-common (closes: #17689)
- fix permission on %%_sysconfdir/xinet.d/%%name

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt3
- fix owner on %%utilsshell

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt2
- fix perm on fbscripts (closes: #22751)
- move %%utilsshell to %%_bindir

* Sat Jan 16 2010 Boris Savelev <boris@altlinux.org> 2.1.3.18185.0-alt1
- new version
- fix fbscripts (closes: #22596)

* Wed Jun 03 2009 Boris Savelev <boris@altlinux.org> 2.1.2.18118.0-alt3
- fix gcc44 build

* Tue May 12 2009 Boris Savelev <boris@altlinux.org> 2.1.2.18118.0-alt2
- fix #19660

* Thu Apr 09 2009 Boris Savelev <boris@altlinux.org> 2.1.2.18118.0-alt1
- new verison
- fix #19448

* Fri Nov 07 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt6
- move adding service desription from firebird-server-common to firebird

* Sat Sep 27 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt5
- add functions library for shell scripts in share for server-common

* Thu Aug 21 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt4
- fix directory permissions
- move gpre to devel
- move common files of servers and utils to package firebird

* Tue Aug 19 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt3
- rename libfbintl.so to fbintl.so
- rename isql to fbsql (conflicts with unixODBC)

* Thu Aug 14 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt2
- close #16681

* Wed Aug 06 2008 Boris Savelev <boris@altlinux.org> 2.1.1.17910.0-alt1
- initial build for Sisyphus

* Tue Mar 11 2008 Tiago Salem <salem@mandriva.com.br> 2.0.3.12981.0-2mdv2008.1
+ Revision: 186539
- Fix initscript and create %_sysconfdir/gds_hosts.equiv on %%post to fix bug #34267
- bump release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 13 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.3.12981.0-1mdv2008.0
+ Revision: 84989
- New upstream: 2.0.3.12981, fixing an annoying bug.

* Fri Aug 24 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.2.12964.0-3mdv2008.0
+ Revision: 71056
- New upstream: 2.0.2

* Fri Aug 17 2007 Funda Wang <fundawang@mandriva.org> 2.0.1.12855.0-3mdv2008.0
+ Revision: 64705
- fix obsoletes old package

* Wed Aug 15 2007 Funda Wang <fundawang@mandriva.org> 2.0.1.12855.0-2mdv2008.0
+ Revision: 63722
- Fix file conflict

* Wed May 09 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.1.12855.0-1mdv2008.0
+ Revision: 25665
- New upstream: 2.0.1
- Removed patch amd64: applied upstream.

* Fri Jan 19 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12748-8mdv2007.0
+ Revision: 110615
- Improve firebird-classic and firebird-superserver summaries in order
  to explicit their difference: xinetd and standalone.

* Fri Nov 24 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12748-7mdv2007.1
+ Revision: 86946
- Added /var/lib/firebird and /var/lib/firebird/backup to server-common
  package.

* Thu Nov 16 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12748-6mdv2007.1
+ Revision: 84834
- Try libncurses-devel instead
- Added buildrequires to libncurses5-devel
- New upstream: 2.0.0.12748 (2.0.0 final)
- Fully disabled parallel build, as it is broken for now.
- Bumped release, in order to be able to rebuild for x86_64.
- Added missing BuildRequires to libtermcap-devel, as required by included
  readline.

* Wed Sep 13 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-4mdv2007.0
+ Revision: 61079
- Added Conflicts in firebird-server-common to firebird-firebird-server-classic
  < 2.0 due to moved files.
- Fix binaries ownership in firebird-server-classic. They should be owned by
  root:root and not firebird:firebird.

* Wed Sep 06 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-3mdv2007.0
+ Revision: 59998
- Applied Philippe Makowski suggestions:
  * Include example employee.fdb
  * -devel should requires libfbclient
  * Tagged security2.fdb as config.

* Tue Sep 05 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-2mdv2007.0
+ Revision: 59875
- Disabled parallel build: it's broken.
- Import firebird

* Sat Sep 02 2006 Marcelo Ricardo Leitner <mrl@mandriva.com> 2.0.0.12724-1mdv2007.0
- Major packaging restructuring, following debian style.
- Enabled superserver flavor.
- Enhanced pre/post sections.
- Do not remove firebird user on package removal: we may leave some files on
  the filesystem.

* Thu Aug 24 2006 Philippe Makowski <makowski@firebird-fr.eu.org> 2.0.0.12724-0.1mdk
- Update to Firebird2

* Tue Jul 26 2005 Stew Benedict <sbenedict@mandriva.com> 1.5.2.4731-0.3mdk
- fix provides in lib package

* Fri Jan 28 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.5.2.4731-0.2mdk
- add deps
- little spec cleaning

* Wed Jan 12 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.5.2.4731-0.1mdk
- from Philippe Makowski <makowski@firebird-fr.eu.org> :
	- adapted to Mandrake
	- updated from the CVS tree
- libification
- bzip2 patches
- use configure macros
- requires on versions not on releases

* Wed Aug 18 2004 Erik S. LaBianca <erik@ilsw.com> - 1.5.1.4481-0.fdr.1
- updated to 1.5.1 official source release
- minimized install patch intrusiveness, move files in .spec file instead
- don't try to remove the user/group on install, just leave the mess

* Wed Feb 04 2004 Erik S. LaBianca <erik@ilsw.com> - 1.5.0.4280-postRC8.1
- updated to CVS code
- remove lock files from post/postun
- set target arch to match prefix.linux settings
- add dependencies to firebird RPM

* Tue Feb 03 2004 Erik S. LaBianca <erik@ilsw.com> - 1.5.0.4201-1
- updated to RC8 code
- added gds_db service entry to %_sysconfdir/services if necessary in post
- fix isql link

