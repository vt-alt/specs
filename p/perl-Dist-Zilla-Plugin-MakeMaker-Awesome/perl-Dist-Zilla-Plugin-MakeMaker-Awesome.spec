## SPEC file for Perl module Dist::Zilla::Plugin::MakeMaker::Awesome

%define real_name Dist-Zilla-Plugin-MakeMaker-Awesome

Name: perl-Dist-Zilla-Plugin-MakeMaker-Awesome
Version: 0.48
Release: alt2

Summary: a more awesome MakeMaker plugin for Dist::Zilla

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-MakeMaker-Awesome/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: gem-power-assert perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-MooseX-Types-Stringlike perl-Pod-Coverage perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Test-Moose-More perl-YAML

%description
Perl module Dist::Zilla::Plugin::MakeMaker::Awesome is a more
awesome MakeMaker plugin for Dist::Zilla.
It is limited, if you want to stray from the marked path and do
something that would normally be done in a package MY section or
otherwise run custom code in your Makefile.PL you're out of luck.

This plugin is 100%% compatible with Dist::Zilla::Plugin::MakeMaker -
we add additional customization hooks by subclassing it.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/MakeMaker/Awesome*

%changelog
* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.48-alt2
- Update BuildRequires

* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.48-alt1
- New version

* Sun Aug 05 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.47-alt1
- New version

* Sat Jun 30 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.45-alt1
- New version

* Wed May 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.42-alt1
- New version

* Sun Mar 04 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.41-alt1
- New version

* Sun Jan 28 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.40-alt1
- New version

* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.39-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.38-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.36-alt1
- New version

* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.35-alt2
- Bump release to override package from the autoimports/Sisyphus repository

* Sun Dec 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.35-alt1
- Initial build for ALT Linux Sisyphus
