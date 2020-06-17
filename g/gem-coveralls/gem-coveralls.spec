%define        pkgname coveralls

Name:          gem-%pkgname
Version:       0.8.23
Release:       alt1.1
Summary:       Coveralls for Ruby
Summary(ru_RU.UTF-8): Покрытия для рубина
License:       MIT
Group:         Development/Ruby
Url:           https://coveralls.io
Vcs:           https://github.com/lemurheavy/coveralls-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(vcr) >= 2.9
BuildRequires: gem(webmock) >= 1.20
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(simplecov) >= 0.17.0
BuildRequires: gem(truthy) >= 1.0

%gem_replace_version simplecov ~> 0.17

%description
Coveralls was designed with Ruby projects in mind, and we've made it as easy as
we possibly can to get started.

%description   -l ru_RU.UTF8
Покрытия были разработаны для проектов рубина с умом, мы сделали его настолько
простым на сколько могли, чтобы сразу начать разработку.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Conflicts:     python-module-z4r-coveralls

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Fri Jun 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.23-alt1.1
- - spec dep to pry

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.23-alt1
- Bump to 0.8.23
- Fixed spec

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.22-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
