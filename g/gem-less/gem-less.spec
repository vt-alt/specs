%define        pkgname less

Name:          gem-%pkgname
Version:       2.6.0
Release:       alt2
Summary:       Leaner CSS, in your browser or Ruby (via less.js)
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://lesscss.org
Vcs:           https://github.com/cowboyd/less.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
The dynamic stylesheet language.

These are Ruby bindings for the next generation LESS, which is implemented in
JavaScript.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n lessc
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Conflicts:     lessjs

%description   -n lessc
Executable file for %gemname gem.

%description   -n lessc -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         -n lessc
%_bindir/%{pkgname}*

%changelog
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt2
- ! spec
 + + explicit conflict for bump to lessjs
 + * minor

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
