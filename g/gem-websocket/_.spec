# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname websocket

Name:          gem-%pkgname
Version:       1.2.8
Release:       alt1
Summary:       Universal Ruby library to handle WebSocket protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/imanel/websocket-ruby
Vcs:           https://github.com/imanel/websocket-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Universal Ruby library to handle WebSocket protocol. It focuses on providing
abstraction layer over WebSocket API instead of providing server or client
functionality.


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
* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
