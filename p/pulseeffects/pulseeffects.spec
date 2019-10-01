%define gst_api_ver 1.0
%define xdg_name com.github.wwmm.pulseeffects

Name: pulseeffects
Version: 4.6.8
Release: alt1

Summary: Audio effects for Pulseaudio applications
License: GPLv3
Group: Sound
Url: https://github.com/wwmm/pulseeffects

Source: %url/archive/v%version/%name-%version.tar.gz

%define gst_ver 1.12.5
%define glibmm_ver 2.56
%define gtk_ver 3.20
%define calf_ver 0.90.1
%define lsp_ver 1.1.7

Requires: pulseaudio-daemon dconf
Requires: gst-plugins-good%gst_api_ver >= %gst_ver
Requires: gst-plugins-bad%gst_api_ver >= %gst_ver
Requires: ladspa-rubberband
Requires: ladspa-zam-plugins
Requires: calf-plugins >= %calf_ver
Requires: lv2-mda-plugins
%ifarch %ix86 x86_64
Requires: lv2-lsp-plugins >= %lsp_ver
%endif

BuildRequires(pre): meson
BuildRequires: yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: gcc-c++ boost-filesystem-devel boost-asio-devel
BuildRequires: libglibmm-devel >= %glibmm_ver libgtkmm3-devel >= %gtk_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel
BuildRequires: libpulseaudio-devel libsndfile-devel libsamplerate-devel libfftw3-devel
BuildRequires: pkgconfig(gstreamer-webrtc-1.0)
BuildRequires: libbs2b-devel
BuildRequires: liblilv-devel
BuildRequires: zita-convolver-devel
BuildRequires: libebur128-devel
BuildRequires: libdbus-devel

%description
PulseEffects is a limiter, compressor, reverberation, stereo equalizer and auto volume
effects for Pulseaudio applications.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/gstreamer-%gst_api_ver/libgstpeconvolver.so
%_libdir/gstreamer-%gst_api_ver/libgstpecrystalizer.so
%_libdir/gstreamer-%gst_api_ver/libgstpeautogain.so
%_libdir/gstreamer-%gst_api_ver/libgstpeadapter.so
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.*gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* CHANGELOG.*

%changelog
* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.8-alt1
- 4.6.8

* Tue Aug 06 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.6-alt1
- 4.6.6

* Mon Jun 24 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.5-alt1
- 4.6.5

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.4-alt1
- 4.6.4

* Mon Jun 03 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.3-alt1
- 4.6.3

* Fri May 31 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.2-alt1
- 4.6.2

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.1-alt1
- 4.6.1

* Tue Apr 30 2019 Yuri N. Sedunov <aris@altlinux.org> 4.6.0-alt1
- 4.6.0

* Mon Apr 15 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.9-alt1
- 4.5.9

* Wed Mar 20 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.7-alt1
- 4.5.7

* Thu Mar 14 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.6-alt1
- 4.5.6

* Thu Mar 07 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.5-alt1
- 4.5.5

* Mon Mar 04 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.4-alt1
- 4.5.4

* Fri Mar 01 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.3-alt1
- 4.5.3

* Tue Feb 26 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.2-alt1
- 4.5.2

* Sun Feb 24 2019 Yuri N. Sedunov <aris@altlinux.org> 4.5.1-alt1
- 4.5.1

* Sat Jan 12 2019 Yuri N. Sedunov <aris@altlinux.org> 4.4.6-alt1
- 4.4.6

* Fri Jan 04 2019 Yuri N. Sedunov <aris@altlinux.org> 4.4.5-alt1
- 4.4.5

* Tue Jan 01 2019 Yuri N. Sedunov <aris@altlinux.org> 4.4.4-alt1
- 4.4.4

* Tue Dec 04 2018 Yuri N. Sedunov <aris@altlinux.org> 4.4.1-alt1
- 4.4.1

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Fri Oct 26 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.9-alt1
- 4.3.9

* Wed Oct 17 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.8-alt1
- 4.3.8

* Thu Sep 27 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.7-alt1
- 4.3.7

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.5-alt1
- 4.3.5

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.4-alt1
- 4.3.4

* Wed Aug 15 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.8-alt1
- 4.2.8

* Sun Aug 12 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.6-alt1
- 4.2.6

* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.5-alt1
- 4.2.5

* Tue Jul 31 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.3-alt1
- 4.2.3

* Sun Jul 29 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.7-alt1
- 4.1.7

* Sat Jul 14 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.5-alt1
- 4.1.5

* Fri Jul 06 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.3-alt1
- 4.1.3

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.2-alt1
- 4.1.2

* Thu Jun 28 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.1-alt1
- 4.1.1

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.7-alt1
- 4.0.7

* Sun Jun 17 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.6-alt1
- 4.0.6

* Sat Jun 16 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.5-alt1
- 4.0.5

* Wed Jun 13 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.4-alt1
- 4.0.4

* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt2
- updated dependencies

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0 (ported to C++, Boost, GTKmm3)

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Sat Apr 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.1.7-alt1
- 3.1.7

* Sun Nov 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Sun Nov 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Sat Oct 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Fri Oct 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Sep 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Sep 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.5-alt1
- 2.3.5

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sat Jul 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Sun Jul 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.9-alt1
- 2.0.9

* Wed Jul 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Jul 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sat Jul 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Jun 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7

* Sun Jun 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.5-alt1
- 1.6.5

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Sun Jun 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.8-alt1
- 1.5.8

* Mon Jun 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- 1.5.7

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Wed Jun 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 05 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun May 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Mon May 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.6-alt1
- 1.3.6

* Sat May 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4

* Fri May 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Tue May 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Sun May 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat May 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.8-alt1
- 1.2.8

* Tue May 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- first build for Sisyphus


