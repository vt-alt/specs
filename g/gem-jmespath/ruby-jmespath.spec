%define        pkgname jmespath

Name:          gem-%pkgname
Version:       1.4.0
Release:       alt2.1
Summary:       Ruby implementation of JMESPath
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/jmespath/jmespath.rb
Vcs:           https://github.com/jmespath/jmespath.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
%summary.


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
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2.1
- ! spec tags

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 31 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
