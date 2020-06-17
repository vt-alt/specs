# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rsec

Name:          gem-%pkgname
Version:       0.4.3
Release:       alt1
Summary:       Parser / Regexp Combinator For Ruby
License:       Ruby
Group:         Development/Ruby
Url:           http://rsec.herokuapp.com
Vcs:           https://github.com/luikore/rsec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Easy and extreme fast dynamic PEG parser combinator.

PEG grammar for Ruby, based on StringScanner. Consistently superior speed: up
to 10 times faster than Treetop, and twice the speed of rex+racc.

Compatible with Ruby v1.9 and above.


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
%ruby_build --ignore=website

%install
%ruby_install

%check
%ruby_test

%files
%doc readme*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- + packaged gem with usage Ruby Policy 2.0
