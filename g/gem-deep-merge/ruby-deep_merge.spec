%define        pkgname deep-merge
%define        gemname deep_merge

Name:          gem-%pkgname
Version:       1.2.1
Release:       alt4.1
Summary:       Recursive merging for Ruby hashes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/danielsdeleo/deep_merge
Vcs:           https://github.com/danielsdeleo/deep_merge.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Deep Merge is a simple set of utility functions for Hash. It permits you
to merge elements inside a hash together recursively. The manner by
which it does this is somewhat arbitrary (since there is no defining
standard for this) but it should end up being pretty intuitive and do
what you expect.


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
* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt4.1
- ! spec tags

* Fri Jan 24 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt4
- Added (+) proper obsolete dependency for gem-deep-merge package

* Thu Jan 23 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt3
- Added (+) proper obsolete dependency for older gems

* Fri Dec 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt2
- Use Ruby Policy 2.0

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.
- Package as gem.

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux
