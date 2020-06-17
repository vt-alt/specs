%define        pkgname gettext-i18n-rails-js
%define        gemname gettext_i18n_rails_js

Name:          gem-%pkgname
Version:       1.3.0
Release:       alt1
Summary:       Extends gettext_i18n_rails making your .PO files available to client side javascript as JSON
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/webhippie/gettext_i18n_rails_js
%vcs           https://github.com/webhippie/gettext_i18n_rails_js.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Extends gettext_i18n_rails, making your .PO files available to client side
javascript as JSON. It will find translations inside your .js, .coffee,
.handlebars and .mustache files, then it will create JSON versions of your .PO
files so you can serve them with the rest of your assets, thus letting you
access all your translations offline from client side javascript.


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
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
