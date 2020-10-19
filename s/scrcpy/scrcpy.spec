# Switch which helps to rebuild server jar with
# nonfree Android SDK.  Don't forget to enable
# newtwork sharing in hasher-priv.
%def_disable build_server

Name: scrcpy
Version: 1.16
Release: alt1
Summary: Display and control your Android device screen
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/Genymobile/scrcpy
# Repacked: https://github.com/Genymobile/scrcpy/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar

# Prebuilt .jar with --enable build_server .
Source1: scrcpy-server.jar

%if_enabled build_server
# Android SDK is not free and is not redistributable.
# If you want to build server application download it here:
# https://developer.android.com/studio#downloads
Source2: commandlinetools-linux-6609375_latest.zip

BuildPreReq: java-devel unzip
%endif

BuildRequires(pre): meson
# Automatically added by buildreq on Fri May 29 2020
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavutil-devel libcairo-gobject libgdk-pixbuf libglvnd-devel libopencore-amrnb0 libopencore-amrwb0 libp11-kit libx265-176 ninja-build pkg-config python2-base python3 python3-base python3-module-pkg_resources sh4 xz
BuildRequires: libSDL2-devel libavformat-devel meson

Requires: android-tools

%description
This application provides display and control of Android devices connected on
USB (or over TCP/IP).  It does not require any root access.

%prep
%setup
%if_enabled build_server
mkdir -p android-sdk
cd android-sdk
unzip %SOURCE2
%endif

%build
%if_enabled build_server
export ANDROID_SDK_ROOT=$PWD/android-sdk
yes | $ANDROID_SDK_ROOT/tools/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT --licenses
%meson \
%else
%meson \
	-Dprebuilt_server=%SOURCE1 \
%endif
	#
%meson_build

%install
%if_enabled build_server
export ANDROID_SDK_ROOT=$PWD/android-sdk
%endif
%meson_install

%files
%doc README.md DEVELOP.md FAQ.md LICENSE
%_bindir/%name
%_datadir/%name
%_mandir/man1/scrcpy.1.*

%changelog
* Mon Oct 12 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.16-alt1
- Updated to v1.16.
- Fixed package summary and description.

* Fri May 29 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.14-alt1
- Initial build.
