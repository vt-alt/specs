%define dist Net-Telnet
Name: perl-Net-Telnet
Version: 3.05
Release: alt1

Summary: Script telnetable connections
License: GPL
Group: Development/Perl

Url: %CPAN %dist
Source0: http://www.cpan.org/authors/id/J/JR/JROGERS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Feb 27 2004
BuildRequires: perl-devel

%description
Net::Telnet allows you to make client connections to a TCP port
and do network I/O, especially to a port using the TELNET protocol.
Simple I/O methods such as print, get, and getline are provided.
More sophisticated interactive features are provided because connecting
to a TELNET port ultimately means communicating with a program designed
for human interaction.  These interactive features include the ability
to specify a time-out and to wait for patterns to appear in the 
stream, such as the prompt from a shell.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%perl_vendor_privlib/Net*

%changelog
* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 3.05-alt1
- automated CPAN update

* Wed Apr 22 2020 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.04-alt3
- Reverted previous change.

* Sun Apr 19 2020 Igor Vlasenko <viy@altlinux.ru> 3.04-alt2
- dropped perl(arybase.pm) autodependency

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.04-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.03-alt2.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.03-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Feb 27 2004 Alexey Tourbin <at@altlinux.ru> 3.03-alt2
- specfile revamped

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 3.03-alt1
- rebuild with new perl

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 3.02-ipl4mdk
- Rebuilt with perl-5.6.1

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Aug 31 2000 Philippe Libat <philippe@mandrakesoft.com> 3.02-2mdk
- description.

* Thu Aug 31 2000 Philippe Libat <philippe@mandrakesoft.com> 3.02-1mdk
- doc
- macroszifications.

* Fri Jun 30 2000 Nicolas Planel <nicolas@mandrakesoft.com>
- Spec file was generated for MandrakeSoft
