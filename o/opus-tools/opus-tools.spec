Name: opus-tools
Version: 0.2
Release: alt2

Summary: Opus Audio Codec utilities
License: BSD-style
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-0.2-elbrus.patch

Buildrequires: libogg-devel libflac-devel libopusenc-devel opusfile-devel opusurl-devel libflac-devel libpcap-devel

%description
The Opus codec is designed for interactive speech and audio transmission
over the Internet. It is designed by the IETF Codec Working Group and
incorporates technology from Skype's SILK codec and Xiph.Org's CELT
codec.

Opus-tools provides command-line utilities to encode, inspect, and
decode .opus files.

%prep
%setup
%patch -p2

%build
echo PACKAGE_VERSION="%version" > package_version
%autoreconf
%configure \
    %ifarch %ix86 x86_64
	--enable-sse
    %endif

%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS COPYING README.md

%changelog
* Tue Mar 24 2020 L.A. Kostis <lakostis@altlinux.ru> 0.2-alt2
- Added Elbrus support (by @mike).
- Enable SSE on x86
- Enable flac support
- Enable pcap support

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.2-alt1
- 0.2.
- Update BR (added libopusenc and opusfile/opusurl).

* Tue Sep 05 2017 L.A. Kostis <lakostis@altlinux.ru> 0.1.10-alt1
- 0.1.10.

* Mon Jun 06 2016 L.A. Kostis <lakostis@altlinux.ru> 0.1.9-alt0.1
- 0.1.9.

* Mon Mar 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.1.6-alt0.M60T.1
- build for t6

* Mon Mar 04 2013 L.A. Kostis <lakostis@altlinux.ru> 0.1.6-alt1
- 0.1.6.

* Sat Aug 25 2012 L.A. Kostis <lakostis@altlinux.ru> 0.1.4-alt1
- 0.1.4.

* Wed Jul 25 2012 L.A. Kostis <lakostis@altlinux.ru> 0.1.3-alt1
- initial build for ALTLinux.
