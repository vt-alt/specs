%define        pkgname eventmachine

Name:          gem-%pkgname
Version:       1.2.7
Release:       alt3
Summary:       Fast, simple event-processing library for Ruby programs
Group:         Development/Ruby
License:       GPLv2 or Ruby
Url:           http://www.rubyeventmachine.com/
Vcs:           https://github.com/eventmachine/eventmachine.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++
BuildRequires: net-tools
BuildRequires: /proc
BuildRequires: libssl-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.


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

Requires:      gcc-c++
Requires:      net-tools
Requires:      /proc
Requires:      libssl-devel

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
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.7-alt3
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.7-alt2
- > Ruby Policy 2.0

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.2
- Rebuild with new Ruby autorequirements.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun May 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- New version.

* Tue May 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jul 31 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version

* Tue Mar 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0.1-alt3
- Rebuild with new %%ruby_sitearchdir location

* Sat Sep 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.0.1-alt2
- Rebuild with Ruby 2.3.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.0.1-alt1
- New version

* Mon Apr 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- New version
- Restore package in Sisyphus
- Disable all tests

* Wed Nov 17 2010 Timur Batyrshin <erthad@altlinux.org> 0.12.11-alt3
- rebuild with new openssl

* Thu Jul 01 2010 Timur Batyrshin <erthad@altlinux.org> 0.12.11-alt2
- fixed tests

* Mon Jun 28 2010 Timur Batyrshin <erthad@altlinux.org> 0.12.11-alt1
- Built for Sisyphus

