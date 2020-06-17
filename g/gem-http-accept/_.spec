# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname http-accept

Name:          gem-%pkgname
Version:       1.7.0
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/http-accept
%vcs           https://github.com/socketry/http-accept.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary. Provides a robust set of parsers for dealing with HTTP Accept,
Accept-Language, Accept-Encoding, Accept-Charset headers.


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
* Wed Sep 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
