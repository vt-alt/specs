%define        pkgname rack

Name:          gem-%pkgname
Version:       2.2.2
Release:       alt1
Epoch:         1
Summary:       Modular Ruby webserver interface
Group:         Development/Ruby
License:       MIT
Url:           https://rack.github.io/
Vcs:           https://github.com/rack/rack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR


%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.

You may need to install appropriate %name-handler-XXX.


%package       doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %name


%package       -n rackup
Summary:       Rackup is an executable file for rack gem.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n rackup
Rackup is an executable file for rack gem.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%files         -n rackup
%_bindir/rackup

%changelog
* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1:2.2.2-alt1
- ^ 2.0.7 -> 2.2.2
- ! spec tags

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.7-alt1
- ^ 2.0.6 -> 2.0.7

* Thu Jan 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.6-alt1
- > Ruby Policy 2.0
- ^ 2.0.4 -> 2.0.6.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.0.4-alt1
- New version.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.4
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.3
- Use system way to install gemspec.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1
- Decrease version for pcs-pcsd
- Package gemspec
- Spec cleanup

* Tue May 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Sat Apr 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Sat Dec 01 2012 Led <led@altlinux.ru> 1.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.2.2-alt1
- [1.2.2]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.0-alt2
- Fix package broken by erthad

* Wed Mar 31 2010 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- [1.1.0]

* Mon Oct 19 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.1-alt1
- [1.0.1]

* Sun Oct 18 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt3
- Updated to 1.0-16-g99c47b8
- Force all form data to be UTF-8 String's

* Sun Aug 16 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt2
- Backported Ruby 1.9 encoding-related fixes.

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt1
- [1.0.0]
- Packaged rackup script
- Dropped unused handlers

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.4.0-alt1
- Built for Sisyphus
