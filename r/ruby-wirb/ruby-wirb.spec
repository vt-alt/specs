%define        pkgname wirb

Name:          ruby-%pkgname
Version:       2.1.2
Release:       alt2
Summary:       Don't use an IRB without WIRB
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/wirb
%vcs           https://github.com/janlelis/wirb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary!

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
* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus
