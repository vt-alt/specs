Name: dav1d
Version: 0.5.2
Release: alt1

Summary: AV1 cross-platform Decoder
License: BSD
Group: Video

Url: https://code.videolan.org/videolan/dav1d
# Source-url: https://github.com/videolan/dav1d/archive/%version.tar.gz
Source: %name-%version.tar
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires: gcc
BuildRequires: nasm
BuildRequires: doxygen
BuildRequires: meson >= 0.47.0

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package -n libdav1d
Group: Video
Summary: Library files for dav1d

%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package -n libdav1d-devel
Group: Video
Summary: Development files for dav1d
Requires: libdav1d = %EVR

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
%setup

%build
%meson --buildtype=release

%meson_build
%meson_build doc/html

%install
%meson_install

%check
%meson_test

%files
%doc COPYING doc/PATENTS
%doc CONTRIBUTING.md NEWS README.md
%_bindir/dav1d

%files -n libdav1d
%doc COPYING doc/PATENTS
%_libdir/libdav1d.so.*

%files -n libdav1d-devel
%doc %_target_platform/doc/html
%_includedir/%name
%_libdir/libdav1d.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Wed May 08 2019 Michael Shigorin <mike@altlinux.org> 0.3.0-alt2
- fixed build on e2k
- minor spec cleanup

* Mon May 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Mon Apr 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Sisyphus

* Tue Mar 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Rebuild with -Db_ndebug=true

* Tue Mar 12 2019 Robert-André Mauchin - 0.2.1-1
- Release 0.2.1

* Tue Mar 05 2019 Robert-André Mauchin - 0.2.0-1
- Release 0.2.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial build
