Name: bzip2
Version: 1.0.8
Release: alt1
Epoch: 1

Summary: A file compression utility
License: bzip2-1.0.6
Group: Archiving/Compression
Url: https://www.sourceware.org/bzip2/

# git://git.altlinux.org/gears/b/bzip2.git
Source: %name-%version-%release.tar

Requires: bzlib = %EVR
BuildPreReq: glibc-devel-static makeinfo

%package -n bzlib
Summary: The bzlib compression and decompression library
Summary(ru_RU.UTF-8): Библиотека сжатия данных bzlib
Group: System/Libraries

%package -n bzlib-devel
Summary: Include files for developing apps which will use bzip2
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel
Requires: bzlib = %EVR

%package -n bzlib-devel-static
Summary: Static library for developing apps which will use bzip2
Group: Development/C
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static
Requires: bzlib-devel = %EVR

%description
bzip2 is a freely available, patent-free, high quality data compressor.

bzip2 compresses files using the Burrows-Wheeler block sorting text
compression algorithm and Huffman coding.  Compression is generally
considerably better than that achieved by more conventional
LZ77/LZ78-based compressors (such as gzip), and approaches the
performance of the PPM family of statistical compressors.  bzip2 is
by far not the fastest compression utility, but it does strike a
balance between speed and compression capability.

The command-line options are deliberately very similar to those of
GNU Gzip, but they are not identical.

%description -n bzlib
The bzip2 compression library provides in-memory compression and
decompression functions, including integrity checks of the uncompressed
data.  The bzip2 library is used by many different system programs.

%description -n bzlib-devel
This package contains the include files needed to develop programs that
use the bzip2 compression and decompression library.

%description -n bzlib-devel-static
This package contains the static library needed to develop statically
linked programs that use the bzip2 compression and decompression
library.

%prep
%setup -n %name-%version-%release

%build
%define _optlevel 3
%add_optflags -Winline
%ifarch %ix86 x86_64
%add_optflags -momit-leaf-frame-pointer
%endif

%autoreconf
%configure --enable-shared --enable-static
%make_build

%check
%make_build -k check

%install
%makeinstall_std

