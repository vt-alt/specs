%define        pkgname opengl

Name:          gem-%pkgname
Epoch:         1
Version:       0.10.0
Release:       alt1.3
Summary:       OpenGL Interface for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/larskanis/opengl
Vcs:           https://github.com/larskanis/opengl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libGL-devel
BuildRequires: libX11-devel
BuildRequires: libfreeglut-devel
BuildRequires: gem(hoe)
BuildRequires: gem(rake-compiler)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
ruby-opengl consists of Ruby extension modules that are bindings for
the OpenGL, GLU, and GLUT libraries. It is intended to be a replacement
for -- and uses the code from -- Yoshi's ruby-opengl.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      doc
Obsoletes:     doc

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development headers for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.0-alt1.3
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.0-alt1.2
- fixed (!) spec according to changelog rules

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.0-alt1.1
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.0-alt1
- Use Ruby Policy 2.0
- Bump to 0.10.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2
- Rebuild with new %%ruby_sitearchdir location

* Tue Sep 27 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt1
- New version from new homepage

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.60.1-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Sun Dec 09 2012 Led <led@altlinux.ru> 0.60.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.60.1-alt2
- Rebuild with Ruby 1.9.2

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.60.1-alt1
- [0.60.1]

* Thu Apr 03 2008 Sir Raorn <raorn@altlinux.ru> 0.60-alt1
- Rebuilt with rpm-build-ruby
- Based on unpublished build:
  * Mon Mar 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.60-alt1
  - 0.60
  - new upstream maintainer(see http://ruby-opengl.rubyforge.org/)
  - MIT licence

* Sat May 08 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32d-alt4
- New version
- Use default gcc for building

* Fri Feb 13 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt3
- BuildRequires fixed

* Thu Feb 05 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt2
- Use set_gcc_version to select gcc

* Sat Jan 10 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt1
- First Build for ALT project
