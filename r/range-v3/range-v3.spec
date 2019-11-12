Name: range-v3

Summary: Experimental range library for C++11/14/17
Version: 0.9.1
Release: alt1

License: Boost
Group: Development/C++
Url: https://github.com/ericniebler/range-v3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ericniebler/range-v3/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%description
Header-only %summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Provides: %name-static = %version-%release

%description -n lib%name-devel
Experimental range library for C++11/14/17.

%prep
%setup

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%buildroot%_includedir/%name"
cp -a include/* "%buildroot%_includedir/%name"

%files -n lib%name-devel
%doc README.md CREDITS.md TODO.md
%doc LICENSE.txt
%_includedir/%name

%changelog
* Thu Oct 03 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version 0.4.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3.6-alt1
- new version 0.3.6 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt1
- new version 0.3.5 (with rpmrb script)

* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1.20171112git0b0dd88
- initial build for ALT Sisyphus

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1.20171112git0b0dd88
- Initial SPEC release.
