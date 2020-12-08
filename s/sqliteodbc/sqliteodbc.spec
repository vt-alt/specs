%def_without sqlite2
Name: sqliteodbc
Summary: ODBC driver for SQLite
Version: 0.9996
Release: alt3
Source: %name-%version.tar.gz
Patch: sqliteodbc-0.993-alt-odbcinstext.patch
Group: Databases
Url: http://www.ch-werner.de/sqliteodbc
License: BSD

# Automatically added by buildreq on Tue Jun 18 2013
# optimized out: libunixODBC-devel
BuildRequires: libiodbc-devel libsqlite3-devel libxml2-devel zlib-devel
%if_with sqlite2
BuildRequires: libsqlite-devel 
%endif

%description
ODBC driver for SQLite interfacing using the
unixODBC or iODBC driver managers. For more information refer to
http://www.sqlite.org    -  SQLite engine
http://www.unixodbc.org  -  unixODBC Driver Manager
http://www.iodbc.org     -  iODBC Driver Manager

%prep
%setup
%patch

%build
rm aclocal.m4
%autoreconf
%configure
%make_build

%install
mkdir -p %buildroot%_libdir
make install DESTDIR=%buildroot
%if_with sqlite2
rm -f %buildroot%_libdir/libsqliteodbc*.{a,la}
%endif
rm -f %buildroot%_libdir/libsqlite3odbc*.{a,la}
rm -f %buildroot%_libdir/libsqlite3_mod_*.{a,la}

%post
if [ -x /usr/bin/odbcinst ] ; then
   INST=$(/bin/mktemp)
   if [ -r %_libdir/libsqliteodbc.so ] ; then
      cat > $INST << 'EOD'
[SQLITE]
Description=SQLite ODBC 2.X
Driver=%_libdir/libsqliteodbc.so
Setup=%_libdir/libsqliteodbc.so
Threading=2
FileUsage=1
EOD
      /usr/bin/odbcinst -q -d -n SQLITE | grep '^\[SQLITE\]' >/dev/null || {
	 /usr/bin/odbcinst -i -d -n SQLITE -f $INST || true
      }
      cat > $INST << 'EOD'
[SQLite Datasource]
Driver=SQLITE
EOD
      /usr/bin/odbcinst -q -s -n "SQLite Datasource" | \
	 grep '^\[SQLite Datasource\]' >/dev/null || {
	 /usr/bin/odbcinst -i -l -s -n "SQLite Datasource" -f $INST || true
      }
   fi
   if [ -r %_libdir/libsqlite3odbc.so ] ; then
      cat > $INST << 'EOD'
[SQLITE3]
Description=SQLite ODBC 3.X
Driver=%_libdir/libsqlite3odbc.so
Setup=%_libdir/libsqlite3odbc.so
Threading=2
FileUsage=1
EOD
      /usr/bin/odbcinst -q -d -n SQLITE3 | grep '^\[SQLITE3\]' >/dev/null || {
	 /usr/bin/odbcinst -i -d -n SQLITE3 -f $INST || true
      }
      cat > $INST << 'EOD'
[SQLite3 Datasource]
Driver=SQLITE3
EOD
      /usr/bin/odbcinst -q -s -n "SQLite3 Datasource" | \
	 grep '^\[SQLite3 Datasource\]' >/dev/null || {
	 /usr/bin/odbcinst -i -l -s -n "SQLite3 Datasource" -f $INST || true
      }
   fi
   rm -f $INST || true
fi

%preun
if [ "$1" = "0" ] ; then
    test -x /usr/bin/odbcinst && {
	/usr/bin/odbcinst -u -d -n SQLITE || true
	/usr/bin/odbcinst -u -l -s -n "SQLite Datasource" || true
	/usr/bin/odbcinst -u -d -n SQLITE3 || true
	/usr/bin/odbcinst -u -l -s -n "SQLite3 Datasource" || true
    }
    true
fi

%files
%doc README license.terms ChangeLog
%_libdir/*.so*

%changelog
* Fri Nov 20 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9996-alt3
- Updated rpm post script (Fixes: CVE-2020-12050).

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9996-alt2
- NMU: rebuild without sqlite2 support

* Mon Aug 20 2018 Fr. Br. George <george@altlinux.ru> 0.9996-alt1
- Autobuild version bump to 0.9996

* Tue Jun 18 2013 Fr. Br. George <george@altlinux.ru> 0.993-alt1
- Initial build from upstream srpm
- Fix build for using ODBCINSTGetProperties
