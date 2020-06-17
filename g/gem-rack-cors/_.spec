# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rack-cors

Name:          gem-%pkgname
Version:       1.0.3
Release:       alt1.1
Summary:       Middleware that will make Rack-based apps CORS compatible
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cyu/rack-cors
%vcs           https://github.com/cyu/rack-cors.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Rack Middleware for handling Cross-Origin Resource Sharing (CORS), which makes
cross-origin AJAX possible.

Build Status

Rack::Cors provides support for Cross-Origin Resource Sharing (CORS) for Rack
compatible web applications.

The CORS spec allows web applications to make cross domain AJAX calls without
using workarounds such as JSONP. See Cross-domain Ajax with Cross-Origin
Resource Sharing.


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
%ruby_build --ignore=rails4,rack

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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- + packaged gem with usage Ruby Policy 2.0
