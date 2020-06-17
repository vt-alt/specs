# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname gitlab-turbolinks-classic

Name:          gem-%pkgname
Version:       2.5.7
Release:       alt1
Summary:       Turbolinks makes navigating your web application faster
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/jamedjo/gitlab-turbolinks-classic/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

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
* Thu May 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.7-alt1
- + packaged gem with usage Ruby Policy 2.0
