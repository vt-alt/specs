# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname fog-ovirt

Name:          ruby-%pkgname
Version:       1.2.1
Release:       alt1
Summary:       fog-ovirt is an ovirt provider for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-ovirt
%vcs           https://github.com/fog/fog-ovirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- update (^) 1.2.0 -> 1.2.1
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Bump to 1.2.0
- Use Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
