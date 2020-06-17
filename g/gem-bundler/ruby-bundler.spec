%define        pkgname bundler

Name:          gem-%pkgname
Version:       2.1.4
Release:       alt1
Summary:       Manage your Ruby application's gem dependencies
License:       MIT
Group:         Development/Ruby
Url:           https://bundler.io/
Vcs:           https://github.com/bundler/bundler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ronn)
BuildRequires: groff-base

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Bundler makes sure Ruby applications run the same code on every machine.
It does this by managing the gems that the application depends on. Given
a list of gems, it can automatically download and install those gems, as
well as any other gems needed by the gems that are listed. Before
installing gems, it checks the versions of every gem to make sure that
they are compatible, and can all be loaded at the same time. After the
gems have been installed, Bundler can help you update some or all of
them when new versions become available. Finally, it records the exact
versions that have been installed, so that others can install the exact
same gems.


%package       -n bundle
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Conflicts:     golang-tools

%description   -n bundle
Executable file for %gemname gem.

%description   -n bundle -l ru_RU.UTF8
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
%ruby_build --ignore=templates

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n bundle
%doc README*
%_bindir/*
%_mandir/*

%files         doc
%ruby_gemdocdir

%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.4-alt1
- updated (^) 2.0.2 -> 2.1.4
- fixed (!) spec

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt2
- added (+) ignore templates gemfile
- fixed (!) spec according changelog policy

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- updated (^) 2.0.1 -> 2.0.2
- fixed (!) spec
- removed (-) findreq build error

* Mon Mar 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt2
- Use Ruby Policy 2.0.

* Wed Jan 9 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- Bump to 2.0.1.
- Place library files into gem folder.

* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.17.1-alt1
- Bump to 1.17.1.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.6-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.5-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.4-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt3.2
- Rebuild with new Ruby autorequirements.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt3.1
- Disable all ruby(*) autoreqs for bootstrap.
- Disable man page generation for bootstrap.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt3
- Fix gemspec name.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt2
- Clarify ignored modules.
- Use common way to package as gem.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.2-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus
