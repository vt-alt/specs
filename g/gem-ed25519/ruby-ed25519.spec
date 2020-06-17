%define        pkgname ed25519

Name:          gem-%pkgname
Version:       1.2.4
Release:       alt3
Summary:       Ruby library for the Ed25519 public-key signature system
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/crypto-rb/ed25519
Vcs:           https://github.com/crypto-rb/ed25519.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.


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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt3
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus
