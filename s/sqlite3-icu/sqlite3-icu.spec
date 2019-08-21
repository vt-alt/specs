Name: sqlite3-icu
Version: 1.7
Release: alt1

Summary: SQLite 'ICU' extension integration of the 'International Components for Unicode' library
License: Public Domain
Group: Databases
URL: https://sqlite.org/src/tree?name=ext/icu

Patch0: icu.patch
Source: %name-%version.tar

BuildRequires: libicu-devel libsqlite3-devel sqlite3

%description
SQLite's built-in implementations of these two functions only provide 
case mapping for the 26 letters used in the English language. The ICU 
based functions provided by this extension provide case mapping, where 
defined, for the full range of unicode characters.

%prep
%setup
%patch -p2

%build
gcc -shared icu.c  -fPIC  `icu-config --ldflags` -o libSqliteIcu.so

%install
install -pD -m755 libSqliteIcu.so %buildroot%_libdir/sqlite3/libSqliteIcu.so

%files
%dir %_libdir/sqlite3
%_libdir/sqlite3/libSqliteIcu.so
%doc README.txt

%changelog
* Thu Aug 20 2019 Anton Shevtsov <x09@altlinux.ru> 1.7-alt1
- initial revision
