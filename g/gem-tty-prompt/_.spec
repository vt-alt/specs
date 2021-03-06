# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname tty-prompt

Name:          gem-%pkgname
Version:       0.22.0.1
Release:       alt0.1
Summary:       A beautiful and powerful interactive command line prompt
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-prompt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

TTY::Prompt provides independent prompt component for TTY toolkit.


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
* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 0.22.0.1-alt0.1
- ^ 0.19.0 -> 0.22.0.1
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt1
- + packaged gem with usage Ruby Policy 2.0
