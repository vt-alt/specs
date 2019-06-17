Name: mpir
Version: 3.0.0
Release: alt4
Summary: A library for arbitrary precision arithmetic

License: LGPLv3+
Group: System/Libraries
Url: http://mpir.org/
Packager: Anton Midyukov <antohami@altlinux.org>

# Repacked http://mpir.org/%name-%version.tar.bz2
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++
BuildRequires: texinfo
BuildRequires: yasm

%description
MPIR is an open source multiprecision integer library derived from
version 4.2.1 of the GMP (GNU Multi Precision) project.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

# Convert ISO-8859-1 files to UTF-8, preserving timestamps
for fil in NEWS doc/devel/projects.html doc/devel/tasks.html; do
  iconv --from=ISO-8859-1 --to=UTF-8 $fil -o $fil.conv
  sed -i 's/charset=iso-8859-1/charset=UTF-8/' $fil
  touch -r $fil $fil.conv
  mv -f $fil.conv $fil
done

# Update texinfo.tex
cp -p %_datadir/texmf/tex/texinfo/texinfo.tex doc

%build
%autoreconf
%ifarch ppc64le
export ABI=mode64
export MPN_PATH=generic
%endif
%configure --disable-static --enable-cxx --with-yasm=%_bindir/yasm \
  CCAS="gcc -c -Wa,--noexecstack" \
  LIBS="-lrt" \
  LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed -Wl,-z,noexecstack"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g.*\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Compile
export LD_LIBRARY_PATH=$PWD/.libs
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -exec rm -f {} ';'
rm -rf %buildroot%_infodir/dir
mv doc/devel doc/html

%check
# FTBFS i586
#export LD_LIBRARY_PATH=$PWD/.libs
#make check

%files
%doc AUTHORS NEWS README
%doc COPYING COPYING.LIB
%_libdir/*.so.*

%files devel
%doc doc/html doc/isa_abi_headache
%_includedir/*
%_libdir/*.so
%_infodir/mpir.info*

%changelog
* Tue Jun 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.0-alt4
- Fixed build on ppc64le.
- Dropped useless aarch64 patch.

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt3
- NMU: remove %ubt from release

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt2%ubt
- Rebuilt for aarch64

* Fri Jan 05 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1%ubt
- Initial build for ALT Sisyphus.
