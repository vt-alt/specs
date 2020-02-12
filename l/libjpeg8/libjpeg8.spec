Name: libjpeg8
Version: 1.5.3
Release: alt1
Summary: The MMX/SSE accelerated JPEG compression/decompression library
License: IJG
Group: System/Libraries
Url: http://sourceforge.net/projects/libjpeg-turbo

Source: http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-%version.tar.gz
Patch: libjpeg-turbo14-noinst.patch
Patch1: libjpeg-turbo-header-files.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: nasm
BuildRequires: gcc

%description
The libjpeg8 package contains a library of functions for manipulating JPEG images.

%prep
%setup -n libjpeg-turbo-%version
%patch -p1
%patch1 -p1
chmod -x README.md

%build
autoreconf -vif
%configure --disable-static --without-turbojpeg --with-jpeg8
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
find %buildroot -name "*.la" -delete

# We need only shared library for this package, so we will remove
# all other installed by default make sequence files.
rm -f %buildroot%_bindir/{cjpeg,djpeg,jpegtran,rdjpgcom,wrjpgcom}
rm -f %buildroot%_libdir/libjpeg.so
rm -rf %buildroot%_pkgconfigdir
rm -rf %buildroot%_includedir
rm -rf %buildroot%_mandir

%files
%doc README.md ChangeLog.md
%doc LICENSE.md README.ijg
%_libdir/libjpeg.so.8*

%changelog
* Mon Feb 03 2020 Leontiy Volodin <lvol@altlinux.org> 1.5.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
