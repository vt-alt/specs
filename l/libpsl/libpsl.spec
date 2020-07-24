%def_disable bootstrap
%def_disable builtin

Name: libpsl
Version: 0.21.1
Release: alt1

Summary: C library for the Public Suffix List
License: MIT
Group: System/Libraries
URL: https://github.com/rockdaboot/libpsl
Vcs: https://github.com/rockdaboot/libpsl.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%if_disabled bootstrap
BuildRequires: glib2-devel libgio-devel
BuildRequires: python3
%{?_enable_builtin:BuildRequires: libicu-devel}
BuildRequires: libidn2-devel
BuildRequires: libunistring-devel
BuildRequires: gtk-doc xsltproc
BuildRequires: publicsuffix-list
BuildRequires: publicsuffix-list-dafsa
%endif

Requires: publicsuffix-list-dafsa

%define _unpackaged_files_terminate_build 1

%description
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: publicsuffix-list

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: This package contains development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: %name-devel = %version-%release

%description devel-doc
This package contains development documentation for %name

%package -n psl
Group: Networking/DNS
Summary: Commandline utility to explore the Public Suffix List

%description -n psl
This package contains a commandline utility to explore the Public Suffix List,
for example it checks if domains are public suffixes, checks if cookie-domain
is acceptable for domains and so on.

%package -n psl-make-dafsa
Group: Networking/DNS
Summary: Compiles the Public Suffix List into DAFSA form
BuildArch: noarch

%description -n psl-make-dafsa
This script produces C/C++ code or an architecture-independent binary object
which represents a Deterministic Acyclic Finite State Automaton (DAFSA)
from a plain text Public Suffix List.

%prep
%setup
%patch -p1

%if_disabled bootstrap
%build
%autoreconf
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-cfi \
	--disable-ubsan \
	--disable-asan \
	--enable-man \
	--enable-gtk-doc \
%if_enabled builtin
	--enable-builtin=libicu \
%else
	--disable-builtin \
%endif
	--enable-runtime=libidn2 \
	--with-psl-distfile=%_datadir/publicsuffix/public_suffix_list.dafsa \
	--with-psl-file=%_datadir/publicsuffix/effective_tld_names.dat \
	--with-psl-testfile=%_datadir/publicsuffix/test_psl.txt
%make_build

%install
%makeinstall_std
# the script is noinst but the manpage is installed
install -Dm0755 src/psl-make-dafsa %buildroot%_bindir/psl-make-dafsa
%else # bootstrap
install -Dm0755 src/psl-make-dafsa %buildroot%_bindir/psl-make-dafsa
install -Dm0644 src/psl-make-dafsa.1 %buildroot%_man1dir/psl-make-dafsa.1
%endif # bootstrap

%if_disabled bootstrap
%check
make check

%files
%doc COPYING
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_man3dir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%files -n psl
%doc AUTHORS NEWS COPYING
%_bindir/psl
%_man1dir/psl.1*
%endif # bootstrap

%files -n psl-make-dafsa
%doc COPYING
%_bindir/psl-make-dafsa
%_man1dir/psl-make-dafsa.1*

%changelog
* Tue Jul 21 2020 Mikhail Efremov <sem@altlinux.org> 0.21.1-alt1
- Add Vcs tag.
- Don't use rpm-build-licenses.
- 0.21.0 -> 0.21.1.

* Tue Sep 03 2019 Mikhail Efremov <sem@altlinux.org> 0.21.0-alt2
- Patch from upstream:
  + gtk-doc: do not include tree_index.sgml.

* Wed Apr 17 2019 Mikhail Efremov <sem@altlinux.org> 0.21.0-alt1
- BR: python -> python3.
- psl-make-dafsa: Use python3.
- Patch from upstream:
  + Fix build when configured with --with-psl-file.
- Make psl-make-dafsa noarch.
- 0.20.2 -> 0.21.0.

* Wed Nov 07 2018 Mikhail Efremov <sem@altlinux.org> 0.20.2-alt2
- Disable builtin PSL.

* Fri Apr 27 2018 Mikhail Efremov <sem@altlinux.org> 0.20.2-alt1
- 0.20.1 -> 0.20.2.

* Wed Mar 14 2018 Mikhail Efremov <sem@altlinux.org> 0.20.1-alt1
- 0.19.1 -> 0.20.1.

* Thu Nov 23 2017 Mikhail Efremov <sem@altlinux.org> 0.19.1-alt1
- New version.

* Mon Jul 31 2017 Mikhail Efremov <sem@altlinux.org> 0.18.0-alt1
- Explicitly disable sanitizers.
- Fix bootstrap.
- New version.

* Fri Apr 07 2017 Mikhail Efremov <sem@altlinux.org> 0.17.0-alt2
- Initail build.
- Patch from upstream:
  + Fix order of files in psl_latest().

* Fri Apr 07 2017 Mikhail Efremov <sem@altlinux.org> 0.17.0-alt1
- Bootstrap build (psl-make-dafsa only).
