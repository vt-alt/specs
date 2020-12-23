%define username guacd
%def_with ffmpeg

Name: guacamole-server
Version: 1.2.0
Release: alt1.M90P.1
Summary: Server-side native components that form the Guacamole proxy
License: Apache-2.0
Url: http://guac-dev.org/
Group: Networking/Remote access

Source0: %name-%version.tar
Source1: %name.sysconfig
Source2: %name.service
Source3: %name.conf

Requires: guacd
Requires: libguac-client-ssh
Requires: libguac-client-rdp
Requires: libguac-client-vnc

BuildRequires: perl-Term-ReadLine-Gnu
BuildRequires: doxygen graphviz
BuildRequires: libjpeg-devel
BuildRequires: libwebsockets-devel
BuildRequires: systemd-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(freerdp2)
BuildRequires: pkgconfig(freerdp-client2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libtelnet)
BuildRequires: pkgconfig(libvncserver)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(ossp-uuid)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(winpr2)
# for test
BuildRequires: CUnit-devel

%if_with ffmpeg
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswscale)
%endif

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

This is virtual package with depends on:
- guacd
- libguac-client-ssh
- libguac-client-rdp
- libguac-client-vnc

%package -n libguac
Summary: The common library used by all C components of Guacamole
Group: System/Libraries

%description -n libguac
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-devel
Summary: Development files for %name
Group: Development/C
Requires: libguac = %EVR

%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %name.

%package -n libguac-client-kubernetes
Summary: Kubernetes pods terminal support for guacd
Group: System/Libraries
Requires: libguac = %EVR

%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.

%package -n libguac-client-rdp
Summary: RDP support for guacd
Group: System/Libraries
Requires: libguac = %EVR

%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Summary: SSH support for guacd
Group: System/Libraries
Requires: libguac = %EVR

%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Summary: VNC support for guacd
Group: System/Libraries
Requires: libguac = %EVR

%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Summary: Telnet support for guacd
Group: System/Libraries
Requires: libguac = %EVR

%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary: Proxy daemon for Guacamole
Group: Networking/Remote access
Requires: libguac = %EVR

%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
%setup

# p9 hack
sed -i s,-Werror,,g `find . -name Makefile.am`

%build
%autoreconf
%configure \
  --disable-silent-rules \
  --disable-static

%make_build
cd doc/
doxygen Doxyfile

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -delete
cp -fr doc/doxygen-output/html .

mkdir -p %buildroot%_sysconfdir/sysconfig
install -p -m 644 -D %SOURCE1 %buildroot%_sysconfdir/sysconfig/guacd
mkdir -p %buildroot%_sharedstatedir/guacd

# Systemd unit files
mkdir -p %buildroot%_unitdir
install -p -m 644 -D %SOURCE2 %buildroot%_unitdir/guacd.service

# Config
mkdir -p %buildroot%_sysconfdir/guacamole
install -p -m 644 -D %SOURCE3 %buildroot%_sysconfdir/guacamole/guacd.conf

%check
%make check

%pre -n guacd
groupadd -r -f %username 2>/dev/null ||:
useradd -r -g %username -c 'Guacamole proxy daemon' \
        -s /sbin/nologin -d %_sharedstatedir/guacd -M %username 2>/dev/null ||:

%post -n guacd
%post_service guacd.service

%preun -n guacd
%preun_service guacd.service

%files

%files -n libguac
%doc LICENSE
%doc README CONTRIBUTING
%_libdir/libguac.so.*

%files -n libguac-devel
%doc html
%_includedir/*
%_libdir/libguac.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%files -n libguac-client-kubernetes
%_libdir/libguac-client-kubernetes.so
%_libdir/libguac-client-kubernetes.so.*

%files -n libguac-client-rdp
%_libdir/libguac-client-rdp.so
%_libdir/libguac-client-rdp.so.*
%_libdir/freerdp2/*.so

%files -n libguac-client-ssh
%_libdir/libguac-client-ssh.so
%_libdir/libguac-client-ssh.so.*

%files -n libguac-client-vnc
%_libdir/libguac-client-vnc.so
%_libdir/libguac-client-vnc.so.*

%files -n libguac-client-telnet
%_libdir/libguac-client-telnet.so
%_libdir/libguac-client-telnet.so.*

%files -n guacd
%config(noreplace) %_sysconfdir/sysconfig/guacd
%dir %_sysconfdir/guacamole
%config(noreplace) %_sysconfdir/guacamole/guacd.conf
%_bindir/guaclog
%if_with ffmpeg
%_bindir/guacenc
%_mandir/man1/guacenc.1.*
%endif
%_mandir/man1/guaclog.1.*
%_mandir/man5/guacd.conf.5.*
%_mandir/man8/guacd.8.*
%_sbindir/guacd
%_unitdir/guacd.service
%attr(750,%username,%username) %_sharedstatedir/guacd

%changelog
* Wed Dec 16 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1.M90P.1
- p9 backport

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt2
- Add virtual package guacamole-server with depends on:
  + guacd
  + libguac-client-ssh
  + libguac-client-rdp
  + libguac-client-vnc

* Wed Nov 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- Initial build
