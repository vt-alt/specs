Name:    libzim
Version: 5.1.0
Release: alt1
Summary: Library for reading/writing ZIM files

License: GPLv2+
Group:   System/Libraries
URL:     http://openzim.org/wiki/Main_Page
# VCS:   https://github.com/openzim/libzim

Source0: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: liblzma-devel
BuildRequires: libgtest-devel
BuildRequires: zlib-devel
BuildRequires: cmake
BuildRequires: libxapian-devel
BuildRequires: libicu-devel
BuildRequires: python3-dev
BuildRequires: python3-module-Cython

Provides: zimlib = %version-%release

%description
The zimlib is the standard implementation of the ZIM specification. It
is a library which implements the read and write method for ZIM files.
Use zimlib in your own software - like reader applications - to make
them ZIM-capable without the need having to dig too much into the ZIM
file format. zimlib is written in C++. It also includes the binaries
zimsearch and zimdump, for directly searching and viewing ZIM file
contents.

%package  devel
Summary:  Development files for %{name}
Group:    Development/Other
Requires: %name = %version-%release
Provides: zimlib-devel = %version-%release

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS README.md
%_libdir/*.so.*

%files devel
%doc examples
%_includedir/zim/
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Aug 22 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Tue Jul 30 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Wed May 29 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Thu Apr 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version.

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Provide zimlib and zimlib-devel for compatibity with Fedora

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Import to ALT Linux from Fedora
