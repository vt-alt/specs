%define        pkgname redcarpet

Name:          gem-%pkgname
Version:       3.5.0
Release:       alt1
Summary:       The safe Markdown parser, reloaded
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vmg/redcarpet
Vcs:           https://github.com/vmg/redcarpet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Redcarpet is a Ruby library for Markdown processing that smells like
butterflies and popcorn.


%package       -n %pkgname
Summary:       HTML, XML, SAX, and Reader parser
Group:         Development/Other
BuildArch:     noarch

%description   -n %pkgname
Redcarpet is a Ruby library for Markdown processing that smells like
butterflies and popcorn.

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

%files         -n %pkgname
%_bindir/*


%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.4.0 -> 3.5.0
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt2
- > Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus
