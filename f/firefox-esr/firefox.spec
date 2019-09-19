%define rname firefox
%set_verify_elf_method relaxed

%define firefox_cid     \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define firefox_prefix  %_libdir/firefox
%define firefox_datadir %_datadir/firefox

%define gst_version 1.0
%define nspr_version 4.21
%define nss_version 3.45.0
%define rust_version  1.35.0
%define cargo_version 1.35.0

Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name:           firefox-esr
Version:        68.1.0
Release:        alt2
License:        MPL/GPL/LGPL
Group:          Networking/WWW
URL:            http://www.mozilla.org/projects/firefox/

Packager:	Andrey Cherepanov <cas@altlinux.ru>

Source0:        firefox-source.tar
Source1:        rpm-build.tar
Source2:        searchplugins.tar
Source3:        cbindgen-vendor.tar
Source4:        firefox-mozconfig
Source5:        distribution.ini
Source6:        firefox.desktop
Source7:        firefox-wayland.desktop
Source8:        firefox.c
Source9:        firefox-prefs.js

### Start Patches
Patch001: 0001-ALT-fix-werror-return-type.patch
Patch002: 0002-SUSE-NonGnome-KDE-integration.patch
Patch003: 0003-ALT-Use-system-nspr-headers.patch
Patch004: 0004-FEDORA-build-arm-libopus.patch
Patch005: 0005-FEDORA-build-arm.patch
Patch006: 0006-MOZILLA-1196777-GTK3-keyboard-input-focus-sticks-on-.patch
Patch007: 0007-ALT-ppc64le-fix-clang-error-invalid-memory-operand.patch
Patch008: 0008-ALT-ppc64le-disable-broken-getProcessorLineSize-code.patch
Patch010: 0010-ALT-Fix-aarch64-build.patch
### End Patches

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: clang7.0
BuildRequires: clang7.0-devel
BuildRequires: llvm7.0-devel
BuildRequires: lld-devel
%ifarch %{ix86}
BuildRequires: gcc
BuildRequires: gcc-c++
%endif
BuildRequires: libstdc++-devel
BuildRequires: rpm-macros-alternatives
BuildRequires: rust >= %rust_version
BuildRequires: rust-cargo >= %cargo_version
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libcurl-devel libgtk+2-devel libgtk+3-devel libhunspell-devel libjpeg-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: zip unzip
BuildRequires: bzlib-devel zlib-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: libproxy-devel
BuildRequires: libshell
BuildRequires: libvpx5-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel
BuildRequires: gstreamer%gst_version-devel gst-plugins%gst_version-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
#BuildRequires: libicu-devel
BuildRequires: libdbus-devel libdbus-glib-devel
BuildRequires: node
BuildRequires: nasm
BuildRequires: libxkbcommon-devel

# Python requires
BuildRequires: /dev/shm
BuildRequires: python3-base
BuildRequires: python-module-distribute
BuildRequires: python-module-pip
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json


# Rust requires
BuildRequires: /proc

# Mozilla requires
BuildRequires: pkgconfig(nspr) >= %nspr_version
BuildRequires: pkgconfig(nss) >= %nss_version
BuildRequires: libnss-devel-static

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

Obsoletes:	firefox-3.6 firefox-4.0 firefox-5.0
Conflicts:	firefox-settings-desktop

Provides:	webclient
Provides:	firefox = %EVR
Conflicts:	firefox
Requires:	mozilla-common

# ALT#30732
Requires:	gst-plugins-ugly%gst_version

Requires: libnspr >= %nspr_version
Requires: libnss >= %nss_version

%description
The Mozilla Firefox project is a redesign of Mozilla's browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF-8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация браузера Mozilla,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package wayland
Summary:    Firefox Wayland launcher.
Group:      Networking/WWW
BuildArch:  noarch
Requires:   %name

%description wayland
The firefox-wayland package contains launcher and desktop file
to run Firefox natively on Wayland.

%prep
%setup -q -n firefox-%version -c

### Begin to apply patches
%patch001 -p1
%patch002 -p1
%patch003 -p1
%patch004 -p1
%patch005 -p1
%patch006 -p1
%patch007 -p1
%patch008 -p1
%patch010 -p1
### Finish apply patches

cd mozilla

tar -xf %SOURCE1
tar -xf %SOURCE2

cp -f %SOURCE4 .mozconfig

cat >> .mozconfig <<'EOF'
ac_add_options --prefix="%_prefix"
ac_add_options --libdir="%_libdir"
%ifnarch %{ix86} ppc64le
ac_add_options --enable-linker=lld
%ifnarch x86_64
ac_add_options --disable-webrtc
%endif
%endif
%ifarch %{ix86} x86_64
ac_add_options --disable-elf-hack
%endif
EOF

mkdir -p -- my_rust_vendor
tar --strip-components=1 -C my_rust_vendor --overwrite -xf %SOURCE3

mkdir -p -- .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/my_rust_vendor"
EOF

%build
cd mozilla

%add_optflags %optflags_shared
%add_findprov_lib_path %firefox_prefix

env CARGO_HOME="$PWD/.cargo" \
	cargo install cbindgen

export MOZ_BUILD_APP=browser

MOZ_OPT_FLAGS="-pipe -O2 -g0"

# PIE, full relro
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -DPIC -fPIC -Wl,-z,relro -Wl,-z,now"

# Add fake RPATH
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wl,-rpath,/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"

# If MOZ_DEBUG_FLAGS is empty, firefox's build will default it to "-g" which
# overrides the -g0 from line above and breaks building on s390
# (OOM when linking, rhbz#1238225)
export MOZ_DEBUG_FLAGS=" "

export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"
# Add fake RPATH
rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
%if_without system_nss
# see mozilla/security/nss/coreconf/Linux.mk:203
export RPATH="-Wl,-rpath,$rpath"
%endif

#ifnarch %{ix86}
export CC="clang"
export CXX="clang++"
#else
#export CC="gcc"
#export CXX="g++"
#endif

