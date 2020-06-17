%define        pkgname arel

Name:          gem-%pkgname
Version:       9.0.0
Release:       alt3
Summary:       A Relational Algebra
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/arel
Vcs:           https://github.com/rails/arel
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Arel Really Exasperates Logicians Arel is a SQL AST manager for Ruby. It 1.
Simplifies the generation of complex SQL queries 2. Adapts to various RDBMSes
It is intended to be a framework framework; that is, you can build your own ORM
with it, focusing on innovative object and collection modeling as opposed to
database compatibility and query generation.


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
* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 9.0.0-alt3
- > Ruby Policy 2.0
- ! spec tags

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt2.1
- Rebuild for new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt2
- Package as gem.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- Initial build for Sisyphus
