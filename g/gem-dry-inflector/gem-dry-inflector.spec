%define        pkgname dry-inflector

Name:          gem-%pkgname
Version:       0.1.2
Release:       alt1
Summary:       String inflections for dry-rb
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-inflector
%vcs           https://github.com/dry-rb/dry-inflector.git
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

%changelog
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
