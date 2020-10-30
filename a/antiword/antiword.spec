%define _unpackaged_files_terminate_build 1

Name: antiword
Version: 0.37
Release: alt4
Summary: Antiword an application to display Microsoft(R) Word files
License: GPL
Group: Text tools
Url: http://www.winfield.demon.nl/index.html

Source: %name-%version.tar

# Patches from Debian
Patch1: 10_fix_buffer_overflow_wordole_c.patch
Patch2: 50_antiword-manpage-hyphen-to-minus.patch
Patch3: docx.patch
Patch4: remove-cjb.net-references.patch
Patch5: use-snprintf.patch

%description
Antiword is a free MS Word reader for Linux and RISC OS. There are ports to
BeOS, OS/2, Mac OS X, Amiga, VMS, NetWare and DOS. Antiword converts the
binary files from Word 2, 6, 7, 97, 2000 and 2002 to plain text and to
PostScript TM.

%package -n kantiword
Summary: KAntiword, KDE viewer for Microsoft(R) Word files
Group: Graphical desktop/KDE
Requires: %name

%description -n kantiword
Antiword is a free MS Word reader. This package contains
its KDE-enabled part.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%make_build

%install
install -pD -m755 antiword %buildroot%_bindir/%name
install -pD -m755 kantiword %buildroot%_bindir/kantiword
install -pD Docs/antiword.1 %buildroot%_man1dir/antiword.1
cp -a Resources/ %buildroot%_datadir/%name

%files
%doc Docs/antiword*.php Docs/ChangeLog Docs/Emacs Docs/Exmh Docs/FAQ
%doc Docs/History Docs/Mozilla Docs/Mutt Docs/Netscape Docs/QandA
%doc Docs/ReadMe Docs/testdoc.doc
%_bindir/%name
%_datadir/%name/
%_man1dir/%name.1*

%files -n kantiword
%_bindir/kantiword

%changelog
* Thu Oct 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.37-alt4
- Applied patches from Debian (Fixes: CVE-2014-8123).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.37-alt3.1.qa1
- NMU: rebuilt for debuginfo.

* Fri Jun 08 2007 Slava Semushin <php-coder@altlinux.ru> 0.37-alt3.1
- NMU
- Exclude antiword.{1,man} and COPYING files from package
  documentation (#10198)
- Spec cleanup:
  + Removed space from %%description of kantiword package
  + s/%%setup -q/%%setup/
  + Use %%make_build instead of %%make
  + Don't use macroses for cp and install commands
  + More strict names in %%files section for man page

* Sat Dec 17 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.37-alt3
- rebuild

* Mon Dec 05 2005 Michael Shigorin <mike@altlinux.org> 0.37-alt0.M30.1
- 0.37
- built for 3.0
- spin kantiword off to a subpackage of its own (#8590)
- spec cleanup

* Mon Mar 21 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.36.1-alt1
- 0.36.1

* Thu Oct 28 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.36-alt1
- new version

* Sat Dec 6 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.35-alt1
- 0.35
- Bug in the use of the environment variable ANTIWORDHOME
- The XML/DocBook output is slightly better
- Scale view window is closed when the main window is closed
- More support for WinWord 1.x documents
- Cleanup spec file

* Thu Oct 30 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.34-alt1
- First version of RPM package

