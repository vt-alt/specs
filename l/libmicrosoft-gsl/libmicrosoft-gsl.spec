Name: libmicrosoft-gsl
Version: 2.1.0
Release: alt1
Epoch: 1

Summary: Guidelines Support Library

Group: Development/C++
License: MIT

Url: https://github.com/Microsoft/GSL
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Microsoft/GSL.git
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake ctest catch2-devel >= 2.11.0-alt2

%description
The Guideline Support Library (GSL) contains functions and types that are suggested
for use by the C++ Core Guidelines maintained by the Standard C++ Foundation.
This repo contains Microsoft's implementation of GSL.

The library includes types like span<T>, string_span, owner<> and others.

The entire implementation is provided inline in the headers under the gsl directory.
The implementation generally assumes a platform that implements C++14 support.
There are specific workarounds to support MSVC 2013 and 2015.

While some types have been broken out into their own headers (e.g. gsl/span),
it is simplest to just include gsl/gsl and gain access to the entire library.


%package devel
Group: Development/Other
Summary: Development files for %name
Provides: guidelines-support-library-devel = %version-%release


%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
# adopt to external catch2
%__subst "s|\(add_custom_target(catch)\)|\1\nfind_package(Catch2)|" tests/CMakeLists.txt
%__subst "s|catch/|catch2/|" tests/*.cpp
%__subst "/-Werror/d" tests/CMakeLists.txt

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%check
make test

%files devel
%_includedir/gsl/

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1:2.1.0-alt1
- new version (2.1.0) with rpmgs script
- move headers to include/gsl

* Mon Jun 18 2018 Vitaly Lipatov <lav@altlinux.ru> 20180615-alt1
- Revert "not_null constructor is now explicit (#659)", see #699

* Sun Jun 10 2018 Vitaly Lipatov <lav@altlinux.ru> 20180608-alt1
- build new version

* Sat Jun 02 2018 Vitaly Lipatov <lav@altlinux.ru> 20180315-alt1
- update to v1.0.0

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 20170612-alt1
- initial build for ALT Sisyphus
