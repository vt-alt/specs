%global vcglibver 2020.12

Name: meshlab
Version: 2020.12
Release: alt1

Summary: A system for processing and editing unstructured 3D triangular meshes
License: GPLv2+ and BSD and Public Domain
Group: Graphics
Url: https://github.com/cnr-isti-vclab/meshlab

Provides: bundled(vcglib) = %vcglibver

ExcludeArch: armh

# https://github.com/cnr-isti-vclab/meshlab/archive/v%version.tar.gz
Source0: %name-%version.tar
# Probably belongs in its own package, but nothing else seems to depend on it.
# https://github.com/cnr-isti-vclab/vcglib/archive/v%vcglibver.tar.gz
Source1: vcglib-%vcglibver.tar
Source2: meshlab-48x48.xpm

# PATCH-FIX-OPENSUSE -- put shaders in appropriate directories
Patch1: meshlab-2016.12-shader-path.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

BuildRequires: libgomp-devel
BuildRequires: bzlib-devel
BuildRequires: pkgconfig(glew)
#BuildRequires: levmar-devel
BuildRequires: lib3ds-devel
#BuildRequires: libgmp-devel
#BuildRequires: qhull-devel
BuildRequires: qt5-base-devel
BuildRequires: eigen3
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: qt5-declarative-devel
BuildRequires: qtsoap5-devel
#BuildRequires: libmuparser-devel
#BuildRequires: chrpath
BuildRequires: patchelf
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
%ifnarch ppc64le
# mpir has ppc64le excluded
BuildRequires: mpir-devel
%endif

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -a1
%patch1 -p1 -b .shader-path

# Turn of execute permissions on source files to avoid rpmlint
# errors and warnings for the debuginfo package
find . \( -name *.h -o -name *.cpp -o -name *.inl \) -a -executable \
    -exec chmod -x {} \;

rmdir src/vcglib
mv vcglib-%vcglibver src/vcglib

# Remove bundled library sources, since we use the packaged libraries
rm -rf vcglib/wrap/system/multithreading vcglib/wrap/system/*getopt* vcglib/wrap/system/time
#rm -r src/external/{levmar*,lib3ds*,muparser*}

# plugin path
sed -i -e 's|"lib"|"%{_lib}"|g' src/common/pluginmanager.cpp

%ifarch %e2k
# lcc 1.23 only got OpenMP 2.5, hope 1.24 will deliver 5.0
find src/meshlabplugins/filter_screened_poisson/ \
	-type f -print0 -name '*.cpp' -o -name '*.inl' |
	xargs -r0 sed -i '/^#pragma omp/d' --
%endif

%build
pushd src
export CXXFLAGS=`echo %{optflags} -fopenmp`
%cmake
%cmake_build
popd

# process icon
convert %SOURCE2 meshlab.png

# create desktop file
cat <<EOF >meshlab.desktop
[Desktop Entry]
Name=meshlab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;3DGraphics;
EOF

%install
pushd src
%cmakeinstall_std
popd

patchelf --set-rpath %_libdir/meshlab %buildroot/%_bindir/%name \
    %buildroot/%_libdir/%name/plugins/*.so

desktop-file-validate %buildroot%_desktopdir/meshlab.desktop

%files
%doc README.md
%doc docs/readme.txt
%doc docs/privacy.txt
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Sun Jan 10 2021 Anton Midyukov <antohami@altlinux.org> 2020.12-alt1
- 2020.12

* Wed Sep 30 2020 Sergey V Turchin <zerg@altlinux.org> 2016.12-alt8
- fix to build with Qt-5.15
- don't build on armh

* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 2016.12-alt6
- E2K: ftbfs workaround (partially disable OpenMP)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2016.12-alt5
- NMU: remove rpm-build-ubt from BR:

* Thu Feb 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 2016.12-alt4
- no return statement in the non-void function fixed (according g++8)

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2016.12-alt3%ubt
- NMU: fixed build with Qt-5.11.

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 2016.12-alt2%ubt
- Rebuilt for aarch64

* Fri Jan 05 2018 Anton Midyukov <antohami@altlinux.org> 2016.12-alt1%ubt
- New version 2016.12

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt2.2
- Updated build with gcc-6

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt2.1
- rebuild with new version of libmuparser

* Fri May 16 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt2
- i586 build fixed.

* Thu May 15 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt1
- 1.3.3;
- patches revised.

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_1
- converted for ALT Linux by srpmconvert tools

