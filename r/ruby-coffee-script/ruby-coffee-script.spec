%define        source_version 1.12.2
%define        gem_version 2.4.1

Name:          ruby-coffee-script
Version:       %gem_version
Release:       alt3
Summary:       Ruby CoffeeScript Compiler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/ruby-coffee-script
%vcs           https://github.com/rails/ruby-coffee-script.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Version:       %gem_version
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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt3
^ Ruby Policy 2.0
- coffee-script-source gem

* Wed Sep 05 2018 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt2
- Split into two gems coffee-script-transpiler and coffee-script-source.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
