# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname logging-journald

Name:          gem-%pkgname
Version:       2.0.3
Release:       alt1.1
Summary:       Plugin for logging gem providing journald appender
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lzap/logging-journald
%vcs           https://github.com/lzap/logging-journald.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Logging Journald is a plugin for logging gem - the flexible logging library for
use in Ruby programs. It supports logging to system journal via journald-logger
and journald-native gems.


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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt1
- + packaged gem with usage Ruby Policy 2.0
