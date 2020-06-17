%define        pkgname ruby-ldap

Name:          gem-%pkgname
Version:       0.9.20
Release:       alt4.2
Summary:       Ruby LDAP library
Group:         Development/Ruby
License:       BSD
Url:           https://github.com/bearded/ruby-ldap
Vcs:           https://github.com/bearded/ruby-ldap.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libldap-devel
BuildRequires: libssl-devel
BuildRequires: libsasl2-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname < %EVR
Provides:      %pkgname = %EVR

%description
Ruby/LDAP is an extension library for Ruby. It provides the interface
to some LDAP libraries (e.g. OpenLDAP, UMich LDAP, Netscape SDK,
ActiveDirectory). The common API for application development is
described in RFC1823 and is supported by Ruby/LDAP.


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
Summary:       Development environment for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libldap-devel
Requires:      libssl-devel
Requires:      libsasl2-devel

%description   devel
Development environment for %gemname gem.

%description   devel -l ru_RU.UTF8
Среда разработки для самоцвета %gemname.


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
%ruby_gemextdir
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Sun Apr 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.20-alt4.2
- + devel package
- ! spec tags and syntax

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.20-alt4.1
- Fix spec

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.20-alt4
- Use setup gem's dependency detection

* Tue Mar 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.20-alt3
- Added devel subpackage.

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.20-alt2
- Use Ruby Policy 2.0.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.20-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt1
- new version 0.9.17

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.9.11-alt2.3
- Rebuilt with ruby-2.0.0-alt1

* Fri Mar 14 2014 Led <led@altlinux.ru> 0.9.11-alt2.2
- ldif.rb: set encoding for fixing build with ruby >= 2.0

* Fri Nov 30 2012 Led <led@altlinux.ru> 0.9.11-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 0.9.11-alt2
- Repair build

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.11-alt1
- [0.9.11]

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 0.9.9-alt1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Wed Jul 08 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.9-alt1
- [0.9.9]
- Ruby 1.9 compatibility (closes: #20714)

* Wed May 13 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.8-alt1
- [0.9.8]

* Thu Aug 14 2008 Sir Raorn <raorn@altlinux.ru> 0.9.7-alt2
- Rebuilt with rpm-build-ruby

* Mon Dec 03 2007 Sir Raorn <raorn@altlinux.ru> 0.9.7-alt1
- [0.9.7] (closes: #9768)
- Fixed license (SourceForge says "BSD License")
- Added RI documentation
- Updated buildrequires
- Updated requires

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.2-alt1.1.1
- Rebuilt with libldap-2.3.so.0.

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.2-alt1.1
- Rebuilt with openldap-2.2.18-alt3.

* Tue Aug 17 2004 Serge A. Volkov <vserge@altlinux.ru> 0.8.2-alt1
- Update to new version 0.8.2

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.2-alt2.1
- Rebuilt with openssl-0.9.7d.

* Sun Jul 06 2003 Alexander Bokovoy <ab@altlinux.ru> 0.7.2-alt2
- Rebuild against Ruby 1.8.0-alt3

* Tue Nov 19 2002 Serge A. Volkov <vserge@altlinux.ru> 0.7.2-alt1
- Initial packaging for ALT Linux Team
