# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname hpricot

Name:          gem-%pkgname
Version:       0.8.6
Release:       alt4.3
Summary:       A Fast, Enjoyable HTML Parser for Ruby
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/hpricot/hpricot
Vcs:           https://github.com/hpricot/hpricot.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Hpricot is a fast, flexible HTML parser written in C.  It's designed to
be very accommodating (like Tanaka Akira's HTree) and to have a very
helpful library (like some JavaScript libs -- JQuery, Prototype -- give
you.)  The XPath and CSS parser, in fact, is based on John Resig's JQuery.


%package       devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
%ruby_gemextdir

%files doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/%{gemname}*


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.6-alt4.3
- fixed (!) spec

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.6-alt4.2
- fixed (!) spec according changelog policy

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.6-alt4.1
- fixed (!) spec

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.6-alt4
- Clean up the spec from the dog-nail

* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.6-alt3.1
- Fix build on i586 with a workaround dog-nail

* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.6-alt3
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt2.1
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt2
- Build ro aarch64.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- new version 0.8.6

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.8-alt1.3
- Rebuilt with ruby-2.0.0-alt1

* Fri Mar 14 2014 Led <led@altlinux.ru> 0.8-alt1.2
- test: fixed for ruby >= 2.0

* Sun Dec 09 2012 Led <led@altlinux.ru> 0.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fix build with libruby 1.9.x

* Fri Jul 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8-alt1
- 0.8-8-g38c781c

* Wed Aug 20 2008 Sir Raorn <raorn@altlinux.ru> 0.5.140-alt1
- Built for Sisyphus
