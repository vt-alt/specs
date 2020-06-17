%define        pkgname multi-json
%define        gemname multi_json

Name: 	       gem-%pkgname
Version:       1.14.1
Release:       alt1
Summary:       A common interface to multiple JSON libraries
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/intridea/multi_json
Vcs:           https://github.com/intridea/multi_json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(yajl-ruby)
BuildRequires: gem(json_pure)
BuildRequires: gem(oj)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
A common interface to multiple JSON libraries, including Oj, Yajl, the
JSON gem (with C-extensions), the pure-Ruby JSON gem,
NSJSONSerialization, gson.rb, JrJackson, and OkJson.


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
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.14.1-alt1
- > Ruby Policy 2.0
- ^ 1.13.1 -> 1.14.1
- ! spec tags and syntax

* Wed Aug 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt2.1
- Rebuild for new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt2
- Package as gem.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.13.0-alt1
- New version.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.12.2-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt1
- Initial build for ALT Linux
