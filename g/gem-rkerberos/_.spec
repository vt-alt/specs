# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rkerberos

Name:          gem-%pkgname
Version:       0.1.5
Release:       alt1
Summary:       A Ruby interface for Kerberos
License:       Artistic-2.0
Group:         Development/Ruby
Url:           https://github.com/domcleal/rkerberos
Vcs:           https://github.com/domcleal/rkerberos.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libkrb5-devel
BuildRequires: gem(rake-compiler)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
The rkerberos library provides a Ruby interface for Kerberos.

The rkerberos library is an interface for the Kerberos 5 network authentication
protocol. It wraps the Kerberos C API.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libkrb5-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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
%ruby_gemextdir

%files         devel
%ruby_includedir/*


%changelog
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with usage Ruby Policy 2.0
