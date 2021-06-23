%define _unpackaged_files_terminate_build 1

Name: uid_wrapper
Version: 1.2.8
Release: alt1

Summary: A wrapper for privilege separation
License: GPLv3+
Group: Development/Other
Url: http://cwrap.org

# Source-git: git://git.samba.org/uid_wrapper.git
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: libcmocka-devel

%description
Some projects like a file server need privilege separation to be able to switch
to the connection user and do file operations. uid_wrapper convincingly lies
to the application letting it believe it is operating as root and even
switching between UIDs and GIDs as needed.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

This package doesn't have a devel package cause this project is for
development/testing.

%prep
%setup

%build
%cmake \
  -DUNIT_TESTING=ON

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%check
pushd BUILD
LD_LIBRARY_PATH=$(pwd)/tests %make test || \
    { find Testing -name "*.log" | xargs cat; exit 2; }
popd

%files
%doc AUTHORS README.md ChangeLog LICENSE
%_libdir/libuid_wrapper.so*
%dir %_libdir/cmake/uid_wrapper
%_libdir/cmake/uid_wrapper/uid_wrapper-config-version.cmake
%_libdir/cmake/uid_wrapper/uid_wrapper-config.cmake
%_libdir/pkgconfig/uid_wrapper.pc
%_man1dir/uid_wrapper.1*

%changelog
* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.2.8-alt1
- Update to latest release

* Fri Jul 20 2018 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus

