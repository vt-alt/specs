%def_with	enigmail
%def_without	google_calendar
%def_with	bundled_cbindgen
%def_enable     mach_build
%define 	r_name thunderbird
%ifndef build_parallel_jobs
%define build_parallel_jobs 32
%endif

%define enigmail_version  2.1.6
%define gdata_version     2.6

Summary:	Thunderbird is Mozilla's e-mail client
Name:		thunderbird
Version:	68.9.0
Release:	alt1
License:	MPL-2.0
Group:		Networking/Mail
URL:		https://www.thunderbird.net

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar
Source1:	enigmail-source.tar
Source2:	rpm-build.tar
Source3:	thunderbird.desktop
Source4:	thunderbird-mozconfig
Source5:	thunderbird-default-prefs.js
Source6:	lightning-langpacks-%version.tar.xz
# Get $HOME/.cargo after run cargo install cbindgen (without bin/cbindgen)
Source7:	cbindgen-source.tar.bz2
Source8:        thunderbird-wayland.desktop

Patch11:	thunderbird-alt-allow-send-in-windows-1251.patch

Patch21:        mozilla-1353817.patch
Patch23:        build-aarch64-skia.patch
Patch25:        Bug-1238661---fix-mozillaSignalTrampoline-to-work-.patch
Patch29:        thunderbird-60.7.2-alt-ppc64le-disable-broken-getProcessorLineSize-code.patch
Patch30:        thunderbird-68.2.2-alt-ppc64le-fix-clang-error-invalid-memory-operand.patch
Patch31: 	mozilla-1512162.patch
Patch33:	mozilla-1576268.patch

Patch40:        enigmail-use-juniorModeForceOff.patch
Patch42:	enigmail-gost.patch
Patch43:        enigmail-disable-pEpAutoDownload.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

%ifarch %{arm} %{ix86}
BuildRequires: gcc-c++
%endif
BuildRequires: clang
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: lld-devel
BuildRequires: libstdc++-devel
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel libXcomposite-devel libXdamage-devel
BuildRequires: libXcursor-devel libXi-devel libxkbcommon-devel
BuildRequires: libcurl-devel libgtk+3-devel libhunspell-devel libjpeg-devel
BuildRequires: libgtk+2-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: bzlib-devel zlib-devel
BuildRequires: mozldap-devel
BuildRequires: zip unzip
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: libvpx5-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel
BuildRequires: libproxy-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libdbus-glib-devel
BuildRequires: node
BuildRequires: nasm

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

# Mozilla requires
BuildRequires:	libnspr-devel
BuildRequires:	libnss-devel
BuildRequires:	libnss-devel-static

Provides:	mailclient
Obsoletes:	thunderbird-calendar
Obsoletes:	thunderbird-calendar-timezones

Provides:	thunderbird-gnome-support = %version-%release
Obsoletes:	thunderbird-gnome-support

Requires:	hunspell-en
Requires:	browser-plugins-npapi

Provides:	%name-esr = %version-%release
Obsoletes:	%name-esr < %version-%release
Provides: 	%name-lightning = %version-%release
Obsoletes:	%name-lightning < %version-%release
Provides: 	%name-esr-lightning = %version-%release
Obsoletes:	%name-esr-lightning < %version-%release

# Protection against fraudulent DigiNotar certificates
Requires:	libnss >= 3.13.1-alt1

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%define tbird_cid                    \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
%define tbird_prefix                 %_libdir/%r_name
%define tbird_datadir                %_datadir/%r_name
%define tbird_idldir                 %_datadir/idl/%r_name
%define tbird_includedir             %_includedir/%r_name
%define tbird_develdir               %tbird_prefix-devel

%description
Thunderbird is Mozilla's next generation e-mail client.
Thunderbird makes emailing safer, faster and easier than
ever before and can also scale to meet the most sophisticated
organizational needs.
The package contains Lightning - an integrated calendar for Thunderbird.

%package wayland
Summary: Thunderbird Wayland launcher
Group: Networking/Mail
BuildArch: noarch
Requires: %name

%description wayland
The thunderbird-wayland package contains launcher and desktop file
to run Thunderbird natively on Wayland.

%if_with enigmail
%package enigmail
%define enigmail_ciddir %mozilla_arch_extdir/%tbird_cid/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
Summary: Enigmail - GPG support for Mozilla Thunderbird
Group: Networking/Mail
Url: https://www.enigmail.net/

Provides:  %name-enigmail = %enigmail_version-%release
Provides:  %name-esr-enigmail = %version-%release
Obsoletes: %name-esr-enigmail < %version-%release
Requires:  %name = %version-%release
Requires:  pinentry-x11

%description enigmail
Enigmail is an extension to the mail client of Mozilla / Netscape 7.x
which allows users to access the authentication and encryption features
provided by the popular GnuPG software.
%endif

%if_with google_calendar
%package google-calendar
%define google_calendar_ciddir %mozilla_noarch_extdir/%tbird_cid/\{a62ef8ec-5fdc-40c2-873c-223b8a6925cc\}
Summary: Provider for Google Calendar
Group: Office
Url: https://www.mozilla.org/projects/calendar

Provides: %name-google-calendar = %gdata_version-%release
Requires: %name = %version-%release

Provides: gdata-provider = %gdata_version-%release
Provides:  %name-esr-google-calendar = %version-%release
Obsoletes: %name-esr-google-calendar < %version-%release

%description google-calendar
Allows bidirectional access to Google Calendar
%endif

%package devel
Summary:	Thunderbird development kit.
Group:		Development/C++
Requires:	%name = %version-%release

Requires:	python-base
AutoReq:	yes, nopython
Provides:  	%name-esr-devel = %version-%release
Obsoletes:	%name-esr-devel < %version-%release


%description devel
Thunderbird development kit.

%package -n rpm-build-%name
Summary: 	RPM helper macros to rebuild thunderbird packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org

%description -n rpm-build-%name
These helper macros provide possibility to rebuild
thunderbird packages by some Alt Linux Team Policy compatible way.

%prep
%setup -q

%if_with bundled_cbindgen
tar xf %SOURCE7
%endif

