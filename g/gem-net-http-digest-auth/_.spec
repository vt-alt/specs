# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname net-http-digest-auth
%define        gemname net-http-digest_auth

Name:          gem-%pkgname
Version:       1.4.1
Release:       alt1
Summary:       An implementation of RFC 2617 Digest Access Authentication
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-digest_auth
%vcs           https://github.com/drbrain/net-http-digest_auth.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe)

%description
An implementation of RFC 2617 - Digest Access Authentication.  At this time
the gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.

In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own.  See the class documentation at Net::HTTP::DigestAuth
for an example.


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
* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
