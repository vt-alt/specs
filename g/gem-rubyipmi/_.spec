# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rubyipmi

Name:          gem-%pkgname
Version:       0.10.0
Release:       alt1
Summary:       Command line wrapper for ipmitool and freeipmi
License:       LGPLv2+
Group:         Development/Ruby
Url:           https://github.com/logicminds/rubyipmi
Vcs:           https://github.com/logicminds/rubyipmi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Provides a library for controlling IPMI devices using pure ruby code.


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
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with usage Ruby Policy 2.0
