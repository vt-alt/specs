%define        pkgname raindrops

Name:          gem-%pkgname
Version:       0.19.1
Release:       alt1
Summary:       real-time stats for preforking Rack servers
Group:         Development/Ruby
License:       LGPLv2
Url:           http://raindrops.bogomips.org/
Vcs:           git://bogomips.org/raindrops.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description 
Raindrops is a real time stats package to show statistics for Rack HTTP
servers.  It is designed for preforking servers such as Rainbows! and
Unicorn, but should support any Rack HTTP server under Ruby and possibly
Rubinius (untested) on platforms supporting POSIX shared memory and
compiled with GCC (for atomic builtins).  Raindrops includes a
Struct-like Raindrops::Struct class that may be used standalone to
create atomic counters shared across any number of forked processes
under SMP.


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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.19.1-alt1
- ^ 0.19.0 -> 0.19.1
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 10 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version

* Thu Mar 23 2017 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.0-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Thu Dec 06 2012 Led <led@altlinux.ru> 0.7.0-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt2
- fix wrong url

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt1
- initial build for ALTLinux
