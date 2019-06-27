Name: coreutils
Version: 8.31.0.3.6bd78
Release: alt2
%define srcname %name-%version-%release

Summary: The GNU versions of common management utilities
License: GPLv3+
Group: System/Base
Url: https://www.gnu.org/software/coreutils/

# git://git.sv.gnu.org/coreutils refs/heads/master
# git://git.altlinux.org/people/ldv/packages/coreutils refs/heads/coreutils-current
Source0: %srcname.tar
# translationproject.org::tp/latest/coreutils/
# git://git.altlinux.org/people/ldv/packages/coreutils refs/heads/po-current
Source1: po-%version-%release.tar

# sources from fileutils
Source11: color_ls.sh
Source12: color_ls.csh

# sources from sh-utils
Source20: exit.c
Source21: getuseruid.c
Source23: runas.c
Source24: runbg.c
Source25: usleep.c
Source26: runas.1
Source27: usleep.1
Source28: true.1
Source29: false.1

# git://git.altlinux.org/people/ldv/packages/coreutils coreutils-current..coreutils-alt
Patch: %srcname.patch

%def_enable selinux

Provides: stat = %version, fileutils = %version, textutils = %version, sh-utils = %version
Provides: mktemp = 0:1.6, mktemp = 1:1.5-alt2
Obsoletes: stat, fileutils, textutils, sh-utils, mktemp
Conflicts: man-pages < 0:1.52-alt2, initscripts < 0:5.49-ipl41mdk, rpm-build < 0:4.0.4-alt7
# due to /bin/arch
Conflicts: util-linux < 0:2.13-alt6
# due to /usr/bin/kill and %_man1dir/kill.1
Conflicts: procps < 0:2.0.10-alt4
# due to incompatible change in "readlink -f"
Conflicts: chrooted < 0:0.3.1-alt1
# due to buggy rpmdups/rpmrdups
Conflicts: rpm-utils < 0:0.7.6-alt1
# due to hostname
Conflicts: net-tools < 0:1.60-alt9

BuildRequires: gnulib >= 0.1.2433.3043e
BuildRequires: makeinfo

# for ACL support in ls/dir/vdir, cp, mv and install utilities
BuildRequires: libacl-devel

# for extended attribute copying support in cp and mv utilities
BuildRequires: libattr-devel

# for colorizing capabilities support in ls utility
BuildRequires: libcap-devel

# for arbitrarily large numbers support in expr and factor utilities
BuildRequires: libgmp-devel

# due to build from git
BuildRequires: gperf

# due to ls
BuildRequires: libtinfo-devel

# due to exit.c
BuildRequires: glibc-devel-static

# for SELinux
%{?_enable_selinux:BuildRequires: libselinux-devel}

# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: strace}}

%description
These are the GNU core utilities.  This package is the union of
the GNU fileutils, sh-utils, and textutils packages.

These tools are the GNU versions of common useful and popular
file and text utilities which are used for:
+ file management
+ shell scripting
+ modifying text file

Most of these programs have significant advantages over their Unix
counterparts, such as greater speed, additional options, and fewer
arbitrary limits.

%prep
%setup -n %srcname -a1
%patch -p1

# Build scripts expect to find coreutils version in this file.
echo -n %version >.tarball-version

# Generate LINGUAS file.
ls po/*.po 2>/dev/null |
	sed 's|.*/||; s|\.po$||' >po/LINGUAS

# Compress docs for packaging.
bzip2 -9k NEWS THANKS

# workarounds for bootstrap
ln -s /bin/false build-aux/git-version-gen
touch m4/cu-progs.m4

%build
./bootstrap --skip-po --gnulib-srcdir=%_datadir/gnulib

# Disable printf_safe for a while,
# required to enforce build with system vfprintf().
sed -i 's/gl_printf_safe=yes/gl_printf_safe=/' m4/gnulib-comp.m4 configure

%configure \
	--exec-prefix=/ \
	%{subst_enable selinux} \
	--enable-install-program=arch,hostname \
	--enable-no-install-program=su,uptime \
	#

%make_build -C po update-po
%make_build

