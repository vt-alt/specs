# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: blktrace
Version: 1.2.0
Release: alt1
Summary: Block queue IO tracer
License: GPL-2.0-only
Group: Development/Debuggers
Url: https://git.kernel.dk/cgit/blktrace/
Vcs: git://git.kernel.dk/blktrace.git

Source: %name-%version.tar
BuildRequires: libaio-devel

# Avoid: "forbidden requires: python-base
# sisyphus_check: check-deps ERROR: package dependencies violation"
AutoReqProv: nopython noshebang

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations up to user space.

%prep
%setup

%build
%make_build CFLAGS="%optflags"
# No building docs to avoid bringing texlive monster.

%install
%makeinstall_std \
	prefix=%prefix \
	mandir=%_mandir

%check
%buildroot%_bindir/blkparse -V
%buildroot%_bindir/btreplay -V
%buildroot%_bindir/btrecord -V
%buildroot%_bindir/btt -V
%buildroot%_bindir/blkiomon -V
# blktrace itself will just segfault, becasue no access to `/sys/devices/system/cpu/online`.
# Other proggies do not support `-V`.

%files
%doc README doc/blktrace.tex
%_bindir/*
%_man1dir/*
%_man8dir/*

%changelog
* Sat Aug 08 2020 Vitaly Chikunov <vt@altlinux.org> 1.2.0-alt1
- Update to blktrace-1.2.0-37-ga021a33 (2020-05-13).
- spec: Do not build blktrace.pdf (read blktrace.tex instead).
- spec: Remove python dependency for rarely useful bno_plot.py.

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.1
- NMU: fixed build with new texlive

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.1
- Rebuild with Python-2.7

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- 1.0.3

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt with python 2.6

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1
- reworked gear repo style

* Sat Jun 14 2008 Michael Shigorin <mike@altlinux.org> 0.99.3-alt1
- built for ALT Linux (based on btrace.spec in source repo)
  + commit 84a26fcd9adebd1537bf2c4eee69d1ca23ccbc5f
    (seems working while last release is a bit dated)
- spec fixup/cleanup
- buildreq

* Mon Oct 10 2005 - axboe@suse.de
- Initial version