export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh
export RUST_BACKTRACE=1
export RUSTFLAGS="-Cdebuginfo=0"
export BUILD_VERBOSE_LOG=1
export MOZ_MAKE_FLAGS="-j8"
export PATH="$PWD/.cargo/bin:$PATH"

autoconf old-configure.in > old-configure
pushd js/src
autoconf old-configure.in > old-configure
popd

./mach build

$CC $CFLAGS \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%firefox_prefix/firefox\" \
	-DMOZ_DIST_BIN=\"%firefox_prefix\"\
	%SOURCE8 -o firefox


%install
cd mozilla

export SHELL=/bin/sh

mkdir -p \
	%buildroot/%mozilla_arch_extdir/%firefox_cid \
	%buildroot/%mozilla_noarch_extdir/%firefox_cid \
	#

make -C objdir \
	DESTDIR=%buildroot \
	INSTALL="/bin/install -p" \
	mozappdir=%firefox_prefix \
	libdir=%_libdir \
	install

# install altlinux-specific configuration
install -D -m 644 %SOURCE9 %buildroot/%firefox_prefix/browser/defaults/preferences/all-altlinux.js

cat > %buildroot/%firefox_prefix/browser/defaults/preferences/firefox-l10n.js <<EOF
pref("intl.locale.matchOS", true);
pref("intl.locale.requested", "");
pref("general.useragent.locale", "chrome://global/locale/intl.properties");
EOF

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		browser/branding/official/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/firefox.png
done

# ALT#30572
if [ ! -e "%buildroot/%firefox_prefix/plugins" ]; then
	what="$(relative %browser_plugins_path %firefox_prefix/plugins)"
	ln -s -- "$what" %buildroot/%firefox_prefix/plugins
fi

# install rpm-build-firefox
mkdir -p -- \
	%buildroot/%_rpmmacrosdir
sed \
	-e 's,@firefox_version@,%version,' \
	-e 's,@firefox_release@,%release,' \
	rpm-build/rpm.macros.firefox.standalone > %buildroot/%_rpmmacrosdir/firefox

install -m755 firefox %buildroot/%_bindir/firefox

cd %buildroot

# Wrapper for wayland
cat > ./%_bindir/firefox-wayland <<'EOF'
#!/bin/sh
export GDK_BACKEND=wayland
export MOZ_ENABLE_WAYLAND=1
export MOZ_GTK_TITLEBAR_DECORATION=client
export XDG_SESSION_TYPE=wayland

unset DISPLAY

exec %_bindir/firefox "$@"
EOF

chmod +x ./%_bindir/firefox-wayland

# Add distribution.ini
mkdir -p -- ./%firefox_prefix/distribution
cp -- %SOURCE5 ./%firefox_prefix/distribution/distribution.ini

# install menu file
install -D -m 644 %SOURCE6 ./%_datadir/applications/firefox.desktop
install -D -m 644 %SOURCE7 ./%_datadir/applications/firefox-wayland.desktop

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/firefox\t100\n' >./%_altdir/firefox

rm -f -- \
	./%firefox_prefix/removed-files

# Remove devel files
rm -rf -- \
	./%_includedir/%rname \
	./%_datadir/idl/%rname \
	./%_libdir/%rname-devel \
#

# Add real RPATH
(set +x
	rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
	find %buildroot/%firefox_prefix -type f |
	while read f; do
		t="$(readlink -ev "$f")"
		file "$t" | fgrep -qs ELF || continue
		if chrpath -l "$t" | fgrep -qs "RPATH=$rpath"; then
			chrpath -r "%firefox_prefix" "$t"
		fi
	done
)

%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%firefox_prefix/$n" ] || rm -f "%firefox_prefix/$n"
done

%files
%_altdir/firefox
%_bindir/firefox
%firefox_prefix
%mozilla_arch_extdir/%firefox_cid
%mozilla_noarch_extdir/%firefox_cid
%_datadir/applications/firefox.desktop
%_iconsdir/hicolor/16x16/apps/firefox.png
%_iconsdir/hicolor/22x22/apps/firefox.png
%_iconsdir/hicolor/24x24/apps/firefox.png
%_iconsdir/hicolor/32x32/apps/firefox.png
%_iconsdir/hicolor/48x48/apps/firefox.png
%_iconsdir/hicolor/256x256/apps/firefox.png

%files wayland
%_bindir/firefox-wayland
%_datadir/applications/firefox-wayland.desktop

%changelog
* Thu Sep 19 2019 Andrey Cherepanov <cas@altlinux.org> 68.1.0-alt2
- Fix open context menu (thanks george@).

* Wed Sep 04 2019 Andrey Cherepanov <cas@altlinux.org> 68.1.0-alt1
- New ESR version (68.1.0).
- Fixed:
  + CVE-2019-11751 Malicious code execution through command line parameters
  + CVE-2019-11746 Use-after-free while manipulating video
  + CVE-2019-11744 XSS by breaking out of title and textarea elements using innerHTML
  + CVE-2019-11742 Same-origin policy violation with SVG filters and canvas to steal cross-origin images
  + CVE-2019-11736 File manipulation and privilege escalation in Mozilla Maintenance Service
  + CVE-2019-11753 Privilege escalation with Mozilla Maintenance Service in custom Firefox installation location
  + CVE-2019-11752 Use-after-free while extracting a key value in IndexedDB
  + CVE-2019-9812 Sandbox escape through Firefox Sync
  + CVE-2019-11743 Cross-origin access to unload event attributes
  + CVE-2019-11748 Persistence of WebRTC permissions in a third party context
  + CVE-2019-11749 Camera information available without prompting using getUserMedia
  + CVE-2019-11750 Type confusion in Spidermonkey
  + CVE-2019-11738 Content security policy bypass through hash-based sources in directives
  + CVE-2019-11747 'Forget about this site' removes sites from pre-loaded HSTS list
  + CVE-2019-11735 Memory safety bugs fixed in Firefox 69 and Firefox ESR 68.1
  + CVE-2019-11740 Memory safety bugs fixed in Firefox 69, Firefox ESR 68.1, and Firefox ESR 60.9
- Build in 8 jobs.

