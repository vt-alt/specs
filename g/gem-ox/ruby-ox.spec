%define        pkgname ox

Name:          gem-%pkgname
Version:       2.13.2
Release:       alt1
Summary:       Ruby Optimized XML Parser
License:       MIT
Group:         Development/Ruby
Url:           http://www.ohler.com/ox
Vcs:           https://github.com/ohler55/ox.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
A fast XML parser and object serializer that uses only standard C lib.
Optimized XML (Ox), as the name implies was written to provide speed
optimized XML handling. It was designed to be an alternative to Nokogiri
and other Ruby XML parsers for generic XML parsing and as an alternative
to Marshal for Object serialization.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.13.2-alt1
- updated (^) 2.11.0 -> 2.13.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.0-alt1.1
- fixed (!) spec according to changelog rules

* Tue Aug 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.0-alt1
- updated (^) 2.10.0 -> 2.11.0
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.10.0-alt2
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.3-alt1
- New version.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.2-alt1.1
- Rebuild for aarch64.

* Tue Apr 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.2-alt1
- New version.

* Sun Apr 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.1-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1.1
- Rebuild with Ruby 2.5.1

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1
- New version.

* Thu Nov 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.2-alt1
- New version

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- Initial build for ALT Linux
