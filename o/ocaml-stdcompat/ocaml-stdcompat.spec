%set_verify_elf_method textrel=relaxed
%define libname stdcompat
Name: ocaml-%libname
Version: 13
Release: alt1
Summary: Compatibility module for OCaml standard library
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/thierry-martinez/stdcompat
Source0: %name-%version.tar
BuildRequires: ocaml-result-devel dune opam

%description
Compatibility module for OCaml standard library allowing programs to use some
recent additions to the OCaml standard library while preserving the ability to
be compiled on former versions of OCaml.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make -f Makefile.bootstrap
%configure --libdir=%_libdir/ocaml
%make

%install
%makeinstall_std


%files
%doc README.md ChangeLog COPYING 
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.cmt*
%exclude %_libdir/ocaml/%libname/*.ml
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmxs


%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.ml
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%changelog
* Thu Mar 05 2020 Anton Farygin <rider@altlinux.ru> 13-alt1
- first build for ALT

