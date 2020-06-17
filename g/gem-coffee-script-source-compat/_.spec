# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname coffee-script-source
%define        gemname coffee-script-source

Name:          gem-%pkgname-compat
Version:       1.12.2
Release:       alt3
Summary:       CoffeeScript js sources
License:       MIT
Group:         Development/Ruby
Url:           http://coffeescript.org/
Vcs:           https://github.com/NickClark/coffee-script-source.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
CoffeeScript is a little language that compiles into JavaScript. Underneath all
of those embarrassing braces and semicolons, JavaScript has always had a
gorgeous object model at its heart. CoffeeScript is an attempt to expose
the good parts of JavaScript in a simple way.

This is the %summary version 1.12.2.



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
%ruby_build --use=%gemname --alias=%pkgname-compat

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.12.2-alt3
- ! spec provides and obsoletes, and EVR

* Wed Sep 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.12.2-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
