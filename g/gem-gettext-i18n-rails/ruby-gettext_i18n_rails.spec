%define        pkgname gettext-i18n-rails
%define        gemname gettext_i18n_rails

Name:          gem-%pkgname
Version:       1.8.1
Release:       alt1
Summary:       Simple FastGettext Rails integration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/gettext_i18n_rails
Vcs:           https://github.com/grosser/gettext_i18n_rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
FastGettext / Rails integration.

Translate via FastGettext, use any other I18n backend as extension/fallback.

Rails does: I18n.t('syntax.with.lots.of.dots') with nested yml files
We do: _('Just translate my damn text!') with simple, flat mo/po/yml files or
directly from db. To use I18n calls add a syntax.with.lots.of.dots translation.

%description -l ru_RU.UTF8
Сопряжение Рельс и FastGettext.

Перевод через FastGettext с использованием любый иных I18n приклёпок в качестве
расширений.

В Рельсах делаюется: I18n.t('syntax.with.lots.of.dots'), используя вложенные
ямл-файлы. У нас делается: _('Just translate my damn text!'), используя простые,
прямые mo/po/yml файлы или напрямую из БД. А чтобы использовать вызовы к I18n
добавьте перевод строки вида "syntax.with.lots.of.dots".


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
%doc Readme*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- > Ruby Policy 2.0
- ^ 1.8.0 -> 1.8.1
- ! spec tags

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- Initial gemified build for Sisyphus
