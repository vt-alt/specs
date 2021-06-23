Name:           resolv_wrapper
Version:        1.1.7
Release:        alt1

Summary:        A wrapper for dns name resolving or dns faking
License:        BSD
Group:          Development/Other
Url:            http://cwrap.org/

# git://git.samba.org/resolv_wrapper.git
Source:        %name-%version.tar

BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel
BuildRequires:  socket_wrapper

Requires:       cmake
Requires:       pkgconfig

%description
It is likely that if you have a server/client architecture, you need to do DNS
queries or a third party library, like Kerberos needs to be able to do queries.
In the case of Kerberos the client needs to look the address of the KDC up via a
SRV record. resolv_wrapper is able to either redirect all DNS queries to your
DNS server implementation, or fake DNS replies!

To use it set the following environment variables:

LD_PRELOAD=libresolv_wrapper.so
RESOLV_WRAPPER_CONF=./my_resolv.conf

This package doesn't have a devel package because this project is for
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
%make test

LD_PRELOAD=src/libpam_wrapper.so bash -c '>/dev/null'
popd

%files
%doc AUTHORS README.md CHANGELOG LICENSE
%_libdir/libresolv_wrapper.so*
%dir %_libdir/cmake/resolv_wrapper
%_libdir/cmake/resolv_wrapper/resolv_wrapper-config-version.cmake
%_libdir/cmake/resolv_wrapper/resolv_wrapper-config.cmake
%_libdir/pkgconfig/resolv_wrapper.pc
%_man1dir/resolv_wrapper.1*

%changelog
* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.1.7-alt1
- Initial build for ALT Sisyphus

