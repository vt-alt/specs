# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname ruby2-keywords
%define        gemname ruby2_keywords

Name:          gem-%pkgname
Version:       0.0.2
Release:       alt1
Summary:       Shim library for Module#ruby2_keywords
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/ruby2_keywords
Vcs:           https://github.com/ruby/ruby2_keywords.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Provides empty Module#ruby2_keywords method, for the forward source-level
compatibility against ruby2.7 and ruby3.


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
# TODO move describe to setup
sed 's,version =.*,version = "%version",' -i %gemname.gemspec

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
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- + packaged gem with usage Ruby Policy 2.0
