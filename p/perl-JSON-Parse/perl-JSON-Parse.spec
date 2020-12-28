%define _unpackaged_files_terminate_build 1
%define module_name JSON-Parse
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.57
Release: alt2
Summary: Read JSON into a Perl variable
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/B/BK/BKB/%{module_name}-%{version}.tar.gz

%description
A module for parsing JSON. (JSON means "JavaScript Object Notation"
and it is specified in the RFC 7159 entry elsewhere in this document.)

JSON::Parse offers the function the parse_json entry elsewhere in this document, which takes a string
containing JSON, and returns an equivalent Perl structure. It also
offers validation of JSON via the valid_json entry elsewhere in this document, which returns true or
false depending on whether the JSON is correct or not, and
the assert_valid_json entry elsewhere in this document, which produces a descriptive fatal error if the
JSON is invalid. A function the json_file_to_perl entry elsewhere in this document reads JSON from a
file, and there is a safer version of the parse_json entry elsewhere in this document called
the parse_json_safe entry elsewhere in this document which doesn't throw exceptions.

For special cases of parsing, there are also methods the new entry elsewhere in this document and
the run entry elsewhere in this document, which create a JSON parsing object and run it on text. See
the METHODS entry elsewhere in this document.

JSON::Parse accepts only UTF-8 as input. See the UTF-8 only entry elsewhere in this document and
the Handling of Unicode entry elsewhere in this document.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description scripts
scripts for %module_name
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/J*
%perl_vendor_autolib/*

%files scripts
%_bindir/*

%changelog
* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.57-alt2
- fixed warning: scripts should be .noarch

* Thu Jul 23 2020 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- automated CPAN update

* Thu Feb 20 2020 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.55-alt3
- to Sisyphus as perl-Finance-Quote dep

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.55-alt2.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.55-alt2
- rebuild with perl 5.26

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- regenerated from template by package builder

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- regenerated from template by package builder

* Mon Feb 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.49-alt2
- rebuild with perl 5.24

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- regenerated from template by package builder

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- regenerated from template by package builder

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- regenerated from template by package builder

* Wed Jul 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- regenerated from template by package builder

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- regenerated from template by package builder

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1.1
- rebuild with perl 5.22

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- regenerated from template by package builder

* Tue Nov 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- regenerated from template by package builder

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- regenerated from template by package builder

* Sun Oct 18 2015 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- regenerated from template by package builder

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.30-alt2
- rebuild to get rid of unmets

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- regenerated from template by package builder

* Tue Dec 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- regenerated from template by package builder

* Wed Dec 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- regenerated from template by package builder

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- initial import by package builder

