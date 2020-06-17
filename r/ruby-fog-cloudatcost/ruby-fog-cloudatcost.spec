%define        pkgname fog-cloudatcost

Name:          ruby-%pkgname
Version:       0.4.0
Release:       alt2
Epoch:         1
Summary:       Module for the 'fog' gem to support CloudAtCost Services
License:       MIT
Group:         Development/Ruby
Url:           http://panel.cloudatcost.com/
%vcs           https://github.com/fog/fog-cloudatcost.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary http://panel.cloudatcost.com/

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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.4.0-alt2
- Use Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.1.2-alt1
- Reset to old version for fog.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
