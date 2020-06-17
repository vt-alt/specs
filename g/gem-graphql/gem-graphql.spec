%define        pkgname graphql

Name:          gem-%pkgname
Version:       1.9.6
Release:       alt1
Summary:       A plain-Ruby implementation of GraphQL
License:       MIT
Group:         Development/Ruby
Url:           https://graphql-ruby.org/
# VCS:         https://github.com/rmosolgo/graphql-ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


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
* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.9.6-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
