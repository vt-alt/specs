%define git_ver 8871
%define git_commit 9bcd7b534b7dc9f9c0251c21b15c0ba44d4d1eb6

%define glslang_commit c11e3156af2297f89a23c8db3f5e2323733ee556
%define asmjit_commit fc251c914e77cd079e58982cdab00a47539d7fc5
%define pugixml_commit 8bf806c035373bd0723a85c0820cfd5c804bf6cd
%define hidapi_commit 9220f5e77c27b8b3717b277ec8d3121deeb50242
%define libusb_commit 7cfa00e9d723f10167b4d71bceebf2b4b2cbd70e
%define yaml_cpp_commit eca9cfd64899525d0a61abb0553849676a0fe511
%define xx_hash_commit 7cc9639699f64b750c0b82333dced9ea77e8436e
%define llvm_commit b860b5e8f4ee90d6eb567d83ce8ed1a3e71e496f
%define gsl_commit 1995e86d1ad70519465374fb4876c6ef7c9f8c61
%define cereal_commit 42a45b6e15fcbd1a3d65b033f5d4d0b2ef6c023d

Name: rpcs3
Version: 0.0.7.%git_ver
Release: alt1

Summary: PS3 emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

Source0: https://github.com/RPCS3/%name/archive/%git_commit/%name-%git_commit.tar.gz
Source1: https://github.com/KhronosGroup/glslang/archive/%glslang_commit/glslang-%glslang_commit.tar.gz
Source2: https://github.com/asmjit/asmjit/archive/%asmjit_commit/asmjit-%asmjit_commit.tar.gz
Source3: https://github.com/zeux/pugixml/archive/%pugixml_commit/pugixml-%pugixml_commit.tar.gz
Source4: https://github.com/RPCS3/hidapi/archive/%hidapi_commit/hidapi-%hidapi_commit.tar.gz
Source5: https://github.com/RPCS3/libusb/archive/%libusb_commit/libusb-%libusb_commit.tar.gz
Source6: https://github.com/jbeder/yaml-cpp/archive/%yaml_cpp_commit/yaml-cpp-%yaml_cpp_commit.tar.gz
Source7: https://github.com/Cyan4973/xxHash/archive/%xx_hash_commit/xxHash-%xx_hash_commit.tar.gz
Source8: https://github.com/RPCS3/llvm/archive/%llvm_commit/llvm-%llvm_commit.tar.gz
Source9: https://github.com/microsoft/GSL/archive/%gsl_commit/GSL-%gsl_commit.tar.gz
Source10: https://github.com/USCiLab/cereal/archive/%cereal_commit/cereal-%cereal_commit.tar.gz

BuildRequires: cmake
BuildRequires: cvs
BuildRequires: git-core
BuildRequires: libGLEW-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libevdev-devel
BuildRequires: libopenal-devel
BuildRequires: libpng-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libswscale-devel
BuildRequires: libudev-devel
BuildRequires: libvulkan-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: python3-dev
BuildRequires: qt5-declarative-devel
BuildRequires: subversion

BuildPreReq: libswresample-devel

%description
The world's first free and open-source PlayStation 3 emulator/debugger, written in C++ for Windows and Linux.

%prep
%setup -n %name-%git_commit -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10
%__mv -Tf ../glslang-%glslang_commit Vulkan/glslang
%__mv -Tf ../asmjit-%asmjit_commit asmjit
%__mv -Tf ../pugixml-%pugixml_commit 3rdparty/pugixml
%__mv -Tf ../hidapi-%hidapi_commit 3rdparty/hidapi
%__mv -Tf ../libusb-%libusb_commit 3rdparty/libusb
%__mv -Tf ../yaml-cpp-%yaml_cpp_commit 3rdparty/yaml-cpp
%__mv -Tf ../xxHash-%xx_hash_commit 3rdparty/xxHash
%__mv -Tf ../llvm-%llvm_commit llvm
%__mv -Tf ../GSL-%gsl_commit 3rdparty/GSL
%__mv -Tf ../cereal-%cereal_commit 3rdparty/cereal

#Generate Version Strings
GIT_VERSION=$(echo %git_ver)
GIT_COMMIT=$(echo %git_commit)

echo "// This is a generated file.

#define RPCS3_GIT_VERSION \"$GIT_VERSION-${GIT_COMMIT:0:8}\"
#define RPCS3_GIT_BRANCH \"HEAD\"

// If you don't want this file to update/recompile, change to 1.
#define RPCS3_GIT_VERSION_NO_UPDATE 1
" > %name/git-version.h

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=TRUE \
	-DUSE_NATIVE_INSTRUCTIONS:BOOL=FALSE \
	-DUSE_SYSTEM_FFMPEG:BOOL=TRUE \
	-DUSE_SYSTEM_LIBPNG:BOOL=TRUE
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%dir %_datadir/metainfo
%_datadir/metainfo/%name.appdata.xml

%changelog
* Sun Oct 13 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8871-alt1
- Version 0.0.7.8871

* Sat Oct 12 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8862-alt1
- Version 0.0.7.8862
- Update asmjit to fc251c9
- Update glslang to c11e315
- Update libusb to 7cfa00e

* Wed May 22 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.6.8156-alt1
- Version 0.0.6.8156

* Tue May 21 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.6.8152-alt1
- Version 0.0.6.8152
- Fix post-install unowned files

* Mon May 20 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.6.8147-alt1
- Initial build for ALT Linux

