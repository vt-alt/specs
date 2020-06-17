%define        pkgname logging

Name:          gem-%pkgname
Version:       2.2.2
Release:       alt2.1
Summary:       A flexible logging library for use in Ruby programs based on the design of Java's log4j library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/logging
Vcs:           https://github.com/TwP/logging.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Logging is a flexible logging library for use in Ruby programs based on
the design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.


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
%ruby_build --use=%gemname --version-replace=%version

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
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt2.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt2
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus
