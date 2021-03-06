%define _unpackaged_files_terminate_build 1
%define module_name Type-Tiny
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(B/Deparse.pm) perl(Benchmark.pm) perl(CPAN/Meta/Requirements.pm) perl(Carp.pm) perl(Class/ISA.pm) perl(Class/InsideOut.pm) perl(Data/Dumper.pm) perl(Data/Validator.pm) perl(DateTime.pm) perl(DateTime/Duration.pm) perl(Devel/StackTrace.pm) perl(Encode.pm) perl(Exporter.pm) perl(Exporter/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(Function/Parameters.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(JSON/PP.pm) perl(Math/BigFloat.pm) perl(Method/Generate/Accessor.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/Types/MooseLike/Base.pm) perl(Moose.pm) perl(Moose/Meta/TypeCoercion.pm) perl(Moose/Meta/TypeConstraint.pm) perl(Moose/Meta/TypeConstraint/Class.pm) perl(Moose/Meta/TypeConstraint/DuckType.pm) perl(Moose/Meta/TypeConstraint/Enum.pm) perl(Moose/Meta/TypeConstraint/Union.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types.pm) perl(MooseX/Types/Moose.pm) perl(Mouse.pm) perl(Mouse/Meta/TypeConstraint.pm) perl(Mouse/Util.pm) perl(Mouse/Util/TypeConstraints.pm) perl(MouseX/Types.pm) perl(MouseX/Types/Moose.pm) perl(Object/Accessor.pm) perl(Params/Check.pm) perl(Params/Validate.pm) perl(Reply/Plugin.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Scalar/Util.pm) perl(Sub/Exporter/Lexical.pm) perl(Sub/Quote.pm) perl(Term/ANSIColor.pm) perl(Test/Builder.pm) perl(Test/Builder/Module.pm) perl(Test/LeakTrace.pm) perl(Test/More.pm) perl(Text/Balanced.pm) perl(Tie/Array.pm) perl(Tie/Hash.pm) perl(Tie/Scalar.pm) perl(Type/Tie.pm) perl(Validation/Class/Simple.pm) perl(base.pm) perl(overload.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.012003
Release: alt1
Summary: tiny, yet Moo(se)-compatible type constraint
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Type-Tiny

Source0: http://www.cpan.org/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes COPYRIGHT examples CREDITS CONTRIBUTING
%perl_vendor_privlib/T*
%perl_vendor_privlib/D*
%perl_vendor_privlib/R*
%perl_vendor_privlib/E*

%changelog
* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 1.012003-alt1
- automated CPAN update

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 1.012001-alt1
- automated CPAN update

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.012000-alt1
- automated CPAN update

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.010006-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.010005-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.010002-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.010001-alt1
- automated CPAN update

* Thu Feb 20 2020 Igor Vlasenko <viy@altlinux.ru> 1.010000-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.008005-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 1.008003-alt1
- automated CPAN update

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.008001-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.006000-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.004004-alt1
- automated CPAN update

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.004002-alt1
- automated CPAN update

* Fri Jul 27 2018 Igor Vlasenko <viy@altlinux.ru> 1.004000-alt1
- automated CPAN update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.002002-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.000006-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.000004-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- automated CPAN update

* Tue Mar 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.032-alt2
- uploaded to Sisyphus as Scalar-Does deep dependency

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- regenerated from template by package builder

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- initial import by package builder

