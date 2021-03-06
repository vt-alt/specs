# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname minitest-retry

Name:          gem-%pkgname
Version:       0.1.9
Release:       alt1
Summary:       re-run the test when the test fails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/y-yagi/minitest-retry
%vcs           https://github.com/y-yagi/minitest-retry.git
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
* Mon Oct 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.9-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
