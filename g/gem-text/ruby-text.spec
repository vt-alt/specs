%define        pkgname text

Name: 	       gem-%pkgname
Version:       1.3.1
Release:       alt5
Summary:       Collection of text algorithms
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/threedaymonk/text
Vcs:           https://github.com/threedaymonk/text.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Collection of text algorithms: Levenshtein, Soundex, Metaphone, Double
Metaphone, Porter Stemming.

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

%files         doc
%ruby_gemdocdir


%changelog
* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt5
- > Ruby Policy 2.0
- ! spec tags

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt4.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt4
- Use system way to package as gem.

* Thu Jun 28 2018 Denis Medvedev <nbr@altlinux.org> 1.3.1-alt3.1
- removed patch from package

* Thu Jun 28 2018 Denis Medvedev <nbr@altlinux.org> 1.3.1-alt3
- fix build: alt-gemspec patch no longer needed

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt2
- Rebuild with Ruby 2.4.2

* Mon May 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build in Sisyphus
