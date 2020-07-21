# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: guitarix
Version: 0.40.0
Release: alt1
Summary: Mono amplifier to JACK
Group: Sound
License: GPL-2.0-or-later
Url: https://sourceforge.net/projects/guitarix
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Source1: %name.appdata.xml

# Fix backported from upstream commit 2609ca14
Patch0: %name-format-string.patch

BuildRequires: gcc-c++
BuildRequires: faust-devel
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(avahi-gobject)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: libfftw3-devel
BuildRequires: gperf
BuildRequires: intltool
BuildRequires: boost-devel
BuildRequires: eigen3
BuildRequires: ladspa_sdk
BuildRequires: python3
BuildRequires: sassc
BuildRequires: waf
BuildRequires: zita-convolver-devel
BuildRequires: zita-resampler-devel
BuildRequires: pkgconfig(glibmm-2.4)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(gtk+-3.0)
Requires: jack_capture
Requires: jconvolver
Requires: ladspa-%name-plugins = %EVR
Requires: qjackctl
Requires: vorbis-tools
#Requires: google-roboto-condensed-fonts

Obsoletes: libgxw < 0.40
Obsoletes: libgxwmm < 0.40

%description
Guitarix is a simple mono amplifier to be used in a 'JACKified' environment,
i.e. a system using the JACK Audio Connection Kit, a professionally-capable
audio/MIDI server and master transport control.

Guitarix provides one JACK input port and two JACK output ports. It is designed
to produce nice trash/metal/rock/blues guitar sounds. Controls for bass, treble,
gain, compressor, preamp, balance, distortion, freeverb, crybaby (wah) and echo
are available. A fixed resonator is used when distortion is disabled. To modify
the sound 'pressure', you can use the feedback and feedforward sliders.

Guitarix includes an experimental tuner and a JACK MIDI output port with 3
channels. They are fed by a mix from a pitch tracker and a beat detector. You
can pitch the octave (2 octaves up or down), choose the MIDI channel, the MIDI
program, the velocity and the sensitivity, which translates into how fast the
note will read after the beat detector emits a signal. Values for the beat
detector can be set for all channels.

%package -n ladspa-%name-plugins
Summary: Collection of Ladspa plug-ins
Group: Sound
# ladspa/distortion.cpp and ladspa/guitarix-ladspa.cpp are BSD
# The rest of ladspa/* is GPLv+
License: GPL-or-later and BSD
Requires: ladspa_sdk

%description -n ladspa-%name-plugins
This package contains the crybaby, distortion, echo, impulseresponse, monoamp,
and monocompressor ladspa plug-ins that come together with guitarix, but can
also be used by any other ladspa host.

%package -n lv2-%name-plugins
Summary: Collection of LV2 guitarix plug-ins
Group: Sound
# ladspa/distortion.cpp and ladspa/guitarix-ladspa.cpp are BSD
# The rest of ladspa/* is GPLv+
License: GPL-2.0-or-later
Requires: lv2
Requires: %name = %EVR

%description -n lv2-%name-plugins
This package contains the guitarix amp plug-ins that come together with
guitarix, but can also be used by any other ladspa host.

%prep
%setup
%patch0 -p1

# fix shebang
find . -type f -print0 |
  xargs -0 sed -i 's,/usr/bin/env python,%_bindir/python3,'

#fix PATH include to Eigen
for i in `grep -r '<Eigen' * | cut -d ':' -f1`; do
    sed -i 's/<Eigen/<eigen3\/Eigen/' -i $i
done

# The build system does not use these bundled libraries by default. But
# just to make sure:
rm -fr src/zita-convolver src/zita-resampler
%__subst 's|-O3||' wscript

%build
./waf -vv configure --prefix=%prefix --libdir=%_libdir \
      --cxxflags="-std=c++0x -fomit-frame-pointer \
      -ffinite-math-only -fno-math-errno -fno-signed-zeros -fstrength-reduce \
%ifarch %ix86 x86_64
      -msse \
%endif
%ifarch %ix86
      -mfxsr \
%endif
      %optflags" \
%ifarch %arm
      --disable-sse \
%endif
      --shared-lib \
      --ladspa --ladspadir=%_libdir/ladspa \
      --lv2dir=%_libdir/lv2 \
      --cxxflags-release="%optflags -DNDEBUG"

./waf -vv build %{?_smp_mflags}

%install
./waf -vv install --destdir="%buildroot" --libdir="%_libdir"

desktop-file-install \
    --add-category="X-DigitalProcessing" \
    --dir=%buildroot%_desktopdir \
        %buildroot/%_desktopdir/%name.desktop

#fix links and remove unwanted devel files
chmod 755 %buildroot%_libdir/libgxw*.so.0.1
rm -rf %buildroot%_libdir/libgxw*.so

# install appdata file
install -d -m755 %buildroot%_datadir/metainfo
install -p -m644 %SOURCE1 %buildroot%_datadir/metainfo

%find_lang %name

%files -f %name.lang
%doc changelog COPYING README
%_bindir/%name
%_pixmapsdir/*
%_desktopdir/%name.desktop
%_datadir/gx_head/
%_libdir/libgx*.so.0*
%_datadir/metainfo/%name.appdata.xml

%files -n ladspa-%name-plugins
%_libdir/ladspa/*.so
%_datadir/ladspa

%files -n lv2-%name-plugins
%_libdir/lv2/*

%changelog
* Wed Jun 24 2020 Anton Midyukov <antohami@altlinux.org> 0.40.0-alt1
- new version 0.40.0
- switch to Gtk+3
- add a metainfo file
- disable build devel packages
- cleanup spec
- first build on armh

* Mon Apr 20 2020 Anton Midyukov <antohami@altlinux.org> 0.39.0-alt1
- new version 0.39.0

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 0.38.1-alt1
- new version 0.38.1

* Tue Apr 23 2019 Anton Midyukov <antohami@altlinux.org> 0.37.3-alt2
- Add russian translations (Thanks Valeriy Shtobbe, Olesya Gerasimenko)

* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 0.37.3-alt1
- new version 0.37.3

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.36.1-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Apr 08 2018 Anton Midyukov <antohami@altlinux.org> 0.36.1-alt1
- new version 0.36.1

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.35.5-alt1.1
- NMU: rebuild with new lv2

* Tue Aug 08 2017 Anton Midyukov <antohami@altlinux.org> 0.35.5-alt1
- new version (0.35.5) with rpmgs script

* Sun May 21 2017 Anton Midyukov <antohami@altlinux.org> 0.35.3-alt1
- Initial build for ALT Linux Sisyphus
