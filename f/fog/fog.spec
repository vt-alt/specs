%define        pkgname fog

Name:          %pkgname
Version:       2.2.0
Release:       alt1
Summary:       The Ruby cloud services library
License:       MIT
Group:         Development/Other
Url:           http://fog.io
%vcs           https://github.com/fog/fog.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%gem_replace_version fog-brightbox ~> 1.0

%description
fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to
  work with and switch between.
- Requests allow power users to get the most out of the features of each
  individual cloud.
- Mocks make testing and integrating a breeze.


%package       -n gem-%pkgname
Summary:       Library files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
Library files for %gemname gem.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      fog-doc
Obsoletes:     fog-doc

%description   -n gem-%pkgname-doc
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
%_bindir/%name

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- Bump to 2.2.0
- Use Ruby Policy 2.0

* Tue Nov 13 2018 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Bump to 2.1.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
