# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname graphql-batch

Name:          gem-%pkgname
Version:       0.4.1
Release:       alt1
Summary:       A query batching executor for the graphql gem 
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/graphql-batch
%vcs           https://github.com/Shopify/graphql-batch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Provides an executor for the graphql gem which allows queries to be batched.


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
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- updated to (^) v0.4.1
- fix (!) spec

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
