%define        pkgname little-plugger

Name:          gem-%pkgname
Version:       1.1.4
Release:       alt2
Summary:       A gems based plugin framework for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/TwP/little-plugger
Vcs:           https://github.com/TwP/little-plugger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
# TODO build with bones faker
Source1:       %pkgname.gemspec

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
LittlePlugger is a module that provides Gem based plugin management. By
extending your own class or module with LittlePlugger you can easily
manage the loading and initializing of plugins provided by other gems.

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
cp -f %SOURCE1 ./

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
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt2
- > Use Ruby Policy 2.0
- ! spec tags

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- New version.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
