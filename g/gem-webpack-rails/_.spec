# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname webpack-rails

Name:          gem-%pkgname
Version:       0.9.11
Release:       alt1.1
Summary:       Integrate webpack with your Ruby on Rails application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mipearson/webpack-rails
Vcs:           https://github.com/mipearson/webpack-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.


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
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1.1
- ! spec obsoletes/provides reqs

* Wed Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1
- + packaged gem with usage Ruby Policy 2.0
