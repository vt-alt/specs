%define        pkgname benchmark-suite
%define        gemname benchmark_suite

Name: 	       gem-%pkgname
Version:       1.0.0
Release:       alt3.git32101ee13
Summary:       A set of enhancements to the standard library benchmark.rb
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evanphx/benchmark_suite
Vcs:           https://github.com/evanphx/benchmark_suite.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit)
BuildRequires: gem(benchmark-ips)
BuildRequires: gem(hoe)

%gem_replace_version benchmark-ips ~> 2.0
%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname
Provides:      ruby-%gemname

%description
This package contains a command line tool for running multiple
benchmarks against multiple rubies. It is also uses benchmark/ips to
report iterations per second.


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
%_bindir/benchmark
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt3.git32101ee13
- ! package's spec tags
- ! build to up sources

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2.git5bded6.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6.1
- Rebuild with new Ruby autorequirements.

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6
- Initial build for ALT Linux
