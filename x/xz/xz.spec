Name: xz
Version: 5.2.5
Release: alt1

Summary: LZMA/XZ compression programs
# We don't package scripts to grep, diff, and view compressed files here
# because they are already packaged in gzip-utils.
# see COPYING
License: ALT-Public-Domain
Group: Archiving/Compression
URL: http://tukaani.org/xz/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: liblzma = %version-%release

# Last lzma-utils version was 4.32.7
Provides: lzma-utils = 4.32.9
Obsoletes: lzma-utils < 4.32.9

# Automatically added by buildreq on Fri Jul 20 2012
# optimized out: xz
BuildRequires: glibc-devel-static

%description
This package provides a set of gzip-style tools for working with
files compressed with the Lempel-Ziv/Markov-chain compression method.
It supports two formats: .xz and the older .lzma format.

%package -n liblzma
Summary: LZMA/XZ compression library
Group: System/Libraries

%package -n liblzma-devel
Summary: API headers and other development files related to liblzma
Group: Development/C
Requires: liblzma = %version-%release
Conflicts: lzmalib-devel

%package -n liblzma-devel-static
Summary: Static liblzma compression library
Group: Development/C
Requires: liblzma-devel = %version-%release

%description -n liblzma
This package provides data compression library for working with
files compressed with the Lempel-Ziv/Markov-chain compression method.
It supports two formats: .xz and the older .lzma format.

%description -n liblzma-devel
This package contains the API headers, development library, and
other development files related to liblzma

%description -n liblzma-devel-static
This package contains static liblzma compression library.

%prep
%setup -q
%patch -p1

%build
%ifarch %ix86
# liblzma uses crc*_x86.S asm code on i686
%add_optflags -Wa,--generate-missing-build-notes=yes
%endif

%autoreconf
%define docdir %_docdir/%name-%version
%configure --enable-dynamic --disable-scripts --docdir=%docdir
cflags=$(sed -n 's/^CFLAGS = //p' src/liblzma/Makefile)
%make_build -C src/liblzma CFLAGS="${cflags:?} %{!?_enable_debug:-O3}" liblzma_la-lzma_decoder.lo
%make_build

%def_enable profile
%if_enabled profile
tar cf .tar */*/*.o */*.[ch] */*/*.[ch] */*/*/*.[ch] */*/*/*/*.[ch] \
	*/*.txt tests/files */*/.libs/*.{o,so*} --sort=name --mtime=@2718281828
md5sum .tar
rm src/liblzma/*.lo src/liblzma/liblzma.la
%make_build -C src/liblzma CFLAGS="$cflags -fprofile-generate %{!?_enable_debug:-O3}" liblzma_la-lzma_decoder.lo
%make_build -C src/liblzma CFLAGS="$cflags -fprofile-generate"
./libtool --tag=CC --mode=link gcc %optflags -fprofile-generate -static src/xz/xz-*.o src/liblzma/liblzma.la -o xz.static
for i in '0 -C none' '2 -C crc32' '6 --arm --lzma2 -C crc64' '6 --x86 --lzma2=lc=4 -C sha256' '7e --format=lzma'; do
	./src/xz/xz -$i <.tar |./xz.static -d >/dev/null
	./xz.static -$i <.tar |./src/xz/xz -d >/dev/null
done
rm src/liblzma/*.lo src/liblzma/liblzma.la
%make_build -C src/liblzma CFLAGS="$cflags -fprofile-use %{!?_enable_debug:-O3}" liblzma_la-lzma_decoder.lo
%make_build -C src/liblzma CFLAGS="$cflags -fprofile-use"
%make_build
readelf -n src/liblzma/.libs/*.so
%endif

%install
%makeinstall_std

# Relocate shared library from %_libdir/ to /lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/liblzma.so; do
	t=$(readlink "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# GPL'ed files are not packaged.
rm %buildroot%docdir/COPYING.GPL*

%find_lang xz

%check
make -k check

%files -f xz.lang
%_bindir/*lz*
%_bindir/*xz*
%_man1dir/*lz*.1*
%_man1dir/*xz*.1*

%files -n liblzma
/%_lib/liblzma.so.*
%docdir
%exclude %docdir/examples*
%exclude %docdir/*-file-format.txt

%files -n liblzma-devel
%_includedir/lzma.h
%_includedir/lzma/
%_libdir/liblzma.so
%_pkgconfigdir/liblzma.pc
%dir %docdir
%docdir/examples*
%docdir/*-file-format.txt

%files -n liblzma-devel-static
%_libdir/liblzma.a

%changelog
* Mon Mar 23 2020 Dmitry V. Levin <ldv@altlinux.org> 5.2.5-alt1
- 5.2.4 -> v5.2.5-2-gcf1ec551.

* Sat Dec 29 2018 Dmitry V. Levin <ldv@altlinux.org> 5.2.4-alt1
- 5.2.3 -> 5.2.4.

* Sat Jan 27 2018 Alexey Tourbin <at@altlinux.ru> 5.2.3-alt2
- Fixed liblzma.so non-reproducible build due to -fprofile-* options.

* Sat Jul 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.2.3-alt1
- 5.0.7 -> 5.2.3.

* Sat Nov 15 2014 Dmitry V. Levin <ldv@altlinux.org> 5.0.7-alt1
- 5.0.5 -> 5.0.7.

* Sun Sep 29 2013 Dmitry V. Levin <ldv@altlinux.org> 5.0.5-alt1
- Updated to 5.0.5 (closes: #29406).

* Fri Jul 20 2012 Alexey Tourbin <at@altlinux.ru> 5.0.4-alt1
- 5.0.3 -> 5.0.4

* Mon May 30 2011 Alexey Tourbin <at@altlinux.ru> 5.0.3-alt1
- Updated to v5.0.3.

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 5.0.1-alt1
- Updated to v5.0.1.

* Wed Jan 05 2011 Alexey Tourbin <at@altlinux.ru> 5.0.0-alt2
- Compiled lzma_decoder.c with -O3; compiled liblzma with -fprofile-*
  options (3%% speed-up).

* Wed Nov 17 2010 Dmitry V. Levin <ldv@altlinux.org> 5.0.0-alt1
- Updated to v5.0.0-3-g3e56470.
- Updated summaries and descriptions.
- Enabled test suite.

* Sun Oct 10 2010 Alexey Tourbin <at@altlinux.ru> 4.999.9-alt1.1
- rebuilt for soname set-versions

* Thu Sep 24 2009 Alexey Tourbin <at@altlinux.ru> 4.999.9-alt1
- updated to v4.999.9beta-22-g49cfc8d
- the code is now under Public Domain
- new package xz replaces older lzma-utils
- packaged liblzma shared library

* Sun May 10 2009 Alexey Tourbin <at@altlinux.ru> 4.999.3alpha-alt2
- rebuilt with gcc-4.4

* Sat May 24 2008 Alexey Tourbin <at@altlinux.ru> 4.999.3alpha-alt1
- initial revision, based on v4.999.3alpha-6-g11de5d5
- only static liblzma.a library is packaged, due to alpha status
