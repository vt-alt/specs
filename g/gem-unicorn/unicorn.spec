%define        pkgname unicorn

Name:          gem-%pkgname
Version:       5.5.4
Release:       alt1
Summary:       Unicorn: Rack HTTP server for fast clients and Unix
License:       GPLv2+ or Ruby
Group:         System/Servers
Url:           https://unicorn.bogomips.org/
Vcs:           https://bogomips.org/unicorn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels. Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between Unicorn and slow clients.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Conflicts:     golang-tools

%description   -n %pkgname
%summary.

Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Крайне быстрый и простой веб-сервер для Рубина.

Исполнямка для %gemname самоцвета.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ragel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n %pkgname
%doc README*
%_bindir/%{pkgname}*
%_mandir/%{pkgname}*

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 5.5.4-alt1
- ^ 5.5.0 -> 5.5.4
- ! spec syntax and tags

* Sat Apr 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.5.0-alt3
- Fix lost gem dependencies
- Fix spec

* Mon Mar 18 2019 Pavel Skrylev <majioa@altlinux.org> 5.5.0-alt2
- Fix shebang line

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version.
- Rewrite spec according Ruby Policy 2.0.

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1.1
- Rebuild with Ruby 2.5.0

* Sun Dec 24 2017 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Wed Oct 04 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- new version 5.2.0

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Wed Nov 19 2014 Anton Gorlov <stalker@altlinux.ru> 4.8.3-alt1
- update to  new version 

* Wed Mar 19 2014 Led <led@altlinux.ru> 4.7.0-alt1.1
- Rebuilt with ruby-2.0.0-alt1

* Sat Dec 07 2013 Anton Gorlov <stalker@altlinux.ru> 4.7.0-alt1
- update to  new version 

* Wed Apr 24 2013 Anton Gorlov <stalker@altlinux.ru> 4.6.2-alt1
- update to  new version 

* Fri Dec 07 2012 Led <led@altlinux.ru> 4.3.1-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri May 18 2012 Anton Gorlov <stalker@altlinux.ru> 4.3.1-alt1
- update to  new version 

* Tue Mar 20 2012 Anton Gorlov <stalker@altlinux.ru> 4.2.0-alt1
- update to  new version

* Sat Sep 03 2011 Anton Gorlov <stalker@altlinux.ru> 4.1.1-alt1
- update to  new version

* Wed Aug 17 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt3
- added examples to main package

* Sat Aug 13 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt2
- fix conflict with with ruby-parseconfig-doc

* Sat Aug 13 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt1
- initial build for ALTLinux

