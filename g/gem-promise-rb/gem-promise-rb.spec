%define        pkgname promise-rb
%define        gemname promise.rb

Name:          gem-%pkgname
Version:       0.7.4
Release:       alt1
Summary:       Promises/A+ for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lgierth/promise.rb
# VCS:         https://github.com/lgierth/promise.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Ruby implementation of the Promises/A+ spec. 100% mutation coverage, tested on
MRI 1.9, 2.0, 2.1, 2.2, Rubinius, and JRuby.


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
* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.4-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
