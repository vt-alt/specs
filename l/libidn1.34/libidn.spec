Name: libidn1.34
Version: 1.34
Release: alt1

Summary: Internationalized Domain Name support library
Group: System/Libraries
License: LGPLv3+/GPLv2+ and GPLv3+ and GFDL
Url: http://www.gnu.org/software/%name/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

# Fix ABI compatibility with libidn-1.33 and earlier
Patch: libidn-tablesize-revert.patch

BuildRequires: gtk-doc makeinfo

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%prep
%setup
%patch -p1

%build
%autoreconf
# These gnulib tests fail.
sed -i 's/test-\(rwlock1\|thread_create\)\$(EXEEXT) //' lib/gltests/Makefile.in
sed -i 's/test-\(rwlock1\|thread_create\)\$(EXEEXT) //' gltests/Makefile.in
%configure \
	--disable-rpath \
	--disable-static \
	--disable-silent-rules

# remove RPATH hardcoding
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# without RPATH this needs to be set for idn executed by help2man
export LD_LIBRARY_PATH=$(pwd)/lib/.libs

%make_build

%install
%set_verify_elf_method strict
%makeinstall_std
rm -rf %buildroot%_infodir

%files
/%_libdir/*.so.*

%changelog
* Wed Jul 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.34-alt1
- Build old version for support of legacy software.
