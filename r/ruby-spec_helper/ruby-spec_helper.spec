%define        pkgname spec_helper
%define        gemname puppetlabs_spec_helper

Name:          ruby-%pkgname
Version:       2.14.1
Release:       alt1
Summary:       A set of shared spec helpers specific to Puppetlabs projects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppetlabs_spec_helper
%vcs           https://github.com/puppetlabs/puppetlabs_spec_helper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
#BuildRequires: ruby-rspec-puppet
#BuildRequires: ruby-rspec-expectations
#BuildRequires: ruby-puppet-lint
#BuildRequires: ruby-puppet-syntax
#BuildRequires: ruby-mocha
%gem_replace_version puppet-lint ~> 3.0
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This repository is meant to provide a single source of truth for how to
initialize different Puppet versions for spec testing.

The common use case is a module such as stdlib that works with many
versions of Puppet. The stdlib module should require the spec helper in
this repository, which will in turn automatically figure out the version
of Puppet being tested against and perform version specific
initialization.


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
%ruby_build --use=%gemname --alias=%pkgname

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
* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 2.14.1-alt1
^ Use Ruby Policy 2.0
^ v2.14.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux (without rspec-puppet support to prevent
  circular dependencies)
