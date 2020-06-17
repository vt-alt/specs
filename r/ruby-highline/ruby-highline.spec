%define        pkgname highline

Name: 	       ruby-%pkgname
Epoch:         1
Version:       2.0.2
Release:       alt1
Summary:       HighLine is a high-level command-line IO Ruby library
License:       GPLv2/Ruby
Group:         Development/Ruby
Url:           https://github.com/JEG2/highline
%vcs           https://github.com/JEG2/highline.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A high-level IO library that provides validation, type conversion, and
more for command-line interfaces. HighLine also includes a complete menu
system that can crank out anything from simple list selection to
complete shells with just minutes of work.


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
* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.2-alt1
^ v2.0.2
^ Ruby Policy 2.0

* Wed Apr 10 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1:1.7.9-alt1
- update to 1.7.9 for opennebula

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.21-alt2
- Reset to old version for ruby-commander and ruby-hiera-eyaml.

* Mon Jul 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.
- Rebuild with new Ruby autorequirements.

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.5.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Jan 04 2010 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt2
- fix Url
- fix License

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt1
- build for Sisyphus

