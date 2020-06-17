%define  pkgname sass

Name:          ruby-%pkgname
Version:       3.7.4
Release:       alt2
Summary:       Sass makes CSS fun again
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sass
%vcs           https://github.com/sass/sass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.


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
%_bindir/s*

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.4-alt2
- Use Ruby Policy 2.0

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.4-alt1
- New version.

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.7-alt1
- New version.

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt2.1
- Rebuild for new Ruby autorequirements.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 3.5.6-alt2
- Rebuild as ruby gem for openqa

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt1
- Initial build for Sisyphus
