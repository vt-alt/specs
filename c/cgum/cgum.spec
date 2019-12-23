%define _unpackaged_files_terminate_build 1

Name:    cgum
Version: 1.0.1
Release: alt2
Summary: The C parser for GumTree
Group:   Development/Other
License: GPLv2
Url:     https://github.com/GumTreeDiff/cgum

# https://github.com/GumTreeDiff/cgum.git
Source: %name-%version.tar

Patch1: %name-%version-alt-paths.patch

BuildRequires: ocaml
#BuildRequires:	ocaml-num-devel
# -- be more flexible (no matter whether "num" is included in core OCaml
# as before in p8 or not as now is Sisyphus);
# let's substitute the pkg dep by a dep on an arbitrary module from it:
BuildPreReq: ocaml-cmx(Num)

Requires: coccinelle

%description
This project is a parser that converts C files to a XML format.
It is mainly used as a backend in GumTree diff tool.

%prep
%setup
%patch1 -p1

find . -type f | xargs sed -i \
	-e "s:@DATADIR@:%_datadir:g" \
	-e "s:@LIBDIR@:%_libdir:g" \
	%nil

%build
%make cgum.opt

%install
install -d %buildroot{%_bindir,%_datadir/cgum}
install -m755 cgum.opt %buildroot%_bindir/cgum
install -m755 cgumw %buildroot%_bindir/
install -m644 standard.h %buildroot%_datadir/cgum/

%files
%_bindir/*
%_datadir/cgum

%changelog
* Thu Dec 19 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2
- Made BuildReqs more flexible. (So that it builds both in Sisyphus and p8;
  no matter whether "num" is included in core OCaml.)

* Fri Nov 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
