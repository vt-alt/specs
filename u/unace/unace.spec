%define _unpackaged_files_terminate_build 1

Name: unace
Version: 1.2b
Release: alt5
Summary: ACE unarchiver
License: Freely distributable
Group: Archiving/Compression
Url: http://www.winace.com

Source: %name-%version.tar

# Patches from Debian
Patch1: 001_cpp_define.patch
Patch2: 002_fix_warnings.patch
Patch3: 003_security.patch
Patch4: 004_64_bit_clean.patch
Patch5: 005_format-security.patch
Patch6: 006_security-afl.patch
Patch7: 007_cross-compiling.patch

# ALT patches
Patch20: alt-fix-for-issue-in-CVE-2015-2063-fix.patch

Summary(ru_RU.UTF-8): Распаковщик архивов ACE 1.x

%description
The %name utility is a freeware program, distributed with source
code and developed for extracting and viewing the contents of
archives created with the ACE archiver v1.x. ACE archiver is
developed by "ACE Compression Software".

%description -l ru_RU.UTF-8
Программа %name предназначена для распаковки и просмотра содержимого
архивов, сжатых архиватором ACE версий 1.х. Архиватор ACE разработан
фирмой "ACE Compression Software".

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch20 -p2

%build
%make_build -f unix/makefile CFLAGS="%optflags"

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%doc readme file_id.diz
%_bindir/*

# 2.5 is closed source and known insecure (#24907)

%changelog
* Mon Nov 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2b-alt5
- Cleaned up sources by importing sources from Debian.
- Forced using system build flags.
- Updated fix for CVE-2015-2063.

* Thu Oct 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2b-alt4
- Applied patches from Debian (Fixes: CVE-2015-2063).
- Updated changelog to conform to vulnerability policy.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2b-alt3.qa1
- NMU: rebuilt for debuginfo.

* Fri Jan 28 2011 Michael Shigorin <mike@altlinux.org> 1.2b-alt3
- applied patch from Gentoo to fix CAN-2005-0160, CAN-2005-0161
  (closes: #24907) (Fixes: CVE-2005-0160, CVE-2005-0161).
- applied unace-1.2b-64bit.patch from Gentoo as well

* Sun Jun 15 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.2b-alt2
- build fix (make clean)

* Thu Mar 20 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.2b-1
- ALTLinux build
