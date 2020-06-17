# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname sdoc

Name:          %pkgname
Version:       1.0.0
Release:       alt2
Summary:       rdoc generator html with javascript search index
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zzak/sdoc
%vcs           https://github.com/zzak/sdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
SDoc is an HTML template built on top of the RDoc documentation
generator for Ruby code.


%package       -n gem-%pkgname
Summary:       Library for %gemname gem
Summary(ru_RU.UTF-8): Библиотечные файлы для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
Library for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
Библиотечные файлы для %gemname самоцвета.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
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
%_bindir/%{pkgname}*

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
