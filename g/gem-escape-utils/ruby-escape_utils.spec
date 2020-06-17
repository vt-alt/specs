%define        pkgname escape-utils
%define        gemname escape_utils

Name:          gem-%pkgname
Version:       1.2.1 
Release:       alt3
Summary:       Faster string escaping routines for your ruby apps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brianmario/escape_utils
Vcs:           https://github.com/brianmario/escape_utils.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Being as though we're all html escaping everything these days, why not make it
faster?

For character encoding in 1.9, the output string's encoding is copied from
the input string.

It has monkey-patches for Rack::Utils, CGI, URI, ERB::Util and Haml and
ActionView so you can drop this in and have your app start escaping fast as
balls in no time

It supports HTML, URL, URI and Javascript escaping/unescaping.


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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt3
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt2
- > Ruby Policy 2.0

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.5
- Build for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
