# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname hansi

Name:          gem-%pkgname
Version:       0.2.0
Release:       alt1
Summary:       Der ANSI Hansi - create colorized console output
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rkh/hansi
Vcs:           https://github.com/rkh/hansi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.
Welcome to The ANSI Hansi. This is your Hipster ANSI color library.
It allows you to produce colorized console output. Many ANSI color libraries
are already out there. However, this library tackles a few issues most of them
have:

* It supports 8 color, 16 color, 88 color, 256 color and 24 bit (True Color)
  mode.
* It transparently converts colors between modes without you having to worry
  about this. It uses the YUV distance (rather than the RGB distance) to closer
  match how our brain perceives color similarity.
* It supports proper color nesting.
* It can automatically detect how many colors the current terminal supports.
* It does not enforce a DSL to be used (in fact, it does not include a DSL, but
  it makes it really easy to build your own DSL).
* Makes it easy to define string templates for highlighting, but doesn't force
  you to use them.
* It supports themes, but doesn't force you to use them. Themes make semantic
  coloring easier.
* It supports converting ANSI colors to CSS rules. It does not support parsing
  an ANSI colored string into HTML, this would be outside the scope of this
  library.
* It has zero dependencies and does not include a native extension.
* It does not monkey patch anything.


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
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with usage Ruby Policy 2.0
