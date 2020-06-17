%define        pkgname fast-gettext
%define        gemname fast_gettext

Name:          gem-%pkgname
Version:       1.8.0
Release:       alt2
Summary:       GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34) and threadsafe
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/grosser/fast_gettext
Vcs:           https://github.com/grosser/fast_gettext.git
BuildArch:     noarch
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7
vs 34) and threadsafe!

It supports multiple backends (.mo, .po, .yml files,
Database(ActiveRecord + any other), Chain, Loggers) and can easily be
extended.

%description -l ru_RU.UTF8
Текущая GetText в 3,5 раза быстрее 560 раз потребляющая память, простая и ясная
в употреблении (7 против 34 пространств имён) и потокобезопасная.

Поддерживает различные конечные точки (.mo, .po, .yml файлы, базы данных
ActiveRecord и другие, цепи и логеры), а также есть легко расширяемым.


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
%ruby_gemslibdir

%files      doc
%ruby_gemsdocdir


%changelog
* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt2
- ! spec tags
- ! .gear/rules
- * license

* Thu Feb 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- ^ 1.7.0 -> 1.8.0
- > Ruby Policy 2.0

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- Bump to 1.7.0.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3
- Fix package as gem.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Rebuild with Ruby 2.4.2

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus
