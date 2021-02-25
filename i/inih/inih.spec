%define soversion 0
%def_disable static

Name: inih
Version: r53
Release: alt1

Summary: Simple .INI file parser in C, good for embedded systems 
License: BSD
Group: System/Libraries

Url: https://github.com/benhoyt/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: meson

%description
inih (INI Not Invented Here) is a simple .INI file parser written in C. It's only a couple of pages of code, and it was designed to be small and simple, so it's good for embedded systems. It's also more or less compatible with Python's ConfigParser style of .INI files, including RFC 822-style multi-line syntax and name: value entries.

To use it, just give ini_parse() an INI file, and it will call a callback for every name=value pair parsed, giving you strings for the section, name, and value. It's done this way ("SAX style") because it works well on low-memory embedded systems, but also because it makes for a KISS implementation.

You can also call ini_parse_file() to parse directly from a FILE* object, ini_parse_string() to parse data from a string, or ini_parse_stream() to parse using a custom fgets-style reader function for custom I/O.

%package -n lib%name%soversion
Summary: Simple .INI file parser in C, good for embedded systems 
Group: System/Libraries

%description -n lib%name%soversion
inih (INI Not Invented Here) is a simple .INI file parser written in C. It's only a couple of pages of code, and it was designed to be small and simple, so it's good for embedded systems. It's also more or less compatible with Python's ConfigParser style of .INI files, including RFC 822-style multi-line syntax and name: value entries.

To use it, just give ini_parse() an INI file, and it will call a callback for every name=value pair parsed, giving you strings for the section, name, and value. It's done this way ("SAX style") because it works well on low-memory embedded systems, but also because it makes for a KISS implementation.

You can also call ini_parse_file() to parse directly from a FILE* object, ini_parse_string() to parse data from a string, or ini_parse_stream() to parse using a custom fgets-style reader function for custom I/O.

%package -n lib%name-devel
Summary: Development files for INI Not Invented Here
Group: Development/C

%description -n lib%name-devel
Development files for INI Not Invented Here

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for INI Not Invented Here
Group: Development/C

%description -n lib%name-devel-static
Static libraries for INI Not Invented Here
%endif

%prep
%setup

%build
%meson -Ddefault_library=shared -Ddistro_install=true -Dwith_INIReader=true
%meson_build

%install
%meson_install

%if_disabled static
%__rm -f %buildroot%_libdir/libINIReader.a
%__rm -f %buildroot%_libdir/lib%name.a
%endif

%files -n lib%name%soversion
%doc LICENSE.txt README.md
%_libdir/libINIReader.so.*
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/INIReader.h
%_includedir/ini.h
%_libdir/libINIReader.so
%_libdir/lib%name.so
%_pkgconfigdir/INIReader.pc
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libINIReader.a
%_libdir/lib%name.a
%endif

%changelog
* Sun Feb 07 2021 Nazarov Denis <nenderus@altlinux.org> r53-alt1
- Version r53

* Sun Jan 31 2021 Nazarov Denis <nenderus@altlinux.org> r52-alt1
- Version r52

* Wed Mar 04 2020 Nazarov Denis <nenderus@altlinux.org> r48-alt1
- Initial build for ALT Linux

