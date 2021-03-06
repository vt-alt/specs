## SPEC file for Perl module Canary::Stability

%define real_name Canary-Stability

Name: perl-Canary-Stability
Version: 2013
Release: alt1

Summary: canary to check perl compatibility for schmorp's modules

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Canary-Stability/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu May 02 2019
# optimized out: gem-power-assert perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-devel

%description
Perl module Canary::Stability is used by Schmorp's modules during
configuration stage to test the installed perl for compatibility
with his modules.

It's not, at this stage, meant as a tool for other module authors,
although in principle nothing prevents them from subscribing to
the same ideas.

See the Makefile.PL in Coro or AnyEvent for usage examples.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Canary/Stability*

%changelog
* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 2013-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2012-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2011-alt1
- New version

* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2006-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2001-alt1
- Initial build for ALT Linux Sisyphus
