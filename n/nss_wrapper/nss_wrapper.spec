Name:           nss_wrapper
Version:        1.1.11
Release:        alt1
License:        BSD
Group:          Development/Other
Summary:        A wrapper for the user, group and hosts NSS API
Url:            https://cwrap.org/

# git://git.samba.org/nss_wrapper.git
Source0:        %{name}-%{version}.tar

BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel

Requires:       cmake
Requires:       pkgconfig

%description
There are projects which provide daemons needing to be able to create, modify
and delete Unix users. Or just switch user ids to interact with the system e.g.
a user space file server. To be able to test that you need the privilege to
modify the passwd and groups file. With nss_wrapper it is possible to define
your own passwd and groups file which will be used by software to act correctly
while under test.

If you have a client and server under test they normally use functions to
resolve network names to addresses (dns) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package doesn't have a devel package cause this project is for
development/testing.

%prep
%setup -q

%build
%cmake \
  -DUNIT_TESTING=ON

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%check
pushd BUILD
%make test
popd

%files
%doc AUTHORS README.md CHANGELOG LICENSE
%_bindir/nss_wrapper.pl
%_libdir/libnss_wrapper.so*
%dir %_libdir/cmake/nss_wrapper
%_libdir/cmake/nss_wrapper/nss_wrapper-config-version.cmake
%_libdir/cmake/nss_wrapper/nss_wrapper-config.cmake
%_libdir/pkgconfig/nss_wrapper.pc
%_mandir/man1/nss_wrapper.1*

%changelog
* Sun Feb 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.1.11-alt1
- Update to latest release.

* Tue Dec 04 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.1.5-alt1
- Update to latest release with compatibility fixes

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt1
- Initial build for ALT.
