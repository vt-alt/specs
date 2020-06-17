%define  pkgname haml

Name: 	       ruby-%pkgname
Version:       5.1.1
Release:       alt1
Summary:       HTML Abstraction Markup Language - A Markup Haiku
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/haml/haml
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%filter_from_requires \!^ruby(haml/filters/textile)$!d;
%filter_from_requires \!^ruby(haml/filters/maruku)$!d;
%filter_from_requires /^ruby(action_view)$/d;

%description
Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting
the underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         -n %pkgname
%_bindir/%pkgname

%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.1-alt1
- Bump to 5.1.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.3-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.0.3-alt1
- Initial build for Sisyphus
