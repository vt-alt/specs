%define _unpackaged_files_terminate_build 1

# Opentoonz libraries are located in non-standard path.
# Launching scripts sets LD_LIBRARY_PATH
%set_verify_elf_method unresolved=relaxed

Name: opentoonz
Version: 1.4.0
Release: alt3
Summary: 2D animation software
Group: Graphics
License: BSD-3-Clause and CC0-1.0 and ALT-Public-Domain and libtiff and CC-BY-NC-4.0
URL: https://opentoonz.github.io/e/

ExcludeArch: armh

# https://github.com/opentoonz/opentoonz.git
Source: %name-%version.tar

# https://github.com/opentoonz/opentoonz_docs.git
Source1: %name-%version-docs.tar

# https://github.com/opentoonz/opentoonz_sample.git
Source2: %name-%version-sample.tar

# NOTE: on each update pull updates to docs and samples

Patch1: %name-%version-alt-return-type.patch
Patch2: %name-%version-alt-libraries-path.patch
Patch3: %name-%version-alt-data-location.patch
Patch4: opensuse-0001-Fix-linker-errors-on-Linux.patch
Patch5: opensuse-0001-Use-the-system-mypaint-brushes.patch
Patch6: %name-%version-alt-qt5-compat.patch
Patch7: %name-%version-upstream-gcc10-compat.patch
Patch8: %name-%version-upstream-glibc-compat.patch

BuildRequires: gcc-c++ cmake
BuildRequires: boost-complete
BuildRequires: libGLEW-devel
BuildRequires: libfreeglut-devel
BuildRequires: libjpeg-devel
BuildRequires: libturbojpeg-devel
BuildRequires: libmypaint-devel
BuildRequires: libpng-devel
BuildRequires: libusb-devel
BuildRequires: liblz4-devel
BuildRequires: liblzo2-devel
BuildRequires: liblapack-devel
BuildRequires: libsuperlu-devel
BuildRequires: zlib-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: libfreetype-devel
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3(sphinx_rtd_theme)

Requires: mypaint-brushes1.0

%description
OpenToonz is a 2D animation software published by
DWANGO (http://dwango.co.jp/english/).
It is based on Toonz Studio Ghibli Version,
originally developed in Italy by Digital Video, Inc. (http://www.toonz.com/),
and customized by Studio Ghibli (http://www.ghibli.jp/)
over many years of production.

%package doc
Summary: OpenToonz documentation and samples
Group: Development/Documentation
BuildArch: noarch

%description doc
OpenToonz is a 2D animation software published by
DWANGO (http://dwango.co.jp/english/).
It is based on Toonz Studio Ghibli Version,
originally developed in Italy by Digital Video, Inc. (http://www.toonz.com/),
and customized by Studio Ghibli (http://www.ghibli.jp/)
over many years of production.

This package contains documentation and samples for OpenToonz.

%prep
%setup -a1 -a2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# prevent using unbundled libraries
# don't unbundle libtiff because it's patched. See: https://github.com/opentoonz/opentoonz/blob/master/doc/how_to_build_linux.md#building-libtiff
rm -rf thirdparty/{boost,glew,glut,LibJPEG,libjpeg-turbo64,libmypaint,libpng-1.6.21,libusb,Lz4,lzo/2.03,openblas,quicktime,superlu,zlib-1.2.8}

%build
# build patched libtiff
pushd thirdparty/tiff-4.0.3
%configure \
	--with-pic \
	--disable-jbig \
	--enable-static \
	--disable-shared \
	%nil

%make_build
popd

# build opentoonz
pushd toonz/sources
%cmake \
	-DTIFF_LIBRARY="%_builddir/%name-%version/thirdparty/tiff-4.0.3/libtiff/.libs/libtiff.a" \
	%nil

%cmake_build
popd

# build opentoonz plugins
for i in plugins/{blur,geom,multiplugin} ; do
pushd $i
%cmake
%cmake_build
popd
done

# build opentoonz documentation
pushd additional/docs
%make html
popd

%install
# install opentoonz
pushd toonz/sources
%cmakeinstall_std
popd

# install opentoonz plugins
for i in plugins/{blur,geom,multiplugin} ; do
pushd $i
install BUILD/*.plugin %buildroot%_libdir/%name/stuff/plugins/
popd
done

%files
%doc LICENSE.txt
%doc README.md
%_bindir/*
%_libdir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml

%files doc
%doc additional/docs/build/html
%doc additional/sample

%changelog
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt3
- Fixed build with new toolchain.

* Fri Aug 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt2
- Fixed build with qt-5.15.0.

* Thu Jul 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Initial build for ALT
