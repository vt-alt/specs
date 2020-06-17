%define        pkgname hiredis

Name: 	       gem-%pkgname
Version:       0.6.3
Release:       alt2
Summary:       Ruby wrapper for hiredis
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://github.com/redis/hiredis-rb
Vcs:           https://github.com/redis/hiredis-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libhiredis-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Ruby extension that wraps hiredis. Both the synchronous connection API and
a separate protocol reader are supported. It is primarily intended to speed up
parsing multi bulk replies.


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

Requires:      libhiredis-devel

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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt2
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- > Ruby Policy 2.0
- > source from github
- ^ 0.6.1 -> 0.6.3

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.1
- Rebuild with Ruby 2.5.0

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
