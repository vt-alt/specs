%define        pkgname jquery-ui-rails

Name:          gem-%pkgname
Version:       6.0.1
Release:       alt1
Summary:       jQuery UI for the Rails asset pipeline
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jquery-ui-rails/jquery-ui-rails
%vcs           https://github.com/jquery-ui-rails/jquery-ui-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
This gem packages the jQuery UI assets (JavaScripts, stylesheets, and images)
for the Rails asset pipeline, so you never have to download a custom package
through the web interface again.

See VERSIONS.md to see which versions of jquery-ui-rails bundle which versions
of jQuery UI.

Warning: This gem is incompatible with the jquery-rails gem before version
3.0.0!
Strange things will happen if you use an earlier jquery-rails version. Run
bundle list to ensure that you either aren't using jquery-rails, or at least
version 3.0.0 of jquery-rails.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета


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
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 6.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