* Thu Aug 15 2019 Andrey Cherepanov <cas@altlinux.org> 68.0.2-alt1
- New ESR version (68.0.2).
- Fixed:
  + CVE-2019-11733 Stored passwords in 'Saved Logins' can be copied without master password entry

* Fri Jul 19 2019 Andrey Cherepanov <cas@altlinux.org> 68.0.1-alt1
- New ESR version (68.0.1).
- Fixed:
  + CVE-2019-9811 Sandbox escape via installation of malicious language pack
  + CVE-2019-11711 Script injection within domain through inner window reuse
  + CVE-2019-11712 Cross-origin POST requests can be made with NPAPI plugins by following 308 redirects
  + CVE-2019-11713 Use-after-free with HTTP/2 cached stream
  + CVE-2019-11729 Empty or malformed p256-ECDH public keys may trigger a segmentation fault
  + CVE-2019-11715 HTML parsing error can contribute to content XSS
  + CVE-2019-11717 Caret character improperly escaped in origins
  + CVE-2019-11719 Out-of-bounds read when importing curve25519 private key
  + CVE-2019-11730 Same-origin policy treats all files in a directory as having the same-origin
  + CVE-2019-11709 Memory safety bugs fixed in Firefox 68 and Firefox ESR 60.8

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 60.8.0-alt2
- Fix Russian description encoding.

* Tue Jul 09 2019 Andrey Cherepanov <cas@altlinux.org> 60.8.0-alt1
- New ESR version (60.8.0).
- Fixed:
  + CVE-2019-9811 Sandbox escape via installation of malicious language pack
  + CVE-2019-11711 Script injection within domain through inner window reuse
  + CVE-2019-11712 Cross-origin POST requests can be made with NPAPI plugins by following 308 redirects
  + CVE-2019-11713 Use-after-free with HTTP/2 cached stream
  + CVE-2019-11729 Empty or malformed p256-ECDH public keys may trigger a segmentation fault
  + CVE-2019-11715 HTML parsing error can contribute to content XSS
  + CVE-2019-11717 Caret character improperly escaped in origins
  + CVE-2019-11719 Out-of-bounds read when importing curve25519 private key
  + CVE-2019-11730 Same-origin policy treats all files in a directory as having the same-origin
  + CVE-2019-11709 Memory safety bugs fixed in Firefox 68 and Firefox ESR 60.8

* Wed Jul 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 60.7.2-alt2
- Added ppc64le support.
- spec: cleaned up rpm-build internal macros.

* Thu Jun 20 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.2-alt1
- New ESR version (60.7.2).
- Fixed:
  + CVE-2019-11708 sandbox escape using Prompt:Open

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.1-alt1
- New ESR version (60.7.1).
- Fixed:
  + CVE-2019-11707 Type confusion in Array.pop

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.0-alt2
- Fix build with Rust > 1.33.

* Tue May 21 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.0-alt1
- New ESR version (60.7.0).
- Fixed:
  + CVE-2019-9815 Disable hyperthreading on content JavaScript threads on macOS
  + CVE-2019-9816 Type confusion with object groups and UnboxedObjects
  + CVE-2019-9817 Stealing of cross-domain images using canvas
  + CVE-2019-9818 Use-after-free in crash generation server
  + CVE-2019-9819 Compartment mismatch with fetch API
  + CVE-2019-9820 Use-after-free of ChromeEventHandler by DocShell
  + CVE-2019-11691 Use-after-free in XMLHttpRequest
  + CVE-2019-11692 Use-after-free removing listeners in the event listener manager
  + CVE-2019-11693 Buffer overflow in WebGL bufferdata on Linux
  + CVE-2019-7317 Use-after-free in png_image_free of libpng library
  + CVE-2019-9797 Cross-origin theft of images with createImageBitmap
  + CVE-2018-18511 Cross-origin theft of images with ImageBitmapRenderingContext
  + CVE-2019-11694 Uninitialized memory memory leakage in Windows sandbox
  + CVE-2019-11698 Theft of user history data through drag and drop of hyperlinks to and from bookmarks
  + CVE-2019-5798 Out-of-bounds read in Skia
  + CVE-2019-9800 Memory safety bugs fixed in Firefox 67 and Firefox ESR 60.7

* Sun May 05 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.2-alt1
- New ESR version (60.6.2).
- Hotfix for addon signing cert has not been applied.

* Sat Mar 23 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.1-alt1
- New ESR version (60.6.1).
- Fixed:
  + CVE-2019-9810 IonMonkey MArraySlice has incorrect alias information
  + CVE-2019-9813 Ionmonkey type confusion with __proto__ mutations

* Thu Mar 21 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.0-alt1
- New ESR version (60.6.0).
- Fixed:
  + CVE-2019-9790 Use-after-free when removing in-use DOM elements
  + CVE-2019-9791 Type inference is incorrect for constructors entered through on-stack replacement with IonMonkey
  + CVE-2019-9792 IonMonkey leaks JS_OPTIMIZED_OUT magic value to script
  + CVE-2019-9793 Improper bounds checks when Spectre mitigations are disabled
  + CVE-2019-9794 Command line arguments not discarded during execution
  + CVE-2019-9795 Type-confusion in IonMonkey JIT compiler
  + CVE-2019-9796 Use-after-free with SMIL animation controller
  + CVE-2019-9801 Windows programs that are not 'URL Handlers' are exposed to web content
  + CVE-2018-18506 Proxy Auto-Configuration file can define localhost access to be proxied
  + CVE-2019-9788 Memory safety bugs fixed in Firefox 66 and Firefox ESR 60.6

* Wed Feb 27 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.2-alt1.1
- Rebuild vith libvpx5.

* Sat Feb 23 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.2-alt1
- New ESR version (60.5.2).

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.1-alt1
- New ESR version (60.5.1).
- Fixed:
  + CVE-2018-18356 Use-after-free in Skia
  + CVE-2019-5785 Integer overflow in Skia
  + CVE-2018-18335 Buffer overflow in Skia with accelerated Canvas 2D

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.0-alt1
- New ESR version (60.5.0).
- Fixed:
  + CVE-2018-18500 Use-after-free parsing HTML5 stream
  + CVE-2018-18505 Privilege escalation through IPC channel messages
  + CVE-2018-18501 Memory safety bugs fixed in Firefox 65 and Firefox ESR 60.5

