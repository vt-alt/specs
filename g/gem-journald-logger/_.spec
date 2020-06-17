# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname journald-logger

Name:          gem-%pkgname
Version:       2.0.4
Release:       alt1.1
Summary:       systemd-journal native logger
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sandfoxme/journald-logger
%vcs           https://github.com/sandfoxme/journald-logger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A Logger drop-in replacement that logs directly to systemd-journal with some
additional features.


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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- + packaged gem with usage Ruby Policy 2.0
