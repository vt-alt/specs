%define        pkgname fog-joyent

Name:          ruby-%pkgname
Version:       0.0.2
Release:       alt2
Epoch:         1
Summary:       Module for the 'fog' gem to support Joyent
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-joyent
%vcs           https://github.com/fog/fog-joyent.git
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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.0.2-alt2
- Bump to 0.0.2
- Use Ruby Policy 2.0

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.1-alt1
- Decrease version for fog-core.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
