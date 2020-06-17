%define        pkgname fog-dnsimple

Name:          ruby-%pkgname
Version:       2.1.0
Release:       alt2
Epoch:         1
Summary:       Module for the 'fog' gem to support DNSimple.
License:       MIT
Group:         Development/Ruby
Url:           https://developer.dnsimple.com/
%vcs           https://github.com/fog/fog-dnsimple.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:  %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary

%package       doc
Summary:       Documentation files for %gemname gem
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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.1.0-alt2
- Bump to 2.1.0
- Use Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.0.0-alt1
- Reset to old version for fog.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
