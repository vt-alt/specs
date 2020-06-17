%define        pkgname net-http-persistent

Name:          gem-%pkgname
Version:       4.0.0
Release:       alt0.1
Summary:       Thread-safe persistent connections with Net::HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-persistent
Vcs:           https://github.com/drbrain/net-http-persistent.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-hoe

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too!

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start over.

Net::HTTP supports persistent connections with some API methods but does not
handle reconnection gracefully. Net::HTTP::Persistent supports reconnection and
retry according to RFC 2616.


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
* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt0.1
- ^ 3.0.1 -> 4.0.0
- ! spec tags

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- > Ruby Policy 2.0
- ^ 3.0.0 -> 3.0.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
