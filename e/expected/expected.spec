Name: expected
Version: 1.0.0
Release: alt1

Summary: C++11/14/17 std::expected with functional-style extensions

License: CC0
Group: Development/C++
Url: https://github.com/TartanLlama/expected
BuildArch: noarch

# Source-url: https://github.com/TartanLlama/expected/archive/v%version.tar.gz
Source: %name-%version.tar

# Backported upstream patch with cmake fixes.
Patch100: %name-cmake.patch

BuildRequires: ninja-build rpm-macros-ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Header-only C++11/14/17 std::expected with functional-style extensions.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for %name
#Provides: %name-static = %{?epoch:%epoch:}%version-%release

%description -n lib%name-devel
Header-only %summary.

std::expected is proposed as the preferred way to represent objec
which will either have an expected value, or an unexpected value
giving information about why something failed. Unfortunately,
chaining together many computations which may fail can be verbose,
as error-checking code will be mixed in with the actual programming
logic. This implementation provides a number of utilities to make
coding with expected cleaner.

%prep
%setup
%patch100 -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXPECTED_BUILD_TESTS=OFF \
    -DEXPECTED_BUILD_PACKAGE=OFF \
    ..
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files -n lib%name-devel
%doc README.md
%doc COPYING
%_includedir/tl/
%_datadir/cmake/tl-%name

%changelog
* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial SPEC release.
