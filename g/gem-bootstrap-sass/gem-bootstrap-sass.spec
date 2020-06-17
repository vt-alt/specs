%define        pkgname bootstrap-sass

Name:          gem-%pkgname
Version:       3.4.1
Release:       alt1
Summary:       Official Sass port of Bootstrap 2 and 3
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/twbs/bootstrap-sass
%vcs           https://github.com/twbs/bootstrap-sass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
bootstrap-sass is a Sass-powered version of Bootstrap 3, ready to drop right
into your Sass powered applications.

This is Bootstrap 3. For Bootstrap 4 use the Bootstrap rubygem if you use Ruby,
and the main repo otherwise.


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
%ruby_build --ignore=dummy_sass_only

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
* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
