%define        pkgname sprockets-rails

Name:          ruby-%pkgname
Version:       3.2.1
Release:       alt3
Summary:       Sprockets Rails integration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sprockets-rails
%vcs           https://github.com/rails/sprockets-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.


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
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.2.1-alt3
- ^ Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt2.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt2
- Package as gem.
- Disable tests.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
