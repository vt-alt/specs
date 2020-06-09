# TODO: build json11 separately

# see LIBTGVOIP_VERSION in VoIPController.h for a version

%def_without json11

Name: libtgvoip
Version: 2.4.4
Release: alt4.d2e6342

Summary: VoIP library for Telegram clients

Group: Networking/Instant messaging
License: Public Domain and BSD

Url: https://github.com/telegramdesktop/libtgvoip
Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-git: https://github.com/grishka/libtgvoip.git
# Source-git: https://github.com/telegramdesktop/libtgvoip.git
Source: %name-%version.tar

Patch1: libtgvoip-system-json11.patch

# TODO:
# from webrtc_dsp/modules/audio_processing/aec/aec_core_sse2.cc:17:
# /usr/lib/gcc/i586-alt-linux/9/include/xmmintrin.h:932:1: error: inlining failed in call to always_inline '__m128 _mm_loadu_ps(const float*)': target specific option mismatch
#  932 | _mm_loadu_ps (float const *__P)
%ifarch %ix86
%add_optflags -msse2
%endif

BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libalsa-devel libpulseaudio-devel
# >= 1.3
BuildRequires: libopus-devel

%description
VoIP library for Telegram clients.
Dinamically loads libalsa or libpulse.


%package devel
Group: Development/Other
Summary: Development files for %name
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup

%if_with json11
%patch1 -p1
# remove bundled json11
rm -vf json11.*
%endif

%__subst "s|-std=gnu++0x|-std=gnu++17|" Makefile.am

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libtgvoip.so.*

%files devel
%doc UNLICENSE
%_libdir/libtgvoip.so
%dir %_includedir/tgvoip/
%_includedir/tgvoip/*.h
%if_without json11
%_includedir/tgvoip/json11.hpp
%endif
%_includedir/tgvoip/audio/
%_includedir/tgvoip/video/
%_includedir/tgvoip/os/
%_pkgconfigdir/tgvoip.pc

%changelog
* Thu Jun 04 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt4.d2e6342
- update to the latest repo commit d2e63429ec94ee178a62b55be01f1cca98e9de83
  from https://github.com/telegramdesktop/libtgvoip
- switch to -std=gnu++17

* Mon May 11 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt3.dc4e9ec
- update to the latest repo commit dc4e9ec48207388e41db1c2ef1cccf9899d9765f
  from https://github.com/telegramdesktop/libtgvoip

* Sat Jan 25 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt2.c5651ffc72
- update to the latest repo commit c5651ffc728336e56d8567f5c6c179e8a5d4fe55
- rewrite spec, use autoconf
- pkg-config name is changed from libtgvoip to tgvoip
- soname is changed
- disable build on ppc64le

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Tue Jan 15 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Tue Dec 11 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt2
- real 2.4 release (tagged release from grishka@)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4 - merge with 78e584c443b93ce2 (used in TG 1.5.0)
- pack include/tgvoip/video/

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version (2.2.4) from upsteam git
 + added --enable-audio-callback to configure
 + fixes

* Wed Aug 29 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt2
- rebuild with openssl 1.1

* Thu Aug 23 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new verson (2.2.2)
 + Refactored audio I/O to allow sharing a common context between input and output
 + Rewritten periodic operation handling to use a "run loop" thingy
 + Fixed a bunch of compiler warnings (closes #13)

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version (2.1.1) with rpmgs script
 + Enabled delay-agnostic AEC on Windows & Linux, it seems to make a difference after all (telegramdesktop/tdesktop#4881)
 + Fixed PulseAudio crashes, at least I hope so (closes #42)
 + Fixed parsing of floating-point server config values in some locales in Linux

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- build new version

* Mon May 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.18t-alt2
- Sync with telegram submodule: Update libtgvoip to fix a possible crash

* Sun May 27 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.18t-alt1
- build new version (latests code from tdesktop)

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.1-alt1
- update to last git commit https://github.com/telegramdesktop/libtgvoip tdesktop

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1.2-alt1
- add pkgconfig file

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1.1-alt1
- update to last git commit
- fix soname

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- rebuild with debuginfo (ALT bug 33544)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- initial build for ALT Sisyphus