%if_with enigmail
tar -xf %SOURCE1
%patch40 -p1
%patch42 -p1
%patch43 -p1
# Fix <br> in translations
subst 's|<html:br/>|<html:br></html:br>|g' enigmail/lang/*/enigmail.dtd
%endif

tar -xf %SOURCE2

%patch11 -p2
%patch21 -p2
%patch23 -p2
%ifarch %arm
%patch25 -p1
%endif
%patch29 -p2
%patch30 -p2
%patch31 -p1
%patch33 -p1

#echo %version > mail/config/version.txt

cp -f %SOURCE4 .mozconfig

%ifnarch ppc64le %{arm} %{ix86}
echo "ac_add_options --enable-linker=lld" >> .mozconfig
%else
echo "ac_add_options --enable-linker=bfd" >> .mozconfig
%endif
%ifarch %{ix86} x86_64
echo "ac_add_options --disable-elf-hack" >> .mozconfig
%endif

# Non blocking stdout for NodeJS
cat > "/tmp/node-stdout-nonblocking-wrapper" << ENDL.
#!/bin/sh
exec /usr/bin/node "\$@" 2>&1 | cat -
ENDL.
chmod +x /tmp/node-stdout-nonblocking-wrapper
echo 'export NODEJS="/tmp/node-stdout-nonblocking-wrapper"' >> .mozconfig

sed -i -e '\,hyphenation/,d' comm/mail/installer/removed-files.in

%build
%add_optflags %optflags_shared
%add_findprov_lib_path %tbird_prefix

%if_with bundled_cbindgen
env CARGO_HOME=.cargo cargo --offline install cbindgen
export PATH=`pwd`/.cargo/bin:$PATH
%endif

# Add fake RPATH
rpath="/$(printf %%s '%tbird_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2

export MOZ_BUILD_APP=mail

# -fpermissive is needed to build with gcc 4.6+ which has become stricter
#
# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo "%optflags -fpermissive" | \
                      sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g' \
                      -e 's/-frecord-gcc-switches/-grecord-gcc-switches/')
# Disable null pointer gcc6 optimization - workaround for
# https://bugzilla.mozilla.org/show_bug.cgi?id=1278795
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fno-delete-null-pointer-checks -fno-schedule-insns2"
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"

%ifarch aarch64 x86_64
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

#ifarch %{arm} %{ix86}
#export CC="gcc"
#export CXX="g++"
#else
export CC="clang"
export CXX="clang++"
#endif
export PREFIX='%_prefix'
export LIBDIR='%_libdir'
export INCLUDEDIR='%_includedir'
export LIBIDL_CONFIG='/usr/bin/libIDL-config-2'
export srcdir="$PWD"
export SHELL=/bin/sh
export MOZILLA_OBJDIR="$PWD"

%__autoconf

mkdir objdir

# Do not use desktop notify during build process
export MOZ_NOSPAM=1

# Don't throw "old profile" dialog box
export MOZ_ALLOW_DOWNGRADE=1

export NPROCS=%build_parallel_jobs
# Decrease NPROCS prevents oomkill terror on x86_64
%ifarch x86_64
export NPROCS=16
%endif
# Build for i586 in one thread
%ifarch %ix86
export NPROCS=1
%endif

./mach configure
%if_enabled mach_build
./mach build -j $NPROCS
./mach buildsymbols
%else
make -f client.mk \
	STRIP="/bin/true" \
	mozappdir=%buildroot%tbird_prefix \
        OBJDIR=objdir \
        TOPSRCDIR=$srcdir \
        MOZ_PARALLEL_BUILD=$NPROCS
	MACH=1 \
	build
%endif

%if_with enigmail
dir="$PWD/objdir"
pushd enigmail
	%_configure_update_config
	./configure
	make \
		STRIP="/bin/true" \
		MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"
	mkdir -p $dir/mozilla/dist
	unzip build-tb/enigmail*.xpi -d $dir/mozilla/dist/enigmail
popd
%endif

%install
export SHELL=/bin/sh
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%mozilla_arch_extdir/%tbird_cid \
	%buildroot/%mozilla_noarch_extdir/%tbird_cid \
	%buildroot/%_datadir/applications \
	#

%makeinstall -C objdir \
	idldir=%buildroot/%tbird_idldir \
	includedir=%buildroot/%tbird_includedir \
	mozappdir=%buildroot/%tbird_prefix \
	#

(set +x
	for f in %buildroot/%tbird_develdir/*; do
		[ -L "$f" ] || continue

		t="$(readlink "$f")"
		r="$(relative "${t#%buildroot}" "${f#%buildroot}")"

		ln -vnsf -- "$r" "$f"
	done
)

(set +x
	rm -vrf -- %buildroot/%tbird_prefix/dictionaries/*
	for suf in aff dic; do
		t="$(relative %_datadir/myspell/en_US.$suf %tbird_prefix/dictionaries/)"
		ln -vs "$t" %buildroot/%tbird_prefix/dictionaries/en-US.$suf
	done
)

rm -rf -- \
	%buildroot/%_bindir/thunderbird \
	%buildroot/%tbird_prefix/js \
	%buildroot/%tbird_prefix/regxpcom \
	%buildroot/%tbird_prefix/xpcshell \
	%buildroot/%tbird_prefix/xpidl \
	%buildroot/%tbird_prefix/xpt_dump \
	%buildroot/%tbird_prefix/xpt_link \
	%buildroot/%tbird_prefix/nsinstall \
	%buildroot/%tbird_prefix/removed-files \
	%buildroot/%tbird_prefix/thunderbird \
	%buildroot/%tbird_prefix/run-mozilla.sh \
	%buildroot/%tbird_prefix/README.txt \
	#

# desktop files
install -Dpm644 %SOURCE3 %buildroot/%_desktopdir/thunderbird.desktop
install -Dpm644 %SOURCE8 %buildroot/%_desktopdir/thunderbird-wayland.desktop

# install altlinux-specific configuration
install -Dpm644 %SOURCE5 %buildroot/%tbird_prefix/defaults/pref/all-altlinux.js

# icons
for s in 16 22 24 32 48 64 128 256; do
	install -Dpm644 \
		comm/mail/branding/thunderbird/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/thunderbird.png
done
install -Dm644 comm/mail/branding/thunderbird/TB-symbolic.svg \
               %buildroot%_iconsdir/hicolor/symbolic/apps/thunderbird-symbolic.svg

# main startup script
cat>%buildroot/%_bindir/thunderbird<<-EOF
	#!/bin/sh -e
	export MOZ_APP_LAUNCHER="\${MOZ_APP_LAUNCHER:-\$0}"
	export MOZ_PLUGIN_PATH="%browser_plugins_path\${MOZ_PLUGIN_PATH:+:\$MOZ_PLUGIN_PATH}"
	export NSS_SSL_ENABLE_RENEGOTIATION=1
	%tbird_prefix/thunderbird-bin \${1:+"\$@"}
EOF
chmod 755 %buildroot/%_bindir/thunderbird

# rpm-build-thunderbird files
mkdir -p %buildroot%_rpmmacrosdir
sed -e 's,@tbird_version@,%version,' \
    -e 's,@tbird_release@,%release,' \
    rpm-build/rpm.macros \
    > %buildroot%_rpmmacrosdir/%r_name

%if_with enigmail
cp -a \
	$PWD/objdir/mozilla/dist/enigmail \
	%buildroot/%enigmail_ciddir
%endif

%if_with google_calendar
mkdir -p %buildroot/%google_calendar_ciddir
unzip -q -u -d %buildroot/%google_calendar_ciddir -- \
	$PWD/objdir/dist/xpi-stage/gdata-provider*.xpi
%endif

# Add real RPATH
(set +x
	rpath="/$(printf %%s '%tbird_prefix' |tr '[:print:]' '_')"

	find \
		%buildroot%tbird_prefix \
		%buildroot%mozilla_arch_extdir/%tbird_cid \
	-type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | fgrep -qs ELF || continue

		if chrpath -l "$t" | egrep -qs "R(UN)?PATH=$rpath"; then
			chrpath -r "%tbird_prefix" "$t"
		fi
	done
)

# Replace packed Lightning extension by unpackaged one to able apply localization by separate packages
%define lightning_dir %buildroot%_libdir/%name/extensions/\{e2fda1a4-762b-4020-b5ad-a41df1933103\}
rm -f %lightning_dir.xpi
mkdir -p %lightning_dir
cp -aL objdir/dist/bin/distribution/extensions/\{e2fda1a4-762b-4020-b5ad-a41df1933103\}/* \
       %lightning_dir

# lightning langpacks install
cd %buildroot%_libdir/%name/extensions
tar xf %SOURCE6
chmod a+r *.xpi

# Wrapper for wayland
cat > %buildroot%_bindir/thunderbird-wayland <<'EOF'
#!/bin/sh
export GDK_BACKEND=wayland
export MOZ_ENABLE_WAYLAND=1
export MOZ_GTK_TITLEBAR_DECORATION=client
export XDG_SESSION_TYPE=wayland

unset DISPLAY

exec %_bindir/thunderbird "$@"
EOF
chmod +x %buildroot%_bindir/thunderbird-wayland

%files
%doc AUTHORS
%_bindir/*
%tbird_prefix
%mozilla_arch_extdir/%tbird_cid
%mozilla_noarch_extdir/%tbird_cid
%defattr(0644,root,root,0755)
%_datadir/applications/%r_name.desktop
%_iconsdir/hicolor/*/apps/thunderbird.png
%_iconsdir/hicolor/symbolic/apps/thunderbird-symbolic.svg

%files wayland
%_bindir/thunderbird-wayland
%_datadir/applications/thunderbird-wayland.desktop

%if_with enigmail
%exclude %enigmail_ciddir
%endif
%if_with google_calendar
%exclude %google_calendar_ciddir
%endif

%if_with enigmail
%files enigmail
%enigmail_ciddir
%endif

%if_with google_calendar
%files google-calendar
%google_calendar_ciddir
%endif

#%%files devel
#%%tbird_idldir
#%%tbird_includedir
#%%tbird_develdir

%files -n rpm-build-%name
%_rpmmacrosdir/%r_name

%changelog
* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 68.9.0-alt1
- New version (68.9.0).
- Fixes:
  + CVE-2020-12399 Timing attack on DSA signatures in NSS library
  + CVE-2020-12405 Use-after-free in SharedWorkerService
  + CVE-2020-12406 JavaScript Type confusion with NativeTypes
  + CVE-2020-12410 Memory safety bugs fixed in Thunderbird 68.9.0
  + CVE-2020-12398 Security downgrade with IMAP STARTTLS leads to information leakage

* Fri May 29 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.1-alt2
- Build with default llvm-devel in repository.
- Fix rpm macros placement.

* Sat May 23 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.1-alt1
- New version (68.8.1).
- Fixes:
  + IMAP stability improvements
  + HTML tags in IRC topic changes were rendered incorrectly
  + MailExtensions: Websockets could not be used

* Wed May 06 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.0-alt2
- Add security fixes information to changelog.

* Tue May 05 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.0-alt1
- New version (68.8.0).
- Fixes:
  + CVE-2020-12397 Sender Email Address Spoofing using encoded Unicode characters
  + CVE-2020-12387 Use-after-free during worker shutdown
  + CVE-2020-6831 Buffer overflow in SCTP chunk input validation
  + CVE-2020-12392 Arbitrary local file access with 'Copy as cURL'
  + CVE-2020-12393 Devtools' 'Copy as cURL' feature did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2020-12395 Memory safety bugs fixed in Thunderbird 68.8.0

