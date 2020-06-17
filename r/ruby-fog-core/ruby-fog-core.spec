%define        pkgname fog-core

Name:          ruby-%pkgname
Version:       2.1.2
Release:       alt1
Epoch:         1
Summary:       fog's core, shared behaviors without API and provider specifics
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-core
# VCS:         https://github.com/fog/fog-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Shared classes and tests for fog providers and services.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
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
* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.1.2-alt1
- Bump to 2.1.2
- Use Ruby Policy 2.0

* Wed Aug 29 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.45.0-alt1
- Decrease version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