* Thu Jan 10 2019 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt2
- Rebuild with llvm7.0 (ALT #35858).
- Build with gcc on %%ix86.

* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt1
- New ESR version (60.4.0)
- Fixed:
  + CVE-2018-17466 Buffer overflow and out-of-bounds read in ANGLE library with TextureStorage11
  + CVE-2018-18492 Use-after-free with select element
  + CVE-2018-18493 Buffer overflow in accelerated 2D canvas with Skia
  + CVE-2018-18494 Same-origin policy violation using location attribute and performance.getEntries to steal cross-origin URLs
  + CVE-2018-18498 Integer overflow when calculating buffer sizes for images
  + CVE-2018-12405 Memory safety bugs fixed in Firefox 64 and Firefox ESR 60.4

* Tue Oct 23 2018 Andrey Cherepanov <cas@altlinux.org> 60.3.0-alt1
- New ESR version (60.3.0).
- Fixed:
  + CVE-2018-12391 HTTP Live Stream audio data is accessible cross-origin
  + CVE-2018-12392 Crash with nested event loops
  + CVE-2018-12393 Integer overflow during Unicode conversion while loading JavaScript
  + CVE-2018-12395 WebExtension bypass of domain restrictions through header rewriting
  + CVE-2018-12396 WebExtension content scripts can execute in disallowed contexts
  + CVE-2018-12397 WebExtension can request access to local files without the warning prompt
  + CVE-2018-12389 Memory safety bugs fixed in Firefox ESR 60.3
  + CVE-2018-12390 Memory safety bugs fixed in Firefox 63 and Firefox ESR 60.3

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.2-alt1
- New ESR version (60.2.2)
- Fixed:
  + CVE-2018-12386 Type confusion in JavaScript
  + CVE-2018-12387 JavaScript JIT compiler inlines Array.prototype.push with multiple arguments

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.1-alt1
- New ESR version (60.2.1).
- Fixed:
  + CVE-2018-12385 Crash in TransportSecurityInfo due to cached data
  + CVE-2018-12383 Setting a master password post-Firefox 58 does not delete unencrypted previously stored passwords

* Mon Sep 10 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.0-alt1
- New ESR version (60.2.0).
- Fixed:
  + CVE-2018-12377 Use-after-free in refresh driver timers
  + CVE-2018-12378 Use-after-free in IndexedDB
  + CVE-2018-12379 Out-of-bounds write with malicious MAR file
  + CVE-2017-16541 Proxy bypass using automount and autofs
  + CVE-2018-12381 Dragging and dropping Outlook email message results in page navigation
  + CVE-2018-12376 Memory safety bugs fixed in Firefox 62 and Firefox ESR 60.2

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 60.1.0-alt1
- New ESR version (60.1.0).
- Fixed:
  + CVE-2018-12359 Buffer overflow using computed size of canvas element
  + CVE-2018-12360 Use-after-free when using focus()
  + CVE-2018-12361 Integer overflow in SwizzleData
  + CVE-2018-12362 Integer overflow in SSSE3 scaler
  + CVE-2018-5156 Media recorder segmentation fault when track type is changed during capture
  + CVE-2018-12363 Use-after-free when appending DOM nodes
  + CVE-2018-12364 CSRF attacks through 307 redirects and NPAPI plugins
  + CVE-2018-12365 Compromised IPC child process can list local filenames
  + CVE-2018-12371 Integer overflow in Skia library during edge builder allocation
  + CVE-2018-12366 Invalid data handling during QCMS transformations
  + CVE-2018-12367 Timing attack mitigation of PerformanceNavigationTiming
  + CVE-2018-12368 No warning when opening executable SettingContent-ms files
  + CVE-2018-12369 WebExtension security permission checks bypassed by embedded experiments
  + CVE-2018-5187 Memory safety bugs fixed in Firefox 60 and Firefox ESR 60.1
  + CVE-2018-5188 Memory safety bugs fixed in Firefox 60, Firefox ESR 60.1, and Firefox ESR 52.9


* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.2-alt2
- Fix build for aarch64 (thanks legion@).

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.2-alt1
- New ESR version (60.0.2).
- Fixed:
  + CVE-2018-6126 Heap buffer overflow rasterizing paths in SVG with Skia

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.1-alt1
- New ESR version (60.0.1).
- Fixed:
  + CVE-2018-5154: Use-after-free with SVG animations and clip paths
  + CVE-2018-5155: Use-after-free with SVG animations and text paths
  + CVE-2018-5157: Same-origin bypass of PDF Viewer to view protected PDF files
  + CVE-2018-5158: Malicious PDF can inject JavaScript into PDF Viewer
  + CVE-2018-5159: Integer overflow and out-of-bounds write in Skia
  + CVE-2018-5160: Uninitialized memory use by WebRTC encoder
  + CVE-2018-5152: WebExtensions information leak through webRequest API
  + CVE-2018-5153: Out-of-bounds read in mixed content websocket messages
  + CVE-2018-5163: Replacing cached data in JavaScript Start-up Bytecode Cache
  + CVE-2018-5164: CSP not applied to all multipart content sent with multipart/x-mixed-replace
  + CVE-2018-5166: WebExtension host permission bypass through filterReponseData
  + CVE-2018-5167: Improper linkification of chrome: and javascript: content in web console and JavaScript debugger
  + CVE-2018-5168: Lightweight themes can be installed without user interaction
  + CVE-2018-5169: Dragging and dropping link text onto home button can set home page to include chrome pages
  + CVE-2018-5172: Pasted script from clipboard can run in the Live Bookmarks page or PDF viewer
  + CVE-2018-5173: File name spoofing of Downloads panel with Unicode characters
  + CVE-2018-5174: Windows Defender SmartScreen UI runs with less secure behavior for downloaded files in Windows 10 April 2018 Update
  + CVE-2018-5175: Universal CSP bypass on sites using strict-dynamic in their policies
  + CVE-2018-5176: JSON Viewer script injection
  + CVE-2018-5177: Buffer overflow in XSLT during number formatting
  + CVE-2018-5165: Checkbox for enabling Flash protected mode is inverted in 32-bit Firefox
  + CVE-2018-5180: heap-use-after-free in mozilla::WebGLContext::DrawElementsInstanced
  + CVE-2018-5181: Local file can be displayed in noopener tab through drag and drop of hyperlink
  + CVE-2018-5182: Local file can be displayed from hyperlink dragged and dropped on addressbar
  + CVE-2018-5151: Memory safety bugs fixed in Firefox 60
  + CVE-2018-5150: Memory safety bugs fixed in Firefox 60 and Firefox ESR 52.8

* Wed May 09 2018 Andrey Cherepanov <cas@altlinux.org> 52.8.0-alt1
- New ESR version (52.8.0).
- Fixes:
  + CVE-2018-5183 Backport critical security fixes in Skia
  + CVE-2018-5154 Use-after-free with SVG animations and clip paths
  + CVE-2018-5155 Use-after-free with SVG animations and text paths
  + CVE-2018-5157 Same-origin bypass of PDF Viewer to view protected PDF files
  + CVE-2018-5158 Malicious PDF can inject JavaScript into PDF Viewer
  + CVE-2018-5159 Integer overflow and out-of-bounds write in Skia
  + CVE-2018-5168 Lightweight themes can be installed without user interaction
  + CVE-2018-5178 Buffer overflow during UTF-8 to Unicode string conversion through legacy extension
  + CVE-2018-5150 Memory safety bugs fixed in Firefox 60 and Firefox ESR 52.8

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.4-alt1
- New ESR version (52.7.4).

* Mon Mar 26 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.3-alt1
- New ESR version (52.7.3)
- Fixes:
  + CVE-2018-5148 Use-after-free in compositor

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.2-alt1
- New ESR version (52.7.2)

* Thu Mar 15 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.1-alt1
- New ESR version (52.7.1)

* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.0-alt1
- New ESR version (52.7.0).
- Fixes:
  + CVE-2018-5127 Buffer overflow manipulating SVG animatedPathSegList
  + CVE-2018-5129 Out-of-bounds write with malformed IPC messages
  + CVE-2018-5130 Mismatched RTP payload type can trigger memory corruption
  + CVE-2018-5131 Fetch API improperly returns cached copies of no-store/no-cache resources
  + CVE-2018-5144 Integer overflow during Unicode conversion
  + CVE-2018-5125 Memory safety bugs fixed in Firefox 59 and Firefox ESR 52.7
  + CVE-2018-5145 Memory safety bugs fixed in Firefox ESR 52.7

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt2
- Enable ALSA support (ALT #34608)

* Mon Jan 22 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt1
- New ESR version (52.6.0)
- Fixes:
  + CVE-2018-5095 Integer overflow in Skia library during edge builder allocation
  + CVE-2018-5096 Use-after-free while editing form elements
  + CVE-2018-5097 Use-after-free when source document is manipulated during XSLT
  + CVE-2018-5098 Use-after-free while manipulating form input elements
  + CVE-2018-5099 Use-after-free with widget listener
  + CVE-2018-5102 Use-after-free in HTML media elements
  + CVE-2018-5103 Use-after-free during mouse event handling
  + CVE-2018-5104 Use-after-free during font face manipulation
  + CVE-2018-5117 URL spoofing with right-to-left text aligned left-to-right
  + CVE-2018-5089 Memory safety bugs fixed in Firefox 58 and Firefox ESR 52.6
- Continue fix of Speculative execution side-channel attack ("Spectre")

* Wed Jan 10 2018 Andrey Cherepanov <cas@altlinux.org> 52.5.3-alt1
- New ESR version (52.5.3)
- Fixes:
  + Speculative execution side-channel attack ("Spectre")

* Sun Dec 10 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.2-alt1
- New ESR version (52.5.2)
- Fixes:
  + CVE-2017-7843 Web worker in Private Browsing mode can write IndexedDB data
- Build with DBUS support (ALT #34302)

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.0-alt1
- New ESR version (52.5.0)
- Fixes:
  + CVE-2017-7828 Use-after-free of PressShell while restyling layout
  + CVE-2017-7830 Cross-origin URL information leak through Resource
  + CVE-2017-7826 Memory safety bugs fixed in Firefox 57 and Firefox ESR

* Fri Sep 29 2017 Andrey Cherepanov <cas@altlinux.org> 52.4.0-alt1
- New ESR version (52.4.0)
- Fixes:
  + CVE-2017-7793 Use-after-free with Fetch API
  + CVE-2017-7818 Use-after-free during ARIA array manipulation
  + CVE-2017-7819 Use-after-free while resizing images in design mode
  + CVE-2017-7824 Buffer overflow when drawing and validating elements with ANGLE
  + CVE-2017-7805 Use-after-free in TLS 1.2 generating handshake hashes
  + CVE-2017-7814 Blob and data URLs bypass phishing and malware protection warnings
  + CVE-2017-7825 OS X fonts render some Tibetan and Arabic unicode characters as spaces
  + CVE-2017-7823 CSP sandbox directive did not create a unique origin
  + CVE-2017-7810 Memory safety bugs fixed in Firefox 56 and Firefox ESR 52.4

* Tue Aug 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.3.0-alt1
- New ESR version (52.3.0)
- Security fixes:
  + CVE-2017-7798: XUL injection in the style editor in devtools
  + CVE-2017-7800: Use-after-free in WebSockets during disconnection
  + CVE-2017-7801: Use-after-free with marquee during window resizing
  + CVE-2017-7809: Use-after-free while deleting attached editor DOM node
  + CVE-2017-7784: Use-after-free with image observers
  + CVE-2017-7802: Use-after-free resizing image elements
  + CVE-2017-7785: Buffer overflow manipulating ARIA attributes in DOM
  + CVE-2017-7786: Buffer overflow while painting non-displayable SVG
  + CVE-2017-7806: Use-after-free in layer manager with SVG
  + CVE-2017-7753: Out-of-bounds read with cached style data and pseudo-elements
  + CVE-2017-7787: Same-origin policy bypass with iframes through page reloads
  + CVE-2017-7807: Domain hijacking through AppCache fallback
  + CVE-2017-7792: Buffer overflow viewing certificates with an extremely long OID
  + CVE-2017-7804: Memory protection bypass through WindowsDllDetourPatcher
  + CVE-2017-7791: Spoofing following page navigation with data: protocol and modal alerts
  + CVE-2017-7782: WindowsDllDetourPatcher allocates memory without DEP protections
  + CVE-2017-7803: CSP containing 'sandbox' improperly applied
  + CVE-2017-7779: Memory safety bugs fixed in Firefox 55 and Firefox ESR 52.3

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.1-alt1
- New ESR version (52.2.1)

* Wed Jun 21 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.0-alt1
- New ESR version (52.2.0)
- Security fixes:
  + CVE-2017-5472: Use-after-free using destroyed node when regenerating trees
  + CVE-2017-7749: Use-after-free during docshell reloading
  + CVE-2017-7750: Use-after-free with track elements
  + CVE-2017-7751: Use-after-free with content viewer listeners
  + CVE-2017-7752: Use-after-free with IME input
  + CVE-2017-7754: Out-of-bounds read in WebGL with ImageInfo object
  + CVE-2017-7755: Privilege escalation through Firefox Installer with same directory DLL files
  + CVE-2017-7756: Use-after-free and use-after-scope logging XHR header errors
  + CVE-2017-7757: Use-after-free in IndexedDB
  + CVE-2017-7778: Vulnerabilities in the Graphite 2 library
  + CVE-2017-7758: Out-of-bounds read in Opus encoder
  + CVE-2017-7760: File manipulation and privilege escalation via callback parameter in Mozilla Windows Updater and Maintenance Service
  + CVE-2017-7761: File deletion and privilege escalation through Mozilla Maintenance Service helper.exe application
  + CVE-2017-7763: Mac fonts render some unicode characters as spaces
  + CVE-2017-7764: Domain spoofing with combination of Canadian Syllabics and other unicode blocks
  + CVE-2017-7765: Mark of the Web bypass when saving executable files
  + CVE-2017-7766: File execution and privilege escalation through updater.ini, Mozilla Windows Updater, and Mozilla Maintenance Service
  + CVE-2017-7767: Privilege escalation and arbitrary file overwrites through Mozilla Windows Updater and Mozilla Maintenance Service
  + CVE-2017-7768: 32 byte arbitrary file read through Mozilla Maintenance Service
  + CVE-2017-5470: Memory safety bugs fixed in Firefox 54 and Firefox ESR 52.2

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.1.1-alt1
- New ESR version (52.1.1)
- Set plugin.load_flash_only setting to false to allow use all NPAPI plugins
- Security fixes since 52.0:
  + CVE-2016-10196: Vulnerabilities in Libevent library
  + CVE-2017-5031: Use after free in ANGLE
  + CVE-2017-5428: integer overflow in createImageBitmap()
  + CVE-2017-5429: Memory safety bugs fixed in Firefox 53, Firefox ESR
  + CVE-2017-5430: Memory safety bugs fixed in Firefox 53 and Firefox ESR
  + CVE-2017-5435: Use-after-free during transaction processing in the
  + CVE-2017-5439: Use-after-free in nsTArray Length() during XSLT
  + CVE-2017-5440: Use-after-free in txExecutionState destructor during
  + CVE-2017-5444: Buffer overflow while parsing
  + CVE-2017-5446: Out-of-bounds read when HTTP/2 DATA frames are sent
  + CVE-2017-5451: Addressbar spoofing with onblur event
  + CVE-2017-5454: Sandbox escape allowing file system read access through
  + CVE-2017-5455: Sandbox escape through internal feed reader APIs
  + CVE-2017-5456: Sandbox escape allowing local file system access
  + CVE-2017-5464: Memory corruption with accessibility and DOM
  + CVE-2017-5466: Origin confusion when reloading isolated data:text/html
  + CVE-2017-5467: Memory corruption when drawing Skia content

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.0-alt1
- New release (52.0) based on legion@ build.
- Built with internal icu.
- Fixed:
  + CVE-2017-5400: asm.js JIT-spray bypass of ASLR and DEP
  + CVE-2017-5401: Memory Corruption when handling ErrorResult
  + CVE-2017-5402: Use-after-free working with events in FontFace objects
  + CVE-2017-5403: Use-after-free using addRange to add range to an incorrect root object
  + CVE-2017-5404: Use-after-free working with ranges in selections
  + CVE-2017-5406: Segmentation fault in Skia with canvas operations
  + CVE-2017-5407: Pixel and history stealing via floating-point timing side channel with SVG filters
  + CVE-2017-5410: Memory corruption during JavaScript garbage collection incremental sweeping
  + CVE-2017-5411: Use-after-free in Buffer Storage in libGLES
  + CVE-2017-5409: File deletion via callback parameter in Mozilla Windows Updater and Maintenance Service
  + CVE-2017-5408: Cross-origin reading of video captions in violation of CORS
  + CVE-2017-5412: Buffer overflow read in SVG filters
  + CVE-2017-5413: Segmentation fault during bidirectional operations
  + CVE-2017-5414: File picker can choose incorrect default directory
  + CVE-2017-5415: Addressbar spoofing through blob URL
  + CVE-2017-5416: Null dereference crash in HttpChannel
  + CVE-2017-5417: Addressbar spoofing by draging and dropping URLs
  + CVE-2017-5425: Overly permissive Gecko Media Plugin sandbox regular expression access
  + CVE-2017-5426: Gecko Media Plugin sandbox is not started if seccomp-bpf filter is running
  + CVE-2017-5427: Non-existent chrome.manifest file loaded during startup
  + CVE-2017-5418: Out of bounds read when parsing HTTP digest authorization responses
  + CVE-2017-5419: Repeated authentication prompts lead to DOS attack
  + CVE-2017-5420: Javascript: URLs can obfuscate addressbar location
  + CVE-2017-5405: FTP response codes can cause use of uninitialized values for ports
  + CVE-2017-5421: Print preview spoofing
  + CVE-2017-5422: DOS attack by using view-source: protocol repeatedly in one hyperlink
  + CVE-2017-5399: Memory safety bugs fixed in Firefox 52
  + CVE-2017-5398: Memory safety bugs fixed in Firefox 52 and Firefox ESR 45.8

* Thu Apr 20 2017 Andrey Cherepanov <cas@altlinux.org> 45.9.0-alt1
- New ESR version
- Security fixes:
  + CVE-2017-5429: Memory safety bugs fixed in Firefox 53, Firefox ESR 45.9,
  + CVE-2017-5462: DRBG flaw in NSS
  + CVE-2017-5445: Uninitialized values used while parsing
  + CVE-2017-5469: Potential Buffer overflow in flex-generated code
  + CVE-2017-5437: Vulnerabilities in Libevent library
  + CVE-2017-5448: Out-of-bounds write in ClearKeyDecryptor
  + CVE-2017-5465: Out-of-bounds read in ConvolvePixel
  + CVE-2017-5447: Out-of-bounds read during glyph processing
  + CVE-2017-5446: Out-of-bounds read when HTTP/2 DATA frames are sent with
  + CVE-2017-5444: Buffer overflow while parsing application/http-index-format
  + CVE-2017-5443: Out-of-bounds write during BinHex decoding
  + CVE-2017-5464: Memory corruption with accessibility and DOM manipulation
  + CVE-2017-5442: Use-after-free during style changes
  + CVE-2017-5441: Use-after-free with selection during scroll events
  + CVE-2017-5440: Use-after-free in txExecutionState destructor during XSLT
  + CVE-2017-5439: Use-after-free in nsTArray Length() during XSLT processing
  + CVE-2017-5438: Use-after-free in nsAutoPtr during XSLT processing
  + CVE-2017-5460: Use-after-free in frame selection
  + CVE-2017-5432: Use-after-free in text input selection
  + CVE-2017-5434: Use-after-free during focus handling
  + CVE-2017-5459: Buffer overflow in WebGL
  + CVE-2017-5461: Out-of-bounds write in Base64 encoding in NSS
  + CVE-2017-5436: Out-of-bounds write with malicious font in Graphite 2
  + CVE-2017-5435: Use-after-free during transaction processing in the editor
  + CVE-2017-5433: Use-after-free in SMIL animation functions

* Tue Mar 07 2017 Andrey Cherepanov <cas@altlinux.org> 45.8.0-alt1
- New ESR version
- Require fresh libnss for correct https open

* Wed Jan 25 2017 Andrey Cherepanov <cas@altlinux.org> 45.7.0-alt1
- New ESR version

* Fri Jan 20 2017 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt2
- Fix build with GCC 6.1

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt1
- New ESR version

* Tue Dec  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 45.5.1-alt2
- Make it pass strict verification of unresolved ELF symbols; this will also
  protect us from missing dependencies on libgtk symbols. (Thx legion@ for
  the original hack, removed in 44.0.2-alt3, but found to be restorable by
  ruslandh@'s work on strict unresolved symbols verification in palemoon.)

* Thu Dec 01 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-92 Firefox SVG Animation Remote Code Execution

* Thu Nov 17 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.0-alt1
- New ESR version

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 45.4.0-alt1
- New ESR version

* Tue Aug 02 2016 Andrey Cherepanov <cas@altlinux.org> 45.3.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-80 Same-origin policy violation using local HTML file and saved shortcut file
  + MFSA 2016-79 Use-after-free when applying SVG effects
  + MFSA 2016-78 Type confusion in display transformation
  + MFSA 2016-77 Buffer overflow in ClearKey Content Decryption Module (CDM) during video playback
  + MFSA 2016-76 Scripts on marquee tag can execute in sandboxed iframes
  + MFSA 2016-73 Use-after-free in service workers with nested sync events
  + MFSA 2016-72 Use-after-free in DTLS during WebRTC session shutdown
  + MFSA 2016-70 Use-after-free when using alt key and toplevel menus
  + MFSA 2016-67 Stack underflow during 2D graphics rendering
  + MFSA 2016-65 Cairo rendering crash due to memory allocation issue with FFmpeg 0.10
  + MFSA 2016-64 Buffer overflow rendering SVG with bidirectional content
  + MFSA 2016-63 Favicon network connection can persist when page is closed


* Sun Jun 12 2016 Andrey Cherepanov <cas@altlinux.org> 45.2.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-58 Entering fullscreen and persistent pointerlock without user permission
  + MFSA 2016-56 Use-after-free when textures are used in WebGL operations after recycle pool destruction
  + MFSA 2016-55 File overwrite and privilege escalation through Mozilla Windows updater
  + MFSA 2016-53 Out-of-bounds write with WebGL shader
  + MFSA 2016-52 Addressbar spoofing though the SELECT element
  + MFSA 2016-51 Use-after-free deleting tables from a contenteditable document
  + MFSA 2016-50 Buffer overflow parsing HTML5 fragments

* Tue May 24 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.1-alt2
- Build with GTK+ 2.x (ALT #32120)

* Wed May 04 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.1-alt1
- New ESR version

* Mon May 02 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-47 Write to invalid HashMap entry through JavaScript.watch()
  + MFSA 2016-44 Buffer overflow in libstagefright with CENC offsets
  + MFSA 2016-39 Miscellaneous memory safety hazards

* Fri Apr 15 2016 Andrey Cherepanov <cas@altlinux.org> 45.0.2-alt1
- New ESR version (switch to 45.x)

* Thu Mar 24 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.1-alt1
- New ESR version

* Thu Mar 10 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt2
- Rebuild with new rpm

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-37 Font vulnerabilities in the Graphite 2 library
  + MFSA 2016-35 Buffer overflow during ASN.1 decoding in NSS
  + MFSA 2016-34 Out-of-bounds read in HTML parser following a failed allocation
  + MFSA 2016-31 Memory corruption with malicious NPAPI plugin
  + MFSA 2016-28 Addressbar spoofing though history navigation and Location protocol property
  + MFSA 2016-27 Use-after-free during XML transformations
  + MFSA 2016-25 Use-after-free when using multiple WebRTC data channels
  + MFSA 2016-24 Use-after-free in SetBody
  + MFSA 2016-23 Use-after-free in HTML5 string parser
  + MFSA 2016-21 Displayed page address can be overridden
  + MFSA 2016-20 Memory leak in libstagefright when deleting an array during MP4 processing
  + MFSA 2016-17 Local file overwriting and potential privilege escalation through CSP reports
  + MFSA 2016-16 Miscellaneous memory safety hazards
  + MFSA 2015-136 Same-origin policy violation using performance.getEntries and history navigation
  + MFSA 2015-81 Use-after-free in MediaStream playback

* Fri Feb 12 2016 Andrey Cherepanov <cas@altlinux.org> 38.6.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-14 Vulnerabilities in Graphite 2

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 38.6.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-03 Buffer overflow in WebGL after out of memory allocation
  + MFSA 2016-01 Miscellaneous memory safety hazards (rv:44.0 / rv:38.6)
  + MFSA 2015-150 MD5 signatures accepted within TLS 1.2 ServerKeyExchange in server signature

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.2-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-150 MD5 signatures accepted within TLS 1.2 ServerKeyExchange in server signature

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.1-alt1
- New ESR version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-149 Cross-site reading attack through data and view-source URIs
  + MFSA 2015-147 Integer underflow and buffer overflow processing MP4 metadata in libstagefright
  + MFSA 2015-146 Integer overflow in MP4 playback in 64-bit versions
  + MFSA 2015-145 Underflow through code inspection
  + MFSA 2015-139 Integer overflow allocating extremely large textures
  + MFSA 2015-138 Use-after-free in WebRTC when datachannel is used after being destroyed

* Wed Nov 04 2015 Andrey Cherepanov <cas@altlinux.org> 38.4.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-133 NSS and NSPR memory corruption issues
  + MFSA 2015-132 Mixed content WebSocket policy bypass through workers
  + MFSA 2015-131 Vulnerabilities found through code inspection
  + MFSA 2015-130 JavaScript garbage collection crash with Java applet
  + MFSA 2015-128 Memory corruption in libjar through zip files
  + MFSA 2015-127 CORS preflight is bypassed when non-standard Content-Type headers are received
  + MFSA 2015-123 Buffer overflow during image interactions in canvas
  + MFSA 2015-122 Trailing whitespace in IP address hostnames can bypass same-origin policy

* Mon Sep 28 2015 Andrey Cherepanov <cas@altlinux.org> 38.3.0-alt2
- Use GStreamer 1.0 (ALT #31305)

* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 38.3.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-113 Memory safety errors in libGLES in the ANGLE graphics library
  + MFSA 2015-112 Vulnerabilities found through code inspection
  + MFSA 2015-111 Errors in the handling of CORS preflight request headers
  + MFSA 2015-110 Dragging and dropping images exposes final URL after redirects
  + MFSA 2015-106 Use-after-free while manipulating HTML media content
  + MFSA 2015-105 Buffer overflow while decoding WebM video
  + MFSA 2015-101 Buffer overflow in libvpx while parsing vp9 format video
  + MFSA 2015-100 Arbitrary file manipulation by local user through Mozilla updater

* Fri Aug 28 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-95 Add-on notification bypass through data URLs
  + MFSA 2015-94 Use-after-free when resizing canvas element during restyling

* Wed Aug 12 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-92 Use-after-free in XMLHttpRequest with shared workers
  + MFSA 2015-90 Vulnerabilities found through code inspection
  + MFSA 2015-89 Buffer overflows on Libvpx when decoding WebM video
  + MFSA 2015-88 Heap overflow in gdk-pixbuf when scaling bitmap images
  + MFSA 2015-87 Crash when using shared memory in JavaScript
  + MFSA 2015-85 Out-of-bounds write with Updater and malicious MAR file
  + MFSA 2015-84 Arbitrary file overwriting through Mozilla Maintenance
                 Service with hard links
  + MFSA 2015-83 Overflow issues in libstagefright
  + MFSA 2015-82 Redefinition of non-configurable JavaScript object
                 properties
  + MFSA 2015-80 Out-of-bounds read with malformed MP3 file

* Sat Aug 08 2015 Andrey Cherepanov <cas@altlinux.org> 38.1.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-78 Same origin violation and local file stealing via PDF reader

* Thu Jul 16 2015 Andrey Cherepanov <cas@altlinux.org> 38.1.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-70 NSS accepts export-length DHE keys with regular DHE cipher suites
  + MFSA 2015-69 Privilege escalation through internal workers
  + MFSA 2015-67 Key pinning is ignored when overridable errors are encountered
  + MFSA 2015-66 Vulnerabilities found through code inspection
  + MFSA 2015-65 Use-after-free in workers while using XMLHttpRequest
  + MFSA 2015-64 ECDSA signature validation fails to handle some signatures correctly
  + MFSA 2015-63 Use-after-free in Content Policy due to microtask execution error
  + MFSA 2015-62 Out-of-bound read while computing an oscillator rendering range in Web Audio
  + MFSA 2015-61 Type confusion in Indexed Database Manager
  + MFSA 2015-60 Local files or privileged URLs in pages can be opened into new tabs

* Mon May 25 2015 Andrey Cherepanov <cas@altlinux.org> 38.0.1-alt1
- New ESR version
  + 2015-19 Out-of-bounds read and write while rendering SVG content
  + 2015-16 Use-after-free in IndexedDB
  + 2015-12 Invoking Mozilla updater will load locally stored DLL files

* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- Package ESR version as firefox-esr
- Fixed:
  + MFSA 2015-06 Read-after-free in WebRTC
  + MFSA 2015-04 Cookie injection through Proxy Authenticate responses
  + MFSA 2015-03 sendBeacon requests lack an Origin header
