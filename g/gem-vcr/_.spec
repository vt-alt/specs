%define        pkgname vcr

Name:          gem-%pkgname
Version:       5.0.0
Release:       alt1
Summary:       Record your test suite's HTTP interactions and replay them during future test runs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vcr/vcr
%vcs           https://github.com/vcr/vcr.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.


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
* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
