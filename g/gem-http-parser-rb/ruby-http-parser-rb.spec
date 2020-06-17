%define        pkgname http-parser-rb
%define        gemname http_parser.rb

Name:          gem-%pkgname
Version:       0.6.1
Release:       alt3
Summary:       A simple callback-based HTTP request/response parser for writing http servers, clients and proxies
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tmm1/http_parser.rb
Vcs:           https://github.com/tmm1/http_parser.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR
Obsoletes:     gem-%gemname < %EVR
Provides:      gem-%gemname = %EVR

%description
Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java

A simple callback-based HTTP request/response parser for writing http servers,
clients and proxies.

This gem is built on top of joyent/http-parser and its java port
http-parser/http-parser.java.


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
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.



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
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt3
- ! spec tags

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt2
- ! spec tags and syntax

* Thu Apr 25 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- > Ruby Policy 2.0
- > source from github
- ^ 0.6.0 -> 0.6.1

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.5
- Rebuild for new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt2
- Rebuild with Ruby 2.3.1

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux
