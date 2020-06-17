%define        pkgname rmagick

Name:          gem-%pkgname
Version:       4.1.1
Release:       alt1
Summary:       ImageMagick for Ruby
Group:         Development/Ruby
License:       MIT
Url:           https://rmagick.github.io/
Vcs:           https://github.com/rmagick/rmagick.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libImageMagick-devel >= 6.6.9.6-alt1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
RMagick is an interface between the Ruby programming language and the
ImageMagick image processing library.


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
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Requires:      libImageMagick-devel >= 6.6.9.6-alt1

%description   devel
Development headers for %gemname gem.

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
%ruby_gemextdir
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 4.1.1-alt1
- ^ 4.0.0 -> 4.1.1
- ! spec tags

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- > Ruby Policy 2.0
- ^ 3.0.0 -> 4.0.0

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt2
- ! spec

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.16.0 -> 3.0.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt5.1
- Rebuild with new Ruby autorequirements.

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 2.16.0-alt5
- rebuilt for ImageMagick 

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt3.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt3.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt3.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt3.1
- Rebuild with Ruby 2.4.1

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 2.16.0-alt3
- Rebuilt for new ImageMagick.

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Sep 24 2016 Andrey Cherepanov <cas@altlinux.org> 2.16.0-alt1
- new version 2.16.0

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 2.13.1-alt3.2
- Rebuild with new libImageMagick

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.13.1-alt3.1
- Rebuilt with ruby-2.0.0-alt1

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 2.13.1-alt3
- Rebuild with new libImageMagick

* Tue Dec 04 2012 Led <led@altlinux.ru> 2.13.1-alt1.2
- Rebuild with ruby-1.9.3-alt1

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 2.13.1-alt1.1
- Rebuild with new libImageMagick

* Tue Apr 26 2011 Anton Farygin <rider@altlinux.ru> 2.13.1-alt1
- 2.13.1
- build with libImageMagick instead of libImageMagick-noHDRI

* Sat Aug 15 2009 Alexey I. Froloff <raorn@altlinux.org> 2.11.0-alt1
- [2.11.0]

* Wed Jul 08 2009 Alexey I. Froloff <raorn@altlinux.org> 2.10.0-alt1
- [2.10.0]

* Thu Aug 14 2008 Sir Raorn <raorn@altlinux.ru> 2.5.2-alt1
- [2.5.2]
- Packaged RI documentation, html docs are not generated

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.15.11-alt1
- 1.15.11.

* Tue Nov 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.15.10-alt1
- 1.15.10.
- Rebuild with newer ImageMagick.

* Fri Jul 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.15.7-alt1
- 1.15.7.
- Introduced myself as a Packager.

* Thu Mar 08 2007 Michael Shigorin <mike@altlinux.org> 1.15.4-alt1
- 1.15.4
- updated build/install to use makefile (current scheme)
- updated buildrequires
- disabled docs build, you can get them at homepage and fixing
  that quite resource-hungry part is not justified right now 
- NB: I am no longer using RMagick, proper maintainer is welcome

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 1.14.1-alt1
- 1.14.1
- minor spec cleanup

* Tue May 23 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.10.0-alt1.1
- Rebuild with libMagick++.so.10.0.2 .

* Tue Feb 21 2006 Michael Shigorin <mike@altlinux.org> 1.10.0-alt1
- 1.10.0

* Mon Feb 13 2006 Anton Farygin <rider@altlinux.ru> 1.9.2-alt1.1
- NMU: rebuild with new ImageMagick

* Fri Sep 16 2005 Michael Shigorin <mike@altlinux.org> 1.9.2-alt1
- 1.9.2

* Fri May 27 2005 Michael Shigorin <mike@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Wed Feb 23 2005 Michael Shigorin <mike@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.0-alt2.1
- Rebuilt with libtiff.so.4.

* Sun Jul 18 2004 Michael Shigorin <mike@altlinux.ru> 1.5.0-alt2
- built against IM 6.0.2
- adapted patch from 
  http://rubyforge.org/tracker/index.php?func=detail&aid=624&group_id=12&atid=133

* Fri Apr 23 2004 Michael Shigorin <mike@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Mar 10 2004 Michael Shigorin <mike@altlinux.ru> 1.4.0-alt1
- 1.4.0
- updated Url:, thanks to the author

* Wed Feb 04 2004 Michael Shigorin <mike@altlinux.ru> 1.3.2-alt1
- 1.3.2
- removed somewhat largish docs to subpackage

* Thu Sep 25 2003 Michael Shigorin <mike@altlinux.ru> 1.3.0-alt1
- built for ALT Linux
