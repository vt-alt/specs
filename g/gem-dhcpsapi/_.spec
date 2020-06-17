# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname dhcpsapi

Name:          gem-%pkgname
Version:       0.0.11
Release:       alt1
Summary:       Ruby wrappers for MS DHCP api
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/dmitri-d/ruby-dhcpsapi
Vcs:           https://github.com/dmitri-d/ruby-dhcpsapi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
This contains ffi-based ruby bindings for MS DHCP server management API.


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
* Thu Jun 11 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.11-alt1
- + packaged gem with usage Ruby Policy 2.0
