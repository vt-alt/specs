%define        pkgname cap2

Name:          gem-%pkgname
Version:       0.2.2
Release:       alt2.3
Summary:       A Ruby library for managing Linux process and file capabilities
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lmars/cap2
Vcs:           https://github.com/lmars/cap2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcap-devel
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Cap2 is a Ruby library for managing the POSIX 1003.1e capabilities available in
Linux kernels. These capabilities are a partitioning of the all powerful root
privilege into a set of distinct privileges. See capabilities(7) for more
information.


%package       devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
%ruby_gemlibdir
%ruby_gemspec
%ruby_gemextdir

%files         devel
%ruby_includedir/%gemname

%files         doc
%ruby_gemdocdir


%changelog
* Tue Apr 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2.3
- ! spec's obsoletes/provides pair

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2.1
- fixed (!) spec according to changelog rules

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2
- used (>) Ruby Policy 2.0
- fixed (!) spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.1
- Rebuild for aarch64.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus
