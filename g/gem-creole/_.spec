%define        pkgname creole

Name:          gem-%pkgname
Version:       0.5.0
Release:       alt1
Summary:       Creole 1.0 to XHTML converter written in ruby
License:       BSD-2-Clause/Ruby
Group:         Development/Ruby
Url:           https://github.com/minad/creole
%vcs           https://github.com/minad/creole.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Creole is a Creole-to-HTML converter for Creole, the lightweight markup language
(http://wikicreole.org/). Github uses this converter to render *.creole files.


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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
