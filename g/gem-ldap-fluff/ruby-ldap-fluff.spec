%define        pkgname ldap-fluff
%define        gemname ldap_fluff

Name:          gem-%pkgname
Version:       0.4.7
Release:       alt2
Summary:       An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA & POSIX
License:       GPLv2+
Group:         Development/Ruby
Url:           https://github.com/theforeman/ldap_fluff
Vcs:           https://github.com/theforeman/ldap_fluff.git
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

Provides multiple implementations of LDAP queries for various backends.
Supports Active Directory, FreeIPA and posix-style LDAP.


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
* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.7-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- New version.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus
