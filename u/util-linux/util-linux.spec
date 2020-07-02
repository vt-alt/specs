%define _unpackaged_files_terminate_build 1
%undefine __libtoolize

### Header
Summary: A collection of basic system utilities
Name: util-linux
Version: 2.33.2
Release: alt2
License: GPL-2.0 and GPL-2.0-or-later and LGPL-2.1-or-later and BSD-3-Clause and BSD-4-Clause-UC and Public-Domain
Group: System/Base
URL: ftp://ftp.kernel.org/pub/linux/utils/util-linux
Packager: Alexey Gladkov <legion@altlinux.ru>

### Macros
%def_enable raw
%def_enable uuidd
%def_with setarch
%def_enable runuser
%def_disable login
%def_disable sulogin
%def_disable su
%def_disable chfn_chsh
%def_disable newgrp
%def_disable vipw
%def_enable schedutils
%def_enable fsck
%def_with selinux
%def_with audit
%def_with udev
%def_without systemd
%def_enable line
%def_disable mountpoint
%def_disable eject

### Dependences
BuildRequires: /proc,/dev/pts
BuildRequires: bash4
BuildRequires: glibc-devel-static
BuildRequires: zlib-devel
BuildRequires: libncursesw-devel
BuildRequires: libpopt-devel
BuildRequires: libcap-ng-devel
%{?_with_selinux:BuildRequires: libselinux-devel}
%{?_with_audit:BuildRequires: libaudit-devel}
%{?_with_udev:BuildRequires: libudev-devel}
%{?_with_systemd:BuildRequires: libsystemd-devel}
%{?_enable_login:BuildRequires: libpam-devel}
%{?_enable_runuser:BuildRequires: libpam-devel}

%ifnarch %arm %e2k
BuildRequires: klibc-devel
%endif

### Sources
Source0: util-linux-%version.tar
Source1: util-linux-login.pamd
Source2: util-linux-runuser.pamd
Source3: util-linux-runuser-l.pamd
Source4: util-linux-chsh-chfn.pamd
Source5: mount.control
Source6: write.control
Source7: vol_id
Source8: nologin.c
Source9: nologin.8
Source10: pause.c
Source11: stacktest.c
Source12: clock_unsynced.c

### Obsoletes & Conflicts & Provides
Obsoletes: tunelp
Obsoletes: util-linux-ng
Obsoletes: util-linux-initramfs

Conflicts: initscripts <= 4.58, timeconfig <= 3.0.1
Provides: util-linux-ng = %version-%release

#for old kernels
Provides: /usr/sbin/rdev
Conflicts: kernel < 2.2.12-7

#due to fsck migration
%if_enabled fsck
Conflicts: e2fsprogs < 0:1.41.9-alt3
%endif

Requires(pre,post): %name-control = %version-%release
Requires: coreutils > 6.10-alt2
Requires: libsmartcols = %version-%release

#due to findmnt
Requires: libmount = %version-%release

# 151635 - makeing /var/log/lastlog
Patch5: util-linux-ng-2.21-login-lastlog.patch

# Owl
Patch41: util-linux-2.29.0-owl-write.patch

Patch50: util-linux-2.25.2-alt-pg.patch
Patch51: util-linux-ng-2.30.2-mount-pamconsole.patch
Patch52: util-linux-2.11a-gecossize.patch
Patch54: util-linux-2.11f-rh-rawman.patch
Patch58: util-linux-2.12r-alt-mount-MS_SILENT.patch
Patch59: util-linux-tests.patch
Patch60: util-linux-2.33.1-alt-agetty-release.patch
Patch61: util-linux-2.33.1-add-new-e2k-subarches.patch

# 33152 - logger without systemd support
Patch70: util-linux-2.29.2-alt-logger_man.patch

Patch71: 0011-setarch-make-verify_arch_domain-extendable.patch
Patch72: 0012-setarch-add-arm-and-aarch64-architectures-to-transit.patch

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.

%package control
Summary: Control scripts for %name and mount
Group: System/Base
BuildArch: noarch

%description control
This package contains control(8) scripts used by %name and mount packages.

%package -n lsblk
Summary: List block devices
Group: System/Base
Requires: libsmartcols = %version-%release

%description -n lsblk
lsblk lists information about all or the specified block devices.

%package -n mount
Summary: Programs for mounting and unmounting filesystems
Group: System/Base
Requires(pre,post): %name-control = %version-%release
Requires: libblkid = %version-%release
Requires: libmount = %version-%release
Requires: libsmartcols = %version-%release

%description -n mount
The %name package contains the mount, umount, swapon and swapoff
programs.  Accessible files on your system are arranged in one big
tree or hierarchy.  These files can be spread out over several
devices. The mount command attaches a filesystem on some device to
your system's file tree.  The umount command detaches a filesystem
from the tree.  Swapon and swapoff, respectively, specify and disable
devices and files for paging and swapping.

%package -n losetup
Summary: Programs for setting up and configuring loopback devices
Group: System/Base
Requires: hashalot
Requires: libsmartcols = %version-%release

%description -n losetup
Linux supports a special block device called the loop device, which
maps a normal file onto a virtual block device.  This allows for the
file to be used as a "virtual file system" inside another file.
Losetup is used to associate loop devices with regular files or block
devices, to detach loop devices and to query the status of a loop device.

%package -n agetty
Summary: Alternative Linux getty
Group: System/Base
Requires: login

%description -n agetty
The alternative getty program for Linux.

%package -n cfdisk
Summary: The partitioning program with ncurses interface
Group: System/Configuration/Hardware
Requires: libblkid = %version-%release
Requires: libsmartcols = %version-%release

%description -n cfdisk
Small user-friendly ncurses-based partitioning program, which will help you
to partition your disk easily.

%package -n fdisk
Summary: The Partitioning Program
Group: System/Configuration/Hardware
Requires: libblkid = %version-%release
Requires: libsmartcols = %version-%release

%description -n fdisk
Small partitioning program with command line interface, that will be hard
for linux newbie, but it is extra stable, and you can trust it.

%package -n sfdisk
Summary: Partitioning program with argument interface
Group: System/Configuration/Hardware

%description -n sfdisk
Small partitioning program with argument interface, that will be hard
for linux newbie, but it is extra stable, and you can trust it.

%package -n hwclock
Summary: Query and set the hardware clock
License: GPL
Group: System/Base
Serial: 1
%ifarch alpha sparc sparc64
Obsoletes: clock
%endif

%description -n hwclock
Hwclock is a program that runs under Linux and sets and queries the
Hardware Clock, which is often called the Real Time Clock, RTC, or
CMOS clock.

You can set the Hardware Clock to a particular time or from the Linux
System Time.  You can set the Linux System Time from the Hardware
Clock, and a typical usage is to invoke Hwclock from a system startup
script to initialize the System Time.

Hwclock's --adjust function corrects systematic drift in the Hardware
Clock.  You just invoke it regularly and it corrects for a fast or
slow Hardware Clock.  Hwclock automatically computes how fast or slow
the Hardware Clock is every time you set it.

Hwclock uses /dev/rtc if it is available.  Otherwise, it uses its own
direct I/O to do what the rtc device driver would normally do.

%package -n getopt
Summary: An improved implementation of getopt
Group: System/Base

%description -n getopt
An improved implementation of getopt(1), a program to parse
options within a shell script. Fully compatible with other
getopt(1) implementations, but with many additions like
long options and mixing of options and parameters.

%package -n login
Summary: Start an interactive session on the system
Group: System/Base
Requires: pam >= 0.75-alt12

%description -n login
The login application opens an interactive session with a Linux workstation.
It is one of the first applications a user interacts with, but is generally
not invoked by a normal user.  Instead some program like mingetty(8) will
invoke login.

%package -n uuidd
Summary: Helper daemon to guarantee uniqueness of time-based UUIDs
Group: System/Servers
Requires: libuuid = %version-%release

%description -n uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.

%package -n setarch
Summary: Personality setter
Group: System/Kernel and hardware
%ifarch sparc sparcv9 sparc64
Provides: sparc32
Obsoletes: sparc32
%endif

%description -n setarch
This utility tells the kernel to report a different architecture than
the current one, then runs a program in that environment.  It can also
set various personality flags.

%package -n schedutils
Summary: Utilities for manipulating process scheduler attributes
Group: System/Kernel and hardware

%description -n schedutils
schedutils is a set of utilities for retrieving and manipulating process 
scheduler-related attributes, such as real-time parameters and CPU affinity. 
 
This package includes the chrt and taskset utilities. 

Install this package if you need to set or get scheduler-related attributes.

%package -n look
Summary: Program to display lines beginning with a given string
Group: System/Base
Requires: words

%description -n look
The look utility displays any lines in file which contain string as a prefix.

%package -n eject
Summary: A program that ejects removable media using software control
Group: System/Kernel and hardware

%description -n eject
Eject  allows  removable  media (typically a CD-ROM, floppy disk, tape,
JAZ, ZIP or USB disk) to be ejected under software control.   The  command
can  also control some multi-disc CD-ROM changers, the auto-eject feature
supported by some devices, and close the disc tray of some  CD-ROM drives.

%package -n rfkill
Summary: A tool to use /dev/rfkill
Group: Networking/Other

%description -n rfkill
rfkill is a small tool to query the state of the rfkill switches,
buttons and subsystem interfaces.

%package -n libblkid
Summary: Dynamic block device id library
Group: System/Libraries
Requires: libuuid = %version-%release

%description -n libblkid
The blkid library which allows system programs like fsck and mount to
quickly and easily find block devices by filesystem UUID and LABEL.

%package -n libblkid-devel
Summary: Development block device id library and include files
Group: Development/C
Requires: libblkid = %version-%release

%description -n libblkid-devel
This package contains the library and include files needed to develop
libblkid-based software.

%package -n libblkid-devel-static
Summary: Static block device id library
Group: Development/C
Requires: libblkid-devel = %version-%release
Requires: libuuid-devel-static

%description -n libblkid-devel-static
This package contains the library and include files needed to develop
statically linked libblkid-based software.

%package -n libuuid
Summary: Dynamic universally unique id library
Group: System/Libraries

