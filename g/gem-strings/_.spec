# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname strings

Name:          gem-%pkgname
Version:       0.1.6
Release:       alt1
Summary:       A set of useful functions for transforming strings
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/strings
%vcs           https://github.com/piotrmurach/strings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
The Strings is a set of useful functions such as fold, truncate, wrap, and many
more for transforming strings.


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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.6-alt1
- ^ v0.1.6
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with usage Ruby Policy 2.0
