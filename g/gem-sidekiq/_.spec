# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname sidekiq

Name:          gem-%pkgname
Version:       5.2.8
Release:       alt1.1
Summary:       Simple, efficient background processing for Ruby
License:       LGPLv3
Group:         Development/Ruby
Url:           http://sidekiq.org
Vcs:           https://github.com/mperham/sidekiq.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version rack ~> 2.0
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
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


%prep
%setup

%build
%ruby_build --ignore=myapp,web

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1.1
- * gem deps for rack to ~> 2.0

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
