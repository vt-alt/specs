%def_disable nacl
%def_enable  clang
%def_disable shared_libraries
%def_enable  widevine
%def_enable  ffmpeg
%def_enable  google_api_keys

%ifndef build_parallel_jobs
%global build_parallel_jobs %__nprocs
%endif

%define is_enabled() %{expand:%%{?_enable_%{1}:true}%%{!?_enable_%{1}:false}}

%global gcc_version %nil
#set_gcc_version %gcc_version

%set_verify_elf_method rpath=relaxed textrel=relaxed lfs=relaxed lint=relaxed

# Leave this alone, please.
%global target out/Release

# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys .
# Note: these are for ALT Linux use ONLY. For your own distribution,
# please get your own set of keys.
%define api_key               AIzaSyAIIWz7zaCwYcUSe3ZaRPviXjMjkBP4-xY
%define default_client_id     1018394967181.apps.googleusercontent.com
%define default_client_secret h_PrTP1ymJu83YTLyz-E25nP

Name:           chromium
Version:        76.0.3809.87
Release:        alt1

Summary:        An open source web browser developed by Google
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Url:            http://www.chromium.org

Source0:        chromium.tar.zst
Source1:        depot_tools.tar

Source30:       master_preferences
Source31:       default_bookmarks.html
Source100:      chromium.sh
Source101:      chromium.desktop
Source102:      chromium.xml
Source200:      chromium.default

Provides:       chromium-browser = %version
Obsoletes:      chromium-browser < %version
Obsoletes:      chromium-stable <= %version

# Unsupported target_cpu
ExcludeArch: ppc64le

### Start Patches
Patch001: 0001-OPENSUSE-enables-reading-of-the-master-preference.patch
Patch002: 0002-OPENSUSE-Compile-the-sandbox-with-fPIE-settings.patch
Patch003: 0003-ALT-Set-appropriate-desktop-file-name-for-default-br.patch
Patch004: 0004-DEBIAN-manpage-fixes.patch
Patch005: 0005-DEBIAN-change-icon.patch
Patch006: 0006-ALT-gcc6-fixes.patch
Patch007: 0007-DEBIAN-disable-third-party-cookies-by-default.patch
Patch008: 0008-DEBIAN-add-ps-printing-capability-gtk2.patch
Patch009: 0009-ALT-fix-shrank-by-one-character.patch
Patch010: 0010-DEBIAN-10-seconds-may-not-be-enough-so-do-not-kill-t.patch
Patch011: 0011-FEDORA-path-max.patch
Patch012: 0012-FEDORA-Ignore-broken-nacl-open-fd-counter.patch
Patch013: 0013-ALT-Fix-last-commit-position-issue.patch
Patch014: 0014-FEDORA-Fix-issue-where-timespec-is-not-defined-when-.patch
Patch015: 0015-ALT-Use-rpath-link-and-absolute-rpath.patch
Patch016: 0016-Enable-VAVDA-VAVEA-and-VAJDA-on-linux-with-VAAPI-onl.patch
Patch017: 0017-FEDORA-Fix-gcc-round.patch
Patch018: 0018-FEDORA-Fix-memcpy.patch
Patch019: 0019-ALT-openh264-always-pic-on-x86.patch
Patch020: 0020-ALT-allow-to-override-clang-through-env-variables.patch
Patch021: 0021-ALT-Hack-to-avoid-build-error-with-clang7.patch
Patch022: 0022-ALT-Add-missing-header-on-aarch64.patch
### End Patches

BuildRequires: /proc

BuildRequires:  bison
BuildRequires:  bzlib-devel
BuildRequires:  flex
BuildRequires:  chrpath
BuildRequires:  gcc%gcc_version-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++-devel-static
BuildRequires:  glibc-kernheaders
%if_enabled clang
BuildRequires:  clang7.0
BuildRequires:  clang7.0-devel
BuildRequires:  llvm7.0-devel
BuildRequires:  lld-devel
%endif
BuildRequires:  ninja-build
BuildRequires:  gperf
BuildRequires:  libcups-devel
BuildRequires:  perl-Switch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
%if_enabled ffmpeg
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  python
BuildRequires:  python-modules-json
BuildRequires:  python-modules-distutils
BuildRequires:  node
BuildRequires:  usbids
BuildRequires:  xdg-utils

Provides:       webclient, /usr/bin/xbrowser

Requires: libva

%description
Chromium is an open-source browser project that aims to build a safer,
faster, and more stable way for all Internet users to experience the web.

%package kde
Summary:        Update to chromium to use KDE's kwallet to store passwords
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Conflicts:      chromium-gnome
Conflicts:      chromium-desktop-gnome
Provides:       chromium-password = %version
Provides:       chromium-desktop-kde = %version
Obsoletes:      chromium-desktop-kde < %version
Requires:       %name = %version
Requires:       kde4base-runtime-core

%description kde
By using the update-alternatives the password store for Chromium is
changed to utilize KDE's kwallet. Please be aware that by this change
the old password are no longer accessible and are also not converted
to kwallet.

%package gnome
Summary:        Update to chromium to use Gnome keyring to store passwords
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Conflicts:      chromium-desktop-kde
Conflicts:      chromium-kde
Provides:       chromium-password = %version
Provides:       chromium-desktop-gnome = %version
Obsoletes:      chromium-desktop-gnome < %version
Requires:       %name = %version
Requires:       gnome-keyring

%description gnome
By using the update-alternatives the password store for Chromium is
changed to utilize Gnome's Keyring. Please be aware that by this change
the old password are no longer accessible and are also not converted
to Gnome's Keyring.

%prep
%setup -q -n chromium
tar -xf %SOURCE1
#tar -xf %%SOURCE2

### Begin to apply patches
%patch001 -p1
%patch002 -p1
%patch003 -p1
%patch004 -p1
%patch005 -p1
%patch006 -p1
%patch007 -p1
%patch008 -p1
%patch009 -p1
%patch010 -p1
%patch011 -p1
%patch012 -p1
%patch013 -p1
%patch014 -p1
%patch015 -p1
%patch016 -p1
%patch017 -p1
%patch018 -p1
%patch019 -p1
%patch020 -p1
%patch021 -p1
%patch022 -p1
### Finish apply patches

echo > "third_party/adobe/flash/flapper_version.h"

# lost sources
for f in .rpm/blinkpy-common/*.py; do
	t="third_party/blink/tools/blinkpy/common/${f##*/}"
	[ -f "$t" ] || install -D "$f" "$t"
done
touch third_party/blink/tools/blinkpy/__init__.py

# unknown warning option '-Wno-ignored-pragma-optimize'
# unknown warning option '-Wno-defaulted-function-deleted'
# clang7: error: unknown argument: '-fsplit-lto-unit'
sed -i \
	-e '/"-Wno-ignored-pragma-optimize"/d' \
	-e '/"-Wno-defaulted-function-deleted"/d' \
	-e '/"-fsplit-lto-unit"/d' \
	build/config/compiler/BUILD.gn

sed -i \
	-e 's/^\([%%#]define CONFIG_PIC\) 0/\1 1/' \
	third_party/libaom/source/config/linux/ia32/config/aom_config.asm \
	third_party/libaom/source/config/linux/ia32/config/aom_config.h

mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/

rm -f -- .rpm/depot_tools/ninja
ln -s /usr/bin/ninja .rpm/depot_tools/ninja


%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%else
export CC="gcc"
export CXX="g++"
export AR="ar"
%endif

bits=$(getconf LONG_BIT)

export RANLIB="ranlib"
export PATH="$PWD/.rpm/depot_tools:$PATH"
export CHROMIUM_RPATH="%_libdir/%name"

CHROMIUM_GN_DEFINES=
gn_arg() { CHROMIUM_GN_DEFINES="$CHROMIUM_GN_DEFINES $*"; }

#gn_arg custom_toolchain=\"//build/toolchain/linux/unbundle:default\"
#gn_arg host_toolchain=\"//build/toolchain/linux/unbundle:default\"
gn_arg is_official_build=true
gn_arg is_desktop_linux=true
gn_arg use_custom_libcxx=false
gn_arg use_sysroot=false
gn_arg use_gio=true
gn_arg use_glib=true
gn_arg use_libpci=true
gn_arg use_pulseaudio=true
gn_arg use_aura=true
gn_arg use_cups=true
gn_arg use_kerberos=true
gn_arg use_gold=false
gn_arg use_vaapi=true
gn_arg optimize_webui=false
gn_arg use_system_freetype=false
gn_arg use_system_harfbuzz=false
gn_arg link_pulseaudio=true
gn_arg ffmpeg_branding=\"ChromeOS\"
gn_arg proprietary_codecs=true
gn_arg enable_hangout_services_extension=true
gn_arg fieldtrial_testing_like_official_build=true
gn_arg linux_use_bundled_binutils=false
gn_arg treat_warnings_as_errors=false
gn_arg fatal_linker_warnings=false
gn_arg system_libdir=\"%_lib\"
gn_arg use_allocator=\"none\"
gn_arg use_icf=false
gn_arg closure_compile=false

# Remove debug
gn_arg is_debug=false
gn_arg symbol_level=0
gn_arg remove_webcore_debug_symbols=true

gn_arg enable_nacl=%{is_enabled nacl}
gn_arg is_component_ffmpeg=%{is_enabled shared_libraries}
gn_arg is_component_build=%{is_enabled shared_libraries}
gn_arg enable_widevine=%{is_enabled widevine}

%if_enabled clang
gn_arg clang_base_path=\"%_prefix\"
gn_arg is_clang=true
gn_arg clang_use_chrome_plugins=false
gn_arg use_lld=true
if [ "$bits" = 64 ]; then
    gn_arg use_thin_lto=true
else
    gn_arg use_thin_lto=false
fi
gn_arg is_cfi=false
gn_arg use_cfi_icall=false
%else
gn_arg is_clang=false
%endif

%ifnarch %{ix86} x86_64
gn_arg icu_use_data_file=false
%endif

%if_enabled google_api_keys
gn_arg google_api_key=\"%api_key\"
gn_arg google_default_client_id=\"%default_client_id\"
gn_arg google_default_client_secret=\"%default_client_secret\"
%endif

unbundle=
unbundle_lib() { unbundle="$unbundle $*"; }

unbundle_lib fontconfig
unbundle_lib freetype
%if_enabled ffmpeg
unbundle_lib ffmpeg opus
%endif

[ -z "$unbundle" ] ||
	build/linux/unbundle/replace_gn_files.py --system-libraries $unbundle

tools/gn/bootstrap/bootstrap.py --gn-gen-args="$CHROMIUM_GN_DEFINES" --build-path=%target
%target/gn gen --args="$CHROMIUM_GN_DEFINES" %target

n=%build_parallel_jobs
[ "$n" -lt 16 ] || n=16

ninja \
	-vvv \
	-j $n \
	-C %target \
	chrome \
	chrome_sandbox \
	chromedriver

%install
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%_man1dir \
	%buildroot/%_libdir/%name \
	%buildroot/%_sysconfdir/%name \
#
install -m 755 %SOURCE100 %buildroot%_libdir/%name/%name-generic
install -m 644 %SOURCE200 %buildroot%_sysconfdir/%name/default

# compatibility symlink
ln -s %name %buildroot/%_bindir/chromium-browser

# manpage
.rpm/scripts/make-manpage.sh > %buildroot/%_man1dir/%name.1
ln -s %name.1  %buildroot/%_man1dir/chrome.1

# x86_64 capable systems need this
sed -i -e 's,/usr/lib/chromium,%_libdir/%name,g' %buildroot%_libdir/%name/%name-generic
ln -s %name-generic %buildroot%_libdir/%name/%name-kde
ln -s %name-generic %buildroot%_libdir/%name/%name-gnome

pushd %target
cp -a chrome         %buildroot%_libdir/%name/%name
cp -a chrome_sandbox %buildroot%_libdir/%name/chrome-sandbox
cp -a chromedriver   %buildroot%_libdir/%name/chromedriver

ln -s -- %_libdir/%name/chromedriver %buildroot/%_bindir/chromedriver

for f in *.bin *.so* *.pak swiftshader locales icudtl.dat; do
	[ ! -e "$f" ] ||
		cp -at %buildroot%_libdir/%name -- "$f"
done

# Remove garbage
find -name '*.TOC' -delete

# NaCl
%if_enabled nacl
cp -at %buildroot%_libdir/%name -- \
 nacl_helper \
 nacl_helper_bootstrap \
 nacl_irt_*.nexe
%endif
popd

# Icons
for size in 22 24 48 64 128 256; do
	install -Dm644 "chrome/app/theme/chromium/product_logo_$size.png" \
		"%buildroot/%_iconsdir/hicolor/${size}x${size}/apps/%name.png"
done
for size in 16 32; do
	install -Dm644 "chrome/app/theme/default_100_percent/chromium/product_logo_$size.png" \
		"%buildroot/%_iconsdir/hicolor/${size}x${size}/apps/%name.png"
done

# Desktop file
install -Dm0644 %SOURCE101 %buildroot/%_desktopdir/%name.desktop

mkdir -p -- %buildroot%_datadir/gnome-control-center/default-apps/
cp -a %SOURCE102 %buildroot%_datadir/gnome-control-center/default-apps/%name.xml

# link to browser plugin path.  Plugin patch doesn't work. Why?
mkdir -p -- %buildroot%_libdir/browser-plugins
ln -s -- %_libdir/browser-plugins %buildroot%_libdir/%name/plugins

# Install the master_preferences file
mkdir -p -- %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE30 %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE31 %buildroot%_sysconfdir/%name

# Set alternative to xbrowser
mkdir -p -- %buildroot%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t50\n'            > %buildroot%_altdir/%name
printf '%_bindir/%name\t%_libdir/%name/%name-generic\t10\n' > %buildroot%_altdir/%name-generic
printf '%_bindir/%name\t%_libdir/%name/%name-kde\t15\n'     > %buildroot%_altdir/%name-kde
printf '%_bindir/%name\t%_libdir/%name/%name-gnome\t15\n'   > %buildroot%_altdir/%name-gnome

(set +x;
	find %buildroot/%_libdir/%name -type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | fgrep -qs ELF || continue

		# Strip Chromium executables to disable debuginfo generation (became too huge)
		#strip -d "$t" ||:

		# Add real RPATH
		chrpath -r '%_libdir/%name' "$t" ||:
	done
)

%files
%doc AUTHORS LICENSE
%dir %_datadir/gnome-control-center
%dir %_datadir/gnome-control-center/default-apps
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/*
%attr(4711,root,root) %_libdir/%name/chrome-sandbox
%_libdir/%name
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_datadir/gnome-control-center/default-apps/*.xml
%_iconsdir/hicolor/*/apps/*.png
%_altdir/%name
%_altdir/%name-generic
%exclude %_libdir/%name/%name-kde
%exclude %_libdir/%name/%name-gnome

%files kde
%attr(755, root, root) %_libdir/%name/%name-kde
%_altdir/%name-kde

%files gnome
%attr(755, root, root) %_libdir/%name/%name-gnome
%_altdir/%name-gnome

%changelog
* Fri Aug 02 2019 Alexey Gladkov <legion@altlinux.ru> 76.0.3809.87-alt1
- New version (76.0.3809.87).
- Security fixes:
  - CVE-2019-5850: Use-after-free in offline page fetcher.
  - CVE-2019-5851: Use-after-poison in offline audio context.
  - CVE-2019-5852: Object leak of utility functions.
  - CVE-2019-5853: Memory corruption in regexp length check.
  - CVE-2019-5854: Integer overflow in PDFium text rendering.
  - CVE-2019-5855: Integer overflow in PDFium.
  - CVE-2019-5856: Insufficient checks on filesystem: URI permissions.
  - CVE-2019-5857: Comparison of -0 and null yields crash.
  - CVE-2019-5858: Insufficient filtering of Open URL service parameters.
  - CVE-2019-5859: res: URIs can load alternative browsers.
  - CVE-2019-5860: Use-after-free in PDFium.
  - CVE-2019-5861: Click location incorrectly checked.
  - CVE-2019-5862: AppCache not robust to compromised renderers.
  - CVE-2019-5863: Use-after-free in WebUSB on Windows.
  - CVE-2019-5864: Insufficient port filtering in CORS for extensions.
  - CVE-2019-5865: Site isolation bypass from compromised renderer.

* Fri May 03 2019 Alexey Gladkov <legion@altlinux.ru> 74.0.3729.131-alt1
- New version (74.0.3729.131).
- Security fixes:
  - CVE-2019-5805: Use after free in PDFium.
  - CVE-2019-5806: Integer overflow in Angle.
  - CVE-2019-5807: Memory corruption in V8.
  - CVE-2019-5808: Use after free in Blink.
  - CVE-2019-5809: Use after free in Blink.
  - CVE-2019-5810: User information disclosure in Autofill.
  - CVE-2019-5811: CORS bypass in Blink.
  - CVE-2019-5812: URL spoof in Omnibox on iOS.
  - CVE-2019-5813: Out of bounds read in V8.
  - CVE-2019-5814: CORS bypass in Blink.
  - CVE-2019-5815: Heap buffer overflow in Blink.
  - CVE-2019-5816: Exploit persistence extension on Android.
  - CVE-2019-5817: Heap buffer overflow in Angle on Windows.
  - CVE-2019-5818: Uninitialized value in media reader.
  - CVE-2019-5819: Incorrect escaping in developer tools.
  - CVE-2019-5820: Integer overflow in PDFium.
  - CVE-2019-5821: Integer overflow in PDFium.
  - CVE-2019-5822: CORS bypass in download manager.
  - CVE-2019-5823: Forced navigation from service worker.
  - CVE-2019-5824: Parameter passing error in media player.
  - CVE-2019-5825: Out-of-bounds write in V8
  - CVE-2019-5826: Use-after-free in IndexedDB
  - CVE-2019-5827: Out-of-bounds access in SQLite.

* Mon Mar 18 2019 Alexey Gladkov <legion@altlinux.ru> 73.0.3683.75-alt1
- New version (73.0.3683.75).
- Security fixes:
  - CVE-2019-5787: Use after free in Canvas.
  - CVE-2019-5788: Use after free in FileAPI.
  - CVE-2019-5789: Use after free in WebMIDI.
  - CVE-2019-5790: Heap buffer overflow in V8.
  - CVE-2019-5791: Type confusion in V8.
  - CVE-2019-5792: Integer overflow in PDFium.
  - CVE-2019-5793: Excessive permissions for private API in Extensions.
  - CVE-2019-5794: Security UI spoofing.
  - CVE-2019-5795: Integer overflow in PDFium.
  - CVE-2019-5796: Race condition in Extensions.
  - CVE-2019-5797: Race condition in DOMStorage.
  - CVE-2019-5798: Out of bounds read in Skia.
  - CVE-2019-5799: CSP bypass with blob URL.
  - CVE-2019-5800: CSP bypass with blob URL.
  - CVE-2019-5801: Incorrect Omnibox display on iOS.
  - CVE-2019-5802: Security UI spoofing.
  - CVE-2019-5803: CSP bypass with Javascript URLs'.
  - CVE-2019-5804: Command line command injection on Windows.

* Sun Mar 03 2019 Alexey Gladkov <legion@altlinux.ru> 72.0.3626.121-alt1
- New version (72.0.3626.121).

* Mon Feb 04 2019 Alexey Gladkov <legion@altlinux.ru> 72.0.3626.81-alt1
- New version (72.0.3626.81).
- Security fixes:
  - CVE-2019-5754: Inappropriate implementation in QUIC Networking.
  - CVE-2019-5755: Inappropriate implementation in V8.
  - CVE-2019-5756: Use after free in PDFium.
  - CVE-2019-5757: Type Confusion in SVG.
  - CVE-2019-5758: Use after free in Blink.
  - CVE-2019-5759: Use after free in HTML select elements.
  - CVE-2019-5760: Use after free in WebRTC.
  - CVE-2019-5761: Use after free in SwiftShader.
  - CVE-2019-5762: Use after free in PDFium.
  - CVE-2019-5763: Insufficient validation of untrusted input in V8.
  - CVE-2019-5764: Use after free in WebRTC.
  - CVE-2019-5765: Insufficient policy enforcement in the browser.
  - CVE-2019-5766: Insufficient policy enforcement in Canvas.
  - CVE-2019-5767: Incorrect security UI in WebAPKs.
  - CVE-2019-5768: Insufficient policy enforcement in DevTools.
  - CVE-2019-5769: Insufficient validation of untrusted input in Blink.
  - CVE-2019-5770: Heap buffer overflow in WebGL.
  - CVE-2019-5771: Heap buffer overflow in SwiftShader.
  - CVE-2019-5772: Use after free in PDFium.
  - CVE-2019-5773: Insufficient data validation in IndexedDB.
  - CVE-2019-5774: Insufficient validation of untrusted input in SafeBrowsing.
  - CVE-2019-5775: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5776: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5777: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5778: Insufficient policy enforcement in Extensions.
  - CVE-2019-5779: Insufficient policy enforcement in ServiceWorker.
  - CVE-2019-5780: Insufficient policy enforcement.
  - CVE-2019-5781: Insufficient policy enforcement in Omnibox.
  - CVE-2019-5782: Inappropriate implementation in V8.
  - CVE-2019-5783: Insufficient validation of untrusted input in DevTools.

* Fri Dec 14 2018 Alexey Gladkov <legion@altlinux.ru> 71.0.3578.98-alt1
- New version (71.0.3578.98).
- Security fixes:
  - CVE-2018-17481: Use after free in PDFium.

* Wed Nov 07 2018 Alexey Gladkov <legion@altlinux.ru> 70.0.3538.77-alt1
- New version (70.0.3538.77).

* Mon Oct 22 2018 Alexey Gladkov <legion@altlinux.ru> 70.0.3538.67-alt1
- New version (70.0.3538.67).
- Security fixes:
  - CVE-2018-17462: Sandbox escape in AppCache.
  - CVE-2018-17463: Remote code execution in V8.
  - CVE to be assigned: Heap buffer overflow in Little CMS in PDFium.
  - CVE-2018-17464: URL spoof in Omnibox.
  - CVE-2018-17465: Use after free in V8.
  - CVE-2018-17466: Memory corruption in Angle.
  - CVE-2018-17467: URL spoof in Omnibox.
  - CVE-2018-17468: Cross-origin URL disclosure in Blink.
  - CVE-2018-17469: Heap buffer overflow in PDFium.
  - CVE-2018-17470: Memory corruption in GPU Internals.
  - CVE-2018-17471: Security UI occlusion in full screen mode.
  - CVE-2018-17472: iframe sandbox escape on iOS.
  - CVE-2018-17473: URL spoof in Omnibox.
  - CVE-2018-17474: Use after free in Blink.
  - CVE-2018-17475: URL spoof in Omnibox.
  - CVE-2018-17476: Security UI occlusion in full screen mode.
  - CVE-2018-5179: Lack of limits on update() in ServiceWorker.
  - CVE-2018-17477: UI spoof in Extensions.

* Thu Oct 11 2018 Alexey Gladkov <legion@altlinux.ru> 69.0.3497.100-alt1
- New version (69.0.3497.100).
- Add symlink /usr/bin/chromium -> chromium-browser.

* Wed Sep 05 2018 Alexey Gladkov <legion@altlinux.ru> 69.0.3497.81-alt1
- New version (69.0.3497.81).
- Security fixes:
  - CVE-2018-16065: Out of bounds write in V8.
  - CVE-2018-16066: Out of bounds read in Blink.
  - CVE-2018-16067: Out of bounds read in WebAudio.
  - CVE-2018-16068: Out of bounds write in Mojo.
  - CVE-2018-16069: Out of bounds read in SwiftShader.
  - CVE-2018-16070: Integer overflow in Skia.
  - CVE-2018-16071: Use after free in WebRTC.
  - CVE-2018-16072: Cross origin pixel leak in Chrome's interaction with Android's MediaPlayer.
  - CVE-2018-16073: Site Isolation bypass after tab restore.
  - CVE-2018-16074: Site Isolation bypass using Blob URLS.
  - CVE-2018-16075: Local file access in Blink.
  - CVE-2018-16076: Out of bounds read in PDFium.
  - CVE-2018-16077: Content security policy bypass in Blink.
  - CVE-2018-16078: Credit card information leak in Autofill.
  - CVE-2018-16079: URL spoof in permission dialogs.
  - CVE-2018-16080: URL spoof in full screen mode.
  - CVE-2018-16081: Local file access in DevTools.
  - CVE-2018-16082: Stack buffer overflow in SwiftShader.
  - CVE-2018-16083: Out of bounds read in WebRTC.
  - CVE-2018-16084: User confirmation bypass in external protocol handling.
  - CVE-2018-16085: Use after free in Memory Instrumentation.
  - Out of bounds read in Little-CMS.

* Wed Aug 08 2018 Alexey Gladkov <legion@altlinux.ru> 68.0.3440.84-alt1
- New version (68.0.3440.84).
- Security fixes:
  - CVE-2018-6153: Stack buffer overflow in Skia.
  - CVE-2018-6154: Heap buffer overflow in WebGL.
  - CVE-2018-6155: Use after free in WebRTC.
  - CVE-2018-6156: Heap buffer overflow in WebRTC.
  - CVE-2018-6157: Type confusion in WebRTC.
  - CVE-2018-6158: Use after free in Blink.
  - CVE-2018-6159: Same origin policy bypass in ServiceWorker.
  - CVE-2018-6160: URL spoof in Chrome on iOS.
  - CVE-2018-6161: Same origin policy bypass in WebAudio.
  - CVE-2018-6162: Heap buffer overflow in WebGL.
  - CVE-2018-6163: URL spoof in Omnibox.
  - CVE-2018-6164: Same origin policy bypass in ServiceWorker.
  - CVE-2018-6165: URL spoof in Omnibox.
  - CVE-2018-6166: URL spoof in Omnibox.
  - CVE-2018-6167: URL spoof in Omnibox.
  - CVE-2018-6168: CORS bypass in Blink.
  - CVE-2018-6169: Permissions bypass in extension installation .
  - CVE-2018-6170: Type confusion in PDFium.
  - CVE-2018-6171: Use after free in WebBluetooth.
  - CVE-2018-6172: URL spoof in Omnibox.
  - CVE-2018-6173: URL spoof in Omnibox.
  - CVE-2018-6174: Integer overflow in SwiftShader.
  - CVE-2018-6175: URL spoof in Omnibox.
  - CVE-2018-6176: Local user privilege escalation in Extensions.
  - CVE-2018-6177: Cross origin information leak in Blink.
  - CVE-2018-6178: UI spoof in Extensions.
  - CVE-2018-6179: Local file information leak in Extensions.
  - CVE-2018-6044: Request privilege escalation in Extensions .
  - CVE-2018-4117: Cross origin information leak in Blink.
  - CVE-2018-6150: Cross origin information disclosure in Service Workers.
  - CVE-2018-6151: Bad cast in DevTools.
  - CVE-2018-6152: Local file write in DevTools.

* Sun Jun 17 2018 Alexey Gladkov <legion@altlinux.ru> 67.0.3396.87-alt1
- New version (67.0.3396.87).
- Use ninja-build.
- Security fixes:
  - CVE-2018-6149: Out of bounds write in V8.
  - CVE-2018-6148: Incorrect handling of CSP header.
  - CVE-2018-6123: Use after free in Blink.
  - CVE-2018-6124: Type confusion in Blink.
  - CVE-2018-6125: Overly permissive policy in WebUSB.
  - CVE-2018-6126: Heap buffer overflow in Skia.
  - CVE-2018-6127: Use after free in indexedDB.
  - CVE-2018-6128: uXSS in Chrome on iOS.
  - CVE-2018-6129: Out of bounds memory access in WebRTC.
  - CVE-2018-6130: Out of bounds memory access in WebRTC.
  - CVE-2018-6131: Incorrect mutability protection in WebAssembly.
  - CVE-2018-6132: Use of uninitialized memory in WebRTC.
  - CVE-2018-6133: URL spoof in Omnibox.
  - CVE-2018-6134: Referrer Policy bypass in Blink.
  - CVE-2018-6135: UI spoofing in Blink.
  - CVE-2018-6136: Out of bounds memory access in V8.
  - CVE-2018-6137: Leak of visited status of page in Blink.
  - CVE-2018-6138: Overly permissive policy in Extensions.
  - CVE-2018-6139: Restrictions bypass in the debugger extension API.
  - CVE-2018-6140: Restrictions bypass in the debugger extension API.
  - CVE-2018-6141: Heap buffer overflow in Skia.
  - CVE-2018-6142: Out of bounds memory access in V8.
  - CVE-2018-6143: Out of bounds memory access in V8.
  - CVE-2018-6144: Out of bounds memory access in PDFium.
  - CVE-2018-6145: Incorrect escaping of MathML in Blink.
  - CVE-2018-6147: Password fields not taking advantage of OS protections in Views.

* Thu Apr 19 2018 Alexey Gladkov <legion@altlinux.ru> 66.0.3359.117-alt1
- New version (66.0.3359.117).
- Security fixes:
  - CVE-2018-6085: Use after free in Disk Cache.
  - CVE-2018-6086: Use after free in Disk Cache.
  - CVE-2018-6087: Use after free in WebAssembly.
  - CVE-2018-6088: Use after free in PDFium.
  - CVE-2018-6089: Same origin policy bypass in Service Worker.
  - CVE-2018-6090: Heap buffer overflow in Skia.
  - CVE-2018-6091: Incorrect handling of plug-ins by Service Worker.
  - CVE-2018-6092: Integer overflow in WebAssembly.
  - CVE-2018-6093: Same origin bypass in Service Worker.
  - CVE-2018-6094: Exploit hardening regression in Oilpan.
  - CVE-2018-6095: Lack of meaningful user interaction requirement before file upload.
  - CVE-2018-6096: Fullscreen UI spoof.
  - CVE-2018-6097: Fullscreen UI spoof.
  - CVE-2018-6098: URL spoof in Omnibox.
  - CVE-2018-6099: CORS bypass in ServiceWorker.
  - CVE-2018-6100: URL spoof in Omnibox.
  - CVE-2018-6101: Insufficient protection of remote debugging prototol in DevTools .
  - CVE-2018-6102: URL spoof in Omnibox.
  - CVE-2018-6103: UI spoof in Permissions.
  - CVE-2018-6104: URL spoof in Omnibox.
  - CVE-2018-6105: URL spoof in Omnibox.
  - CVE-2018-6106: Incorrect handling of promises in V8.
  - CVE-2018-6107: URL spoof in Omnibox.
  - CVE-2018-6108: URL spoof in Omnibox.
  - CVE-2018-6109: Incorrect handling of files by FileAPI.
  - CVE-2018-6110: Incorrect handling of plaintext files via file:// .
  - CVE-2018-6111: Heap-use-after-free in DevTools.
  - CVE-2018-6112: Incorrect URL handling in DevTools.
  - CVE-2018-6113: URL spoof in Navigation.
  - CVE-2018-6114: CSP bypass.
  - CVE-2018-6115: SmartScreen bypass in downloads.
  - CVE-2018-6116: Incorrect low memory handling in WebAssembly.
  - CVE-2018-6117: Confusing autofill settings.
  - CVE-2018-6084: Incorrect use of Distributed Objects in Google Software Updater on MacOS.

* Fri Mar 30 2018 Alexey Gladkov <legion@altlinux.ru> 65.0.3325.181-alt1
- New version (65.0.3325.181).

* Wed Mar 07 2018 Alexey Gladkov <legion@altlinux.ru> 65.0.3325.146-alt1
- New version (65.0.3325.146).
- Use clang.
- Security fixes:
  - CVE-2018-6058: Use after free in Flash.
  - CVE-2018-6059: Use after free in Flash.
  - CVE-2018-6060: Use after free in Blink.
  - CVE-2018-6061: Race condition in V8.
  - CVE-2018-6062: Heap buffer overflow in Skia.
  - CVE-2018-6057: Incorrect permissions on shared memory.
  - CVE-2018-6063: Incorrect permissions on shared memory.
  - CVE-2018-6064: Type confusion in V8.
  - CVE-2018-6065: Integer overflow in V8.
  - CVE-2018-6066: Same Origin Bypass via canvas.
  - CVE-2018-6067: Buffer overflow in Skia.
  - CVE-2018-6068: Object lifecycle issues in Chrome Custom Tab.
  - CVE-2018-6069: Stack buffer overflow in Skia.
  - CVE-2018-6070: CSP bypass through extensions.
  - CVE-2018-6071: Heap bufffer overflow in Skia.
  - CVE-2018-6072: Integer overflow in PDFium.
  - CVE-2018-6073: Heap bufffer overflow in WebGL.
  - CVE-2018-6074: Mark-of-the-Web bypass.
  - CVE-2018-6075: Overly permissive cross origin downloads.
  - CVE-2018-6076: Incorrect handling of URL fragment identifiers in Blink.
  - CVE-2018-6077: Timing attack using SVG filters.
  - CVE-2018-6078: URL Spoof in OmniBox.
  - CVE-2018-6079: Information disclosure via texture data in WebGL.
  - CVE-2018-6080: Information disclosure in IPC call.
  - CVE-2018-6081: XSS in interstitials.
  - CVE-2018-6082: Circumvention of port blocking.
  - CVE-2018-6083: Incorrect processing of AppManifests.

* Thu Jan 25 2018 Alexey Gladkov <legion@altlinux.ru> 64.0.3282.119-alt1
- New version (64.0.3282.119).
- Security fixes:
  - CVE-2018-6031: Use after free in PDFium.
  - CVE-2018-6032: Same origin bypass in Shared Worker.
  - CVE-2018-6033: Race when opening downloaded files.
  - CVE-2018-6034: Integer overflow in Blink.
  - CVE-2018-6035: Insufficient isolation of devtools from extensions.
  - CVE-2018-6036: Integer underflow in WebAssembly.
  - CVE-2018-6037: Insufficient user gesture requirements in autofill.
  - CVE-2018-6038: Heap buffer overflow in WebGL.
  - CVE-2018-6039: XSS in DevTools.
  - CVE-2018-6040: Content security policy bypass.
  - CVE-2018-6041: URL spoof in Navigation.
  - CVE-2018-6042: URL spoof in OmniBox.
  - CVE-2018-6043: Insufficient escaping with external URL handlers.
  - CVE-2018-6045: Insufficient isolation of devtools from extensions.
  - CVE-2018-6046: Insufficient isolation of devtools from extensions.
  - CVE-2018-6047: Cross origin URL leak in WebGL.
  - CVE-2018-6048: Referrer policy bypass in Blink.
  - CVE-2017-15420: URL spoofing in Omnibox.
  - CVE-2018-6049: UI spoof in Permissions.
  - CVE-2018-6050: URL spoof in OmniBox.
  - CVE-2018-6051: Referrer leak in XSS Auditor.
  - CVE-2018-6052: Incomplete no-referrer policy implementation.
  - CVE-2018-6053: Leak of page thumbnails in New Tab Page.
  - CVE-2018-6054: Use after free in WebUI.

* Fri Jan 05 2018 Alexey Gladkov <legion@altlinux.ru> 63.0.3239.132-alt1
- New version (63.0.3239.132).
- Build contains a number of bug fixes and security updates.

* Sat Dec 16 2017 Alexey Gladkov <legion@altlinux.ru> 63.0.3239.108-alt1
- New version (63.0.3239.108).
- Security fixes:
  - CVE-2017-15429: UXSS in V8.

* Mon Nov 13 2017 Alexey Gladkov <legion@altlinux.ru> 62.0.3202.89-alt1
- New version (62.0.3202.89).
- Security fixes:
  - CVE-2017-15398: Stack buffer overflow in QUIC.
  - CVE-2017-15399: Use after free in V8.

* Tue Oct 24 2017 Alexey Gladkov <legion@altlinux.ru> 62.0.3202.75-alt1
- New version (62.0.3202.75).
- Security fixes:
  - CVE-2017-5124: UXSS with MHTML.
  - CVE-2017-5125: Heap overflow in Skia.
  - CVE-2017-5126: Use after free in PDFium.
  - CVE-2017-5127: Use after free in PDFium.
  - CVE-2017-5128: Heap overflow in WebGL.
  - CVE-2017-5129: Use after free in WebAudio.
  - CVE-2017-5132: Incorrect stack manipulation in WebAssembly.
  - CVE-2017-5130: Heap overflow in libxml2.
  - CVE-2017-5131: Out of bounds write in Skia.
  - CVE-2017-5133: Out of bounds write in Skia.
  - CVE-2017-15386: UI spoofing in Blink.
  - CVE-2017-15387: Content security bypass.
  - CVE-2017-15388: Out of bounds read in Skia.
  - CVE-2017-15389: URL spoofing in OmniBox.
  - CVE-2017-15390: URL spoofing in OmniBox.
  - CVE-2017-15391: Extension limitation bypass in Extensions.
  - CVE-2017-15392: Incorrect registry key handling in PlatformIntegration.
  - CVE-2017-15393: Referrer leak in Devtools.
  - CVE-2017-15394: URL spoofing in extensions UI.
  - CVE-2017-15395: Null pointer dereference in ImageCapture.

* Tue Sep 26 2017 Alexey Gladkov <legion@altlinux.ru> 61.0.3163.100-alt1
- Security fixes:
  - CVE-2017-5121: Out-of-bounds access in V8. Reported by Jordan Rabet, Microsoft Offensive Security Research and Microsoft ChakraCore team on 2017-09-14
  - CVE-2017-5122: Out-of-bounds access in V8. Reported by Choongwoo Han of Naver Corporation on 2017-08-04

* Tue Sep 12 2017 Alexey Gladkov <legion@altlinux.ru> 61.0.3163.79-alt1
- New version (61.0.3163.79).
- Security fixes:
  - CVE-2017-5111: Use after free in PDFium. Reported by Luat Nguyen (@l4wio) of KeenLab, Tencent on 2017-06-27
  - CVE-2017-5112: Heap buffer overflow in WebGL. Reported by Tobias Klein (www.trapkit.de) on 2017-07-10
  - CVE-2017-5113: Heap buffer overflow in Skia. Reported by Anonymous on 2017-07-20
  - CVE-2017-5114: Memory lifecycle issue in PDFium. Reported by Ke Liu of Tencent's Xuanwu LAB on 2017-08-07
  - CVE-2017-5115: Type confusion in V8. Reported by Marco Giovannini on 2017-07-17
  - CVE-2017-5116: Type confusion in V8. Reported Guang Gong of Alpha Team, Qihoo 360 on 2017-08-28
  - CVE-2017-5117: Use of uninitialized value in Skia. Reported by Tobias Klein (www.trapkit.de) on 2017-07-04
  - CVE-2017-5118: Bypass of Content Security Policy in Blink. Reported by WenXu Wu of Tencent's Xuanwu Lab on 2017-07-24
  - CVE-2017-5119: Use of uninitialized value in Skia. Reported by Anonymous on 2017-05-22
  - CVE-2017-5120: Potential HTTPS downgrade during redirect navigation. Reported by Xiaoyin Liu (@general_nfs) on 2017-05-05

* Tue Aug 15 2017 Alexey Gladkov <legion@altlinux.ru> 60.0.3112.90-alt2
- Add missing libraries (ALT#33750).

* Mon Aug 14 2017 Alexey Gladkov <legion@altlinux.ru> 60.0.3112.90-alt1
- New version (60.0.3112.90).

* Tue Aug 01 2017 Alexey Gladkov <legion@altlinux.ru> 60.0.3112.78-alt1
- New version (60.0.3112.78).
- Security fixes:
  - CVE-2017-5091: Use after free in IndexedDB. Reported by Ned Williamson on 2017-06-02
  - CVE-2017-5092: Use after free in PPAPI. Reported by Yu Zhou, Yuan Deng of Ant-financial Light-Year Security Lab on 2017-06-15
  - CVE-2017-5093: UI spoofing in Blink. Reported by Luan Herrera on 2015-10-31
  - CVE-2017-5094: Type confusion in extensions. Reported by Anonymous on 2017-03-19
  - CVE-2017-5095: Out-of-bounds write in PDFium. Reported by Anonymous on 2017-06-13
  - CVE-2017-5096: User information leak via Android intents. Reported by Takeshi Terada on 2017-04-23
  - CVE-2017-5097: Out-of-bounds read in Skia. Reported by Anonymous on 2017-07-11
  - CVE-2017-5098: Use after free in V8. Reported by Jihoon Kim on 2017-07-11
  - CVE-2017-5099: Out-of-bounds write in PPAPI. Reported by Yuan Deng, Yu Zhou of Ant-financial Light-Year Security Lab on 2017-06-15
  - CVE-2017-5100: Use after free in Chrome Apps. Reported by Anonymous on 2017-05-04
  - CVE-2017-5101: URL spoofing in OmniBox. Reported by Luan Herrera on 2017-01-17
  - CVE-2017-5102: Uninitialized use in Skia. Reported by Anonymous on 2017-05-30
  - CVE-2017-5103: Uninitialized use in Skia. Reported by Anonymous on 2017-05-25
  - CVE-2017-5104: UI spoofing in browser. Reported by Khalil Zhani on 2017-06-02
  - CVE-2017-7000: Pointer disclosure in SQLite. Reported by Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
  - CVE-2017-5105: URL spoofing in OmniBox. Reported by Rayyan Bijoora on 2017-06-06
  - CVE-2017-5106: URL spoofing in OmniBox. Reported by Jack Zac on 2017-04-24
  - CVE-2017-5107: User information leak via SVG. Reported by David Kohlbrenner of UC San Diego on 2017-01-27
  - CVE-2017-5108: Type confusion in PDFium. Reported by Guang Gong of Alpha Team, Qihoo 360 on 2017-02-24
  - CVE-2017-5109: UI spoofing in browser. Reported by Jose Maria Acuna Morgado on 2017-04-11
  - CVE-2017-5110: UI spoofing in payments dialog. Reported by xisigr of Tencent's Xuanwu Lab on 2017-05-02

* Fri Jun 09 2017 Alexey Gladkov <legion@altlinux.ru> 59.0.3071.86-alt1
- New version (59.0.3071.86).
- Security fixes:
  - CVE-2017-5070: Type confusion in V8. Reported by Zhao Qixun(@S0rryMybad) of Qihoo 360 Vulcan Team on 2017-05-16
  - CVE-2017-5071: Out of bounds read in V8. Reported by Choongwoo Han on 2017-04-26
  - CVE-2017-5072: Address spoofing in Omnibox. Reported by Rayyan Bijoora on 2017-04-07
  - CVE-2017-5073: Use after free in print preview. Reported by Khalil Zhani on 2017-04-28
  - CVE-2017-5074: Use after free in Apps Bluetooth. Reported by anonymous on 2017-03-09
  - CVE-2017-5075: Information leak in CSP reporting. Reported by Emmanuel Gil Peyrot on 2017-01-05
  - CVE-2017-5086: Address spoofing in Omnibox. Reported by Rayyan Bijoora on 2017-05-16
  - CVE-2017-5076: Address spoofing in Omnibox. Reported by Samuel Erb on 2017-05-06
  - CVE-2017-5077: Heap buffer overflow in Skia. Reported by Sweetchip on 2017-04-28
  - CVE-2017-5078: Possible command injection in mailto handling. Reported by Jose Carlos Exposito Bueno on 2017-04-12
  - CVE-2017-5079: UI spoofing in Blink. Reported by Khalil Zhani on 2017-04-20
  - CVE-2017-5080: Use after free in credit card autofill. Reported by Khalil Zhani on 2017-04-05
  - CVE-2017-5081: Extension verification bypass. Reported by Andrey Kovalev (@L1kvID) Yandex Security Team on 2016-12-07
  - CVE-2017-5082: Insufficient hardening in credit card editor. Reported by Nightwatch Cybersecurity Research on 2017-05-11
  - CVE-2017-5083: UI spoofing in Blink. Reported by Khalil Zhani on 2017-04-24
  - CVE-2017-5085: Inappropriate javascript execution on WebUI pages. Reported by Zhiyang Zeng of Tencent security platform department on 2017-02-15

* Wed May 10 2017 Alexey Gladkov <legion@altlinux.ru> 58.0.3029.110-alt1
- New version (58.0.3029.110).

* Mon Mar 27 2017 Alexey Gladkov <legion@altlinux.ru> 57.0.2987.110-alt1
- New version (57.0.2987.110).
- Security fixes:
  - CVE-2017-5030: Memory corruption in V8. Credit to Brendon Tiszka
  - CVE-2017-5031: Use after free in ANGLE. Credit to Looben Yang
  - CVE-2017-5032: Out of bounds write in PDFium. Credit to Ashfaq Ansari - Project Srishti
  - CVE-2017-5029: Integer overflow in libxslt. Credit to Holger Fuhrmannek
  - CVE-2017-5034: Use after free in PDFium. Credit to Ke Liu of Tencent's Xuanwu LAB
  - CVE-2017-5035: Incorrect security UI in Omnibox. Credit to Enzo Aguado
  - CVE-2017-5036: Use after free in PDFium. Credit to Anonymous
  - CVE-2017-5037: Multiple out of bounds writes in ChunkDemuxer. Credit to Yongke Wang of Tencent's Xuanwu Lab (xlab.tencent.com)
  - CVE-2017-5039: Use after free in PDFium. Credit to jinmo123
  - CVE-2017-5040: Information disclosure in V8. Credit to Choongwoo Han
  - CVE-2017-5041: Address spoofing in Omnibox. Credit to Jordi Chancel
  - CVE-2017-5033: Bypass of Content Security Policy in Blink. Credit to Nicolai Grodum
  - CVE-2017-5042: Incorrect handling of cookies in Cast. Credit to Mike Ruddy
  - CVE-2017-5038: Use after free in GuestView. Credit to Anonymous
  - CVE-2017-5043: Use after free in GuestView. Credit to Anonymous
  - CVE-2017-5044: Heap overflow in Skia. Credit to Kushal Arvind Shah of Fortinet's FortiGuard Labs
  - CVE-2017-5045: Information disclosure in XSS Auditor. Credit to Dhaval Kapil (vampire)
  - CVE-2017-5046: Information disclosure in Blink. Credit to Masato Kinugawa

* Wed Feb 08 2017 Alexey Gladkov <legion@altlinux.ru> 56.0.2924.87-alt1
- New version (56.0.2924.87).
- Security fixes:
  - CVE-2017-5007: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5006: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5008: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5010: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2017-5011: Unauthorised file access in Devtools. Credit to Khalil Zhani
  - CVE-2017-5009: Out of bounds memory access in WebRTC. Credit to Sean Stanek and Chip Bradford
  - CVE-2017-5012: Heap overflow in V8. Credit to Gergely Nagy (Tresorit)
  - CVE-2017-5013: Address spoofing in Omnibox. Credit to Haosheng Wang (@gnehsoah)
  - CVE-2017-5014: Heap overflow in Skia. Credit to sweetchip
  - CVE-2017-5015: Address spoofing in Omnibox. Credit to Armin Razmdjou
  - CVE-2017-5019: Use after free in Renderer. Credit to Wadih Matar
  - CVE-2017-5016: UI spoofing in Blink. Credit to Haosheng Wang (@gnehsoah)
  - CVE-2017-5017: Uninitialised memory access in webm video. Credit to Dan Berman
  - CVE-2017-5018: Universal XSS in chrome://apps. Credit to Rob Wu
  - CVE-2017-5020: Universal XSS in chrome://downloads. Credit to Rob Wu
  - CVE-2017-5021: Use after free in Extensions. Credit to Rob Wu
  - CVE-2017-5022: Bypass of Content Security Policy in Blink. Credit to  evi1m0#ly.com
  - CVE-2017-5023: Type confusion in metrics. Credit to the UK's National Cyber Security Centre (NCSC)
  - CVE-2017-5024: Heap overflow in FFmpeg. Credit to Paul Mehta
  - CVE-2017-5025: Heap overflow in FFmpeg. Credit to Paul Mehta
  - CVE-2017-5026: UI spoofing. Credit to Ronni Skansing
  - CVE-2017-5027: Bypass of Content Security Policy in Blink.

* Thu Dec 08 2016 Alexey Gladkov <legion@altlinux.ru> 55.0.2883.75-alt1
- New version (55.0.2883.75).
- Security fixes:
  - CVE-2016-9651: Private property access in V8. Credit to Guang Gong of Alpha Team Of Qihoo 360
  - CVE-2016-5208: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2016-5207: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2016-5206: Same-origin bypass in PDFium. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5205: Universal XSS in Blink. Credit to Anonymous
  - CVE-2016-5204: Universal XSS in Blink. Credit to Mariusz Mlynski
  - CVE-2016-5209: Out of bounds write in Blink. Credit to Giwan Go of STEALIEN
  - CVE-2016-5203: Use after free in PDFium. Credit to Anonymous
  - CVE-2016-5210: Out of bounds write in PDFium. Credit to Ke Liu of Tencent's Xuanwu LAB
  - CVE-2016-5212: Local file disclosure in DevTools. Credit to Khalil Zhani
  - CVE-2016-5211: Use after free in PDFium. Credit to Anonymous
  - CVE-2016-5213: Use after free in V8. Credit to Khalil Zhani
  - CVE-2016-5214: File download protection bypass. Credit to Jonathan Birch and MSVR
  - CVE-2016-5216: Use after free in PDFium. Credit to Anonymous
  - CVE-2016-5215: Use after free in Webaudio. Credit to Looben Yang
  - CVE-2016-5217: Use of unvalidated data in PDFium. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5218: Address spoofing in Omnibox. Credit to Abdulrahman Alqabandi (@qab)
  - CVE-2016-5219: Use after free in V8. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5221: Integer overflow in ANGLE. Credit to Tim Becker of ForAllSecure
  - CVE-2016-5220: Local file access in PDFium. Credit to Rob Wu (robwu.nl)
  - CVE-2016-5222: Address spoofing in Omnibox. Credit to xisigr of Tencent's Xuanwu Lab
  - CVE-2016-9650: CSP Referrer disclosure. Credit to Jakub Zoczek
  - CVE-2016-5223: Integer overflow in PDFium. Credit to Hwiwon Lee 
  - CVE-2016-5226: Limited XSS in Blink. Credit to Jun Kokatsu (@shhnjk)
  - CVE-2016-5225: CSP bypass in Blink. Credit to Scott Helme (@Scott_Helme, scotthelme.co.uk)
  - CVE-2016-5224: Same-origin bypass in SVG. Credit to Roeland Krak
  - CVE-2016-9652: Various fixes from internal audits, fuzzing and other initiatives

* Sun Oct 30 2016 Alexey Gladkov <legion@altlinux.ru> 54.0.2840.59-alt3
- Fix Requires.
- Add debuginfo.

* Tue Oct 25 2016 Alexey Gladkov <legion@altlinux.ru> 54.0.2840.59-alt2
- Rename chromium-stable to chromium.
- Enable VAAPI.

* Fri Oct 14 2016 Alexey Gladkov <legion@altlinux.ru> 54.0.2840.59-alt1
- New version (54.0.2840.59).
- Major spec-file changes.
- Many security fixes.

* Fri Mar 25 2016 Andrey Cherepanov <cas@altlinux.org> 49.0.2623.108-alt1
- New version
- Security fixes:
  - High CVE-2016-1647: Use-after-free in Navigation.
  - High CVE-2016-1648: Use-after-free in Extensions.
  - High CVE-2016-1649: Buffer overflow in libANGLE.

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 49.0.2623.87-alt1
- New version
- Security fixes:
  - High CVE-2016-1643: Type confusion in Blink.
  - High CVE-2016-1644: Use-after-free in Blink.
  - High CVE-2016-1645: Out-of-bounds write in PDFium.

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 49.0.2623.75-alt1
- New version
- Security fixes:
  - High CVE-2016-1630: Same-origin bypass in Blink.
  - High CVE-2016-1631: Same-origin bypass in Pepper Plugin.
  - High CVE-2016-1632: Bad cast in Extensions.
  - High CVE-2016-1633: Use-after-free in Blink.
  - High CVE-2016-1634: Use-after-free in Blink.
  - High CVE-2016-1635: Use-after-free in Blink.
  - High CVE-2016-1636: SRI Validation Bypass.
  - High CVE-2015-8126: Out-of-bounds access in libpng.
  - Medium CVE-2016-1637: Information Leak in Skia.
  - Medium CVE-2016-1638: WebAPI Bypass.
  - Medium CVE-2016-1639: Use-after-free in WebRTC.
  - Medium CVE-2016-1640: Origin confusion in Extensions UI.
  - Medium CVE-2016-1641: Use-after-free in Favicon.

* Fri Feb 19 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.116-alt1
- New version
- Security fixes:
  - Critical CVE-2016-1629: Same-origin bypass in Blink and Sandbox escape in Chrome.

* Wed Feb 17 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.109-alt2
- Require libv8-chromium-bin as separate package

* Mon Feb 15 2016 L.A. Kostis <lakostis@altlinux.ru> 48.0.2564.109-alt1.1
- Enabled WebRTC support on non-ARM platforms.
- Restored build of widevine (support of DRM-protected content playback).
- Added patches from Debian:
  + fix_building_widevinecdm_with_chromium.patch: If exterior-sourced 
    widevine library exists at run-time, use it.

* Wed Feb 10 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.109-alt1
- New version
- Security fixes:
  - High CVE-2016-1622: Same-origin bypass in Extensions.
  - High CVE-2016-1623: Same-origin bypass in DOM.
  - High CVE-2016-1624: Buffer overflow in Brotli.
  - Medium CVE-2016-1625: Navigation bypass in Chrome Instant.
  - Medium CVE-2016-1626: Out-of-bounds read in PDFium.

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.103-alt2
- Enable experimental VAAPI support (ALT #31772) (thanks L.A. Kostis
  for patch)

* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.103-alt1
- New version

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.97-alt1
- New version

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 48.0.2564.82-alt1
- New version
- Security fixes:
  - High CVE-2016-1613: Use-after-free in PDFium.
  - Medium CVE-2016-1614: Information leak in Blink.
  - Medium CVE-2016-1615: Origin confusion in Omnibox.
  - Medium CVE-2016-1616: URL Spoofing.
  - Medium CVE-2016-1617: History sniffing with HSTS and CSP.
  - Medium CVE-2016-1618: Weak random number generator in Blink.
  - Medium CVE-2016-1619: Out-of-bounds read in PDFium.

* Thu Jan 14 2016 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.111-alt1
- New version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.106-alt1
- New version
- Security fix CVE-2015-6792: Fixes from internal audits and fuzzing
- Add missing requirements skipping by autoreq (ALT #31397)

* Wed Dec 09 2015 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.80-alt1
- New version
- Security fixes:
  - High CVE-2015-6788: Type confusion in extensions.
  - High CVE-2015-6789: Use-after-free in Blink.
  - Medium CVE-2015-6790: Escaping issue in saved pages.

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 47.0.2526.73-alt1
- New version
- Security fixes:
  - Critical CVE-2015-6765: Use-after-free in AppCache.
  - High CVE-2015-6766: Use-after-free in AppCache.
  - High CVE-2015-6767: Use-after-free in AppCache.
  - High CVE-2015-6768: Cross-origin bypass in DOM.
  - High CVE-2015-6769: Cross-origin bypass in core.
  - High CVE-2015-6770: Cross-origin bypass in DOM.
  - High CVE-2015-6771: Out of bounds access in v8.
  - High CVE-2015-6772: Cross-origin bypass in DOM.
  - High CVE-2015-6764: Out of bounds access in v8.
  - High CVE-2015-6773: Out of bounds access in Skia.
  - High CVE-2015-6774: Use-after-free in Extensions.
  - High CVE-2015-6775: Type confusion in PDFium.
  - High CVE-2015-6776: Out of bounds access in PDFium.
  - High CVE-2015-6777: Use-after-free in DOM.
  - Medium CVE-2015-6778: Out of bounds access in PDFium.
  - Medium CVE-2015-6779: Scheme bypass in PDFium.
  - Medium CVE-2015-6780: Use-after-free in Infobars.
  - Medium CVE-2015-6781: Integer overflow in Sfntly.
  - Medium CVE-2015-6782: Content spoofing in Omnibox.
  - Low CVE-2015-6784: Escaping issue in saved pages.
  - Low CVE-2015-6785: Wildcard matching issue in CSP.
  - Low CVE-2015-6786: Scheme bypass in CSP.
- Include libchromiumcontent (build disabled by default)

* Wed Nov 11 2015 Andrey Cherepanov <cas@altlinux.org> 46.0.2490.86-alt1
- New version
- Security fixes:
  - High CVE-2015-1302: Information leak in PDF viewer.

* Mon Nov 02 2015 Andrey Cherepanov <cas@altlinux.org> 46.0.2490.80-alt1
- New version

* Wed Oct 14 2015 Andrey Cherepanov <cas@altlinux.org> 46.0.2490.71-alt1
- New version
- Security fixes:
  - High CVE-2015-6755: Cross-origin bypass in Blink.
  - High CVE-2015-6756: Use-after-free in PDFium.
  - High CVE-2015-6757: Use-after-free in ServiceWorker.
  - High CVE-2015-6758: Bad-cast in PDFium.
  - Medium CVE-2015-6759: Information leakage in LocalStorage.
  - Medium CVE-2015-6760: Improper error handling in libANGLE.
  - Medium CVE-2015-6761: Memory corruption in FFMpeg.
  - Low CVE-2015-6762: CORS bypass via CSS fonts.

* Mon Sep 28 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.101-alt1
- New version
- Security fixes:
  - High CVE-2015-1303: Cross-origin bypass in DOM.
  - High CVE-2015-1304: Cross-origin bypass in V8.

* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.99-alt1
- New version
- Strip binaries before install

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.93-alt1
- New version

* Wed Sep 02 2015 Andrey Cherepanov <cas@altlinux.org> 45.0.2454.85-alt1
- New version
- Security fixes:
  - High CVE-2015-1291: Cross-origin bypass in DOM.
  - High CVE-2015-1292: Cross-origin bypass in ServiceWorker.
  - High CVE-2015-1293: Cross-origin bypass in DOM.
  - High CVE-2015-1294: Use-after-free in Skia.
  - High CVE-2015-1295: Use-after-free in Printing.
  - High CVE-2015-1296: Character spoofing in omnibox.
  - Medium CVE-2015-1297: Permission scoping error in WebRequest.
  - Medium CVE-2015-1298: URL validation error in extensions.
  - Medium CVE-2015-1299: Use-after-free in Blink.
  - Medium CVE-2015-1300: Information leak in Blink.

* Wed Aug 26 2015 Andrey Cherepanov <cas@altlinux.org> 44.0.2403.157-alt1
- New version

* Wed Jul 15 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.134-alt1
- New version
- Critical update to Adobe Flash Player (18.0.0.209) and a fix for a
  full screen casting issue

* Wed Jul 08 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.132-alt1
- New version

* Mon Jun 29 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.130-alt1
- New version
- Security fixes:
  - High CVE-2015-1266: Scheme validation error in WebUI.
  - High CVE-2015-1268: Cross-origin bypass in Blink.
  - Medium CVE-2015-1267: Cross-origin bypass in Blink.
  - Medium CVE-2015-1269: Normalization error in HSTS/HPKP preload list.
- use more external shared libraries (especially libv8)

* Mon Jun 15 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.125-alt1
- New version
- Fixes:
  - Resolved browser font magnification/scaling issue
- Cannot package missing libpdf.so
- Add clearkeycdm component
- Disable build on i586 (because memory exhausted while linking)
- Disable automatic external extensions loading (see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=786909)
  Also you can use --show-component-extension-options command line parameter
  to view all hidden extensions

* Thu Jun 04 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.81-alt1
- New version
- Fixes:
  - [490611] Fixed an issue where sometimes a blank page would print.
  - [478714] Icons not displaying properly on Linux.

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 43.0.2357.65-alt1
- New version
- Security fixes:
  - High CVE-2015-1252: Sandbox escape in Chrome.
  - High CVE-2015-1253: Cross-origin bypass in DOM.
  - High CVE-2015-1254: Cross-origin bypass in Editing.
  - High CVE-2015-1255: Use-after-free in WebAudio.
  - High CVE-2015-1256: Use-after-free in SVG.
  - High CVE-2015-1251: Use-after-free in Speech.
  - Medium CVE-2015-1257: Container-overflow in SVG.
  - Medium CVE-2015-1258: Negative-size parameter in Libvpx.
  - Medium CVE-2015-1259: Uninitialized value in PDFium.
  - Medium CVE-2015-1260: Use-after-free in WebRTC.
  - Medium CVE-2015-1261: URL bar spoofing.
  - Medium CVE-2015-1262: Uninitialized value in Blink.
  - Low CVE-2015-1263: Insecure download of spellcheck dictionary.
  - Low CVE-2015-1264: Cross-site scripting in bookmarks.

* Tue May 19 2015 Andrey Cherepanov <cas@altlinux.org> 42.0.2311.152-alt1
- New version

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 42.0.2311.135-alt1
- New version
- Security fixes:
  - High CVE-2015-1243: Use-after-free in DOM.

* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 42.0.2311.90-alt1
- New version
- Security fixes:
  - High CVE-2015-1235: Cross-origin-bypass in HTML parser.
  - Medium CVE-2015-1236: Cross-origin-bypass in Blink.
  - High CVE-2015-1237: Use-after-free in IPC.
  - High CVE-2015-1238: Out-of-bounds write in Skia.
  - Medium CVE-2015-1240: Out-of-bounds read in WebGL.
  - Medium CVE-2015-1241: Tap-Jacking.
  - High CVE-2015-1242: Type confusion in V8.
  - Medium CVE-2015-1244: HSTS bypass in WebSockets.
  - Medium CVE-2015-1245: Use-after-free in PDFium.
  - Medium CVE-2015-1246: Out-of-bounds read in Blink.
  - Medium CVE-2015-1247: Scheme issues in OpenSearch.
  - Medium CVE-2015-1248: SafeBrowsing bypass.


* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.118-alt1
- New version
- Security fixes:
  - Critical CVE-2015-1233: A special thanks to Anonymous for a
    combination of V8, Gamepad and IPC bugs that can lead to remote
    code execution outside of the sandbox.
  - High CVE-2015-1234: Buffer overflow via race condition in GPU.

* Fri Mar 20 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.101-alt1
- New version
- Package all *.bin files

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.89-alt1
- New version

* Wed Mar 04 2015 Andrey Cherepanov <cas@altlinux.org> 41.0.2272.76-alt1
- New version
- Security fixes:
  - High CVE-2015-1212: Out-of-bounds write in media.
  - High CVE-2015-1213: Out-of-bounds write in skia filters.
  - High CVE-2015-1214: Out-of-bounds write in skia filters.
  - High CVE-2015-1215: Out-of-bounds write in skia filters.
  - High CVE-2015-1216: Use-after-free in v8 bindings.
  - High CVE-2015-1217: Type confusion in v8 bindings.
  - High CVE-2015-1218: Use-after-free in dom.
  - High CVE-2015-1219: Integer overflow in webgl.
  - High CVE-2015-1220: Use-after-free in gif decoder.
  - High CVE-2015-1221: Use-after-free in web databases.
  - High CVE-2015-1222: Use-after-free in service workers.
  - High CVE-2015-1223: Use-after-free in dom.
  - High CVE-2015-1230: Type confusion in v8.
  - Medium CVE-2015-1224: Out-of-bounds read in vpxdecoder.
  - Medium CVE-2015-1225: Out-of-bounds read in pdfium.
  - Medium CVE-2015-1226: Validation issue in debugger.
  - Medium CVE-2015-1227: Uninitialized value in blink.
  - Medium CVE-2015-1228: Uninitialized value in rendering.
  - Medium CVE-2015-1229: Cookie injection via proxies.

* Fri Feb 20 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.115-alt1
- New version

* Fri Feb 06 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.111-alt1
- New version
- Security fixes:
  - High CVE-2015-1211: Privilege escalation using service workers.

* Tue Jan 27 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.93-alt1
- New version

* Fri Jan 23 2015 Andrey Cherepanov <cas@altlinux.org> 40.0.2214.91-alt1
- New version
- Security fixes:
  - High CVE-2014-7923: Memory corruption in ICU.
  - High CVE-2014-7924: Use-after-free in IndexedDB.
  - High CVE-2014-7925: Use-after-free in WebAudio.
  - High CVE-2014-7926: Memory corruption in ICU.
  - High CVE-2014-7927: Memory corruption in V8.
  - High CVE-2014-7928: Memory corruption in V8.
  - High CVE-2014-7930: Use-after-free in DOM.
  - High CVE-2014-7931: Memory corruption in V8.
  - High CVE-2014-7929: Use-after-free in DOM.
  - High CVE-2014-7932: Use-after-free in DOM.
  - High CVE-2014-7933: Use-after-free in FFmpeg.
  - High CVE-2014-7934: Use-after-free in DOM.
  - High CVE-2014-7935: Use-after-free in Speech.
  - High CVE-2014-7936: Use-after-free in Views.
  - High CVE-2014-7937: Use-after-free in FFmpeg.
  - High CVE-2014-7938: Memory corruption in Fonts.
  - High CVE-2014-7939: Same-origin-bypass in V8.
  - Medium CVE-2014-7940: Uninitialized-value in ICU.
  - Medium CVE-2014-7941: Out-of-bounds read in UI.
  - Medium CVE-2014-7942: Uninitialized-value in Fonts.
  - Medium CVE-2014-7943: Out-of-bounds read in Skia.
  - Medium CVE-2014-7944: Out-of-bounds read in PDFium.
  - Medium CVE-2014-7945: Out-of-bounds read in PDFium.
  - Medium CVE-2014-7946: Out-of-bounds read in Fonts.
  - Medium CVE-2014-7947: Out-of-bounds read in PDFium.
  - Medium CVE-2014-7948: Caching error in AppCache.

* Wed Jan 14 2015 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.99-alt1
- New version

* Wed Dec 10 2014 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.95-alt1
- New version

* Tue Dec 09 2014 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.71-alt1
- New version

* Fri Nov 21 2014 Andrey Cherepanov <cas@altlinux.org> 39.0.2171.65-alt1
- New version
- Security fixes:
  - High CVE-2014-7899: Address bar spoofing.
  - High CVE-2014-7900: Use-after-free in pdfium.
  - High CVE-2014-7901: Integer overflow in pdfium.
  - High CVE-2014-7902: Use-after-free in pdfium.
  - High CVE-2014-7903: Buffer overflow in pdfium.
  - High CVE-2014-7904: Buffer overflow in Skia.
  - High CVE-2014-7905: Flaw allowing navigation to intents that do not
    have the BROWSABLE category.
  - High CVE-2014-7906: Use-after-free in pepper plugins.
  - High CVE-2014-0574: Double-free in Flash.
  - High CVE-2014-7907: Use-after-free in blink.
  - High CVE-2014-7908: Integer overflow in media.
  - Medium CVE-2014-7909: Uninitialized memory read in Skia.
- Mark all files in /etc/chromium as config
- Strip Chromium executables to disable debuginfo generation (became too
  huge)

* Wed Nov 12 2014 Andrey Cherepanov <cas@altlinux.org> 38.0.2125.122-alt1
- New version

* Thu Nov 06 2014 Andrey Cherepanov <cas@altlinux.org> 38.0.2125.111-alt1
- New version
- Use sed insted of strings utility from binutils for detect PepperFlash
  plugin version
- Remove second tab in master preferences
- Replace default config

* Thu Oct 09 2014 Andrey Cherepanov <cas@altlinux.org> 38.0.2125.101-alt1
- New version
- Security fixes:
  - Critical CVE-2014-3188: A special thanks to Juri Aedla for a
    combination of V8 and IPC bugs that can lead to remote code
    execution outside of the sandbox.
  - High CVE-2014-3189: Out-of-bounds read in PDFium.
  - High CVE-2014-3190: Use-after-free in Events.
  - High CVE-2014-3191: Use-after-free in Rendering.
  - High CVE-2014-3192: Use-after-free in DOM.
  - High CVE-2014-3193: Type confusion in Session Management.
  - High CVE-2014-3194: Use-after-free in Web Workers.
  - Medium CVE-2014-3195: Information Leak in V8.
  - Medium CVE-2014-3197: Information Leak in XSS Auditor.
  - Medium CVE-2014-3198: Out-of-bounds read in PDFium.
  - Low CVE-2014-3199: Release Assert in V8 bindings.
- Replace chromium-support-ModeSwitch-key.patch by upstream version from
  commit 8585724

* Fri Sep 26 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.124-alt2
- New version
- Security fixes:
  - CVE-2014-1568: RSA signature malleability in NSS
- Fix path and version detection of PepperFlash

* Tue Sep 23 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.120-alt2
- Fix RightAlt behaviour. See https://code.google.com/p/chromium/issues/detail?id=377203
  for details
- Build PDF viewer plugin

* Thu Sep 18 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.120-alt1
- New version
- Security fixes:
  - High CVE-2014-3178: Use-after-free in rendering.
- Disable bundled binutils and gold

* Wed Aug 27 2014 Andrey Cherepanov <cas@altlinux.org> 37.0.2062.94-alt1
- New version
- Security fixes:
  - Critical CVE-2014-3176, CVE-2014-3177: A special reward to
    lokihardt@asrt for a combination of bugs in V8, IPC, sync, and
    extensions that can lead to remote code execution outside of the
    sandbox.
  - High CVE-2014-3168: Use-after-free in SVG.
  - High CVE-2014-3169: Use-after-free in DOM.
  - High CVE-2014-3170: Extension permission dialog spoofing.
  - High CVE-2014-3171: Use-after-free in bindings.
  - Medium CVE-2014-3172: Issue related to extension debugging.
  - Medium CVE-2014-3173: Uninitialized memory read in WebGL.
  - Medium CVE-2014-3174: Uninitialized memory read in Web Audio.

* Mon Aug 18 2014 Andrey Cherepanov <cas@altlinux.org> 36.0.1985.143-alt1
- New version
- Security fixes:
  - High CVE-2014-3165: Use-after-free in web sockets.
  - High CVE-2014-3166: Information disclosure in SPDY.

* Fri Jul 25 2014 Andrey Cherepanov <cas@altlinux.org> 36.0.1985.125-alt2
- Fix small user interface fonts (see https://code.google.com/p/chromium/issues/detail?id=375824)

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 36.0.1985.125-alt1
- New version
- Security fixes:
  - Medium CVE-2014-3160: Same-Origin-Policy bypass in SVG.
- Fix wrong Russian translation (ALT #30182)
- Add flags to avoid memory exhaustion while linking on i586
- Use internal version of v8 library

* Mon Jul 14 2014 Andrey Cherepanov <cas@altlinux.org> 35.0.1916.153-alt1
- New version
- Security fixes:
  - High CVE-2014-3154: Use-after-free in filesystem api.
  - High CVE-2014-3155: Out-of-bounds read in SPDY.
  - Medium CVE-2014-3156: Buffer overflow in clipboard.
  - CVE-2014-3157: Heap overflow in media.

* Wed May 21 2014 Andrey Cherepanov <cas@altlinux.org> 35.0.1916.114-alt1
- New version
- Security fixes:
  - High CVE-2014-1743: Use-after-free in styles.
  - High CVE-2014-1744: Integer overflow in audio.
  - High CVE-2014-1745: Use-after-free in SVG.
  - Medium CVE-2014-1746: Out-of-bounds read in media filters.
  - Medium CVE-2014-1747: UXSS with local MHTML file.
  - Medium CVE-2014-1748: UI spoofing with scrollbar.

* Wed May 14 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.137-alt1
- New version
- Security fixes:
  - High CVE-2014-1740: Use-after-free in WebSockets.
  - High CVE-2014-1741: Integer overflow in DOM ranges.
  - High CVE-2014-1742: Use-after-free in editing.

* Fri May 02 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.132-alt2
- Add support for playing mp3 and mpeg4 (ALT #27863)
- Package icudtl.dat

* Wed Apr 30 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.132-alt1
- New version
- Security fixes:
  - High CVE-2014-1731: Type confusion in DOM.
  - Medium CVE-2014-1732: Use-after-free in Speech Recognition.
  - Medium CVE-2014-1733: Compiler bug in Seccomp-BPF.

* Tue Apr 15 2014 Andrey Cherepanov <cas@altlinux.org> 34.0.1847.116-alt1
- New version
- Security fixes:
  - High CVE-2014-1718: Integer overflow in compositor.
  - High CVE-2014-1719: Use-after-free in web workers.
  - High CVE-2014-1720: Use-after-free in DOM.
  - High CVE-2014-1722: Use-after-free in rendering.
  - High CVE-2014-1723: Url confusion with RTL characters.
  - High CVE-2014-1724: Use-after-free in speech.
  - Medium CVE-2014-1725: OOB read with window property.
  - Medium CVE-2014-1726: Local cross-origin bypass.
  - Medium CVE-2014-1727: Use-after-free in forms.
- Package depot-tools to correct build
- Do not show apps shortcut button on bookmark bar by default
- Switch build from make to ninja-build

* Tue Mar 18 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.152-alt1
- New version
- Security fixes:
  - High CVE-2014-1713: Use-after-free in Blink bindings
  - High CVE-2014-1705: Memory corruption in V8
  - High CVE-2014-1715: Directory traversal issue

* Wed Mar 12 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.149-alt1
- New version
- Security fixes:
  - High CVE-2014-1700: Use-after-free in speech.
  - High CVE-2014-1701: UXSS in events.
  - High CVE-2014-1702: Use-after-free in web database.

* Tue Mar 04 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.146-alt1
- New version
- Security fixes:
  - High CVE-2013-6663: Use-after-free in svg images.
  - High CVE-2013-6664: Use-after-free in speech recognition.
  - High CVE-2013-6665: Heap buffer overflow in software rendering.
  - Medium CVE-2013-6666: Chrome allows requests in flash header request.

* Fri Feb 21 2014 Andrey Cherepanov <cas@altlinux.org> 33.0.1750.117-alt1
- New version
- Security fixes:
  - High CVE-2013-6653: Use-after-free related to web contents.
  - High CVE-2013-6654: Bad cast in SVG.
  - High CVE-2013-6655: Use-after-free in layout.
  - High CVE-2013-6656: Information leak in XSS auditor.
  - Medium CVE-2013-6657: Information leak in XSS auditor.
  - Medium CVE-2013-6658: Use-after-free in layout.
  - Medium CVE-2013-6659: Issue with certificates validation in TLS handshake.
  - Low CVE-2013-6660: Information leak in drag and drop.
- Update patches from SUSE, Debian and Arch

* Tue Jan 28 2014 Andrey Cherepanov <cas@altlinux.org> 32.0.1700.102-alt1
- New version
- Security fixes:
  - High CVE-2013-6649: Use-after-free in SVG images.
- Fixes:
  - Mouse Pointer disappears after exiting full-screen mode. (317496)
  - Drag and drop files into Chrome may not work properly. (332579)
  - Quicktime Plugin crashes in Chrome. (308466)
  - Chrome becomes unresponsive. (335248)
  - Trackpad users may not be able to scroll horizontally. (332797)
  - Scrolling does not work in combo box. (334454)
  - Chrome does not work with all CSS minifiers such as whitespace
    around a media query's `and` keyword. (333035)

* Tue Jan 21 2014 Andrey Cherepanov <cas@altlinux.org> 32.0.1700.77-alt1
- New version
- Security fixes:
  - High CVE-2013-6646: Use-after-free in web workers.
  - High CVE-2013-6641: Use-after-free related to forms.
  - High CVE-2013-6643: Unprompted sync with an attacker's Google account.
  - Medium CVE-2013-6645 Use-after-free related to speech input elements.
- Set interpreter /bin/bash for main executable for correct ulimit call

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 31.0.1650.63-alt1
- New version
- Security fixes:
  - Medium CVE-2013-6634: Session fixation in sync related to 302 redirects.
  - High CVE-2013-6635: Use-after-free in editing.
  - Medium CVE-2013-6636: Address bar spoofing related to modal dialogs.
- Increase default nproc limit from 1024 to 1536
- Remove SVN commit from release number

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 31.0.1650.57-alt1.r235101
- New version
- Security fixes:
  - Critical CVE-2013-6632: Multiple memory corruption issues

* Wed Nov 13 2013 Andrey Cherepanov <cas@altlinux.org> 31.0.1650.48-alt1.r233213
- New version
- Security fixes:
  - Medium CVE-2013-6621: Use after free related to speech input elements.
  - High CVE-2013-6622: Use after free related to media elements.
  - High CVE-2013-6623: Out of bounds read in SVG.
  - High CVE-2013-6624: Use after free related to "id" attribute strings.
  - High CVE-2013-6625: Use after free in DOM ranges.
  - Low CVE-2013-6626: Address bar spoofing related to interstitial warnings.
  - High CVE-2013-6627: Out of bounds read in HTTP parsing.
  - Medium CVE-2013-6628: Issue with certificates not being checked during TLS renegotiation.

* Fri Oct 25 2013 Andrey Cherepanov <cas@altlinux.org> 30.0.1599.114-alt1.r229842
- New version
- Move chrome_sandbox to %%_libdir/chromium/chrome-sandbox

* Fri Oct 11 2013 Andrey Cherepanov <cas@altlinux.org> 30.0.1599.66-alt1.r225456
- New version
- Security fixes:
  - Medium CVE-2013-2906: Races in Web Audio.
  - Medium CVE-2013-2907: Out of bounds read in Window.prototype object.
  - Medium CVE-2013-2908: Address bar spoofing related to the "204 No Content" status code.
  - High CVE-2013-2909: Use after free in inline-block rendering.
  - Medium CVE-2013-2910: Use-after-free in Web Audio.
  - High CVE-2013-2911: Use-after-free in XSLT.
  - High CVE-2013-2912: Use-after-free in PPAPI.
  - High CVE-2013-2913: Use-after-free in XML document parsing.
  - Low CVE-2013-2915: Address bar spoofing via a malformed scheme.
  - High CVE-2013-2916: Address bar spoofing related to the "204 No Content" status code.
  - Medium CVE-2013-2917: Out of bounds read in Web Audio.
  - High CVE-2013-2918: Use-after-free in DOM.
  - High CVE-2013-2919: Memory corruption in V8.
  - Medium CVE-2013-2920: Out of bounds read in URL parsing.
  - High CVE-2013-2921: Use-after-free in resource loader.
  - High CVE-2013-2922: Use-after-free in template element.
  - CVE-2013-2923: Various fixes from internal audits, fuzzing and other initiatives.

* Wed Sep 25 2013 Andrey Cherepanov <cas@altlinux.org> 29.0.1547.76-alt2.r223446
- New version 29.0.1547.76

* Tue Sep 03 2013 Andrey Cherepanov <cas@altlinux.org> 29.0.1547.65-alt1.r220622
- New version 29.0.1547.62
- Security fixes:
  - High CVE-2013-2900: Incomplete path sanitization in file handling.
  - Low CVE-2013-2905: Information leak via overly broad permissions on
    shared memory files.
  - High CVE-2013-2901: Integer overflow in ANGLE.
  - High CVE-2013-2902: Use after free in XSLT.
  - High CVE-2013-2903: Use after free in media element.
  - High CVE-2013-2904: Use after free in document parsing.
- Improved Omnibox suggestions based on the recency of sites you have
  visited
- Ability to reset your profile back to its original state
- Many new apps and extensions APIs
- Lots of stability and performance improvements
- Fix an issue with printing from Google Docs applications
- Fix an issue with Sync

* Wed Jul 31 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 28.0.1500.95-alt2.r213514
- rebuild with versioned v8

* Wed Jul 31 2013 Andrey Cherepanov <cas@altlinux.org> 28.0.1500.95-alt1.r213514
- New version 28.0.1500.95
- Security fixes:
  - Medium CVE-2013-2881: Origin bypass in frame handling.
  - High CVE-2013-2883: Use-after-free in MutationObserver.
  - High CVE-2013-2884: Use-after-free in DOM.
  - High CVE-2013-2885: Use-after-free in input handling.

* Wed Jul 24 2013 Andrey Cherepanov <cas@altlinux.org> 28.0.1500.71-alt1.r209842
- New version 28.0.1500.71
- Security fixes:
  - High CVE-2013-2879: Confusion setting up sign-in and sync.
  - Medium CVE-2013-2868: Incorrect sync of NPAPI extension component.
  - Medium CVE-2013-2869: Out-of-bounds read in JPEG2000 handling.
  - Critical CVE-2013-2870: Use-after-free with network sockets.
  - Medium CVE-2013-2853: Man-in-the-middle attack against HTTP in SSL.
  - High CVE-2013-2871: Use-after-free in input handling.
  - High CVE-2013-2873: Use-after-free in resource loading.
  - Medium CVE-2013-2875: Out-of-bounds-read in SVG.
  - Medium CVE-2013-2876: Extensions permissions confusion with interstitials.
  - Low CVE-2013-2877: Out-of-bounds read in XML parsing.
  - None: Remove the "viewsource" attribute on iframes.
  - Medium CVE-2013-2878: Out-of-bounds read in text handling.
  - High CVE-2013-2880: Various fixes from internal audits, fuzzing and other initiatives

* Wed Jun 05 2013 Andrey Cherepanov <cas@altlinux.org> 27.0.1453.110-alt1.r202711
- New version 27.0.1453.110
- Security fixes:
  - Critical CVE-2013-2863: Memory corruption in SSL socket handling.
  - High CVE-2013-2856: Use-after-free in input handling.
  - High CVE-2013-2857: Use-after-free in image handling.
  - High CVE-2013-2858: Use-after-free in HTML5 Audio.
  - High CVE-2013-2859: Cross-origin namespace pollution.
  - High CVE-2013-2860: Use-after-free with workers accessing database APIs.
  - High CVE-2013-2861: Use-after-free with SVG.
  - High CVE-2013-2862: Memory corruption in Skia GPU handling.
  - High CVE-2013-2864: Bad free in PDF viewer.
  - High CVE-2013-2865: Various fixes from internal audits, fuzzing and other initiatives. 
  - Medium CVE-2013-2855: Memory corruption in dev tools API.

* Thu May 30 2013 Andrey Cherepanov <cas@altlinux.org> 27.0.1453.93-alt1.r200836
- New version 27.0.1453.93
- Security fixes:
  - High CVE-2013-2836: Various fixes from internal audits, fuzzing and
    other initiatives.
  - High CVE-2013-2837: Use-after-free in SVG.
  - High CVE-2013-2839: Bad cast in clipboard handling.
  - High CVE-2013-2840: Use-after-free in media loader.
  - High CVE-2013-2841: Use-after-free in Pepper resource handling.
  - High CVE-2013-2842: Use-after-free in widget handling.
  - High CVE-2013-2843: Use-after-free in speech handling.
  - High CVE-2013-2844: Use-after-free in style resolution.
  - High CVE-2013-2845: Memory safety issues in Web Audio.
  - High CVE-2013-2846: Use-after-free in media loader.
  - High CVE-2013-2847: Use-after-free race condition with workers.
  - Medium CVE-2013-2848: Possible data extraction with XSS Auditor.
  - Low CVE-2013-2849: Possible XSS with drag+drop or copy+paste.
- Web pages load 5%% faster on average
- New chrome.syncFileSystem API
- Improved ranking of predictions, improved spell correction, and
  numerous fundamental improvements for Omnibox predictions. Please see
  the Help Center for more information on our updated policies.

* Mon May 13 2013 Andrey Cherepanov <cas@altlinux.org> 26.0.1410.57-alt1.r191765
- New version 26.0.1410.57
- Security fixes:
  - High CVE-2013-0927: Unsafe config option loading in Pango.
- Requires new version speech-dispatcher

* Sun Mar 31 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt4.r187217
- Rebuild with libv8-3.15

* Wed Mar 27 2013 Andrey Cherepanov <cas@altlinux.org> 26.0.1410.43-alt1.r189671
- New version 26.0.1410.43
- Security fixes:
  - Medium CVE-2013-0926: Avoid pasting active tags in certain situations.
  - Low CVE-2013-0925: Avoid leaking URLs to extensions without the tabs permissions.
  - Low CVE-2013-0924: Check an extension's permissions API usage again file permissions.
  - Medium CVE-2013-0923: Memory safety issues in the USB Apps API.
  - Low CVE-2013-0922: Avoid HTTP basic auth brute force attempts.
  - High CVE-2013-0921: Ensure isolated web sites run in their own processes.
  - Medium CVE-2013-0920: Use-after-free in extension bookmarks API.
  - Medium CVE-2013-0919: Use-after-free with pop-up windows in extensions.
  - Low CVE-2013-0918: Do not navigate dev tools upon drag and drop.
  - Low CVE-2013-0917: Out-of-bounds read in URL loader.
  - High CVE-2013-0916: Use-after-free in Web Audio.

* Thu Mar 21 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt3.r187217
- Add note that the keys for Google API are only to be used for ALT Linux
- Fix run script if CHROMIUM_ULIMIT is not set in /etc/chromium/default

* Wed Mar 20 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt2.r187217
- Build with access to Google API

* Wed Mar 13 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt1.r187217
- New version 25.0.1364.172

* Mon Mar 11 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.160-alt1.r186726
- New version 25.0.1364.160
- Security fixes:
  - CVE-2013-0912: Type confusion in WebKit.
- Build with system libpng12 (old version)

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.152-alt1.r185281
- New version 25.0.1364.152
- Security fixes:
  - High CVE-2013-0902: Use-after-free in frame loader.
  - High CVE-2013-0903: Use-after-free in browser navigation handling.
  - High CVE-2013-0904: Memory corruption in Web Audio.
  - High CVE-2013-0905: Use-after-free with SVG animations.
  - High CVE-2013-0906: Memory corruption in Indexed DB.
  - Medium CVE-2013-0907: Race condition in media thread handling.
  - Medium CVE-2013-0908: Incorrect handling of bindings for extension processes.
  - Low CVE-2013-0909: Referer leakage with XSS Auditor.
  - Medium CVE-2013-0910: Mediate renderer -> browser plug-in loads more strictly.
  - High CVE-2013-0911: Possible path traversal in database handling.
- Use builtin libpng

* Fri Feb 22 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.97-alt1.r183676
- New version 25.0.1364.97
- Security fixes:
  - High CVE-2013-0879: Memory corruption with web audio node.
  - High CVE-2013-0880: Use-after-free in database handling.
  - Medium CVE-2013-0881: Bad read in Matroska handling.
  - High CVE-2013-0882: Bad memory access with excessive SVG parameters.
  - Medium CVE-2013-0883: Bad read in Skia.
  - Low CVE-2013-0884: Inappropriate load of NaCl.
  - Medium CVE-2013-0885: Too many API permissions granted to web store.
  - Low CVE-2013-0887: Developer tools process has too many permissions
    and places too much trust in the connected server.
  - Medium CVE-2013-0888: Out-of-bounds read in Skia.
  - Low CVE-2013-0889: Tighten user gesture check for dangerous file
    downloads.
  - High CVE-2013-0890: Memory safety issues across the IPC layer.
  - High CVE-2013-0891: Integer overflow in blob handling.
  - Medium CVE-2013-0892: Lower severity issues across the IPC layer.
  - Medium CVE-2013-0893: Race condition in media handling.
  - High CVE-2013-0894: Buffer overflow in vorbis decoding.
  - High CVE-2013-0895: Incorrect path handling in file copying.
  - High CVE-2013-0896: Memory management issues in plug-in message
    handling.
  - Low CVE-2013-0897: Off-by-one read in PDF.
  - High CVE-2013-0898: Use-after-free in URL handling.
  - Low CVE-2013-0899: Integer overflow in Opus handling.
  - Medium CVE-2013-0900: Race condition in ICU.

* Thu Jan 31 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.57-alt1.r178923
- New version 24.0.1312.57
- Remove revision number from tarball name

* Wed Jan 23 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.56-alt1.r177594
- New version 24.0.1312.56
- Security fixes:
  - High CVE-2013-0839: Use-after-free in canvas font handling.
  - Medium CVE-2013-0840: Missing URL validation when opening new windows.
  - High CVE-2013-0841: Unchecked array index in content blocking.
  - Medium CVE-2013-0842: Problems with NULL characters embedded in paths.

* Mon Jan 14 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.52-alt1.r175374
- New version 24.0.1312.52
- Security fixes:
  - High CVE-2012-5145: Use-after-free in SVG layout.
  - High CVE-2012-5146: Same origin policy bypass with malformed URL.
  - High CVE-2012-5147: Use-after-free in DOM handling.
  - Medium CVE-2012-5148: Missing filename sanitization in hyphenation support.
  - High CVE-2012-5149: Integer overflow in audio IPC handling.
  - High CVE-2012-5150: Use-after-free when seeking video.
  - High CVE-2012-5151: Integer overflow in PDF JavaScript.
  - Medium CVE-2012-5152: Out-of-bounds read when seeking video.
  - High CVE-2012-5156: Use-after-free in PDF fields.
  - Medium CVE-2012-5157: Out-of-bounds reads in PDF image handling.
  - High CVE-2013-0828: Bad cast in PDF root handling.
  - High CVE-2013-0829: Corruption of database metadata leading to incorrect file access.
  - Low CVE-2013-0831: Possible path traversal from extension process.
  - Medium CVE-2013-0832: Use-after-free with printing.
  - Medium CVE-2013-0833: Out-of-bounds read with printing.
  - Medium CVE-2013-0834: Out-of-bounds read with glyph handling.
  - Low CVE-2013-0835: Browser crash with geolocation.
  - Medium CVE-2013-0837: Crash in extension tab handling.
  - Low CVE-2013-0838: Tighten permissions on shared memory segments.
- Fixes:
  - Add new option CHROMIUM_ULIMIT in /etc/chromium/default for increase
    for example maximum number of open file descriptors ("-n 1024"
    is recommended for many opened tabs) if needed.

* Wed Dec 12 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.97-alt1.r171054
- New version 23.0.1271.97
- Security fixes:
  - High CVE-2012-5139: Use-after-free with visibility events.
  - High CVE-2012-5140: Use-after-free in URL loader.
  - Medium CVE-2012-5141: Limit Chromoting client plug-in instantiation.
  - Critical CVE-2012-5142: Crash in history navigation.
  - Medium CVE-2012-5143: Integer overflow in PPAPI image buffers.
  - High CVE-2012-5144: Stack corruption in AAC decoding.
- Fixes:
  - Some texts in a Website Settings popup are trimmed
  - <input> selection renders white text on white bg in apps
  - some plugins stopped working

* Fri Nov 30 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.95-alt1.r169798
- New version 23.0.1271.95
- Security fixes:
  - High CVE-2012-5138: Incorrect file path handling.
  - High CVE-2012-5137: Use-after-free in media source handling.
  - High CVE-2012-5133: Use-after-free in SVG filters.

* Thu Nov 08 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.64-alt1.r165196
- New version 23.0.1271.64
- Fixes:
  - High CVE-2012-5116: Use-after-free in SVG filter handling.
  - High CVE-2012-5121: Use-after-free in video layout.
  - High CVE-2012-5124: Memory corruption in texture handling.
  - Critical CVE-2012-5112: SVG use-after-free and IPC arbitrary file
    write.
  - High CVE-2012-2900: Crash in Skia text rendering.
  - Critical CVE-2012-5108: Race condition in audio device handling.
  - High CVE-2012-2896: Integer overflow in WebGL
  - High CVE-2012-2895: Out-of-bounds writes in PDF viewer.
  - High CVE-2012-2894: Crash in graphics context handling.
  - High CVE-2012-2893: Double free in XSL transforms.
  - High CVE-2012-2890: Use-after-free in PDF viewer.
  - High CVE-2012-2889: UXSS in frame handling.
  - High CVE-2012-2888: Use-after-free in SVG text references.
  - High CVE-2012-2887: Use-after-free in onclick handling.
  - High CVE-2012-2886: UXSS in v8 bindings.
  - High CVE-2012-2883: Out-of-bounds write in Skia.
  - High CVE-2012-2882: Wild pointer in OGG container handling.
  - High CVE-2012-2881: DOM tree corruption with plug-ins.
  - High CVE-2012-2878: Use-after-free in plug-in handling.
  - High CVE-2012-2876: Buffer overflow in SSE2 optimizations.
  - High CVE-2012-2874: Out-of-bounds write in Skia.
- Total move to system v8
- Use builtin icu-4.6 and patched zlib (see http://code.google.com/p/chromium/issues/detail?id=143623)

* Wed Oct 03 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt4.r154005
- Set flags for build on ARM
- Rebuild with new version of v8

* Tue Oct 02 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt3.r154005
- Enable video and audio support in HTML5

* Thu Sep 13 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt2.r154005
- Disable debug version and fix problem with Google accounts (ALT 27731)
- Build with system icu libraries
- Open blank initial tab and distribution start page
- Add ALT-specific initial bookmarks

* Fri Sep 07 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt1.r154005
- New version 21.0.1180.89
- Fixes:
  - Several Pepper Flash fixes (Issue 140577, 144107, 140498, 142479)
  - Microphone issues with tinychat.com (Issue: 143192)
  - Devtools regression with "save as" of edited source (issue: 141180)
  - Mini ninjas shaders fails (Issue: 142705)
  - Page randomly turns red/green gradient boxes (Issue: 110343)
  - Medium CVE-2012-2865: Out-of-bounds read in line breaking.
  - High CVE-2012-2866: Bad cast with run-ins.
  - Low CVE-2012-2867: Browser crash with SPDY.
  - Medium CVE-2012-2868: Race condition with workers and XHR.
  - High CVE-2012-2869: Avoid stale buffer in URL loading.
  - Low CVE-2012-2870: Lower severity memory management issues in XPath.
  - High CVE-2012-2871: Bad cast in XSL transforms.
  - Medium CVE-2012-2872: XSS in SSL interstitial.
- Export patches and flags from Debian
- Disable tcmalloc

* Fri Aug 24 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.81-alt1.r151980
- New version 21.0.1180.81
- Disable plugin installation
- Fix tcmalloc because glibc 2.16 removed the undocumented definition of
  'struct siginfo' from <bits/siginfo.h>

* Wed Aug 15 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt5.r139751
- Set appropriate desktop file name for default browser check

* Mon Aug 13 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt4.r139751
- Fix crash when displaying system print dialog on Linux
  (http://code.google.com/p/chromium/issues/detail?id=130095)
- Rename .desktop file and add localization strings

* Fri Aug 10 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt3.r139751
- Add missing file chrome_sandbox

* Thu Aug 09 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt2.r139751
- Rename DE specific packages and set appropriate requirement to wallet subsystem
- Set alternatives to chromium-kde and chromium-gnome
- Add default parameters support in /etc/chromium/default

* Wed Aug 08 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt1.r139751
- Build for Sisyphus version 21.0.1158.0 (import from SUSE)
- Rename to chromium

