# SPEC file for cadaver package

Name:    cadaver
Version: 0.23.3
Release: alt5.git.4cbea82

Summary: a command-line WebDAV client
Summary(ru_RU.UTF-8): консольный клиент WebDAV

License: %gpl2plus
Group:   Networking/File transfer
URL:     http://www.webdav.org/cadaver/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.23.2-debian-manpage_hyphen.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 20 2011
BuildRequires: libexpat-devel libkeyutils-devel libncurses-devel libneon-devel libreadline-devel libssl-devel zlib-devel

%description
cadaver is a command-line WebDAV client for Unix.  It supports
file upload, download, on-screen display, namespace operations
(move/copy), collection creation and deletion, and locking
operations.

%prep
%setup
%patch0 -p1

%patch1 -p1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
./autogen.sh

# Add missed automake files:
for f in config.guess config.sub; do cp -p -- /usr/share/automake/$f .; done

autoconf -f
%configure --with-ssl=openssl --with-neon
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files  -f %name.lang
%doc FAQ README THANKS TODO BUGS INTEROP
%doc --no-dereference COPYING

%_bindir/%name
%_man1dir/%{name}*

%changelog
* Wed Jun 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.23.3-alt5.git.4cbea82
- Rebuild with libneon 0.31

* Tue Feb 12 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.23.3-alt4
- Rebuild with readline7

* Sun Nov 24 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.3-alt3
- Rebuild with libneon 0.30

* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.3-alt2
- Fix remote args globbing (Closes: #26649)

* Sun Mar 20 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.3-alt1
- New version

* Mon Nov 23 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt3
- Rebuild with libneon-0.29.0-alt1

* Tue May 26 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt2
- Rebuild with libneon-0.28.4-alt1

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt1
- Initial build for ALT Linux Sisyphus

* Sat Dec 06 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt0.1
- Initial build
