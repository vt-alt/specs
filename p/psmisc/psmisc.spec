# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: psmisc
Version: 23.3
Release: alt2

Summary: Miscellaneous utilities that use proc filesystem
License: GPL-2.0-only
Group: System/Base
Url: https://gitlab.com/psmisc/psmisc
Vcs: https://gitlab.com/psmisc/psmisc.git
Source: %name-%version.tar

%def_enable selinux
BuildRequires: libncurses-devel %{?_enable_selinux:libselinux-devel}
BuildRequires: libseccomp-devel
BuildRequires: libcap-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: banner dejagnu rpm-build-vm >= 1.9 strace /proc}}

%description
A package of small utilities that use proc filesystem.
  fuser   - Identifies processes using files or sockets
  killall - Kills processes by name, e.g. killall -HUP named
  prtstat - Prints statistics of a process
  pslog   - Prints log path(s) of a process
  pstree  - Shows currently running processes as a tree
  peekfd  - Shows the data travelling over a file descriptor

%prep
%setup

%define _configure_script ../configure
%build
./autogen.sh
mkdir build
cd build
%configure %{subst_enable selinux} --disable-harden-flags --enable-sandbox
%make_build

%install
%makeinstall_std -C build
mkdir -p %buildroot/sbin
mv %buildroot%_bindir/fuser %buildroot/sbin/
ln -s ../../sbin/fuser %buildroot%_bindir/

pushd %buildroot%_bindir/
ln -sf pstree pstree.x11
popd

%find_lang %name

%check
pushd build
PATH=%buildroot/sbin:%buildroot%_bindir:$PATH
%ifarch x86_64
 strace -o killall.log killall -s0 -u $USER
 grep ^seccomp.*SECCOMP_SET_MODE_FILTER killall.log
 grep ^prlimit.*RLIMIT_NPROC killall.log
 grep ^capset.*CAP_SYS_PTRACE killall.log
%endif

my_tests() {
  type killall pstree prtstat fuser pslog peekfd || :
  killall --list
  sleep 1m & sleep 1; killall sleep
  sleep 1m & sleep 1; killall -e sleep
  sleep 1m & sleep 1; killall -I SLEEP
  sleep 1m & sleep 1; killall -r sl.ep
  sleep 1m & sleep 1; killall -v sleep
  sleep 1m & sleep 1; killall -w sleep
  ! killall -s0 killall
  killall -s0 -u $USER
  yes | killall -s0 -u $USER -i > /dev/null
  pstree
  pstree -a >/dev/null
  pstree -A >/dev/null
  pstree -c >/dev/null
  pstree -g >/dev/null
  pstree -l >/dev/null
  pstree -n >/dev/null
  pstree -p >/dev/null
  pstree -S >/dev/null
  pstree -s >/dev/null
  pstree -t >/dev/null
  pstree -T >/dev/null
  pstree -u >/dev/null
  pstree -U >/dev/null
  prtstat $$
  prtstat -r $$
  fuser --list-signals
  fuser -v /proc  >/dev/null
  fuser -mv /proc >/dev/null
  fuser -m . -n file >/dev/null
  fuser -m . -n udp  >/dev/null
  fuser -m . -n tcp  >/dev/null
  fuser -m . -u  >/dev/null
  fuser -m . -4  >/dev/null
  fuser -m . -6  >/dev/null
  pslog $$
}
export -f my_tests

banner TESTS
my_tests
make check

banner VM
vm-run "set -xe
  type killall
  /sbin/capsh --user=nobody -- -c 'sleep 1m' & sleep 1; killall sleep
  /sbin/capsh --user=nobody -- -c 'sleep 1m' & sleep 1; killall -u nobody
  # conflicts with kernel.yama.ptrace_scope=1
  if type peekfd 2>/dev/null; then
    timeout 1 peekfd \$\$ || test \$? = 124
  fi
  my_tests"
popd

banner ASAN
PATH=src:$PATH
mkdir asan
cd asan
# detect_leaks=0 or configure will fail to detect malloc due to leak in test
ASAN_OPTIONS=detect_leaks=0 CFLAGS=-fsanitize=address \
     ../configure %{subst_enable selinux} --disable-harden-flags -q --disable-sandbox
%make_build -s
my_tests
make check

