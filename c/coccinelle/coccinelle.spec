%define _unpackaged_files_terminate_build 1

Name:		coccinelle
Version:	1.0.6
Release:	alt2
Summary:	Semantic patching for C source code (spatch)

Group:		Development/C
License:	GPLv2
Url:		http://coccinelle.lip6.fr/

Source:		%name-%version.tar
Provides:	spatch

#BuildRequires:	ocaml-num-devel
# -- be more flexible (no matter whether "num" is included in core OCaml
# as before in p8 or not as now is Sisyphus);
# let's substitute the pkg dep by a dep on an arbitrary module from it:
BuildPreReq: ocaml-cmx(Num)

BuildRequires:	ocaml >= 3.12.1
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamldoc
BuildRequires:	ocaml-menhir
BuildRequires:	ocaml-pcre-devel
BuildRequires:	rpm-build-python python-devel python-modules-multiprocessing
BuildRequires:	chrpath

# only if vim coccigui is used
%filter_from_requires /^python.*(pida)$/d
# bogus internal name
%filter_from_requires /^python.*(coccinelle)$/d

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
sed -i '1s:^#!/usr/bin/env python$:#!/usr/bin/python%__python_version:' tools/pycocci

%build
./autogen
%configure
# -unsafe-string
export OCAMLPARAM="safe-string=0,_"
make EXTLIBDIR=`ocamlc -where`/extlib

%install
make DESTDIR=%buildroot install
rm -rf %buildroot%_libdir/coccinelle/ocaml
# relocate python module
install -d %buildroot%python_sitelibdir
mv %buildroot%_libdir/coccinelle/python/coccilib %buildroot%python_sitelibdir/
rm -rf %buildroot%_libdir/coccinelle/python

# Make "libpython*.so" findable for coccinelle even without the python-dev pkg;
# otherwise, the embedded Python interpreter won't work
# and *.cocci scripts with embedded Python scripts would fail. (This is checked
# in %%check and the checkinstall subpackage.)
# (TODO: it looks for the simple "*.so" filename in runtime, but this should be
# fixed--in the bundled pyml probably; BTW, why not package pyml unbundled?)
ln -s -v "$(realpath %__libpython)" \
   -T %buildroot%_libdir/%name/"$(basename %__libpython)"

# delete spgen
rm -rf %buildroot%_bindir/spgen
rm -rf %buildroot%_libdir/coccinelle/spgen
rm -rf %buildroot%_mandir/man1/spgen.*
rm -rf %buildroot%_mandir/man3

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
export PYTHONPATH=%buildroot%python_sitelibdir
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
%_bindir/spatch.opt
%_libdir/%name/
%python_sitelibdir/coccilib
%_mandir/man1/*.1*

%files demos
%doc demos tests

%files checkinstall

%changelog
* Thu Dec 19 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt2
- Adapted BuildReqs for any OCaml (whether with "num" or without in the core),
  so that it can be built in Sisyphus/p9 and p8.
- For testing, made a checkinstall subpkg and added more tests
  (with embedded Python scripts).
- Worked-around the problem with the loading of libpython (to enable
  the built-in Python interpreter).

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0.6-alt1
- Initial build for ALT.
