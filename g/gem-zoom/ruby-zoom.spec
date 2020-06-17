%define        pkgname zoom

Name:          gem-%pkgname
Version:       0.5.0
Release:       alt3.1
Summary:       Ruby binding to the Z39.50 Object-Orientation Model (ZOOM)
Group:         Development/Ruby
License:       LGPLv2.1
Url:           https://github.com/bricestacey/ruby-zoom
Vcs:           https://github.com/bricestacey/ruby-zoom.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-test-unit
BuildRequires: libyaz-devel
BuildRequires: zlib-devel
BuildRequires: libgcrypt-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model
(ZOOM), an abstract object-oriented programming interface to a subset of the
services specified by the Z39.50 standard, also known as the international
standard ISO 23950.

This software is based (and therefore depends) on YAZ, a free-software
implementation of the Z39.50/SRW/SRU standards, but could be easily ported to
any ZOOM compliant implementation.


%package       devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libyaz-devel
Requires:      zlib-devel
Requires:      libgcrypt-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files devel
%ruby_includedir/*

%changelog
* Wed Apr 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt3.1
- + proper buildarch for devel package

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt3
- ! spec tags

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt2
- Fix build

* Thu Feb 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- Bump to 0.5;
- Use Ruby Policy 2.0.

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.1-alt3
- Repair build

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt2
- Rebuilt with Ruby 1.9.2

* Sun May 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.1-alt1
- Built for Sisyphus

