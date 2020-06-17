%define        pkgname asciidoctor
%define        gemname asciidoctor

Name:          %pkgname
Version:       2.0.10
Release:       alt1
Summary:       A fast text processor and publishing toolchain for converting AsciiDoc content to different formats
License:       MIT
Group:         Documentation
Url:           https://github.com/asciidoctor/asciidoctor
%vcs           https://github.com/asciidoctor/asciidoctor.git
Packager:      Gordeev Mikhail <obirvalger@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch1:        asciidoctor-1.5.6.1-alt-fix-DATA_PATH.patch
BuildRequires(pre): rpm-build-ruby
# BuildRequires: nokogiri

%description
Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.


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
Obsoletes:     %pkgname-doc
Provides:      %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup
#%patch1 -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%_bindir/%pkgname
%_mandir/%pkgname.1.xz

%files         -n gem-%pkgname
%ruby_gemlibdir
%ruby_gemspec

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Thu Jun 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.10-alt1
- Use Ruby Policy 2.0
- Bump to 2.0.10

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.7.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 21 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.7.1-alt1
- Build new version.

* Thu Aug 03 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.6.1-alt1
- Initial build for Sisyphus
