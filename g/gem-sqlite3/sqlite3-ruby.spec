%define        pkgname sqlite3

Name:          gem-%pkgname
Version:       1.4.2
Release:       alt2
Summary:       A Ruby interface for the SQLite database engine
Group:         Development/Ruby
License:       BSD
Url:           https://github.com/sparklemotion/sqlite3-ruby
Vcs:           https://github.com/sparklemotion/sqlite3-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libsqlite3-devel
BuildRequires: gem(rake-compiler)
BuildRequires: gem(mini_portile2)
BuildRequires: gem(hoe)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname-ruby < %EVR
Provides:      %pkgname-ruby = %EVR

%description
A Ruby interface for the SQLite database engine.


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

Requires:      libsqlite3-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG* README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         devel
%ruby_includedir/*

%files         doc
%ruby_gemdocdir

%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt2
- ! spec tags and syntax

* Thu Dec 19 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- New version.

* Tue Jun 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.4.0 -> 1.4.1

* Tue Jun 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2
- Fix specfile

* Mon Mar 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- Bump to 1.4.0
- Use Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.6
- Rebuild with new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.5
- Package as gem.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt1
- new version 1.3.13

* Wed Sep 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt2
- Rebuild with Ruby 2.3.1

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.3.0-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.3.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.0-alt1
- [1.3.0]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.5-alt2
- Force encoding to UTF-8

* Sun Aug 16 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.5-alt1
- [1.2.5]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.4-alt1
- [1.2.4]

* Tue Apr 01 2008 Sir Raorn <raorn@altlinux.ru> 1.2.1-alt2
- Rebuilt with rpm-build-ruby

* Wed Jan 09 2008 Sir Raorn <raorn@altlinux.ru> 1.2.1-alt1
- Initial build for ALT Linux
