%define        pkgname autoprefixer-rails

Name:          gem-%pkgname
Version:       9.6.0
Release:       alt1
Summary:       Autoprefixer for Ruby and Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ai/autoprefixer-rails
%vcs           https://github.com/ai/autoprefixer-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.


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
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 9.6.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
