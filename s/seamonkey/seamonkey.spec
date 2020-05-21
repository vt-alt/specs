%def_without	lightning
%def_without 	system_mozldap
%def_without 	enigmail

%define sm_prefix	%_libdir/%name
%define sm_datadir	%_datadir/%name
%define sm_version	%name-%version
%define sm_arch_extensionsdir	%sm_prefix/extensions
%define sm_noarch_extensionsdir	%sm_datadir/extensions
%define sm_cid		\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}
%define enigmail_ciddir	%sm_arch_extensionsdir/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
%define sm_idldir       %_datadir/idl/%name
%define sm_includedir   %_includedir/%name
%define sm_develdir     %sm_prefix-devel
%ifndef build_parallel_jobs
%define build_parallel_jobs 32
%endif
%define beta_suffix	%nil

Name: 	 seamonkey
Version: 2.53.2
Release: alt1
Epoch:   1
Summary: Web browser and mail reader
License: MPL-2.0
Group:   Networking/WWW

Packager:   Andrey Cherepanov <cas@altlinux.org>

Url: http://www.mozilla.org/projects/seamonkey/

# TODO: build failed on aarch64 and ppc64le
ExclusiveArch: %ix86 x86_64

Source0:	%name-%version%beta_suffix.source.tar.xz
Source2:	mozilla-searchplugins.tar
Source3:	seamonkey-alt-browser.desktop
Source4:	seamonkey-alt-mail.desktop
Source5:	seamonkey-prefs.js
Source6:	enigmail.tar
Source7:	seamonkey-mozconfig
Source8:	rpm-build.tar
Source9:        cbindgen-vendor.tar

Patch0:		seamonkey-fix-installdirs.patch
Patch1:		seamonkey-2.2-alt-machOS-fix.patch
Patch2:		seamonkey-2.0.14-alt-fix-plugin-path.patch
Patch3:		xulrunner-noarch-extensions.patch
%if_with system_mozldap
Patch5:		thunderbird-with-system-mozldap.patch
%endif
Patch6:		seamonkey-2.13.2-alt-fix-build.patch
Patch8:		seamonkey-2.26-enable-addons.patch
Patch9:		mozilla-js-makefile.patch
Patch10:	firefox-32-baseline-disable.patch
Patch11:        seamonkey-2.53.2-alt-ppc64le-disable-broken-getProcessorLineSize-code.patch
Patch12:        seamonkey-2.53.2-alt-ppc64le-fix-clang-error-invalid-memory-operand.patch


Requires(pre,postun): urw-fonts

#Obsoletes
Obsoletes:	seamonkey-dom-inspector
Provides:	seamonkey-dom-inspector
Obsoletes:	seamonkey-enigmail
Provides:	seamonkey-enigmail
Obsoletes:	seamonkey-irc
Provides:	seamonkey-irc
Obsoletes:	seamonkey-js-debugger
Provides:	seamonkey-js-debugger
Obsoletes:	seamonkey-mail
Provides:	seamonkey-mail
Obsoletes:	seamonkey-plugins-common
Provides:	seamonkey-plugins-common
Obsoletes:	seamonkey-psm
Provides:	seamonkey-psm
Obsoletes:	seamonkey-spellchecker
Provides:	seamonkey-spellchecker

BuildRequires(pre): rpm-macros-alternatives
BuildRequires(pre): browser-plugins-npapi-devel

# Automatically added by buildreq on Sun Jul 16 2006
%if_with system_mozldap
BuildPreReq: mozldap-devel
%endif
BuildRequires: gcc-c++
%define clang_version %nil
BuildRequires: clang%clang_version
BuildRequires: clang%clang_version-devel
BuildRequires: llvm%clang_version-devel
BuildRequires: lld-devel
BuildRequires: libdnet-devel libgtk+2-devel libgtk+3-devel libIDL-devel wget libarchive-devel libpixman-devel
BuildRequires: libjpeg-devel libpng-devel libXinerama-devel libXext-devel
BuildRequires: libXp-devel libXt-devel makedepend net-tools unzip libalsa-devel yasm libwireless-devel
BuildRequires: xorg-cf-files zip libXft-devel libvpx5-devel
BuildRequires: desktop-file-utils libcurl-devel libhunspell-devel libsqlite3-devel
BuildRequires: autoconf_2.13 chrpath alternatives libGL-devel
BuildRequires: libstartup-notification-devel libfreetype-devel fontconfig-devel libnotify-devel
BuildRequires: libffi-devel libgio-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libGConf-devel
BuildRequires: libevent-devel
BuildRequires: libproxy-devel
BuildRequires: libdbus-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
# Rust requires
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc

