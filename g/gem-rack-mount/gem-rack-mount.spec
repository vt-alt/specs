%define        pkgname rack-mount

Name:          gem-%pkgname
Version:       0.8.3
Release:       alt2
Summary:       Stackable dynamic tree based Rack router
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sporkmonger/rack-mount
Vcs:           https://github.com/sporkmonger/rack-mount.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

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
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt2
- used (>) Ruby Policy 2.0
- fixed (!) spec minorly

* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus, packaged as gem
