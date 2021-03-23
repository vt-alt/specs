%define sover 7

Name: libfmt
Version: 7.1.3
Release: alt1

Summary: An open-source formatting library for C++
License: BSD
Group: System/Libraries
Url: http://fmtlib.net/

# https://github.com/fmtlib/fmt.git
Source: %name-%version.tar

BuildRequires: cmake ctest gcc-c++

%package -n %name%sover
Summary: An open-source formatting library for C++
Group: System/Libraries

%package devel
Summary: An open-source formatting library for C++
Group: Development/C++

%define desc fmt (formerly cppformat) is an open-source formatting library. \
It can be used as a fast and safe alternative to printf and IOStreams.

%description
%desc

%description -n %name%sover
%desc

%description devel
%desc
This package contains development part of fmt.

%prep
%setup

%build
%cmake_insource \
	-DFMT_PKGCONFIG_DIR=%_pkgconfigdir \
	-DBUILD_SHARED_LIBS=ON \
	%nil

%make_build VERBOSE=1

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
make test

%install
%makeinstall_std

%files -n %name%sover
%doc LICENSE* README*
%_libdir/libfmt.so.*

%files devel
%_includedir/fmt
%_libdir/cmake/fmt
%_pkgconfigdir/fmt.pc
%_libdir/libfmt.so

%changelog
* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 7.1.3-alt1
- Updated to upstream version 7.1.3.

* Fri Jun 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.1-alt1
- Updated to upstream version 6.2.1.

* Fri Apr 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2-alt1
- Updated to upstream version 6.1.2.

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.0-alt1
- initial
