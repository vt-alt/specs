Name: lib3mf
Version: 2.0.1
Release: alt1

Summary: lib3mf is an implementation of the 3D Manufacturing Format file standard
License: BSD-2-Clause
Group: Graphics
Url: https://github.com/3MFConsortium/lib3mf

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: lib3mf-cmake-adjustments.patch
#Source-url: https://github.com/3MFConsortium/lib3mf/archive/v%version/lib3mf-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: act

# fot tests
#BuildRequires: libgtest-devel
#BuildRequires: ctest

%description
lib3mf is a C++ implementation of the 3D Manufacturing Format standard.
This is a 3D printing standard for representing geometry as meshes.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
lib3mf is a C++ implementation of the 3D Manufacturing Format standard.
This is a 3D printing standard for representing geometry as meshes.

%prep
%setup
%patch -p1

# Set version
%__subst 's|@PROJECT_VERSION@|%version|' lib3MF.pc.in 

# A bundled x86 executable, we use the packaged one instead
# https://github.com/3MFConsortium/lib3mf/issues/199
rm AutomaticComponentToolkit/bin/act.linux
ln -s %_bindir/act AutomaticComponentToolkit/bin/act.linux

%build
%cmake_insource -DLIB3MF_TESTS=OFF
%make_build

%install
%makeinstall_std

# https://github.com/3MFConsortium/lib3mf/issues/8#issuecomment-605931967
mkdir -p %buildroot%_includedir/%name
mv -n %buildroot%_includedir/Bindings/*/*.{h,hpp} %buildroot%_includedir/%name
rm -rf %buildroot%_includedir/Bindings

# Also include the other headers
cp -a Include/* %buildroot%_includedir/%name/
# ...but not the 3rd party libraries
rm -r %buildroot%_includedir/%name/Libraries

# Match Debian
%__subst 's|include$|include/%name|' %buildroot%_pkgconfigdir/lib3MF.pc

%check
#make_build test

%files
%doc README.md
%doc LICENSE
%_libdir/%name.so.2
%_libdir/%name.so.%version.0

%files devel
%_libdir/%name.so
%_includedir/%name/
%_pkgconfigdir/lib3MF.pc

%changelog
* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build
