# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname equatable

Name:          gem-%pkgname
Version:       0.6.1
Release:       alt1.1
Summary:       Allows ruby objects to implement equality comparison and inspection methods
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/equatable
%vcs           https://github.com/piotrmurach/equatable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

By including this module, a class indicates that its instances have explicit
general contracts for hash, == and eql? methods. Specifically eql? contract
requires that it implements an equivalence relation. By default each instance of
the class is equal only to itself. This is a right behaviour when you have
distinct objects. However, it is the responsibility of any class to clearly
define their equality. Failure to do so may prevent instances to behave as
expected when for instance Array#uniq is invoked or when they are used as Hash
keys.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with usage Ruby Policy 2.0
