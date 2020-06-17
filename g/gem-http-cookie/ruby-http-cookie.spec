%define        pkgname http-cookie

Name:          gem-%pkgname
Version:       1.0.4
Release:       alt0.1
Summary:       A Ruby library to handle HTTP cookies in a way both compliant with RFCs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sparklemotion/http-cookie
Vcs:           https://github.com/sparklemotion/http-cookie.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(domain_name)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
A Ruby library to handle HTTP cookies in a way both compliant with RFCs and
compatible with today's major browsers


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
* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt0.1
- > Ruby Policy 2.0
- ^ 1.0.3 -> 1.0.4pre
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
