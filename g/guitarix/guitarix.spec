# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global altname gx_head
%global altname2 guitarix2

Name: guitarix
Version: 0.38.1
Release: alt1
Summary: Mono amplifier to JACK
Group: Sound
License: GPLv2+
Url: https://sourceforge.net/projects/guitarix
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
# Source-url: https://sourceforge.net/projects/%name/files/%name/%altname2-%version.tar.xz
Source1: ru.po

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: faust-devel
BuildRequires: libfftw3-devel
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: libgtkmm2-devel
BuildRequires: pkgconfig(jack)
BuildRequires: ladspa_sdk
BuildRequires: libsigc++2-devel
BuildRequires: libsndfile-devel
BuildRequires: zita-convolver-devel >= 3.0.2
BuildRequires: zita-resampler-devel >= 0.1.1-3
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: boost-program_options-devel
BuildRequires: liblrdf-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: gperf
BuildRequires: libavahi-gobject-devel
BuildRequires: eigen3
BuildRequires: libcurl-devel
Requires: jack_capture
Requires: jconvolver
Requires: ladspa-%name-plugins = %EVR
Requires: qjackctl
Requires: vorbis-tools
#Requires: google-roboto-condensed-fonts

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

%package -n libgxw
Summary: Guitarix GTK library
Group: Development/Other
License: GPLv2+

%description -n libgxw
This package contains the Guitarix GTK widget library

%package -n libgxwmm
Summary: Guitarix GTK C++ library
Group: Development/Other
License: GPLv2+

%description -n libgxwmm
This package contains the Guitarix GTK C++ widget library

%package -n libgxw-devel
Summary: Development files for libgxw
Group: Development/Other
License: GPLv2+
Requires: libgxw = %EVR

%description -n libgxw-devel
This package contains files required to use the libgxw C Guitarix
widget library

%package -n libgxwmm-devel
Summary: Development files for libgxwmm
Group: Development/Other
License: GPLv2+
Requires: libgxwmm = %EVR

%description -n libgxwmm-devel
This package contains files required to use the libgxwmm C++ Guitarix widget
library

%package -n gxw-glade
Summary: Guitarix GTK library glade support
Group: Development/Other
License: GPLv2+
Requires: glade
Requires: libgxw-devel = %EVR

%description -n gxw-glade
This package contains support for using the Guitarix GTK widget library
with glade

%package -n ladspa-%name-plugins
Summary: Collection of Ladspa plug-ins
Group: Sound
# ladspa/distortion.cpp and ladspa/guitarix-ladspa.cpp are BSD
# The rest of ladspa/* is GPLv+
License: GPL+ and BSD
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
License: GPLv2+
Requires: lv2
Requires: %name = %EVR

%description -n lv2-%name-plugins
This package contains the guitarix amp plug-ins that come together with
guitarix, but can also be used by any other ladspa host.

%prep
%setup
cp %SOURCE1 po/

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
      %optflags" \
      --shared-lib --lib-dev \
      --ladspa --ladspadir=%_libdir/ladspa --lv2dir=%_libdir/lv2 \
      --glade-support --glade-catalog-dir=%_datadir/glade/catalogs \
      --glade-modules-dir=%_libdir/glade/modules
./waf -vv build %{?_smp_mflags}

%install
./waf -vv install --destdir="%buildroot" --libdir="%_libdir"

desktop-file-install \
    --add-category="X-DigitalProcessing" \
    --dir=%buildroot%_desktopdir \
        %buildroot/%_desktopdir/%name.desktop
rm -rf %buildroot%_libdir/libgxw*.so
ln -s %_libdir/libgxwmm.so.0.1 %buildroot%_libdir/libgxwmm.so
ln -s %_libdir/libgxw.so.0.1 %buildroot%_libdir/libgxw.so

%find_lang %name

%files -f %name.lang
%doc changelog COPYING README
%_bindir/%name
%_datadir/%altname/
%_pixmapsdir/*
%_desktopdir/%name.desktop

%files -n libgxw
%_libdir/libgxw.so.*

%files -n libgxwmm
%_libdir/libgxwmm.so.*

%files -n libgxw-devel
%_libdir/libgxw.so
%_includedir/gxw
%_includedir/gxw.h
%_pkgconfigdir/gxw.pc

%files -n libgxwmm-devel
%_libdir/libgxwmm.so
%_includedir/gxwmm
%_includedir/gxwmm.h
%_pkgconfigdir/gxwmm.pc

%files -n gxw-glade
%_libdir/glade/modules/libgladegx.so
%_datadir/%name/icons
%_datadir/glade/catalogs/*

%files -n ladspa-%name-plugins
%_libdir/ladspa/*.so
%_datadir/ladspa

%files -n lv2-%name-plugins
%_libdir/lv2/*

%changelog
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
