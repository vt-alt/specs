# vim: set ft=spec: -*- rpm-spec -*-

%define        pkgname ruby-prof

Name:          gem-%pkgname
Version:       0.18.0
Release:       alt1
Summary:       Fast code profiler for Ruby
Group:         Development/Ruby
License:       BSD-2-Clause
Url:           https://github.com/ruby-prof/ruby-prof
Vcs:           https://github.com/ruby-prof/ruby-prof.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
ruby-prof is a fast code profiler for MRI Ruby. Its features include:

* Speed - it is a C extension and therefore many times faster than the standard
  Ruby profiler.
* Modes - Ruby prof can measure a number of different parameters, including call
  times, memory usage and object allocations.
* Reports - can generate text and cross-referenced html reports
 - Flat Profiles - similar to the reports generated by the standard Ruby
   profiler
 - Graph profiles - similar to GProf, these show how long a method runs, which
   methods call it and which methods it calls.
 - Call tree profiles - outputs results in the calltree format suitable for
   the KCacheGrind profiling tool.
 - Many more - see reports section of this README.
* Threads - supports profiling multiple threads simultaneously


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   doc
Documentation files for %gemname gem.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   devel
Development files for %gemname gem.


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

%files         -n %pkgname
%_bindir/%{pkgname}*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 0.18.0-alt1
- ^ 0.17.0 -> 0.18.0
- ! spec tags

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt1
- new version 0.16.2

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.9.2-alt1.3
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.2-alt1.2
- fix ruby 2.0 compile error

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.9.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.2-alt1
- [0.9.2]

* Mon Jun 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.7.3-alt1
- [0.7.3]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- Built for Sisyphus
