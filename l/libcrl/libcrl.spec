Name: libcrl
Version: 0.9
Release: alt1

%define soname %version

Summary: Concurrency Runtime Library for Telegram Desktop

Group: Networking/Instant messaging
License: %gpl3only

Url: https://github.com/telegramdesktop/crl
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/telegramdesktop/crl.git
Source: %name-%version.tar
Source1: crl.gyp

BuildRequires: gyp gcc-c++

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5
BuildRequires: qt5-base-devel

%add_optflags -fPIC

%description
Concurrency Runtime Library for Telegram Desktop.

%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
cp %SOURCE1 .
%__subst "s|so\.0\..|so.%version|" crl.gyp

%build
# --no-parallel due gyp in hasher:
#    sl = self._semlock = _multiprocessing.SemLock(kind, value, maxvalue)
#OSError: [Errno 38] Function not implemented
gyp --depth=. --no-parallel
%make_build CXXFLAGS="%optflags -std=c++17 $(pkg-config --cflags Qt5Core)" CFLAGS="%optflags" V=1

cat <<EOF >%name.pc
includedir=%_includedir

Name: %name
Description: %summary
URL: %url
Version: %version
Requires:
Conflicts:
Libs: -lcrl
Libs.private:
Cflags: -I\${includedir}/%name
EOF

%install
install -m644 -D out/Default/lib.target/%name.so.%soname %buildroot%_libdir/%name.so.%soname
install -m644 -D %name.pc %buildroot%_pkgconfigdir/%name.pc
ln -s %name.so.%soname %buildroot%_libdir/%name.so
for i in "" qt dispatch common ; do
    mkdir -p %buildroot%_includedir/%name/crl/$i
    cp -a src/crl/$i/*.h %buildroot%_includedir/%name/crl/$i/
done

%files
%_libdir/%name.so.%soname

%files devel
%_libdir/%name.so
%_includedir/%name/
%_pkgconfigdir/%name.pc

%changelog
* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- merge commit '9ea870038a2a667add7f621be6252db909068386'

* Sun Jun 02 2019 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- merge commit 'd259aebc11df52cb6ff8c738580dc4d8f245d681'

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- merge commit '84072fb'

* Fri Jan 04 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- merge commit '9b7c6b5d9f1b59d2160bf6e9c4e74510f955efe1'

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- compile missed functions

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- merge commit '4291015efab76bda5886a56b5007f4531be17d46'

* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- merge commit '9bc641f2d4ab140a84aea64c7f2d4669f7633246'

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- build next latest commit

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
