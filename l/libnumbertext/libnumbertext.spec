Name: libnumbertext
Version: 1.0.6
Release: alt1
Summary: Number to number name and money text conversion library
Group: Development/C++

License: LGPLv3+
Url: https://github.com/Numbertext/libnumbertext
Source: %name-%version.tar.xz

# Automatically added by buildreq on Mon Aug 20 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel perl python-base python-modules python3 python3-base sh3 xz
BuildRequires: gcc-c++ python3-dev

%description
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package devel
Requires: libnumbertext = %version-%release
Summary: Files for developing with libnumbertext
Group: Development/C++

%description devel
Includes and definitions for developing with libnumbertext

%prep
%setup

%build
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror --with-pic
%make_build

%check
make check

%install
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%_libdir/*.la

%files
%doc AUTHORS ChangeLog README* NEWS THANKS
%_bindir/spellout
%_libdir/*.so.*
%_datadir/libnumbertext

%files devel
%_includedir/libnumbertext
%_libdir/pkgconfig/libnumbertext.pc
%_libdir/*.so

%changelog
* Wed Sep 23 2020 Fr. Br. George <george@altlinux.ru> 1.0.6-alt1
- Autobuild version bump to 1.0.6

* Mon Aug 20 2018 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Mon Aug 20 2018 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build from Fedora

