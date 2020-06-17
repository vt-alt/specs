# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname docker-api

Name:          gem-%pkgname
Version:       1.34.2
Release:       alt1.1
Summary:       A lightweight Ruby client for the Docker Remote API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/swipely/docker-api
%vcs           https://github.com/swipely/docker-api.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.34.2-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.34.2-alt1
- + packaged gem with usage Ruby Policy 2.0
