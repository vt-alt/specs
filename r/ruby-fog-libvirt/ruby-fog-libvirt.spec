%define        pkgname fog-libvirt

Name:          ruby-%pkgname
Version:       0.6.0
Release:       alt1
Summary:       libvirt provider for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-libvirt
%vcs           https://github.com/fog/fog-libvirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
fog-libvirt is a libvirt provider for fog.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- Bump to 0.6.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
