%define        pkgname benchmark-ips

Name: 	       ruby-%pkgname
Version:       2.7.2
Release:       alt1
Summary:       A iterations per second enhancement to Benchmark
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evanphx/benchmark-ips
%vcs           https://github.com/evanphx/benchmark-ips.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit)
BuildRequires: gem(rdoc)
BuildRequires: gem(hoe)

%description
Benchmark/ips benchmarks a blocks iterations/second. For short snippets
of code, ips automatically figures out how many times to run the code to
get interesting data. No more guessing at random iteration counts.


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

%files         doc
%ruby_gemdocdir

%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.2-alt1
- Use Ruby Policy 2.0
- Use git source
- Bump to 2.7.2

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt2.gite47e416
- Rebuild for new Ruby autorequirements.

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.gite47e416
- Initial build for ALT Linux
