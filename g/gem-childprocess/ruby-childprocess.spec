%define        pkgname childprocess

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       Cross-platform Ruby library for managing child processes.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/enkessler/childprocess
Vcs:           https://github.com/enkessler/childprocess
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
%summary


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
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- updated (^) 2.0.0 -> 3.0.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- updated (^) 0.9.0 -> 2.0.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus
