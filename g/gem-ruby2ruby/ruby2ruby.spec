%define        pkgname ruby2ruby

Name:          gem-%pkgname
Version:       2.4.4
Release:       alt1
Summary:       ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby2ruby
Vcs:           https://github.com/seattlerb/ruby2ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sexp_processor)
BuildRequires: gem(parser)
BuildRequires: gem(hoe)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname
Provides:      %pkgname

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!


%package       -n r2r_show
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n r2r_show
Executable file for %gemname gem.

%description   -n r2r_show -l ru_RU.UTF8
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

%files         -n r2r_show
%_bindir/r2r_show

%files         doc
%ruby_gemdocdir

%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.4-alt1
- updated (^) 2.4.3 -> 2.4.4
- fixed (-) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt1.1
- fixed (!) spec according to changelog rules

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt1
- updated (^) 2.4.2 -> 2.4.3
- added (+) rpm "r2r_show" build
- fixed (!) spec

* Sat Mar 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt2
- Use Ruby Policy 2.0
- Bump to 2.4.2

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
