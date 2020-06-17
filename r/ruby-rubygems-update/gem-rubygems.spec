%define        pkgname rubygems-update

Name:          ruby-%pkgname
Version:       3.0.4
Release:       alt1
Summary:       Library packaging and distribution for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://rubygems.org/
%vcs           https://github.com/rubygems/rubygems.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
Requires:      /usr/bin/gem

%description
RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and
load these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers.
See our guide on publishing a Gem at guides.rubygems.org


%package       -n update_rubygems
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n update_rubygems
Executable file for %gemname gem

%description   -n update_rubygems -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%ruby_build --srclibdir=lib --ignore=bar

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n update_rubygems
%_bindir/*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.4-alt1
- Bump to 3.0.4
- Fix spec to confirm setup.rb

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- Bump to 3.0.3
- Use Ruby Policy 2.0

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem
