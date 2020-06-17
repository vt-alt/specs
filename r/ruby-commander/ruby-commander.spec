%define        pkgname commander

Name:          ruby-%pkgname
Version:       4.4.7
Release:       alt1
Summary:       The complete solution for Ruby command-line executable
Group:         Development/Ruby
License:       MIT
Url:           http://visionmedia.github.com/commander
%vcs           https://github.com/commander-rb/commander.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
The complete solution for Ruby command-line executables. Commander bridges
the gap between other terminal related libraries you know and love
(OptionParser, HighLine), while providing many new features, and an elegant API.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 4.4.7-alt1
^ 4.4.7
^ Ruby Policy 2.0

* Tue Apr 09 2019 Mikhail Gordeev <obirvalger@altlinux.org> 4.3.1-alt1
- new version 4.3.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Aug 13 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.5-alt1
- Update to new release

* Fri Nov 30 2012 Led <led@altlinux.ru> 4.1.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Aug 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.2-alt1
- Initial build for Sisyphus
