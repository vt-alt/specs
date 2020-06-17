# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname oga

Name:          gem-%pkgname
Version:       2.17
Release:       alt1
Summary:       Oga is an XML/HTML parser written in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/yorickpeterse/oga
Vcs:           https://gitlab.com/yorickpeterse/oga.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard)
BuildRequires: gem(simplecov)
BuildRequires: gem(kramdown)
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(rake-compiler)
BuildRequires: gem-ruby-ll >= 2.1
BuildRequires: gem(ast)
BuildRequires: gem-ox
BuildRequires: gem-nokogiri
BuildRequires: ragel
BuildRequires: /usr/bin/ruby-ll

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Oga is an XML/HTML parser written in Ruby. It provides an easy to use API for
parsing, modifying and querying documents (using XPath expressions). Oga does
not require system libraries such as libxml, making it easier and faster to
install on various platforms. To achieve better performance Oga uses a small,
native extension (C for MRI/Rubinius, Java for JRuby).

Oga provides an API that allows you to safely parse and query documents in
a multi-threaded environment, without having to worry about your applications
blowing up.


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
%ruby_build --pre=lexer,parser

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemextdir
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 2.17-alt1
- ^ 2.15 -> 2.17
- ! spec tag

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.15-alt1.1
- ! spec according to changelog rules

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.15-alt1
- + packaged as a gem with usage Ruby Policy 2.0
