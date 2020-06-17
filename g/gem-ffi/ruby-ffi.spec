%define        pkgname ffi

Name:          gem-%pkgname
Version:       1.12.2
Release:       alt1
Summary:       Ruby foreign function interface
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/ffi/ffi/wiki
Vcs:           https://github.com/ffi/ffi.git
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libffi-devel
BuildRequires: gem(rspec)
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rubygems-tasks)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Ruby-FFI is a gem for programmatically loading dynamically-linked native
libraries, binding functions within them, and calling those functions from Ruby
code. Moreover, a Ruby-FFI extension works without changes on CRuby (MRI),
JRuby, Rubinius and TruffleRuby. Discover why you should write your next
extension using Ruby-FFI.


%package       devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   devel
Development headers for %gemname gem.

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

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/ffi*

%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.12.2-alt1
- ^ 1.11.3 -> 1.12.2
- ! spec tags

* Sun Dec 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.11.3-alt1
- updated (^) 1.11.1 -> 1.11.3
- fixed (!) spec's changelog, Vcs tag, minor others

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.11.1-alt1
- updated (^) 1.10.0 -> 1.11.1
- fixed (!) spec

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- updated (^) 1.9.25 -> 1.10.0
- updated (^) -> Ruby Policy 2.0

* Wed Aug 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.25-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.25-alt1
- New version.
- Package as gem in form libraries+gemspec.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 1.9.23-alt2
- Rebuild as ruby gem for openqa

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Feb 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1
- New version.

* Fri Feb 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.22-alt1
- New version.

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.21-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Mar 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt1
- New version

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.17-alt1
- new version 1.9.17
- fix module requires pathes

* Sat Sep 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.14-alt1
- new version 1.9.14

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- New version
- Fix project URL

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.6.3-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.6.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.3-alt1
- 0.6.3
- Rebuild with new libffi

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.5-alt1
- Built for Sisyphus

