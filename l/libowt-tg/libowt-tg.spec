# https://bugzilla.altlinux.org/show_bug.cgi?id=38832
%def_without packaged_openh264
%def_without packaged_vpx

Name: libowt-tg
Version: 4.3.0.3
Release: alt1

Summary: Open WebRTC Toolkit with Telegram desktop patches

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/desktop-app/tg_owt

# Source-url: https://github.com/desktop-app/tg_owt/archive/master.zip
Source: %name-%version.tar

Patch4: 0001-add-support-for-packaged-libvpx-enabled-via-TG_OWT_V.patch

ExcludeArch: armh

# Automatically added by buildreq on Sun Aug 23 2020
BuildRequires: libalsa-devel libavformat-devel libdb4-devel libjpeg-devel libopus-devel libpulseaudio-devel libssl-devel yasm

BuildRequires: gcc-c++ cmake ninja-build

%if_with packaged_vpx
BuildRequires: libvpx-devel
%endif

%if_with packaged_openh264
BuildRequires: libopenh264-devel
%endif

# TODO: obsoleted in the distro
#BuildRequires: libyuv-devel

#add_optflags -D_FILE_OFFSET_BITS=64
# TODO: enable logging and debugging
#add_optflags -DRTC_DISABLE_LOGGING=1

%description
Open WebRTC Toolkit with Telegram desktop patches.

WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package devel
Summary: Open WebRTC Toolkit library and header files
Group: Development/C
#Requires: %name = %EVR
AutoReq:no
AutoProv:no

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup
#patch4 -p1

%if_with packaged_vpx
rm -rfv src/third_party/libvpx/
%endif

%if_with packaged_openh264
rm -rfv src/third_party/openh264/
mkdir -p src/third_party/openh264/src/codec/api/
ln -s %_includedir/wels src/third_party/openh264/src/codec/api/svc
%__subst "s|.*openh264.*||" CMakeLists.txt
%endif

#rm -rfv src/third_party/libyuv/
#mkdir -p src/third_party/libyuv/
#ln -s %_includedir src/third_party/libyuv/include

%build
%cmake_insource \
          -DCMAKE_BUILD_TYPE=Release \
          -DTG_OWT_SPECIAL_TARGET=linux \
%if_with packaged_vpx
          -DTG_OWT_VPX_PACKAGED_BUILD=TRUE \
%endif
          -DTG_OWT_LIBJPEG_INCLUDE_PATH=%_includedir \
          -DTG_OWT_OPENSSL_INCLUDE_PATH=%_includedir \
          -DTG_OWT_OPUS_INCLUDE_PATH=%_includedir/opus \
          -DTG_OWT_FFMPEG_INCLUDE_PATH=%_includedir \
          ../..
%make_build

%install
%makeinstall_std

%files devel
%_includedir/tg_owt/
%_libdir/libtg_owt.a
%_libdir/cmake/tg_owt/

%changelog
* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.3-alt1
- build from git 1d4f7d74ff1a627db6e45682efd0e3b85738e426
- pack as usual static lib with cmake module

* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.2-alt1
- build from git ceef372ff87c1b6b9ab925cb30ccd00388f8fe73
- build with bundled libvpx

* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.1-alt1
- build from git a4d3a58afda96b4e92426fb464f644205e07acae
- temp. exclude armh arch

* Sat Aug 22 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- build OWT patched for Telegram Desktop
