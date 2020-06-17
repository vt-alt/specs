# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname wisper

Name:          gem-%pkgname
Version:       2.0.1
Release:       alt1
Summary:       A micro library providing Ruby objects with Publish-Subscribe capabilities
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/krisleech/wisper
%vcs           https://github.com/krisleech/wisper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

* Decouple core business logic from external concerns in Hexagonal style
  architectures
* Use as an alternative to ActiveRecord callbacks and Observers in Rails apps
* Connect objects based on context without permanence
* Publish events synchronously or asynchronously

Note: Wisper was originally extracted from a Rails codebase but is not
dependant on Rails.


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
%ruby_build --srcexedir=

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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ v2.0.1
- ! spec according to changelog rules

* Fri Aug 09 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
