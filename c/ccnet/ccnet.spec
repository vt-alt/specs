Name: ccnet
Version: 7.1.1
Release: alt1

Summary: Framework for writing networked applications in C

Group: Networking/File transfer
License: GPLv2 with permissions for OpenSSL
Url: https://github.com/haiwen/ccnet-server

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/ccnet-server/archive/v%version-server.tar.gz
Source: %name-%version.tar

BuildRequires: libevent-devel libssl-devel libuuid-devel

BuildRequires: libsqlite3-devel

BuildRequires: libsearpc-devel >= 3.2.0

BuildRequires: vala >= 0.8

# TODO: postgresql
BuildRequires: libmysqlclient-devel

BuildRequires: libzdb-devel >= 2.10.2

BuildRequires: rpm-build-python3

#Requires: lib%name = %version-%release

%description
Ccnet is a framework for writing networked applications in C.

%package -n lib%name
Summary: Library of framework for writing networked applications in C
Group: Networking/File transfer
Requires: libsearpc >= 3.2.0


%description -n lib%name
Ccnet is a framework for writing networked applications in C.

%package -n lib%name-devel
Summary: Development files for lib%name
Requires: lib%name = %version-%release
Group: Networking/File transfer

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name.

%package server
Summary: Ccnet server
Requires: lib%name = %version-%release
Requires: %name = %version-%release
Group: Networking/File transfer
Conflicts: %name < %EVR

%description server
Ccnet server part.
Ccnet is a framework for writing networked applications in C.

%package -n python3-module-%name
Summary: Ccnet python module
Requires: lib%name = %version-%release
Group: Networking/File transfer

%description -n python3-module-%name
Ccnet python module.

%prep
%setup
%__subst 's/(DESTDIR)//' libccnet.pc.in
# since MySQL 8.0
%__subst "s|my_bool|bool|" net/common/ccnet-db.c

%build
%autoreconf
%configure --disable-static PYTHON=%__python3

# smp build does not work
%make_build || %make

%install
%makeinstall_std

%files
#_bindir/ccnet
#%_bindir/ccnet-tool

%files -n lib%name
%_libdir/*.so.*

%files -n python3-module-%name
%python3_sitelibdir/%name/

%files server
%_bindir/ccnet-init
%_bindir/%name-server
#_bindir/%name-servtool

%files -n lib%name-devel
%doc HACKING
%_includedir/ccnet/
%_includedir/ccnet.h
%_libdir/*.so
%_pkgconfigdir/lib%name.pc

%changelog
* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 7.1.1-alt1
- new version 7.1.1 (with rpmrb script)
- python3 fix

* Wed Mar 06 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3.4-alt3
- fix build with MySQL 8.x

* Tue Feb 26 2019 Vitaly Lipatov <lav@altlinux.ru> 6.3.4-alt2
- rebuild with libevent2.1

* Sun Oct 07 2018 Vitaly Lipatov <lav@altlinux.ru> 6.3.4-alt1
- new version (6.3.4) with rpmgs script
- build from ccnet-server only for SeaFile server purposes

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 6.1.8-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.8-alt1
- new version 6.1.8 (with rpmrb script)

* Fri Apr 06 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.7-alt1
- new version 6.1.7 (with rpmrb script)

* Tue Mar 13 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.6-alt1
- new version 6.1.6 (with rpmrb script)

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.5-alt1
- new version 6.1.5 (with rpmrb script)

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.4-alt1
- new version 6.1.4 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.3-alt1
- new version 6.1.3 (with rpmrb script)

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- new version 5.1.4 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.3-alt1
- new version 5.1.3 (with rpmrb script)

* Tue May 17 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt1
- new version 5.0.5 (with rpmrb script)

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt2
- real build 5.0.4

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Fri Nov 21 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version 3.1.11 (with rpmrb script)

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Mon Aug 25 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt7
- new build for ALT Linux Sisyphus (drop old source tree)
- rename repository and subpackages

* Mon Aug 25 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt6
- new version (3.1.4) with rpmgs script
- cleanup spec, drop extraneous files

* Sun Aug 24 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt6
- add ccnet server
- update to 1.4.2

* Fri Nov 08 2013 Denis Baranov <baraka@altlinux.ru> 1.3.6-alt1
- Update to 1.3.6

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus
