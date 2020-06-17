# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname webmock

Name:          gem-%pkgname
Version:       3.7.5
Release:       alt1
Summary:       Library for stubbing and setting expectations on HTTP requests in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bblimke/webmock
%vcs           https://github.com/bblimke/webmock.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

* Stubbing HTTP requests at low http client lib level (no need to change tests
  when you change HTTP library)
* Setting and verifying expectations on HTTP requests
* Matching requests based on method, URI, headers and body
* Smart matching of the same URIs in different representations (also encoded and
  non encoded forms)
* Smart matching of the same headers in different representations.
* Support for Test::Unit
* Support for RSpec
* Support for MiniTest


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
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.5-alt1
- updated ti (^) v3.7.5
- fix (!) spec

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- ̈added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0
