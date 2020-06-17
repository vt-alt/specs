%define        pkgname bson

Name: 	       gem-%pkgname
Version:       4.8.2
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+)
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://bsonspec.org
Vcs:           https://github.com/mongodb/bson-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

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


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*

%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 4.8.2-alt1
- ^ 4.4.2 -> 4.8.2
- ! spec tags

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 4.4.2-alt1
- > Ruby Policy 2.0
- ^ 4.3.0 -> 4.4.2

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
