%define        pkgname posix-spawn

Name:          gem-%pkgname
Version:       0.3.13
Release:       alt2.3
Summary:       Ruby process spawning library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rtomayko/posix-spawn
Vcs:           https://github.com/rtomayko/posix-spawn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         upstream-fix-build-on-i586.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
%summary.

fork(2) calls slow down as the parent process uses more memory due to the need
to copy page tables. In many common uses of fork(), where it is followed by one
of the exec family of functions to spawn child processes (Kernel#system,
IO::popen, Process::spawn, etc.), it's possible to remove this overhead by
using special process spawning interfaces (posix_spawn(), vfork(), etc.)

The posix-spawn library aims to implement a subset of the Ruby 1.9
Process::spawn interface in a way that takes advantage of fast process spawning
interfaces when available and provides sane fallbacks on systems that do not.


%package       -n posix-spawn-benchmark
Summary:       %summary
Group:         Development/Documentation
BuildArch:     noarch

%description   -n posix-spawn-benchmark
%summary.

Executables files for %gemname gem.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup
%patch -p1

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

%files         -n posix-spawn-benchmark
%_bindir/posix-spawn-benchmark


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2.3
- fixed (!) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2.2
- fixed (!) spec according to changelog rules

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2.1
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt2
- used (>) Ruby Policy 2.0

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.13-alt1
- Initial build for Sisyphus
