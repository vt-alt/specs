%define        pkgname scoped-search
%define        gemname scoped_search

Name:          gem-%pkgname
Version:       4.1.7
Release:       alt1.1
Summary:       Easily search you ActiveRecord models with a simple query language that converts to SQL
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/wvanbergen/scoped_search
Vcs:           http://github.com/wvanbergen/scoped_search.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
The scoped_search gem makes it easy to search your ActiveRecord models.
Searching is performed using a query string, which should be passed to
the named_scope search_for. Based on a definition in what fields to look, it
will build query conditions and return those as a named scope.

Scoped search is great if you want to offer a simple yet powerful search box to
your users and build a query based on the search string they enter. It comes
with a built-in search syntax auto-completer and a value auto-completer. It
also comes with a set of helpers that makes it easy to create a clean web UI
with sorting and an ajax auto-completer.


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
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 4.1.7-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.7-alt1
- updated (^) 4.1.5 -> 4.1.7
- used (>) Ruby Policy 2.0

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.5-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.4-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.3-alt1
- Initial build for Sisyphus
