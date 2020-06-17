%define        pkgname io-extra

Name:          gem-%pkgname
Version:       1.3.0
Release:       alt1.1
Summary:       Adds IO.fdwalk, IO.closefrom and IO.directio
Group:         Development/Ruby
License:       Apache-2.0
Url:           https://github.com/djberg96/io-extra
Vcs:           https://github.com/djberg96/io-extra.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
the io-extra library provides a few extra IO methods that you may find
handy. They are IO.closefrom, IO.fdwalk, IO#directio and IO#directio.

Adds the IO.closefrom, IO.fdwalk, IO.pread, IO.pread_ptr, IO.pwrite, and
IO.writev singleton methods as well as the IO#directio, IO#directio? and
IO#ttyname instance methods (for those platforms that support them).


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

%files         doc
%ruby_gemdocdir

%changelog
* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1.1
- + build required gem package

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt0.1
- > Ruby Policy 2.0
- > source from github
- ^ 1.2.7 -> 1.3.0

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.6
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.5
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.4
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.3
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.2
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.1
- Rebuild with Ruby 2.3.1

* Wed Nov 05 2014 Anton Gorlov <stalker@altlinux.ru> 1.2.7-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.2.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Aug 11 2011 Anton Gorlov <stalker@altlinux.ru> 1.2.2-alt1
- initial build for ALTLinux
