%define        pkgname apipie-params

Name:          gem-%pkgname
Version:       0.0.5
Release:       alt2
Summary:       DSL for describing data structures with json-schema bindings
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/iNecas/apipie-params
Vcs:           https://github.com/iNecas/apipie-params.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

DSL for Hash/JSON descriptions. Describe format of hashes using Ruby code,
generate a json-schema for it and validate values against it.


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
* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus
