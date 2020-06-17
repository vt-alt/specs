%define        pkgname jwt

Name:          gem-%pkgname
Version:       2.2.1
Release:       alt1
Summary:       A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jwt/ruby-jwt
Vcs:           https://github.com/jwt/ruby-jwt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

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
* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- updated (^) 2.1.0 -> 2.2.1
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
