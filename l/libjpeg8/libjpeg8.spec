Name: libjpeg8
Version: 2.0.5
Release: alt1
Summary: The MMX/SSE accelerated JPEG compression/decompression library
License: IJG and BSD-3-Clause and Zlib
Group: System/Libraries
Url: http://sourceforge.net/projects/libjpeg-turbo

Source: https://sourceforge.net/projects/libjpeg-turbo/files/%version/libjpeg-turbo-%version.tar.gz
Patch: libjpeg-turbo14-noinst.patch
Patch1: libjpeg-turbo-header-files.patch
Patch11: libjpeg-turbo-alt-header-files.patch

BuildRequires: cmake gcc

%description
The libjpeg8 package contains a library of functions for manipulating JPEG images.

%prep
%setup -n libjpeg-turbo-%version
%patch11 -p2
chmod -x README.md

%build
%cmake_insource \
    -DENABLE_STATIC=false \
    -DWITH_TURBOJPEG=false \
    -DWITH_JPEG8=true
%make_build

%install
%makeinstall_std
find %buildroot -name "*.la" -delete

# We need only shared library for this package, so we will remove
# all other installed by default make sequence files.
rm -f %buildroot%_bindir/{cjpeg,djpeg,jpegtran,rdjpgcom,wrjpgcom}
rm -f %buildroot%_libdir/libjpeg.so
rm -rf %buildroot%_pkgconfigdir
rm -rf %buildroot%_includedir
rm -rf %buildroot%_mandir
# Packaged using %%doc
rm -rf %buildroot%_datadir/doc/libjpeg-turbo

%files
%doc README.md ChangeLog.md LICENSE.md README.ijg
%_libdir/libjpeg.so.8*

%changelog
* Thu Jun 25 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version (2.0.5) with rpmgs script.
- Updated license tag.
- Fixes:
  + CVE-2020-13790.

* Tue Feb 04 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- New version (2.0.4) with rpmgs script.
- Built with cmake.
- Updated source link.

* Mon Feb 03 2020 Leontiy Volodin <lvol@altlinux.org> 1.5.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
