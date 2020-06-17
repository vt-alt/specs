%define        pkgname record-tag-helper
%define        gemname record_tag_helper

Name:          gem-%pkgname
Version:       1.0.1
Release:       alt1
Summary:       ActionView Record Tag Helpers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/record_tag_helper
Vcs:           https://github.com/rails/record_tag_helper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
RecordTagHelper consists of code that was formerly a part of ActionView, but has
been removed from core in Rails 5. This gem is provided to ensure projects that
use functionality from ActionView::Helpers::RecordTagHelper have an appropriate
upgrade path.

This gem provides methods for generating container tags, such as div, for your
record. This is the recommended way of creating a container for your Active
Record object, as it adds appropriate class and id attributes to that container.
You can then refer to those containers easily by following that convention,
instead of having to think about which class or id attribute you should use.

%description -l ru_RU.UTF8
RecordTagHelper состоит из кода, который был частью ActionView, но был удалён из
ядра Рельс 5.0. Этот бисер позволяет увериться в том, что проекты, которые
используют функциональность из ActionView::Helpers::RecordTagHelper, будут иметь
подобающий путь обновления.

Этот бисер предоставляет методы для генерирования меток контейнеров, например,
"div", для вашей записи. Это рекоменндуемый способ создания контейнера для ваших
объектов Активной Записи, так как он добавляет подобающие атрибуты класса и
знака (id) в ваш контейнер. Дабы вы смогли ссылаться на те контейнеры легко
следуя соглашению, вместо того, чтобы думать о том, какие аттрибуты вы должны
использовать.


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
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- > Ruby Policy 2.0
- ^ 1.0.0 -> 1.0.1
- ! spec tags

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial gemified build for Sisyphus
