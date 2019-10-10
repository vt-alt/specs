
%def_without jemalloc
%def_without java
%def_with snappy
%def_with lz4
%def_with zlib
%def_with bzip2
%def_with zstd
%def_with tbb
%def_with numa
%def_without rocksdb_lite

Name: rocksdb
Version: 6.1.2
Release: alt1
Summary: A Persistent Key-Value Store for Flash and RAM Storage
Group: Databases
License: BSD
Url: https://github.com/facebook/rocksdb.git
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: gcc-c++
BuildRequires: libgtest-devel  cmake
%{?_with_jemalloc:BuildRequires: libjemalloc-devel}
%{?_with_java:BuildRequires: java-devel}
%{?_with_snappy:BuildRequires: libsnappy-devel}
%{?_with_lz4:BuildRequires: liblz4-devel}
%{?_with_zlib:BuildRequires: zlib-devel}
%{?_with_bzip2:BuildRequires: bzlib-devel}
%{?_with_zstd:BuildRequires: libzstd-devel}
%{?_with_tbb:BuildRequires: tbb-devel}
%{?_with_numa:BuildRequires: libnuma-devel}

%description
Rocksdb is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multithreaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package -n lib%name
Summary: A Persistent Key-Value Store for Flash and RAM Storage
Group: System/Libraries

%description -n lib%name
Rocksdb is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multithreaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package -n lib%name-devel
Summary: Development files for rocksdb
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for rocksdb

%package -n lib%name-devel-static
Summary: Static library for rocksdb
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
Static library for rocksdb

%prep
%setup
%patch -p1

#rm -rf third-party/gtest-1.7.0
#rm java/benchmark/src/main/java/org/rocksdb/benchmark/DbBenchmark.java
rm build_tools/gnu_parallel

%build
%cmake \
    %{?_with_jemalloc:-DWITH_JEMALLOC:BOOL=ON} \
    %{?_with_java:-DWITH_JNI:BOOL=ON} \
    %{?_with_snappy:-DWITH_SNAPPY:BOOL=ON} \
    %{?_with_zlib:-DWITH_ZLIB:BOOL=ON} \
    %{?_with_lz4:-DWITH_LZ4:BOOL=ON} \
    %{?_with_bzip2:-DWITH_BZ2:BOOL=ON} \
    %{?_with_zstd:-DWITH_ZSTD:BOOL=ON} \
    %{?_with_rocksdb_lite:-DROCKSDB_LITE:BOOL=ON} \
    -DPORTABLE:BOOL=ON

#export EXTRA_CFLAGS="-fPIC"
#export EXTRA_CXXFLAGS="-fPIC"
%cmake_build

#export PORTABLE="1"
#%%make_build static_lib
#%%make_build shared_lib

%install
%cmakeinstall_std
#%%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Mon Oct 07 2019 Alexey Shabalin <shaba@altlinux.org> 6.1.2-alt1
- 6.1.2

* Thu Feb 28 2019 Alexey Shabalin <shaba@altlinux.org> 5.17.2-alt1
- 5.17.2

* Fri Oct 26 2018 Alexey Shabalin <shaba@altlinux.org> 5.14.3-alt1
- 5.14.3
- build with PORTABLE=ON

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 5.13.3-alt1%ubt
- 5.13.3

* Wed Jun 06 2018 Alexey Shabalin <shaba@altlinux.ru> 5.8.8-alt1%ubt
- 5.8.8

* Thu Dec 07 2017 Alexey Shabalin <shaba@altlinux.ru> 5.7.5-alt1%ubt
- 5.7.5

* Mon Sep 25 2017 Alexey Shabalin <shaba@altlinux.ru> 5.7.4-alt1
- 5.7.4

* Wed Sep 20 2017 Alexey Shabalin <shaba@altlinux.ru> 5.7.3-alt1
- Initial build