# Build our version of true and false.
build_exit() {
	%__cc %optflags -W %_sourcedir/exit.c \
		$@ -DSTATUS=0 -o true

	%__cc %optflags -W %_sourcedir/exit.c \
		$@ -DSTATUS=1 -o false
}

# Executable may fail on some architectures if it uses libc's syscall wrapper
# without initialization performed in start files.  Fall back to simple static
# true/false implementation if it happens.
build_exit -U_FORTIFY_SOURCE -fno-stack-protector -nostartfiles -static -DNOSTARTFILES=1
./true ||
	build_exit -static

# Build additional utilities.
for n in getuseruid runas runbg usleep; do
	%__cc %optflags "%_sourcedir/$n.c" -o $n
done

%install
%makeinstall_std
install -pD -m644 src/dircolors.hin "%buildroot%_sysconfdir/DIR_COLORS"

pushd "%buildroot"
	mkdir -p bin
	
	# %_bindir -> /bin relocations
        for n in \
		basename cat chgrp chmod chown cp cut date \
		dd df du echo false head hostname install \
		kill link ln ls mkdir mkfifo mknod mktemp \
		mv nice pwd readlink rm rmdir sleep sort \
		stty sync tail touch true uname unlink wc \
	; do
		mv .%_bindir/$n bin/
	done

	# compatibility symlinks
	for n in cat cut du head install kill mkfifo sort tail wc; do
		ln -s ../../bin/$n .%_bindir/
	done

	# chroot
	mkdir -p sbin .%_sbindir
	mv .%_bindir/chroot sbin/
		ln -s ../../sbin/chroot .%_sbindir/

	# hostname
	for n in dnsdomainname domainname nisdomainname ypdomainname; do
		ln -s hostname ./bin/$n
		ln -s hostname.1 ./%_man1dir/$n.1
	done

	mkdir -p .%_sysconfdir/profile.d
	install -pm755 %_sourcedir/color_ls.{sh,csh} .%_sysconfdir/profile.d/
	ln -s ../../bin/install .%_bindir/ginstall
popd

# Install assembler versions of true and false and their manpages.
install -pm755 true false %buildroot/bin/
install -pm644 %_sourcedir/{true,false}.1 %buildroot%_mandir/man1/

# Install additional utilities and their manpages.
install -pm755 getuseruid runas usleep %buildroot/bin/
install -pm755 runbg %buildroot%_bindir/
install -pm644 %_sourcedir/{runas,usleep}.1 %buildroot%_man1dir/

%find_lang %name

%check
: ${SHELL:=/bin/sh} ${VERBOSE:=no}
export SHELL VERBOSE
%make_build -k check

