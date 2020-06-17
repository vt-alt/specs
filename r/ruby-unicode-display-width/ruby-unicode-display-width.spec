%define        pkgname unicode-display-width
%define        gemname unicode-display_width

Name:          ruby-unicode-display-width
Version:       1.6.0
Release:       alt1
Summary:       Monospace Unicode character width in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/unicode-display_width
%vcs           https://github.com/janlelis/unicode-display_width.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar
Patch:         alt-fix-datadir.patch

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

%files
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir


%changelog
* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
^ v1.6.0

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Bump to 1.4.1;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