# Mozilla requires
BuildRequires:	libnspr-devel       >= 4.9.2-alt1
BuildRequires:	libnss-devel        >= 3.15.1-alt1
BuildRequires:	libnss-devel-static >= 3.15.1-alt1

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

%set_autoconf_version 2.13
%add_findprov_lib_path %sm_prefix

%description
SeaMonkey is an open-source web browser, designed for standards
compliance, performance and portability.

%if_with lightning
%package lightning
%define lightning_ciddir %sm_arch_extensionsdir/\{e2fda1a4-762b-4020-b5ad-a41df1933103\}
Summary: An integrated calendar for Seamonkey
Group: Office
Url: http://www.mozilla.org/projects/calendar/lightning/
Requires: %name = %epoch:%version-%release

%description lightning
An integrated calendar for Seamonkey.
%endif

%package devel
Summary:	Seamonkey development kit.
Group:		Development/C++
Requires: %name = %epoch:%version-%release

Requires:	python-base
AutoReq:	yes, nopython

%description devel
Seamonkey development kit.

%package -n rpm-build-seamonkey
Summary: 	RPM helper macros to rebuild seamonkey packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org

%description -n rpm-build-seamonkey
These helper macros provide possibility to rebuild
seamonkey packages by some Alt Linux Team Policy compatible way.

%prep
%setup -n %name-%version%beta_suffix

### Moved enigmail to mailnews
%if_with enigmail
tar -xf %SOURCE6 -C mailnews/extensions/
%endif

#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%if_with system_mozldap
%patch5 -p1 -b .mozldap
%endif
%patch6 -p2
#%%patch8 -p2
#patch9 -p2

# https://bugzilla.altlinux.org/30322
%ifarch %{ix86}
%patch10 -p1
%endif
%patch11 -p1
%patch12 -p1

### Copying .mozconfig to build directory
cp -f %SOURCE7 .mozconfig

%if_with lightning
echo 'ac_add_options --enable-calendar' >> .mozconfig
%endif

mkdir -p -- my_rust_vendor
tar --strip-components=1 -C my_rust_vendor --overwrite -xf %SOURCE9

mkdir -p -- .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/my_rust_vendor"
EOF

%build
%add_optflags %optflags_shared
%add_findprov_lib_path %sm_prefix

env CARGO_HOME="$PWD/.cargo" \
        cargo install cbindgen

# Add fake RPATH
rpath="/$(printf %%s '%sm_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2

export MOZ_BUILD_APP=suite

%ifarch x86_64
export CFLAGS="$CFLAGS -DHAVE_USR_LIB64_DIR=1"
%endif

%ifarch %{arm} %{ix86}
export RUSTFLAGS="-Cdebuginfo=0"
export LLVM_PARALLEL_LINK_JOBS=1
# See https://lwn.net/Articles/797303/ for linker flags
# For bfd on i586
export CXXFLAGS="$CXXFLAGS -Wl,--no-keep-memory -Wl,--reduce-memory-overheads -Wl,--hash-size=1021"
# For gold on i586
#export CXXFLAGS="$CXXFLAGS -Wl,--no-threads -Wl,--no-keep-files-mapped -Wl,--no-map-whole-files -Wl,--no-mmap-output-file -Wl,--stats"
%endif

export CC="clang"
export CXX="clang++"

export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export SHELL="/bin/bash"
export srcdir="$PWD"
export MOZILLA_SRCDIR="$srcdir/mozilla"

autoconf

export NPROCS=%build_parallel_jobs
# Decrease NPROCS prevents oomkill terror on x86_64
%ifarch x86_64
export NPROCS=16
%endif
# Build for i586 in one thread
%ifarch %ix86
export NPROCS=1
%endif

# a kludge since 2.26 ...
mkdir objdir
ln -s ../objdir mozilla/objdir

%make_build -f client.mk build \
	-j $NPROCS \
	MOZ_PARALLEL_BUILD=$NPROCS \
	mozappdir=%sm_prefix \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"

%if_with enigmail
cd mailnews/extensions/enigmail
    ./makemake -r
cd -

