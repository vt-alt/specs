%define        pkgname rack-test

Name: 	       ruby-%pkgname
Version:       1.1.0
Release:       alt2
Summary:       Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rack-test/rack-test
%vcs           https://github.com/rack-test/rack-test.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета


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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt2
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.

* Tue Jun 13 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus
