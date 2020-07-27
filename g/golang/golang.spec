# build ids are not currently generated:
# https://code.google.com/p/go/issues/detail?id=5238
#
# also, debuginfo extraction currently fails with
# "Failed to write file: invalid section alignment"
%global __find_debuginfo_files %nil

# we are shipping the full contents of src in the data subpackage, which
# contains binary-like things (ELF data for tests, etc)
%global _unpackaged_files_terminate_build 1

%global go_arches %ix86 x86_64 aarch64 %arm mipsel ppc64le riscv64
%global go_root %_libdir/golang

%ifarch x86_64
%global go_hostarch  amd64
%endif
%ifarch %ix86
%global go_hostarch  386
%endif
%ifarch %arm
%global go_hostarch  arm
%endif
%ifarch aarch64
%global go_hostarch  arm64
%endif
%ifarch mipsel
%global go_hostarch  mipsle
%endif
%ifarch ppc64le
%global go_hostarch  ppc64le
%endif
%ifarch riscv64
%global go_hostarch  riscv64
%endif


%def_disable check

Name:    golang
Version: 1.14.6
Release: alt1
Summary: The Go Programming Language
Group:   Development/Other
License: BSD
URL:     http://golang.org/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: golang-%version.tar
Source1: golang-gdbinit
Patch2:  golang-alt-certs-path.patch
Patch100: 0001-Don-t-use-the-bundled-tzdata-at-runtime-except-for-t.patch
Patch101: 0001-avoid-requires-libselinux-utils.patch

ExclusiveArch: %go_arches

%set_verify_elf_method skip
%add_debuginfo_skiplist %go_root
%brp_strip_none %go_root/bin/*

AutoReq: nocpp

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libselinux-utils
BuildRequires: libpcre-devel

# for test suite
%{?_enable_check:BuildRequires: /proc}

Provides: go = %version-%release

Provides:  golang-godoc = %version-%release
Obsoletes: golang-godoc

# Due to vet, cover utilities.
Conflicts: golang-tools <= 0-alt1.git7e09e072


%description
Go is expressive, concise, clean, and efficient. Its concurrency mechanisms
make it easy to write programs that get the most out of multicore and
networked machines, while its novel type system enables flexible and
modular program construction.


%package gdb
Summary:   The Go Runtime support for GDB
Group:     Development/Other
Requires:  %name = %version-%release

%description gdb
The Go Runtime support for GDB.


%ifarch x86_64
%package shared
Summary: Golang shared object libraries
Group:   Development/Other

%description shared
%summary.
%endif


%package docs
Summary:   Go sources and documentation
Group:     Documentation
BuildArch: noarch
Requires:  %name = %version-%release

%description docs
Go sources and documentation.


%prep
%setup -q

%patch2 -p1
%patch100 -p1
%patch101 -p1

%build
# go1.5 bootstrapping. The compiler is written in golang.
export GOROOT_BOOTSTRAP=%go_root

# set up final install location
export GOROOT_FINAL=%go_root

export GOHOSTOS=linux
export GOHOSTARCH=%go_hostarch

export GOOS=linux
export GOARCH=%go_hostarch

# use our gcc options for this build, but store gcc as default for compiler
export CC="gcc"
export CC_FOR_TARGET="gcc"
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"

# build
cd src
./make.bash --no-clean
cd ..

%ifarch x86_64
export GOROOT=$PWD
export PATH="$GOROOT/bin:$PATH"

# TODO get linux/386 support for shared objects.
# golang shared objects for stdlib
go install -v -buildmode=shared std
%endif


%check
%if_enabled check
export GOROOT=$PWD
export PATH="$GOROOT/bin:$PATH"
export CGO_ENABLED=0
export CC="gcc"
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"

cd src
./run.bash --no-rebuild -v -k
%endif


%install
# create the top level directories
mkdir -p -- \
	%buildroot/%_bindir \
	%buildroot/%go_root \
	%buildroot/%_datadir/%name

cp -afv api bin doc favicon.ico lib pkg robots.txt src test VERSION \
	%buildroot/%go_root/

find %buildroot/%go_root -exec touch -r $PWD/VERSION "{}" \;

# remove bootstrap files
rm -rfv -- %buildroot/%go_root/pkg/bootstrap

# remove testdata, tests, and non-go files
find \
	%buildroot/%go_root/src \
	\( \
		\( -type d -name 'testdata'   \) -o \
		\( -type f -name 'Makefile'   \) -o \
		\( -type f -name '*_test.go'  \) -o \
		\( -type f -name 'test_*'     \) -o \
		\( -type f -name '*test.bash' \) -o \
		\( -type f -name 'test.'      \) \
	\) \
		-print0 |
	xargs -0 rm -rfv --

# remove scripts for other platform.
find \
	%buildroot/%go_root/src \
		-maxdepth 1 \
	\( \
		\( -type f -name '*.rc'  \) -o \
		\( -type f -name '*.bat' \)    \
	\) \
		-print0 |
	xargs -0 rm -fv --

# remove the unnecessary zoneinfo file (Go will always use the system one first)
rm -rfv -- \
	%buildroot/%go_root/lib/time

# add symlinks for binaries.
for z in %buildroot%go_root/bin/*; do
	[ -x "$z" ] || continue

	n="${z##*/}"
	path="$(relative "$z" "%buildroot/%_bindir/$n")"

	ln -sv -- "$path" %buildroot/%_bindir/$n
