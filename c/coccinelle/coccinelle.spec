# coccinelle.spec
%define _unpackaged_files_terminate_build 1

Name:		coccinelle
Version:	1.0.8
Release:	alt7
Summary:	Semantic patching for Linux (spatch)

Group:		Development/C
License:	GPL-2.0-only
Url:		http://coccinelle.lip6.fr/

Source:		%name-%version.tar
Provides:	spatch

BuildRequires(pre): rpm-build-ocaml
BuildRequires(pre): rpm-build-python3
BuildRequires:	ocaml >= 3.12.1
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamldoc
BuildRequires:	ocaml-menhir
BuildRequires:	ocaml-stdcompat-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-parmap-devel
BuildRequires:	python3-dev

Requires:	python3-dev

# Bogus internal name
%filter_from_requires /^python.*(coccinelle)/d
# Bogus dependencies to OCaml
AutoReqProv: noocaml
# Only what's matter
Provides: ocaml-cmi(Coccilib) = %version-%release
Provides: ocaml-cmx(Coccilib) = %version-%release
# No cocciguis (pida for vim, gtk output), yet
%add_findreq_skiplist %python3_sitelibdir/coccilib/coccigui/*
# No trac integraion
%add_findreq_skiplist %python3_sitelibdir/coccilib/trac.py

%description
Coccinelle (French for "ladybug") is a utility for matching and transforming
the source code of programs written in the C programming language.

The source code to be matched or replaced is specified using
a "semantic patch" syntax based on the patch syntax.
The Semantic Patch Language (SmPL) pattern resembles a unified diff
with C-like declarations.

Coccinelle was initially used to aid the evolution of the Linux kernel
(and ease the maintenance of device drivers), providing support for
changes to APIs such as renaming a function, adding a function
argument whose value is somehow context-dependent, and reorganizing a
data structure.

It can also be used to find bad programming patterns in code (i.e.,
pieces of code that are erroneous with high probability such as
possible NULL pointer dereference) without transforming them.
(Then coccinelle's role is close to that of static analysis tools.)

%package demos
%global demos_summary Demos of coccinelle semantic patches with C code examples
Summary: %demos_summary
Group: Documentation
Requires: %name
BuildArch: noarch

%description demos
%demos_summary.

They can be applied to the corresponding C code examples by a command like:

  spatch -sp_file F.cocci F.c

and you'll get a normal patch for this C code example.

The tests from coccinelle are also included in this package; they can be run with:

  spatch --testall --no-update-score-file

in the directory which includes the tests/ subdir (with *.res files).

%package checkinstall
%global checkinstall_summary Immediately run some tests for %name
Summary: %checkinstall_summary
Group: Other
Requires: %name-demos
BuildArch: noarch

%description checkinstall
%checkinstall_summary.

%prep
%setup -q -n %{name}-%{version}
sed -i '1s:^#!/usr/bin/env python$:#!/usr/bin/python3:' tools/pycocci

%build
./autogen
%configure \
	--with-python=%_bindir/python3 \

make EXTLIBDIR=`ocamlc -where`/extlib

%install
make DESTDIR=%buildroot install

# relocate python module
install -d %buildroot%python3_sitelibdir
mv %buildroot%_libdir/coccinelle/python/coccilib %buildroot%python3_sitelibdir/
rm -rf %buildroot%_libdir/coccinelle/python

# Somebody forgot to install this
install ./tools/pycocci %buildroot%_bindir/pycocci

%check
%define run_tests \
demos=( \
        simple # a simple demo \
        python_identifier # with embedded Python \
) \
for f in "${demos[@]}"; do \
    %spatch -sp_file demos/"$f".{cocci,c} \
done \
%nil

export COCCINELLE_HOME=%buildroot%_libdir/coccinelle
export PYTHONPATH=%buildroot%python3_sitelibdir
%global spatch %buildroot%_bindir/spatch
%run_tests

%pre checkinstall -p %_sbindir/sh-safely
cd %_docdir/%name-demos-%version
%global spatch spatch
%run_tests

%files
%doc authors.txt bugs.txt changes.txt copyright.txt credits.txt
%doc license.txt readme.txt
%_bindir/pycocci
%_bindir/spatch
%_bindir/spgen
%_libdir/%name/
%python3_sitelibdir/coccilib
%_man1dir/*.1*
%_man3dir/Coccilib.3cocci*
/usr/share/bash-completion/completions/spatch

%files demos
%doc demos tests

%files checkinstall

%changelog
* Fri May 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.0.8-alt7
- fix changelog

* Wed Apr 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.0.8-alt6
- merge changes from p9 branch (imz@altlinux.org)

* Mon Apr 20 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt5
- spec: Fix `Cannot infer Python version'.

* Sat Apr 18 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt4
- Convert to python3, add spgen, delete spatch.opt, clean up reqs.

* Sat Apr 18 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt3
- Install coccinelle ocaml libs (for coccicheck).

* Thu Mar 05 2020 Anton Farygin <rider@altlinux.ru> 1.0.8-alt2
- removed unsafe-string build flag to avoid problems with ocaml-4.10
- built with external stdcompat
- removed chrpath from build dependencies (it is no longer required)

* Mon Feb 17 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt1
- Update to 1.0.8.

* Thu Dec 19 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt2
- Adapted BuildReqs for any OCaml (whether with "num" or without in the core),
  so that it can be built in Sisyphus/p9 and p8.
- For testing, made a checkinstall subpkg and added more tests
  (with embedded Python scripts).
- Worked-around the problem with the loading of libpython (to enable
  the built-in Python interpreter).

* Wed Aug 07 2019 Vitaly Chikunov <vt@altlinux.org> 1.0.7.0.217.ged1eb8e0-alt1
- Update to 1.0.7-217-ged1eb8e0.

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0.6-alt1
- Initial build for ALT.
