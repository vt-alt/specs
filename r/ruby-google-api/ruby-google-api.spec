%define        pkgname google-api-client
%define        gemname %pkgname

Name:          ruby-google-api
Version:       0.30.5
Release:       alt1
Summary:       Google API Client for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://developers.google.com/api-client-library/ruby/
%vcs           https://github.com/google/google-api-ruby-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemlibdir/*

%description
These client libraries are officially supported by Google. However,
the libraries are considered complete and are in maintenance mode. This means
that we will address critical bugs and security issues but will not add any new
features.


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
%ruby_build --ignore=cli,web --use=%gemname --alias=google-api

%install
%ruby_install

%check
%ruby_test

%files
%_bindir/generate-api
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.30.5-alt1
- Bump to 0.30.5
- Fix spec

* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 0.30.2-alt1
- Fix lost provides (closes #36888)

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 0.28.4-alt1
- Use Ruby Policy 2.0;
- Bump to v0.28.4;
- Gem build rocedure replaced with only config.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 0.25.0-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.24.2-alt1
- New version.

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.24.1-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.24.0-alt1
- New version.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.23.0-alt1
- New version.
- Package as gem.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.22.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.21.2-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- Initial build for Sisyphus
