%define        pkgname json

Name:          gem-%pkgname
Version:       2.3.1
Release:       alt0.1
Summary:       JSON parser and generator
License:       MIT
Group:         Development/Ruby
Url:           http://flori.github.io/json/
Vcs:           https://github.com/flori/json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR
Obsoletes:     ruby-json-utils ruby-json-pure
Provides:      ruby-json-utils ruby-json-pure

%description
This library can parse JSON texts and generate them from ruby data
structures.


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


%package       pure
Summary:       JSON parser and generator
Group:         Development/Documentation
BuildArch:     noarch

%description   pure
This library can parse JSON texts and generate them from ruby data
structures.

The package is the compiled-less version of the %pkgname gem.

%package       pure-doc
Summary:       Documentation files for json_pure gem
Group:         Development/Documentation
BuildArch:     noarch

%description   pure-doc
Documentation files for json_pure gem

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета json_pure.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version --use=%{gemname}_pure --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*

%files         pure
%ruby_gemspecdir/json_pure-%version.gemspec
%ruby_gemslibdir/json_pure-%version

%files         pure-doc
%ruby_gemsdocdir/json_pure-%version

%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt0.1
- ^ 2.2.0 -> 2.3.1
- ! spec tags and syntax

* Wed Mar 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- > Ruby Policy 2.0
- ^ 2.1.0 -> 2.2.0

* Wed Jan 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- ! provides and obsoletes.

* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- 1.5.1 -> 2.1.0

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.5.1-alt1
- [1.5.1]

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.9-alt1
- [1.1.9]

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.7-alt1
- Built for Sisyphus
