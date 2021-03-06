# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname wmi-lite

Name:          gem-%pkgname
Version:       1.0.5
Release:       alt1
Summary:       Lightweight, low-dependency wrapper for basic WMI functionality on Windows
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/wmi-lite
Vcs:           https://github.com/chef/wmi-lite.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A lightweight utility over win32ole for accessing basic WMI (Windows Management
Instrumentation) functionality in the Microsoft Windows operating system. It has
no runtime dependencies other than Ruby, so it can be used without concerns
around dependency issues.


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
* Wed Jul 8 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with usage Ruby Policy 2.0
