# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname strings-ansi

Name:          gem-%pkgname
Version:       0.2.0
Release:       alt1
Summary:       Handle ANSI escape codes in strings
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/strings-ansi
Vcs:           https://github.com/piotrmurach/strings-ansi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Strings::ANSI provides ANSI handling for Strings utilities.


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
* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- ^ 0.1.0 -> 0.2.0
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
