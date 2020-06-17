# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname fog-openstack

Name:          ruby-%pkgname
Version:       1.0.10
Release:       alt1
Summary:       Fog for OpenStack Platform
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-openstack
%vcs           https://github.com/fog/fog-openstack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary. This is the plugin Gem to talk to OpenStack clouds via fog.

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
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.10-alt1
- update (^) 1.0.8 -> 1.0.10
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- Bump to 1.0.8
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.24-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.24-alt1
- Initial build for Sisyphus
