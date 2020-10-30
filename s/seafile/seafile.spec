Name: seafile
Version: 7.0.10
Release: alt1

Summary: Full-fledged cloud storage platform

Group: Networking/File transfer
License: GPLv2 with permissions for OpenSSL
Url: https://github.com/haiwen/seafile

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/seafile/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: README.ALT.utf8.txt
Source2: nginx.conf.example

Patch: seafile-curl-7.62.patch

Requires: lib%name = %version-%release

BuildRequires: intltool libssl-devel libuuid-devel
BuildRequires: zlib-devel libjson-glib-devel
BuildRequires: vala
BuildRequires: rpm-build-python3 python3-devel

BuildRequires: libsearpc-devel >= 3.2.0

BuildRequires: libsqlite3-devel >= 3.7
BuildRequires: libevent-devel >= 2.0
BuildRequires: libarchive-devel >= 2.8.5
BuildRequires: libcurl-devel >= 7.17

%description
Seafile is a next-generation open source cloud storage system
with advanced support for file syncing, privacy protection and teamwork.

Collections of files are called libraries, and each library can be synced separately.
A library can be encrypted with a user chosen password.
This password is not stored on the server,
so even the server admin cannot view a file's contents.

Seafile allows users to create groups with file syncing,
wiki, and discussion to enable easy collaboration around documents within a team.

%package -n fuse-seafile
Summary: Seafile FUSE access
Group: Networking/File transfer
Requires: lib%name = %version-%release

%description -n fuse-seafile
Seafile FUSE access.
Seafile is a next-generation open source cloud storage system
with advanced support for file syncing, privacy protection and teamwork.

%package cli
Summary: Seafile CLI client
Group: Networking/File transfer
Requires: lib%name = %version-%release

%description cli
Seafile CLI client.

Seafile is a next-generation open source cloud storage system
with advanced support for file syncing, privacy protection and teamwork.

%package -n python3-module-seafile
Summary: Seafile client python3 module
Group: Networking/File transfer

%description -n python3-module-seafile
The python3 module with Seafile client.

%package -n lib%name
Summary: Seafile library files
Group: Networking/File transfer

%description -n lib%name
The lib%name package contains libraries for Seafile.

%package -n lib%name-devel
Summary: Development files for lib%name
Requires: lib%name = %version-%release
Group: Development/C

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name.

%prep
%setup
#patch -p1
cp %SOURCE1 .
# remove buildroot from .pc file
%__subst 's/(DESTDIR)//' lib/libseafile.pc.in
#%__subst 's@#!/usr/bin/env python@#!%__python3@' app/seaf-cli

%build
%autoreconf
%configure --disable-static PYTHON=%__python3
# FIXME: breakes build
%make_build || %make

%install
%makeinstall_std

%files
%_bindir/seaf-daemon
%_man1dir/seaf-daemon*.1.*

%files cli
%_bindir/seaf-cli
%_man1dir/seaf-cli.1.*

%files -n lib%name
%_libdir/*.so.*

%files -n python3-module-seafile
%python3_sitelibdir/%name/

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/lib%name.pc

%changelog
* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.10-alt1
- new version 7.0.10 (with rpmrb script)

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.9-alt1
- new version 7.0.9 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.8-alt1
- new version 7.0.8 (with rpmrb script)

* Tue May 12 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.7-alt1
- new version 7.0.7 (with rpmrb script)

* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.6-alt1
- new version 7.0.6 (with rpmrb script)

* Sat Jan 18 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.5-alt1
- new version 7.0.5 (with rpmrb script)
- pack seaf-cli in standalone package
- use python3 only

* Fri Aug 30 2019 Vitaly Lipatov <lav@altlinux.ru> 7.0.2-alt1
- new version 7.0.2 (with rpmrb script)

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 7.0.1-alt1
- new version 7.0.1 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2.11-alt1
- new version 6.2.11 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.9-alt1
- new version 6.2.9 (with rpmrb script)

* Mon Nov 05 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.5-alt2
- fix build with curl 7.62

* Tue Sep 11 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.5-alt1
- new version 6.2.5 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.4-alt1
- new version 6.2.4 (with rpmrb script)

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt1
- new version 6.2.2 (with rpmrb script)
- drop libccnet-devel, libzdb-devel build requires

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.8-alt1
- new version 6.1.8 (with rpmrb script)

* Fri Apr 06 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.7-alt1
- new version 6.1.7 (with rpmrb script)
- drop obsoleted buildreq libevhtp-seafile-devel (used in seafile-server only)

* Tue Mar 13 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.6-alt1
- new version 6.1.6 (with rpmrb script)

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1.5-alt1
- new version 6.1.5 (with rpmrb script)

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.4-alt1
- new version 6.1.4 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.3-alt1
- new version 6.1.3 (with rpmrb script)

* Mon Feb 13 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.3-alt1
- new version 6.0.3 (with rpmrb script)

* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt3
- build with compat libevhtp-seafile = 1.2.9
- fix license in spec to GPLv2 with permissions for OpenSSL

* Sat Aug 06 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt2
- fix build with libevhtp >= 1.2.11

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- new version 5.1.4 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.3-alt1
- new version 5.1.3 (with rpmrb script)

* Tue May 17 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Fri Nov 21 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version 3.1.11 (with rpmrb script)

* Sun Aug 31 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt2
- separate seafile fuse client
- add nginx server config
- add man for ccnet and seafile-applet

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)
- add ccnet requires

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version (3.1.4) with rpmgs script
- cleanup spec
- build server part

* Fri Aug 22 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt5
- update buildrequires

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt4
- + libjansson-devel

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt3
- update to 3.1.0

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt2
- update source

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt2
- Fix some error in repository

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt1
- Initial build libseafile for ALTLinux

