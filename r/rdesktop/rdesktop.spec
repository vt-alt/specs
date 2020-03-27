Name: rdesktop
Version: 1.9.0
Release: alt1

Summary: A RDP client for accessing Windows Remote Desktop Services

License: GPLv3+
Group: Networking/Remote access
Url: http://www.rdesktop.org/

# Source0-url: https://github.com/rdesktop/rdesktop/archive/v%version.tar.gz
Source0: %name-%version.tar
Patch0: rdesktop-1.8.3-deb-alt-openssl1.1-support.patch

BuildRequires: libgnutls-devel libkrb5-devel libnettle-devel libpcsclite-devel libtasn1-devel
BuildRequires: libao-devel libsamplerate-devel 
BuildRequires: libX11-devel libXrandr-devel libXcursor-devel

%description
Rdesktop is an open source client for Windows Remote Desktop Services,
capable of natively speaking Remote Desktop Protocol (RDP) in order to
present the user's Windows desktop. Rdesktop is known to work with
Windows versions such as NT 4 Terminal Server, 2000, XP, 2003, 2003 R2,
Vista, 2008, 7, and 2008 R2.

%prep
%setup
#patch0 -p1

%build
%autoreconf
export ac_cv_prog_STRIP=/bin/true
%configure \
	--with-ipv6 \
	--with-sound=libao \
	--enable-credssp \
	--enable-smartcard
%make_build

%install
%makeinstall

sed -i 's/slash 0x56 altgr/#slash 0x56 altgr/' %buildroot%_datadir/%name/keymaps/ru

%files
%doc COPYING README.md doc/{AUTHORS,ChangeLog,HACKING,TODO,*.txt}
%_bindir/%name
%_datadir/%name
%_man1dir/*

%changelog
* Sun Oct 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)
- use GnuTLS and nettle instead of OpenSSL
- update buildreqs

* Sun Oct 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version 1.8.4 (with rpmrb script) (ALT bug 36068)
- CVE-2018-8794, CVE-2018-8795, CVE-2018-8797, CVE-2018-20175
- CVE-2018-20176, CVE-2018-8791, CVE-2018-8792, CVE-2018-8793
- CVE-2018-8796, CVE-2018-8798, CVE-2018-8799, CVE-2018-8800
- CVE-2018-20174, CVE-2018-20177, CVE-2018-20178, CVE-2018-20179
- CVE-2018-20180, CVE-2018-20181, CVE-2018-20182

* Tue Oct 02 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.3-alt1.qa1
- Fixed build and rebuilt with openssl 1.1.
- Disabled ELF strip(1)ping to enable debuginfo subpackage.

* Wed Jul 15 2015 Michael A. Kangin <prividen@altlinux.org> 1.8.3-alt1
- 1.8.3

* Tue Dec 10 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.1-alt1
- 1.8.1 (closes: #29643)
- Update Raw-keyboard-patch-for-1.8.1.patch
- Remove %{name}-libao.patch
- Fix ru keymaps (closes: #20053)

* Mon Aug 13 2012 Michael A. Kangin <prividen@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt4.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Jan 26 2010 Michael Shigorin <mike@altlinux.org> 1.6.0-alt4
- fixed (historical/unused) patch0 compression, thanks ldv@

* Mon Jan 25 2010 Michael Shigorin <mike@altlinux.org> 1.6.0-alt3
- built for Sisyphus (closes: #19968)
- buildreq

* Sun Jan 24 2010 Michael A. Kangin <prividen@altlinux.org> 1.6.0-alt2.1.2
- New raw keyboard patch

* Thu Aug 27 2009 Michael A. Kangin <prividen@altlinux.org> 1.6.0-alt2.1.1
- remove '-y' patch due evdev incompatibility (#19968)
- fixed RU keymap (#5912)

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.0-alt2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Wed Jul 09 2008 Igor Zubkov <icesik@altlinux.org> 1.6.0-alt2
- fix crash with long filenames (closes #13495)

* Wed May 14 2008 Igor Zubkov <icesik@altlinux.org> 1.6.0-alt1
- 1.6.0 release

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt7
- CVE-2008-1801
- CVE-2008-1802
- CVE-2008-1803

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt6
- add description of -y option to man page (closes #11447)

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt5
- remove menu file (closes #12794)

* Sat Apr 21 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt4
- update patch for raw input

* Sat Apr 21 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt3
- update from CVS (20070521) which fix random segfaults (#11441)
- build with alsa and without libao

* Thu Feb 22 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt2
- build with libao (closes #10741)
- buildreq

* Thu Feb 22 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt1
- enable IPv6 support (closes #10739)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.0-alt0.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Dec 04 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.5.0-alt0
- NMU: Fix (#6280)
- new version
- drop %name-1.4.1.20060218-rawkeyboard.patch
- add %name-1.5.0-rawkeyboard_nofreespace_kbswitch.tar.bz2

* Sat Feb 18 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.4.1.20060218-alt0
- CVS 20060218 (utf8 support in clipboard)

* Wed Oct 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- add patch from Serge Ryabchun (sr@) for raw keyboard mode (-y option)

* Thu Jul 07 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt0.1
- new version
- dropped a patches as merged with mainstream

* Fri Apr 01 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1
- new version

* Sat Oct 30 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt4
- add patch for KDE embedded (krdc)

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt3
- fix username encoding in command line options
  (add patch from Alexey V. Novikov (bug #5054))

* Wed Jul 28 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- remove menu entry (bug #3975)

* Sun May 02 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version

* Mon Jan 12 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version
- spec cleanup

* Fri Feb 14 2003 Dmitry Malenko <maldim@altlinux.ru> 1.2.0-alt2
- Fixed to look for keymaps in proper place

* Thu Feb 06 2003 Dmitry Malenko <maldim@altlinux.ru> 1.2.0-alt1
- New version
- Spec cleanup

* Wed Jan 29 2003 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt4
- Spec cleanup

* Fri Jan 24 2003 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt3
- Added Mandrake patch:
    * fixed NumLock behavior
    * support for mouse wheel
- Added man to distribution

* Mon Jun 24 2002 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt2
- Changed rdesktop.menu to accept RDP_CONNECTION variable as a parameter

* Wed May 29 2002 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt1
- Packaged for ALT Linux