dir="$PWD/objdir"

cd $dir/mailnews/extensions/enigmail
	make \
		STRIP="/bin/true" \
		MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"
	make xpi
	mv -f -- $dir/mozilla/dist/bin/enigmail-*.xpi $dir/mozilla/dist/xpi-stage/
	make clean
cd -
%endif

%install
export SHELL=/bin/sh
dir="$PWD/objdir"

mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%sm_prefix/plugins \
	%buildroot/%sm_arch_extensionsdir \
	%buildroot/%sm_noarch_extensionsdir \
	%buildroot/%_datadir/applications \
	#

%makeinstall -C objdir \
	idldir=%buildroot/%sm_idldir \
	includedir=%buildroot/%sm_includedir \
	mozappdir=%buildroot/%sm_prefix \
	#

ln -sf -- $(relative "%sm_noarch_extensionsdir" "%sm_prefix/") \
    %buildroot/%sm_prefix/extensions-noarch

(set +x
    for f in %buildroot/%sm_develdir/*; do
	[ -L "$f" ] || continue

	t="$(readlink "$f")"
	r="$(relative "${t#%buildroot}" "${f#%buildroot}")"

	ln -vnsf -- "$r" "$f"
    done
)

(set +x
    rm -vrf -- %buildroot/%sm_prefix/dictionaries/*
    for suf in aff dic; do
	t="$(relative %_datadir/myspell/en_US.$suf %sm_prefix/dictionaries/)"
	ln -vs "$t" %buildroot/%sm_prefix/dictionaries/en-US.$suf
    done
)

rm -rf -- \
	%buildroot/%_bindir/seamonkey \
	%buildroot/%sm_prefix/js \
	%buildroot/%sm_prefix/regxpcom \
	%buildroot/%sm_prefix/xpcshell \
	%buildroot/%sm_prefix/xpidl \
	%buildroot/%sm_prefix/xpt_dump \
	%buildroot/%sm_prefix/xpt_link \
	%buildroot/%sm_prefix/nsinstall \
	%buildroot/%sm_prefix/removed-files \
	%buildroot/%sm_prefix/seamonkey \
	%buildroot/%sm_prefix/run-mozilla.sh \
	%buildroot/%sm_prefix/README.txt \
	#

dir="$PWD/objdir"

###From Enigmail
%if_with enigmail
mkdir -p %buildroot/%enigmail_ciddir
unzip -q -u -d %buildroot/%enigmail_ciddir -- \
    $dir/mozilla/dist/xpi-stage/enigmail*.xpi
%endif

###From Lightning
%if_with lightning
mkdir -p %buildroot/%lightning_ciddir
unzip -q -u -d %buildroot/%lightning_ciddir -- \
    $dir/dist/xpi-stage/lightning*.xpi

rm -f -- %buildroot/%lightning_ciddir/application.ini
%endif

# rpm-build-seamonkey files
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
tar -xf %SOURCE8
cp -a rpm-build/rpm.macros.seamonkey %buildroot/%_sysconfdir/rpm/macros.d/%name

# install altlinux-specific configuration
install -D -m 644 %SOURCE5 %buildroot/%sm_prefix/defaults/preferences/all-altlinux.js

# install icons
test -e suite/branding/seamonkey/default32.png || cp suite/branding/seamonkey/default{,32}.png
for s in 16 32 48 64 128; do
	install -Dpm0644 suite/branding/seamonkey/default${s}.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done

# install search plugins
tar -C %buildroot%sm_prefix -xf %SOURCE2

# install browser menu file
install -D -m 644 %SOURCE3 %buildroot%_datadir/applications/seamonkey-alt-browser.desktop
# install mail menu file
install -D -m 644 %SOURCE4 %buildroot%_datadir/applications/seamonkey-alt-mail.desktop

# main startup script
cat>%buildroot/%_bindir/seamonkey<<-EOF
#!/bin/sh -e
    export MOZ_APP_LAUNCHER="\${MOZ_APP_LAUNCHER:-\$0}"
    export MOZ_PLUGIN_PATH="%browser_plugins_path\${MOZ_PLUGIN_PATH:+:\$MOZ_PLUGIN_PATH}"
    export NSS_SSL_ENABLE_RENEGOTIATION=1
    %sm_prefix/seamonkey-bin \${1:+"\$@"}
EOF


chmod 755 %buildroot/%_bindir/seamonkey

# Add alternatives
mkdir -p %buildroot%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t100\n' > %buildroot%_altdir/%name

# Add real RPATH
(set +x
    rpath="/$(printf %%s '%sm_prefix' |tr '[:print:]' '_')"

    find \
	%buildroot/%sm_prefix \
	%buildroot/%sm_develdir \
	%buildroot/%sm_arch_extensionsdir \
    -type f |
    while read f; do
	t="$(readlink -ev "$f")"

	file "$t" | fgrep -qs ELF || continue

	if chrpath -l "$t" | fgrep -qs "RPATH=$rpath"; then
	chrpath -r "%sm_prefix" "$t"
	fi
    done
)

%files
%dir %sm_datadir
%_altdir/%name
%_bindir/%name
%_datadir/applications/*.desktop
%sm_prefix
%sm_noarch_extensionsdir
%_iconsdir/hicolor/*/apps/%name.png
%if_with lightning
%exclude %lightning_ciddir
%endif

%if_with lightning
%files lightning
%lightning_ciddir
%endif

%files -n rpm-build-seamonkey
%_sysconfdir/rpm/macros.d/%name

%changelog
* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.53.2-alt1
- New stable version.
- Remove deprecated lbzip2.

* Thu Apr 30 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.53.2-alt0.1.b1
- 2.53.2 Beta 1 compatible with Rust 1.41.0 (ALT #38169).
- Do not package deprecated seamonkey-devel package.
- Use Clang for build.
- Fix License tag according to SPDX.

* Mon Apr 20 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.53.1-alt1
- 2.53.1
- build with gtk3

* Mon Jul 30 2018 Michael Shigorin <mike@altlinux.org> 1:2.49.4-alt1
- 2.49.4

* Fri May 04 2018 Michael Shigorin <mike@altlinux.org> 1:2.49.3-alt1
- 2.49.3

* Wed Feb 21 2018 Michael Shigorin <mike@altlinux.org> 1:2.49.2-alt1
- 2.49.2
- move off gstreamer-0.10

* Sun Nov 05 2017 Michael Shigorin <mike@altlinux.org> 1:2.49.1-alt1
- 2.49.1
  + NB: lightning no more included in upstream tarball

* Mon Jul 31 2017 Michael Shigorin <mike@altlinux.org> 1:2.48-alt1
- 2.48
- dropped patch9
- %%install: set SHELL environment variable explicitly too

* Wed Dec 28 2016 Michael Shigorin <mike@altlinux.org> 1:2.46-alt1
- 2.46 released

* Mon Oct 10 2016 Michael Shigorin <mike@altlinux.org> 1:2.46-alt0.6
- 2.46 (candidate build6 tarball)

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 1:2.46-alt0.5
- 2.46 (candidate build5 tarball)

* Sun Mar 20 2016 Michael Shigorin <mike@altlinux.org> 1:2.40-alt2
- 2.40 released

* Sat Mar 05 2016 Michael Shigorin <mike@altlinux.org> 1:2.40-alt1
- 2.40 (candidate build4 tarball)

* Tue Nov 10 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.39-alt1
- 2.39

* Mon Oct 12 2015 Michael Shigorin <mike@altlinux.org> 1:2.38-alt2
- Enabled logging, see https://bugzilla.mozilla.org/1129718

* Mon Oct 12 2015 <cas@altlinux.org> 1:2.38-alt1
- New version

* Fri Sep 04 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.35-alt1
- New version

* Wed Mar 25 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.33.1-alt1
- New version
- Security fixes:
  + MFSA 2015-29 Code execution through incorrect JavaScript bounds
    checking elimination
  + MFSA 2015-28 Privilege escalation through SVG navigation

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.33-alt1
- New version

* Tue Feb 10 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.32.1-alt1
- New version

* Thu Jan 15 2015 Andrey Cherepanov <cas@altlinux.org> 1:2.32-alt1
- New version
- Security fixes:
  + MFSA 2015-09 XrayWrapper bypass through DOM objects
  + MFSA 2015-08 Delegated OCSP responder certificates failure with
    id-pkix-ocsp-nocheck extension
  + MFSA 2015-06 Read-after-free in WebRTC
  + MFSA 2015-05 Read of uninitialized memory in Web Audio
  + MFSA 2015-04 Cookie injection through Proxy Authenticate responses
  + MFSA 2015-03 sendBeacon requests lack an Origin header
  + MFSA 2015-02 Uninitialized memory use during bitmap rendering

* Wed Dec 10 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.31-alt1
- New version
- Build from src.rpm contains upstream tarball

* Mon Oct 20 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.30-alt1
- New version

* Fri Sep 26 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.29.1-alt1
- New version with security fix:
  + MFSA 2014-73 RSA Signature Forgery in NSS

* Tue Sep 23 2014 Michael Shigorin <mike@altlinux.org> 1:2.29-alt2
- NMU: applied fedora patch to disable baseline jit
  working around a segfault on i586 (closes: #30322)

* Tue Sep 09 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.29-alt1
- New version

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.26.1-alt1
- New version
- Security fixes:
  + MFSA 2014-54 Buffer overflow in Gamepad API
  + MFSA 2014-53 Buffer overflow in Web Audio Speex resampler
  + MFSA 2014-52 Use-after-free with SMIL Animation Controller
  + MFSA 2014-51 Use-after-free in Event Listener Manager
  + MFSA 2014-49 Use-after-free and out of bounds issues found using Address Sanitizer
  + MFSA 2014-48 Miscellaneous memory safety hazards

* Mon May 19 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.26-alt1
- New version
- Security fixes:
  + MFSA 2014-47 Debugger can bypass XrayWrappers with JavaScript
  + MFSA 2014-46 Use-after-free in nsHostResolve
  + MFSA 2014-45 Incorrect IDNA domain name matching for wildcard certificates
  + MFSA 2014-44 Use-after-free in imgLoader while resizing images
  + MFSA 2014-43 Cross-site scripting (XSS) using history navigations
  + MFSA 2014-42 Privilege escalation through Web Notification API
  + MFSA 2014-41 Out-of-bounds write in Cairo
  + MFSA 2014-39 Use-after-free in the Text Track Manager for HTML video
  + MFSA 2014-38 Buffer overflow when using non-XBL object as XBL
  + MFSA 2014-37 Out of bounds read while decoding JPG images
  + MFSA 2014-36 Web Audio memory corruption issues
  + MFSA 2014-34 Miscellaneous memory safety hazards

* Sun Mar 30 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.25-alt1
- New version
- Security fixes:
  + MFSA 2014-32 Out-of-bounds write through TypedArrayObject after neutering
  + MFSA 2014-31 Out-of-bounds read/write through neutering ArrayBuffer objects
  + MFSA 2014-30 Use-after-free in TypeObject
  + MFSA 2014-29 Privilege escalation using WebIDL-implemented APIs
  + MFSA 2014-28 SVG filters information disclosure through feDisplacementMap
  + MFSA 2014-27 Memory corruption in Cairo during PDF font rendering
  + MFSA 2014-26 Information disclosure through polygon rendering in MathML
  + MFSA 2014-23 Content Security Policy for data: documents not preserved by session restore
  + MFSA 2014-22 WebGL content injection from one domain to rendering in another
  + MFSA 2014-20 onbeforeunload and Javascript navigation DOS
  + MFSA 2014-19 Spoofing attack on WebRTC permission prompt
  + MFSA 2014-18 crypto.generateCRMFRequest does not validate type of key
  + MFSA 2014-17 Out of bounds read during WAV file decoding
  + MFSA 2014-16 Files extracted during updates are not always read only
  + MFSA 2014-15 Miscellaneous memory safety hazards

* Thu Mar 06 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.24-alt1
- New version
- Security fixes:
  + MFSA 2014-13 Inconsistent JavaScript handling of access to Window objects
  + MFSA 2014-12 NSS ticket handling issues
  + MFSA 2014-11 Crash when using web workers with asm.js
  + MFSA 2014-09 Cross-origin information leak through web workers
  + MFSA 2014-08 Use-after-free with imgRequestProxy and image proccessing
  + MFSA 2014-07 XSLT stylesheets treated as styles in Content Security Policy
  + MFSA 2014-05 Information disclosure with *FromPoint on iframes
  + MFSA 2014-04 Incorrect use of discarded images by RasterImage
  + MFSA 2014-03 UI selection timeout missing on download prompts
  + MFSA 2014-02 Clone protected content with XBL scopes
  + MFSA 2014-01 Miscellaneous memory safety hazards
- Disable firstrun page show

* Mon Feb 17 2014 Andrey Cherepanov <cas@altlinux.org> 1:2.23-alt1
- New version of Seamonkey 2.23
- Security fixes since 2.21:
  + MFSA 2013-117 Mis-issued ANSSI/DCSSI certificate
  + MFSA 2013-116 JPEG information leak
  + MFSA 2013-115 GetElementIC typed array stubs can be generated outside observed typesets
  + MFSA 2013-114 Use-after-free in synthetic mouse movement
  + MFSA 2013-113 Trust settings for built-in roots ignored during EV certificate validation
  + MFSA 2013-112 Linux clipboard information disclosure though selection paste
  + MFSA 2013-111 Segmentation violation when replacing ordered list elements
  + MFSA 2013-110 Potential overflow in JavaScript binary search algorithms
  + MFSA 2013-109 Use-after-free during Table Editing
  + MFSA 2013-108 Use-after-free in event listeners
  + MFSA 2013-107 Sandbox restrictions not applied to nested object elements
  + MFSA 2013-106 Character encoding cross-origin XSS attack
  + MFSA 2013-104 Miscellaneous memory safety hazards
  + MFSA 2013-102 Use-after-free in HTML document templates
  + MFSA 2013-101 Memory corruption in workers
  + MFSA 2013-100 Miscellaneous use-after-free issues found through ASAN fuzzing
  + MFSA 2013-98 Use-after-free when updating offline cache
  + MFSA 2013-97 Writing to cycle collected object during image decoding
  + MFSA 2013-96 Improperly initialized memory and overflows in some JavaScript functions
  + MFSA 2013-95 Access violation with XSLT and uninitialized data
  + MFSA 2013-94 Spoofing addressbar though SELECT element
  + MFSA 2013-93 Miscellaneous memory safety hazards
- Disable Enigmail extension (ALT #29678)

* Mon Sep 23 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.21-alt1
- New version 2.21
- Security fixes:
  + MFSA 2013-92 GC hazard with default compartments and frame chain restoration
  + MFSA 2013-91 User-defined properties on DOM proxies get the wrong "this" object
  + MFSA 2013-90 Memory corruption involving scrolling
  + MFSA 2013-89 Buffer overflow with multi-column, lists, and floats
  + MFSA 2013-88 compartment mismatch re-attaching XBL-backed nodes
  + MFSA 2013-85 Uninitialized data in IonMonkey
  + MFSA 2013-83 Mozilla Updater does not lock MAR file after signature verification
  + MFSA 2013-82 Calling scope for new Javascript objects can lead to memory corruption
  + MFSA 2013-81 Use-after-free with select element
  + MFSA 2013-80 NativeKey continues handling key messages after widget is destroyed
  + MFSA 2013-79 Use-after-free in Animation Manager during stylesheet cloning
  + MFSA 2013-78 Integer overflow in ANGLE library
  + MFSA 2013-77 Improper state in HTML5 Tree Builder with templates
  + MFSA 2013-76 Miscellaneous memory safety hazards
- Add build requires of Gstreamer

* Thu Aug 08 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.20-alt1
- New version 2.20
- Security fixes:
  - MFSA 2013-75 Local Java applets may read contents of local file system
  - MFSA 2013-73 Same-origin bypass with web workers and XMLHttpRequest
  - MFSA 2013-72 Wrong principal used for validating URI for some Javascript components
  - MFSA 2013-70 Bypass of XrayWrappers using XBL Scopes
  - MFSA 2013-69 CRMF requests allow for code execution and XSS attacks
  - MFSA 2013-68 Document URI misrepresentation and masquerading
  - MFSA 2013-67 Crash during WAV audio file decoding
  - MFSA 2013-65 Buffer underflow when generating CRMF requests
  - MFSA 2013-64 Use after free mutating DOM during SetBody
  - MFSA 2013-63 Miscellaneous memory safety hazards
- Drop deprecated seamonkey-disable-cairo.patch

* Thu Jul 25 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.19-alt1
- New version 2.19
- Set SHELL environment variable explicitly
- Update Enigmail to 1.5.2

* Tue May 28 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.17.1-alt1
- New version 2.17.1
- Security fixes:
  - MFSA 2013-40 Out-of-bounds array read in CERT_DecodeCertPackage
  - MFSA 2013-39 Memory corruption while rendering grayscale PNG images
  - MFSA 2013-38 Cross-site scripting (XSS) using timed history navigations
  - MFSA 2013-37 Bypass of tab-modal dialog origin disclosure
  - MFSA 2013-36 Bypass of SOW protections allows cloning of protected nodes
  - MFSA 2013-35 WebGL crash with Mesa graphics driver on Linux
  - MFSA 2013-34 Privilege escalation through Mozilla Updater
  - MFSA 2013-31 Out-of-bounds write in Cairo library
  - MFSA 2013-30 Miscellaneous memory safety hazards
  - MFSA 2013-29 Use-after-free in HTML Editor
  - MFSA 2013-28 Use-after-free, out of bounds read, and buffer overflow issues found using Address Sanitizer
  - MFSA 2013-27 Phishing on HTTPS connection through malicious proxy
  - MFSA 2013-26 Use-after-free in nsImageLoadingContent
  - MFSA 2013-25 Privacy leak in JavaScript Workers
  - MFSA 2013-24 Web content bypass of COW and SOW security wrappers
  - MFSA 2013-23 Wrapped WebIDL objects can be wrapped again
  - MFSA 2013-22 Out-of-bounds read in image rendering
  - MFSA 2013-21 Miscellaneous memory safety hazards

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.15.2-alt2
- Build with libarchive-devel instead of libarchive

* Wed Feb 27 2013 Andrey Cherepanov <cas@altlinux.org> 1:2.15.2-alt1
- New version 2.15.2

* Thu Jan 31 2013 Alexey Gladkov <legion@altlinux.ru> 1:2.15.1-alt2
- Fix build.
- Add to seamonkey-lightning, seamonkey-devel a strict dependency on seamonkey.
- Remove recursive build dependency.

* Tue Jan 22 2013 Radik Usupov <radik@altlinux.org> 1:2.15.1-alt1
- New version seamonkey (2.15.1)
- New version enigmail (1.5.0)

* Sun Dec 09 2012 Radik Usupov <radik@altlinux.org> 1:2.14.1-alt1
- New version seamonkey (2.14.1)

* Fri Nov 23 2012 Radik Usupov <radik@altlinux.org> 1:2.14-alt1
- New version seamonkey (2.14)
- New version enigmail (1.4.6)

* Wed Oct 31 2012 Radik Usupov <radik@altlinux.org> 1:2.13.2-alt1
- New version seamonkey (2.13.2) (Closes: 27764)

* Thu Oct 18 2012 Radik Usupov <radik@altlinux.org> 1:2.13.1-alt1
- New version seamonkey (2.13.1) (tnx legion@)
- New version enigmail (1.4.5)
- Build with rpm-build-seamonkey (external build macros)
- Added devel packages

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:2.8-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for seamonkey
  * postclean-03-private-rpm-macros for the spec file

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 1:2.8-alt1
- New version seamonkey (2.8)
- Fixed automatic install from specific locations (tnx legion@)
- New version enigmail (1.4)

* Thu Feb 09 2012 Radik Usupov <radik@altlinux.org> 1:2.7-alt1
- New version seamonkey (2.7)
- New version enigmail (1.3.5)
- Added seamonkey-lightning package

* Thu Feb 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.5-alt1.qa1
- Rebuilt with libvpx.so.1.

* Wed Nov 23 2011 Radik Usupov <radik@altlinux.org> 1:2.5-alt1
- New version seamonkey (2.5)
- New version enigmail (1.3.3)

* Fri Sep 30 2011 Radik Usupov <radik@altlinux.org> 1:2.4.1-alt1
- New version (2.4.1)

* Wed Sep 07 2011 Radik Usupov <radik@altlinux.org> 1:2.3.3-alt1
- New version (2.3.3)

* Thu Sep 01 2011 Radik Usupov <radik@altlinux.org> 1:2.3.2-alt1
- New version (2.3.2)

* Sun Aug 28 2011 Radik Usupov <radik@altlinux.org> 1:2.3.1-alt1
- New version (2.3.1)
- Provides: seamonkey-devel

* Wed Aug 17 2011 Radik Usupov <radik@altlinux.org> 1:2.3-alt1
- New version (2.3)

* Fri Jul 22 2011 Radik Usupov <radik@altlinux.org> 1:2.2-alt1
- New version (2.2)

* Thu Mar 17 2011 Radik Usupov <radik@altlinux.org> 1:2.0.14-alt1
- New version (2.0.14)
- Thanks legion@!
