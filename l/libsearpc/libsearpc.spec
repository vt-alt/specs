Name: libsearpc
Version: 3.2.0
Release: alt1

Summary: RPC library for Seafile

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/libsearpc

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/libsearpc/archive/v%version.tar.gz
Source: %name-%version.tar
Patch: 9b2e2dc65213fb22ed400dc54e4c2279564df62b.patch

BuildRequires: glib2-devel libjansson-devel

BuildRequires: libgio-devel

BuildRequires: rpm-build-python3 python3-devel

%description
Searpc is a simple C language RPC framework based on GObject system.
Searpc handles the serialization/deserialization part of RPC, the transport part is left to users.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n python3-module-pysearpc
Summary: Seafile RPC python3 module
Group: Networking/File transfer

%description -n python3-module-pysearpc
Seafile RPC python3 module.


%prep
%setup
%patch -p1
sed -i 's/(DESTDIR)//' libsearpc.pc.in
sed -i -e 's@#!/usr/bin/env python@#!%__python3@' lib/searpc-codegen.py

%build
%autoreconf
%configure --disable-static --disable-compile-demo --enable-server-pkg PYTHON=%__python3
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README.markdown
%_libdir/*.so.*

%files -n python3-module-pysearpc
%python3_sitelibdir/pysearpc/

%files devel
%_bindir/searpc-codegen.py
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version (3.2.0) with rpmgs script
- switch to python3 (build the module as standalone package)
- add fix memory leak patch (out of release)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.1-alt3.qa1
- NMU: applied repocop patch

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt3
- fix build

* Tue Sep 11 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt2
- build real 3.1

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version (3.1-latest) with rpmgs script

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 3.0.7-alt2
- move searpc-codegen.py to devel subpackage
- fix build requires

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 3.0.7-alt1
- new version 3.0.7 (with rpmrb script)

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- new version (3.0.4) with rpmgs script
- cleanup spec, drop extraneous files

* Sun Aug 03 2014 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt3
- plus libjansson

* Sun Aug 03 2014 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt2
- update to 1.2.2

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-2
- updated for seafile 1.7.0

* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to 1.1.0 from seafile 1.6.1

* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