done

# https://golang.org/doc/go1.5#moving
# Because the go/types package has now moved into the main repository (see below),
# the vet and cover tools have also been moved. They are no longer maintained in
# the external golang.org/x/tools repository, although (deprecated) source still
# resides there for compatibility with old releases.
for z in cover vet; do
	z="%buildroot%go_root/pkg/tool/linux_%{go_hostarch}/$z"
	[ -x "$z" ] || continue

	n="${z##*/}"
	path="$(relative "$z" "%buildroot/%_bindir/$n")"

	ln -sv -- "$path" %buildroot/%_bindir/$n
done

# restore the gdb debugging script, needed at runtime by gdb
mkdir -p -- %buildroot/%_datadir/%name/gdb
sed \
    -e 's,@GOROOT@,%go_root,g' \
    %SOURCE1 > %buildroot/%_datadir/%name/gdb/golang-gdbinit

mkdir -p -- %buildroot/%_datadir/%name/src
for n in syscall regexp; do
	mkdir -- %buildroot/%_datadir/%name/src/$n

	find %buildroot/%go_root/src/$n \
		\( \
			\( -type f -name '*.sh' \) -o \
			\( -type f -name '*.pl' \)    \
		\) \
			-print0 |
		xargs -0 mv -fvt %buildroot/%_datadir/%name/src/$n --
done

# ensure these exist and are owned
mkdir -p -- \
	%buildroot/%go_path/src/github.com \
	%buildroot/%go_path/src/bitbucket.org \
	%buildroot/%go_path/src/code.google.com/p \
	%buildroot/%go_path/src/golang.org/x \
#

