%define        pkgname strptime

Name:          gem-%pkgname
Version:       0.2.3
Release:       alt4
Summary:       A fast strpitme engine
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/nurse/strptime/
Vcs:           https://github.com/nurse/strptime.git
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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt4
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt3
- > Ruby Policy 2.0

* Fri Feb 22 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.3-alt2
- Fix license

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
