# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname tty-color

Name:          gem-%pkgname
Version:       0.5.0
Release:       alt1.1
Summary:       Terminal color capabilities detection
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
%vcs           https://github.com/piotrmurach/tty-color.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

TTY::Color provides independent color support detection component for TTY
toolkit.


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
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with usage Ruby Policy 2.0
