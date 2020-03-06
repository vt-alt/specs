%global richname QR-Code-generator

%global commit0 67c62461d380352500fc39557fd9f046b7fe1d18
%global shortcommit0 %(c=%commit0; echo ${c:0:7})

Name: libqrcodegen
Version: 1.5.0
Release: alt1.git%shortcommit0

Summary: High-quality QR Code generator library

License: MIT
Group: System/Libraries
Url: https://github.com/nayuki/QR-Code-generator

# Source0-url: %url/archive/%commit0/%name-%shortcommit0.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# https://github.com/nayuki/QR-Code-generator/pull/72
Patch1: qr-code-generator-build-fixes.patch

BuildRequires: python3-devel
BuildRequires: gcc-c++

%description
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package devel
Group: Development/C
Summary: Development files for libqrcodegen
Requires: libqrcodegen = %EVR

%description devel
Development files and headers for high-quality QR Code generator library
(plain C version).

%package -n libqrcodegen-cpp
Group: System/Libraries
Summary: High-quality QR Code generator library (C++ version)

%description -n libqrcodegen-cpp
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen-cpp-devel
Group: Development/C++
Summary: Development files for libqrcodegencpp
Requires: libqrcodegen-cpp = %EVR

%description -n libqrcodegen-cpp-devel
Development files and headers for high-quality QR Code generator library
(C++ version).

%package -n python3-module-qrcodegen
Group: Development/Python
Summary: High-quality QR Code generator library (Python version)
BuildArch: noarch

%description -n python3-module-qrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%prep
%setup
%patch1 -p1

%build
# Building plain C version...
pushd c
%make_build
popd

# Building C++ version...
pushd cpp
%make_build
popd

# Building Python version...
pushd python
%python3_build
popd

%install
# Installing plain C version...
pushd c
%make_install install LIBDIR=%buildroot%_libdir INCLUDEDIR=%buildroot%_includedir/qrcodegen
popd

# Installing C++ version...
pushd cpp
%make_install install LIBDIR=%buildroot%_libdir INCLUDEDIR=%buildroot%_includedir/qrcodegencpp
popd

# Installing Python version...
pushd python
%python3_install
popd

%files
%doc Readme.markdown
%_libdir/libqrcodegen.so.1*

%files devel
%_includedir/qrcodegen/
%_libdir/libqrcodegen.so

%files -n libqrcodegen-cpp
%doc Readme.markdown
%_libdir/libqrcodegencpp.so.1*

%files -n libqrcodegen-cpp-devel
%_includedir/qrcodegencpp/
%_libdir/libqrcodegencpp.so

%files -n python3-module-qrcodegen
%doc Readme.markdown
%python3_sitelibdir_noarch/qrcodegen.py
%python3_sitelibdir_noarch/__pycache__/*
%python3_sitelibdir_noarch/qrcodegen-*.egg-info/

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1.git67c6246
- initial build for ALT Sisyphus

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1.20191014git67c6246
- Initial SPEC release.
