%define        pkgname gridster-rails

Name:          gem-%pkgname
Version:       0.5.6.1
Release:       alt1
Summary:       This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+ application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vanetten/gridster-rails
%vcs           https://github.com/vanetten/gridster-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary. This is gridster.js GEMified for the Rails >= 3.1 asset pipeline.


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
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
