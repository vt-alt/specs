%define        pkgname simplecov

Name: 	       ruby-%pkgname
Version:       0.17.0
Release:       alt1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/colszowka/simplecov
%vcs           https://github.com/colszowka/simplecov.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
%filter_from_requires \,^ruby(\(jruby\|simplecov/railties/tasks.rake\),d

%description
SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's
built-in Coverage library to gather code coverage data, but makes
processing its results much easier by providing a clean API to filter,
group, merge, format, and display those results, giving you a complete
code coverage suite that can be set up with just a couple lines of code.

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
* Tue Jul 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- Bump to 0.17.0
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt0.M70C.1
- Rebuild with Ruby 2.4.3

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt1
- New version

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.1-alt1
- New version

* Fri Mar 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt2
- Rebuild with missing requirements

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- Initial build in Sisyphus
