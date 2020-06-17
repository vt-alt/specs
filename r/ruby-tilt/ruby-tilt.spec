# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname tilt

Name: 	       ruby-%pkgname
Version:       2.0.10
Release:       alt1
Summary:       Generic interface to multiple Ruby template engines
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rtomayko/tilt
%vcs           https://github.com/rtomayko/tilt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ronn)

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Tilt is a thin interface over a bunch of different Ruby template engines in an
attempt to make their usage as generic as possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):
* Custom template evaluation scopes / bindings
* Ability to pass locals to template evaluation
* Support for passing a block to template evaluation for "yield"
* Backtraces with correct filenames and line numbers
* Template file caching and reloading
* Fast, method-based template source compilation


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         -n %pkgname
%_bindir/%{pkgname}*
%_mandir/%pkgname.1*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.10-alt1
- updated to (^) v2.0.10
- fixed (!) spec

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.9-alt2
- updated to (^) Ruby Policy 2.0

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.9-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Oct 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1
- New version

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- Initial build for Sisyphus
