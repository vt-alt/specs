# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname will-paginate
%define        gemname will_paginate

Name:          ruby-%gemname
Version:       3.1.8
Release:       alt1
Summary:       Pagination library for Rails, Sinatra, Merb, DataMapper, and more
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mislav/will_paginate
%vcs           https://github.com/mislav/will_paginate.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
will_paginate is a pagination library that integrates with Ruby on Rails,
Sinatra, Merb, DataMapper and Sequel.

%description   -l ru_RU.UTF8
will_paginate есть самоцвет остраничивания, которая может быть состроена с
Рельсами, Синатрою, Мербом, Датамапером и Секвелом.


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
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.8-alt1
- updated to (^) v3.1.8
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.7-alt1
- updated to (^) v3.1.7
- updated to (^) Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 3.1.6-alt1
- added (+) initial gemified build for Sisyphus
