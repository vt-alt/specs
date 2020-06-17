%define        pkgname validates-lengths-from-database
%define        gemname validates_lengths_from_database

Name:          gem-%pkgname
Version:       0.8.0
Release:       alt1

Summary:       Introspects your database string field maximum lengths and automatically defines length validations.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubiety/validates_lengths_from_database
#Vcs:           https://github.com/rubiety/validates_lengths_from_database.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Few people add length validations to fields in their database, and when saving
such fields that have exhausted their length, an SQL error occurs. This gem
introspects your table schema for maximum lengths on string and text fields and
automatically adds length validations to the model.

%description -l ru_RU.UTF8
Некоторые люди добавляют проверки длины для полей в своих базах данных, но затем
сохранение в такие поля данных, длина которых превышает ограничение, вызывает
ошибки SQL. Сей бисер наблюдает за схемой таблицы в части превышения длины строк
и текста таких полей, и автоматически добавляет проверки длины для таких полей в
модель.


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
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- > Ruby Policy 2.0
- ^ 0.7.0 -> 0.8.0
- ! spec tags

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- Initial gemified build for Sisyphus
