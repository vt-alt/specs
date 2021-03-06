# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname hrx

Name:          gem-%pkgname
Version:       1.0.0.1
Release:       alt0.1
Summary:       A Ruby implementation of the HRX format
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/google/hrx-ruby
Vcs:           https://github.com/google/hrx-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%gem_replace_version thor ~> 1.0

%description
%summary. This gem is a parser and serializer for the HRX format.


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
%ruby_build --use=%gemname --version-replace=%version

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

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt0.1
- ^ 1.0.0 -> 1.0.0.1pre
- * relicensing
- ! deps

* Tue Feb 18 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
