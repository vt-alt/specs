Name: remove-obsoleted-packages
Version: 1.1
Release: alt1

Summary: Remove obsoleted packages

Group: System/Servers
License: GPL

#Source: %name-%version.tar

BuildArch: noarch

Conflicts: libzip libzip4

Conflicts: gcc4.3 gcc4.4 cpp4.3 cpp4.4 gcc4.8 cpp4.8 gcc6 cpp6 cpp7 gcc7-fortran gcc7
Conflicts: clang6.0

Conflicts: libqt3 qt4-common

# Note: Obsoletes using does effect Provides too.
Conflicts: hald libhal hal-info hal-laptop hal-cups-utils DeviceKit
Conflicts: arts libarts libarts-qtmcop libarts-devel
Conflicts: xpdf xpdf-common xpdf-reader

Conflicts: libwpd libwpd9

Conflicts: libmysqlclient12 libmysqlclient15 libmysqlclient16 libmysqlclient17

# obsoleted ffmpeg
Conflicts: libavdevice55 libswscale libavresample2
Conflicts: libavfilter5 libavfilter6
Conflicts: libavcodec53 libavcodec56
Conflicts: libavutil51 libavutil53 libavutil54
Conflicts: libavformat53 libavformat56

Conflicts: libx265 libx264.142 
Conflicts: libwebp < 0.5
Conflicts: libwebp6
Conflicts: libwrap libevent2 libprotobuf7 libprotobuf9
Conflicts: libGLEW2.0 libGLEW1.13

Conflicts: libmozjs17 
Conflicts: libreadline6
Conflicts: libpq5.3

Conflicts: libicu42 libicu44 libicu46 libicu4.8 libicu50 libicu56
Conflicts: libicu60 libicu61 libicu62

Conflicts: libpoppler2 libpoppler3 libpoppler4 libpoppler5 libpoppler6 libpoppler7
Conflicts: libpoppler08 libpoppler8 libpoppler12 libpoppler13 libpoppler19
Conflicts: libpoppler26 libpoppler27 libpoppler28 libpoppler29 libpoppler30
Conflicts: libpoppler31 libpoppler22 libpoppler33 libpoppler34 libpoppler35
Conflicts: libpoppler36 libpoppler37 libpoppler38 libpoppler39 libpoppler40
Conflicts: libpoppler41 libpoppler42 libpoppler43 libpoppler44 libpoppler45
Conflicts: libpoppler46 libpoppler47 libpoppler48 libpoppler50 libpoppler51
Conflicts: libpoppler52 libpoppler53 libpoppler54 libpoppler56 libpoppler57
Conflicts: libpoppler58 libpoppler59 libpoppler60 libpoppler61 libpoppler62
Conflicts: libpoppler63 libpoppler64 libpoppler65 libpoppler66 libpoppler67
Conflicts: libpoppler68 libpoppler69 libpoppler70 libpoppler71 libpoppler72
Conflicts: libpoppler73 libpoppler74 libpoppler75 libpoppler76 libpoppler77
Conflicts: libpoppler78 libpoppler79 libpoppler80 libpoppler81 libpoppler82
Conflicts: libpoppler83 libpoppler84
# libpoppler85 is latest at 24.03.2019

Conflicts: libv8-3.15 libv8-3.18 libv8-3.19 libv8-3.21 libv8-3.22 libv8-3.23 libv8-3.24
Conflicts: libv8-4.1 libv8-4.2 libv8-4.3 libv8-4.4

%define ConflictBoost() \
Conflicts: libboost_regex%{1} \
Conflicts: libboost_python%{1} \
Conflicts: libboost_python3-%{1} \
Conflicts: libboost_system%{1} \
Conflicts: libboost_serialization%{1} \
Conflicts: boost_serialization%{1} \
Conflicts: libboost_thread%{1} \
Conflicts: libboost_test%{1} \
Conflicts: libboost_signals%{1} \
Conflicts: libboost_container%{1} \
Conflicts: libboost_context%{1} \
Conflicts: libboost_stacktrace%{1} \
Conflicts: libboost_random%{1} \
Conflicts: libboost_iostreams%{1} \
Conflicts: libboost_program_options%{1} \
Conflicts: libboost_date_time%{1} \
Conflicts: libboost_graph1%{1} \
%nil

%ConflictBoost 1.34.1
%ConflictBoost 1.36.0
%ConflictBoost 1.39.0
%ConflictBoost 1.40.0
%ConflictBoost 1.41.0
%ConflictBoost 1.42.0
%ConflictBoost 1.43.0
%ConflictBoost 1.44.0
%ConflictBoost 1.45.0
%ConflictBoost 1.46.0
%ConflictBoost 1.47.0
%ConflictBoost 1.48.0
%ConflictBoost 1.49.0
%ConflictBoost 1.50.0
%ConflictBoost 1.51.0
%ConflictBoost 1.52.0
%ConflictBoost 1.53.0
%ConflictBoost 1.57.0
%ConflictBoost 1.58.0
%ConflictBoost 1.63.0
%ConflictBoost 1.65.0
%ConflictBoost 1.66.0

Conflicts: libjasper1
Conflicts: libpng12
Conflicts: libpng15

# there are 7colors, soundtracker, fvwm-gtk, xtetty using imlib
Conflicts: imlib

Conflicts: glib gtk+

Conflicts: gnome-libs

%description
This package will remove obsoleted packages from your system
during install.

%files

%changelog
* Tue Mar 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- add ffmpeg libs and some others

* Sun Mar 24 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- major update (qt3, qt4, old gcc, old boost)

* Tue Apr 19 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- update conflicts
- conflicts gtk+, glib

* Thu Feb 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- update conflicts
- rewrite boost conflicts

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- improve obsoleted packages list

* Sat Feb 08 2014 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt2
- update conflicts

* Sat Feb 08 2014 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- new build (add many libpopplers)

* Tue Oct 15 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new build (add many libpopplers)

* Sun Mar 31 2013 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- use conflicts instead obsoletes (fix provides effect)

* Fri Mar 22 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- new build

* Thu Nov 29 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
