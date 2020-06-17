%define        pkgname sshkey

Name:          gem-%pkgname
Version:       1.9.0
Release:       alt2
Summary:       SSH private and public key generator in pure Ruby (RSA & DSA)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bensie/sshkey
Vcs:           https://github.com/bensie/sshkey.git
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
* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus
