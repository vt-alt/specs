%define        pkgname thin

Name:          gem-%pkgname
Version:       1.7.2
Release:       alt1.1
Summary:       A very fast & simple Ruby web server
License:       GPLv2+
Group:         Development/Ruby
Url:           https://github.com/macournoyer/thin
Vcs:           https://github.com/macournoyer/thin.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

%description   -l ru_RU.UTF8
Крайне быстрый и простой веб-сервер для Рубина.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
%summary.

Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Крайне быстрый и простой веб-сервер для Рубина.

Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n %pkgname
%doc *.md
%_bindir/%pkgname

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1.1
- ! spec syntax and tags

* Thu Apr 11 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus
