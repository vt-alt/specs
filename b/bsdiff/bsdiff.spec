Summary:	Binary diff/patch utility
Name:		bsdiff
Version:	4.3
Release:	alt2
Group:		File tools
License:	BSD-2-Clause
Packager:	Fr. Br. George <george@altlinux.org>
URL:		https://www.daemonology.net/bsdiff/
Source:		%name-%version.tar
BuildRequires:	gcc bzlib-devel

%description
bsdiff and bspatch are tools for building and applying patches to
binary files. By using suffix sorting (specifically, Larsson and
Sadakane's qsufsort) and taking advantage of how executable files
change, bsdiff routinely produces binary patches 50-80%% smaller
than those produced by Xdelta, and 15%% smaller than those produced
by .RTPatch.

%prep
%setup

%build
%__cc %optflags bsdiff.c -lbz2 -o bsdiff
%__cc %optflags bspatch.c -lbz2 -o bspatch

%install
install -D -s bsdiff %buildroot%_bindir/bsdiff
install -D -s bspatch %buildroot%_bindir/bspatch

install -D bsdiff.1 %buildroot%_mandir/man1/bsdiff.1
install -D bspatch.1 %buildroot%_mandir/man1/bspatch.1

%files
%_bindir/bsdiff
%_bindir/bspatch
%_mandir/man1/bsdiff.1*
%_mandir/man1/bspatch.1*

%changelog
* Mon Mar 02 2020 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt2
- Rebuilt.

* Sun Aug 06 2006 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Initial ALT build

* Sat Mar 18 2006 Anssi Hannula <anssi@mandriva.org> 4.3-1mdk
- initial Mandriva release