%files
%_bindir/*
%go_root
%go_path

%exclude %go_root/src/runtime/runtime-gdb.py*

%ifarch x86_64
%exclude %go_root/pkg/linux_%{go_hostarch}_dynlink

%files shared
%go_root/pkg/linux_%{go_hostarch}_dynlink
%endif


%files gdb
%_datadir/%name/gdb
%go_root/src/runtime/runtime-gdb.py*


%files docs
%dir %_datadir/%name
%_datadir/%name/src

%doc AUTHORS CONTRIBUTORS LICENSE PATENTS VERSION


%changelog
* Thu Jul 23 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.6-alt1
- New version (1.14.6). (Fixes: CVE-2020-15586, CVE-2020-14039)

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.4-alt1
- New version (1.14.4).

* Sun May 17 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt2
- merge chanlog with p9

* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt1
- New version (1.14.3).

* Sat May 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.2-alt2
- avoid requires libselinux-utils.

* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.2-alt1
- 1.14.2

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Feb 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.14-alt1
- 1.14
- Build on riscv64

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.8-alt1
- 1.13.8

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.17-alt1
- 1.12.17

* Tue Jan 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.6-alt1
- 1.13.6

* Tue Jan 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.15-alt1
- 1.12.15

* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.5-alt1
- 1.13.5

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.4-alt1
- 1.13.4 (Fixes: CVE-2019-17596)

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.13-alt1
- New version (1.12.13).

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.11-alt1
- New version (1.12.11). (Fixes: CVE-2019-17596)

* Thu Oct 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.1-alt1
- 1.13.1

* Thu Oct 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.10-alt1
- New version (1.12.10). (Fixes: CVE-2019-16276)

* Thu Sep 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.13-alt1
- 1.13

* Mon Aug 19 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.9-alt1
- 1.12.9 (Fixes: CVE-2019-14809, CVE-2019-9512, CVE-2019-9514)

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.7-alt1
- New version (1.12.7).

* Tue Jun 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.6-alt1
- New version (1.12.6).

* Fri Apr 12 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.4-alt1
- 1.12.4

* Wed Mar 27 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- New version (1.12.1).
- Apply timezone patch, avoid using bundled data

* Thu Jan 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.5-alt1
- 1.11.5
- fixed CPU DoS vulnerability affecting P-521 and P-384 (Fixes: CVE-2019-6486)
- add ppc64le to go_arches

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.4-alt1
- New version (1.11.4).

* Thu Jan 17 2019 Ivan A. Melnikov <iv@altlinux.org> 1.11.2-alt1.0.mips1
- Build on mipsel.

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- New version (1.11.2).

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- New version (1.11.1).

* Fri Sep 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.11-alt1
- New version (1.11).

* Fri Jun 22 2018 Alexey Shabalin <shaba@altlinux.ru> 1.10.3-alt1
- New version (1.10.3).
- backport patches from upstream for aarch64

* Thu May 03 2018 Alexey Gladkov <legion@altlinux.ru> 1.10.2-alt1
- New version (1.10.2).

* Wed Jan 10 2018 Alexey Gladkov <legion@altlinux.ru> 1.9.2-alt1
- New version (1.9.2).

* Tue Aug 29 2017 Alexey Gladkov <legion@altlinux.ru> 1.9-alt2
- Enable build for aarch64.

* Mon Aug 28 2017 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1
- New version (1.9).

* Fri Apr 07 2017 Alexey Gladkov <legion@altlinux.ru> 1.8.1-alt1
- New version (1.8.1).

* Tue Aug 16 2016 Alexey Gladkov <legion@altlinux.ru> 1.7-alt1
- New version (1.7).

* Mon Feb 29 2016 Alexey Gladkov <legion@altlinux.ru> 1.6-alt1
- New version (1.6).

* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 1.5.3-alt1
- New version (1.5.3).

* Tue Sep 22 2015 Alexey Gladkov <legion@altlinux.ru> 1.5.1-alt1
- New version (1.5.1).
- The vet and cover tools have been moved to this package.

* Sun May 03 2015 Alexey Gladkov <legion@altlinux.ru> 1.4.2-alt1
- New version (1.4.2).
- Disable tests.

* Fri Dec 12 2014 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- New version (1.4).
- Drop vim subpackage.

* Mon Jun 23 2014 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- New version (1.3).

* Tue Dec 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.2-alt1
- New version (1.2).

* Mon Oct 28 2013 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt2
- Add gdb and vim plugins.
- Fix rebuild command (ALT#29508).

* Thu Oct 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt1
- New version (1.1.2).
- Fix ssl certs search path (ALT#29449).

* Fri Jun 14 2013 Alexey Gladkov <legion@altlinux.ru> 1.1-alt1
- First build for ALTLinux.

* Sat May 25 2013 Dan Horák <dan[at]danny.cz> - 1.1-3
- set ExclusiveArch

* Fri May 24 2013 Adam Goode <adam@spicenitz.org> - 1.1-2
- Fix noarch package discrepancies

* Fri May 24 2013 Adam Goode <adam@spicenitz.org> - 1.1-1
- Initial Fedora release.
- Update to 1.1

* Thu May  9 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.3.rc3
- Update to rc3

* Thu Apr 11 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.2.beta2
- Update to beta2

* Tue Apr  9 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.1.beta1
- Initial packaging.
