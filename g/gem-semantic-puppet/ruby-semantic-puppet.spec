%define        pkgname semantic-puppet
%define        gemname semantic_puppet

Name:          gem-%pkgname
Version:       1.0.2
Release:       alt2.1
Summary:       Library of useful tools for working with Semantic Versions and module dependencies
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/semantic_puppet
Vcs:           https://github.com/puppetlabs/semantic_puppet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
%summary.


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
* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt2.1
- ! spec obsolete dep

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
