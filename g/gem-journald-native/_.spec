# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname journald-native

Name:          gem-%pkgname
Version:       1.0.11
Release:       alt1.3
Summary:       systemd-journal logging interface wrapper for ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/theforeman/journald-native
Vcs:           https://github.com/theforeman/journald-native.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libsystemd-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A systemd-journal native logging lib wrapper.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development headers for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
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
%ruby_gemextdir
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1.3
- ! spec tag

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1.1
- fixed (!) spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1
- + packaged gem with usage Ruby Policy 2.0
