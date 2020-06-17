%define        pkgname memcached

Name:          gem-%pkgname
Version:       2.0.0
Release:       alt1.1
Summary:       A Ruby interface to the libmemcached C client
License:       AFL-3.0
Group:         Development/Ruby
Url:           https://github.com/arthurnn/memcached
Vcs:           https://github.com/arthurnn/memcached.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         allow-use-system-libraries-arg.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libsasl2-devel
BuildRequires: libstdc++-devel
BuildRequires: libmemcached-devel
BuildRequires: gnu-config

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
An interface to the libmemcached C client.

Features

* clean API
* robust access to all memcached features
* SASL support for the binary protocol
* multiple hashing modes, including consistent hashing
* ludicrous speed, including optional pipelined IO with no_reply

The memcached library wraps the pure-C libmemcached client via SWIG.


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

Requires:      libsasl2-devel
Requires:      libstdc++-devel
Requires:      libmemcached-devel
Requires:      gnu-config

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.

%prep
%setup
%patch -p1

%build
%ruby_build --use=%gemname --version-replace=%version

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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- ! spec tags and syntax

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- > Ruby Policy 2.0
- ^ 1.8.0 -> 2.0.0alpha

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
