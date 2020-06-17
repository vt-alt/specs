%define        pkgname bump

Name:          gem-%pkgname
Version:       0.8.0
Release:       alt3.1
Summary:       Bump is a gem that will simplify the way you build gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gregorym/bump
Vcs:           https://github.com/gregorym/bump.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Bump is a gem that will simplify the way you build gems and chef-cookbooks.

%description -l ru_RU.UTF-8
Бамп есть бисер, который позволяет упростить путь в построении
бисеров и поваренных книг.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%description   doc -l ru_RU.UTF-8
Документация для %{name}.


%package       -n bump
Summary:       Bump is the executable file for bump gem.
Group:         Development/Ruby
BuildArch:     noarch

Conflicts:     mesa-demos
Conflicts:     bumper

%description   -n bump
Bump is the executable file for bump gem, which is a gem that will simplify
the way you build gems and chef-cookbooks.

%description   -n bump -l ru_RU.UTF-8
Исполняемый файл для бисера bump, который позволяет упростить путь в построении
бисеров и поваренных книг.


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

%files         -n bump
%_bindir/*

%changelog
* Thu Jun 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt3.1
- + conflict dep to bumper

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt3
- ! spec by adding explicit conflict for bump to mesa-demos

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt2
- fix spec

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
