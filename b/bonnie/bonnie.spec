Name: bonnie
Version: 1.5
Release: alt4

Summary: Unix filesystem performance benchmark
License: Artistic
Group: System/Kernel and hardware

URL: https://fossies.org/linux/privat/old/
Source: %url/bonnie-%version.tar.gz

%description
bonnie is a classic file system and storage device benchmark. It tests
for linear character-based and block-based reads and writes, and the
rewrite pattern. It also does a seek test. While other benchmarks do
more sophisticated tests, bonnie is a very reliable and portable program
that is suitable for basic testing. Optionally, you can test the
operations with direct I/O (O_DIRECT on Linux).

%prep
%setup -n bonnie

%build
%make CFLAGS="%optflags"

%install
install -pD -m755 Bonnie %buildroot%_bindir/bonnie
install -pD -m644 bonnie.1 %buildroot%_man1dir/bonnie.1

%files
%_bindir/*
%_man1dir/*
%doc bonnie.doc README

%changelog
* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.5-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3
- NMU: remove %ubt from release

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt2%ubt
- fixed typo in manpage

* Wed May 30 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt1%ubt
- 1.5

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4-alt3.qa1
- NMU: rebuilt for debuginfo.

* Mon Feb 18 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt3
- Include sys/user.h for PAGE_MASK definition due to unexported
  asm/page.h in glibc-kernheaders-2.6.18-alt4.

* Fri Apr 13 2007 Victor Forsyuk <force@altlinux.org> 1.4-alt2
- Fix "License:" value: license is Artistic, not just distributable.

* Wed May 11 2005 Victor Forsyuk <force@altlinux.ru> 1.4-alt1
- New version from new maintainer.
- Better description (taken from freshmeat project page).

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 1.0-ipl9mdk
- Rebuild

* Tue Mar 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl8mdk
- Rebuilt

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl7mdk
- RE and Fandra adaptions.

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0-6mdk
- group fix

* Sun Nov 28 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Fix group

* Thu Nov 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- initial release.
