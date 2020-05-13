%def_without sqlite3
%def_without oracle_support
%define sope_makeflags %nil
%define sope_version 4.9
%define sbjson_major_version 2
%define module_name ngobjweb

Summary:      SOPE is an extensive set of frameworks which form a complete Web application server environment
Name:         sope
Version:      4.3.2
Release:      alt1
License:      GPL-2.0+
URL:          http://sogo.nu/
Group:        Development/Objective-C
Packager:     Andrey Cherepanov <cas@altlinux.org>

Source:       SOPE-%version.tar.gz
Patch:	      %name-%version-%release.patch

BuildRequires: gnustep-make-devel 
BuildRequires: gnustep-base-devel
BuildRequires: gcc-objc
BuildRequires(pre): rpm-build-apache2
BuildRequires: postgresql-devel
BuildRequires: libffi-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmp-devel
BuildRequires: libgnutls-devel
BuildRequires: libicu-devel
BuildRequires: libldap-devel
BuildRequires: liblzma-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: apache2-devel
BuildRequires: libapr1-devel
BuildRequires: zlib-devel
BuildRequires: /proc

%description
SOPE is an extensive set of frameworks which form a complete Web
application server environment. Besides the Apple WebObjects compatible
appserver extended with Zope concepts, it contains a large set of
reusable classes: XML processing (SAX, DOM, XML-RPC), MIME/IMAP4
processing, LDAP connectivity, RDBMS connectivity, and iCalendar
parsing.

%package -n libsope
Summary:   SOPE libraries
Group:     Development/Objective-C
Provides:  %name-appserver = %EVR
Obsoletes: %name-appserver < %EVR
Provides:  %name-core = %EVR
Obsoletes: %name-core < %EVR
Provides:  %name-gdl1 = %EVR
Obsoletes: %name-gdl1 < %EVR
Provides:  %name-ldap = %EVR
Obsoletes: %name-ldap < %EVR
Provides:  %name-mime = %EVR
Obsoletes: %name-mime < %EVR
Provides:  %name-sbjson = %EVR
Obsoletes: %name-sbjson < %EVR
Provides:  %name-xml = %EVR
Obsoletes: %name-xml < %EVR


%description -n libsope
SOPE is an extensive set of frameworks which form a complete Web
application server environment. Besides the Apple WebObjects compatible
appserver extended with Zope concepts, it contains a large set of
reusable classes: XML processing (SAX, DOM, XML-RPC), MIME/IMAP4
processing, LDAP connectivity, RDBMS connectivity, and iCalendar
parsing.

%package -n libsope-devel
Summary:   Development files for the SOPE libraries
Group:     Development/Objective-C
Requires:  libsope = %EVR
Provides:  %name-appserver-devel = %EVR
Obsoletes: %name-appserver-devel < %EVR
Provides:  %name-core-devel = %EVR
Obsoletes: %name-core-devel < %EVR
Provides:  %name-gdl1-devel = %EVR
Obsoletes: %name-gdl1-devel < %EVR
Provides:  %name-ldap-devel = %EVR
Obsoletes: %name-ldap-devel < %EVR
Provides:  %name-mime-devel = %EVR
Obsoletes: %name-mime-devel < %EVR
Provides:  %name-sbjson-devel = %EVR
Obsoletes: %name-sbjson-devel < %EVR
Provides:  %name-xml-devel = %EVR
Obsoletes: %name-xml-devel < %EVR

%description -n libsope-devel
This package contains the development files of the SOPE libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package gdl1-postgresql
Summary:      PostgreSQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     libsope 
#Requires:    postgresql-libs

%description gdl1-postgresql
This package contains the PostgreSQL connector for SOPE's fork of the
GNUstep database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%if_with oracle_support
%package gdl1-oracle
Summary:      Oracle connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     libsope
#Requires:    oracle-instantclient-basic

%description gdl1-oracle
This package contains the Oracle connector for SOPE's fork of the
GNUstep database libraries.
%endif

%package gdl1-mysql
Summary:      MySQL connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     libsope

%description gdl1-mysql
This package contains the MySQL connector for SOPE's fork of the
GNUstep database libraries.

%if_with sqlite3
%package gdl1-sqlite3
Summary:      SQLite3 connector for SOPE's fork of the GNUstep database environment
Group:        Development/Objective-C
Requires:     libsope

%description gdl1-sqlite3
This package contains the SQLite3 connector for SOPE's fork of the
GNUstep database libraries.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.
%endif

%package -n apache2-mod_ngobjweb
Summary:      mod_ngobjweb module for Apache2
Group:        System/Servers
Requires:     libsope

%description -n apache2-mod_ngobjweb
Enables apache2 to handle HTTP requests for the
OpenGroupware.org application server.

%prep
%setup -q -n SOPE
%patch -p1
for f in config.guess config.sub;do
	rm -f sope-core/NGStreams/$f
	cp -vL /usr/share/automake/$f sope-core/NGStreams
done

