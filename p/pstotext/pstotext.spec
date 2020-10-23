%define _unpackaged_files_terminate_build 1

Name: pstotext
Version: 1.9
Release: alt3
Summary: PostScript to text converter
License: Digital's paranoid but open-source license
Group: Text tools

Url: http://pages.cs.wisc.edu/~ghost/doc/pstotext.htm
# ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/contrib/%name-%version.tar.gz
Source: %name-%version.tar

# Patch from Debian
Patch1: 1.9-3_and_1.9-4.patch
# Patch from Gentoo
Patch2: 1.9-flags.patch

Requires: ghostscript

Summary(pl): Konwerter PostScriptu do czystego tekstu

%description
This utility reads in postscript files and outputs an ASCII rendering.
While the rendering is not always accurate, it is often sufficient.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%optflags"
%make

%install
install -pDm755 pstotext %buildroot%_bindir/%name
install -pDm644 pstotext.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Oct 22 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9-alt3
- Applied patches from Debian and Gentoo (Fixes: CVE-2005-2536, CVE-2006-5869).
- Build now respects %%optflags.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.9-alt2
- updated Url:
- spec cleanup

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 1.9-alt1
- built for ALT Linux (based on spec by Eugene Chernov
  which was in its turn adapted from PLD)

