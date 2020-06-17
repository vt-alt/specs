%define        pkgname nio4r

Name:          gem-%pkgname
Version:       2.5.2
Release:       alt1
Summary:       New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable network clients and servers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/nio4r
Vcs:           https://github.com/socketry/nio4r.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

Provides:      ruby-%pkgname
Obsoletes:     ruby-%pkgname

%description
New I/O for Ruby (nio4r): cross-platform asynchronous I/O primitives for
scalable network clients and servers. Modeled after the Java NIO API,
but simplified for ease-of-use. nio4r provides an abstract,
cross-platform stateful I/O selector API for Ruby. I/O selectors are the
heart of "reactor"-based event loops, and monitor multiple I/O objects
for various types of readiness, e.g. ready for reading or writing.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Conflicts:     libev-devel

%description   -n gem-%pkgname-devel
Development files for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- updated (^) 2.5.1 -> 2.5.2
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- updated (^) 2.3.1 -> 2.5.1

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt2
- moved to (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
