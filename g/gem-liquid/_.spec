%define        pkgname liquid

Name:          gem-%pkgname
Version:       4.0.3
Release:       alt1
Summary:       Liquid markup language
License:       MIT
Group:         Development/Ruby
Url:           https://shopify.github.io/liquid/
%vcs           https://shopify.github.io/liquid/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Liquid is a template engine which was written with very specific requirements:

* It has to have beautiful and simple markup. Template engines which don't
  produce good looking markup are no fun to use.
* It needs to be non evaling and secure. Liquid templates are made so that users
  can edit them. You don't want to run code on your server which your users
  wrote.
* It has to be stateless. Compile and render steps have to be separate so that
  the expensive parsing and compiling can be done once and later on you can just
  render it passing in a hash with local variables and objects.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
