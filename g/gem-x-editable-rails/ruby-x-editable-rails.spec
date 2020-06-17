# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname x-editable-rails

Name:          gem-%pkgname
Version:       1.5.5.1
Release:       alt3.1
Summary:       Edit fields easily with X-Editable helper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/werein/x-editable-rails
Vcs:           https://github.com/werein/x-editable-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

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
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.5.1-alt3.1
- ! spec tags

* Wed Sep 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.5.1-alt3
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt2
- Disable tests.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt1
- New version.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- Initial build for Sisyphus
