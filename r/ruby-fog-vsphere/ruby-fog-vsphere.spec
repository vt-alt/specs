%define        pkgname fog-vsphere

Name:          ruby-%pkgname
Version:       3.2.1
Release:       alt1
Summary:       Fog for vSphere
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-vsphere
%vcs           https://github.com/fog/fog-vsphere.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.2.1-alt1
- ^ v3.2.1

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ v3.1.0
- ^ Ruby Policy 2.0

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ v2.5.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