%description -n libuuid
The uuid library generates and parses 128-bit universally unique id's
(UUID's).  See RFC 4122 for more information.

%package -n libuuid-devel
Summary: Development universally unique id library and include files
Group: Development/C
Requires: libuuid = %version-%release

%description -n libuuid-devel
This package contains the library and include files needed to develop
libuuid-based software.

%package -n libuuid-devel-static
Summary: Static block device id library
Group: Development/C
Requires: libuuid-devel = %version-%release

%description -n libuuid-devel-static
This package contains the library and include files needed to develop
statically linked libuuid-based software.

%package -n libmount
Summary: Device mounting library
Group: System/Libraries
Requires: libblkid = %version-%release

%description -n libmount
This is the device mounting library, part of util-linux-ng.

%package -n libmount-devel
Summary: Device mounting library
Group: Development/C
Requires: libmount = %version-%release

%description -n libmount-devel
This is the device mounting development library and headers,
part of util-linux-ng.

%package -n libmount-devel-static
Summary: Device mounting static library
Group: Development/C
Requires: libmount-devel = %version-%release

%description -n libmount-devel-static
This is the device mounting development static library.

%package -n libsmartcols
Summary: table or tree library
Group: System/Libraries

%description -n libsmartcols
The libsmartcols library is used for smart adaptive formatting of tabular data.

%package -n libsmartcols-devel
Summary: table or tree library
Group: Development/C
Requires: libsmartcols = %version-%release

%description -n libsmartcols-devel
This is the smartcols development library and headers,
part of util-linux-ng.

%package -n libsmartcols-devel-static
Summary: Table or tree static library
Group: Development/C
Requires: libsmartcols-devel = %version-%release

%description -n libsmartcols-devel-static
This is the smartcols development static library.

%package -n libfdisk
Summary: Partitioning library for fdisk-like programs.
Group: System/Libraries
License: LGPLv2+

%description -n libfdisk
This is library for fdisk-like programs, part of util-linux.

%package -n libfdisk-devel
Summary:  Partitioning library for fdisk-like programs.
Group: Development/C
License: LGPLv2+
Requires: libfdisk = %version-%release
Requires: pkgconfig

%description -n libfdisk-devel
This is development library and headers for fdisk-like programs,
part of util-linux.

%package -n libfdisk-devel-static
Summary:  Partitioning library for fdisk-like programs.
Group: Development/C
License: LGPLv2+
Requires: libfdisk = %version-%release
Requires: pkgconfig

%description -n libfdisk-devel-static
This is development static library for fdisk-like programs,
part of util-linux.

%package -n bash-completion-%name
Summary: Bash completion for %name utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %version-%release

%description -n bash-completion-%name
Bash completion for %name.

%prep
%setup -q
cp -r -- %SOURCE8 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 .

%patch5 -p1

%patch41 -p1 -b .write

%patch50 -p1
%patch51 -p2 -b .pamconsole
%patch52 -p1
%patch54 -p1
%patch59 -p2
%patch60 -p1
%patch61 -p1

%if_without systemd
%patch70 -p1
%endif

%patch71 -p2
%patch72 -p2

echo %version > .tarball-version

mkdir -p rpm
cp -- %SOURCE7 rpm/

%build
#add_optflags %(getconf LFS_CFLAGS) -D_LARGEFILE64_SOURCE
export SUID_CFLAGS="-fpie"
export SUID_LDFLAGS="-pie"
export HAS_GTKDOC=1
export runstatedir="%_runtimedir"

po/update-potfiles
autopoint --force
libtoolize --force
aclocal --force -I m4
autoconf --force
autoheader --force
automake --add-missing --force-missing

%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--disable-kill \
	--disable-wall \
	--disable-arch \
	--disable-last \
	--disable-mesg \
	--disable-chfn-chsh \
	--disable-pylibmount \
	--without-python \
	--enable-partx \
	--enable-write \
	--enable-rdev \
	%{subst_enable raw} \
	%{subst_enable runuser} \
	%{subst_enable login} \
	%{subst_enable sulogin} \
	%{subst_enable su} \
	%{?_enable_chfn_chsh:--enable-chfn-chsh} \
	%{subst_enable newgrp} \
	%{subst_enable vipw} \
	%{subst_enable schedutils} \
	--enable-libsmartcols \
	--enable-libblkid \
	--enable-libuuid \
	%{subst_enable fsck} \
	%{subst_enable uuidd} \
	%{subst_with udev} \
	%{subst_with selinux} \
	%{subst_with audit} \
	%{subst_with systemd} \
	%{subst_enable line} \
	%{subst_enable mountpoint} \
	%{subst_enable eject} \
	--enable-ddate \
	--disable-makeinstall-chown

# build util-linux-ng
%make_build

%ifarch %ix86 x86_64
%__cc %optflags stacktest.c -o stacktest
%endif

# build nologin
%ifarch %arm %e2k
%__cc -static \
	-Wall -Wextra -Werror nologin.c -o nologin
%else
klcc \
	-Wall -Wextra -Werror nologin.c -o nologin
%endif

%__cc %optflags clock_unsynced.c -o clock_unsynced
%__cc %optflags pause.c -o pause


%check
# cal: broken.
# mount, swapon: required real root and ignored in hasher.
# ipcs/limits*: failed in hasher.
# lsblk: 'failed to access sysfs directory: /sys/dev/block: No such file or directory' in hasher.
rm -rf tests/ts/{cal,fincore,login,look,ipcs/limits*,libmount/{lock,utils},lsblk,misc/{setarch,ionice},more/regexp}
LANG=C %make check-local-tests

%install
mkdir -p %buildroot/{bin,sbin,etc/pam.d}
mkdir -p %buildroot/{%_bindir,%_sbindir,%_libdir,%_infodir,%_mandir/man{1,6,5,8}}

# install util-linux-ng
%make_install install DESTDIR=%buildroot

install -pD -m755 %SOURCE5 %buildroot%_controldir/mount
install -pD -m755 %SOURCE6 %buildroot%_controldir/write

%ifarch %ix86 x86_64
install -p -m755 stacktest %buildroot/%_bindir
%endif
install -p -m755 pause %buildroot/%_bindir
install -p -m755 nologin %buildroot/sbin/
install -p -m644 nologin.8 %buildroot/%_man8dir/

%if_enabled raw
echo '.so man8/raw.8' > %buildroot/%_man8dir/rawdevices.8
ln -sf ../../bin/raw %buildroot/%_bindir/raw
%endif

%if_enabled runuser
	install -m 644 %SOURCE2 %buildroot/%_sysconfdir/pam.d/runuser
	install -m 644 %SOURCE3 %buildroot/%_sysconfdir/pam.d/runuser-l
%endif
%if_enabled chfn_chsh
	chmod 4711 %buildroot/%_bindir/{ch{sh,fn}
	install -m 644 %SOURCE4 %buildroot/%_sysconfdir/pam.d/chsh
	install -m 644 %SOURCE4 %buildroot/%_sysconfdir/pam.d/chfn
%endif
%if_enabled newgrp
	chmod 4711 %buildroot/%_bindir/newgrp
%endif

	install -pD -m755 clock_unsynced %buildroot/bin/clock_unsynced
	ln -sf ../../sbin/hwclock %buildroot/%_sbindir/hwclock
	ln -sf hwclock %buildroot/sbin/clock
	mkdir -p -- %buildroot/%_localstatedir/hwclock
	install -pD -m644 /dev/null %buildroot/%_localstatedir/hwclock/lastdate
	install -pD -m644 /dev/null %buildroot/%_sysconfdir/adjtime

# deprecated commands
for prog in \
	/sbin/fsck.minix /sbin/mkfs.{bfs,minix} /sbin/sln /sbin/shutdown /bin/kill \
	%_bindir/newgrp \
	\
	%_man1dir/newgrp.1 \
	%_man8dir/fsck.minix.8 %_man8dir/mkfs.minix.8 %_man8dir/mkfs.bfs.8 \
	\
	%_datadir/getopt;
do
	rm -rf -- %buildroot/$prog
done

# we install getopt/getopt-*.{bash,tcsh} as doc files
chmod 644 misc-utils/getopt-*.{bash,tcsh}

# Relocate shared libraries from %_libdir/ to /%_lib/. 
mkdir -p -- %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# /sbin -> /usr/sbin
for I in cfdisk; do
	[ ! -e %buildroot/sbin/$I ] ||
		mv -- %buildroot/sbin/$I %buildroot/%_sbindir/$I
done

# /usr/sbin -> /sbin
for I in addpart delpart partx; do
	[ ! -e %buildroot/%_sbindir/$I ] ||
		mv -- %buildroot/%_sbindir/$I %buildroot/sbin/$I
done

# /usr/bin -> /bin
for I in getopt taskset; do
	[ -e %buildroot/%_bindir/$I ] ||
		continue
	mv -- %buildroot/%_bindir/$I %buildroot/bin/$I
	path="$(relative "%buildroot/bin/$I" "%buildroot/%_bindir/$I")"
	ln -s "$path" %buildroot/%_bindir/$I
done

# /sbin -> /bin
for I in raw; do
	[ ! -e %buildroot/sbin/$I ] ||
		mv -- %buildroot/sbin/$I %buildroot/bin/$I
done

%if_without systemd
install -pD -m644 sys-utils/fstrim.timer   %buildroot/%_unitdir/fstrim.timer
sed 's,@sbindir@,/sbin,' < sys-utils/fstrim.service.in > %buildroot/%_unitdir/fstrim.service
%endif

LINKS="linux32 linux64"
%ifarch s390 s390x
	LINKS="$LINKS s390 s390x"
%endif
%ifarch %ix86 x86_64 amd64 ia32e
	LINKS="$LINKS i386 i486 i586 i686 x86_64"
%endif
%ifarch ppc ppc64
	LINKS="$LINKS ppc ppc64 ppc32"
%endif
%ifarch sparc sparc64
	LINKS="$LINKS sparc sparc64 sparc32"
%endif
%ifarch mips mips64
	LINKS="$LINKS mips mips64 mips32"
%endif
%ifarch ia64
	LINKS="$LINKS i386 ia64"
%endif

exclude_archs='setarch'
for i in $LINKS; do
	exclude_archs="$exclude_archs|$i"

%if_with setarch
	ln -sf -- setarch %buildroot/%_bindir/$i
	echo '.so man8/setarch.8' > %buildroot/%_man8dir/$i.8
	
	echo "%_bindir/$i"
	echo "%_man8dir/$i.8.*"
%endif #with setarch
done > setarch.files

%if_enabled uuidd
	:> uuidd.files

	ls -1 %buildroot/%_sbindir |
		egrep '^uuidd$' |
		sed -e 's|^\(.*\)$|%%_sbindir/\1|g' \
		>> uuidd.files

	ls -1 %buildroot%_man8dir |
		egrep '^uuidd\.' |
		sed -e 's|^\(.*\)$|%%_man8dir/\1*|g' \
		>> uuidd.files

	ls -1 %buildroot%_unitdir |
		egrep '^uuidd\.*' |
		sed -e 's|^\(.*\)$|%%_unitdir/\1|g' \
		>> uuidd.files

%endif #enabled uuidd

{
	# bindir
	ls -1 %buildroot/%_bindir |
		egrep -v "^($exclude_archs)\$" |
		egrep -v '^(eject|write|getopt|look|taskset|chrt|ionice)$' |
		sed -e 's|^\(.*\)$|%%_bindir/\1|g'

	# sbindir
	ls -1 %buildroot/%_sbindir |
		egrep -v '(fdisk|hwclock|uuidd|rfkill)' |
    		sed -e 's|^\(.*\)$|%%_sbindir/\1|g'

	# man1dir
	ls -1 %buildroot%_man1dir |
		egrep -v '^(eject|getopt|login|look|taskset|chrt|ionice)' |
		sed -e 's|^\(.*\)$|%%_man1dir/\1*|g'

	# man5dir
	ls -1 %buildroot%_man5dir |
		egrep    '^(terminal-colors\.d)' |
		sed -e 's|^\(.*\)$|%%_man5dir/\1*|g'

	# man8dir
	ls -1 %buildroot%_man8dir |
		egrep -v "^($exclude_archs)\.8*\$" |
		egrep -v '(mount|^swapo|losetup|lsblk|clock|getty|fdisk|part|uuidd|rfkill)' |
		sed -e 's|^\(.*\)$|%%_man8dir/\1*|g'

	# unitdir
	ls -1 %buildroot%_unitdir |
		egrep -e '^(fstrim\.*)' |
		sed -e 's|^\(.*\)$|%%_unitdir/\1|g'

	# /bin
	ls -1 %buildroot/bin |
		egrep -v '(getopt|login|lsblk|mount|taskset|clock_unsynced)' |
		sed -e 's|^\(.*\)$|/bin/\1|g'

	# /sbin
	ls -1 %buildroot/sbin |
		egrep -v '(^swapo|^losetup|addpart|delpart|partx|clock|getty|fdisk)' |
		sed -e 's|^\(.*\)$|/sbin/\1|g'
} > %name.files

ln -s /proc/mounts %buildroot/etc/mtab

# omit info/dir file
rm -f -- %buildroot/%_infodir/dir

# remove getopt docs
rm -rf -- %buildroot/%_defaultdocdir/%name/getopt

mkdir -p %buildroot/lib/tmpfiles.d
cat > %buildroot/lib/tmpfiles.d/losetup-loop.conf <<EOF
b /dev/loop0 0660 root disk - 7:0
b /dev/loop1 0660 root disk - 7:1
b /dev/loop2 0660 root disk - 7:2
b /dev/loop3 0660 root disk - 7:3
EOF

# find MO files
%find_lang %name
cat %name.lang >> %name.files

%triggerpostun -n hwclock -- startup <= 0.6-alt1, initscripts < 1:5.49.1-alt1
f=%_sysconfdir/adjtime
if [ ! -f "$f" ]; then
    if [ -f "$f".rpmsave ]; then
        cp -pf "$f".rpmsave "$f"
    elif [ -f "$f".rpmnew ]; then
        cp -pf "$f".rpmnew "$f"
    fi
fi

%pre
%pre_control write

%post
%post_control write

%pre -n mount
%pre_control mount

%post -n mount
%post_control mount

%files control
%config %_controldir/mount
%config %_controldir/write

%files -n lsblk
/bin/lsblk
%_man8dir/lsblk.*

%files -n mount
/etc/mtab
/bin/*mount
/sbin/swapo*
%_man5dir/fstab.*
%_man8dir/*mount*
%_man8dir/swapo*

%files -n losetup
/sbin/losetup
%_man8dir/losetup*
/lib/tmpfiles.d/losetup-loop.conf

%files -n hwclock
%config(noreplace) %_sysconfdir/adjtime
%config(noreplace) %_localstatedir/hwclock/lastdate
/bin/clock_unsynced
/sbin/*clock
%_sbindir/hwclock
%dir %_localstatedir/hwclock
%_man5dir/adjtime_config.5*
%_man8dir/*clock.*
%doc Documentation/hwclock.txt

%files -n getopt
/bin/getopt
%_bindir/getopt
%_man1dir/getopt.*
%doc misc-utils/getopt-*.{bash,tcsh}

%files -n agetty
/sbin/agetty
%_man8dir/agetty.*
%doc Documentation/modems-with-agetty.txt

%files -n cfdisk
%_sbindir/cfdisk
%_man8dir/cfdisk.*

%files -n fdisk
/sbin/fdisk
/sbin/*part*
%_man8dir/fdisk.*
%_man8dir/*part*.*

%files -n sfdisk
/sbin/sfdisk
%_man8dir/sfdisk.*

%files -n look
%_bindir/look
%_man1dir/look.*

%files -n rfkill
%_sbindir/rfkill
%_man8dir/rfkill.*

%if_enabled login
%files -n login
/bin/login
%_man8dir/login.8*
%config(noreplace) %_sysconfdir/pam.d/login
%config(noreplace) %_sysconfdir/pam.d/ch??
%endif #enabled login

%if_enabled schedutils
%files -n schedutils
/bin/taskset
%_bindir/chrt
%_bindir/ionice
%_bindir/taskset
%_man1dir/chrt.*
%_man1dir/ionice.*
%_man1dir/taskset.*
%endif #enabled schedutils

%if_with setarch
%files -n setarch -f setarch.files
%_bindir/setarch
%_man8dir/setarch.*
%endif #with setarch

%if_enabled eject
%files -n eject
%_bindir/eject
%_man1dir/eject.1*
%endif #enabled eject

%files -n libblkid
/%_lib/libblkid.so.*

%files -n libblkid-devel
%_includedir/blkid
%_pkgconfigdir/blkid.pc
%_libdir/libblkid.so
%_man3dir/libblkid.*

%files -n libblkid-devel-static
%_libdir/libblkid.a

%files -n libuuid
/%_lib/libuuid.so.*

%files -n libuuid-devel
%_includedir/uuid
%_pkgconfigdir/uuid.pc
%_libdir/libuuid.so
%_man3dir/uuid*

%files -n libuuid-devel-static
%_libdir/libuuid.a

%if_enabled uuidd
%files -n uuidd -f uuidd.files
%endif #with uuidd

%files -n libmount
/%_lib/libmount.so.*

%files -n libmount-devel
%_includedir/libmount
%_libdir/libmount.so
%_pkgconfigdir/mount.pc

%files -n libmount-devel-static
%_libdir/libmount.a

%files -n libsmartcols
/%_lib/libsmartcols.so.*

%files -n libsmartcols-devel
%_includedir/libsmartcols
%_libdir/libsmartcols.so
%_pkgconfigdir/smartcols.pc

%files -n libsmartcols-devel-static
%_libdir/libsmartcols.a

%files -n libfdisk
/%_lib/libfdisk.so.*

%files -n libfdisk-devel
%_includedir/libfdisk
%_libdir/libfdisk.so
%_pkgconfigdir/fdisk.pc

%files -n libfdisk-devel-static
%_libdir/libfdisk.a

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%files -f %name.files
%if_enabled runuser
%config(noreplace) %_sysconfdir/pam.d/runuser
%config(noreplace) %_sysconfdir/pam.d/runuser-l
%endif
%attr(2711,root,tty) %_bindir/write
%doc Documentation/*.txt NEWS AUTHORS README* Documentation/licenses/* Documentation/TODO

%changelog
* Thu Jun 25 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.33.2-alt2
- backported:
  + Build nologin with glibc on armh.
  + setarch: add arm and aarch64 architectures.

* Thu Apr 11 2019 Alexey Gladkov <legion@altlinux.ru> 2.33.2-alt1
- New version (2.33.2).
- Obsolete util-linux-initramfs.
- Fix build on %%e2k.

* Tue Apr 09 2019 Alexey Gladkov <legion@altlinux.ru> 2.33.1-alt1
- New version (2.33.1).

* Wed Jun 06 2018 Alexey Gladkov <legion@altlinux.ru> 2.32-alt2
- Add runuser.

* Thu Mar 29 2018 Alexey Gladkov <legion@altlinux.ru> 2.32-alt1
- New version (2.32).
- New subpackage rfkill.

* Mon Oct 16 2017 Alexey Gladkov <legion@altlinux.ru> 2.30.2-alt1
- New version (2.30.2).

* Sun Apr 02 2017 Alexey Gladkov <legion@altlinux.ru> 2.29.2-alt1
- New version (2.29.2).
- Fix `blkid -v` exit code (ALT#29544).
- Add fstrim service/timer (ALT#32687).
- Cleanup logger man-page (ALT#33152).

* Thu Nov 17 2016 Alexey Gladkov <legion@altlinux.ru> 2.29.0-alt1
- New version (2.29).

* Tue Aug 16 2016 Alexey Gladkov <legion@altlinux.ru> 2.28.1-alt1
- New version (2.28.1).
- Remove /lib/udev/devices/loop{0,1,2,3} (ALT#31890).

* Mon Dec 07 2015 Alexey Gladkov <legion@altlinux.ru> 2.27.1-alt2
- Add uuidd subpackage.

* Mon Nov 16 2015 Alexey Gladkov <legion@altlinux.ru> 2.27.1-alt1
- New version (2.27.1).
- Remove explicit nfs-utils requirement (ALT#31498).
- Rewrite pause in a portable way (thx: glebfm@).

* Sun May 03 2015 Alexey Gladkov <legion@altlinux.ru> 2.26.2-alt1
- New version (2.26.2).
- Add libsmartcols, libfdisk.

* Sun Nov 02 2014 Alexey Gladkov <legion@altlinux.ru> 2.25.2-alt1
- New version (2.25.2).
- Use tarballs to import upstream sources.

* Tue Apr 02 2013 Alexey Gladkov <legion@altlinux.ru> 2.22.1-alt1
- New version (2.22.1).

* Thu Nov 15 2012 Alexey Gladkov <legion@altlinux.ru> 2.22-alt4
- libmount: fix support of comma-separated fs types lists (thx: glebfm@) (ALT#27942).

* Mon Oct 08 2012 Alexey Gladkov <legion@altlinux.ru> 2.22-alt3
- Move lsblk to subpackage.
- Remove util-linux-60-raw.rules (moved to udev-rules).

* Wed Sep 26 2012 Alexey Gladkov <legion@altlinux.ru> 2.22-alt2
- Fix regression in previous release ('pamconsole' mount option
  has been silently lost).
- Fix device type and permissions in losetup-loop.conf (ALT#27767).

* Wed Sep 12 2012 Alexey Shabalin <shaba@altlinux.ru> 2.22-alt1
- 2.22
- Add strict dependency on libmount to mount.
- Add eject subpackage, but disable.
- Drop conditions for hwclock.
- Update configure options.
- Update fedora patches.

* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.org> 2.20.1-alt2
- add /lib/tmpfiles.d/losetup-loop.conf for create character devices
  /dev/loop{0-4}.

* Fri Jan 27 2012 Alexey Gladkov <legion@altlinux.ru> 2.20.1-alt1
- New version (2.20.1).
- libmount: unable to umount nfs shares using the force option (ALT#26576).

* Tue Aug 30 2011 Alexey Gladkov <legion@altlinux.ru> 2.20.0-alt2
- Update fedora patches.

* Mon Aug 29 2011 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- New version (2.20).

* Thu Aug 18 2011 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt0.2
- New version (2.20-rc2).

* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 2.19.1-alt4.20110512
- New snapshot (2.19.1 20110512).
- Revert "configure.ac: version generation changed to subst template"
- drop unneeded define "with_nfsv4"
- drop Requires: nfs-utils for mount package
- legion@:
  + New snapshot (2.19.1 20110511).
  + Remove util-linux-initramfs subpackage.
  + Fix version definition.
  + losetup: Add /lib/udev/devices/loop[0-3] devices.
  + selinux: Use pkgconfig.

* Tue May 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.19.1-alt2
- version substitution in configure.ac added

* Thu May 05 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.19.1-alt1
- new version
- add static /lib/udev/devices/loop[0-3] devices (vitty@)

* Wed May 04 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.19.0-alt4.20110215
- fixed double multiplication in addpart

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 2.19.0-alt3.20110215
- /etc/mtab as symlink to /proc/mounts
- build with selinux support
- build with audit support

* Thu Feb 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.19.0-alt2.20110215
- build to sisyphus

* Tue Feb 15 2011 Alexey Gladkov <legion@altlinux.ru> 2.19.0-alt1.20110215
- New snapshot (2.19 20110215).
- Remove conditions to disable blkid and uuid.
- agetty: Add altlinux-specific '\R' special char (ALT#24987).
- unshare: SIGSEGV on invalid command line option (ALT#24856).
- raw incompatible with udev (ALT#11204).

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 2.18.0-alt2.20101027
- rebuilt for debuginfo
- enabled strict dependencies between subpackages
- linked cfdisk with libncursesw instead of plain ncurses

* Wed Oct 27 2010 Alexey Gladkov <legion@altlinux.ru> 2.18.0-alt1.20101027
- New snapshot (2.18 20101027).
- Add libmount subpackage.

* Fri Apr 30 2010 Alexey Gladkov <legion@altlinux.ru> 2.17.2-alt1
- New version (2.17.2).
- Add scriptreplay utility (ALT#23170).

* Sun Feb 28 2010 Alexey Gladkov <legion@altlinux.ru> 2.17.1-alt1
- New version (2.17.1).
- Remove support for --rmpart[s] from blockdev(8).

* Tue Nov 17 2009 Alexey Gladkov <legion@altlinux.ru> 2.16.1-alt3
- Add util-linux-initramfs subpackage.

* Sat Nov 14 2009 Alexey Gladkov <legion@altlinux.ru> 2.16.1-alt2
- Enable fsck, libblkid and libuuid.

* Fri Sep 11 2009 Alexey Gladkov <legion@altlinux.ru> 2.16.1-alt1
- New version (2.16.1).
- Disable fsck, libuuid and libblkid for a while.
- Add tests.

* Sun Jul 12 2009 Alexey Gladkov <legion@altlinux.ru> 2.16-alt0.2
- New version (2.16-rc2).
- The libuuid library has been moved from e2fsprogs to util-linux-ng.

* Tue May 12 2009 Alexey Gladkov <legion@altlinux.ru> 2.15-alt2
- New version (2.15).
- The libblkid library has been moved from e2fsprogs to util-linux-ng.

* Thu Apr 02 2009 Alexey Gladkov <legion@altlinux.ru> 2.15-alt1
- New upstream stapshot (2.15 rc1 20090402).

* Sun Jan 25 2009 Alexey Gladkov <legion@altlinux.ru> 2.14.1-alt1
- New version (2.14.1).
- Move %_sbindir/hwclock to hwclock subpackage (Dmitry V. Levin).
- Move control files to separate subpackage (Dmitry V. Levin).
- mount.control: Add "unprivileged" mode (Dmitry V. Levin).
- Resurrect mount control %pre/%post scripts(Dmitry V. Levin).
- flock: Allow lock directory.

* Wed Jul 30 2008 Alexey Gladkov <legion@altlinux.ru> 2.14-alt1
- New version (2.14).
- Build hwclock subpackage:
  + Add clock_unsynced utiltiy from hwclock-2.24-alt2.
- mount:
  + Allow users at console to mount (pamconsole fstab option).

* Sun Mar 30 2008 Alexey Gladkov <legion@altlinux.ru> 2.13-alt8
- Increase getopt version up to util-linux version.
- Remove schedutils files from util-linux subpackage.

* Tue Mar 25 2008 Alexey Gladkov <legion@altlinux.ru> 2.13-alt7
- Move /usr/bin/getopt to /bin/getopt.

* Mon Mar 24 2008 Alexey Gladkov <legion@altlinux.ru> 2.13-alt6
- New upstream stapshot.
- Exclude /bin/arch from util-linux.
- Enable build schedutils (closes #13924, #14670) and getopt packages.
- nologin statically linked with klibc.

* Sun Nov 25 2007 Alexey Gladkov <legion@altlinux.ru> 2.13-alt5
- New upstream stapshot.
- Fix buildrequires.

* Mon Nov 19 2007 Alexey Gladkov <legion@altlinux.ru> 2.13-alt4
- Rename util-linux-ng back to util-linux.
- pause: rewritten in C for portability reason (kas@).
- stacktest: compile only on %%ix86 and x86_64 due inline assembler (kas@).

* Fri Nov 16 2007 Alexey Gladkov <legion@altlinux.ru> 2.13-alt3
- Add compatibility with old setarch utility.

* Mon Nov 12 2007 Alexey Gladkov <legion@altlinux.ru> 2.13-alt2
- New util-linux-ng snapshot.

* Tue Sep 11 2007 Alexey Gladkov <legion@altlinux.ru> 2.13-alt1
- New version for ALT Linux.

* Tue Aug 28 2007 Karel Zak <kzak@redhat.com> 2.13-1
- upgrade to stable util-linux-ng release

* Fri Aug 24 2007 Karel Zak <kzak@redhat.com> 2.13-0.59
- add release number to util-linux Provides and increment setarch Obsoletes
- fix #254114 - spec typo
- upgrade to floppy-0.16
- add BuildRequires: popt-devel

* Wed Aug 22 2007 Jesse Keating <jkeating@redhat.com>  2.13-0.58
- Obsolete a sufficiently high enough version of setarch

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com>  2.13-0.57
- fix #253664 - util-linux-ng fails to build on sparc (patch by Dennis Gilmore)
- rebase to new GIT snapshot

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com> 2.13-0.56
- fix obsoletes field

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com> 2.13-0.55
- util-linux-ng includes setarch(1), define relevat Obsoletes+Provides

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com> 2.13-0.54
- port "blockdev --rmpart" patch from util-linux
- use same Provides/Obsoletes setting like in util-linux

* Wed Aug 15 2007 Karel Zak <kzak@redhat.com> 2.13-0.53
- fix #252046 - review Request: util-linux-ng (util-linux replacement)

* Mon Aug 13 2007 Karel Zak <kzak@redhat.com> 2.13-0.52
- rebase to util-linux-ng (new util-linux upstream fork,
		based on util-linux 2.13-pre7)
- more than 70 Fedora/RHEL patches have been merged to upstream code

* Fri Apr  6 2007 Karel Zak <kzak@redhat.com> 2.13-0.51
- fix #150493 - hwclock --systohc sets clock 0.5 seconds slow
- fix #220873 - starting RPC idmapd: Error: RPC MTAB does not exist.
		(added rpc_pipefs to util-linux-2.13-umount-sysfs.patch)
- fix #227903 - mount -f does not work with NFS-mounted

* Sat Mar  3 2007 David Zeuthen <davidz@redhat.com> 2.13-0.50
- include ConsoleKit session module by default (#229172)

* Thu Jan 11 2007 Karel Zak <kzak@redhat.com> 2.13-0.49
- fix #222293 - undocumented partx,addpart, delpart

* Sun Dec 17 2006 Karel Zak <kzak@redhat.com> 2.13-0.48
- fix paths in po/Makefile.in.in

* Fri Dec 15 2006 Karel Zak <kzak@redhat.com> 2.13-0.47
- fix #217240 - namei ignores non-directory components instead of saying "Not a directory"
- fix #217241 - namei enforces symlink limits inconsistently

* Wed Dec 14 2006 Karel Zak <kzak@redhat.com> 2.13-0.46
- fix leaking file descriptor in the more command (patch by Steve Grubb)

* Wed Dec 13 2006 Karel Zak <kzak@redhat.com> 2.13-0.45
- use ncurses only
- fix #218915 - fdisk -b 4K
- upgrade to -pre7 release
- fix building problem with raw0 patch
- fix #217186 - /bin/sh: @MKINSTALLDIRS@: No such file or directory 
  (port po/Makefile.in.in from gettext-0.16)
- sync with FC6 and RHEL5:
- fix #216489 - SCHED_BATCH option missing in chrt
- fix #216712 - issues with raw device support ("raw0" is wrong device name)
- fix #216760 - mount with context or fscontext option fails
  (temporarily disabled the support for additional contexts -- not supported by kernel yet)
- fix #211827 - Can't mount with additional contexts
- fix #213127 - mount --make-unbindable does not work
- fix #211749 - add -r option to losetup to create a read-only loop

* Thu Oct 12 2006 Karel Zak <kzak@redhat.com> 2.13-0.44
- fix #209911 - losetup.8 updated (use dm-crypt rather than deprecated cryptoloop)
- fix #210338 - spurious error from '/bin/login -h $PHONENUMBER' (bug in IPv6 patch)
- fix #208634 - mkswap "works" without warning on a mounted device

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.43
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Karel Zak <kzak@redhat.com> 2.13-0.42
- remove obsolete NFS code and patches (we use /sbin/mount.nfs
  and /sbin/umount.nfs from nfs-utils now)
- move nfs.5 to nfs-utils

* Fri Sep 15 2006 Karel Zak <kzak@redhat.com> 2.13-0.41
- fix #205038 - mount not allowing sloppy option (exports "-s"
  to external /sbin/mount.nfs(4) calls) 
- fix minor bug in util-linux-2.13-mount-twiceloop.patch
- fix #188193- util-linux should provide plugin infrastructure for HAL

* Mon Aug 21 2006 Karel Zak <kzak@redhat.com> 2.13-0.40
- fix Makefile.am in util-linux-2.13-mount-context.patch
- fix #201343 - pam_securetty requires known user to work
		(split PAM login configuration to two files)
- fix #203358 - change location of taskset binary to allow for early affinity work

* Fri Aug 11 2006 Karel Zak <kzak@redhat.com> 2.13-0.39
- fix #199745 - non-existant simpleinit(8) mentioned in ctrlaltdel(8)

* Thu Aug 10 2006 Dan Walsh <dwalsh@redhat.com> 2.13-0.38
- Change keycreate line to happen after pam_selinux open call so it gets correct context

* Thu Aug 10 2006 Karel Zak <kzak@redhat.com> 2.13-0.37
- fix #176494 - last -i returns strange IP addresses (patch by Bill Nottingham)

* Thu Jul 27 2006 Karel Zak <kzak@redhat.com> 2.13-0.36
- fix #198300, #199557 - util-linux "post" scriptlet failure

* Thu Jul 27 2006 Steve Dickson <steved@redhat.com> 2.13-0.35
- Added the -o fsc flag to nfsmount.

* Wed Jul 26 2006 Karel Zak <kzak@redhat.com> 2.13-0.34
- rebuild

* Tue Jul 18 2006 Karel Zak <kzak@redhat.com> 2.13-0.33
- add Requires(post): libselinux

* Mon Jul 17 2006 Karel Zak <kzak@redhat.com> 2.13-0.32
- add IPv6 support to the login command (patch by Milan Zazrivec)
- fix #198626 - add keyinit instructions to the login PAM script 
  (patch by David Howells) 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.31.1
- rebuild

* Tue Jul 11 2006 Karel Zak <kzak@redhat.com> 2.13-0.31
- cleanup dependences for post and preun scriptlets

* Mon Jul 10 2006 Karsten Hopp <karsten@redhat.de> 2.13-0.30
- silence install in minimal buildroot without /var/log

* Fri Jul  7 2006 Karel Zak <kzak@redhat.com> 2.13-0.29 
- include the raw command for RHELs

* Mon Jun 26 2006 Florian La Roche <laroche@redhat.com> 2.13-0.28
- move install-info parts from postun to preun

* Wed Jun 21 2006 Dan Walsh <dwalsh@RedHat.com> 2.13-0.27
- Only execute chcon on machines with selinux enabled

* Wed Jun 14 2006 Steve Dickson <steved@redhat.com> 2.13-0.26
- Remove unneeded header files from nfsmount.c

* Mon Jun 12 2006 Karel Zak <kzak@redhat.com> 2.13-0.25
- fix #187014 - umount segfaults for normal user
- fix #183446 - cal not UTF-8-aware
- fix #186915 - mount does not translate SELIinux context options though libselinux
- fix #185500 - Need man page entry for -o context= mount option
- fix #152579 - missing info about /etc/mtab and /proc/mounts mismatch
- fix #183890 - missing info about possible ioctl() and fcntl() problems on NFS filesystem
- fix #191230 - using mount --move results in wrong data in /etc/mtab
- added mount subtrees support
- fdisk: wrong number of sectors for large disks (suse#160822)
- merge fdisk-xvd (#182553) with new fdisk-isfull (#188981) patch 
- fix #181549 - raw(8) manpage has old information about dd
- remove asm/page.h usage

* Wed May 24 2006 Dan Walsh <dwalsh@RedHat.com> 2.13-0.24
- Remove requirement on restorecon, since we can do the same thing
- with chcon/matchpathcon, and not add requirement on policycoreutils

* Wed May 24 2006 Steve Dickson <steved@redhat.com> 2.13-0.23
- Fixed bug in patch for bz183713 which cause nfs4 mounts to fail.

* Tue May  2 2006 Steve Dickson <steved@redhat.com> 2.13-0.22
- Added syslog logging to background mounts as suggested
  by a customer.

* Mon May  1 2006 Steve Dickson <steved@redhat.com> 2.13-0.21
- fix #183713 - foreground mounts are not retrying as advertised
- fix #151549 - Added 'noacl' mount flag
- fix #169042 - Changed nfsmount to try udp before using tcp when rpc-ing
		the remote rpc.mountd (iff -o tcp is not specified).
		This drastically increases the total number of tcp mounts
		that can happen at once (ala autofs).

* Wed Mar  9 2006 Jesse Keating <jkeating@redhat.com> 2.13-0.20
- Better calling of restorecon as suggested by Bill Nottingham
- prereq restorecon to avoid ordering issues

* Wed Mar  9 2006 Jesse Keating <jkeating@redhat.com> 2.13-0.19
- restorecon /var/log/lastlog

* Wed Mar  8 2006 Karel Zak <kzak@redhat.com> 2.13-0.17
- fix #181782 - mkswap selinux relabeling (fix util-linux-2.13-mkswap-selinux.patch)

* Wed Feb 22 2006 Karel Zak <kzak@redhat.com> 2.13-0.16
- fix #181782 - mkswap should automatically add selinux label to swapfile
- fix #180730 - col is exiting with 1 (fix util-linux-2.12p-col-EILSEQ.patch)
- fix #181896 - broken example in schedutils man pages
- fix #177331 - login omits pam_acct_mgmt & pam_chauthtok when authentication is skipped.
- fix #177523 - umount -a should not unmount sysfs
- fix #182553 - fdisk -l inside xen guest shows no disks

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.15.1
- bump again for double-long bug on ppc(64)

* Wed Feb  8 2006 Peter Jones <pjones@redhat.com> 2.13-0.15
- add "blockdev --rmpart N <device>" and "blockdev --rmparts <device>"

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.14.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Jan 19 2006 Steve Dickson <steved@redhat.com> 2.13-0.14
- Updated the gssd_check() and idmapd_check(), used with
  nfsv4 mounts, to looked for the correct file in /var/lock/subsys
  which stops bogus warnings. 

* Tue Jan  3 2006 Karel Zak <kzak@redhat.com> 2.13-0.13
- fix #174676 - hwclock audit return code mismatch
- fix #176441: col truncates data
- fix #174111 - mount allows loopback devices to be mounted more than once to the same mount point
- better wide chars usage in the cal command (based on the old 'moremisc' patch)

* Mon Dec 12 2005 Karel Zak <kzak@redhat.com> 2.13-0.12
- rebuilt

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 25 2005 Karel Zak <kzak@redhat.com> 2.13-0.11.pre6
- update to upstream version 2.13-pre6
- fix #172203 - mount man page in RHEL4 lacks any info on cifs mount options

* Mon Nov  7 2005 Karel Zak <kzak@redhat.com> 2.13-0.10.pre5
- fix #171337 - mkfs.cramfs doesn't work correctly with empty files

* Fri Oct 28 2005 Karel Zak <kzak@redhat.com> 2.13-0.9.pre5
- rebuild

* Wed Oct 26 2005 Karel Zak <kzak@redhat.com> 2.13-0.8.pre5
- updated version of the patch for hwclock audit

* Thu Oct 20 2005 Karel Zak <kzak@redhat.com> 2.13-0.7.pre5
- fix #171337 - mkfs.cramfs dies creating installer image

* Thu Oct 20 2005 Karel Zak <kzak@redhat.com> 2.13-0.6.pre5
- update to upstream 2.13pre5
- remove separated cramfs1.1 (already in upstream package)
- remove odd symlink /usr/bin/mkcramfs -> ../../sbin/mkfs.cramfs
- fix #170171 - ipcs -lm always report "max total shared memory (kbytes) = 0"

* Mon Oct 17 2005 Karel Zak <kzak@redhat.com> 2.13-0.5.pre4
* fix #170564 - add audit message to login

* Fri Oct  7 2005 Karel Zak <kzak@redhat.com> 2.13-0.4.pre4
- fix #169628 - /usr/bin/floppy doesn't work with /dev/fd0
- fix #168436 - login will attempt to run if it has no read/write access to its terminal
- fix #168434 - login's timeout can fail - needs to call siginterrupt(SIGALRM,1)
- fix #165253 - losetup missing option -a [new feature]
- update PAM files (replace pam_stack with new "include" PAM directive)
- remove kbdrate from src.rpm
- update to 2.13pre4

* Fri Oct  7 2005 Steve Dickson <steved@redhat.com> 2.13-0.3.pre3
- fix #170110 - Documentation for 'rsize' and 'wsize' NFS mount options
		is misleading

* Fri Sep  2 2005 Karel Zak <kzak@redhat.com> 2.13-0.3.pre2
- fix #166923 - hwclock will not run on a non audit-enabled kernel
- fix #159410 - mkswap(8) claims max swap area size is 2 GB
- fix #165863 - swsusp swaps should be reinitialized
- change /var/log/lastlog perms to 0644

* Tue Aug 16 2005 Karel Zak <kzak@redhat.com> 2.13-0.2.pre2
- /usr/share/misc/getopt/* -move-> /usr/share/doc/util-linux-2.13/getopt-*
- the arch command marked as deprecated
- removed: elvtune, rescuept and setfdprm
- removed: man8/sln.8 (moved to man-pages, see #10601)
- removed REDAME.pg and README.reset
- .spec file cleanup
- added schedutils (commands: chrt, ionice and taskset)

* Tue Jul 12 2005 Karel Zak <kzak@redhat.com> 2.12p-9.7
- fix #159339 - util-linux updates for new audit system
- fix #158737 - sfdisk warning for large partitions, gpt
- fix #150912 - Add ocfs2 support
- NULL is better than zero at end of execl()

* Thu Jun 16 2005 Karel Zak <kzak@redhat.com> 2.12p-9.5
- fix #157656 - CRM 546998: Possible bug in vipw, changes permissions of /etc/shadow and /etc/gshadow
- fix #159339 - util-linux updates for new audit system (pam_loginuid.so added to util-linux-selinux.pamd)
- fix #159418 - sfdisk unusable - crashes immediately on invocation
- fix #157674 - sync option on VFAT mount destroys flash drives
- fix .spec file /usr/sbin/{hwclock,clock} symlinks

* Wed May  4 2005 Jeremy Katz <katzj@redhat.com> - 2.12p-9.3
- rebuild against new libe2fsprogs (and libblkid) to fix cramfs auto-detection

* Mon May  2 2005 Karel Zak <kzak@redhat.com> 2.12p-9.2
- rebuild

* Mon May  2 2005 Karel Zak <kzak@redhat.com> 2.12p-9
- fix #156597 - look - doesn't work with separators

* Mon Apr 25 2005 Karel Zak <kzak@redhat.com> 2.12p-8
- fix #154498 - util-linux login & pam session
- fix #155293 - man 5 nfs should include vers as a mount option
- fix #76467 - At boot time, fsck chokes on LVs listed by label in fstab
- new Source URL
- added note about ATAPI IDE floppy to fdformat.8
- fix #145355 - Man pages for fstab and fstab-sync in conflict

* Tue Apr  5 2005 Karel Zak <kzak@redhat.com> 2.12p-7
- enable build with libblkid from e2fsprogs-devel
- remove workaround for duplicated labels

* Thu Mar 31 2005 Steve Dickson <SteveD@RedHat.com> 2.12p-5
- Fixed nfs mount to rollback correctly.

* Fri Mar 25 2005 Karel Zak <kzak@redhat.com> 2.12p-4
- added /var/log/lastlog to util-linux (#151635)
- disabled 'newgrp' in util-linux (enabled in shadow-utils) (#149997, #151613)
- improved mtab lock (#143118)
- fixed ipcs typo (#151156)
- implemented mount workaround for duplicated labels (#116300)

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com> 2.12p-3
- rebuilt

* Fri Feb 25 2005 Steve Dickson <SteveD@RedHat.com> 2.12p-2
- Changed nfsmount to only use reserve ports when necessary
  (bz# 141773) 

* Thu Dec 23 2004 Elliot Lee <sopwith@redhat.com> 2.12p-1
- Update to util-linux-2.12p. This changes swap header format
  from - you may need to rerun mkswap if you did a clean install of
  FC3.

* Fri Dec 10 2004 Elliot Lee <sopwith@redhat.com> 2.12j-1
- Update to util-linux-2.12j

* Tue Dec  7 2004 Steve Dickson <SteveD@RedHat.com> 2.12a-20
- Corrected a buffer overflow problem with nfs mounts.
  (bz# 141733) 

* Wed Dec 01 2004 Elliot Lee <sopwith@redhat.com> 2.12a-19
- Patches for various bugs.

* Mon Nov 29 2004 Steve Dickson <SteveD@RedHat.com> 2.12a-18
- Made NFS mounts adhere to the IP protocol if specified on
  command line as well as made NFS umounts adhere to the
  current IP protocol. Fix #140016

* Thu Oct 14 2004 Elliot Lee <sopwith@redhat.com> 2.12a-16
- Add include_raw macro, build with it off for Fedora

* Wed Oct 13 2004 Stephen C. Tweedie <sct@redhat.com> - 2.12a-15
- Add raw patch to allow binding of devices not yet in /dev

* Wed Oct 13 2004 John (J5) Palmieri <johnp@redhat.com> 2.12a-14
- Add David Zeuthen's patch to enable the pamconsole flag #133941

* Wed Oct 13 2004 Stephen C. Tweedie <sct@redhat.com> 2.12a-13
- Restore raw utils (bugzilla #130016)

* Mon Oct 11 2004 Phil Knirsch <pknirsch@redhat.com> 2.12a-12
- Add the missing remote entry in pam.d

* Wed Oct  6 2004 Steve Dickson <SteveD@RedHat.com>
- Rechecked in some missing NFS mounting code.

* Wed Sep 29 2004 Elliot Lee <sopwith@redhat.com> 2.12a-10
- Make swaplabel support work with swapon -a -e

* Tue Sep 28 2004 Steve Dickson <SteveD@RedHat.com>
- Updated the NFS and NFS4 code to the latest CITI patch set
  (in which they incorporate a number of our local patches).

* Wed Sep 15 2004 Nalin Dahybhai <nalin@redhat.com> 2.12a-8
- Fix #132196 - turn on SELinux support at build-time.

* Wed Sep 15 2004 Phil Knirsch <pknirsch@redhat.com> 2.12a-7
- Fix #91174 with pamstart.patch

* Tue Aug 31 2004 Elliot Lee <sopwith@redhat.com> 2.12a-6
- Fix #16415, #70616 with rdevman.patch
- Fix #102566 with loginman.patch
- Fix #104321 with rescuept.patch (just use plain lseek - we're in _FILE_OFFSET_BITS=64 land now)
- Fix #130016 - remove raw.
- Re-add agetty (replacing it with mgetty is too much pain, and mgetty is much larger)

* Thu Aug 26 2004 Steve Dickson <SteveD@RedHat.com>
- Made the NFS security checks more explicit to avoid confusion
  (an upstream fix)
- Also removed a compilation warning

* Wed Aug 11 2004 Alasdair Kergon <agk@redhat.com>
- Remove unused mount libdevmapper inclusion.

* Wed Aug 11 2004 Alasdair Kergon <agk@redhat.com>
- Add device-mapper mount-by-label support
- Fix segfault in mount-by-label when a device without a label is present.

* Wed Aug 11 2004 Steve Dickson <SteveD@RedHat.com>
- Updated nfs man page to show that intr are on by
  default for nfs4

* Thu Aug 05 2004 Jindrich Novy <jnovy@redhat.com>
- modified warning causing heart attack for >16 partitions, #107824

* Fri Jul 09 2004 Elliot Lee <sopwith@redhat.com> 2.12a-3
- Fix #126623, #126572
- Patch cleanup
- Remove agetty (use mgetty, agetty is broken)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 03 2004 Elliot Lee <sopwith@redhat.com> 2.12a-1
- Update to 2.12a
- Fix #122448

* Thu May 13 2004 Dan Walsh <dwalsh@RedHat.com> 2.12-19
- Change pam_selinux to run last

* Tue May 04 2004 Elliot Lee <sopwith@redhat.com> 2.12-18
- Fix #122448 (autofs issues)

* Fri Apr 23 2004 Elliot Lee <sopwith@redhat.com> 2.12-17
- Fix #119157 by editing the patch
- Add patch145 to fix #119986

* Fri Apr 16 2004 Elliot Lee <sopwith@redhat.com> 2.12-16
- Fix #118803

* Tue Mar 23 2004 Jeremy Katz <katzj@redhat.com> 2.12-15
- mkcramfs: use PAGE_SIZE for default blocksize (#118681)

* Sat Mar 20 2004 <SteveD@RedHat.com>
- Updated the nfs-mount.patch to correctly 
  handle the mounthost option and to ignore 
  servers that do not set auth flavors

* Tue Mar 16 2004 Dan Walsh <dwalsh@RedHat.com> 2.12-13
- Fix selinux ordering or pam for login

* Tue Mar 16 2004 <SteveD@RedHat.com>
- Make RPC error messages displayed with -v argument
- Added two checks to the nfs4 path what will print warnings
  when rpc.idmapd and rpc.gssd are not running
- Ping NFS v4 servers before diving into kernel
- Make v4 mount interruptible which also make the intr option on by default 

* Sun Mar 13 2004  <SteveD@RedHat.com>
- Reworked how the rpc.idmapd and rpc.gssd checks were
  done due to review comments from upstream.
- Added rpc_strerror() so the '-v' flag will show RPC errors.

* Sat Mar 13 2004  <SteveD@RedHat.com>
- Added two checks to the nfs4 path what will print warnings
  when rpc.idmapd and rpc.gssd are not running.

* Thu Mar 11 2004 <SteveD@RedHat.com>
- Reworked and updated the nfsv4 patches.

* Wed Mar 10 2004 Dan Walsh <dwalsh@RedHat.com>
- Bump version

* Wed Mar 10 2004 Steve Dickson <SteveD@RedHat.com>
- Tried to make nfs error message a bit more meaninful
- Cleaned up some warnings

* Sun Mar  7 2004 Steve Dickson <SteveD@RedHat.com> 
- Added pesudo flavors for nfsv4 mounts.
- Added BuildRequires: libselinux-devel and Requires: libselinux
  when WITH_SELINUX is set. 

* Fri Feb 27 2004 Dan Walsh <dwalsh@redhat.com> 2.12-5
- check for 2.6.3 kernel in mount options

* Mon Feb 23 2004 Elliot Lee <sopwith@redhat.com> 2.12-4
- Remove /bin/kill for #116100

* Fri Feb 20 2004 Dan Walsh <dwalsh@redhat.com> 2.12-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Elliot Lee <sopwith@redhat.com> 2.12-1
- Final 2.12 has been out for ages - might as well use it.

* Wed Jan 28 2004 Steve Dickson <SteveD@RedHat.com> 2.12pre-4
- Added mount patches that have NFS version 4 support

* Mon Jan 26 2004 Elliot Lee <sopwith@redhat.com> 2.12pre-3
- Provides: mount losetup

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 2.12pre-2
- Add multiple to /etc/pam.d/login for SELinux

* Thu Jan 15 2004 Elliot Lee <sopwith@redhat.com> 2.12pre-1
- 2.12pre-1
- Merge mount/losetup packages into the main package (#112324)
- Lose separate 

* Mon Nov 3 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-35.sel
- remove selinux code from login and use pam_selinux

* Thu Oct 30 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-34.sel
- turn on selinux

* Fri Oct 24 2003 Elliot Lee <sopwith@redhat.com> 2.11y-34
- Add BuildRequires: texinfo (from a bug# I don't remember)
- Fix #90588 with mountman patch142.

* Mon Oct 6 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-33
- turn off selinux

* Thu Sep 25 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-32.sel
- turn on selinux
- remove context selection

* Fri Sep 19 2003 Elliot Lee <sopwith@redhat.com> 2.11y-31
- Add patch140 (alldevs) to fix #101772. Printing the total size of
  all devices was deemed a lower priority than having all devices
  (e.g. /dev/ida/c0d9) displayed.

* Fri Sep 12 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-31
- turn off selinux

* Fri Sep 12 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-30.sel
- turn on selinux

* Fri Sep 5 2003 Elliot Lee <sopwith@redhat.com> 2.11y-28
- Fix #103004, #103954

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-27
- turn off selinux

* Thu Sep 4 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-26.sel
- build with selinux

* Mon Aug 11 2003 Elliot Lee <sopwith@redhat.com> 2.11y-25
- Use urandom instead for mkcramfs

* Tue Jul 29 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-24
- add SELINUX 2.5 support

* Wed Jul 23 2003 Elliot Lee <sopwith@redhat.com> 2.11y-22
- #100433 patch

* Mon Jun 14 2003 Elliot Lee <sopwith@redhat.com> 2.11y-20
- #97381 patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 21 2003 Elliot Lee <sopwith@redhat.com> 2.11y-17
- Change patch128 to improve ipcs -l

* Fri Apr 11 2003 Elliot Lee <sopwith@redhat.com> 2.11y-16
- Fix #85407

* Fri Apr 11 2003 Elliot Lee <sopwith@redhat.com> 2.11y-15
- Change patch128 to util-linux-2.11f-ipcs-84243-86285.patch to get all
ipcs fixes

* Thu Apr 10 2003 Matt Wilson <msw@redhat.com> 2.11y-14
- fix last login date display on AMD64 (#88574)

* Mon Apr  7 2003 Jeremy Katz <katzj@redhat.com> 2.11y-13
- include sfdisk on ppc

* Fri Mar 28 2003 Jeremy Katz <katzj@redhat.com> 2.11y-12
- add patch from msw to change mkcramfs blocksize with a command line option

* Tue Mar 25 2003 Phil Knirsch <pknirsch@redhat.com> 2.11y-11
- Fix segfault on s390x due to wrong usage of BLKGETSIZE.

* Thu Mar 13 2003 Elliot Lee <sopwith@redhat.com> 2.11y-10
- Really apply the ipcs patch. Doh.

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 19 2003 Elliot Lee <sopwith@redhat.com> 2.11y-8
- ipcs-84243.patch to fix #84243

* Thu Feb 13 2003 Yukihiro Nakai <ynakai@redhat.com> 2.11y-7
- Update moremisc patch to fix swprintf()'s minimum field (bug #83361).

* Mon Feb 03 2003 Elliot Lee <sopwith@redhat.com> 2.11y-6
- Fix mcookie segfault on many 64-bit architectures (bug #83345).

* Mon Feb 03 2003 Tim Waugh <twaugh@redhat.com> 2.11y-5
- Fix underlined multibyte characters (bug #83376).

* Sun Feb 02 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild to have again a s390 rpm
- disable some more apps for mainframe

* Wed Jan 29 2003 Elliot Lee <sopwith@redhat.com> 2.11y-4
- util-linux-2.11y-umask-82552.patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Elliot Lee <sopwith@redhat.com> 2.11y-2
- Fix #81069, #75421

* Mon Jan 13 2003 Elliot Lee <sopwith@redhat.com> 2.11y-1
- Update to 2.11y
- Fix #80953
- Update patch0, patch107, patch117, patch120 for 2.11y
- Remove patch60, patch61, patch207, patch211, patch212, patch119, patch121
- Remove patch122, patch200

* Wed Oct 30 2002 Elliot Lee <sopwith@redhat.com> 2.11w-2
- Remove some crack/unnecessary patches while submitting stuff upstream.
- Build with -D_FILE_OFFSET_BITS=64

* Tue Oct 29 2002 Elliot Lee <sopwith@redhat.com> 2.11w-1
- Update to 2.11w, resolve patch conflicts

* Tue Oct 08 2002 Phil Knirsch <pknirsch@redhat.com> 2.11r-10hammer.3
- Extended util-linux-2.11b-s390x patch to work again.

* Thu Oct 03 2002 Elliot Lee <sopwith@redhat.com> 2.11r-10hammer.2
- Add patch122 for hwclock on x86_64

* Thu Sep 12 2002 Than Ngo <than@redhat.com> 2.11r-10hammer.1
- Fixed pam config files

* Wed Sep 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.11r-10hammer
- Port to hammer

* Fri Aug 30 2002 Elliot Lee <sopwith@redhat.com> 2.11r-10
- Patch120 (hwclock) to fix #72140
- Include isosize util

* Wed Aug 7 2002  Elliot Lee <sopwith@redhat.com> 2.11r-9
- Patch120 (skipraid2) to fix #70353, because the original patch was 
totally useless.

* Fri Aug 2 2002  Elliot Lee <sopwith@redhat.com> 2.11r-8
- Patch119 (fdisk-add-primary) from #67898

* Wed Jul 24 2002 Elliot Lee <sopwith@redhat.com> 2.11r-7
- Really add the gptsize patch, instead of what I think the patch says.
(+1)

* Tue Jul 23 2002 Elliot Lee <sopwith@redhat.com> 2.11r-6
- Add the sp[n].size part of the patch from #69603

* Mon Jul 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- adjust mainframe patches

* Tue Jul  2 2002 Bill Nottingham <notting@redhat.com> 2.11r-4
- only require usermode if we're shipping kbdrate here

* Fri Jun 28 2002 Trond Eivind Glomsrod <teg@redhat.com> 2.11r-3
- Port the large swap patch to new util-linux... the off_t changes 
  now in main aren't sufficient

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.11r-2
- Remove swapondetect (patch301) until it avoids possible false positives.

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.11r-1
- Update to 2.11r, wheeee
- Remove unused patches

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.11n-19
- Make a note here that this package was the source of the single change 
contained in util-linux-2.11f-18 (in 7.2/Alpha), and also contains the 
rawman patch from util-linux-2.11f-17.1 (in 2.1AS).
- Package has no runtime deps on slang, so remove the BuildRequires: 
slang-devel.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Elliot Lee <sopwith@redhat.com> 2.11n-17
- Fix teg's swapondetect patch to not print out the usage message when 
'swapon -a -e' is run. (#66690) (edit existing patch)
- Apply hjl's utmp handling patch (#66950) (patch116)
- Fix fdisk man page notes on IDE disk partition limit (#64013) (patch117)
- Fix mount.8 man page notes on vfat shortname option (#65628) (patch117)
- Fix possible cal overflow with widechars (#67090) (patch117)

* Tue Jun 11 2002 Trond Eivind Glomsrod <teg@redhat.com> 2.11n-16
- support large swap partitions
- add '-d' option to autodetect available swap partitions

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 15 2002 Elliot Lee <sopwith@redhat.com> 2.11n-14
- Remove kbdrate (again).

* Mon Apr 29 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- adjust mainframe patches to apply to current rpm
- do not include fdisk until it is fixed to work on mainframe

* Mon Apr 01 2002 Elliot Lee <sopwith@redhat.com> 2.11n-12
- Don't strip binaries - rpm does it for us.

* Sun Mar 31 2002 Elliot Lee <sopwith@redhat.com> 2.11n-11
- Apply patch115 from ejb@ql.org for bug #61868

* Wed Mar 27 2002 Elliot Lee <sopwith@redhat.com> 2.11n-10
- Finish fixing #60675 (ipcrm man page), updated the patch.
- Fix #61203 (patch114 - dumboctal.patch).

* Tue Mar 12 2002 Elliot Lee <sopwith@redhat.com> 2.11n-9
- Update ctty3 patch to ignore SIGHUP while dropping controlling terminal

* Fri Mar 08 2002 Elliot Lee <sopwith@redhat.com> 2.11n-8
- Update ctty3 patch to drop controlling terminal before forking.

* Fri Mar 08 2002 Elliot Lee <sopwith@redhat.com> 2.11n-7
  Fix various bugs:
- Add patch110 (skipraid) to properly skip devices that are part of a RAID array.
- Add patch111 (mkfsman) to update the mkfs man page's "SEE ALSO" section.
- remove README.cfdisk
- Include partx
- Fix 54741 and related bugs for good(hah!) with patch113 (ctty3)

* Wed Mar 06 2002 Elliot Lee <sopwith@redhat.com> 2.11n-6
- Put kbdrate in, add usermode dep.

* Tue Feb 26 2002 Elliot Lee <sopwith@redhat.com> 2.11n-5
- Fix #60363 (tweak raw.8 man page, make rawdevices.8 symlink).

* Tue Jan 28 2002 Bill Nottingham <notting@redhat.com> 2.11n-4
- remove kbdrate (fixes kbd conflict)

* Fri Dec 28 2001 Elliot Lee <sopwith@redhat.com> 2.11n-3
- Add util-linux-2.11n-ownerumount.patch (#56593)
- Add patch102 (util-linux-2.11n-colrm.patch) to fix #51887
- Fix #53452 nits.
- Fix #56953 (remove tunelp on s390)
- Fix #56459, and in addition switch to using sed instead of perl.
- Fix #58471
- Fix #57300
- Fix #37436
- Fix #32132

* Wed Dec 26 2001 Elliot Lee <sopwith@redhat.com> 2.11n-1
- Update to 2.11n
- Merge mount/losetup back in.

* Tue Dec 04 2001 Elliot Lee <sopwith@redhat.com> 2.11f-17
- Add patch38 (util-linux-2.11f-ctty2.patch) to ignore SIGINT/SIGTERM/SIGQUIT in the parent, so that ^\ won't break things.

* Fri Nov 09 2001 Elliot Lee <sopwith@redhat.com> 2.11f-16
- Merge patches 36, 75, 76, and 77 into patch #37, to attempt resolve all the remaining issues with #54741.

* Wed Oct 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add nologin man-page for s390/s390x

* Wed Oct 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11f-14
- Don't build kbdrate on s390/s390x
- Don't make the pivot_root.8 man page executable(!)

* Tue Oct 23 2001 Elliot Lee <sopwith@redhat.com> 2.11f-13
- Patch/idea #76 from HJL, fixes bug #54741 (race condition in login 
acquisition of controlling terminal).

* Thu Oct 11 2001 Bill Nottingham <notting@redhat.com>
- fix permissions problem with vipw & shadow files, again (doh!)

* Tue Oct 09 2001 Erik Troan <ewt@redhat.com>
- added patch from Olaf Kirch to fix possible pwent structure overwriting

* Fri Sep 28 2001 Elliot Lee <sopwith@redhat.com> 2.11f-10
- fdisk patch from arjan

* Sun Aug 26 2001 Elliot Lee <sopwith@redhat.com> 2.11f-9
- Don't include cfdisk, since it appears to be an even bigger pile of junk than fdisk? :)

* Wed Aug  1 2001 Tim Powers <timp@redhat.com>
- don't require usermode

* Mon Jul 30 2001 Elliot Lee <sopwith@redhat.com> 2.11f-7
- Incorporate kbdrate back in.

* Mon Jul 30 2001 Bill Nottingham <notting@redhat.com>
- revert the patch that calls setsid() in login that we had reverted
  locally but got integrated upstream (#46223)

* Tue Jul 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- correct s390x patch

* Mon Jul 23 2001 Elliot Lee <sopwith@redhat.com>
- Add my megapatch (various bugs)
- Include pivot_root (#44828)

* Thu Jul 12 2001 Bill Nottingham <notting@redhat.com>
- make shadow files 0400, not 0600

* Wed Jul 11 2001 Bill Nottingham <notting@redhat.com>
- fix permissions problem with vipw & shadow files

* Mon Jun 18 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.11f, remove any merged patches
- add s390x patches for somewhat larger swap

* Thu Jun 14 2001 Erik Troan <ewt@redhat.com>
- added --verbose patch to mkcramfs; it's much quieter by default now

* Tue May 22 2001 Erik Troan <ewt@redhat.com>
- removed warning about starting partitions on cylinder 0 -- swap version2
  makes it unnecessary

* Wed May  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11b-2
- Fix up s390x support

* Mon May  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11b-1
- Fix up login for real (a console session should be the controlling tty)
  by reverting to 2.10s code (#36839, #36840, #39237)
- Add man page for agetty (#39287)
- 2.11b, while at it

* Fri Apr 27 2001 Preston Brown <pbrown@redhat.com> 2.11a-4
- /sbin/nologin from OpenBSD added.

* Fri Apr 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11a-3
- Fix up login - exiting immediately even if the password is correct
  is not exactly a nice feature.
- Make definite plans to kill people who update login without checking
  if the new version works ;)

* Tue Apr 17 2001 Erik Troan <ewt@redhat.com>
- upgraded to 2.11a (kbdrate moved to kbd, among other things)
- turned off ALLOW_VCS_USE
- modified mkcramfs to not use a large number of file descriptors
- include mkfs.bfs

* Sun Apr  8 2001 Matt Wilson <msw@redhat.com>
- changed Requires: kernel >= 2.2.12-7 to Conflicts: kernel < 2.2.12-7
  (fixes a initscripts -> util-linux -> kernel -> initscripts prereq loop)

* Tue Mar 20 2001 Matt Wilson <msw@redhat.com>
- patched mkcramfs to use the PAGE_SIZE from asm/page.h instead of hard
  coding 4096 (fixes mkcramfs on alpha...)

* Mon Mar 19 2001 Matt Wilson <msw@redhat.com>
- added mkcramfs (from linux/scripts/mkcramfs)

* Mon Feb 26 2001 Tim Powers <timp@redhat.com>
- fixed bug #29131, where ipc.info didn't have an info dir entry,
  added the dir entry to ipc.texi (Patch58)

* Fri Feb 23 2001 Preston Brown <pbrown@redhat.com>
- use lang finder script
- install info files

* Thu Feb 08 2001 Erik Troan <ewt@redhat.com>
- reverted login patch; seems to cause problems
- added agetty

* Wed Feb 07 2001 Erik Troan <ewt@redhat.com>
- updated kill man page
- added patch to fix vipw race
- updated vipw to edit /etc/shadow and /etc/gshadow, if appropriate
- added patch to disassociate login from tty, session, and pgrp

* Tue Feb 06 2001 Erik Troan <ewt@redhat.com>
- fixed problem w/ empty extended partitions
- added patch to fix the date in the more man page
- set OPT to pass optimization flags to make rather then RPM_OPT_FLAG
- fixed fdisk -l /Proc/partitions parsing
- updated to 2.10s

* Tue Jan 23 2001 Preston Brown <pbrown@redhat.com>
- danish translations added

* Mon Jan 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix segfault in login in btmp patch (#24025)

* Mon Dec 11 2000 Oliver Paukstadt <oliver.paukstadt@millenux.com>
- ported to s390

* Wed Nov 01 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.10p
- update patch37 to newer fdisk version

* Mon Oct  9 2000 Jeff Johnson <jbj@redhat.com>
- update to 2.10o
-  fdformat: fixed to work with kernel 2.4.0test6 (Marek Wojtowicz)
-  login: not installed suid
-  getopt: by default install aux files in /usr/share/misc
- update to 2.10n:
-  added blockdev.8
-  change to elvtune (andrea)
-  fixed overrun in agetty (vii@penguinpowered.com)
-  shutdown: prefer umounting by mount point (rgooch)
-  fdisk: added plan9
-  fdisk: remove empty links in chain of extended partitions
-  hwclock: handle both /dev/rtc and /dev/efirtc (Bill Nottingham)
-  script: added -f (flush) option (Ivan Schreter)
-  script: added -q (quiet) option (Per Andreas Buer)
-  getopt: updated to version 1.1.0 (Frodo Looijaard)
-  Czech messages (Jiri Pavlovsky)
- login.1 man page had not /var/spool/mail path (#16998).
- sln.8 man page (but not executable) included (#10601).
- teach fdisk 0xde(Dell), 0xee(EFI GPT), 0xef(EFI FAT) partitions (#17610).

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Mon Aug 14 2000 Jeff Johnson <jbj@redhat.com>
- setfdprm should open with O_WRONLY, not 3.

* Fri Aug 11 2000 Jeff Johnson <jbj@redhat.com>
- fdformat should open with O_WRONLY, not 3.

* Fri Jul 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- make 'look' look in /usr/share/dict

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- put /usr/local/sbin:/usr/local/bin in root's path

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Bill Nottingham <notting@redhat.com>
- enable hwclock to use /dev/efirtc on ia64 (gettext is fun. :( )

* Mon Jul  3 2000 Bill Nottingham <notting@redhat.com>
- move cfdisk to /usr/sbin, it depends on /usr stuff
- add rescuept

* Fri Jun 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- point more at the correct path to vi (for "v"), Bug #10882

* Sun Jun  4 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging changes.

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Mon May  1 2000 Bill Nottingham <notting@redhat.com>
- eek, where did login go? (specfile tweaks)

* Mon Apr 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.10k
- fix compilation with current glibc

* Tue Mar 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.10h

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Sat Mar  4 2000 Matt Wilson <msw@redhat.com>
- use snprintf - not sprintf - when doing
  sprintf ("%%s\n", _("Some string")) to avoid overflows and
  segfaults.

* Mon Feb 21 2000 Jeff Johnson <jbj@redhat.com>
- raw control file was /dev/raw, now /dev/rawctl.
- raw access files were /dev/raw*, now /dev/raw/raw*.

* Thu Feb 17 2000 Erik Troan <ewt@redhat.com>
- -v argument to mkswap wasn't working

* Thu Feb 10 2000 Jakub Jelinek <jakub@redhat.com>
- Recognize 0xfd on Sun disklabels as RAID

* Tue Feb  8 2000 Bill Nottingham <notting@redhat.com>
- more lives in /bin, and was linked against /usr/lib/libnurses. Bad.

* Thu Feb 03 2000 Jakub Jelinek <jakub@redhat.com>
- update to 2.10f
- fix issues in the new realpath code, avoid leaking memory

* Tue Feb 01 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies
- add NFSv3 patches

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- don't require csh

* Mon Jan 24 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.10e
- add rename

* Thu Jan 20 2000 Jeff Johnson <jbj@redhat.com>
- strip newlines in logger input.

* Mon Jan 10 2000 Jeff Johnson <jbj@redhat.com>
- rebuild with correct ncurses libs.

* Tue Dec  7 1999 Matt Wilson <msw@redhat.com>
- updated to util-linux 2.10c
- deprecated IMAP login mail notification patch17
- deprecated raw patch22
- depricated readprofile patch24

* Tue Dec  7 1999 Bill Nottingham <notting@redhat.com>
- add patch for readprofile

* Thu Nov 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- tunelp should come from util-linux

* Tue Nov  9 1999 Jakub Jelinek <jakub@redhat.com>
- kbdrate cannot use /dev/port on sparc.

* Wed Nov  3 1999 Jakub Jelinek <jakub@redhat.com>
- fix kbdrate on sparc.

* Wed Oct 27 1999 Bill Nottingham <notting@redhat.com>
- ship hwclock on alpha.

* Tue Oct  5 1999 Bill Nottingham <notting@redhat.com>
- don't ship symlinks to rdev if we don't ship rdev.

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- add rawIO support from sct

* Mon Aug 30 1999 Preston Brown <pbrown@redhat.com>
- don't display "new mail" message when the only piece of mail is from IMAP

* Fri Aug 27 1999 Michael K. Johnson <johnsonm@redhat.com>
- kbdrate is now a console program

* Thu Aug 26 1999 Jeff Johnson <jbj@redhat.com>
- hostid is now in sh-utils. On sparc, install hostid as sunhostid (#4581).
- update to 2.9w:
-  Updated mount.8 (Yann Droneaud)
-  Improved makefiles
-  Fixed flaw in fdisk

* Tue Aug 10 1999 Jeff Johnson <jbj@redhat.com>
- tsort is now in textutils.

* Wed Aug  4 1999 Bill Nottingham <notting@redhat.com>
- turn off setuid bit on login. Again. :(

* Tue Aug  3 1999 Peter Jones, <pjones@redhat.com>
- hostid script for sparc (#3803).

* Tue Aug 03 1999 Christian 'Dr. Disk' Hechelmann <drdisk@tc-gruppe.de>
- added locale message catalogs to %%file
- added patch for non-root build
- vigr.8 and /usr/lib/getopt  man-page was missing from file list
- /etc/fdprm really is a config file

* Fri Jul 23 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9v:
- cfdisk no longer believes the kernel's HDGETGEO
	(and may be able to partition a 2 TB disk)

* Fri Jul 16 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9u:
- Czech more.help and messages (Jiri Pavlovsky)
- Japanese messages (Daisuke Yamashita)
- fdisk fix (Klaus G. Wagner)
- mount fix (Hirokazu Takahashi)
- agetty: enable hardware flow control (Thorsten Kranzkowski)
- minor cfdisk improvements
- fdisk no longer accepts a default device
- Makefile fix

* Tue Jul  6 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9t:
- national language support for hwclock
- Japanese messages (both by Daisuke Yamashita)
- German messages and some misc i18n fixes (Elrond)
- Czech messages (Jiri Pavlovsky)
- wall fixed for /dev/pts/xx ttys
- make last and wall use getutent() (Sascha Schumann)
	[Maybe this is bad: last reading all of wtmp may be too slow.
	Revert in case people complain.]
- documented UUID= and LABEL= in fstab.5
- added some partition types
- swapon: warn only if verbose

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9s.

* Sat May 29 1999 Jeff Johnson <jbj@redhat.com>
- fix mkswap sets incorrect bits on sparc64 (#3140).

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- on sparc64 random ioctls on clock interface cause kernel messages.

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- improved raid patch (H.J. Lu).

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- added patch for smartraid controllers

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- fix logging problems caused by setproctitle and PAM interaction
  (#2045)

* Wed Mar 31 1999 Jeff Johnson <jbj@redhat.com>
- include docs and examples for sfdisk (#1164)

* Mon Mar 29 1999 Matt Wilson <msw@redhat.com>
- rtc is not working properly on alpha, we can't use hwclock yet.

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to make mkswap more 64 bit friendly... Patch from
  eranian@hpl.hp.com (ahem!)

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- include sfdisk (#1164)
- fix write (#1784)
- use positive logic in spec file (%%ifarch rather than %ifnarch).
- (re)-use 1st matching utmp slot if search by mypid not found.
- update to 2.9o
- lastb wants bad logins in wtmp clone /var/run/btmp (#884)

* Thu Mar 25 1999 Jakub Jelinek <jj@ultra.linux.cz>
- if hwclock is to be compiled on sparc,
  it must actually work. Also, it should obsolete
  clock, otherwise it clashes.
- limit the swap size in mkswap for 2.2.1+ kernels
  by the actual maximum size kernel can handle.
- fix kbdrate on sparc, patch by J. S. Connell
  <ankh@canuck.gen.nz>

* Wed Mar 24 1999 Matt Wilson <msw@redhat.com>
- added pam_console back into pam.d/login

* Tue Mar 23 1999 Matt Wilson <msw@redhat.com>
- updated to 2.9i
- added hwclock for sparcs and alpha

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- added vigr to file list

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- remove most of the ifnarch arm stuff

* Mon Mar 15 1999 Michael Johnson <johnsonm@redhat.com>
- added pam_console.so to /etc/pam.d/login

* Thu Feb  4 1999 Michael K. Johnson <johnsonm@redhat.com>
- .perms patch to login to make it retain root in parent process
  for pam_close_session to work correctly

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- strip fdisk in buildroot correctly (#718)

* Mon Jan 11 1999 Cristian Gafton <gafton@redhat.com>
- have fdisk compiled on sparc and arm

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added beos partition type to fdisk

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- incorporate fdisk on all arches

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- restore PAM functionality at end of login (Bug #201)

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch top build on the arm without PAM and related utilities, for now.
- build hwclock only on intel

* Wed Nov 18 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 2.9

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)
- patch kbdrate wackiness so it builds with egcs

* Tue Oct 13 1998 Erik Troan <ewt@redhat.com>
- patched more to use termcap

* Mon Oct 12 1998 Erik Troan <ewt@redhat.com>
- added warning about alpha/bsd label starting cylinder

* Mon Sep 21 1998 Erik Troan <ewt@redhat.com>
- use sigsetjmp/siglongjmp in more rather then sig'less versions

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- explicit attrs for setuid/setgid programs

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- sln is now included in glibc

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- add cbm1581 floppy definitions (problem #787)

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- remove /etc/nologin at end of shutdown/halt.

* Fri Jun 19 1998 Jeff Johnson <jbj@redhat.com>
- add mount/losetup.

* Thu Jun 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.8 with 2.8b clean up. hostid now defunct?

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- "more" now works properly on sparc

* Sat May 02 1998 Jeff Johnson <jbj@redhat.com>
- Fix "fdisk -l" fault on mounted cdrom. (prob #513)

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild

* Mon Dec 29 1997 Erik Troan <ewt@redhat.com>
- more didn't suspend properly on glibc
- use proper tc*() calls rather then ioctl's

* Sun Dec 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed a security problem in chfn and chsh accepting too 
  long gecos fields

* Fri Dec 19 1997 Mike Wangsmo <wanger@redhat.com>
- removed "." from default path

* Tue Dec 02 1997 Cristian Gafton <gafton@redhat.com>
- added (again) the vipw patch

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- minor cleanups for glibc 2.1

* Fri Oct 17 1997 Michael Fulbright <msf@redhat.com>
- added vfat32 filesystem type to list recognized by fdisk

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- don't build clock on the alpha 
- don't install chkdupexe

* Thu Oct 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Update to new pam standard.
- BuildRoot.

* Thu Sep 25 1997 Cristian Gafton <gafton@redhat.com>
- added rootok and setproctitle patches
- updated pam config files for chfn and chsh

* Tue Sep 02 1997 Erik Troan <ewt@redhat.com>
- updated MCONFIG to automatically determine the architecture
- added glibc header hacks to fdisk code
- rdev is only available on the intel

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- update to util-linux 2.7, fixed login problems

* Wed Jun 25 1997 Erik Troan <ewt@redhat.com>
- Merged Red Hat changes into main util-linux source, updated package to
  development util-linux (nearly 2.7).

* Tue Apr 22 1997 Michael K. Johnson <johnsonm@redhat.com>
- LOG_AUTH --> LOG_AUTHPRIV in login and shutdown

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam and from pam.conf to pam.d

* Tue Feb 25 1997 Michael K. Johnson <johnsonm@redhat.com>
- pam.patch differentiated between different kinds of bad logins.
  In particular, "user does not exist" and "bad password" were treated
  differently.  This was a minor security hole.
