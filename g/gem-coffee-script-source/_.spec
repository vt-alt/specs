# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname coffee-script-source

Name:          gem-%pkgname
Version:       2.1.1
Release:       alt2
Summary:       CoffeeScript js sources
License:       MIT
Group:         Development/Ruby
Url:           http://coffeescript.org/
%vcs           https://github.com/joeldrapper/coffee-script-source.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
CoffeeScript is a little language that compiles into JavaScript. Underneath all
of those embarrassing braces and semicolons, JavaScript has always had a
gorgeous object model at its heart. CoffeeScript is an attempt to expose
the good parts of JavaScript in a simple way.

This is the %summary.


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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt2
- ! spec according to changelog rules

* Fri Aug 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- + packaged gem with usage Ruby Policy 2.0
