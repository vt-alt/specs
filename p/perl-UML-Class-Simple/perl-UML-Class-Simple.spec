%define _unpackaged_files_terminate_build 1
#
#   - UML-Class-Simple -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug UML::Class::Simple
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module UML-Class-Simple
%define m_distro UML-Class-Simple
%define m_name UML-Class-Simple
%define m_author_id unknown
%define _enable_test 1

Name: perl-UML-Class-Simple
Version: 0.22
Release: alt3

Summary: Render simple UML class diagrams, by loading the code

License: Artistic and GPL
Group: Development/Perl
Url: http://search.cpan.org/dist/UML-Class-Simple/

BuildArch: noarch
Source: http://www.cpan.org/authors/id/A/AG/AGENT/UML-Class-Simple-%{version}.tar.gz

# Automatically added by buildreq on Fri Dec 26 2008 (-bi)
BuildRequires: fonts-ttf-liberation graphviz perl-Class-Accessor perl-Class-Accessor-Grouped perl-File-Slurp perl-HTML-Parser perl-IPC-Run3 perl-PPI perl-Template perl-Test-Pod perl-Test-Pod-Coverage perl-XML-SAX perl-YAML perl-YAML-Syck perl-threads perl(Class/Inspector.pm) perl(List/MoreUtils.pm)

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
UML::Class::Simple is a Perl CPAN module that generates UML class diagrams (PNG
format, GIF format, XMI format, or dot source) automatically from Perl 5 source
or Perl 5 runtime.

Perl developers can use this module to obtain pretty class diagrams for
arbitrary existing Perl class libraries (including modern perl OO modules based
on Moose.pm), by only a single command. Companies can also use the resulting
pictures to visualize the project hierarchy and embed them into their
documentation.

The users no longer need to drag a mouse on the screen so as to draw figures
themselves or provide any specs other than the source code of their own
libraries that they want to depict. This module does all the jobs for them! :)

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/UML*
%_bindir/*
%_man1dir/*
%doc Changes README.md samples 

%changelog
* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt3
- fixed build

* Tue Jan 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2
- build w/o apache1

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Dec 26 2008 Michael Bochkaryov <misha@altlinux.ru> 0.17-alt1
- 0.17 version build
- remove fonts-ttf-ms from build requirements

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 0.15-alt1
- 0.15 version
- fix directory ownership violation

* Wed Jul 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.12-alt1
- first build for ALT Linux Sisyphus

