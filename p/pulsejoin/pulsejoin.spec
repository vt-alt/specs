Name: pulsejoin
Summary: PulseJoin
Version: 2.4
Release: alt1
License: GPLv3
Group: Sound
Url: https://gitlab.com/mikhailnov/pulsejoin
BuildArch: noarch
Source0: %name-%version.tar

# Recomended dependency:
Requires: pavucontrol

%description
GUI for making a virtual PulseAudio microphone,
from which sound from both microphone
and audio output can be recorded.

%description -l ru_RU.UTF-8
GUI для создания виртуального микрофона PulseAudio,
с которого можно записывать звук одновременно настоящего
микрофона и тот, что выводится на динамики.

%prep
%setup
# Workaround of https://bugzilla.altlinux.org/show_bug.cgi?id=35376
sed -i ./pulsejoin.sh -e 's,#!/usr/bin/env bash,#!/bin/bash,g'

%install
%makeinstall_std
%find_lang pulsejoin

%files -f pulsejoin.lang
%_bindir/*
%_datadir/applications/*

%changelog
* Wed Sep 18 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.4-alt1
- Version 2.4:
  + Report error if PulseAudio default source and/or sink have not been found
  + LANG=c was not a valid value, set LANG=POSIX instead (LANG=C would also be valid)
  + In addition to LANG=POSIX, set LC_ALL=POSIX to ensure that English output of pactl
    is being grepped (RB#10163)
* Fri Apr 12 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3-alt1
- Version 2.3:
  + Added Spanish translation
  + Remove empty temp directory on exit
  + Fallback to universal mktemp -d if needed
  + Don't remove temp file if unloading PulseAudio modules failed
  + Handle errors while creating/removing devices
  + Better handle errors on restarting PulseAudio
  + Fixed compatibility with both GNU and BSD sed
* Thu Apr 05 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.2-alt1
- Version 2.2
* Thu Apr 05 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.1-alt1
- Version 2.1
* Thu Apr 05 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0-alt1
- Version 2.0
* Thu Apr 04 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.3-alt1
- Version 1.3
* Thu Nov 08 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.2-alt1
- Version 1.2
* Mon Sep 09 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.1-alt1
- Version 1.1
* Sun Sep 09 2018 Mikhail Novosyolov <mikhailnov@dumalogiya.ru> 1.0-alt1
- initial RPM build for ALT Linux
