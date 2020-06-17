%define        pkgname unf
Name: 	       gem-%pkgname
Version:       0.2.0
Release:       alt0.1
Summary:       A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-unf
Vcs:           https://github.com/knu/ruby-unf.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
%summary.

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

%files doc
%ruby_gemdocdir


%changelog
* Fri Apr 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt0.1
- > Ruby Policy 2.0
- ^ 0.1.4 -> 0.2.0pre
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus.
