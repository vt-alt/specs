%define        pkgname fog-brightbox

Name:          ruby-%pkgname
Version:       1.0.0
Release:       alt1
Summary:       Brightbox Cloud support for the fog gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-brightbox
%vcs           https://github.com/fog/fog-brightbox.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary. Officially supported.

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
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Use Ruby Policy 2.0
- Bump to 1.0.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
