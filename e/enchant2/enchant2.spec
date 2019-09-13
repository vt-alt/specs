%def_disable snapshot
%define _name enchant
%define api_ver 2

%def_enable aspell
%def_disable relocatable
%def_disable check


Name: %_name%api_ver
Version: 2.2.6
Release: alt1

Summary: An Enchanting Spell Checking Program
Group: Text tools
License: LGPL
Url: https://abiword.github.io/%_name/

%if_disabled snapshot
Source: https://github.com/AbiWord/%_name/releases/download/v%version/%_name-%version.tar.gz
%else
#VCS: https://github.com/AbiWord/enchant.git
Source: %_name-%version.tar
%endif

Requires:  lib%name = %version-%release

BuildRequires: gcc-c++ glib2-devel libdbus-glib-devel libhunspell-devel
%{?_enable_aspell:BuildRequires: libaspell-devel}
%{?_enable_check:BuildRequires: libunittest-cpp-devel}

%description
This package contains simple programs that wrap other spell checking backends,
including an Ispell compatible script.

%package -n lib%name
Summary: An Enchanting Spell Checking Library
Group: System/Libraries

%description -n lib%name
A library that wraps other spell checking backends.

%package -n lib%name-devel
Summary: Support files necessary to compile applications with libenchant.
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries, headers, and support files necessary to compile applications
using libenchant.

%prep
%setup -n %_name-%version

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure --disable-static \
	%{subst_enable relocatable} \
	--with-hunspell-dir=%_datadir/myspell \
	%{?_enable_aspell:--with-aspell-dir=%_libdir/aspell}
%make_build pkgdatadir=%_datadir/%_name-%api_ver

%install
%makeinstall_std pkgdatadir=%_datadir/%_name-%api_ver

%check
%make check

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%_datadir/%_name-%api_ver/
%doc AUTHORS README NEWS

%exclude %_libdir/%_name-%api_ver/*.la

%files -n lib%name-devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc

%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.6-alt1
- 2.2.6

* Tue Jul 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt2
- rebuilt with hunspell-1.6.2

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Dec 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Sat Dec 09 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt0.1
- first build for Sisyphus (v2.1.3-10-g6f9d407)

