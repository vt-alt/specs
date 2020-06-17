%define        pkgname ruby-openid

Name:          gem-%pkgname
Version:       2.9.2
Release:       alt1
Summary:       OpenID library for Ruby
License:       MIT/Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/openid/ruby-openid
Vcs:           https://github.com/openid/ruby-openid.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname
Provides:      %pkgname

%description
A Ruby library for verifying and serving OpenID identities.

* Easy to use API for verifying OpenID identites - OpenID::Consumer
* Support for serving OpenID identites - OpenID::Server
* Does not depend on underlying web framework
* Supports multiple storage mechanisms (Filesystem, ActiveRecord, Memory)
* Example code to help you get started, including:
  + Ruby on Rails based consumer and server
  + OpenIDLoginGenerator for quickly getting creating a rails app that uses
    OpenID for authentication
  + ActiveRecordOpenIDStore plugin
* Comprehensive test suite
* Supports both OpenID 1 and OpenID 2 transparently


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
%ruby_build --use=%gemname --version-replace=%version --alias=openid --ignore=rails_openid

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
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.9.2-alt1
- updated (^) 2.9.1 -> 2.9.2
- fixed (!) spec

* Wed Sep 18 2019 Pavel Skrylev <majioa@altlinux.org> 2.9.1-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.8.0 -> 2.9.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