* Mon May 04 2020 Andrey Cherepanov <cas@altlinux.org> 68.7.0-alt3
- Add Wayland support (ALT #38433).

* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 68.7.0-alt2
- Add security fixes information to changelog.

* Wed Apr 08 2020 Andrey Cherepanov <cas@altlinux.org> 68.7.0-alt1
- New version (68.7.0).
- Fixes:
  + CVE-2020-6819 Use-after-free while running the nsDocShell destructor
  + CVE-2020-6820 Use-after-free when handling a ReadableStream
  + CVE-2020-6821 Uninitialized memory could be read when using the WebGL copyTexSubImage method
  + CVE-2020-6822 Out of bounds write in GMPDecodeData when processing large images
  + CVE-2020-6825 Memory safety bugs fixed in Thunderbird 68.7.0
- Enigmail 2.1.6.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 68.6.0-alt1
- New version (68.6.0).
- Fixed:
  + CVE-2020-6805 Use-after-free when removing data about origins
  + CVE-2020-6806 BodyStream::OnInputStreamReady was missing protections against state confusion
  + CVE-2020-6807 Use-after-free in cubeb during stream destruction
  + CVE-2020-6811 Devtools' 'Copy as cURL' feature did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2019-20503 Out of bounds reads in sctp_load_addresses_from_init
  + CVE-2020-6812 The names of AirPods with personally identifiable information were exposed to websites with camera or microphone permission
  + CVE-2020-6814 Memory safety bugs fixed in Thunderbird 68.6

* Wed Feb 12 2020 Andrey Cherepanov <cas@altlinux.org> 68.5.0-alt1
- New version (68.5.0).
- Fixed:
  + CVE-2020-6793 Out-of-bounds read when processing certain email messages
  + CVE-2020-6794 Setting a master password post-Thunderbird 52 does not delete unencrypted previously stored passwords
  + CVE-2020-6795 Crash processing S/MIME messages with multiple signatures
  + CVE-2020-6797 Extensions granted downloads.open permission could open arbitrary applications on Mac OSX
  + CVE-2020-6798 Incorrect parsing of template tag could result in JavaScript injection
  + CVE-2020-6792 Message ID calculcation was based on uninitialized data
  + CVE-2020-6800 Memory safety bugs fixed in Thunderbird 68.5

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 68.4.2-alt1
- New version.

* Sat Jan 11 2020 Andrey Cherepanov <cas@altlinux.org> 68.4.1-alt1
- New version (68.4.1).
- Fixed:
  + CVE-2019-17026 IonMonkey type confusion with StoreElementHole and FallibleStoreElement
  + CVE-2019-17015 Memory corruption in parent process during new content process initialization on Windows
  + CVE-2019-17016 Bypass of @namespace CSS sanitization during pasting
  + CVE-2019-17017 Type Confusion in XPCVariant.cpp
  + CVE-2019-17021 Heap address disclosure in parent process during content process initialization on Windows
  + CVE-2019-17022 CSS sanitization does not escape HTML tags
  + CVE-2019-17024 Memory safety bugs fixed in Thunderbird 68.4.1
- Enigmail 2.1.5.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 68.3.1-alt1
- New version (68.3.1).
- Fixed:
  + CVE-2019-17008 Use-after-free in worker destruction
  + CVE-2019-13722 Stack corruption due to incorrect number of arguments in WebRTC code
  + CVE-2019-11745 Out of bounds write in NSS when encrypting with a block cipher
  + CVE-2019-17009 Updater temporary files accessible to unprivileged processes
  + CVE-2019-17010 Use-after-free when performing device orientation checks
  + CVE-2019-17005 Buffer overflow in plain text serializer
  + CVE-2019-17011 Use-after-free when retrieving a document in antitracking
  + CVE-2019-17012 Memory safety bugs fixed in Firefox 71, Firefox ESR 68.3, and Thunderbird 68.3
- Enigmail 2.1.4.

* Sat Nov 09 2019 Andrey Cherepanov <cas@altlinux.org> 68.2.2-alt1
- New version (68.2.2).
- Fixed:
  + CVE-2019-15903 Heap overflow in expat library in XML_GetCurrentLineNumber
  + CVE-2019-11757 Use-after-free when creating index updates in IndexedDB
  + CVE-2019-11758 Potentially exploitable crash due to 360 Total Security
  + CVE-2019-11759 Stack buffer overflow in HKDF output
  + CVE-2019-11760 Stack buffer overflow in WebRTC networking
  + CVE-2019-11761 Unintended access to a privileged JSONView object
  + CVE-2019-11762 document.domain-based origin isolation has same-origin-property violation
  + CVE-2019-11763 Incorrect HTML parsing results in XSS bypass technique
  + CVE-2019-11764 Memory safety bugs fixed in Thunderbird 68.2
- Enigmail 2.1.3.

* Sun Oct 13 2019 Andrey Cherepanov <cas@altlinux.org> 68.1.2-alt1
- New version (68.1.2).
- Fixed:
  + CVE-2019-11739 Covert Content Attack on S/MIME encryption using a crafted multipart/alternative message
  + CVE-2019-11746 Use-after-free while manipulating video
  + CVE-2019-11744 XSS by breaking out of title and textarea elements using innerHTML
  + CVE-2019-11742 Same-origin policy violation with SVG filters and canvas to steal cross-origin images
  + CVE-2019-11752 Use-after-free while extracting a key value in IndexedDB
  + CVE-2019-11743 Cross-origin access to unload event attributes
  + CVE-2019-11740 Memory safety bugs fixed in Firefox 69, Firefox ESR 68.1, Firefox ESR 60.9, Thunderbird 68.1, and Thunderbird 60.9
  + CVE-2019-11755 Spoofing a message author via a crafted S/MIME message

* Thu Aug 29 2019 Andrey Cherepanov <cas@altlinux.org> 68.0-alt1
- New version (68.0).
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
  + CVE-2019-11709 Memory safety bugs fixed in Firefox 68, Firefox ESR 60.8, and Thunderbird 60.8
- Enigmail 2.1.2.

* Wed Jul 10 2019 Andrey Cherepanov <cas@altlinux.org> 60.8.0-alt1
- New version (60.8.0).
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
  + CVE-2019-11709 Memory safety bugs fixed in Firefox 68, Firefox ESR 60.8, and Thunderbird 60.8
- Enigmail 2.0.12.

* Wed Jul 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 60.7.2-alt2
- Added ppc64le support.

* Sat Jun 22 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.2-alt1
- New version (60.7.2).
- Fixed:
  + CVE-2019-11707 Type confusion in Array.pop
  + CVE-2019-11708 sandbox escape using Prompt:Open

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.1-alt2
- enigmail: disable pEpAutoDownload.

* Fri Jun 14 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.1-alt1
- New version (60.7.1).
- Fixed:
  + CVE-2019-11703 Heap buffer overflow in icalparser.c
  + CVE-2019-11704 Heap buffer overflow in icalvalue.c
  + CVE-2019-11705 Stack buffer overflow in icalrecur.c
  + CVE-2019-11706 Type confusion in icalproperty.c
- Enigmail 2.0.11.
- thunderbird-enigmail now requires pinentry-x11 (ALT #18790).
- Use juniorModeForceOff by default in Enigmail (ALT #36447).
- Fix l10n dtd of Enigmail.

* Mon May 20 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.0-alt1
- New version (60.7.0).
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
  + CVE-2019-9800 Memory safety bugs fixed in Firefox 67, Firefox ESR 60.7, and Thunderbird 60.7

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.1-alt2
- Fix global serch indexing by link with bundled sqlite3 (ALT #35761).

* Tue Mar 26 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.1-alt1
- New version (60.6.1).
- Fixes:
  + CVE-2019-9810 IonMonkey MArraySlice has incorrect alias information
  + CVE-2019-9813 Ionmonkey type confusion with __proto__ mutations

* Thu Mar 21 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.0-alt1
- New version (60.6.0).
- Fixes:
  + CVE-2019-9790 Use-after-free when removing in-use DOM elements
  + CVE-2019-9791 Type inference is incorrect for constructors entered through on-stack replacement with IonMonkey
  + CVE-2019-9792 IonMonkey leaks JS_OPTIMIZED_OUT magic value to script
  + CVE-2019-9793 Improper bounds checks when Spectre mitigations are disabled
  + CVE-2019-9794 Command line arguments not discarded during execution
  + CVE-2019-9795 Type-confusion in IonMonkey JIT compiler
  + CVE-2019-9796 Use-after-free with SMIL animation controller
  + CVE-2019-9801 Windows programs that are not 'URL Handlers' are exposed to web content
  + CVE-2018-18506 Proxy Auto-Configuration file can define localhost access to be proxied
  + CVE-2019-9788 Memory safety bugs fixed in Firefox 66, Firefox ESR 60.6, and Thunderbird 60.6
- Build with Clang.

* Wed Feb 27 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.2-alt1
- New version (60.5.2).

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.1-alt1
- New version (60.5.1).
- Fixes:
  + CVE-2018-18356 Use-after-free in Skia
  + CVE-2019-5785 Integer overflow in Skia
  + CVE-2018-18335 Buffer overflow in Skia with accelerated Canvas 2D
  + CVE-2018-18509 S/MIME signature spoofing

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.0-alt1
- New version (60.5.0).
- Fixes:
  + CVE-2018-18500 Use-after-free parsing HTML5 stream
  + CVE-2018-18505 Privilege escalation through IPC channel messages
  + CVE-2016-5824 DoS (use-after-free) via a crafted ics file
  + CVE-2018-18501 Memory safety bugs fixed in Firefox 65, Firefox ESR 60.5, and Thunderbird 60.5

* Tue Jan 29 2019 Paul Wolneykien <manowar@altlinux.org> 60.4.0-alt3
- Added Enigmail GOST patch.

* Thu Jan 10 2019 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt2
- Rebuild with llvm7.0.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt1
- New version (60.4.0).
- Enigmail 2.0.9.
- Fixes:
  + CVE-2018-17466 Buffer overflow and out-of-bounds read in ANGLE library with TextureStorage11
  + CVE-2018-18492 Use-after-free with select element
  + CVE-2018-18493 Buffer overflow in accelerated 2D canvas with Skia
  + CVE-2018-18494 Same-origin policy violation using location attribute and performance.getEntries to steal cross-origin URLs
  + CVE-2018-18498 Integer overflow when calculating buffer sizes for images
  + CVE-2018-12405 Memory safety bugs fixed in Firefox 64, Firefox ESR 60.4, and Thunderbird 60.4

* Sun Dec 09 2018 Andrey Cherepanov <cas@altlinux.org> 60.3.3-alt1
- New version (60.3.3).

* Fri Nov 30 2018 Andrey Cherepanov <cas@altlinux.org> 60.3.2-alt1
- New version (60.3.2).

* Thu Nov 22 2018 Andrey Cherepanov <cas@altlinux.org> 60.3.1-alt1
- New version (60.3.1).

* Fri Nov 02 2018 Andrey Cherepanov <cas@altlinux.org> 60.3.0-alt1
- New version (60.3.0).
- Fixes:
  + CVE-2018-12391 HTTP Live Stream audio data is accessible cross-origin
  + CVE-2018-12392 Crash with nested event loops
  + CVE-2018-12393 Integer overflow during Unicode conversion while loading JavaScript
  + CVE-2018-12389 Memory safety bugs fixed in Firefox ESR 60.3 and Thunderbird 60.3
  + CVE-2018-12390 Memory safety bugs fixed in Firefox 63, Firefox ESR 60.3, and Thunderbird 60.3

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.1-alt1
- New version (60.2.1).
- Fixes:
  + CVE-2018-12377 Use-after-free in refresh driver timers
  + CVE-2018-12378 Use-after-free in IndexedDB
  + CVE-2018-12379 Out-of-bounds write with malicious MAR file
  + CVE-2017-16541 Proxy bypass using automount and autofs
  + CVE-2018-12376 Memory safety bugs fixed in Firefox 62 and Firefox ESR 60.2
  + CVE-2018-12385 Crash in TransportSecurityInfo due to cached data
  + CVE-2018-12383 Setting a master password post-Firefox 58 does not delete unencrypted previously stored passwords

* Mon Aug 13 2018 Andrey Cherepanov <cas@altlinux.org> 60.0-alt1
- New version (60.0).
- Enigmail 2.0.8.
- Fixes:
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
  + CVE-2018-5187 Memory safety bugs fixed in Firefox 61, Firefox ESR 60.1, and Thunderbird 60
  + CVE-2018-5188 Memory safety bugs fixed in Firefox 61, Firefox ESR 60.1, Firefox ESR 52.9, and Thunderbird 60

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 52.9.1-alt1
- New version (52.9.1).
- Complete fix of the EFAIL vulnerability.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 52.9.0-alt1
- New version (52.9.0).
- Enigmail 2.0.7.
- Fixes:
  + CVE-2018-12359 Buffer overflow using computed size of canvas element
  + CVE-2018-12360 Use-after-free when using focus()
  + CVE-2018-12372 S/MIME and PGP decryption oracles can be built with HTML emails
  + CVE-2018-12373 S/MIME plaintext can be leaked through HTML reply/forward
  + CVE-2018-12362 Integer overflow in SSSE3 scaler
  + CVE-2018-12363 Use-after-free when appending DOM nodes
  + CVE-2018-12364 CSRF attacks through 307 redirects and NPAPI plugins
  + CVE-2018-12365 Compromised IPC child process can list local filenames
  + CVE-2018-12366 Invalid data handling during QCMS transformations
  + CVE-2018-12368 No warning when opening executable SettingContent-ms files
  + CVE-2018-12374 Using form to exfiltrate encrypted mail part by pressing enter in form field
  + CVE-2018-5188 Memory safety bugs fixed in Firefox 60, Firefox ESR 60.1, Firefox ESR 52.9, and Thunderbird 52.9

* Sat May 19 2018 Andrey Cherepanov <cas@altlinux.org> 52.8.0-alt1
- New version (52.8.0).
- Enigmail 2.0.4.
- Fixes:
  + CVE-2018-5183 Backport critical security fixes in Skia
  + CVE-2018-5184 Full plaintext recovery in S/MIME via chosen-ciphertext attack
  + CVE-2018-5154 Use-after-free with SVG animations and clip paths
  + CVE-2018-5155 Use-after-free with SVG animations and text paths
  + CVE-2018-5159 Integer overflow and out-of-bounds write in Skia
  + CVE-2018-5161 Hang via malformed headers
  + CVE-2018-5162 Encrypted mail leaks plaintext through src attribute
  + CVE-2018-5170 Filename spoofing for external attachments
  + CVE-2018-5168 Lightweight themes can be installed without user interaction
  + CVE-2018-5178 Buffer overflow during UTF-8 to Unicode string conversion through legacy extension
  + CVE-2018-5185 Leaking plaintext through HTML forms
  + CVE-2018-5150 Memory safety bugs fixed in Firefox 60, Firefox ESR 52.8, and Thunderbird 52.8
- Build in several threads.

* Sat Mar 24 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.0-alt1
- New version (52.7.0)
- Fixes:
  + CVE-2018-5127 Buffer overflow manipulating SVG animatedPathSegList
  + CVE-2018-5129 Out-of-bounds write with malformed IPC messages
  + CVE-2018-5144 Integer overflow during Unicode conversion
  + CVE-2018-5146 Out of bounds memory write in libvorbis
  + CVE-2018-5125 Memory safety bugs fixed in Firefox 59, Firefox ESR 52.7, and Thunderbird 52.7
  + CVE-2018-5145 Memory safety bugs fixed in Firefox ESR 52.7 and Thunderbird 52.7

* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt1
- New version (52.6.0)
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
  + CVE-2018-5089 Memory safety bugs fixed in Firefox 58, Firefox ESR 52.6, and Thunderbird 52.6

* Mon Dec 25 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.2-alt1
- New version (52.5.2)
- Enigmail 1.9.9
- Fixes:
  + CVE-2017-7846 JavaScript Execution via RSS in mailbox:// origin
  + CVE-2017-7847 Local path string can be leaked from RSS feed
  + CVE-2017-7848 RSS Feed vulnerable to new line Injection
  + CVE-2017-7829 Mailsploit part 1: From address with encoded null character is cut off in message header display

* Fri Nov 24 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.0-alt1
- New version (52.5.0)
- Fixes:
  + CVE-2017-7828 Use-after-free of PressShell while restyling layout
  + CVE-2017-7830 Cross-origin URL information leak through Resource
  + CVE-2017-7826 Memory safety bugs fixed in Firefox 57, Firefox ESR 52.5, and Thunderbird 52.5

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 52.4.0-alt1
- New version (52.4.0)
- Enigmail 1.9.8.3
- Fixes:
  + CVE-2017-7793 Use-after-free with Fetch API
  + CVE-2017-7818 Use-after-free during ARIA array manipulation
  + CVE-2017-7819 Use-after-free while resizing images in design mode
  + CVE-2017-7824 Buffer overflow when drawing and validating elements with ANGLE
  + CVE-2017-7805 Use-after-free in TLS 1.2 generating handshake hashes
  + CVE-2017-7814 Blob and data URLs bypass phishing and malware protection warnings
  + CVE-2017-7825 OS X fonts render some Tibetan and Arabic unicode characters as spaces
  + CVE-2017-7823 CSP sandbox directive did not create a unique origin
  + CVE-2017-7810 Memory safety bugs fixed in Firefox 56, Firefox ESR 52.4, and Thunderbird 52.4

* Sun Aug 20 2017 Andrey Cherepanov <cas@altlinux.org> 52.3.0-alt1
- New version (52.3.0)
- Enigmail 1.9.8.1

* Mon Jun 26 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.1-alt1
- New version (52.2.1)

* Thu Jun 22 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.0-alt1
- New version (52.2.0)
- Security fixes:
  + CVE-2017-5472: Use-after-free using destroyed node when regenerating trees
  + CVE-2017-7749: Use-after-free during docshell reloading
  + CVE-2017-7750: Use-after-free with track elements
  + CVE-2017-7751: Use-after-free with content viewer listeners
  + CVE-2017-7752: Use-after-free with IME input
  + CVE-2017-7754: Out-of-bounds read in WebGL with ImageInfo object
  + CVE-2017-7756: Use-after-free and use-after-scope logging XHR header errors
  + CVE-2017-7757: Use-after-free in IndexedDB
  + CVE-2017-7778: Vulnerabilities in the Graphite 2 library
  + CVE-2017-7758: Out-of-bounds read in Opus encoder
  + CVE-2017-7763: Mac fonts render some unicode characters as spaces
  + CVE-2017-7764: Domain spoofing with combination of Canadian Syllabics and other unicode blocks
  + CVE-2017-7765: Mark of the Web bypass when saving executable files
  + CVE-2017-5470: Memory safety bugs fixed in Firefox 54 and Firefox ESR 52.2, and Thunderbird 52.2

* Tue May 16 2017 Andrey Cherepanov <cas@altlinux.org> 52.1.1-alt1
- New version (52.1.1)
- New Enigmail 1.9.7

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 52.1.0-alt1
- New version (52.0.1)
- Security fixes:
  + CVE-2017-5429: Memory safety bugs fixed in Firefox 53, Firefox ESR
  + CVE-2017-5430: Memory safety bugs fixed in Firefox 53, Firefox ESR
  + CVE-2017-5432: Use-after-free in text input selection
  + CVE-2017-5433: Use-after-free in SMIL animation functions
  + CVE-2017-5434: Use-after-free during focus handling
  + CVE-2017-5435: Use-after-free during transaction processing in the
  + CVE-2017-5436: Out-of-bounds write with malicious font in Graphite 2
  + CVE-2017-5438: Use-after-free in nsAutoPtr during XSLT processing
  + CVE-2017-5439: Use-after-free in nsTArray Length() during XSLT
  + CVE-2017-5440: Use-after-free in txExecutionState destructor during
  + CVE-2017-5441: Use-after-free with selection during scroll events
  + CVE-2017-5442: Use-after-free during style changes
  + CVE-2017-5443: Out-of-bounds write during BinHex decoding
  + CVE-2017-5444: Buffer overflow while parsing
  + CVE-2017-5445: Uninitialized values used while parsing
  + CVE-2017-5446: Out-of-bounds read when HTTP/2 DATA frames are sent
  + CVE-2017-5447: Out-of-bounds read during glyph processing
  + CVE-2017-5449: Crash during bidirectional unicode manipulation with
  + CVE-2017-5451: Addressbar spoofing with onblur event
  + CVE-2017-5454: Sandbox escape allowing file system read access through
  + CVE-2017-5459: Buffer overflow in WebGL
  + CVE-2017-5460: Use-after-free in frame selection
  + CVE-2017-5461: Out-of-bounds write in Base64 encoding in NSS
  + CVE-2017-5462: DRBG flaw in NSS
  + CVE-2017-5464: Memory corruption with accessibility and DOM
  + CVE-2017-5465: Out-of-bounds read in ConvolvePixel
  + CVE-2017-5466: Origin confusion when reloading isolated data:text/html
  + CVE-2017-5467: Memory corruption when drawing Skia content
  + CVE-2017-5469: Potential Buffer overflow in flex-generated code
  + CVE-2016-10196: Vulnerabilities in Libevent library

* Mon Apr 17 2017 Andrey Cherepanov <cas@altlinux.org> 52.0.1-alt1
- New version (52.0.1)

* Wed Apr 05 2017 Andrey Cherepanov <cas@altlinux.org> 52.0-alt1
- New version (52.0)

* Tue Mar 07 2017 Andrey Cherepanov <cas@altlinux.org> 45.8.0-alt1
- New versoin (45.8.0)

* Fri Mar 03 2017 Andrey Cherepanov <cas@altlinux.org> 45.7.1-alt1
- New version (45.7.1)
- Add windows-1251 to sendDefaultCharsetList
- Fix subdirectory name from mozilla to thunderbird-<version>

* Thu Feb 02 2017 Anton Farygin <rider@altlinux.ru> 45.7.0-alt3
- prevent thunderbird segfault due overoptimisation of new gcc6 (closes: #33048)

* Fri Jan 27 2017 Vladimir Didenko <cow@altlinux.org> 45.7.0-alt2
- Disable null pointer gcc6 optimization (closes: #33048)

* Thu Jan 26 2017 Andrey Cherepanov <cas@altlinux.org> 45.7.0-alt1
- New version (45.7.0)

* Sat Jan 21 2017 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt2
- Fix build with GCC 6.1

* Thu Dec 29 2016 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt1
- New version (45.6.0)

* Thu Dec 01 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.1-alt1
- New version (45.5.1)
- Security fixes:
  + MFSA 2016-92 Firefox SVG Animation Remote Code Execution

* Mon Nov 21 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.0-alt1
- New version (45.5.0)
- Enigmail 1.9.6.1

* Sat Oct 01 2016 Andrey Cherepanov <cas@altlinux.org> 45.4.0-alt1
- New version (45.4.0)

* Mon Sep 05 2016 Andrey Cherepanov <cas@altlinux.org> 45.3.0-alt1
- New version (45.3.0)
- Enigmail 1.9.5
- Remove separate package with Lightning because Lightning is part of
  Thunderbird

* Sat Jul 02 2016 Andrey Cherepanov <cas@altlinux.org> 45.2.0-alt1
- New version (45.2.0)
- Enigmail 1.9.3

* Wed Jun 01 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.1-alt1
- New version (45.1.1)

* Fri May 20 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.0-alt1
- New version (45.1.0)
- Enigmail 1.9.2
- Set correct URL and version to extension packages

* Thu Apr 14 2016 Andrey Cherepanov <cas@altlinux.org> 45.0.0-alt1
- New version (45.0.0)

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.1-alt1
- New version (38.7.1)

* Tue Mar 15 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt1
- New version (38.7.0)
- Enigmail (1.9.1)
- Obsoletes thunderbird-esr

* Wed Feb 17 2016 Andrey Cherepanov <cas@altlinux.org> 38.6.0-alt1
- New version
- Security fixes:
  + MFSA 2016-14 Vulnerabilities in Graphite 2
  + MFSA 2016-03 Buffer overflow in WebGL after out of memory allocation
  + MFSA 2016-01 Miscellaneous memory safety hazards (rv:44.0 / rv:38.6)
  + MFSA 2015-150 MD5 signatures accepted within TLS 1.2
    ServerKeyExchange in server signature

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 38.5.1-alt1
- New version

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.0-alt1
- New version
- Security fixes:
  + MFSA 2015-149 Cross-site reading attack through data and view-source URIs
  + MFSA 2015-146 Integer overflow in MP4 playback in 64-bit versions
  + MFSA 2015-145 Underflow through code inspection
  + MFSA 2015-139 Integer overflow allocating extremely large textures

* Thu Nov 26 2015 Alexey Gladkov <legion@altlinux.ru> 38.4.0-alt1
- New version (38.4.0).
- Enigmail (1.8.2).
- Fixed:
  + 2015-90 Vulnerabilities found through code inspection
  + 2015-88 Heap overflow in gdk-pixbuf when scaling bitmap images
  + 2015-85 Out-of-bounds write with Updater and malicious MAR file
  + 2015-84 Arbitrary file overwriting through Mozilla Maintenance Service with hard links
  + 2015-79 Miscellaneous memory safety hazards (rv:40.0 / rv:38.2)
  + 2015-71 NSS incorrectly permits skipping of ServerKeyExchange
  + 2015-70 NSS accepts export-length DHE keys with regular DHE cipher suites
  + 2015-67 Key pinning is ignored when overridable errors are encountered
  + 2015-66 Vulnerabilities found through code inspection
  + 2015-63 Use-after-free in Content Policy due to microtask execution error
  + 2015-59 Miscellaneous memory safety hazards (rv:39.0 / rv:31.8 / rv:38.1)

* Sat Jun 20 2015 Alexey Gladkov <legion@altlinux.ru> 38.0.1-alt1
- New version (38.0.1).

* Thu Dec 11 2014 Alexey Gladkov <legion@altlinux.ru> 31.3.0-alt1
- New version (31.3.0).
- Fixed:
  + MFSA 2014-90 Apple CoreGraphics framework on OS X 10.10 logging input data to /tmp directory
  + MFSA 2014-89 Bad casting from the BasicThebesLayer to BasicContainerLayer
  + MFSA 2014-88 Buffer overflow while parsing media content
  + MFSA 2014-87 Use-after-free during HTML5 parsing
  + MFSA 2014-85 XMLHttpRequest crashes with some input streams
  + MFSA 2014-83 Miscellaneous memory safety hazards (rv:34.0 / rv:31.3)

* Thu Oct 23 2014 Alexey Gladkov <legion@altlinux.ru> 31.2.0-alt1
- New version (31.2.0).
- Fixed:
  + MFSA 2014-81 Inconsistent video sharing within iframe
  + MFSA 2014-79 Use-after-free interacting with text directionality
  + MFSA 2014-77 Out-of-bounds write with WebM video
  + MFSA 2014-76 Web Audio memory corruption issues with custom waveforms
  + MFSA 2014-75 Buffer overflow during CSS manipulation
  + MFSA 2014-74 Miscellaneous memory safety hazards (rv:33.0 / rv:31.2)

* Thu Sep 25 2014 Alexey Gladkov <legion@altlinux.ru> 31.1.2-alt1
- New version (31.1.2).
- Fixed:
  + MFSA 2014-73 RSA Signature Forgery in NSS
  + MFSA 2014-72 Use-after-free setting text directionality
  + MFSA 2014-70 Out-of-bounds read in Web Audio audio timeline
  + MFSA 2014-69 Uninitialized memory use during GIF rendering
  + MFSA 2014-68 Use-after-free during DOM interactions with SVG
  + MFSA 2014-67 Miscellaneous memory safety hazards (rv:32.0 / rv:31.1 / rv:24.8)

* Mon Jul 28 2014 Alexey Gladkov <legion@altlinux.ru> 31.0-alt1
- New version (31.0).
- Fixed:
  + MFSA 2014-66 IFRAME sandbox same-origin access through redirect
  + MFSA 2014-65 Certificate parsing broken by non-standard character encoding
  + MFSA 2014-64 Crash in Skia library when scaling high quality images
  + MFSA 2014-63 Use-after-free while when manipulating certificates in the trusted cache
  + MFSA 2014-62 Exploitable WebGL crash with Cesium JavaScript library
  + MFSA 2014-61 Use-after-free with FireOnStateChange event
  + MFSA 2014-59 Use-after-free in DirectWrite font handling
  + MFSA 2014-58 Use-after-free in Web Audio due to incorrect control message ordering
  + MFSA 2014-57 Buffer overflow during Web Audio buffering for playback
  + MFSA 2014-56 Miscellaneous memory safety hazards (rv:31.0 / rv:24.7)

* Mon Jul 21 2014 Alexey Gladkov <legion@altlinux.ru> 24.6.0-alt1
- New version (24.6.0).
- Fixed:
  + MFSA 2014-52 Use-after-free with SMIL Animation Controller
  + MFSA 2014-49 Use-after-free and out of bounds issues found using Address Sanitizer
  + MFSA 2014-48 Miscellaneous memory safety hazards (rv:30.0 / rv:24.6)

* Sun May 11 2014 Alexey Gladkov <legion@altlinux.ru> 24.5.0-alt1
- New version (24.5.0).
- Fixed:
  + MFSA 2014-46 Use-after-free in nsHostResolve
  + MFSA 2014-44 Use-after-free in imgLoader while resizing images
  + MFSA 2014-43 Cross-site scripting (XSS) using history navigations
  + MFSA 2014-42 Privilege escalation through Web Notification API
  + MFSA 2014-38 Buffer overflow when using non-XBL object as XBL
  + MFSA 2014-37 Out of bounds read while decoding JPG images
  + MFSA 2014-35 Privilege escalation through Mozilla Maintenance Service Installer
  + MFSA 2014-34 Miscellaneous memory safety hazards (rv:29.0 / rv:24.5)

* Sun Mar 23 2014 Alexey Gladkov <legion@altlinux.ru> 24.4.0-alt1
- New version (24.4.0).
- Fixed:
  + MFSA 2014-32 Out-of-bounds write through TypedArrayObject after neutering
  + MFSA 2014-31 Out-of-bounds read/write through neutering ArrayBuffer objects
  + MFSA 2014-30 Use-after-free in TypeObject
  + MFSA 2014-29 Privilege escalation using WebIDL-implemented APIs
  + MFSA 2014-28 SVG filters information disclosure through feDisplacementMap
  + MFSA 2014-27 Memory corruption in Cairo during PDF font rendering
  + MFSA 2014-26 Information disclosure through polygon rendering in MathML
  + MFSA 2014-17 Out of bounds read during WAV file decoding
  + MFSA 2014-16 Files extracted during updates are not always read only
  + MFSA 2014-15 Miscellaneous memory safety hazards (rv:28.0 / rv:24.4)

* Sun Feb 09 2014 Alexey Gladkov <legion@altlinux.ru> 24.3.0-alt1
- New version (24.3.0).
- Fixed:
  + MFSA 2014-13 Inconsistent JavaScript handling of access to Window objects
  + MFSA 2014-12 NSS ticket handling issues
  + MFSA 2014-09 Cross-origin information leak through web workers
  + MFSA 2014-08 Use-after-free with imgRequestProxy and image proccessing
  + MFSA 2014-04 Incorrect use of discarded images by RasterImage
  + MFSA 2014-02 Clone protected content with XBL scopes
  + MFSA 2014-01 Miscellaneous memory safety hazards (rv:27.0 / rv:24.3)

* Tue Dec 24 2013 Alexey Gladkov <legion@altlinux.ru> 24.2.0-alt1
- New version (24.2.0).
- Fixed:
  + MFSA 2013-117 Mis-issued ANSSI/DCSSI certificate
  + MFSA 2013-116 JPEG information leak
  + MFSA 2013-115 GetElementIC typed array stubs can be generated outside observed typesets
  + MFSA 2013-114 Use-after-free in synthetic mouse movement
  + MFSA 2013-113 Trust settings for built-in roots ignored during EV certificate validation
  + MFSA 2013-111 Segmentation violation when replacing ordered list elements
  + MFSA 2013-109 Use-after-free during Table Editing
  + MFSA 2013-108 Use-after-free in event listeners
  + MFSA 2013-104 Miscellaneous memory safety hazards (rv:26.0 / rv:24.2)

* Thu Nov 21 2013 Alexey Gladkov <legion@altlinux.ru> 24.1.1-alt1
- New version (24.1.1).
- Fixed:
  + MFSA 2013-103 Miscellaneous Network Security Services (NSS) vulnerabilities

* Sun Nov 03 2013 Alexey Gladkov <legion@altlinux.ru> 24.1.0-alt1
- New version (24.1.0).
- Fixed:
  + MFSA 2013-102 Use-after-free in HTML document templates
  + MFSA 2013-101 Memory corruption in workers
  + MFSA 2013-100 Miscellaneous use-after-free issues found through ASAN fuzzing
  + MFSA 2013-98 Use-after-free when updating offline cache
  + MFSA 2013-97 Writing to cycle collected object during image decoding
  + MFSA 2013-96 Improperly initialized memory and overflows in some JavaScript functions
  + MFSA 2013-95 Access violation with XSLT and uninitialized data
  + MFSA 2013-94 Spoofing addressbar though SELECT element
  + MFSA 2013-93 Miscellaneous memory safety hazards (rv:25.0 / rv:24.1 / rv:17.0.10)

* Sun Oct 13 2013 Alexey Gladkov <legion@altlinux.ru> 24.0.1-alt1
- New version (24.0.1).
- Use internal mozldap.
- Fixed:
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
  + MFSA 2013-77 Improper state in HTML5 Tree Builder with templates
  + MFSA 2013-76 Miscellaneous memory safety hazards (rv:24.0 / rv:17.0.9)

* Tue Aug 13 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.8-alt1
- New version (17.0.8).
- Fixed:
  + MFSA 2013-75 Local Java applets may read contents of local file system
  + MFSA 2013-73 Same-origin bypass with web workers and XMLHttpRequest
  + MFSA 2013-72 Wrong principal used for validating URI for some Javascript components
  + MFSA 2013-71 Further Privilege escalation through Mozilla Updater
  + MFSA 2013-69 CRMF requests allow for code execution and XSS attacks
  + MFSA 2013-68 Document URI misrepresentation and masquerading
  + MFSA 2013-66 Buffer overflow in Mozilla Maintenance Service and Mozilla Updater
  + MFSA 2013-63 Miscellaneous memory safety hazards (rv:23.0 / rv:17.0.8)

* Sun Jun 30 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.7-alt1
- New version (17.0.7).
- Fixed:
  + MFSA 2013-59 XrayWrappers can be bypassed to run user defined methods in a privileged context
  + MFSA 2013-56 PreserveWrapper has inconsistent behavior
  + MFSA 2013-55 SVG filters can lead to information disclosure
  + MFSA 2013-54 Data in the body of XHR HEAD requests leads to CSRF attacks
  + MFSA 2013-53 Execution of unmapped memory through onreadystatechange event
  + MFSA 2013-51 Privileged content access and execution via XBL
  + MFSA 2013-50 Memory corruption found using Address Sanitizer
  + MFSA 2013-49 Miscellaneous memory safety hazards (rv:22.0 / rv:17.0.7)

* Wed Jun 05 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.6-alt1
- New version (17.0.6).
- Fixed:
  + MFSA 2013-48 Memory corruption found using Address Sanitizer
  + MFSA 2013-47 Uninitialized functions in DOMSVGZoomEvent
  + MFSA 2013-46 Use-after-free with video and onresize event
  + MFSA 2013-44 Local privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-42 Privileged access for content level constructor
  + MFSA 2013-41 Miscellaneous memory safety hazards (rv:21.0 / rv:17.0.6)

* Thu Apr 11 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.5-alt1
- New version (17.0.5).
- Enigmail (1.5.1).
- Fixed:
  + MFSA 2013-40 Out-of-bounds array read in CERT_DecodeCertPackage
  + MFSA 2013-38 Cross-site scripting (XSS) using timed history navigations
  + MFSA 2013-36 Bypass of SOW protections allows cloning of protected nodes
  + MFSA 2013-35 WebGL crash with Mesa graphics driver on Linux
  + MFSA 2013-34 Privilege escalation through Mozilla Updater
  + MFSA 2013-32 Privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-31 Out-of-bounds write in Cairo library
  + MFSA 2013-30 Miscellaneous memory safety hazards (rv:20.0 / rv:17.0.5)
  + MFSA 2013-29 Use-after-free in HTML Editor

* Fri Mar 01 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.3-alt1
- New version (17.0.3).
- Fixed:
  + MFSA 2013-28 Use-after-free, out of bounds read, and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-27 Phishing on HTTPS connection through malicious proxy
  + MFSA 2013-26 Use-after-free in nsImageLoadingContent
  + MFSA 2013-25 Privacy leak in JavaScript Workers
  + MFSA 2013-24 Web content bypass of COW and SOW security wrappers
  + MFSA 2013-21 Miscellaneous memory safety hazards (rv:19.0 / rv:17.0.3)

* Thu Jan 17 2013 Alexey Gladkov <legion@altlinux.ru> 17.0.2-alt1
- New version (17.0.2).
- Fixed:
  + MFSA 2013-20 Mis-issued TURKTRUST certificates
  + MFSA 2013-19 Use-after-free in Javascript Proxy objects
  + MFSA 2013-18 Use-after-free in Vibrate
  + MFSA 2013-17 Use-after-free in ListenerManager
  + MFSA 2013-16 Use-after-free in serializeToStream
  + MFSA 2013-15 Privilege escalation through plugin objects
  + MFSA 2013-14 Chrome Object Wrapper (COW) bypass through changing prototype
  + MFSA 2013-13 Memory corruption in XBL with XML bindings containing SVG
  + MFSA 2013-12 Buffer overflow in Javascript string concatenation
  + MFSA 2013-11 Address space layout leaked in XBL objects
  + MFSA 2013-10 Event manipulation in plugin handler to bypass same-origin policy
  + MFSA 2013-09 Compartment mismatch with quickstubs returned values
  + MFSA 2013-08 AutoWrapperChanger fails to keep objects alive during garbage collection
  + MFSA 2013-07 Crash due to handling of SSL on threads
  + MFSA 2013-05 Use-after-free when displaying table with many columns and column groups
  + MFSA 2013-04 URL spoofing in addressbar during page loads
  + MFSA 2013-03 Buffer Overflow in Canvas
  + MFSA 2013-02 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-01 Miscellaneous memory safety hazards (rv:18.0/ rv:10.0.12 / rv:17.0.2)

* Fri Nov 23 2012 Alexey Gladkov <legion@altlinux.ru> 17.0-alt1
- New version (17.0).
- Fixed:
  + MFSA 2012-106 Use-after-free, buffer overflow, and memory corruption issues found using Address Sanitizer
  + MFSA 2012-105 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2012-103 Frames can shadow top.location
  + MFSA 2012-101 Improper character decoding in HZ-GB-2312 charset
  + MFSA 2012-100 Improper security filtering for cross-origin wrappers
  + MFSA 2012-99 XrayWrappers exposes chrome-only properties when not in chrome compartment
  + MFSA 2012-97 XMLHttpRequest inherits incorrect principal within sandbox
  + MFSA 2012-96 Memory corruption in str_unescape
  + MFSA 2012-94 Crash when combining SVG text on path with CSS
  + MFSA 2012-93 evalInSanbox location context incorrectly applied
  + MFSA 2012-92 Buffer overflow while rendering GIF images
  + MFSA 2012-91 Miscellaneous memory safety hazards (rv:17.0/ rv:10.0.11)

* Thu Nov 01 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.2-alt1
- New version (16.0.2).
- Fixed:
  + MFSA 2012-90 Fixes for Location object issues
  + MFSA 2012-67 Installer will launch incorrect executable following new installation

* Tue Oct 23 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.1-alt1
- New version (16.0.1).
- Enigmail (1.4.5).
- Fixed:
  + MFSA 2012-89 defaultValue security checks not applied
  + MFSA 2012-88 Miscellaneous memory safety hazards (rv:16.0.1)
  + MFSA 2012-87 Use-after-free in the IME State Manager
  + MFSA 2012-86 Heap memory corruption issues found using Address Sanitizer
  + MFSA 2012-85 Use-after-free, buffer overflow, and out of bounds read issues found using Address Sanitizer
  + MFSA 2012-84 Spoofing and script injection through location.hash
  + MFSA 2012-83 Chrome Object Wrapper (COW) does not disallow acces to privileged functions or properties
  + MFSA 2012-82 top object and location property accessible by plugins
  + MFSA 2012-81 GetProperty function can bypass security checks
  + MFSA 2012-80 Crash with invalid cast when using instanceof operator
  + MFSA 2012-79 DOS and crash with full screen and history navigation
  + MFSA 2012-77 Some DOMWindowUtils methods bypass security checks
  + MFSA 2012-76 Continued access to initial origin after setting document.domain
  + MFSA 2012-75 select element persistance allows for attacks
  + MFSA 2012-74 Miscellaneous memory safety hazards (rv:16.0/ rv:10.0.8)

* Wed Aug 29 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt1
- New version (15.0).
- Fixed:
  + MFSA 2012-72 Web console eval capable of executing chrome-privileged code
  + MFSA 2012-70 Location object security checks bypassed by chrome code
  + MFSA 2012-68 DOMParser loads linked resources in extensions when parsing text/html
  + MFSA 2012-67 Installer will launch incorrect executable following new installation
  + MFSA 2012-65 Out-of-bounds read in format-number in XSLT
  + MFSA 2012-64 Graphite 2 memory corruption
  + MFSA 2012-63 SVG buffer overflow and use-after-free issues
  + MFSA 2012-62 WebGL use-after-free and memory corruption
  + MFSA 2012-61 Memory corruption with bitmap format images with negative height
  + MFSA 2012-59 Location object can be shadowed using Object.defineProperty
  + MFSA 2012-58 Use-after-free issues found using Address Sanitizer
  + MFSA 2012-57 Miscellaneous memory safety hazards (rv:15.0/ rv:10.0.7)

* Mon Jul 30 2012 Alexey Gladkov <legion@altlinux.ru> 14.0-alt1
- New version (14.0).
- Fixed:
  + MFSA 2012-56 Code execution through javascript: URLs
  + MFSA 2012-53 Content Security Policy 1.0 implementation errors cause data leakage
  + MFSA 2012-52 JSDependentString::undepend string conversion results in memory corruption
  + MFSA 2012-51 X-Frame-Options header ignored when duplicated
  + MFSA 2012-50 Out of bounds read in QCMS
  + MFSA 2012-49 Same-compartment Security Wrappers can be bypassed
  + MFSA 2012-48 use-after-free in nsGlobalWindow::PageHidden
  + MFSA 2012-47 Improper filtering of javascript in HTML feed-view
  + MFSA 2012-45 Spoofing issue with location
  + MFSA 2012-44 Gecko memory corruption
  + MFSA 2012-42 Miscellaneous memory safety hazards (rv:14.0/ rv:10.0.6)

* Thu Jul 05 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New version (13.0.1).
- Fixed:
  + MFSA 2012-40 Buffer overflow and use-after-free issues found using Address Sanitizer
  + MFSA 2012-39 NSS parsing errors with zero length items
  + MFSA 2012-38 Use-after-free while replacing/inserting a node in a document
  + MFSA 2012-37 Information disclosure though Windows file shares and shortcut files
  + MFSA 2012-36 Content Security Policy inline-script bypass
  + MFSA 2012-35 Privilege escalation through Mozilla Updater and Windows Updater Service
  + MFSA 2012-34 Miscellaneous memory safety hazards

* Wed May 09 2012 Alexey Gladkov <legion@altlinux.ru> 12.0.1-alt1
- New version (12.0.1).
- Use internal libcairo.
- Fixed:
  + MFSA 2012-33 Potential site identity spoofing when loading RSS and Atom feeds
  + MFSA 2012-32 HTTP Redirections and remote content can be read by javascript errors
  + MFSA 2012-31 Off-by-one error in OpenType Sanitizer
  + MFSA 2012-30 Crash with WebGL content using textImage2D
  + MFSA 2012-29 Potential XSS through ISO-2022-KR/ISO-2022-CN decoding issues
  + MFSA 2012-28 Ambiguous IPv6 in Origin headers may bypass webserver access restrictions
  + MFSA 2012-27 Page load short-circuit can lead to XSS
  + MFSA 2012-26 WebGL.drawElements may read illegal video memory due to FindMaxUshortElement error
  + MFSA 2012-25 Potential memory corruption during font rendering using cairo-dwrite
  + MFSA 2012-24 Potential XSS via multibyte content processing errors
  + MFSA 2012-23 Invalid frees causes heap corruption in gfxImageSurface
  + MFSA 2012-22 use-after-free in IDBKeyRange
  + MFSA 2012-20 Miscellaneous memory safety hazards (rv:12.0/ rv:10.0.4)

* Fri Apr 20 2012 Alexey Gladkov <legion@altlinux.ru> 11.0.1-alt1
- New version (11.0.1).
- Fixed:
  + MFSA 2012-19 Miscellaneous memory safety hazards (rv:11.0/ rv:10.0.3 / rv:1.9.2.28)
  + MFSA 2012-18 window.fullScreen writeable by untrusted content
  + MFSA 2012-17 Crash when accessing keyframe cssText after dynamic modification
  + MFSA 2012-16 Escalation of privilege with Javascript: URL as home page
  + MFSA 2012-15 XSS with multiple Content Security Policy headers
  + MFSA 2012-14 SVG issues found with Address Sanitizer
  + MFSA 2012-13 XSS with Drag and Drop and Javascript: URL

* Thu Feb 23 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New version (10.0.2).
- Fixed:
  + MFSA 2012-11 libpng integer overflow
  + MFSA 2012-10 use after free in nsXBLDocumentInfo::ReadPrototypeBindings
  + MFSA 2012-08 Crash with malformed embedded XSLT stylesheets
  + MFSA 2012-07 Potential Memory Corruption When Decoding Ogg Vorbis files
  + MFSA 2012-06 Uninitialized memory appended when encoding icon images may cause information disclosure
  + MFSA 2012-05 Frame scripts calling into untrusted objects bypass security checks
  + MFSA 2012-04 Child nodes from nsDOMAttribute still accessible after removal of nodes
  + MFSA 2012-03 <iframe> element exposed across domains via name attribute
  + MFSA 2012-01 Miscellaneous memory safety hazards (rv:10.0/ rv:1.9.2.26)
  + MFSA 2011-58 Crash scaling <video> to extreme sizes
  + MFSA 2011-57 Crash when plugin removes itself on Mac OS X
  + MFSA 2011-56 Key detection without JavaScript via SVG animation
  + MFSA 2011-55 nsSVGValue out-of-bounds access
  + MFSA 2011-54 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-53 Miscellaneous memory safety hazards (rv:9.0)

* Tue Jan 31 2012 Alexey Gladkov <legion@altlinux.ru> 8.0-alt2
- Rebuilt with libvpx.

* Tue Nov 15 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New version (8.0).
- Fixed:
  + MFSA 2011-52 Code execution via NoWaiverWrapper
  + MFSA 2011-51 Cross-origin image theft on Mac with integrated Intel GPU
  + MFSA 2011-50 Cross-origin data theft using canvas and Windows D2D
  + MFSA 2011-49 Memory corruption while profiling using Firebug
  + MFSA 2011-48 Miscellaneous memory safety hazards (rv:8.0)
  + MFSA 2011-47 Potential XSS against sites using Shift-JIS
  + MFSA 2011-44 Use after free reading OGG headers
  + MFSA 2011-42 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-40 Code installation through holding down Enter
  + MFSA 2011-39 Defense against multiple Location headers due to CRLF Injection
  + MFSA 2011-36 Miscellaneous memory safety hazards (rv:7.0 / rv:1.9.2.23)

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.1-alt1
- New version (6.0.1).
- Fixed:
  + MFSA 2011-34 Protection against fraudulent DigiNotar certificates

* Thu Aug 25 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New version (6.0).
- Add GIO support (ALT#11503).
- Fixed:
  + MFSA 2011-31 Security issues addressed in Thunderbird 6

* Thu Jul 21 2011 Alexey Gladkov <legion@altlinux.ru> 5.0-alt1
- New version (5.0).
- Remove gnome-support subpackage.

* Sat Apr 09 2011 Alexey Gladkov <legion@altlinux.ru> 3.1.9-alt1.20110409
- New snapshot (3.1.9 20110409).
- Use xdg-open (ALT#25403).

* Tue Mar 08 2011 Alexey Gladkov <legion@altlinux.ru> 3.1.9-alt1.20110308
- New version (3.1.9 20110308).
- Fixed:
  + MFSA 2011-09 Crash caused by corrupted JPEG image
  + MFSA 2011-08 ParanoidFragmentSink allows javascript: URLs in chrome documents
  + MFSA 2011-01 Miscellaneous memory safety hazards (rv:1.9.2.14/ 1.9.1.17)

* Sun Jan 23 2011 Alexey Gladkov <legion@altlinux.ru> 3.1.7-alt1.20110123
- New snapshot (3.1.7 20110123)
- Fix update request (ALT#23867)

* Sun Aug 15 2010 Alexey Gladkov <legion@altlinux.ru> 3.1.2-alt1.20100815
- New snapshot (3.1.2 20100810)
- Fixed:
  + MFSA 2010-47 Cross-origin data leakage from script filename in error messages
  + MFSA 2010-46 Cross-domain data theft using CSS
  + MFSA 2010-44 Characters mapped to U+FFFD in 8 bit encodings cause subsequent character to vanish
  + MFSA 2010-43 Same-origin bypass using canvas context
  + MFSA 2010-42 Cross-origin data disclosure via Web Workers and importScripts
  + MFSA 2010-41 Remote code execution using malformed PNG image
  + MFSA 2010-40 nsTreeSelection dangling pointer remote code execution vulnerability
  + MFSA 2010-39 nsCSSValue::Array index integer overflow
  + MFSA 2010-38 Arbitrary code execution using SJOW and fast native function
  + MFSA 2010-34 Miscellaneous memory safety hazards (rv:1.9.2.7/ 1.9.1.11)

* Tue Jun 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.1.1-alt1.20100626
- New snapshot

* Mon Apr 05 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.4-alt1.20100404
- New snapshot (3.0.4 20100404)
- Add gnome support.
- Fixed:
  + MFSA 2010-24 XMLDocument::load() doesn't check nsIContentPolicy
  + MFSA 2010-22 Update NSS to support TLS renegotiation indication
  + MFSA 2010-18 Dangling pointer vulnerability in nsTreeContentView
  + MFSA 2010-17 Remote code execution with use-after-free in nsTreeSelection
  + MFSA 2010-16 Crashes with evidence of memory corruption (rv:1.9.2.2/ 1.9.1.9/ 1.9.0.19)

* Thu Jan 28 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1.20100128
- New snapshot (3.0.1 20100128)

* Thu Nov 26 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20091126
- New snapshot (3.0 20091126)

* Sun Oct 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20091018
- New snapshot (3.0 20091018)

* Sun Oct 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20091010
- New snapshot (3.0 20091010)

* Tue Sep 29 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090929
- New snapshot (3.0 20090929)

* Tue Sep 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090917
- New snapshot (3.0 20090917)

* Mon Aug 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090817
- New snapshot (3.0 20090817)

* Wed Jul 29 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090729
- New snapshot (3.0 20090729)

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090601
- New snapshot (3.0 20090601)

* Sun Apr 26 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090424
- New snapshot (3.0 20090424)

* Thu Mar 12 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090312
- New snapshot (3.0 20090312)
- Use system mozsqlite3 (sqlite3 unsupported)

* Mon Nov 24 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.18-alt1
- New version (2.0.0.18)
- Fixed:
    + MFSA 2008-59 Script access to .documentURI and .textContent in mail
    + MFSA 2008-58 Parsing error in E4X default namespace
    + MFSA 2008-56 nsXMLHttpRequest::NotifyEventListeners() same-origin violation
    + MFSA 2008-55 Crash and remote code execution in nsFrameManager
    + MFSA 2008-52 Crashes with evidence of memory corruption (rv:1.9.0.4/1.8.1.18)
    + MFSA 2008-50 Crash and remote code execution via __proto__ tampering
    + MFSA 2008-48 Image stealing via canvas and HTTP redirect

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.17-alt1
- New version (2.0.0.17)
- Fixed:
    + MFSA 2008-46 Heap overflow when canceling newsgroup message
    + MFSA 2008-44 resource: traversal vulnerabilities
    + MFSA 2008-43 BOM characters stripped from JavaScript before execution
    + MFSA 2008-42 Crashes with evidence of memory corruption (rv:1.9.0.2/1.8.1.17)
    + MFSA 2008-41 Privilege escalation via XPCnativeWrapper pollution
    + MFSA 2008-38 nsXMLDocument::OnChannelRedirect() same-origin violation
    + MFSA 2008-37 UTF-8 URL stack buffer overflow
    + MFSA 2008-34 Remote code execution by overflowing CSS reference counter
    + MFSA 2008-33 Crash and remote code execution in block reflow
    + MFSA 2008-31 Peer-trusted certs can use alt names to spoof
    + MFSA 2008-29 Faulty .properties file results in uninitialized memory being used
    + MFSA 2008-26 Buffer length checks in MIME processing
    + MFSA 2008-25 Arbitrary code execution in mozIJSSubScriptLoader.loadSubScript()
    + MFSA 2008-24 Chrome script loading from fastload file
    + MFSA 2008-21 Crashes with evidence of memory corruption (rv:1.8.1.15)

* Thu Jul 17 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.14-alt2
- Bugfix build.
- Dont use LD_LIBRARY_PATH in startup scripts.

* Sun May 11 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.14-alt1
- New version (2.0.0.14)
- Fixed:
    + MFSA 2008-15 Crashes with evidence of memory corruption (rv:1.8.1.13)
    + MFSA 2008-14 JavaScript privilege escalation and arbitrary code execution

* Sun Mar 02 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.12-alt1
- New version (2.0.0.12)
- Fixed:
    + MFSA 2008-12 Heap buffer overflow in external MIME bodies
    + MFSA 2008-05 Directory traversal via chrome: URI
    + MFSA 2008-03 Privilege escalation, XSS, Remote Code Execution
    + MFSA 2008-01 Crashes with evidence of memory corruption (rv:1.8.1.12)
    + MFSA 2007-36 URIs with invalid %-encoding mishandled by Windows
    + MFSA 2007-29 Crashes with evidence of memory corruption (rv:1.8.1.8)
    + MFSA 2007-27 Unescaped URIs passed to external programs
    + MFSA 2007-26 Privilege escalation through chrome-loaded about:blank windows

* Thu Aug 02 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.6-alt1
- New version (2.0.0.6)
- Fixed:
    + MFSA 2007-27 Unescaped URIs passed to external programs
    + MFSA 2007-26 Privilege escalation through chrome-loaded about:blank windows

* Fri Jul 20 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.5-alt1
- New version (2.0.0.5)
- Fixed:
    + MFSA 2007-23 Remote code execution by launching Firefox from Internet Explorer
    + MFSA 2007-18 Crashes with evidence of memory corruption

* Fri Jun 29 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.4-alt1
- New version (2.0.0.4)
- Fix normal icons.
- Fixed:
    + MFSA 2007-15 Security Vulnerability in APOP Authentication
    + MFSA 2007-12 Crashes with evidence of memory corruption (rv:1.8.0.12/1.8.1.4)

* Sun Apr 22 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.0-alt1
- New version (2.0.0.0)
- Many bugfixes (see http://weblogs.mozillazine.org/rumblingedge/archives/2007/03/tb_2.html).
- Add RSS files (again).

* Tue Feb 27 2007 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1.b2
- New version (2.0 Beta 2)

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.8-alt1
- New version (1.5.0.8)
- Remove version specific paths.
- Add %%pre script.
- Improvements to product stability.
- Fixed:
    + MFSA 2006-67 Running Script can be recompiled
    + MFSA 2006-66 RSA signature forgery (variant)
    + MFSA 2006-65 Crashes with evidence of memory corruption (rv:1.8.0.8)
    + MFSA 2006-64 Crashes with evidence of memory corruption (rv:1.8.0.7)
    + MFSA 2006-63 JavaScript execution in mail via XBL
    + MFSA 2006-60 RSA Signature Forgery
    + MFSA 2006-59 Concurrency-related vulnerability
    + MFSA 2006-58 Auto-Update compromise through DNS and SSL spoofing
    + MFSA 2006-57 JavaScript Regular Expression Heap Corruption

* Thu Aug 17 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.5-alt1
- New version (1.5.0.5)
- Build with MozLDAP support.
- Improvements to product stability.
- Fixed:
    + MFSA 2006-55 Crashes with evidence of memory corruption (rv:1.8.0.5)
    + MFSA 2006-54 XSS with XPCNativeWrapper(window).Function(...)
    + MFSA 2006-53 UniversalBrowserRead privilege escalation
    + MFSA 2006-52 PAC privilege escalation using Function.prototype.call
    + MFSA 2006-51 Privilege escalation using named-functions and redefined "new Object()"
    + MFSA 2006-50 JavaScript engine vulnerabilities
    + MFSA 2006-49 Heap buffer overwrite on malformed VCard
    + MFSA 2006-48 JavaScript new Function race condition
    + MFSA 2006-47 Native DOM methods can be hijacked across domains
    + MFSA 2006-46 Memory corruption with simultaneous events
    + MFSA 2006-44 Code execution through deleted frame reference

* Tue May 02 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.2-alt1
- New bugfix version.
- Improvements to product stability.
- Fixed:
    + MFSA 2006-28 Security check of js_ValueToFunctionObject() can be circumvented;
    + MFSA 2006-27 Table Rebuilding Code Execution Vulnerability;
    + MFSA 2006-26 Mail Multiple Information Disclosure;
    + MFSA 2006-25 Privilege escalation through Print Preview;
    + MFSA 2006-24 Privilege escalation using crypto.generateCRMFRequest;
    + MFSA 2006-22 CSS Letter-Spacing Heap Overflow Vulnerability;
    + MFSA 2006-21 JavaScript execution in mail when forwarding in-line;
    + MFSA 2006-20 Crashes with evidence of memory corruption (rv:1.8.0.2);
    + MFSA 2006-08 "AnyName" entrainment and access control hazard;
    + MFSA 2006-07 Read beyond buffer while parsing XML;
    + MFSA 2006-06 Integer overflows in E4X, SVG and Canvas;
    + MFSA 2006-05 Localstore.rdf XML injection through XULDocument.persist();
    + MFSA 2006-04 Memory corruption via QueryInterface on Location, Navigator objects;
    + MFSA 2006-02 Changing postion:relative to static corrupts memory;
    + MFSA 2006-01 JavaScript garbage-collection hazards.

* Fri Mar 24 2006 Alexey Gladkov <legion@altlinux.ru> 1.5-alt2
- bugfix build.
- share extension directory fix.

* Tue Feb 21 2006 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- new version 1.5
- build with rpm-build-thunderbird (external build macros)
- Build with system NSS and NSPR.
- Buildrequires updated for xorg-7.0 
- directory /usr/share/thunderbird-@version@/extensions was added to extensions search path .
  * this location is controled by the option extensions.dir.extensions .
- Startup script rewritten. Now it is single script.
  * command line shortcut added: altmail:MAILLIST 
    (example: "altmail:devel" -> mailto:devel@list.altlinux.org).
- LDAP support disabled.
- firsttime script removed
- NoX patch removed

* Wed Aug 24 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt2
- packaging bugfix.
- rpm mascros bugfix.
- The script is added for switching language after installation/removal 
  of a localization package.
- Bug: #6204, #6254 fixed.

* Mon Aug 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1
- new version.
- firsttime script added.

* Wed May 11 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- new version;
- RSS missing files add;

* Tue Feb 01 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- update patch thunderbird-1.0-20050201-alt-nox.patch 
  * uninstall-global-theme command-line option was added;
  * update-register command-line option was added;
- thunderbird-1.0-alt-rpm-scripts.tar.bz2 bugfix;

* Thu Jan 27 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- fix crush when comiling with gcc3.4 .

* Wed Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- Rebuilt with libstdc++.so.6.

* Thu Jan 06 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- new version;
- new extension load scheme;
- uninstall-global-extension option fixed;
- add RPATH=%%_libdir/%%fullname to the all binares;
- rpm macros was updated;
- %%post_ldconfig and %%postun_ldconfig was removed.
- icons updated (thx shrek@);

* Fri Jul 16 2004 Alexey Morozov <morozov@altlinux.org> 0.7.2-alt2
- new version (0.7.2)
- rpm macros file is splitted to base and devel parts
- Russian spec translation
- A patch to handle external URLs w/ url_handler
- Requirements cleanup

* Fri May 07 2004 Alexey Gladkov <legion@altlinux.ru> 0.6-alt1
- New version;
- Splash screen added;
- Default userContent.css added;
- Offline extension added by default;
- Confilct between mozilla-like devel packages was removed.

* Wed Feb 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.5-alt1
- New version.

* Tue Jan 13 2004 Alexey Gladkov <legion@altlinux.ru> 0.4-alt4
- Spec changes.

* Fri Dec 26 2003 Alexey Gladkov <legion@altlinux.ru> 0.4-alt3
- first build for ALT Linux.
- rpm macro added.
- new scheme loading extensions added (thx force@)
- Spec modifications.