%build
%ifarch x86_64
  ORACLELIB_PATH="%_libdir/oracle/11.2/client64/lib/"
%else
  ORACLELIB_PATH="%_libdir/oracle/11.2/client/lib/"
%endif

. /usr/share/GNUstep/Makefiles/GNUstep.sh
./configure --with-gnustep

make %{sope_makeflags} apr=/usr/bin/apr-1-config apxs=%apache2_apxs apu=/usr/bin/apu-1-config

pushd sope-gdl1/MySQL
make LDFLAGS="-L%_libdir/mysql" %{sope_makeflags}
popd

%if_with oracle_support
pushd Oracle8
make LDFLAGS="-L$ORACLELIB_PATH" %{sope_makeflags}
popd
%endif

%install
install -d %buildroot%apache2_libexecdir
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM %{sope_makeflags} apxs="%apache2_apxs -S LIBEXECDIR=%buildroot%apache2_libexecdir"

pushd sope-gdl1/MySQL
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM %{sope_makeflags}
popd

%if_with oracle_support
pushd Oracle8
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM %{sope_makeflags}
popd
%endif

rm -f  %buildroot%_bindir/otest
rm -fr %buildroot%_libdir/GNUstep/GDLAdaptors-%{sope_version}/SQLite3.gdladaptor

# Fix path to NGObjWeb in sope-appserver
mkdir -p %buildroot%_datadir/%name-%{sope_version}
mv %buildroot%_libdir/GNUstep/Resources/NGObjWeb %buildroot%_datadir/%name-%{sope_version}/ngobjweb

install -d %buildroot%apache2_mods_available
echo "LoadModule ngobjweb_module %apache2_libexecdir/mod_ngobjweb.so" > %buildroot%apache2_mods_available/%module_name.load
#install -Dpm644 %module_name.conf %buildroot%apache2_mods_available/%module_name.conf
install -d %buildroot%apache2_mods_start
echo "%module_name=yes" > %buildroot%apache2_mods_start/100-%module_name.conf

%files -n libsope
%_libdir/lib*.so.*
%_libdir/GNUstep/*
%exclude %_libdir/GNUstep/GDLAdaptors-%{sope_version}/*.gdladaptor
%_datadir/sope-%{sope_version}/ngobjweb/*.plist

%files -n libsope-devel
%_bindir/*
%_includedir/*
%_libdir/lib*.so
%_datadir/GNUstep/Makefiles

%files gdl1-postgresql
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/PostgreSQL.gdladaptor

%if_with oracle_support
%files gdl1-oracle
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/Oracle8.gdladaptor
%endif

%files gdl1-mysql
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/MySQL.gdladaptor

%if_with sqlite3
%files gdl1-sqlite3
%_libdir/GNUstep/GDLAdaptors-%{sope_version}/SQLite3.gdladaptor
%endif

%files -n apache2-mod_ngobjweb
%apache2_libexecdir/*.so
%config %apache2_mods_available/%module_name.load
%config %apache2_mods_start/100-%module_name.conf

%post -n apache2-mod_ngobjweb
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To use %module_name check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %module_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun -n apache2-mod_ngobjweb
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun -n apache2-mod_ngobjweb
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To complete %module_name uninstalling check configuration and restart %apache2_dname service."
        echo
    fi
fi

%changelog
* Thu May 07 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version.

* Sat May 02 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version.

* Mon Jan 27 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Wed Dec 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.
- Fix license tag.

* Fri Nov 01 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.1-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.8-alt1
- New version.

* Tue Jun 25 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt2
- Do not restrict architecture.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version.

* Thu Feb 21 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.6-alt1
- New version.

* Wed Jan 09 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.5-alt1
- New version.

* Wed Oct 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt1
- New version.

* Thu Oct 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.3-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Jul 10 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- New version.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Mon Oct 09 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.2.10-alt2
- mUTF7 corrections (RFC3501) for non-ASCII IMAP folder names
  (ALT: #33722, #32426)

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.10-alt1
- New version

* Tue May 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1
- New version

* Fri Mar 24 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.8-alt1
- New version

* Wed Feb 15 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1
- new version 3.2.7

* Tue Jan 24 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.6-alt1
- new version 3.2.6
- package all libraries to libsope and development files to libsope-devel

* Wed Jan 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- new version 3.2.5

* Tue Dec 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- new version 3.2.4

* Thu Nov 24 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Thu Nov 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- new version 3.2.0

* Mon Aug 22 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt1
- new version 3.1.5

* Wed Jul 13 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.4-alt1
- new version 3.1.4

* Thu Jun 23 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version

* Fri Apr 29 2016 Sergey Alembekov <rt@altlinux.ru> 3.0.2-alt3
- rebuild with apache-2.4

* Thu Mar 10 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt2
- Rebuild with new rpm

* Tue Mar 08 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version

* Mon Feb 08 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Tue Jan 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.7-alt1
- New version

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1
- New version

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version

* Mon Nov 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- Inital build in Sisyphus
- Build apache2-mod_ngobjweb
