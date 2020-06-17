# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rest-client

Summary:       Simple REST client for Ruby
Name:          ruby-%pkgname
Version:       2.1.0
Release:       alt1
Group:         Development/Ruby
License:       MIT
Url:           http://github.com/archiloque/rest-client
%vcs           http://github.com/archiloque/rest-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.


%package       -n restclient
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n restclient
Executable file for %gemname gem.

%description   -n restclient -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%ruby_build --use=%gemname --alias=restclient

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n restclient
%_bindir/restclient

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- update (^) 2.0.2 -> 2.1.0
- update to (^) Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.6-alt1.2
- Rebuild with new Ruby autorequirements.

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.6.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- cleaned up BuildRequires

* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Initial build for Sisyphus

