%define        pkgname treetop

Name: 	       ruby-%pkgname
Epoch:         1
Version:       1.6.10
Release:       alt2
Summary:       A Ruby-based text parsing and interpretation DSL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cjheath/treetop
%vcs           https://github.com/cjheath/treetop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Treetop is a language for describing languages. Combining the elegance
of Ruby with cutting-edge parsing expression grammars, it helps you
analyze syntax with revolutionary ease.


%package       -n tt
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n tt
Executable file for %gemname gem.

%description   -n tt -l ru_RU.UTF8
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
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n tt
%_bindir/tt
%_mandir/tt*

%files         doc
%ruby_gemdocdir


%changelog
* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.6.10-alt2
^ Ruby Policy 2.0
^ v1.6.10

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1.1.1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.10-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.10-alt1
- New version.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.5-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux
