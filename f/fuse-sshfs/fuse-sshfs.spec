Name: fuse-sshfs
Version: 3.7.0
Release: alt2

Summary: SSH filesystem using FUSE
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/libfuse/sshfs

# repacked https://github.com/libfuse/sshfs/releases/download/sshfs-%version/sshfs-%version.tar.xz
Source: sshfs-%version.tar
Source1: sshfs.watch
Patch1: alt-find-rst2man.patch

BuildRequires: libfuse3-devel >= 3.1.0 meson python3-module-docutils
Requires: ssh-provider-openssh-clients

Provides: sshfs-fuse = %version sshfs = %version
Obsoletes: sshfs-fuse < %version sshfs < %version

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: glib2-devel libfuse-devel openssh-clients

%description
This is a filesystem client based on the SSH File Transfer Protocol. Since most
SSH servers already support this protocol it is very easy to set up: i.e. on
the server side there's nothing to do. On the client side mounting the 
filesystem is as easy as logging into the server with ssh.

The idea of sshfs was taken from the SSHFS filesystem distributed with LUFS,
which sshfs-fuse's author found very useful. There were some limitations of
that codebase, so he rewrote it. Features of this implementation are:

* Based on FUSE (the best userspace filesystem framework for linux ;-)
* Multithreading: more than one request can be on it's way to the server
* Allowing large reads (max 64k)
* Caching directory contents
* Reconnect on failure

%prep
%setup -q -n sshfs-%version
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS README.rst
%_bindir/sshfs
%_sbindir/mount.sshfs
%_sbindir/mount.fuse.sshfs
%_man1dir/sshfs.*

%changelog
* Thu Jun 11 2020 Sergey V Turchin <zerg@altlinux.org> 3.7.0-alt2
- fix build manpage
- allow to install with openssh-gostcrypto

* Fri Feb 07 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.7.0-alt1
- Updated 3.7.0.

* Fri Nov 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.6.0-alt1
- Updated to 3.6.0.
- Packed watch file in the sourcerpm.

* Thu Sep 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.5.2-alt1
- 3.5.2.
- Refreshed Url for new upstream.

* Thu Oct  9 2014 Terechkov Evgenii <evg@altlinux.org> 2.5-alt1
- 2.4 -> 2.5

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.4-alt1
- 2.3 -> 2.4

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 2.3-alt1
- 2.2 -> 2.3

* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * specfile-macros-get_dep-is-deprecated for fuse-sshfs

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 2.2-alt1
- 2.1 -> 2.2

* Sun Jul 20 2008 Igor Zubkov <icesik@altlinux.org> 2.1-alt1
- 2.0 -> 2.1

* Fri Jun 13 2008 Igor Zubkov <icesik@altlinux.org> 2.0-alt1
- 1.9 -> 2.0

* Mon Dec 17 2007 Igor Zubkov <icesik@altlinux.org> 1.9-alt1
- 1.8 -> 1.9
- don't build the sshnodelay.so workaround

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 1.8-alt1
- 1.7 -> 1.8

* Tue Oct 24 2006 Andrei Bulava <abulava@altlinux.ru> 1.7-alt1
- 1.7

* Mon Apr 03 2006 Andrei Bulava <abulava@altlinux.ru> 1.6-alt1
- 1.6

* Thu Nov 24 2005 Andrei Bulava <abulava@altlinux.ru> 1.3-alt1
- 1.3
- relaxed Requires regarding fuse

* Tue Oct 11 2005 Andrei Bulava <abulava@altlinux.ru> 1.2-alt2
- minor spec fixes:
  + got rid of an awkward hack and used %%get_version macro instead
  + added Packager field

* Wed Sep 14 2005 Andrei Bulava <abulava@altlinux.ru> 1.2-alt1
- 1.2
- updated BuildRequires

* Tue Jun 07 2005 Andrei Bulava <abulava@altlinux.ru> 1.1-alt2.1
- rebuilt with fuse-2.3

* Fri Apr 29 2005 Andrei Bulava <abulava@altlinux.ru> 1.1-alt2
- renamed to fuse-sshfs (#6588)
- added dependency on fuse-<version> to track lame ABI changes of libfuse
  (#6599, see also #6588)

* Mon Apr 18 2005 Andrei Bulava <abulava@altlinux.ru> 1.1-alt1
- initial build for ALT Linux

