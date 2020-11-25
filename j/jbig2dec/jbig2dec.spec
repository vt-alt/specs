%define _unpackaged_files_terminate_build 1

Name:           jbig2dec
Version:        0.19
Release:        alt1
Summary:        A decoder implementation of the JBIG2 image compression format 
Summary(ru_RU.UTF-8): Декодер формата изображений JBIG2
License:        AGPL-3.0+
Group: Graphics
URL:            http://jbig2dec.sourceforge.net/

Source:         %name-%version.tar

# Automatically added by buildreq on Sun Apr 15 2012
# optimized out: zlib-devel
BuildRequires: libpng-devel

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

%package  -n lib%name
Summary: A decoder implementation of the JBIG2 image compression format
Summary(ru_RU.UTF-8): Библиотека, реализующая декодер формата изображений JBIG2
Group: System/Libraries

%description -n lib%name
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package provides the shared jbig2dec library.

%package -n lib%name-devel
Summary:  Static library and header files for development with jbig2dec
Summary(ru_RU.UTF-8): Заголовочные файлы библиотеки, реализующей декодер формата изображений JBIG2
Group:    Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package is only needed if you plan to develop or compile applications
which requires the jbig2dec library.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_libdir/*.la

%files
%doc CHANGES COPYING LICENSE README
%_bindir/jbig2dec
%_man1dir/jbig2dec.1*

%files -n lib%name-devel
%doc CHANGES COPYING LICENSE README
%_includedir/jbig2.h
%_libdir/libjbig2dec.so
%_pkgconfigdir/*.pc

%files -n lib%name
%doc CHANGES COPYING LICENSE README
%_libdir/libjbig2dec.so.0
%_libdir/libjbig2dec.so.0.0.0

# TODO:
# - consider debian patches

%changelog
* Fri Nov 20 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19-alt1
- Updated to upstream version 0.19 (Fixes: CVE-2016-9601, CVE-2020-12268).

* Thu Mar 02 2017 Michael Shigorin <mike@altlinux.org> 0.11-alt0.2.2
- Fixed manpage name.

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt0.2.1
- Rebuilt with libpng15

* Mon Apr 16 2012 Andrey Bergman <vkni@altlinux.org> 0.11-alt0.2
- Renamed devel package.

* Sun Apr 15 2012 Andrey Bergman <vkni@altlinux.org> 0.11-alt0.1
- Initial port from Fedora.

