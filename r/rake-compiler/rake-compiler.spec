%define        pkgname rake-compiler
%define        gemname rake-compiler

Name:          %pkgname
Version:       1.1.0
Release:       alt1
Summary:       Provide a standard and simplified way to build and package Ruby C and Java extensions using Rake as glue.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rake-compiler/rake-compiler
# VCS          https://github.com/rake-compiler/rake-compiler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
rake-compiler is first and foremost a productivity tool for Ruby
developers. Its goal is to make the busy developer's life easier by
simplifying the building and packaging of Ruby extensions by simplifying
code and reducing duplication.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.


%prep
%setup

%build
%gem_build --use=rake-compiler --join=lib:bin

%install
%gem_install

%check
%gem_test

%files
%_bindir/%name
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Dec 25 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt1
- New version.

* Wed Nov 06 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.8-alt1
- New version.

* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt3
- Fix built provides (closes #36888)

* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt2
- Use Ruby Policy 2.0.

* Fri Jan 04 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Wed Jul 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Package as gem.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
