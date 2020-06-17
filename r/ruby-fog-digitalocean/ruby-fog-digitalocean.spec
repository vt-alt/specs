%define        pkgname fog-digitalocean

Name:          ruby-%pkgname
Version:       0.4.0
Release:       alt1
Summary:       Fog for DigitalOcean Platform
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-digitalocean
%vcs           https://github.com/fog/fog-digitalocean.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Bump to 0.4.0
- Use Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
