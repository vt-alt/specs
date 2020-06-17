# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname augeas

Name:          gem-%pkgname
Version:       0.6.4
Release:       alt1
Summary:       A fork of ruby-augeas (bindings for augeas) with exceptions support
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           http://augeas.net/
Vcs:           https://github.com/dotdoom/augeas.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libaugeas-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary. The class Augeas provides bindings to augeas [augeas.net] library.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Requires:      libaugeas-devel

%description   devel
Development headers for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
