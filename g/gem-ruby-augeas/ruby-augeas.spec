%define        pkgname ruby-augeas

Name:          gem-%pkgname
Epoch:         1
Version:       0.5.0
Release:       alt4
Summary:       Provides bindings for augeas
License:       LGPLv2
Group:         Development/Ruby
Url:           http://augeas.net
Vcs:           https://github.com/hercules-team/ruby-augeas.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rdoc)
BuildRequires: libaugeas-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname
Provides:      %pkgname

%description
The class Augeas provides bindings to Augeas library.


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

Requires:      gem(rake)
Requires:      gem(rdoc)
Requires:      libaugeas-devel
Requires:      libxml2-devel
Requires:      pkgconfig

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
%ruby_gemspecdir/%gemname-%version.gemspec
%ruby_gemslibdir/%gemname-%version
%ruby_gemsextdir/%gemname-%version

%files         doc
%ruby_gemsdocdir/%gemname-%version

%files         devel
%ruby_includedir/*

%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.5.0-alt4
- ! spec tags

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.5.0-alt3
- Use Ruby Policy 2.0

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.5
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2.1
- Rebuild with Ruby 2.4.1

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt2
- Use original gem in Sisyphus (ALT #33345)

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.5.0-alt1
- Initial build in Sisyphus with errored version 0.6.4
