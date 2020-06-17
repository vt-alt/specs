# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname train-winrm

Name:          gem-%pkgname
Version:       0.2.6
Release:       alt1
Summary:       WinRM transport for Train
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/inspec/train-winrm
Vcs:           https://github.com/inspec/train-winrm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

This plugin allows applications that rely on Train to communicate with the
WinRM API. For example, you could use this to audit Windows Server 2016
machines.

This plugin relies on the winrm and winrm-fs gems for implementation.

Train itself has no CLI, nor a sophisticated test harness. Chef InSpec does have
such facilities, so installing Train plugins will require a Chef InSpec
installation. You do not need to use or understand Chef InSpec.

Train plugins may be developed without a Chef InSpec installation.


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
* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.6-alt1
- + packaged gem with usage Ruby Policy 2.0
