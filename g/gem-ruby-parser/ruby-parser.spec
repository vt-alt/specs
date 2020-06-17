%define        pkgname ruby-parser
%define        gemname ruby_parser

Name:          gem-%pkgname
Version:       3.14.2
Release:       alt0.1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby_parser
Vcs:           https://github.com/seattlerb/ruby_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: unifdef
BuildRequires: gem-hoe
BuildRequires: gem(sexp_processor)
BuildRequires: gem(oedipus_lex)
BuildRequires: gem-racc

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc-which does by default use a C extension). RP's output is the same
as ParseTree's output: s-expressions using ruby's arrays and base types.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc-which does by default use a C extension). RP's output is the same
as ParseTree's output: s-expressions using ruby's arrays and base types.

Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%prep
%setup

%build
%ruby_build ́--pre=repackage --use=%gemname --alias=parser --join=bin:lib --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.14.2-alt0.1
- updated (^) 3.13.1 -> 3.14.2
- fixed (!) spec

* Wed Sep 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt2
- fixed (!) ref to v3.13.1

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt1
- updated (^) 3.13.0 -> 3.13.1
- fixed (!) spec

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- added (+) using setup gem's dependency detection
- updated (^) 3.12.0 -> 3.13.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.12.0-alt1
- updated (^) 3.11.0 -> 3.12.0
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- Initial build for Sisyphus
