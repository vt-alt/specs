%define soname 0

Name: argon2
Version: 20190702
Release: alt1

Summary: The password-hashing tools
License: Public Domain or ASL 2.0
Group: System/Base

Url: https://github.com/P-H-C/phc-winner-argon2
# Git-VCS: https://github.com/P-H-C/phc-winner-argon2.git
Source: %name-%version.tar

Requires: lib%name = %EVR

%description
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.

It has a simple design aimed at the highest memory filling rate and
effective use of multiple computing units, while still providing defense
against tradeoff attacks (by exploiting the cache and memory organization
of the recent processors).

Argon2 has three variants: Argon2i, Argon2d, and Argon2id.

* Argon2d is faster and uses data-depending memory access, which makes it
  highly resistant against GPU cracking attacks and suitable for applications
  with no threats from side-channel timing attacks (eg. cryptocurrencies).
* Argon2i instead uses data-independent memory access, which is preferred for
  password hashing and password-based key derivation, but it is slower as it
  makes more passes over the memory to protect from tradeoff attacks.
* Argon2id is a hybrid of Argon2i and Argon2d, using a combination of
  data-depending and data-independent memory accesses, which gives some of
  Argon2i's resistance to side-channel cache timing attacks and much of
  Argon2d's resistance to GPU cracking attacks.

%package -n lib%name
Group: System/Libraries
Summary: The password-hashing library

%description -n lib%name
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for lib%name
Requires: lib%name = %EVR

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name.

%prep
%setup

# Honour default RPM build options and library path, do not use -march=native
sed -e 's:-O3 -Wall:%optflags:' \
    -e 's:-march=\$(OPTTARGET) :${CFLAGS} :' \
    -e 's:CFLAGS += -march=\$(OPTTARGET)::' \
    -i Makefile

%ifarch %e2k
# lcc 1.23's edg frontend can only do numbers here (#4061)
sed -i 's,"O0",0,' src/core.c
%endif

%build
# parallel build is not supported
%make ARGON2_VERSION=%version LIBRARY_REL=%_lib 

%install
%makeinstall_std ARGON2_VERSION=%version LIBRARY_REL=%_lib

# Drop static library
rm %buildroot%_libdir/lib%name.a

# Relocate shared libraries from %%_libdir/ to /%%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
       t=$(readlink -v "$f")
       ln -fnrs %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%check
%make test

%files
%_bindir/%name

%files -n lib%name
/%_lib/*.so.*

%files -n lib%name-devel
%doc *.md
%_includedir/%name.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Jul 31 2019 Alexey Shabalin <shaba@altlinux.org> 20190702-alt1
- 20190702

* Sat May 11 2019 Michael Shigorin <mike@altlinux.org> 20171227-alt3
- fixed build with lcc on e2k
- minor spec cleanup

* Fri Nov 23 2018 Andrey Bychkov <mrdrew@altlinux.org> 20171227-alt2
- broke tag re-signed

* Fri Jan 26 2018 Alexey Shabalin <shaba@altlinux.ru> 20171227-alt1
- initial package (based on fedora spec)
