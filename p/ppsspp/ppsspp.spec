%define armips_commit 7885552b208493a6a0f21663770c446c3ba65576
%define discord_rpc_commit 3d3ae7129d17643bc706da0a2eea85aafd10ab3a
%define glslang_commit d0850f875ec392a130ccf00018dab458b546f27c
%define ppsspp_ffmpeg_commit 55147e5f33f5ae4904f75ec082af809267122b94
%define ppsspp_lang_commit 1c64b8fbd3cb6bd87935eb53f302f7de6f86e209
%define spirv_cross_commit a1f7c8dc8ea2f94443951ee27003bffa562c1f13

Name: ppsspp
Version: 1.10.3
Release: alt1

Summary: PlayStation Portable Emulator
License: GPL-2.0-or-later
Group: Emulators

Url: https://www.%name.org
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le armh

# https://github.com/hrydgard/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/Kingcom/armips/archive/%armips_commit/armips-%armips_commit.tar.gz
Source1: armips-%armips_commit.tar
# https://github.com/discord/discord-rpc/archive/%discord_rpc_commit/discord-rpc-%discord_rpc_commit.tar.gz
Source2: discord-rpc-%discord_rpc_commit.tar
# https://github.com/hrydgard/glslang/archive/%glslang_commit/glslang-%glslang_commit.tar.gz
Source3: glslang-%glslang_commit.tar
# https://github.com/hrydgard/ppsspp-ffmpeg/archive/%ppsspp_ffmpeg_commit/ppsspp-ffmpeg-%ppsspp_ffmpeg_commit.tar.gz
Source4: ppsspp-ffmpeg-%ppsspp_ffmpeg_commit.tar
# https://github.com/hrydgard/ppsspp-lang/archive/%ppsspp_lang_commit/ppsspp-lang-%ppsspp_lang_commit.tar.gz
Source5: ppsspp-lang-%ppsspp_lang_commit.tar
# https://github.com/KhronosGroup/SPIRV-Cross/archive/%spirv_cross_commit/SPIRV-Cross-%spirv_cross_commit.tar.gz
Source6: SPIRV-Cross-%spirv_cross_commit.tar
Source7: %name.desktop
Source8: %name-qt.desktop

Patch0: %name-alt-git.patch

BuildRequires: cmake
BuildRequires: libGLEW-devel
BuildRequires: libSDL2-devel
BuildRequires: libpng-devel
BuildRequires: libsnappy-devel
BuildRequires: libzip-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: rapidjson

Requires: %name-common = %EVR

%description
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).

%package common
Summary: PPSSPP assets
Group: Emulators
BuildArch: noarch

%description common
Required assets for PPSSPP GUI and assorted configuration files

%package headless
Summary: PlayStation Portable Emulator (headless)
Group: Emulators
Requires: %name-common = %EVR

%description headless
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).
This build headless only.

%package qt
Summary: PlayStation Portable Emulator (Qt frontend)
Group: Emulators
Requires: %name-common = %EVR

%description qt
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).
This build using the Qt frontend.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6

%__mv -Tf ../armips-%armips_commit ext/armips
%__mv -Tf ../discord-rpc-%discord_rpc_commit ext/discord-rpc
%__mv -Tf ../glslang-%glslang_commit ext/glslang
%__mv -Tf ../ppsspp-ffmpeg-%ppsspp_ffmpeg_commit ffmpeg
%__mv -Tf ../ppsspp-lang-%ppsspp_lang_commit assets/lang
%__mv -Tf ../SPIRV-Cross-%spirv_cross_commit ext/SPIRV-Cross

%patch0 -p1

echo "// This is a generated file.

const char *PPSSPP_GIT_VERSION = \"%version\";

// If you don't want this file to update/recompile, change to 1.
#define PPSSPP_GIT_VERSION_NO_UPDATE 1
" > git-version.cpp

%build

# Build SDL and headless versions

%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=TRUE \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
	-DHEADLESS:BOOL=TRUE \
	-DLIBZIP_INCLUDE_DIR=%_includedir \
	-DPNG_LIBRARY=%_libdir/libpng.so \
	-DPNG_PNG_INCLUDE_DIR=%_includedir \
	-DOpenGL_GL_PREFERENCE:STRING=GLVND \
	-Wno-dev
popd

CPLUS_INCLUDE_PATH=%_includedir/libzip %make_build -C %_target_platform

# Build Qt version

%__mkdir_p %_target_platform-qt
pushd %_target_platform-qt

cmake .. \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=TRUE \
	-DUSE_SYSTEM_SNAPPY:BOOL=TRUE \
	-DUSE_SYSTEM_LIBZIP:BOOL=TRUE \
	-DUSING_QT_UI:BOOL=TRUE \
	-DLIBZIP_INCLUDE_DIR=%_includedir \
	-DPNG_LIBRARY=%_libdir/libpng.so \
	-DPNG_PNG_INCLUDE_DIR=%_includedir \
	-DOpenGL_GL_PREFERENCE:STRING=GLVND \
	-Wno-dev
popd

CPLUS_INCLUDE_PATH=%_includedir/libzip %make_build -C %_target_platform-qt

%install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_datadir/%name
%__mkdir_p %buildroot%_pixmapsdir
%__mkdir_p %buildroot%_iconsdir
%__mkdir_p %buildroot%_desktopdir

%__install -Dp -m0755 %_target_platform/PPSSPPSDL %buildroot%_bindir/
%__install -Dp -m0755 %_target_platform/PPSSPPHeadless %buildroot%_bindir/
%__install -Dp -m0755 %_target_platform-qt/PPSSPPQt %buildroot%_bindir/

%__cp -r assets %buildroot%_datadir/%name/

%__cp -r icons/hicolor %buildroot%_iconsdir/

%__install -Dp -m0644 icons/icon-512.svg %buildroot%_pixmapsdir/%name.svg

%__install -Dp -m0644 %SOURCE7 %buildroot%_desktopdir/
%__install -Dp -m0644 %SOURCE8 %buildroot%_desktopdir/

%files
%_bindir/PPSSPPSDL
%_desktopdir/%name.desktop

%files common
%doc LICENSE.TXT README.md
%_datadir/%name
%_pixmapsdir/%name.svg
%_iconsdir/hicolor/*/apps/%name.png

%files headless
%_bindir/PPSSPPHeadless

%files qt
%_bindir/PPSSPPQt
%_desktopdir/%name-qt.desktop

%changelog
* Mon Jul 13 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.3-alt1
- Version 1.10.3

* Tue Jul 07 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.2-alt1
- Version 1.10.2

* Sat Jul 04 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.1-alt1
- Version 1.10.1

* Sat Jun 27 2020 Nazarov Denis <nenderus@altlinux.org> 1.10-alt1
- Version 1.10

* Tue Jun 02 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt4
- Don't gzip sources to speedup rpmbuild -bp

* Tue Jun 02 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt3
- Build also ARMv7hf and MIPS Little Endian

* Fri May 29 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt2
- Add ppsspp-ffmpeg 3dparty library
- Don't use system ffmpeg
- Don't find git package
- Use GLVND

* Thu May 28 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.4-alt1
- Initial build for ALT Linux

