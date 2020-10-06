Name: pulseaudio-dlna
Version: 0.6.0
Release: alt1.20190209
Summary: A lightweight streaming server which brings DLNA/UPNP and Chromecast

License: GPLv3
Group: Sound
Url: https://github.com/masmu/pulseaudio-dlna
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%add_python3_req_skip BaseHTTPServer SocketServer urlparse

%description
This is pulseaudio-dlna. A lightweight streaming server which brings DLNA / UPNP
and Chromecast support to PulseAudio and Linux. It can stream your current
PulseAudio playback to different UPNP devices (UPNP Media Renderers) or
Chromecasts in your network. It's main goals are: easy to use, no configuration
hassle, no big dependencies.

UPNP renderers in your network will show up as pulseaudio sinks.

%prep
%setup

%build
%python3_build

%install
%python3_install

rm %buildroot%python3_sitelibdir/*.egg-info/requires.txt

%files
%_bindir/*
%doc LICENSE
%doc README.*
%python3_sitelibdir/pulseaudio_dlna
%python3_sitelibdir/*.egg-info
%_man1dir/%name.1.*

%changelog
* Sat Sep 26 2020 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1.20190209
- New snapshot (future 0.6.0)
- switch to python3
- change Group: Sound

* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.5.2-alt1
- Initial build for ALT Linux Sisyphus.
