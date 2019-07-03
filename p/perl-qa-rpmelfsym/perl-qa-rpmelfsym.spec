%define dist qa-rpmelfsym
Name: perl-%dist
Version: 0.12.2
Release: alt1

Summary: Faster rpmelfsym(1) and bad_elf_symbols implementation
License: GPLv2+
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

# rpmelfsym.pm uses nm(1)
Requires: binutils

# Automatically added by buildreq on Mon Oct 10 2011 (-bi)
BuildRequires: perl-File-LibMagic perl-devel perl-qa-cache

%description
%summary.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# MakeMaker sucks (and I don't know how to tweak it)
rm %buildroot%perl_vendor_archlib/qa/*.pl

%files
%_bindir/*.pl
%perl_vendor_archlib/qa*
%perl_vendor_autolib/qa*

%changelog
* Wed Jul 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12.2-alt1
- Added 'S' (for mips/mipsel) and 'G' (for riscv64 and ppc64le) symbol types.
- Changed rpmelfsym.pm to skip files under /boot directory (ldv@).

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1.1
- rebuild with new perl 5.22.0

* Mon Sep 28 2015 Dmitry V. Levin <ldv@altlinux.org> 0.12.1-alt1
- rpmelfsym.pm: tolerate wider class of symbol names in nm(1) output.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt3
- built for perl 5.18

* Wed Nov 21 2012 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt2
- Added binutils to package requirements.

* Tue Oct 02 2012 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- rpmelfsym.pl: reimplemented print_elfysm() routine in XS
- rpmelfsym.xs: further optimized PerlIO_write() calls
- scripts: added --include=GLOB option

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt3
- rebuilt for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- rebuilt for perl-5.14

* Sun Sep 11 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- qa/rpmelfsym.pm: implemented parallel collect_bad_elfsym routine
- bad_elf_symbols_dircmp.pl: optimized def0 usage for parallel join

* Thu Sep 08 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- changed internal data format to argz blob
- rewritten bad_elf_symbols inner loop in XS

* Sun Feb 06 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- qa/rpmelfsym.pm: ignore *.debug files under /usr/lib/debug
- bad_elf_symbols*.pl: added support for "i" indirect functions

* Tue Aug 10 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- bad_elf_symbols*.pl: handle unique global symbols (Dmitry V. Levin)

* Tue Apr 07 2009 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- switched to (rpm-basename,size,mtime) caching mode
- flattened down internal data structure, for efficiency
- reverted piping to sort(1) and other optimizations proved inefficient
- optimized by saving (rpm-basename,filename) in a separate file
- optimized by eliminating huge 'sort -m' merges

* Fri Apr 03 2009 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- optimized inner loop writes for speed

* Wed Apr 01 2009 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- bad_elf_symbols*.pl: optimize by running sort(1) in background

* Sun Feb 22 2009 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- rpmelfsym.pm: fixed ELF magic check for nm(1)

* Fri Feb 20 2009 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- implemented bad_elf_symbols_dircmp.pl, for use in girar-builder

* Thu Feb 19 2009 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- rpmelfsym.pm: better handling of tmp write errors

* Wed Feb 18 2009 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial revision