%files -f %name.lang
/sbin/*
%_bindir/*
%_man1dir/*.1*
%doc AUTHORS ChangeLog COPYING README.md

%changelog
* Wed Jul 08 2020 Vitaly Chikunov <vt@altlinux.org> 23.3-alt2
- spec: Simplify binaries packing.

* Fri Jul 03 2020 Vitaly Chikunov <vt@altlinux.org> 23.3-alt1
- Fresh re-import of v23.3.
- spec: Add tests into %%check section.
- Add seccomp sandboxing and drop most of root capabilities.

* Sat Dec 08 2012 Dmitry V. Levin <ldv@altlinux.org> 22.20-alt1
- Updated to v22.20 (closes: #28204).

* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 22.13-alt1
- Updated to v22.13-7-g64e6225.
- Packaged %_bindir/fuser symlink (closes: #11762).
- Enabled selinux support.

* Sun Nov 19 2006 Dmitry V. Levin <ldv@altlinux.org> 22.3-alt1
- Updated to 22.3.
- Fixed a few uninitialized read errors.

* Tue May  2 2006 Ilya Evseev <evseev@altlinux.ru> 22.2-alt1
- updated to new version 22.2

* Thu Jan 12 2006 Ilya Evseev <evseev@altlinux.ru> 22.1-alt1
- updated to new version 22.1, revisite patchset:
   + rewrite patch #1 (hrrrr..),
   + obsolete patch #5 (included to upstream).

* Tue Nov  8 2005 Ilya Evseev <evseev@altlinux.ru> 21.8-alt1
- updated to new version 21.8, revisite P1 (fuser patch)

* Tue Nov  1 2005 Ilya Evseev <evseev@altlinux.ru> 21.7-alt1
- updated to new version, revisite patchset:
   + patch #1 is rewritten from scratch
   + patches #3 and #4 are removed because they are included to upstream

* Mon Sep 19 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.6-alt3
- Added patch #5: prevent failures on validation of generated signal names list
  (fails incorrectly in hasher environment even signames.h is fine)

* Mon Sep 12 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.6-alt2
- Added russian language messages file

* Sun Mar 15 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.6-alt1
- Updated to 21.6, revisited patches: P3

* Tue Jan 18 2005 Dmitry V. Levin <ldv@altlinux.org> 21.5-alt3
- Implemented support for restricted proc kernel patch (Owl).

* Fri Jan 14 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.5-alt2
- remove actually unneeded dependency from C++

* Sun Jan  9 2005 Ilya G. Evseev <evseev@altlinux.ru> 21.5-alt1
- Updated to 21.5

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 21.4-alt1
- Updated to 21.4
- Updated patches.
- Fixed potential null dereference bug introduced in 21.4.

* Thu Dec 26 2002 Dmitry V. Levin <ldv@altlinux.org> 21.2-alt2
- (Owl) Fixed the segfault in pstree(1) when asked to report
  information for a user, but entry with PID 1 (init) is
  inaccessible, thanks to (GalaxyMaster).
- Fixed build with fresh autotools.

* Tue Oct 22 2002 Dmitry V. Levin <ldv@altlinux.org> 21.2-alt1
- Updated to 21.2

* Mon Jun 24 2002 Dmitry V. Levin <ldv@altlinux.org> 21-alt2
- Patched to link with libtinfo.

* Sun May 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 21-alt1
- 21

* Wed Mar 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 20.2-alt1
- 20.2
- License and url's changed
- useless man(1) pidof removed, it conflicts with man(8) from SysVinit
  package.

* Mon Apr 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 20.1-alt1
- 20.1

* Tue Dec 26 2000 Dmitry V. Levin <ldv@fandra.org> 19-ipl3mdk
- FHSification.

* Wed May 17 2000 Dmitry V. Levin <ldv@fandra.org> 19-ipl2mdk
- Fixed: kill patch.
- RE adaptions.

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 19-2mdk
- Fix bad tag value.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 19-1mdk
- Version update (19)
- Use default Mandrake Optimisations.
- Patch the Makefile for psmisc rpm to be compiled by non root user.
- bziped psmisc-17-buildroot.patch

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Move fuser to /sbin(r).

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Sat Mar 13 1999 Michael Maher <mike@redhat.com>
- updated package

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- renamed the patch file .patch instead of .spec

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to psmisc version 17
- buildrooted

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from version 11 to version 16
- spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