%files -f %name.lang
%config(noreplace) %_sysconfdir/DIR_COLORS
%config(noreplace) %_sysconfdir/profile.d/*
/bin/*
%_bindir/*
/sbin/*
%_sbindir/*
%_libexecdir/%name/
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS NEWS.bz2 README THANKS.bz2 TODO

%changelog
* Tue May 21 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 8.31.0.3.6bd78-alt2
- true, false: build a portable implementation if the traditional one fails
  (fixes these utilities at least on ppc64le architecture).

* Fri Mar 15 2019 Dmitry V. Levin <ldv@altlinux.org> 8.31.0.3.6bd78-alt1
- coreutils: v8.30-31-g69df9e20e -> v8.31-3-g6bd78f27f.
- gnulib: v0.1-2305-g95c96b6dd -> v0.1-2433-g3043e43a7.
- Updated translations from translationproject.org.

* Wed Dec 26 2018 Dmitry V. Levin <ldv@altlinux.org> 8.30.0.31.69df9-alt1
- coreutils: v8.27-23-gf4570a9 -> v8.30-31-g69df9e20e.
- gnulib: v0.1-1209-g24b3216 -> v0.1-2305-g95c96b6dd.
- Updated translations from translationproject.org.

* Sun Apr 23 2017 Dmitry V. Levin <ldv@altlinux.org> 8.27.0.23.f4570-alt1
- coreutils: v8.27-6-g04148c9 -> v8.27-23-gf4570a9.
- Changed *domainname aliases to accept hostname(1) options (closes: #33385).

* Tue Mar 21 2017 Dmitry V. Levin <ldv@altlinux.org> 8.27.0.6.04148-alt1
- coreutils: v8.24-40-gc1dba59 -> v8.27-6-g04148c9.
- gnulib: v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Thu Oct 08 2015 Dmitry V. Levin <ldv@altlinux.org> 8.24.0.40.c1dba-alt1
- Updated to v8.24-40-gc1dba59.
- Updated translations from translationproject.org.
- Built with gnulib v0.1-585-g2fda85e.

* Thu Jan 02 2014 Dmitry V. Levin <ldv@altlinux.org> 8.22-alt1
- Updated to v8.22-5-g299924f.
- Updated translations from translationproject.org.
- Built with gnulib v0.1-58-g0f3a662.

* Tue Oct 29 2013 Dmitry V. Levin <ldv@altlinux.org> 8.21-alt2
- Updated to v8.21-135-gc90b9e0.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-8061-g5191b35.

* Mon Apr 08 2013 Dmitry V. Levin <ldv@altlinux.org> 8.21-alt1
- Updated to v8.21-32-gec02161.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7901-g076ac82.

* Mon Oct 29 2012 Dmitry V. Levin <ldv@altlinux.org> 8.20-alt1
- Updated coreutils to v8.20-9-g1cace4a.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7677-g4027785.

* Mon Aug 20 2012 Dmitry V. Levin <ldv@altlinux.org> 8.19-alt1
- Updated coreutils to v8.19.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7591-g898f143.

* Mon Aug 13 2012 Dmitry V. Levin <ldv@altlinux.org> 8.18-alt1
- Updated coreutils to v8.18.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7575-gd22f151.

* Fri Aug 03 2012 Dmitry V. Levin <ldv@altlinux.org> 8.17-alt1
- Updated coreutils to v8.17-62-g74a1c05.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7557-gee60576.

* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 8.16-alt1
- Updated coreutils to v8.16.
- Updated translations from translationproject.org.

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 8.15-alt1
- Updated coreutils to v8.15.
- Updated translations from translationproject.org.
- Changed build to use external gnulib package.

* Thu Oct 13 2011 Dmitry V. Levin <ldv@altlinux.org> 8.14-alt1
- Updated coreutils to v8.14.
- Updated gnulib to v0.0-6453-g6a4c64c.
- Updated translations from translationproject.org.

* Fri Sep 09 2011 Dmitry V. Levin <ldv@altlinux.org> 8.13-alt1
- Updated coreutils to v8.13.
- Updated gnulib to v0.0-6125-gda1717b.
- Updated translations from translationproject.org.

* Wed May 11 2011 Dmitry V. Levin <ldv@altlinux.org> 8.12-alt1
- Updated coreutils to v8.12-20-g73fd918.
- Updated gnulib to v0.0-5239-gd801cb7.
- Updated translations from translationproject.org.

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 8.11-alt1
- Updated coreutils to v8.11-10-g302cfca.
- Updated gnulib to v0.0-5115-ga81348d.
- Updated translations from translationproject.org.

* Sun Mar 06 2011 Dmitry V. Levin <ldv@altlinux.org> 8.10-alt2
- Resurrected /usr/bin/dir, /usr/bin/vdir, and /usr/bin/[
  executables instead of symlinks (closes: #25197).

* Fri Feb 04 2011 Dmitry V. Levin <ldv@altlinux.org> 8.10-alt1
- Updated coreutils to v8.10.
- Updated gnulib to v0.0-4800-ga036b76.
- Updated translations from translationproject.org.

* Fri Jan 07 2011 Dmitry V. Levin <ldv@altlinux.org> 8.9-alt1
- Updated coreutils to v8.9.
- Updated gnulib to v0.0-4679-g2aa56dd.
- Updated translations from translationproject.org.

* Thu Dec 30 2010 Dmitry V. Levin <ldv@altlinux.org> 8.8-alt2
- Updated coreutils to v8.8-7-g44dbcae (closes: #24841).

* Fri Dec 24 2010 Dmitry V. Levin <ldv@altlinux.org> 8.8-alt1
- Updated coreutils to v8.8.
- Updated gnulib to v0.0-4551-gfe2a230.
- Updated translations from translationproject.org.

* Sun Nov 14 2010 Dmitry V. Levin <ldv@altlinux.org> 8.7-alt1
- Updated coreutils to v8.7.
- Updated gnulib to v0.0-4439-ga14bd22.
- Updated translations from translationproject.org.
- Fixed build with new perl.

* Fri Oct 15 2010 Dmitry V. Levin <ldv@altlinux.org> 8.6-alt1
- Updated coreutils to v8.6.
- Updated gnulib to v0.0-4380-g78c0415.
- Updated translations from translationproject.org.

* Tue Sep 14 2010 Dmitry V. Levin <ldv@altlinux.org> 8.5-alt3
- Backported upstream fixes to tac(1).
- Backported upstream updates to /etc/DIR_COLORS (closes: #24052).

* Thu Aug 19 2010 Dmitry V. Levin <ldv@altlinux.org> 8.5-alt2
- Enabled SELinux support.

* Wed May 19 2010 Dmitry V. Levin <ldv@altlinux.org> 8.5-alt1
- Updated coreutils to v8.5.
- Updated gnulib to v0.0-3828-g6d126a8.
- Updated translations from translationproject.org.

* Mon Mar 22 2010 Dmitry V. Levin <ldv@altlinux.org> 8.4-alt3
- Fixed coreutils version that was inadvertenly lost during the
  last update.

* Sat Mar 20 2010 Dmitry V. Levin <ldv@altlinux.org> 8.4-alt2
- Updated coreutils to v8.4-63-g9f793de.
- Updated gnulib to v0.0-3591-geb2f221.
- Updated translations from translationproject.org.

* Thu Jan 14 2010 Dmitry V. Levin <ldv@altlinux.org> 8.4-alt1
- Updated coreutils to v8.4.
- Updated gnulib to v0.0-3307-g7521ea0.
- Updated translations from translationproject.org.

* Fri Jan 08 2010 Dmitry V. Levin <ldv@altlinux.org> 8.3-alt1
- Updated coreutils to v8.3.
- Updated gnulib to v0.0-3169-gcb361c9.
- Updated translations from translationproject.org.

* Sat Sep 19 2009 Dmitry V. Levin <ldv@altlinux.org> 7.6-alt1
- Updated coreutils to v7.6.
- Updated gnulib to v0.0-2561-g10322ac.
- Updated translations from translationproject.org.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 7.4-alt3
- Moved "make check" to %%check section.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 7.4-alt2
- Built --without-included-regex.

* Sat Jun 06 2009 Dmitry V. Levin <ldv@altlinux.org> 7.4-alt1
- Updated coreutils to v7.4.
- Updated gnulib to v0.0-2123-gc90c5cc.
- Updated translations from translationproject.org.
- Removed obsolete %%install_info/%%uninstall_info calls.
- Enabled colorizing capabilities support in ls(1).
- Enabled extended attribute copying support in cp(1) and mv(1).
- Enabled arbitrarily large numbers support in expr(1) and factor(1).

* Mon Oct 27 2008 Dmitry V. Levin <ldv@altlinux.org> 6.12-alt2
- Backported utimensat fixes from gnulib.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 6.12-alt1
- Updated coreutils to v6.12.
- Updated gnulib to v0.0-949-gca19d95.
- Updated translations from translationproject.org.
- chroot: Purge TMP and TMPDIR variables from environment (closes: #16024).

* Sat Apr 19 2008 Dmitry V. Levin <ldv@altlinux.org> 6.11-alt1
- Updated coreutils to v6.11-1-gb29e812.
- Updated gnulib to v0.0-513-g2e89567.
- Updated translations from translationproject.org.

* Mon Apr 07 2008 Dmitry V. Levin <ldv@altlinux.org> 6.10-alt4
- Updated coreutils to v6.10-177-g8b3ec19.
- Updated gnulib to v0.0-451-g2f1b8f5.
- Updated translations from translationproject.org.

* Tue Mar 25 2008 Dmitry V. Levin <ldv@altlinux.org> 6.10-alt3
- Updated coreutils to v6.10-142-g157a274.
- Updated gnulib to v0.0-378-g8b7bf41.
- join: Fix regression introduced by commit v6.10-70-ga1e7156.
- Build and package arch utility, originally from util-linux.

* Fri Mar 21 2008 Dmitry V. Levin <ldv@altlinux.org> 6.10-alt2
- Updated coreutils to v6.10-133-g677610e.
- Updated gnulib to v0.0-378-g8b7bf41.
- Relocated mktemp utility back from /usr/bin/ to /bin/.
- Added libacl-devel to BuildRequires, thus enabling ACL support
  in ls/dir/vdir, cp, mv and install utilities.

* Thu Mar 20 2008 Dmitry V. Levin <ldv@altlinux.org> 6.10-alt1
- Updated coreutils to v6.10-128-g9e2ed55.
- Updated gnulib to v0.0-374-g19676b3.
- Updated translations from translationproject.org::tp/latest/coreutils/.
- Dropped a few applicable but obsolete patches.
- Added Provides/Obsoletes tags for mktemp.
- Added strace to BuildRequires for test suite.
- Removed explicit pathname provides and %%post* script requirements.
- Previous packaged coreutils release (5.97) is about 1.5 years old.
  New release, among with new features described in
  /usr/share/doc/coreutils-6.10/NEWS.bz2 file, introduces
  incompatibilities (also described in that NEWS file).
  That is, prepare to fix your scripts!

* Tue May 22 2007 Dmitry V. Levin <ldv@altlinux.org> 5.97-alt6
- Reverted recent ls "fix" (#11740).

* Tue Apr 17 2007 Dmitry V. Levin <ldv@altlinux.org> 5.97-alt5
- Backported upstream fix for "ls --indicator-style=file-type" (RH#230052).
- Import coreutils-5.97-rh-remove_cwd_entries.patch (RH#235401).

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 5.97-alt4
- color_ls.sh: Quoted $TERM (#11440).
- color_ls.csh: Synced with color_ls.sh

* Sat Feb 03 2007 Dmitry V. Levin <ldv@altlinux.org> 5.97-alt3
- Fixed getcwd() to make pwd(1) and readlink(1) work also
  when run with an unreadable parent dir on systems with
  openat(2) support (Jim Meyering, fixes RH#227168).

* Fri Feb 02 2007 Dmitry V. Levin <ldv@altlinux.org> 5.97-alt2
- Updated to b5_9x snapshot 20060628.
- true, false: Rewritten without using glibc.
- Fixed a double-free bug in cut (Jim Meyering, fixes RH#220312).
- Fixed mv(1) error reporting (Jim Meyering, fixes DEB#376749).
- Backported new hashes: base64, sha224sum sha256sum sha384sum sha512sum.
- Added cifs to df(1) remote filesystems list (FC, fixes RH#183703).

* Sun Jun 25 2006 Dmitry V. Levin <ldv@altlinux.org> 5.97-alt1
- Updated to 5.97.

* Sat May 27 2006 Dmitry V. Levin <ldv@altlinux.org> 5.96-alt2
- Backported chgrp fix from 5_94 branch.
- Rewritten assembler version of true and false in C to avoid
  portability issues.

* Mon May 22 2006 Dmitry V. Levin <ldv@altlinux.org> 5.96-alt1
- Updated to 5.96.

* Tue May 16 2006 Dmitry V. Levin <ldv@altlinux.org> 5.95-alt1
- Updated to 5.95.

* Wed Apr 05 2006 Dmitry V. Levin <ldv@altlinux.org> 5.94-alt2
- Added .note.GNU-stack to exit.S.

* Wed Feb 15 2006 Dmitry V. Levin <ldv@altlinux.org> 5.94-alt1
- Updated to 5.94.
- Updated russian translation.

* Fri Feb 03 2006 Dmitry V. Levin <ldv@altlinux.org> 5.93-alt2
- Backported fts fixes from 5_94 branch.

* Mon Nov 07 2005 Dmitry V. Levin <ldv@altlinux.org> 5.93-alt1
- Updated to 5.93.

* Sat Nov 05 2005 Dmitry V. Levin <ldv@altlinux.org> 5.92-alt4
- Updated to 20051102 snapshot from stable 5_9x branch.

* Thu Oct 27 2005 Dmitry V. Levin <ldv@altlinux.org> 5.92-alt3
- md5sum: Changed default read mode back to text, to sync
  with documentation and for backwards compatibility.

* Mon Oct 24 2005 Dmitry V. Levin <ldv@altlinux.org> 5.92-alt2
- mkdir -p, install -d: When creating final component
  of the file name, do not fail when it already exists.

* Sun Oct 23 2005 Dmitry V. Levin <ldv@altlinux.org> 5.92-alt1
- Updated to 5.92.

* Thu Oct 20 2005 Dmitry V. Levin <ldv@altlinux.org> 5.91-alt1
- Updated to 5.91.
- Replaced rh-owl-ls_default_time_style patch with
  eggert-ls-time-style patch.
- Removed already disabled rh-owl-install-C patch.
- Reviewed and updated alt-posix2_version patch.
- Fixed 'ls --help' output (Eric Blake, closes #8176).
- Updated russian translation (closes #7628, #7633)

* Mon Apr 25 2005 Dmitry V. Levin <ldv@altlinux.org> 5.3.1-alt0.4
- Updated to 5.3.1 snapshot 200504240446.
- Updated mksock and ls_dir_vdir patches to use
  program_invocation_short_name instead of __progname.

* Wed Apr 13 2005 Dmitry V. Levin <ldv@altlinux.org> 5.3.1-alt0.3
- Updated to 5.3.1 snapshot 200504120741.

* Mon Apr 11 2005 Dmitry V. Levin <ldv@altlinux.org> 5.3.1-alt0.2
- Relocated chroot utility from %_sbindir to /sbin.
- Packaged hostname(1) (#6360).
- Patched hostname(1) to be somewhat compatible with
  traditional hostname utility from net-tools package.

* Mon Apr 04 2005 Dmitry V. Levin <ldv@altlinux.org> 5.3.1-alt0.1
- Updated to 5.3.1 snapshot 200504010740.
- tee: do not close stdout more than once.

* Tue Jan 11 2005 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt1
- Updated to 5.3.0 snapshot 200501082045 (release).

* Sun Jan 02 2005 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.10
- Updated to 5.3.0 snapshot 200412311006.

* Sat Nov 20 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.9
- Updated to 5.3.0 snapshot 200411200857.

* Mon Nov 01 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.8
- Updated to 5.3.0 snapshot 200410292210.

* Sun Oct 17 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.7
- Updated to 5.3.0 snapshot 200410151932.

* Thu Sep 30 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.6
- Updated to 5.3.0 snapshot 200409280634.

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.5
- Updated to 5.3.0 snapshot 200408240736.

* Mon Aug 23 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.4
- Updated to 5.3.0 snapshot 200408200229.

* Fri Aug 13 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.3
- chown: Fixed USER.GROUP bug.

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.2
- Updated to 5.3.0 snapshot 200408112347.
- install: Fixed one more regression.
- exit.S: Added x86_64 support.

* Tue Aug 10 2004 Dmitry V. Levin <ldv@altlinux.org> 5.3.0-alt0.1
- Updated to 5.3.0 snapshot 200408100654.
- Merged upstream: 7 patches.
- Reworked patches.
- install: Fixed two regressions.

* Thu Jun 03 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt5
- Fixed canonicalize_file_name behaviour.
- Changed default behaviour for chown/chgrp.

* Sun Apr 25 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt4
- Backported "stty -iutf8" option support.
  Requires quite fresh glibc-devel package at build time.

* Sun Apr 04 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt3
- readlink: implemented more canonicalize options.

* Wed Mar 31 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt2
- Assorted backports from cvs head.
- Package /bin/kill, %_bindir/kill and its manpage from coreutils.

* Sat Mar 13 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt1
- Updated to 5.2.1
- Merged upstream patches:
  eggert-chown-lsb
  alt-cloexec

* Tue Mar 02 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.0-alt2
- chown: applied patch from Paul Eggert, see
  http://mail.gnu.org/archive/html/bug-coreutils/2004-02/msg00125.html
- nohup: fixed nasty fd leak.

* Mon Feb 23 2004 Dmitry V. Levin <ldv@altlinux.org> 5.2.0-alt1
- Updated to 5.2.0, reviewed patches.
- Merged upstream patches:
  alt-owl-chown
- Removed obsolete patches:
  rh-CLOCK_REALTIME
  rh-df_spacedir
  rh-mem
  rh-utmp
- Added RH patches:
  rh-afs
  rh-langinfo
  rh-allow_old_options
  rh-alt-ls-stat
- Use tweaked help2man from this package for manpage generation.
- Do not build and package rm-static.

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt3
- Fixed file descriptor leakage in du (Jim Meyering).
- Build statically linked version of the GNU rm program
  and package it into rm-static subpackage.

* Fri May 02 2003 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt2
- Regenerated manpages with help2man-1.29-alt2.
- Ported %%pre script to new uninstall_info.

* Sun Apr 06 2003 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt1
- Updated to 5.0

* Mon Mar 31 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt1
- Updated to 4.5.12

* Thu Mar 20 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt1
- Updated to 4.5.11

* Fri Mar 14 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.10-alt1
- Updated to 4.5.10

* Wed Mar 05 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.9-alt1
- Updated to 4.5.9

* Sat Feb 22 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.8-alt1
- Updated to 4.5.8

* Mon Feb 10 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt1
- Updated to 4.5.7
- Updated patches:
  + alt-texinfo

* Thu Feb 06 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.6-alt1
- Updated to 4.5.6
- Merged upstream patches:
  + alt-who_xmalloc_fix
- Updated patches:
  + alt-texinfo

* Tue Feb 04 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.5-alt1
- Updated to 4.5.5
- Merged upstream patches:
  + alt-xalloc
  + alt-xgetcwd
  + alt-canonicalize
  + alt-readlink
  + alt-owl-rh-ls_restore_color
- New patches:
  + alt-xalloc
- Updated patches:
  + alt-mksock
  + alt-without-hostname-su-uptime

* Tue Feb 04 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt3
- who: fixed memory allocation arithmetic (#0002149).

* Sun Dec 01 2002 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt2
- Removed automake patch (no longer needed with automake >= 1.7).
- Minor code cleanups (xalloc and xgetcwd).
- Added canonicalize_file_name implementation to libfetish;
  affects non-glibc platforms.
- Turned dir and vdir into symlinks to ls (#0001635).
- Updated dircolors.
- Removed obsolete (merged) patches:
  sh-utils-2.0-rh-rfc822
- Removed obsolete (not applied) patches:
  fileutils-4.0.38-alt-cp_deref_always
  fileutils-4.1-alt-cp_force_ignore
- Rediffed patches:
  rh-df_spacedir
  rh-install_strip
  rh-owl-alt-ls_dumbterm
  rh-CLOCK_REALTIME
  alt-owl-chown
- Corrected description.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt1
- Updated to 4.5.3
- Our "ln --target-dir" fix merged upstream.

* Sun Oct 13 2002 Dmitry V. Levin <ldv@altlinux.org> 4.5.2-alt2
- Minor specfile tweaks.
- Updated buildrequires.

* Tue Oct 08 2002 Dmitry V. Levin <ldv@altlinux.org> 4.5.2-alt1
- Updated to 4.5.2
- Disabled cp_deref_always patch.
- Enabled tests by default.
- Fixed "ln --target-dir" (#0001369).

* Thu Sep 26 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.1-alt2
- Ressurected Conflicts.

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.1-alt1
- Inital build for ALT. This package is the union of the
  fileutils, sh-utils, and textutils packages.
- Review patches:
  + dropped "rh-stoneage" patch;
  + adopted readlink and mksock patches;
  + disabled "force interactive" patch.
