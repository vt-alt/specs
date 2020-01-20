%define git_ver 9300
%define git_commit 341fdf7eb14763fd06e2eab9a4b2b8f1adf9fdbd

%define glslang_version 7.13.3496
%define asmjit_commit fc251c914e77cd079e58982cdab00a47539d7fc5
%define pugixml_commit 8bf806c035373bd0723a85c0820cfd5c804bf6cd
%define hidapi_commit 9220f5e77c27b8b3717b277ec8d3121deeb50242
%define libusb_commit 7cfa00e9d723f10167b4d71bceebf2b4b2cbd70e
%define yaml_cpp_commit eca9cfd64899525d0a61abb0553849676a0fe511
%define xx_hash_version 0.6.5
%define llvm_commit 2e038bff1082175b510a2e8336edf897af9b87a3
%define cereal_version 1.2.0
%define faudio_version 19.10
%define span_commit 9d7559aabdebf569cab3480a7ea2a87948c0ae47

Name: rpcs3
Version: 0.0.8
Release: alt2

Summary: PS3 emulator/debugger
License: GPLv2
Group: Emulators

Url: https://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: glslang-%glslang_version.tar
Source2: asmjit-%asmjit_commit.tar
Source3: pugixml-%pugixml_commit.tar
Source4: hidapi-%hidapi_commit.tar
Source5: libusb-%libusb_commit.tar
Source6: yaml-cpp-%yaml_cpp_commit.tar
Source7: xxHash-%xx_hash_version.tar
Source8: llvm-%llvm_commit.tar
Source9: cereal-%cereal_version.tar
Source10: FAudio-%faudio_version.tar
Source11: span-%span_commit.tar

BuildRequires: cmake
BuildRequires: cvs
BuildRequires: git-core
BuildRequires: libGLEW-devel
BuildRequires: libSDL2-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libevdev-devel
BuildRequires: libfaudio-devel
BuildRequires: libopenal-devel
BuildRequires: libpng-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libswscale-devel
BuildRequires: libudev-devel
BuildRequires: libvulkan-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwayland-server-devel
BuildRequires: libxml2-devel
BuildRequires: rpm-build-python3 python3-devel python3-module-yaml python3-module-Pygments
BuildRequires: qt5-declarative-devel
BuildRequires: subversion

BuildPreReq: libswresample-devel

%description
The world's first free and open-source PlayStation 3 emulator/debugger, written in C++ for Windows and Linux.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11
%__mv -Tf ../glslang-%glslang_version Vulkan/glslang
%__mv -Tf ../asmjit-%asmjit_commit asmjit
%__mv -Tf ../pugixml-%pugixml_commit 3rdparty/pugixml
%__mv -Tf ../hidapi-%hidapi_commit 3rdparty/hidapi
%__mv -Tf ../libusb-%libusb_commit 3rdparty/libusb
%__mv -Tf ../yaml-cpp-%yaml_cpp_commit 3rdparty/yaml-cpp
%__mv -Tf ../xxHash-%xx_hash_version 3rdparty/xxHash
%__mv -Tf ../llvm-%llvm_commit llvm
%__mv -Tf ../cereal-%cereal_version 3rdparty/cereal
%__mv -Tf ../FAudio-%faudio_version 3rdparty/FAudio
%__mv -Tf ../span-%span_commit 3rdparty/span

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
	-DUSE_SYSTEM_LIBPNG:BOOL=TRUE \
	-DPYTHON_EXECUTABLE="%__python3" \
	#
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
* Sat Jan 04 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt2
- Update glslang to 7.13.3496

* Fri Jan 03 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt1.1
- build with python3
- don't gzip sources

* Thu Jan 02 2020 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt1
- Version 0.0.8

* Thu Dec 26 2019 Sergey V Turchin <zerg@altlinux.org> 0.0.7.9212-alt1.1
- build with python3
- don't gzip sources

* Tue Dec 24 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9250-alt1
- Version 0.0.7.9250

* Sat Dec 07 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9212-alt1
- Version 0.0.7-9212

* Wed Nov 27 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9180-alt1
- Version 0.0.7.9180

* Fri Nov 15 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9135-alt1
- Version 0.0.7.9135

* Tue Nov 12 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9123-alt1
- Version 0.0.7.9123

* Mon Nov 11 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9122-alt1
- Version 0.0.7.9122
- Remove GSL package
- Add span package in 3rdparty

* Sat Nov 09 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9095-alt1
- Version 0.0.7.9095

* Fri Nov 08 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9086-alt1
- Version 0.0.7.9086
- Change commits to version on 3rdparty packages (if possible)

* Sun Nov 03 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9061-alt1
- Version 0.0.7.9061
- Add FAudio in 3rdparty
- Update build requires

* Thu Oct 31 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.9053-alt1
- Version 0.0.7.9053

* Wed Oct 23 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8990-alt1
- Version 0.0.7.8990
- Update LLVM to 9836c29

* Mon Oct 21 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8963-alt1
- Version 0.0.7.8963

* Sat Oct 19 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8935-alt1
- Version 0.0.7.8935

* Tue Oct 15 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8896-alt1
- Version 0.0.7.8896

* Mon Oct 14 2019 Nazarov Denis <nenderus@altlinux.org> 0.0.7.8886-alt1
- Version 0.0.7.8886

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

