%define        pkgname curb

Name: 	       gem-%pkgname
Version:       0.9.10
Release:       alt1
Summary:       Ruby bindings for libcurl
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/taf2/curb
Vcs:           https://github.com/taf2/curb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcurl-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for
the libcurl(3), a fully-featured client-side URL transfer library. cURL and
libcurl live at http://curl.haxx.se/ .

Curb is a work-in-progress, and currently only supports libcurl's 'easy' and
'multi' modes.


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
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.10-alt1
- ^ 0.9.9 -> 0.9.10
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.9-alt1
- > Ruby Policy 2.0
- ^ 0.9.7 -> 0.9.9

* Wed Nov 07 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.7-alt1
- ^ 0.9.6 -> 0.9.7

* Fri Nov 02 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.6-alt1
- ^ 0.9.4 -> 0.9.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.6
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.5
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Leonid Krivoshein <klark@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
