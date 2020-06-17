%define        pkgname optimist

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way
License:       MIT
Group:         Development/Ruby
Url:           http://manageiq.github.io/optimist/
%vcs           https://github.com/ManageIQ/optimist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary. One line of code per option is all you need to write. For that,
you get a nice automatically-generated help page, robust option parsing,
command subcompletion, and sensible defaults for everything you don't specify.

* Dirt-simple usage.
* Single file. Throw it in lib/ if you don't want to make it a Rubygem
  dependency.
* Sensible defaults. No tweaking necessary, much tweaking possible.
* Support for long options, short options, subcommands, and automatic type
  validation and conversion.
* Automatic help message generation, wrapped to current screen width.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
