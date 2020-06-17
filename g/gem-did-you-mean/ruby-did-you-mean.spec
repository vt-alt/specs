# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname did-you-mean
%define        gemname did_you_mean

Name:          gem-%pkgname
Version:       1.3.0
Release:       alt2.1
Summary:       The gem that has been saving people from typos since 2014
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/yuki24/did_you_mean
%vcs           https://github.com/yuki24/did_you_mean.git
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
* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt2.1
- ! spec according to changelog rules

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt2
- ! Use Ruby Policy 2.0

* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
