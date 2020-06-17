%define        pkgname responders

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       A set of Rails responders to dry up your application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/plataformatec/responders
Vcs:           https://github.com/plataformatec/responders.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
A set of responders modules to dry up your Rails 4.2+ app.

%description   -l ru_RU.UTF8
Наборы модулей отвечиков для очистки коджа вашего приложения для Рельс 4.2+.

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
* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- updated (^) 2.4.0 -> 3.0.0
- used (>) Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial gemified build for Sisyphus
