%def_enable docs

Name: editorconfig
Version: 0.12.3
Release: alt1.1

Summary: Parser for EditorConfig files written in C
Group: Development/Other
License: BSD-like
Url: https://%name.org

%define srcname %name-core-c
#VCS: https://github.com/%name/%srcname
Source: %url/archive/v%version/%srcname-%version.tar.gz

Requires: lib%name = %EVR

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libpcre2-devel
%{?_enable_docs:BuildRequires: doxygen}

%description
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.

%package -n lib%name
Summary: EditorConfig shared library
Group: System/Libraries

%description -n lib%name
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.

This package contains shared EditorConfig library.

%package -n lib%name-devel
Summary: Development files for EditorConfig library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.

This package contains files needed for development EditorConfig plugins.

%prep
%setup -n %srcname-%version

%build
%cmake %{?_disable_docs:-DBUILD_DOCUMENTATION=OFF}

%install
%cmakeinstall_std

%files
%_bindir/%name
%_bindir/%name-%version
%{?_enable_docs:%_man1dir/%name.1.*}
%{?_enable_docs:%_man5dir/%{name}*}
%doc CHANGELOG README.md LICENSE

%files -n lib%name
%_libdir/lib%name.so.0*

%exclude %_libdir/*.a

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_libdir/cmake/EditorConfig/
%_pkgconfigdir/%name.pc
%{?_enable_docs:%_man3dir/%{name}*}

%changelog
* Thu Jun 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1.1
- fixed build if "docs" disabled

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- first build for Sisyphus

