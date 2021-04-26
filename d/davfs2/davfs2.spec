Name: davfs2
Version: 1.6.0
Release: alt1

Summary: Linux file system driver that allows you to mount a WebDAV server as a local file system.
License: GPLv3+
Group: Networking/Other
Url: http://savannah.nongnu.org/projects/davfs2/

Source: %name-%version.tar

# Automatically added by buildreq on Mon May 25 2009
BuildRequires: libexpat-devel libneon-devel libssl-devel zlib-devel libkeyutils-devel

%description
WebDAV is an extension to HTTP that allows remote collaborative
authoring of Web resources, defined in RFC 4918.

davfs2 is a Linux file system driver that allows you to mount a WebDAV
server as a local file system, like a disk drive. This way applications
can access resources on a Web server without knowing anything about HTTP
or WebDAV.

davfs2 runs as a daemon in userspace. It uses the kernel file system
fuse. To connect to the WebDAV server it makes use of the neon library.
Neon supports TLS/SSL (using OpenSSL or GnuTLS) and access
via proxy server.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot
ln -sf %_sbindir/mount.davfs %buildroot/sbin/mount.davfs
ln -sf %_sbindir/umount.davfs %buildroot/sbin/umount.davfs
%find_lang %name

%pre
# Add davfs2 group
%_sbindir/groupadd -r -f davfs2 2>/dev/null || :

%files -f %name.lang
%doc AUTHORS ChangeLog FAQ INSTALL NEWS README TODO THANKS
%config %_sysconfdir/%name/
/sbin/mount.davfs
/sbin/umount.davfs
%_sbindir/*
%_man5dir/*
%_man8dir/*
%_datadir/%name/
%exclude %_defaultdocdir/%name
%exclude %_mandir/de
%exclude %_mandir/es

%changelog
* Tue Sep 15 2020 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Jan 14 2020 Anton Farygin <rider@altlinux.ru> 1.5.6-alt1
- 1.5.6

* Sun Mar 17 2019 Anton Farygin <rider@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Wed Jul 12 2017 Anton Farygin <rider@altlinux.ru> 1.5.4-alt1
- new version with security fixes:
	+ CVE-2013-4362 Unsecure use of system()

* Sun Nov  3 2013 Sergey Kurakin <kurakin@altlinux.org> 1.4.7-alt2
- allow building with libneon v.30

* Sun Jul 21 2013 Sergey Kurakin <kurakin@altlinux.org> 1.4.7-alt1
- 1.4.7: bugfix release

* Mon Mar  8 2011 Sergey Kurakin <kurakin@altlinux.org> 1.4.6-alt2
- build fixed (buildreq)

* Wed Jun  2 2010 Sergey Kurakin <kurakin@altlinux.org> 1.4.6-alt1
- 1.4.6: just two bugs fixed

* Tue Oct 20 2009 Sergey Kurakin <kurakin@altlinux.org> 1.4.5-alt1
- 1.4.5: fixes some of the more stupid bugs

* Tue Oct 20 2009 Sergey Kurakin <kurakin@altlinux.org> 1.4.3-alt1
- 1.4.3:
  + Neon 0.29 support
  + new configuration options and command line options
  + bug fixes and workarounds for server bugs

* Wed Jul 22 2009 Sergey Kurakin <kurakin@altlinux.org> 1.4.1-alt1
- 1.4.1: bugfix release
- fixed unowned directory

* Mon May 25 2009 Sergey Kurakin <kurakin@altlinux.org> 1.4.0-alt1
- 1.4.0
  + bugs fixing
  + significant changes in the default configuration (read NEWS)
  + license changed (GPLv2 to GPLv3+)
  + home Url changed (sourceforge to savannah)
- fixed build (BuildRequires)

* Tue Oct 28 2008 Sergey Kurakin <kurakin@altlinux.org> 1.3.3-alt2
- fixed build with gcc4.3

* Mon Aug 25 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Thu Jun 27 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.3.2-alt2
- build with libneon 0.28

* Thu Jun  5 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.3.2-alt1
- new version (bugfix release)

* Wed Apr 23 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.3.0-alt2
- user configuration templates moved back to /usr/share/davfs2/

* Wed Feb 27 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.3.0-alt1
- initial build for Sisyphus

