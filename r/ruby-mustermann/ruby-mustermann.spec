# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname mustermann
%define        gemname1 mustermann
%define        gemname2 mustermann-contrib

Name:          ruby-%pkgname
Version:       1.1.1
Release:       alt1
Summary:       The Amazing Mustermann
License:       MIT
Group:         Development/Ruby
Url:           http://sinatrarb.com/mustermann/
Vcs:           https://github.com/sinatra/mustermann.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(%gemname1)
Requires:      gem(%gemname2)

%description
%summary.


%package       -n gem-%gemname1
Summary:       Your personal string matching expert
Summary(ru_RU.UTF-8): Твой личный мастер поиска совпадений строк
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%gemname1
Your personal string matching expert.

A library implementing patterns that behave like regular expressions.

%description   -n gem-%gemname1 -l ru_RU.UTF8
Твой личный мастер поиска совпадений строк.

Библиотека воплощающая шаблоны, которые работают как регулярные выражения.


%package       -n gem-%gemname1-doc
Summary:       Documentation files for %gemname1 gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname1
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%gemname1-doc
Documentation files for %gemname1 gem.

%description   -n gem-%gemname1-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname1.


%package       -n gem-%gemname2
Summary:       A meta gem depending on all other official mustermann gems
Summary(ru_RU.UTF-8): Мета-самоцвет зависящий от всех других официальных самоцветов мастермана
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%gemname2
A meta gem depending on all other official mustermann gems.

%description   -n gem-%gemname2 -l ru_RU.UTF8
Мета-самоцвет зависящий от всех других официальных самоцветов мастермана.


%package       -n gem-%gemname2-doc
Summary:       Documentation files for %gemname2 gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname2
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%gemname2-doc
Documentation files for %gemname2 gem.

%description   -n gem-%gemname2-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname2.


%prep
%setup

%build
%ruby_build --ignore=support,ruby-mustermann

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-%gemname1
%doc README*
%ruby_gemspecdir/%gemname1-%version.gemspec
%ruby_gemslibdir/%gemname1-%version

%files         -n gem-%gemname1-doc
%ruby_gemsdocdir/%gemname1-%version

%files         -n gem-%gemname2
%doc README*
%ruby_gemspecdir/%gemname2-%version.gemspec
%ruby_gemslibdir/%gemname2-%version

%files         -n gem-%gemname2-doc
%ruby_gemsdocdir/%gemname2-%version


%changelog
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with usage Ruby Policy 2.0
