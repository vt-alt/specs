%define  pkgname facets

Name:          ruby-%pkgname
Version:       3.1.0
Release:       alt2
Summary:       Ruby Facets
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://github.com/rubyworks/facets
%vcs           https://github.com/rubyworks/facets.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
%filter_from_requires \,^ruby(facets/string/random_binary),d

%description
Ruby Facets is the premiere collection of general purpose method
extensions and standard additions for the Ruby programming language.

Facets houses the largest single collection of methods available for
extending the core capabilities of Ruby's built-in classes and modules.
This collection of extension methods are unique by virtue of their
atomicity. The methods are stored in individual files so that each can
be required independently. This gives developers the potential for much
finer control over which extra methods to bring into their code.

In addition Facets provides a collection of extensions to Ruby standard
library plus a small collection of add-on classes and modules. Together
these libraries constitute an reliable source of reusable components,
suitable to a wide variety of usecases.


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
* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
