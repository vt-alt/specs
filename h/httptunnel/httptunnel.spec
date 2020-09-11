Name: httptunnel
Version: 3.3
Release: alt1

Url: http://www.nocrew.org/software/httptunnel.html

Summary: Bidirectional virtual data over HTTP-proxy
License: GPL-2.0
Group: Networking/Other

Packager: Andrey Cherepanov <cas@altlinux.org>

# Use debian repackage tarball, it doesn't include non-free documentation files
# from http://ftp.de.debian.org/debian/pool/main/h/httptunnel/httptunnel_%{version}+dfsg.orig.tar.gz
Source: %name-%version.tar

%description
httptunnel creates a bidirectional virtual data path tunnelled in HTTP
requests.  The requests can be sent via an HTTP proxy if so desired.

This can be useful for users behind restrictive firewalls.  If WWW
access is allowed through an HTTP proxy, it's possible to use
httptunnel and, say, telnet or PPP to connect to a computer outside
the firewall.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog DISCLAIMER FAQ HACKING NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Fri Sep 04 2020 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version (ALT #38889).
- Fix License tag according to SPDX.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0.5-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Nov 19 2008 Denis Smirnov <mithraen@altlinux.ru> 3.0.5-alt2
- cleanup spec

* Thu Feb 12 2004 Denis Smirnov <mithraen@altlinux.ru> 3.0.5-alt1
- Patch for binding at specified address
- First build for ALT Linux Sisyphus
