%define        pkgname fog-profitbricks

Name:          ruby-%pkgname
Version:       4.1.1
Release:       alt1
Summary:       Module for the 'fog' gem to support ProfitBricks
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-profitbricks
%vcs           https://github.com/fog/fog-profitbricks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
%gem_replace_version fog-core ~> 2.0

%description
This library can be used as a module for 'fog' or as standalone ProfitBricks
provider.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.1-alt1
- Bump to 4.1.1
- Use Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus
