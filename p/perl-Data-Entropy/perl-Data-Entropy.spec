# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Data-Entropy
%define upstream_version 0.007

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt4_8

Summary:    Download entropy from
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Crypt/Rijndael.pm)
BuildRequires: perl(Data/Float.pm)
BuildRequires: perl(Errno.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(HTTP/Lite.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Params/Classify.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(integer.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This module maintains a concept of a current selection of entropy source.
Algorithms that require entropy, such as those in the
Data::Entropy::Algorithms manpage, can use the source nominated by this
module, avoiding the need for entropy source objects to be explicitly
passed around. This is convenient because usually one entropy source will
be used for an entire program run and so an explicit entropy source
parameter would rarely vary. There is also a default entropy source,
avoiding the need to explicitly configure a source at all.

If nothing is done to set a source then it defaults to the use of Rijndael
(AES) in counter mode (see the Data::Entropy::RawSource::CryptCounter
manpage and the Crypt::Rijndael manpage), keyed using Perl's built-in
'rand' function. This gives a data stream that looks like concentrated
entropy, but really only has at most the entropy of the 'rand' seed. Within
a single run it is cryptographically difficult to detect the correlation
between parts of the pseudo-entropy stream. If more true entropy is
required then it is necessary to configure a different entropy source.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README SIGNATURE
%perl_vendor_privlib/*

%changelog
* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.007-alt4_8
- to Sisyphus

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.007-alt3_8
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt3_7
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt3_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt3_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt3_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.007-alt3_3
- rebuild to get rid of unmets

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.007-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_1
- converted for ALT Linux by srpmconvert tools

