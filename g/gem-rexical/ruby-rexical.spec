%define        pkgname rexical

Name:          gem-%pkgname
Version:       1.0.7
Release:       alt1.3
Summary:       Lexical scanner generator for ruby
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/tenderlove/rexical
Vcs:           https://github.com/tenderlove/rexical.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-hoe

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Rexical is a lexical scanner generator. It is written in Ruby itself,
and generates Ruby program. It is designed for use with Racc.


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
mv %buildroot%_bindir/rex %buildroot%_bindir/rex.rb

%files
%_bindir/rex.rb
%ruby_gemspec
%ruby_gemlibdir/*

%files         doc
%ruby_gemdocdir/*


%changelog
* Wed May 27 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1.3
- ! spec and syntax
- * relicensed

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1.1
- fixed (!) spec according to changelog rules

* Mon Aug 12 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1
- updated (^) 1.0.5.gitd8af06b89 -> 1.0.7
- fixed (!) spec
- fixed (!) rename executable rex to rex.rb

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt4.gitd8af06b89
- Use Ruby Policy 2.0;
- Use latest git commit.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt3.1
- Rebuild with new Ruby autorequirements.

* Thu Dec 13 2012 Led <led@altlinux.ru> 1.0.5-alt3
- rename %%_bindir/rex -> %%_bindir/rexical for avoid file conflict
  with (R)?ex (rex package)
- fixed BuildRequires

* Fri Nov 30 2012 Led <led@altlinux.ru> 1.0.5-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt2
- Pick off rubygems.

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt1
- [1.0.5]
