%define        pkgname ast

Name:          gem-%pkgname
Version:       2.4.1
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees
License:       MIT
Group:         Development/Ruby
Url:           https://whitequark.github.io/ast/
Vcs:           https://github.com/whitequark/ast.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
AST is a small library for working with immutable abstract syntax trees.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt1
- ^ 2.4.0 -> 2.4.1
- ! spec syntax

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
