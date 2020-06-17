%define        pkgname unf-ext
%define        gemname unf_ext

Name: 	       gem-%pkgname
Version:       0.0.7.6
Release:       alt1
Summary:       Unicode Normalization Form support library for CRuby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-unf_ext
Vcs:           https://github.com/knu/ruby-unf_ext.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.7.6-alt1
- ^ 0.0.7.5 -> 0.0.7.6
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.7.5-alt2
- > Ruby Policy 2.0

* Wed Aug 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.3
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.0.M80P.1
- Rebuild with Ruby 2.4.2

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.1
- Rebuild with Ruby 2.4.2

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1
- Initial build for Sisyphus.
