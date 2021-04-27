%define pulseaudio_version 14.2

Name:     pulseaudio-module-xrdp
Version:  0.5
Release:  alt0.p1.1

Summary:  xrdp sink / source pulseaudio modules
License:  Apache-2.0
Group:    Other
Url:      https://github.com/neutrinolabs/pulseaudio-module-xrdp

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Source1:  pulseaudio-src.tar

BuildRequires: libpulseaudio-devel

BuildRequires: gcc-c++
BuildRequires: intltool jackit-devel libalsa-devel libasyncns-devel
BuildRequires: libavahi-devel libbluez-devel
BuildRequires: libcap-devel libdbus-devel libgdbm-devel libudev-devel
BuildRequires: liblirc-devel libltdl7-devel libsoxr-devel
BuildRequires: libsndfile-devel libspeex-devel libspeexdsp-devel libwebrtc-devel
BuildRequires: libSM-devel libX11-devel libXtst-devel libxcbutil-devel
BuildRequires: libGConf-devel
BuildRequires: libfftw3-devel libsbc-devel liborc-devel orc xmltoman
BuildRequires: libssl-devel libsystemd-devel

%description
xrdp implements Audio Output redirection using PulseAudio, which is a
sound system used on POSIX operating systems.

%prep
%setup
tar xf %SOURCE1

%build
%undefine _configure_gettext
# Configure Pulseaudio like pulseaudio.spec
pushd pulseaudio-src
echo "%pulseaudio_version" > .tarball-version
touch config.rpath
%autoreconf
%configure \
    --localstatedir=/var \
    --with-access-group=audio \
    --enable-per-user-esound-socket \
    --enable-adrian-aec \
    --disable-bluez4 \
    --disable-static \
    #
popd
# Build pulseaudio-module-xrdp
%autoreconf
%configure PULSE_DIR=`pwd`/pulseaudio-src
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/pulse-*/modules/*.la

%check
%make_build check

%files
%doc README.md
%_libdir/pulse-*/modules/*.so

%changelog
* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.5-alt0.p1.1
- Backport new version to p9 branch.

* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- New version.
- Rebuild woth Pulseaudio 14.2.

* Wed Mar 18 2020 Andrey Cherepanov <cas@altlinux.org> 0.4-alt0.p9.1
- Build to p9 branch.

* Mon Oct 28 2019 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- New version.

* Mon Jun 17 2019 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
