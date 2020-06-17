%define        pkgname cool-io
%define        gemname cool.io

Name:          gem-%pkgname
Version:       1.6.0
Release:       alt1.1
Summary:       Simple evented I/O for Ruby (but please check out Celluloid::IO instead)
License:       MIT
Group:         Development/Ruby
Url:           https://coolio.github.io/
Vcs:           https://github.com/tarcieri/cool.io.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

Cool.io is an event library for Ruby, built on the libev event library, which
provides a cross-platform interface to high performance system calls. This
includes the epoll system call for Linux, the kqueue system call for BSDs and
OS X, and the completion ports interface for Solaris.

Cool.io also binds asynchronous wrappers to Ruby's core socket classes so you
can use them in conjunction with Cool.io to build asynchronous event-driven
applications.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Conflicts:     libev-devel

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
* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1.1
- + proper conflict dep to libev-devel

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- ^ 1.5.4 -> 1.6.0
- ! spec syntax and tags

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- > Ruby Policy 2.0
- ^ 1.5.3 -> 1.5.4

* Sat Sep 29 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.3-alt1
- Initial build for Sisyphus
