%define        pkgname commonjs

Name:          gem-%pkgname
Version:       0.2.7
Release:       alt1
Summary:       Common JS for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/cowboyd/commonjs.rb
%vcs           http://github.com/cowboyd/commonjs.rb
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Host CommonJS JavaScript environments in Ruby.


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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
