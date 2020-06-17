# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname paint

Name:          ruby-%pkgname
Version:       2.1.1
Release:       alt1
Summary:       Ruby gem for ANSI terminal colors
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/paint
%vcs           https://github.com/janlelis/paint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Paint creates terminal colors and effects for you. It combines the
strengths of term-ansicolor, rainbow, and similar projects into a simple
to use, however still flexible terminal colors gem with no core
extensions by default.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-shortcuts
Summary:       Library files for %gemname-shortcuts gem
Summary(ru_RU.UTF-8):     %gemname-shortcuts
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-shortcuts
Library files for %gemname gem.

%description   -n gem-%pkgname-shortcuts -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-shortcuts-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-shortcuts-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-shortcuts-doc -l ru_RU.UTF8
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

%files         -n gem-%pkgname-shortcuts
%doc README*
%ruby_gemspecdir/%pkgname-shortcuts-2.0.0.gemspec
%ruby_gemslibdir/%pkgname-shortcuts-2.0.0

%files         -n gem-%pkgname-shortcuts-doc
%ruby_gemsdocdir/%pkgname-shortcuts-2.0.0


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- update (^) 2.1.0 -> v2.1.1
- fix (!) spec

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Bump to 2.1.0
- Use Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
