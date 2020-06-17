# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname license-acceptance

Name:          gem-%pkgname
Version:       1.0.13
Release:       alt1.1
Summary:       Chef Software libraries for accepting usage license
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/license-acceptance/
%vcs           https://github.com/chef/license-acceptance.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

This repo consists of a few parts:

* A specification for the acceptance of the new Chef EULA
 - The Trademark page contains useful information, especially for users who
   have questions about building an open source fork of Chef Software products.
* A Ruby library used for accepting the license
* A Golang library intended to be used by a Habitat package for accepting
  the license


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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.13-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.13-alt1
- + packaged gem with usage Ruby Policy 2.0