# Relocate shared libraries from %_libdir/ to /%_lib/.
mkdir %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# Relocate binaries and manpages
pushd %buildroot
	mkdir -p bin sbin
	mv .%_bindir/* bin/

	for f in bzip bunzip; do
		ln -s ../../bin/bzip2 .%_bindir/$f
		ln -s bzip2.1 .%_man1dir/$f.1
	done
	for f in bzip2 bunzip2 bzcat; do
		ln -s ../../bin/bzip2 .%_bindir/$f
	done
	for f in bzip2recover; do
		ln -s ../../bin/$f .%_bindir/$f
		ln -s bzip2.1 .%_man1dir/$f.1
	done

	# Our bzless and bzmore live in less package.
	rm bin/bz{less,more} .%_man1dir/bz{less,more}.*

	# Our bzdiff, bzcmp and bz*grep live in gzip-utils package.
	rm .{/bin,%_man1dir}/{bzdiff,bzcmp,bzgrep,bzfgrep,bzegrep}*
popd

# Package pkgconfig file
mkdir -p %buildroot%_pkgconfigdir
cat > %buildroot%_pkgconfigdir/%name.pc <<'EOF'
prefix=%_prefix
exec_prefix=%_exec_prefix
libdir=%_libdir
includedir=%_includedir

Name: %name
Version: %version
Description: bzlib compression and decompression library
Libs: -lbz2
Cflags:
EOF

%define docdir %_docdir/%name
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -pm644 CHANGES LICENSE README %buildroot%docdir/

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files -n bzlib
/%_lib/*
%dir %docdir/
%docdir/LICENSE

%files -n bzlib-devel
%_libdir/*.so
%_includedir/*
%_infodir/*.info*
%_pkgconfigdir/%name.pc

%files -n bzlib-devel-static
%_libdir/*.a

%files
/bin/*
%_bindir/b*zip*
%_bindir/bzcat
%_man1dir/b*zip*.*
%_man1dir/bzcat.*
%dir %docdir/
%docdir/[CR]*

%changelog
* Mon Mar 02 2020 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.8-alt1
- 1.0.6 -> 1.0.8.
- Removed symbol versioning stub.

* Sun Mar 10 2019 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.6-alt6
- bzlib-devel: packaged pkgconfig file (requested by viy@).

* Tue Oct 24 2017 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.6-alt5
- bzip2recover: fixed a use-after-free bug (by sem@; fixes: CVE-2016-3189).

* Wed Dec 02 2015 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.6-alt4
- Regenerated texinfo documentation.

* Sat Feb 19 2011 Alexey Tourbin <at@altlinux.ru> 1:1.0.6-alt3
- Disabled symbol versioning.

* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.6-alt2
- Rebuilt for debuginfo.

* Mon Sep 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.6-alt1
- Updated to 1.0.6 (fixes CVE-2010-0405).

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.5-alt5
- Moved "make check" to %%check section.

* Tue Sep 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.5-alt4
- Removed obsolete %%install_info/%%uninstall_info calls.
- Packaged %name-doc subpackage as noarch.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.5-alt3
- Removed obsolete %%post_ldconfig_sys/%%postun_ldconfig calls.

* Fri Mar 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.5-alt2
- bzip2.texi: Synced with LICENSE file.
- Rebuilt using texinfo-4.11-alt3 to fix direntry.

* Tue Mar 18 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.5-alt1
- Updated to 1.0.5 (fixes CERT-FI 20469 as it applies to bzip2, CVE-2008-1372).
- Removed explicit pathname provides and %%post* script requirements.

* Fri May 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.4-alt3
- Fixed interpackage dependencies w.r.t. rpm-4_4.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.4-alt2
- bzip2.texi: Updated for 1.0.4.

* Wed Jan 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.4-alt1
- Updated to 1.0.4.
- Removed compat interface.
- Removed obsolete bzlib_triggerpostun.

* Fri May 20 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt5
- bzip2-utils: obsoleted by gzip-utils package.

* Wed May 18 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt4
- bzip2:
  + Replaced Char* with const Char* where appropriate.
  + Trimmed usage text to bare minimum.

* Mon May 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt3
- Fixed double fclose bug in bunzip2 introduced in 1.0.3-alt1.

* Thu May 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt2
- Split autotools support patch into two parts.
- bzip2: changed -h/-L/-V options behaviour to output to stdout
  instead of stderr and cause program exit (for -L/-V) without
  processing any more options.

* Fri Apr 08 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt1
- Updated to 1.0.3.
- %name-utils: updated zme script.
- Rewritten autotools support patch.
- bzip2: fixed chmod/chown race condition.
- bzip2recover: fixed output file permissions.
- bzip2,bzip2recover: fixed invocation with empty arglist.
- bzlib-devel:
  + updated texinfo ducumentation.
  + disabled packaging of the bzlib_compat.h file.

* Tue Feb 08 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt11
- Fixed multilib (closes #4878).
- Added --show-progress option, based on patch from
  http://www.vanheusden.com/Linux/.

* Wed Apr 28 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt10
- Rebuilt with glibc-2.3.x.

* Tue Nov 25 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt9
- Do not package .la files.
- Updated URLs (#3313).

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt8
- Explicitly use old libtool for build.

* Thu Apr 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt7
- bzlib: Provides: /sbin/bzlib_triggerpostun.

* Fri Nov 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt6
- Explicitly use autoconf-2.13 and automake-1.4 for build.

* Tue Sep 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt5
- Updated %post/%postun scripts.
- Updated devel-static requirements.

* Wed Jun 12 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt4
- Added "Provides: /bin/bunzip, /bin/bunzip2, /bin/bzcat,
  /bin/bzip, /bin/bzip2" to bzip2 subpackage.

* Thu Jun 06 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.2-alt3
- Resurrected bzip2recover (thanks to Nikita Gergel).

* Thu Apr 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.0.2-alt2
- bzlib: added trigger to repair compatibility symlink.

* Mon Feb 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.0.2-alt1
- 1.0.2 (bugfix release).
- Moved utilities to bzip2-utils subpackage.

* Tue Nov 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.0.1-alt2
- Relocated texinfo documentation to bzlib-devel subpackage.

* Fri Oct 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.0.1-alt1
- Added libtool/configure support.
- Added symbol versioning.
- Implemented support for both 0.9 and 1.0 bzlib interfaces.
- Corrected libification.
- Added texinfo documentation.

* Tue Jun 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.1-ipl8mdk
- Updated requires.

* Fri May 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.1-ipl7mdk
- Fixed broken symlink for libbz2.so
- Moved static library to devel-static subpackage.

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl6mdk
- Moved bzip2 from %_bindir to /bin (but keep links to old place).
- Explicit set strip methods.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl5mdk
- Commented out translations in specfile for a while.

* Sat Dec 02 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl4mdk
- Moved bzgrep from %name to %name-devel.
- Moved "Provides: libbz2.so" from bzlib to bzip2-devel.

* Tue Nov 28 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl3mdk
- Moved library into separate subpackage (bzlib).
- Added libbz2.so.1 to bzlib explicit provides list.
- Updated zme script (more robust to user input).

* Tue Aug 29 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl2mdk
- Moved bzless to less package.

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl1mdk
- 1.0.1
- Added URL.
- FHSification.

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.0-ipl1mdk
- Revert to previous naming scheme for exported symbol (without BZ2_ prefixes).
- Provides: libbz2.so (for compatibility with old applications).

* Wed May 17 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.0-1mdk.ldv
- 1.0.0

* Thu Apr 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.0pre7-1mdk.ldv
- merged with Fandra version: new zme script

* Wed Apr 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0pre5-1mdk
- new symlinks for Lord Jeff : bzip & bunzip
- 1.0 pre-release for Lord Chmou

* Wed Mar 22 2000 Pixel <pixel@mandrakesoft.com> 0.9.5d-7mdk
- remove provides bzip2

* Tue Mar 21 2000 Daouda LO <daouda@mandrakesoft.com> 0.9.5d-6mdk
- change to new group architecture

* Sat Mar  4 2000 Pixel <pixel@mandrakesoft.com> 0.9.5d-5mdk
- remove the silly commented out chmod in %post
(that way, bzip2 don't need /bin/sh anymore)

* Thu Mar 02 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix bzme script : now it use a lot less disk space.

* Thu Oct 21 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add bzme script

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Thu Sep 16 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 0.9.5d (sanity fixes such as warnings killers casts)

* Wed Aug 25 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- No really, allow users into the docdir.. (don't put %%attr on %%doc files)

* Wed Aug 25 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- %%defattr(-,root,root,755)

* Tue Aug 17 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix a bug in the spec
- clean spec

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix bogus permissions on doc

* Wed Aug 11 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 0.9.5c

* Thu Aug 05 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- updated to 0.9.5b
- remove unused patch
- merge all packages in one
- clean spec

* Tue Jul  6 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- added overly redundant provides to help clean up install.log's

* Fri May 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add a bzgrep script.

* Fri Apr 16 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.
- Add patch to permit the bunzip2 on link.

* Thu Jan 14 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- version 0.9.0c

* Sun Nov 29 1998 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- remove CC="egcs" - we want to compile with pgcc
- bzip2 manpages
- build a shared libbz2.so; move libbz2 and bzlib.h to bzip2-devel

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- force compilation with egcs to avoid gcc optimization bug (thank God
  we haven't been beaten by it)

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- version 0.9.0b

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.9.0

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- first build for Manhattan
