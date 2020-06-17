# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname ruby-ll

Name:          gem-%pkgname
Version:       2.1.2
Release:       alt1.2
Summary:       An LL(1) parser generator for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/yorickpeterse/ruby-ll
Vcs:           https://gitlab.com/yorickpeterse/ruby-ll.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
BuildRequires: gem(rake)
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard)
BuildRequires: gem(simplecov)
BuildRequires: gem(kramdown)
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(rake-compiler)
BuildRequires: gem(ast)
BuildRequires: gem(ansi)
BuildRequires: ragel

%description
ruby-ll is a high performance LL(1) table based parser generator for Ruby.
The parser driver is written in C/Java to ensure good runtime performance,
the compiler is written entirely in Ruby.

ruby-ll was written to serve as a fast and easy to use alternative to Racc
for the various parsers used in Oga. However, ruby-ll isn't limited to just Oga,
you can use it to write a parser for any language that can be represented using
an LL(1) grammar.

ruby-ll is self-hosting, this allows one to use ruby-ll to modify its own
parser. Self-hosting was achieved by bootstrapping the parser using a Racc
parser that outputs the same AST as the ruby-ll parser. The Racc parser remains
in the repository for historical purposes and in case it's ever needed again,
it can be found in bootstrap/parser.y.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
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


%package       devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   devel
Development headers for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --pre=lexer,parser --use=%gemname --alias=%pkgname

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemextdir
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1.2
- ! spec tag

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1.1
- ! spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- + packaged as a gem with usage Ruby Policy 2.0
